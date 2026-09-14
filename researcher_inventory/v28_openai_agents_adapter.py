#!/usr/bin/env python3
"""V28 bounded adapter: atomic function-bearing units, then story bindings.

The worker sees only its durable V28 contract, neutral task rules, the bounded
source/request, and one unscored provisional output from another stateless pass.
No archetype, evaluator finding, expected count, scored output, or sealed holdout
material is supplied.
"""
from __future__ import annotations

import json
import os
import sys

from openai_agents_adapter import AGENT_ID_FILE, final_answer, request, wait

SESSION_WAIT_SECONDS = int(os.environ.get("RI_AGENT_SESSION_TIMEOUT_SECONDS", "600"))


def _bounded_request(payload: dict) -> dict:
    keep = {
        "task", "rules", "class", "class_rule", "response_schema", "source",
        "units", "candidate", "researcher_interest", "created_by_ref", "correction",
    }
    return {k: v for k, v in payload.items() if k in keep}


def _attention_for(bounded: dict) -> str:
    if bounded.get("task") == "researcher_inventory_extract_one_class":
        return (
            "UNIT-LAYER PASS. Read the whole source before deciding rows. Units are selectable source coordinates, NOT complete propositions and NOT grammar tokens. "
            "Preserve the smallest complete function-bearing span for THIS class. A candidate may be a valid unit even when it must later join other units in a compound. "
            "Do not let a larger proposition-sized span replace two distinct source-presented coordinates. Split coordinated, governed, embedded, sequential, or complement material whenever each piece independently performs the requested class function. "
            "For VERB specifically, inventory distinct lexical action/relation edges: state, copular/location, perception, report, intention, embedded, questioned, negated, recurring, and prospective relations can all count. Keep only the auxiliaries/particles/support words needed for ONE edge. A valid VERB is not suppressed because LABEL/PLACE/LOCATOR also applies. "
            "For PLACE/TIME preserve unnamed scene/frame roles established by progression. For LOCATOR preserve genuine contextual/orienting relations, including association, target/path, deictic position, recurring context, or materially spatialized context when they orient the story; do not treat every preposition as a locator. "
            "For OBJECT preserve source-treated choices/decisions/relations/results as referents, but do not substitute a bare discourse wrapper for its richer content. For LABEL preserve exact source-applied states/characterizations, including spatialized/internal state formulations, without promoting every modifier. "
            "Resolve coreference before ordering and use first referential establishment, not a merely anticipated/hypothetical lexical mention. "
            "Finish with an omission scan and a grain scan. Split absorbed independent coordinates; merge only fragments with no independent class function. Preserve exact contiguous wording and source posture. Never target an expected count."
        )
    if bounded.get("task") == "researcher_inventory_build_lightweight_compounds":
        return (
            "COMPOUND-LAYER PASS. Units are final and must not be changed or repaired here. Re-read the source and reconstruct each materially distinct source-presented proposition/event/state/question/report/reflection/intention/relation from already-retained units. "
            "Use all and only participating refs in source/semantic order. Do not create sentence-wide graphs, arbitrary subsets, every recombination, redundant nested subsets, or a compound whose purpose is to compensate for a missing unit."
        )
    return "Apply the installed V28 durable contract exactly to this bounded request."


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
    wait(session_id, timeout=SESSION_WAIT_SECONDS)
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
        "Execute only this bounded request under your installed durable V28 contract and supplied neutral apparatus rules. "
        "Return ONLY the JSON value required by response_schema. Do not infer or reconstruct any archetype, expected answer, expected count, evaluator preference, prior scored output, sealed holdout source, or holdout output.\n\n"
        "TASK ATTENTION:\n" + attention + "\n\n"
        "REQUEST JSON:\n" + json.dumps(bounded, ensure_ascii=False)
    )
    provisional = _session(agent_id, initial_prompt, "researcher_inventory_v28_extract")

    verify_prompt = (
        "Perform a separate stateless V28 adjudication. Re-read the complete source and independently rebuild the requested result BEFORE comparing with the provisional output. "
        "Apply four checks in order: "
        "(1) COVERAGE — identify every source-presented coordinate genuinely doing THIS class job; "
        "(2) FUNCTION — retain a coordinate when it is independently useful/selectable for the requested class even if it is not a complete proposition; "
        "(3) GRAIN — split proposition-sized spans that absorb another independent coordinate, but merge bare grammatical fragments that have no independent class function; "
        "(4) REPAIR — add genuine omissions, remove unsupported duplicates/inferences, and preserve exact source order/coreference/posture. "
        "For VERB, rebuild distinct lexical relation edges rather than complete proposition-sized predicate packages; split coordinated/governed/embedded relations when each is independently represented, and allow state/copular/location relation edges when genuine. "
        "For LOCATOR, use contextual/orienting function rather than physical-preposition-only or every-preposition rules. PLACE/TIME may be unnamed scene/frame coordinates. OBJECT may be an explicit abstract choice/decision/relation. LABEL may be an exact state/characterization formulation. "
        "Do not target a count. Return the complete replacement JSON, not a critique.\n\n"
        "TASK ATTENTION:\n" + attention + "\n\n"
        "REQUEST JSON:\n" + json.dumps(bounded, ensure_ascii=False) + "\n\n"
        "PROVISIONAL_UNSCORED_OUTPUT:\n" + json.dumps(provisional, ensure_ascii=False)
    )
    verified = _session(agent_id, verify_prompt, "researcher_inventory_v28_adjudication")
    sys.stdout.write(json.dumps(verified, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
