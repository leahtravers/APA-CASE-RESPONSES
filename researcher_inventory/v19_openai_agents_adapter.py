#!/usr/bin/env python3
"""V19 bounded adapter with stateless class-local verification.

The worker sees only its installed durable V19 contract, neutral apparatus rules, the
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
        "Check the whole represented-situation spine for distinct where-coordinates, including unnamed occurrence-positions for materially distinct waits, conversations, relations, remembered/reported episodes, and present telling. Do not collapse merely because physical location may overlap; do not split one undifferentiated scene merely because it contains many actions."
    ),
    "TIME": (
        "Check for distinct episodes/subepisodes, standing spans, changed-state periods, reported/remembered frames, recurring frames, present reflection, and separate prospective frames. Do not use verb count or temporal grammar as the boundary."
    ),
    "PERSON": (
        "Resolve aliases/pronouns/kinship/stable groups before counting. Preserve materially represented actors and relation-only human endpoints when a material relation otherwise loses them."
    ),
    "OBJECT": (
        "Apply a strict referential test. Preserve stable represented things/values/sets/choices/relations-as-things/internal or figurative objects. Delete proposition wrappers, metadiscourse wrappers, grammatical nominalizations, pronoun repeats, and abstract duplicates around more specific retained referents."
    ),
    "LABEL": (
        "Preserve materially source-applied characterization phrases even when they occur only once. Include states, qualities, comparisons, identities, evaluations, questions, corrections/rejections/contrasts/calibrations. Delete only support/reporting scaffolding, bare intensifier debris, or true duplicate characterization. Q is not a replacement for a material LABEL."
    ),
    "VERB": (
        "Preserve one row per materially distinct lexical predicate relation. Keep semantically bound support/control/negation/particle material with the relation rather than fragmenting it. Keep coordinated wording together when it is one contemplated/idiomatic action; split only genuinely separate predicate relations."
    ),
    "LOCATOR": (
        "Preserve independently useful physical, situational, figurative, or mental locating/context relations. Do not restrict to literal space, but delete isolated prepositions, routine argument marking, temporal-only phrases, and characterization-only wording."
    ),
}

COMPOUND_ATTENTION = (
    "Build compounds at complete represented proposition/situation grain after units are final. For each proposition, include every retained unit that materially participates in it, including applicable PLACE/TIME/LOCATOR frame units. Keep one proposition together; split materially different propositions. Do not create arbitrary subsets, quality-only fragments, every possible recombination, or a compound merely because a unit exists."
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
            "Read the complete source. First build a silent represented-situation spine in source order, then resolve only the requested class at its own natural grain. Use both tests for every row: COVERAGE (removing it erases a materially distinct function of this class) and INDEPENDENCE (that function is not present only because grammar/qualification/another class makes the wording describable). Run a whole-source omission pass and excess pass. "
            "ORDER BY EARLIEST SEMANTIC ANCHOR after alias/coreference resolution, not by the later phrase selected as source_wording/tag. "
            "COPY SOURCE FIELDS EXACTLY: source_wording, source_cue, and order_cue must be contiguous character-for-character source substrings with original punctuation, apostrophes, hyphens, capitalization, spelling, and dialect. For a materially required unnamed PLACE/TIME only, source_wording may be null. "
            + CLASS_ATTENTION.get(cls, "")
        )
    if task == "researcher_inventory_build_lightweight_compounds":
        return COMPOUND_ATTENTION
    return "Apply the installed V19 durable contract and supplied neutral apparatus rules exactly to this bounded task."


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
        "Execute only this bounded request under your installed durable V19 contract and supplied neutral apparatus rules. Return ONLY the JSON value required by response_schema. Do not infer or reconstruct any archetype, expected answer, expected count, evaluator preference, prior scored output, sealed holdout source, or holdout output.\n\n"
        "TASK ATTENTION:\n" + attention + "\n\n"
        "REQUEST JSON:\n" + json.dumps(bounded, ensure_ascii=False)
    )
    provisional = _session(agent_id, initial_prompt, "researcher_inventory_v19_initial")

    verify_prompt = (
        "Perform a separate stateless V19 verification. The provisional output is unscored and non-authoritative. Re-read the complete source, silently rebuild the represented-situation spine, and rebuild the requested result from the durable contract. Use the provisional only as a checklist. "
        "ADD class functions that are genuinely missing. KEEP only rows that satisfy both coverage and independence for this class. DELETE unsupported inference, wrong-class-only material, grammatical debris, proposition wrappers, support fragments, or true same-class duplicates as applicable. Do not delete a valid PLACE/TIME/LABEL merely to shorten the list. Do not add OBJECT/VERB/LOCATOR merely because grammar permits it. "
        "Recheck earliest-semantic-anchor ordering after alias/coreference resolution. Repair any source field by exact character-for-character copying without changing the semantic inventory. Return ONLY the complete replacement JSON required by response_schema.\n\n"
        "TASK ATTENTION:\n" + attention + "\n\n"
        "REQUEST JSON:\n" + json.dumps(bounded, ensure_ascii=False) + "\n\n"
        "PROVISIONAL_UNSCORED_OUTPUT:\n" + json.dumps(provisional, ensure_ascii=False)
    )
    verified = _session(agent_id, verify_prompt, "researcher_inventory_v19_verification")
    sys.stdout.write(json.dumps(verified, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
