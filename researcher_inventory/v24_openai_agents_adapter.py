#!/usr/bin/env python3
"""V24 bounded adapter with lightweight-coordinate and exact-source verification.

The worker sees only its installed durable V24 contract, neutral apparatus rules,
the bounded source/request, and one unscored provisional output from another
stateless pass under the same contract. No archetype, evaluator finding, expected
count, scored output, or sealed holdout material is supplied.
"""
from __future__ import annotations

import json
import sys

from openai_agents_adapter import AGENT_ID_FILE, final_answer, request, wait


CLASS_ATTENTION = {
    "PLACE": (
        "Identify distinct represented where-ANCHORS at lightweight story grain. Preserve real settings/scene positions and source-distinguished unnamed where-slots, but do not promote direction, path, departure, proximity, containment, or deixis into a PLACE unless the source independently establishes a location anchor."
    ),
    "TIME": (
        "Identify distinct represented episode/frame/span/recurrence/prospective HORIZON coordinates at lightweight story grain. Group actions that remain inside one represented frame. Do not create a TIME for every verb, embedded clause, purpose, question, state, property, or contemplated micro-action."
    ),
    "PERSON": (
        "Inventory the speaker and represented people/stable human groups who are actual participants/referents. Resolve aliases/pronouns/kinship before same-class deduplication. A role word used only as characterization does not create another PERSON."
    ),
    "OBJECT": (
        "Inventory source-represented referable things: concrete or abstract/internal things, source-distinguished parts/wholes, values, sets, services/results, decisions/next steps, and contemplated choices when treated as things. Do not nominalize every predicate/clause/state/pronoun/deictic/place/time into OBJECT."
    ),
    "LABEL": (
        "Inventory source-applied characterizations, not every predicate, participant noun, quantity, modifier, or whole proposition. Select the shortest complete exact contiguous source phrase that carries the characterization itself and preserve polarity/qualification when part of it."
    ),
    "VERB": (
        "Inventory each distinct lexical action/relation edge. Use the shortest complete contiguous source-near predicate construction and keep required phrasal/multiword predicates intact. Do not absorb subject/object/place/time/label/complement material into the VERB wording when those are separate units."
    ),
    "LOCATOR": (
        "Inventory the smallest complete represented locating/context relation: setting relation, position, direction, path, origin/destination, containment, proximity, movement, recurring context, participant-relative accompaniment/association, or genuine figurative/mental location. A LOCATOR relates coordinates and does not automatically create a PLACE/TIME anchor."
    ),
}

COMPOUND_ATTENTION = (
    "Build compounds only after units are final. Use one lightweight compound per distinct source-level proposition/relation. Include only units that actually participate or govern that proposition; do not add every class-parallel unit sharing the sentence. PLACE/TIME/LOCATOR appear only when they genuinely anchor/situate the proposition. Do not create arbitrary subset variants or redundant expansions."
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
            "LIGHTWEIGHT COORDINATE PASS. Read the entire source first. Scan in source order for represented coordinates that independently perform the requested class job at story grain. "
            "Do not apply importance/salience/researcher-worthiness/material-consequence pruning. Also do not mechanically enumerate every phrase that could be redescribed as this class. "
            "ANCHOR-VERSUS-RELATION CHECK. PLACE/TIME are anchors; PERSON/OBJECT are participants/referents; LABEL is characterization; VERB is a lexical relation edge; LOCATOR is a locating/contextual relation. Prevent class-parallel inflation. "
            "CROSS-CLASS OVERLAP requires an independent job in each class; it is not automatic. "
            "SOURCE-SPAN LOCK. For every explicit row, copy the shortest complete exact contiguous source substring that carries this class job into source_wording; source_cue must also be an exact contiguous substring. Only unnamed PLACE/TIME may use null source_wording. "
            "DEDUPE after the ledger: resolve aliases/coreference and remove true same-class duplicates, unsupported invention, and grammatical debris. "
            "SECOND PASS: scan for both omissions and over-splitting before returning. "
            + CLASS_ATTENTION.get(cls, "")
        )
    if task == "researcher_inventory_build_lightweight_compounds":
        return COMPOUND_ATTENTION
    return "Apply the installed V24 durable contract and supplied neutral apparatus rules exactly to this bounded task."


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
        "Execute only this bounded request under your installed durable V24 contract and supplied neutral apparatus rules. Return ONLY the JSON value required by response_schema. Do not infer or reconstruct any archetype, expected answer, expected count, evaluator preference, prior scored output, sealed holdout source, or holdout output.\n\n"
        "TASK ATTENTION:\n" + attention + "\n\n"
        "REQUEST JSON:\n" + json.dumps(bounded, ensure_ascii=False)
    )
    provisional = _session(agent_id, initial_prompt, "researcher_inventory_v24_initial")

    verify_prompt = (
        "Perform a separate stateless V24 verification. The provisional output is unscored and non-authoritative. Re-read the complete source and independently rebuild the requested result from the durable contract before comparing it with the provisional output. "
        "FIRST build your own source-order ledger at lightweight story grain. For each candidate require source grounding, the class positive job, and a distinct coordinate of that class rather than grammatical material inside another coordinate/relation. Do not use importance/salience/researcher-worthiness/material-consequence pruning. "
        "SECOND enforce anchor-versus-relation class boundaries and require independent class jobs for any cross-class overlap. "
        "THIRD enforce SOURCE-SPAN LOCK using the smallest complete exact contiguous phrase appropriate to the requested class. "
        "FOURTH resolve aliases/coreference, then remove true same-class duplicates, unsupported invention, grammatical debris, and over-split class-parallel rows. "
        "FIFTH compare your independently rebuilt ledger with the provisional output, recover omissions, remove extras, and correct source-copy/grain errors. Ignore the provisional row count. "
        "Return ONLY the complete replacement JSON required by response_schema.\n\n"
        "TASK ATTENTION:\n" + attention + "\n\n"
        "REQUEST JSON:\n" + json.dumps(bounded, ensure_ascii=False) + "\n\n"
        "PROVISIONAL_UNSCORED_OUTPUT:\n" + json.dumps(provisional, ensure_ascii=False)
    )
    verified = _session(agent_id, verify_prompt, "researcher_inventory_v24_verification")
    sys.stdout.write(json.dumps(verified, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
