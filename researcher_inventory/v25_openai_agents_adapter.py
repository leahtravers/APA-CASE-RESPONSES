#!/usr/bin/env python3
"""V25 bounded adapter using conservative story-grain extraction.

The worker sees only its durable V25 contract, neutral task rules, the bounded
source/request, and one unscored provisional output from another stateless pass.
No archetype, evaluator finding, expected count, scored output, or sealed holdout
material is supplied.
"""
from __future__ import annotations

import json
import sys

from openai_agents_adapter import AGENT_ID_FILE, final_answer, request, wait


def _bounded_request(payload: dict) -> dict:
    keep = {
        "task", "rules", "class", "class_rule", "response_schema", "source",
        "units", "candidate", "researcher_interest", "created_by_ref", "correction",
    }
    return {k: v for k, v in payload.items() if k in keep}


def _attention_for(bounded: dict) -> str:
    if bounded.get("task") == "researcher_inventory_extract_one_class":
        return (
            "CONSERVATIVE INVENTORY PASS. Read the whole source. Work in source order. "
            "Create a row only when the source itself presents one separate coordinate whose job is the requested class at story grain. "
            "If words merely help say a larger proposition, do not make another row. If uncertain, do less. "
            "Do not use importance or salience. Do not substitute synonyms. "
            "Explicit source_wording and source_cue must be exact contiguous source text; only unnamed PLACE/TIME may use null source_wording. "
            "Resolve coreference, remove same-class duplicates, and remove grammatical/class-parallel debris before returning. "
            "Do not lose an unnamed PLACE or TIME merely because the source gives no place-name, date, or clock time."
        )
    if bounded.get("task") == "researcher_inventory_build_lightweight_compounds":
        return (
            "COMPOUND PASS. Units are already final. Build one lightweight compound for one source-presented proposition/relation at story grain. "
            "Use only retained units that actually participate. Do not invent units, arbitrary subsets, expanded duplicates, or attach every coordinate sharing the sentence."
        )
    return "Apply the installed V25 durable contract exactly to this bounded request."


def _session(agent_id: str, prompt: str, session_type: str):
    session = request(
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
    wait(session_id)
    raw = final_answer(session_id)
    if raw.startswith("```"):
        lines = raw.splitlines()
        if lines and lines[0].startswith("```"):
            lines = lines[1:]
        if lines and lines[-1].strip() == "```":
            lines = lines[:-1]
        raw = "\n".join(lines).strip()
    return json.loads(raw)


def main() -> int:
    payload = json.load(sys.stdin)
    agent_id = AGENT_ID_FILE.read_text(encoding="utf-8").strip()
    bounded = _bounded_request(payload)
    attention = _attention_for(bounded)

    initial_prompt = (
        "Execute only this bounded request under your installed durable V25 contract and supplied neutral apparatus rules. "
        "Return ONLY the JSON value required by response_schema. Do not infer or reconstruct any archetype, expected answer, expected count, evaluator preference, prior scored output, sealed holdout source, or holdout output.\n\n"
        "TASK ATTENTION:\n" + attention + "\n\n"
        "REQUEST JSON:\n" + json.dumps(bounded, ensure_ascii=False)
    )
    provisional = _session(agent_id, initial_prompt, "researcher_inventory_v25_initial")

    verify_prompt = (
        "Perform a separate stateless V25 verification. Re-read the complete source and independently rebuild the requested result before comparing it with the unscored provisional output. "
        "Use the contract's one admission test mechanically: the source itself must present one separate coordinate doing the requested class job at story grain. "
        "Remove proposition-internal grammatical pieces, class-parallel duplicates, unsupported inference, synonym substitution, and over-splitting. Under ambiguity, do less. "
        "Recover only genuine omissions, including unnamed PLACE/TIME coordinates established by actual source scenes/episodes. "
        "Then compare with the provisional output and return the complete replacement JSON. Ignore the provisional row count.\n\n"
        "TASK ATTENTION:\n" + attention + "\n\n"
        "REQUEST JSON:\n" + json.dumps(bounded, ensure_ascii=False) + "\n\n"
        "PROVISIONAL_UNSCORED_OUTPUT:\n" + json.dumps(provisional, ensure_ascii=False)
    )
    verified = _session(agent_id, verify_prompt, "researcher_inventory_v25_verification")
    sys.stdout.write(json.dumps(verified, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
