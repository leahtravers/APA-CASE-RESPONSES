#!/usr/bin/env python3
"""V20 bounded adapter with stateless positive-job verification.

The worker sees only its installed durable V20 contract, neutral apparatus rules, the
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
        "Keep only genuine WHERE jobs. An actual occurrence can have an unnamed place even when no place name appears. Present telling/reporting is an actual occurrence. Do not turn hypotheticals, generic recurrence, mental metaphor, or every movement/predicate into PLACE."
    ),
    "TIME": (
        "Keep only genuine EPISODE/SPAN jobs. No clock/date is required. Preserve materially distinct episodes, spans, recurrence, present reflection, intended periods, and prospective frames when they are actually established as temporal frames. Do not derive TIME from every verb, question, duration phrase, or hypothetical action."
    ),
    "PERSON": (
        "Keep materially represented human actors/stable groups and necessary relation-only human endpoints. Resolve aliases, pronouns, kinship, and stable groups before counting."
    ),
    "OBJECT": (
        "Keep independently selectable referents, including material choices/decisions/relations treated as things. Reject noun-phrase exhaustiveness, proposition wrappers, pronoun repeats, metadiscourse, and abstract duplicates."
    ),
    "LABEL": (
        "Return the characterization itself at shortest complete source phrase grain. Strip subject/question/reporting/copular scaffolding when it is not part of the characterization. Do not return a whole question or clause just because it contains a quality."
    ),
    "VERB": (
        "Return the shortest complete material lexical action/relation. Do not fragment auxiliaries/support/control/negation/infinitives. Do not emit copular/support predicates whose only job is carrying a LABEL state. Preserve real locative/reporting/thinking/perception relations."
    ),
    "LOCATOR": (
        "Keep only phrases with an independent locating/context job: setting, position, path, direction, containment, movement, proximity, recurring context, or genuine mental/figurative path/location. Reject routine argument marking and spatial-looking wording whose primary job is only a LABEL state."
    ),
}

COMPOUND_ATTENTION = (
    "Build compounds only after units are final. Include only units that materially participate in the proposition. Do not automatically inherit every broad scene/place/time/locator that is globally true of the story. Use the nearest specific frame only when it actually belongs to that proposition. Keep one proposition together, split materially different propositions, and do not create arbitrary subsets or quality-only fragments."
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
            "Read the complete source. For each proposed row state its POSITIVE JOB for this class. Keep it only if that job is materially represented/necessary, independent, nonduplicate, and materially useful if retained. If the row exists only because grammar or another class makes the phrase describable, delete it. When a marginal row has no clear positive class job, omit it. "
            "ORDER BY EARLIEST MATERIAL SEMANTIC ANCHOR after alias/coreference resolution. "
            "COPY SOURCE FIELDS EXACTLY: source_wording and source_cue must be contiguous character-for-character source substrings with original punctuation, apostrophes, hyphens, capitalization, spelling, and dialect. For a materially required unnamed PLACE/TIME only, source_wording may be null. "
            + CLASS_ATTENTION.get(cls, "")
        )
    if task == "researcher_inventory_build_lightweight_compounds":
        return COMPOUND_ATTENTION
    return "Apply the installed V20 durable contract and supplied neutral apparatus rules exactly to this bounded task."


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
        "Execute only this bounded request under your installed durable V20 contract and supplied neutral apparatus rules. Return ONLY the JSON value required by response_schema. Do not infer or reconstruct any archetype, expected answer, expected count, evaluator preference, prior scored output, sealed holdout source, or holdout output.\n\n"
        "TASK ATTENTION:\n" + attention + "\n\n"
        "REQUEST JSON:\n" + json.dumps(bounded, ensure_ascii=False)
    )
    provisional = _session(agent_id, initial_prompt, "researcher_inventory_v20_initial")

    verify_prompt = (
        "Perform a separate stateless V20 verification. The provisional output is unscored and non-authoritative. Re-read the complete source and rebuild the requested result from the durable contract. For EVERY provisional row, identify its positive job for this class; remove it if the job is unclear, grammatical-only, another-class-only, redundant, or marginal. Add only a clearly missing positive job. Resolve aliases/coreference and exact source copying. Return ONLY the complete replacement JSON required by response_schema.\n\n"
        "TASK ATTENTION:\n" + attention + "\n\n"
        "REQUEST JSON:\n" + json.dumps(bounded, ensure_ascii=False) + "\n\n"
        "PROVISIONAL_UNSCORED_OUTPUT:\n" + json.dumps(provisional, ensure_ascii=False)
    )
    verified = _session(agent_id, verify_prompt, "researcher_inventory_v20_verification")
    sys.stdout.write(json.dumps(verified, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
