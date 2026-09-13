#!/usr/bin/env python3
"""V11 adapter: keep the durable agent contract authoritative.

The apparatus may carry legacy per-request helper prose for provider-neutral
adapters. V11 calibration must not let that transport prose override or conflict
with the durable contract installed on the saved agent. This adapter therefore
passes only bounded task data/schema plus mechanical retry corrections.
No archetype, expected output, evaluator finding, or holdout material is added.
"""
from __future__ import annotations

import json
import sys

# This file is executed by path from the repository root. In that mode Python puts
# researcher_inventory/ itself on sys.path, so import the sibling module directly.
from openai_agents_adapter import AGENT_ID_FILE, final_answer, request, wait


def _bounded_request(payload: dict) -> dict:
    """Strip behavioral helper prose; preserve task data and mechanical feedback."""
    keep = {
        "task",
        "class",
        "response_schema",
        "source",
        "units",
        "candidate",
        "researcher_interest",
        "created_by_ref",
        "correction",
    }
    return {k: v for k, v in payload.items() if k in keep}


def main() -> int:
    payload = json.load(sys.stdin)
    agent_id = AGENT_ID_FILE.read_text(encoding="utf-8").strip()
    bounded = _bounded_request(payload)
    prompt = (
        "Execute only this bounded request under your installed durable contract. "
        "The durable contract is the sole behavioral authority. "
        "Return ONLY the JSON value required by response_schema. "
        "Do not infer any expected answer, expected count, archetype, or evaluator preference.\n\n"
        "REQUEST JSON:\n" + json.dumps(bounded, ensure_ascii=False)
    )
    session = request(
        "/agents/sessions",
        method="POST",
        body={
            "agent_id": agent_id,
            "environment": {"type": "none"},
            "input": prompt,
            "metadata": {"apa_session_type": "researcher_inventory_semantic_subroutine_v11"},
        },
    )
    session_id = session["id"]
    wait(session_id)
    raw = final_answer(session_id)
    if raw.startswith("```"):
        lines = raw.splitlines()
        if lines and lines[0].startswith("```"):
            lines = lines[1:]
        if lines and lines[-1].strip() == "```":
            lines = lines[:-1]
        raw = "\n".join(lines).strip()
    value = json.loads(raw)
    sys.stdout.write(json.dumps(value, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
