#!/usr/bin/env python3
"""V26 bounded adapter using coverage-first then prune-and-repair verification.

The worker sees only its durable V26 contract, neutral task rules, the bounded
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
            "COVERAGE-FIRST CLASS-LOCAL PASS. Read the whole source. Lightweight is structural resolution, not sparsity or salience. "
            "Scan beginning to end and retain every source-supported researcher-selectable coordinate that independently performs the requested class job at story grain. "
            "Then prune unsupported inference, synonym/normalization, proposition-internal grammatical debris without its own class job, over-split fragments, and same-class duplicates after coreference resolution. "
            "Do not delete merely because wording also supports another class; retain cross-class overlap only when this requested class job is independently present. "
            "Do not delete a source-supported coordinate merely because its posture is uncertain, questioned, negated, hypothetical, reported, intended, recurring, comparative, or prospective. Preserve that posture. "
            "Explicit source_wording and source_cue must be exact contiguous source text; only unnamed PLACE/TIME may use null source_wording. "
            "Finish with both an omission scan and an over-splitting scan. Do not target an expected count."
        )
    if bounded.get("task") == "researcher_inventory_build_lightweight_compounds":
        return (
            "COMPOUND PASS. Units are already final. Re-read the source and build one lightweight compound for each source-presented proposition/relation/characterization/question/report/reflection/intention at the apparatus grain. "
            "Use all and only retained units that actually participate. Do not invent units, arbitrary subsets, expanded duplicates, or sentence-wide bundles merely because coordinates share a sentence."
        )
    return "Apply the installed V26 durable contract exactly to this bounded request."


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
        "Execute only this bounded request under your installed durable V26 contract and supplied neutral apparatus rules. "
        "Return ONLY the JSON value required by response_schema. Do not infer or reconstruct any archetype, expected answer, expected count, evaluator preference, prior scored output, sealed holdout source, or holdout output.\n\n"
        "TASK ATTENTION:\n" + attention + "\n\n"
        "REQUEST JSON:\n" + json.dumps(bounded, ensure_ascii=False)
    )
    provisional = _session(agent_id, initial_prompt, "researcher_inventory_v26_coverage")

    verify_prompt = (
        "Perform a separate stateless V26 adjudication. Re-read the complete source and independently rebuild the requested result before comparing it with the unscored provisional output. "
        "Apply three checks in order: (1) COVERAGE — what source-supported coordinates independently do this requested class job at story grain? (2) PRUNING — which candidates are unsupported inference, grammatical debris, over-split fragments, or same-class duplicates? (3) REPAIR — what genuine source-supported coordinates are missing from the provisional result? "
        "Lightweight is structural resolution, not sparse selection. Another class is not a deletion reason; retain overlap only when this class job is independently present. "
        "Uncertainty/question/negation/hypothetical/report/intention/recurrence/prospect preserves posture and is not by itself a deletion reason. "
        "Use exact contiguous source spans and never target a row count. Return the complete replacement JSON, not a critique.\n\n"
        "TASK ATTENTION:\n" + attention + "\n\n"
        "REQUEST JSON:\n" + json.dumps(bounded, ensure_ascii=False) + "\n\n"
        "PROVISIONAL_UNSCORED_OUTPUT:\n" + json.dumps(provisional, ensure_ascii=False)
    )
    verified = _session(agent_id, verify_prompt, "researcher_inventory_v26_adjudication")
    sys.stdout.write(json.dumps(verified, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
