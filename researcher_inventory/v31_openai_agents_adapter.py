#!/usr/bin/env python3
"""V31 bounded adapter: class-specific units, then source-presented bindings.

The worker sees only its durable V31 contract, neutral task rules, the bounded
source/request, and one unscored provisional output from another session. No
archetype, evaluator finding, expected count, scored output, case-specific
correction example, or sealed holdout material is supplied.
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
        cls = bounded.get("class")
        grain = {
            "PLACE": "SCENE-POSITION GRAIN: settings and stable source-progressed scene-position roles; not every path/deictic/context token.",
            "TIME": "EPISODE/FRAME GRAIN: stable story episodes, spans, recurrences, intended/report/present/prospective frames; NEVER one time per verb/action.",
            "PERSON": "RESOLVED ACTOR GRAIN: represented human/social referents after alias/coreference resolution.",
            "OBJECT": "SOURCE-TREATED REFERENT GRAIN: concrete/abstract things, values, choices, decisions, relations or action-content only when source treats them as referable/selectable; no analyst proposition nominalization.",
            "LABEL": "CHARACTERIZATION-INCREMENT GRAIN: shortest exact source-applied characterization regardless of adjective/noun/adverb/participle/relational/verbal grammar.",
            "VERB": "LEXICAL RELATION-EDGE GRAIN: shortest exact complete predicate construction; split distinct edges but keep one source-selected coordinated action package together when it functions as one option.",
            "LOCATOR": "ORIENTING-RELATION GRAIN: smallest complete materially useful setting/position/path/accompaniment/context orientation; not every relational phrase.",
        }.get(cls, "Use the installed class-specific grain exactly.")
        correction = bounded.get("correction")
        correction_note = ""
        if correction:
            correction_note = (
                "\nVALIDATOR CORRECTION FROM YOUR PRIOR UNSCORED ATTEMPT: " + str(correction) +
                " Rebuild the complete class result from the source. Do not patch only the named field. "
                "Before return, verify every non-null source_wording, every source_cue, and every non-null order_cue by exact character-for-character substring lookup in source."
            )
        return (
            "UNIT PASS. Read the whole source first. The REQUESTED CLASS controls resolution; do not use one universal smallest-unit rule. "
            + grain + " "
            "Use this sequence: whole-source coverage -> positive THIS-class function -> class-specific grain -> reject grammar/reification/inference -> coreference/duplicates -> literal exact-span/order self-check. "
            "Cross-class overlap is allowed only for genuinely different positive functions. Preserve question/negation/hypothetical/intention/report/recurrence/uncertainty/dialect/prospective posture. "
            "LITERAL LOCK: explicit wording/cues/order cues must be copied exactly from contiguous source text; never repair punctuation or add/remove particles. If an intended phrase is not literally present, choose an exact source substring carrying that coordinate instead. "
            "Never target an expected count or infer an archetype." + correction_note
        )
    if bounded.get("task") == "researcher_inventory_build_lightweight_compounds":
        correction = bounded.get("correction")
        correction_note = ""
        if correction:
            correction_note = "\nVALIDATOR CORRECTION: " + str(correction) + " Rebuild the complete compound set from final units rather than patching one row."
        return (
            "COMPOUND PASS. Units are final and cannot be repaired here. Re-read source and identify SOURCE-PRESENTED BINDINGS at proposition/event/state/question/report/reflection/intention/characterization/relation-cluster grain. "
            "For each binding use all and only final units materially participating, in semantic/source order. Multiple VERB refs may belong in one event cluster. Make separate compounds only for separately presented bindings. "
            "Do not graph every sentence, emit arbitrary subsets/every recombination, duplicate nested subsets unless separately source-presented, or invent units to make a compound complete." + correction_note
        )
    return "Apply the installed V31 durable contract exactly to this bounded request."


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
        "Execute only this bounded request under your installed durable V31 contract and supplied neutral apparatus rules. "
        "Return ONLY the JSON value required by response_schema. Do not infer or reconstruct any archetype, expected answer, expected count, evaluator preference, prior scored output, case-specific correction, sealed holdout source, or holdout output.\n\n"
        "TASK ATTENTION:\n" + attention + "\n\n"
        "REQUEST JSON:\n" + json.dumps(bounded, ensure_ascii=False)
    )
    provisional = _session(agent_id, initial_prompt, "researcher_inventory_v31_extract")

    verify_prompt = (
        "Perform a separate V31 adjudication in a new session. Re-read the complete source and independently rebuild the requested result BEFORE comparing with the provisional output. "
        "Use this order: (1) COVERAGE at THIS class's own grain; (2) POSITIVE FUNCTION for THIS class; (3) CLASS-GRAIN test; (4) ANTI-DEBRIS/ANTI-REIFICATION; (5) COREFERENCE/DUPLICATES; (6) LITERAL LOCK — character-for-character exact substring check for every explicit span; (7) REPAIR omissions/extras only from those principles. "
        "Do not import VERB granularity into TIME or PLACE. TIME is episode/frame grain; PLACE is scene-position grain; OBJECT is source-treated referent grain; LABEL is characterization increment grain regardless of grammar; VERB is lexical relation-edge grain; LOCATOR is orienting-relation grain. "
        "Do not target a count. Return the complete replacement JSON, not a critique.\n\n"
        "TASK ATTENTION:\n" + attention + "\n\n"
        "REQUEST JSON:\n" + json.dumps(bounded, ensure_ascii=False) + "\n\n"
        "PROVISIONAL_UNSCORED_OUTPUT:\n" + json.dumps(provisional, ensure_ascii=False)
    )
    verified = _session(agent_id, verify_prompt, "researcher_inventory_v31_adjudication")
    sys.stdout.write(json.dumps(verified, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
