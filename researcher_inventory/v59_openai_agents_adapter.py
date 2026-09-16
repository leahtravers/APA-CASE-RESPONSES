#!/usr/bin/env python3
"""V59 contract-version-correct isolated agent adapter with additive transient-session recovery.

Reuses the V55 semantic-isolation adapter. The only harness change is uncertain-state preservation for transient API/status/result-read failures so an existing saved-agent session is recovered rather than silently replaced. Gold/evaluator/holdout material is never sent to the worker.
"""
from __future__ import annotations

import json
import os
from pathlib import Path

import v55_openai_agents_adapter as base
import v32_openai_agents_adapter as recovery

base.CONTRACT_VERSION = os.environ.get("CONTRACT_VERSION", "RI-CONTRACT-V59").strip() or "RI-CONTRACT-V59"
RECOVERY_DIR = Path("researcher_inventory/runtime/v59_session_recovery")
recovery.RECOVERY_DIR = RECOVERY_DIR
base.recovery.RECOVERY_DIR = RECOVERY_DIR


def _is_transient_transport_error(exc: Exception) -> bool:
    text = str(exc).lower()
    markers = (
        "http 500",
        "http 502",
        "http 503",
        "http 504",
        "internal error",
        "bad gateway",
        "service unavailable",
        "gateway timeout",
        "temporar",
        "connection reset",
        "connection refused",
        "remote end closed",
        "timed out",
    )
    return any(marker in text for marker in markers)


def _save_uncertain(state_path: Path, trace_path: Path, state: dict, phase: str, phase_state: dict, session_type: str, session_id: str, exc: Exception, event: str) -> None:
    phase_state["status"] = "unknown"
    phase_state["last_error"] = str(exc)
    state[phase] = phase_state
    recovery._save_state(state_path, state)
    recovery._trace(trace_path, event, session_type, session_id, "unknown", str(exc))


def _session_v59(agent_id: str, prompt: str, session_type: str, state_path: Path, trace_path: Path, phase: str):
    state = recovery._load_state(state_path)
    phase_state = state.get(phase) if isinstance(state.get(phase), dict) else {}

    if "result" in phase_state:
        recovery._trace(trace_path, "recovered_completed_result", session_type, phase_state.get("session_id"), "completed")
        return phase_state["result"]

    session_id = phase_state.get("session_id")
    if session_id:
        recovery._trace(trace_path, "resume_existing_session", session_type, session_id, phase_state.get("status"))
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

    try:
        recovery.wait(session_id, timeout=recovery.SESSION_WAIT_SECONDS)
    except RuntimeError as exc:
        if str(exc) == "session timeout":
            try:
                current = recovery.request(f"/agents/sessions/{session_id}")
                status = str(current.get("status") or "unknown")
            except Exception as status_exc:
                _save_uncertain(
                    state_path, trace_path, state, phase, phase_state,
                    session_type, session_id, status_exc, "timeout_status_unknown",
                )
                raise recovery.SessionUncertain(
                    f"V59_SESSION_UNCERTAIN session_id={session_id} status=unknown"
                ) from exc

            phase_state["status"] = status
            state[phase] = phase_state
            recovery._save_state(state_path, state)
            recovery._trace(trace_path, "timeout_status_checked", session_type, session_id, status)

            if status == "idle":
                pass
            elif status in ("failed", "requires_action"):
                raise RuntimeError(f"session terminal status {status}") from exc
            else:
                raise recovery.SessionUncertain(
                    f"V59_SESSION_UNCERTAIN session_id={session_id} status={status}"
                ) from exc
        elif _is_transient_transport_error(exc):
            _save_uncertain(
                state_path, trace_path, state, phase, phase_state,
                session_type, session_id, exc, "transient_wait_uncertain",
            )
            raise recovery.SessionUncertain(
                f"V59_SESSION_UNCERTAIN session_id={session_id} status=unknown transient_transport"
            ) from exc
        else:
            recovery._trace(trace_path, "session_terminal_error", session_type, session_id, detail=str(exc))
            raise

    try:
        raw = recovery.final_answer(session_id)
    except Exception as exc:
        if _is_transient_transport_error(exc):
            state = recovery._load_state(state_path)
            phase_state = state.get(phase) if isinstance(state.get(phase), dict) else {"session_id": session_id}
            _save_uncertain(
                state_path, trace_path, state, phase, phase_state,
                session_type, session_id, exc, "transient_result_read_uncertain",
            )
            raise recovery.SessionUncertain(
                f"V59_SESSION_UNCERTAIN session_id={session_id} status=unknown transient_result_read"
            ) from exc
        raise

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


base.recovery._session = _session_v59

if __name__ == "__main__":
    raise SystemExit(base.main())
