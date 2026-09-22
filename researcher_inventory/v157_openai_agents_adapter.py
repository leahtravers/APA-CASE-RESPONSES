#!/usr/bin/env python3
"""V157 harness successor: turn-aware result reconciliation for V156 semantics.

The semantic worker still receives only the installed durable V156 contract and bounded
source request. This adapter changes managed-session result reconciliation only. It does
not expose archetypes, evaluator findings, expected counts, prior scored outputs, or
holdout material.
"""
from __future__ import annotations

import os
import time
import urllib.parse
from pathlib import Path

import v156_openai_agents_adapter as v156

CONTRACT_VERSION = os.environ.get("CONTRACT_VERSION", "RI-CONTRACT-V156").strip() or "RI-CONTRACT-V156"
V157_RECOVERY_DIR = Path("researcher_inventory/runtime/v157_session_recovery")
RESULT_WAIT_SECONDS = int(os.environ.get("RI_AGENT_RESULT_WAIT_SECONDS", "120"))
RESULT_POLL_SECONDS = float(os.environ.get("RI_AGENT_RESULT_POLL_SECONDS", "2"))

base = v156.base
base.CONTRACT_VERSION = CONTRACT_VERSION

# Move the inherited recovery lineage onto a new V157 harness directory while retaining
# the V92 same-session recovery behavior and the unchanged V156 semantic contract.
v156.v155.v126.V126_RECOVERY_DIR = V157_RECOVERY_DIR
v156.v155.v126.v125.V125_RECOVERY_DIR = V157_RECOVERY_DIR
v156.v155.v126.v125.v124.v123.v122.v121.v120.v119.v118.v117.v116.v115.v114.v113.v112.v111.v110.v109.v108.v107.v100.v99.v98.v97.v96.v95.v94.v93.v92.RECOVERY_DIR = V157_RECOVERY_DIR
v156.v155.v126.v125.v124.v123.v122.v121.v120.v119.v118.v117.v116.v115.v114.v113.v112.v111.v110.v109.v108.v107.v100.v99.v98.v97.v96.v95.v94.v93.v92.recovery.RECOVERY_DIR = V157_RECOVERY_DIR
base.recovery.RECOVERY_DIR = V157_RECOVERY_DIR

recovery = base.recovery

# Within one adapter process, once a root turn is observed for a session, never silently
# switch to a different turn. A fresh process may reconstruct this binding from the
# session's latest root turn; the harness itself never creates another turn on recovery.
_BOUND_ROOT_TURNS: dict[str, str] = {}


def _latest_root_turn(session_id: str) -> dict | None:
    query = urllib.parse.urlencode({"order": "desc", "limit": 100})
    page = recovery.request(f"/agents/sessions/{session_id}/turns?{query}") or {}
    data = page.get("data", []) if isinstance(page, dict) else []
    if not isinstance(data, list):
        return None
    for turn in data:
        if not isinstance(turn, dict):
            continue
        # Root turns have no subagent identity. Session-turn listing is root-scoped in
        # the public API, but keep this guard so future mixed histories fail safely.
        if turn.get("subagent_id") in (None, ""):
            return turn
    return None


def _bound_root_turn(session_id: str) -> dict | None:
    bound_id = _BOUND_ROOT_TURNS.get(session_id)
    if bound_id:
        quoted = urllib.parse.quote(bound_id, safe="")
        turn = recovery.request(f"/agents/sessions/{session_id}/turns/{quoted}") or {}
        if not isinstance(turn, dict):
            return None
        return turn

    turn = _latest_root_turn(session_id)
    if turn is None:
        return None
    turn_id = str(turn.get("id") or "")
    if not turn_id:
        raise RuntimeError("root turn missing id")
    _BOUND_ROOT_TURNS[session_id] = turn_id
    return turn


