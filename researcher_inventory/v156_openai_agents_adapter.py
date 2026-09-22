#!/usr/bin/env python3
"""V156 adapter: V156 semantics plus semantically-neutral result retrieval repair.

The semantic worker receives only the installed durable V156 contract and bounded
source request. This adapter does not expose archetypes, evaluator findings, expected
counts, prior scored outputs, or holdout material.
"""
from __future__ import annotations

import os
import time
import urllib.parse
from pathlib import Path

import v155_openai_agents_adapter as v155

CONTRACT_VERSION = os.environ.get("CONTRACT_VERSION", "RI-CONTRACT-V156").strip() or "RI-CONTRACT-V156"
V156_RECOVERY_DIR = Path("researcher_inventory/runtime/v156_session_recovery")
RESULT_WAIT_SECONDS = int(os.environ.get("RI_AGENT_RESULT_WAIT_SECONDS", "120"))
RESULT_POLL_SECONDS = float(os.environ.get("RI_AGENT_RESULT_POLL_SECONDS", "2"))

base = v155.base
base.CONTRACT_VERSION = CONTRACT_VERSION

# Move all inherited recovery custody onto a new V156 lineage directory without
# changing the established V92 same-session recovery topology.
v155.v126.V126_RECOVERY_DIR = V156_RECOVERY_DIR
v155.v126.v125.V125_RECOVERY_DIR = V156_RECOVERY_DIR
v155.v126.v125.v124.v123.v122.v121.v120.v119.v118.v117.v116.v115.v114.v113.v112.v111.v110.v109.v108.v107.v100.v99.v98.v97.v96.v95.v94.v93.v92.RECOVERY_DIR = V156_RECOVERY_DIR
v155.v126.v125.v124.v123.v122.v121.v120.v119.v118.v117.v116.v115.v114.v113.v112.v111.v110.v109.v108.v107.v100.v99.v98.v97.v96.v95.v94.v93.v92.recovery.RECOVERY_DIR = V156_RECOVERY_DIR
base.recovery.RECOVERY_DIR = V156_RECOVERY_DIR

recovery = base.recovery


def _collect_final_answers(session_id: str) -> list[str]:
    """Read all session-item pages and collect completed final-answer text."""
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
            if not isinstance(item, dict):
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


def _paged_final_answer(session_id: str) -> str:
    """Reconcile final-answer visibility on the same completed session.

    The Agents session can report idle/completed before a final-answer item is visible
    to the first item-list read. Treat that as result-read uncertainty, not permission
    to mint a replacement semantic execution. Also traverse all item pages so a final
    answer beyond the first 100 items cannot be missed.
    """
    deadline = time.monotonic() + RESULT_WAIT_SECONDS

    while True:
        answers = _collect_final_answers(session_id)
        if answers:
            return "\n".join(answers).strip()

        state = recovery.request(f"/agents/sessions/{session_id}") or {}
        status = str(state.get("status") or "unknown") if isinstance(state, dict) else "unknown"
        if status in {"failed", "requires_action", "cancelled", "canceled", "expired"}:
            raise RuntimeError(f"session terminal status {status}")

        if time.monotonic() >= deadline:
            # `timed out` is intentionally transport/recovery-class language used by
            # the inherited V92 layer. That layer reconciles and preserves this same
            # session instead of allowing the outer apparatus retry to create another.
            raise RuntimeError(
                f"timed out waiting for final answer visibility session_id={session_id} status={status}"
            )
        time.sleep(RESULT_POLL_SECONDS)


# v92's `_session_v92` reads `recovery.final_answer` dynamically from this shared
# module object, so patching the module preserves the existing session topology while
# changing only result retrieval.
recovery.final_answer = _paged_final_answer

if __name__ == "__main__":
    raise SystemExit(base.main())
