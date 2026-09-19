#!/usr/bin/env python3
"""V90 contract adapter with bounded same-session continuation on long-running agent turns.

Semantic authority remains the saved agent bootstrapped from AGENT_CONTRACT_V90. This file
changes only recovery behavior demonstrated by V89 run 35418642627-A1: a backend session
that is still in progress at the first wait boundary is polled/resumed under the same session
identity instead of immediately becoming a calibration failure or causing duplicate execution.
"""
from __future__ import annotations

import json
import os
import time
from pathlib import Path

import v60_openai_agents_adapter as prior

prior.base.CONTRACT_VERSION = os.environ.get("CONTRACT_VERSION", "RI-CONTRACT-V90").strip() or "RI-CONTRACT-V90"
recovery = prior.recovery
RECOVERY_DIR = Path("researcher_inventory/runtime/v90_session_recovery")
recovery.RECOVERY_DIR = RECOVERY_DIR
prior.base.recovery.RECOVERY_DIR = RECOVERY_DIR

TOTAL_WAIT_SECONDS = int(os.environ.get("RI_AGENT_SESSION_TOTAL_TIMEOUT_SECONDS", "1800"))


def _session_v90(agent_id: str, prompt: str, session_type: str, state_path: Path, trace_path: Path, phase: str):
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

    deadline = time.monotonic() + max(TOTAL_WAIT_SECONDS, recovery.SESSION_WAIT_SECONDS)

    while True:
        try:
            recovery.wait(session_id, timeout=recovery.SESSION_WAIT_SECONDS)
            break
        except RuntimeError as exc:
            if str(exc) == "session timeout":
                try:
                    current = recovery.request(f"/agents/sessions/{session_id}")
                    status = str(current.get("status") or "unknown")
                except Exception as status_exc:
                    prior._save_uncertain(
                        state_path, trace_path, state, phase, phase_state,
                        session_type, session_id, status_exc, "timeout_status_unknown",
                    )
                    raise recovery.SessionUncertain(
                        f"V90_SESSION_UNCERTAIN session_id={session_id} status=unknown"
                    ) from exc

                phase_state["status"] = status
                state[phase] = phase_state
                recovery._save_state(state_path, state)
                recovery._trace(trace_path, "timeout_status_checked", session_type, session_id, status)

                if status in ("idle", "completed"):
                    break
                if status in ("failed", "requires_action", "cancelled", "expired"):
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
                        f"V90_SESSION_UNCERTAIN session_id={session_id} status={status} continuation_window_exhausted"
                    ) from exc

                recovery._trace(
                    trace_path,
                    "same_session_still_running_continue",
                    session_type,
                    session_id,
                    status,
                    f"slice_seconds={recovery.SESSION_WAIT_SECONDS}",
                )
                continue

            if prior._is_transient_transport_error(exc):
                prior._save_uncertain(
                    state_path, trace_path, state, phase, phase_state,
                    session_type, session_id, exc, "transient_wait_uncertain",
                )
                raise recovery.SessionUncertain(
                    f"V90_SESSION_UNCERTAIN session_id={session_id} status=unknown transient_transport"
                ) from exc

            recovery._trace(trace_path, "session_terminal_error", session_type, session_id, detail=str(exc))
            raise

    try:
        raw = recovery.final_answer(session_id)
    except Exception as exc:
        if prior._is_transient_transport_error(exc):
            state = recovery._load_state(state_path)
            phase_state = state.get(phase) if isinstance(state.get(phase), dict) else {"session_id": session_id}
            prior._save_uncertain(
                state_path, trace_path, state, phase, phase_state,
                session_type, session_id, exc, "transient_result_read_uncertain",
            )
            raise recovery.SessionUncertain(
                f"V90_SESSION_UNCERTAIN session_id={session_id} status=unknown transient_result_read"
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


prior.base.recovery._session = _session_v90

if __name__ == "__main__":
    raise SystemExit(prior.base.main())