def _collect_turn_final_answers(session_id: str, turn_id: str) -> list[str]:
    """Read all root-session item pages and collect final answers for one exact turn."""
    answers: list[str] = []
    after: str | None = None
    seen_cursors: set[str] = set()

    while True:
        params: dict[str, str | int] = {"order": "asc", "limit": 100}
        if after:
            params["after"] = after
        query = urllib.parse.urlencode(params)
        page = recovery.request(f"/agents/sessions/{session_id}/items?{query}") or {}
        data = page.get("data", []) if isinstance(page, dict) else []
        if not isinstance(data, list):
            data = []

        for item in data:
            if not isinstance(item, dict) or str(item.get("turn_id") or "") != turn_id:
                continue
            if item.get("type") != "message" or item.get("role") != "assistant":
                continue
            if item.get("status") != "completed" or item.get("phase") != "final_answer":
                continue
            content = item.get("content", [])
            if not isinstance(content, list):
                continue
            for part in content:
                if isinstance(part, dict) and part.get("type") == "output_text":
                    text = str(part.get("text", ""))
                    if text:
                        answers.append(text)

        if not isinstance(page, dict) or not page.get("has_more"):
            break

        cursor = page.get("last_id")
        if not cursor and data:
            last = data[-1]
            if isinstance(last, dict):
                cursor = last.get("id")
        cursor = str(cursor or "")
        if not cursor or cursor in seen_cursors:
            raise RuntimeError("session item pagination stalled")
        seen_cursors.add(cursor)
        after = cursor

    return answers


def _safe_turn_error(turn: dict) -> str:
    error = turn.get("error")
    if not isinstance(error, dict):
        return ""
    code = str(error.get("code") or "")[:120]
    message = str(error.get("message") or "")[:500]
    if code and message:
        return f" code={code} message={message}"
    if code:
        return f" code={code}"
    if message:
        return f" message={message}"
    return ""


def _turn_aware_final_answer(session_id: str) -> str:
    """Reconcile the exact root turn before treating a session as successful.

    Session `idle` only means the session can receive more input. It does not prove the
    latest root turn completed. This function binds to that root turn, polls its own
    lifecycle, and accepts only final-answer items belonging to that exact turn.
    """
    deadline = time.monotonic() + RESULT_WAIT_SECONDS

    while True:
        turn = _bound_root_turn(session_id)
        if turn is None:
            if time.monotonic() >= deadline:
                raise RuntimeError(
                    f"timed out waiting for root turn visibility session_id={session_id}"
                )
            time.sleep(RESULT_POLL_SECONDS)
            continue

        turn_id = str(turn.get("id") or "")
        bound_id = _BOUND_ROOT_TURNS.get(session_id)
        if not turn_id or (bound_id and turn_id != bound_id):
            raise RuntimeError(
                f"root turn identity changed unexpectedly session_id={session_id} "
                f"bound_turn_id={bound_id} observed_turn_id={turn_id or 'missing'}"
            )

        status = str(turn.get("status") or "unknown")
        if status == "failed":
            raise RuntimeError(
                f"turn terminal status failed session_id={session_id} turn_id={turn_id}"
                f"{_safe_turn_error(turn)}"
            )
        if status in {"cancelled", "canceled"}:
            raise RuntimeError(
                f"turn terminal status {status} session_id={session_id} turn_id={turn_id}"
            )

        if status == "completed":
            answers = _collect_turn_final_answers(session_id, turn_id)
            if answers:
                return "\n".join(answers).strip()
            if time.monotonic() >= deadline:
                raise RuntimeError(
                    f"timed out waiting for completed-turn final answer visibility "
                    f"session_id={session_id} turn_id={turn_id}"
                )
            time.sleep(RESULT_POLL_SECONDS)
            continue

        if time.monotonic() >= deadline:
            raise RuntimeError(
                f"timed out waiting for root turn completion session_id={session_id} "
                f"turn_id={turn_id} status={status}"
            )
        time.sleep(RESULT_POLL_SECONDS)


# V92 reads `recovery.final_answer` dynamically from this shared module object. Patch
# only result reconciliation; session creation, prompt construction, semantic contract,
# same-session retry topology, and evaluator behavior remain unchanged.
recovery.final_answer = _turn_aware_final_answer

if __name__ == "__main__":
    raise SystemExit(base.main())
