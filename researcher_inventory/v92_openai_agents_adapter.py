#!/usr/bin/env python3
"""V92 contract adapter with bounded same-session transient transport recovery.

Semantic authority remains the saved agent bootstrapped from AGENT_CONTRACT_V92.
This file changes runtime recovery only. It preserves a created session ID across
timeouts, connection resets, and transient result-read failures and never creates
a replacement session merely because transport is uncertain.
"""
from __future__ import annotations

import json
import os
import time
from pathlib import Path

import v90_openai_agents_adapter as v90

v90.prior.base.CONTRACT_VERSION = os.environ.get("CONTRACT_VERSION", "RI-CONTRACT-V92").strip() or "RI-CONTRACT-V92"
recovery = v90.recovery
RECOVERY_DIR = Path("researcher_inventory/runtime/v92_session_recovery")
recovery.RECOVERY_DIR = RECOVERY_DIR
v90.prior.base.recovery.RECOVERY_DIR = RECOVERY_DIR

TOTAL_WAIT_SECONDS = int(os.environ.get("RI_AGENT_SESSION_TOTAL_TIMEOUT_SECONDS", "1800"))
TRANSIENT_BACKOFF_SECONDS = float(os.environ.get("RI_AGENT_TRANSIENT_BACKOFF_SECONDS", "5"))

_TERMINAL_FAILURE = {"failed", "requires_action", "cancelled", "expired"}
_TERMINAL_SUCCESS = {"idle", "completed"}


def _persist_status(state_path: Path, state: dict, phase: str, phase_state: dict, status: str) -> None:
    phase_state["status"] = status
    state[phase] = phase_state
    recovery._save_state(state_path, state)


def _remote_status(session_id: str) -> str:
    current = recovery.request(f"/agents/sessions/{session_id}")
    return str(current.get("status") or "unknown")


def _bounded_uncertain(
    state_path: Path,
    trace_path: Path,
    state: dict,
    phase: str,
    phase_state: dict,
    session_type: str,
    session_id: str,
    exc: Exception,
    event: str,
    reason: str,
):
    v90.prior._save_uncertain(
        state_path,
        trace_path,
        state,
        phase,
        phase_state,
        session_type,
        session_id,
        exc,
        event,
    )
    raise recovery.SessionUncertain(
        f"V92_SESSION_UNCERTAIN session_id={session_id} status=unknown {reason}"
    ) from exc


def _reconcile_after_transient(
    *,
    state_path: Path,
    trace_path: Path,
    state: dict,
    phase: str,
    phase_state: dict,
    session_type: str,
    session_id: str,
    deadline: float,
    original_exc: Exception,
    event_prefix: str,
) -> str | None:
    """Return known status, or None when a bounded transient retry should continue."""
    recovery._trace(
        trace_path,
        f"{event_prefix}_transport_error",
        session_type,
        session_id,
        phase_state.get("status"),
        str(original_exc),
    )

    try:
        status = _remote_status(session_id)
    except Exception as status_exc:
        if v90.prior._is_transient_transport_error(status_exc) and time.monotonic() < deadline:
            phase_state["last_error"] = str(status_exc)
            state[phase] = phase_state
            recovery._save_state(state_path, state)
            recovery._trace(
                trace_path,
                f"{event_prefix}_status_transport_retry",
                session_type,
                session_id,
                "unknown",
                str(status_exc),
            )
            time.sleep(TRANSIENT_BACKOFF_SECONDS)
            return None
        _bounded_uncertain(
            state_path,
            trace_path,
            state,
            phase,
            phase_state,
            session_type,
            session_id,
            status_exc,
            f"{event_prefix}_status_unresolved",
            f"{event_prefix}_status_unresolved",
        )

    _persist_status(state_path, state, phase, phase_state, status)
    recovery._trace(
        trace_path,
        f"{event_prefix}_status_reconciled",
        session_type,
        session_id,
        status,
    )
    return status


