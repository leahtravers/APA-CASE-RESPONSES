#!/usr/bin/env python3
"""V22 bounded adapter with balanced admission/closure verification.

The worker sees only its installed durable V22 contract, neutral apparatus rules, the
bounded source/request, and one unscored provisional output from another stateless
pass under the same contract. No archetype, evaluator finding, expected count,
scored output, or sealed holdout material is supplied.
"""
from __future__ import annotations

import json
import sys

from openai_agents_adapter import AGENT_ID_FILE, final_answer, request, wait


CLASS_ATTENTION = {
    "PLACE": (
        "Admit a WHERE row only when the location is independently researcher-indexable at lightweight grain: a setting, materially distinct situation-position, origin, or destination. Do not index every entity association, accompaniment, object position, spatially imaginable predicate, or path wording that belongs only in LOCATOR. Local unnamed positions remain valid when they are genuinely separate where-frames."
    ),
    "TIME": (
        "Admit a TIME row only when it is an independently reselectable episode/frame/span. Preserve genuine subepisode boundaries, recurrence, standing spans, reports, changed-state periods, intention/reflection/prospective frames. Do not create TIME for each action, clause, purpose, question, or micro-step inside an unchanged frame."
    ),
    "PERSON": (
        "Admit materially represented human actors/stable groups and relation endpoints whose identity independently matters. Resolve aliases, pronouns, kinship, and stable groups before counting."
    ),
    "OBJECT": (
        "Admit only independently referable things, explicitly reified relations, values, sets, choices, decisions, or alternatives. Do not turn every noun phrase, predicate, clause, state, action, or nominalizable proposition into OBJECT."
    ),
    "LABEL": (
        "Admit only independently retrievable characterizations. Use the shortest complete phrase preserving material polarity/qualification. Do not index every modifier, quantity, clause, action failure, or descriptive residue."
    ),
    "VERB": (
        "Admit one VERB per independently reconnectable semantic action/relation edge. Nested or embedded predicates earn separate rows only when they contribute their own material relation edge; do not split support/control/modal/purpose scaffolding mechanically."
    ),
    "LOCATOR": (
        "Admit only independently indexable locating/context relations. Preserve meaningful setting/position/path/direction/origin/destination/containment/proximity/trajectory relations, but reject routine possession/accompaniment/instrument/recipient/topic marking and spatial metaphor that is not independently locative."
    ),
}

COMPOUND_ATTENTION = (
    "Build compounds only after units are final. Create one lightweight compound per materially distinct proposition/relation. Include all retained units that materially participate. Include a retained PLACE/TIME/LOCATOR frame only when it specifically governs the proposition; inherit a nearby frame only while that independently indexed frame is actually in force. Do not make variants from optional frame inheritance, arbitrary subsets, or quality-only details."
)


def _bounded_request(payload: dict) -> dict:
    keep = {
        "task", "rules", "class", "class_rule", "response_schema", "source",
        "units", "candidate", "researcher_interest", "created_by_ref", "correction",
    }
    return {k: v for k, v in payload.items() if k in keep}


def _attention_for(bounded: dict) -> str:
    task = bounded.get("task")
    if task == "researcher_inventory_extract_one_class":
        cls = bounded.get("class")
        return (
            "Read the complete source. Use ADMISSION FIRST, BOUNDED CLOSURE SECOND, PRUNE THIRD. "
            "ADMISSION: for each candidate require source grounding, a real positive job for this class, independent researcher-selectable/reconnective coordinate status at lightweight semantic grain, material semantic/navigation loss if omitted, and no same-class duplicate. Material representation alone is not enough. "
            "BOUNDED CLOSURE: after applying that gate, scan the complete source for omitted local or cross-class-overlapping candidates that independently pass the SAME gate. Do not widen the gate to maximize coverage. "
            "PRUNE/EXACTNESS: remove aliases, true duplicates, grammar/support debris, invention, and candidates that fail independent coordinate status; then repair exact source copying and semantic ordering. Do not optimize for fewer rows or more rows. "
            "ORDER BY EARLIEST MATERIAL SEMANTIC ANCHOR after alias/coreference resolution. "
            "COPY SOURCE FIELDS EXACTLY: explicit source_wording and source_cue must be contiguous character-for-character source substrings with original punctuation, apostrophes, hyphens, capitalization, spelling, and dialect. For a materially required unnamed PLACE/TIME only, source_wording may be null. "
            + CLASS_ATTENTION.get(cls, "")
        )
    if task == "researcher_inventory_build_lightweight_compounds":
        return COMPOUND_ATTENTION
    return "Apply the installed V22 durable contract and supplied neutral apparatus rules exactly to this bounded task."


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
        "Execute only this bounded request under your installed durable V22 contract and supplied neutral apparatus rules. Return ONLY the JSON value required by response_schema. Do not infer or reconstruct any archetype, expected answer, expected count, evaluator preference, prior scored output, sealed holdout source, or holdout output.\n\n"
        "TASK ATTENTION:\n" + attention + "\n\n"
        "REQUEST JSON:\n" + json.dumps(bounded, ensure_ascii=False)
    )
    provisional = _session(agent_id, initial_prompt, "researcher_inventory_v22_initial")

    verify_prompt = (
        "Perform a separate stateless V22 verification. The provisional output is unscored and non-authoritative. Re-read the complete source and rebuild the requested result from the durable contract. "
        "FIRST perform an ADMISSION AUDIT: test every provisional row against the full independent lightweight admission gate and remove any row that fails it, even if materially represented. "
        "SECOND perform BOUNDED CLOSURE: scan the entire source for omitted candidates and add only those that independently pass the exact same gate, including valid local coordinates and valid cross-class overlap. "
        "THIRD resolve aliases/true duplicates, remove grammar debris/invention, repair exact source copying, and order by earliest semantic anchor. "
        "Do not prefer the provisional row count. Do not optimize for fewer rows or more rows. Do not widen or narrow the gate because a candidate appeared or did not appear in the provisional output. Return ONLY the complete replacement JSON required by response_schema.\n\n"
        "TASK ATTENTION:\n" + attention + "\n\n"
        "REQUEST JSON:\n" + json.dumps(bounded, ensure_ascii=False) + "\n\n"
        "PROVISIONAL_UNSCORED_OUTPUT:\n" + json.dumps(provisional, ensure_ascii=False)
    )
    verified = _session(agent_id, verify_prompt, "researcher_inventory_v22_verification")
    sys.stdout.write(json.dumps(verified, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
