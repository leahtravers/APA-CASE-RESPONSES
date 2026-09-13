#!/usr/bin/env python3
"""V18 bounded adapter with symmetric stateless verification.

The worker sees only the durable V18 contract, neutral apparatus task rules, the
bounded source/request, and one unscored provisional output from another stateless
pass under the same contract. No archetype, evaluator finding, expected count,
scored output, or holdout output is ever supplied to the worker.
"""
from __future__ import annotations

import json
import sys

from openai_agents_adapter import AGENT_ID_FILE, final_answer, request, wait


CLASS_ATTENTION = {
    "PLACE": (
        "Retain the fewest PLACE rows that preserve every materially distinct where/scene/site/position function. "
        "Unnamed PLACE rows are valid when a distinct represented occurrence or relation genuinely needs a separate where-coordinate. "
        "Do not create a new PLACE for every action, surface, path, direction, figurative phrase, or object merely because spatial wording is present."
    ),
    "TIME": (
        "Retain the fewest TIME rows that preserve every materially distinct represented episode/span/frame. "
        "Unnamed TIME rows are valid when a distinct frame is represented without a clock/date phrase. "
        "Several predicates/questions may share one frame; do not create TIME from every verb, duration question, frequency token, subordinate phrase, or contemplated action inside the same frame."
    ),
    "PERSON": (
        "Resolve aliases/pronouns/stable groups before counting. Retain materially represented actors and relation-only human endpoints only when a material retained relation would otherwise lose that person/group."
    ),
    "OBJECT": (
        "Retain independently selectable represented referents: concrete/abstract things, source-distinguished parts, values, decisions/choices, relations-as-things, named sets, internal or figurative objects. "
        "Do not nominalize every clause/complement/quality/predicate into OBJECT, and do not duplicate wording whose only independent job is another class."
    ),
    "LABEL": (
        "Retain only independently reusable source-applied characterizations. Ordinary descriptive material may set qualities_available without becoming a LABEL row. "
        "Do not inventory every adjective, modifier, intensifier, predicate token, or descriptive fragment as LABEL."
    ),
    "VERB": (
        "Retain materially distinct lexical predicate relations at lightweight researcher grain. Use the shortest complete exact lexical construction. "
        "Do not emit standalone auxiliaries, infinitival markers, discourse scaffolding, reporting-control fragments, or whole clauses when a shorter predicate carries the relation. Split only when distinct predicate relations would otherwise disappear."
    ),
    "LOCATOR": (
        "Retain only independently useful setting/position/path/direction/origin/destination/containment/movement/proximity/situational-context relations. "
        "Do not turn emotion/state, characterization, ordinary argument marking, temporal clauses, isolated prepositions, or every occurrence of directional words into LOCATOR."
    ),
}

COMPOUND_ATTENTION = (
    "Build the smallest complete reassembly spine of materially distinct represented propositions/situations. "
    "Use only retained coordinates that genuinely belong to each proposition. Keep one proposition together; split materially different propositions. "
    "Do not create arbitrary subsets, quality-only fragments, every possible recombination, or a compound merely because a unit exists."
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
            "Read the complete source before answering this class. Apply the class-local removal test: retain a row only if removing it would erase a materially distinct researcher-selectable function of this class. "
            "Then run both an omission pass and an excess pass. Preserve unnamed PLACE/TIME coordinates when materially required, but do not manufacture rows from mere grammar or describability. "
            "Cross-class overlap is allowed only when the same source material independently does different class jobs. "
            "COPY SOURCE FIELDS EXACTLY: source_wording, source_cue, and order_cue must be character-for-character contiguous substrings of the supplied source, with the same punctuation, apostrophes, hyphens, capitalization, dialect, and spelling. Never reconstruct a source phrase from memory. "
            "For explicit non-PLACE/TIME coordinates, source_wording cannot be null. Prefer the shortest complete exact lexical span that carries the coordinate. "
            + CLASS_ATTENTION.get(cls, "")
        )
    if task == "researcher_inventory_build_lightweight_compounds":
        return COMPOUND_ATTENTION
    return "Apply the installed V18 durable contract and supplied neutral apparatus rules exactly to this bounded task."


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
        "Execute only this bounded request under your installed durable V18 contract and supplied neutral apparatus rules. "
        "Return ONLY the JSON value required by response_schema. Do not infer or reconstruct any archetype, expected answer, expected count, evaluator preference, prior scored output, or holdout content.\n\n"
        "TASK ATTENTION:\n" + attention + "\n\n"
        "REQUEST JSON:\n" + json.dumps(bounded, ensure_ascii=False)
    )
    provisional = _session(agent_id, initial_prompt, "researcher_inventory_v18_initial")

    verify_prompt = (
        "Perform a separate stateless symmetric verification under your installed durable V18 contract and supplied neutral apparatus rules. "
        "The provisional output is unscored and non-authoritative. Re-read the complete source and rebuild the requested result. "
        "Use the provisional only as a checklist. ADD only genuinely missing rows whose removal would erase a materially distinct class function. KEEP only rows that independently pass that same removal test. DELETE unsupported inference, wrong-class-only material, grammatical debris, qualifier-only material, or true same-class duplicates. "
        "Do not keep a row merely because it is source-grounded. Do not delete a row merely because it is unnamed, co-located, less salient, or overlaps another class. "
        "For source fields, copy exact contiguous source substrings character-for-character; if the provisional copied a phrase inaccurately, repair the copy without changing the semantic inventory. "
        "Return ONLY the complete replacement JSON required by response_schema.\n\n"
        "TASK ATTENTION:\n" + attention + "\n\n"
        "REQUEST JSON:\n" + json.dumps(bounded, ensure_ascii=False) + "\n\n"
        "PROVISIONAL_UNSCORED_OUTPUT:\n" + json.dumps(provisional, ensure_ascii=False)
    )
    verified = _session(agent_id, verify_prompt, "researcher_inventory_v18_verification")
    sys.stdout.write(json.dumps(verified, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