def _session_v92(agent_id: str, prompt: str, session_type: str, state_path: Path, trace_path: Path, phase: str):
    state = recovery._load_state(state_path)
    phase_state = state.get(phase) if isinstance(state.get(phase), dict) else {}

    if "result" in phase_state:
        recovery._trace(
            trace_path,
            "recovered_completed_result",
            session_type,
            phase_state.get("session_id"),
            "completed",
        )
        return phase_state["result"]

    session_id = phase_state.get("session_id")
    if session_id:
        recovery._trace(
            trace_path,
            "resume_existing_session",
            session_type,
            session_id,
            phase_state.get("status"),
        )
    else:
        session = recovery.request(
            "/agents/sessions",
            method="POST",
            body={
                "agent_id": agent_id,
                "environment": {"type": "none"},
                "input": prompt,
                "metadata": {"apa_session_type": session_type},
            },
        )
        session_id = session["id"]
        phase_state = {"session_id": session_id, "status": session.get("status") or "created"}
        state[phase] = phase_state
        recovery._save_state(state_path, state)
        recovery._trace(trace_path, "session_created", session_type, session_id, phase_state["status"])

    deadline = time.monotonic() + max(TOTAL_WAIT_SECONDS, recovery.SESSION_WAIT_SECONDS)

    # Wait/reconcile loop. All transient transport exception classes are handled here,
    # not only RuntimeError, so URLError/connection-reset paths keep the same session.
    while True:
        try:
            recovery.wait(session_id, timeout=recovery.SESSION_WAIT_SECONDS)
            break
        except Exception as exc:
            is_timeout = isinstance(exc, RuntimeError) and str(exc) == "session timeout"
            is_transient = v90.prior._is_transient_transport_error(exc)

            if not is_timeout and not is_transient:
                recovery._trace(trace_path, "session_terminal_error", session_type, session_id, detail=str(exc))
                raise

            prefix = "timeout" if is_timeout else "transient_wait"
            status = _reconcile_after_transient(
                state_path=state_path,
                trace_path=trace_path,
                state=state,
                phase=phase,
                phase_state=phase_state,
                session_type=session_type,
                session_id=session_id,
                deadline=deadline,
                original_exc=exc,
                event_prefix=prefix,
            )

            if status is None:
                if time.monotonic() >= deadline:
                    _bounded_uncertain(
                        state_path,
                        trace_path,
                        state,
                        phase,
                        phase_state,
                        session_type,
                        session_id,
                        exc,
                        f"{prefix}_window_exhausted",
                        "continuation_window_exhausted",
                    )
                continue

            if status in _TERMINAL_SUCCESS:
                break
            if status in _TERMINAL_FAILURE:
                raise RuntimeError(f"session terminal status {status}") from exc

            if time.monotonic() >= deadline:
                phase_state["last_error"] = "same-session continuation window exhausted"
                state[phase] = phase_state
                recovery._save_state(state_path, state)
                recovery._trace(
                    trace_path,
                    "same_session_continuation_window_exhausted",
                    session_type,
                    session_id,
                    status,
                    f"total_wait_seconds={TOTAL_WAIT_SECONDS}",
                )
                raise recovery.SessionUncertain(
                    f"V92_SESSION_UNCERTAIN session_id={session_id} status={status} continuation_window_exhausted"
                ) from exc

            recovery._trace(
                trace_path,
                "same_session_still_running_continue",
                session_type,
                session_id,
                status,
                f"slice_seconds={recovery.SESSION_WAIT_SECONDS}",
            )
            time.sleep(TRANSIENT_BACKOFF_SECONDS)

    # Result retrieval also remains on the same completed session. A transient read
    # failure is retried within the same bounded window instead of creating a new run.
    while True:
        try:
            raw = recovery.final_answer(session_id)
            break
        except Exception as exc:
            if not v90.prior._is_transient_transport_error(exc):
                raise

            status = _reconcile_after_transient(
                state_path=state_path,
                trace_path=trace_path,
                state=state,
                phase=phase,
                phase_state=phase_state,
                session_type=session_type,
                session_id=session_id,
                deadline=deadline,
                original_exc=exc,
                event_prefix="transient_result_read",
            )

            if status in _TERMINAL_FAILURE:
                raise RuntimeError(f"session terminal status {status}") from exc

            if time.monotonic() >= deadline:
                _bounded_uncertain(
                    state_path,
                    trace_path,
                    state,
                    phase,
                    phase_state,
                    session_type,
                    session_id,
                    exc,
                    "transient_result_read_window_exhausted",
                    "transient_result_read_window_exhausted",
                )

            time.sleep(TRANSIENT_BACKOFF_SECONDS)

    if raw.startswith("```"):
        lines = raw.splitlines()
        if lines and lines[0].startswith("```"):
            lines = lines[1:]
        if lines and lines[-1].strip() == "```":
            lines = lines[:-1]
        raw = "\n".join(lines).strip()

    result = json.loads(raw)
    state = recovery._load_state(state_path)
    phase_state = state.get(phase) if isinstance(state.get(phase), dict) else {"session_id": session_id}
    phase_state["status"] = "completed"
    phase_state["result"] = result
    state[phase] = phase_state
    recovery._save_state(state_path, state)
    recovery._trace(trace_path, "session_completed", session_type, session_id, "completed")
    return result


v90.prior.base.recovery._session = _session_v92

if __name__ == "__main__":
    raise SystemExit(v90.prior.base.main())
