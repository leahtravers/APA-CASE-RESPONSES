#!/usr/bin/env python3
"""V17 bounded adapter with independent coverage-and-boundary verification.

The worker sees only the durable V17 contract, neutral apparatus task rules, the
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
        "Cover every materially represented scene/site/container/object-position/destination/occurrence-position that does a distinct PLACE job. "
        "Unnamed places are valid when a represented interaction, wait, relation, conversation, report, object position, origin, or destination needs a where coordinate. "
        "Do not turn path/direction/surface language whose job is relational into PLACE; those belong in LOCATOR when independently useful."
    ),
    "TIME": (
        "Cover every materially distinct represented episode/span/transition/recurring frame/present frame/prospective frame. "
        "A represented episode does not need a clock or date to receive TIME. Do not manufacture a TIME from every verb, frequency token, duration modifier, or subordinate phrase when no distinct frame exists."
    ),
    "PERSON": (
        "Resolve aliases, pronouns, and stable groups before counting. Retain materially represented actors/endpoints and relation-only people or groups when they are needed by a material retained source relation or object."
    ),
    "OBJECT": (
        "Cover materially represented selectable things, source-distinguished parts, values, decisions/choices, relations-as-things, named sets, internal represented objects, conditions-as-things, and figurative objects. "
        "Reject generic filler, worker-created nominalizations, grammatical complements, and wording whose only source job belongs to another class."
    ),
    "LABEL": (
        "Cover source-applied reusable characterizations: qualities/states, comparisons, identity terms, evaluations, characterization questions, corrections, rejections, contrasts, and material source answers. "
        "Do not turn every modifier into LABEL. Keep a LABEL when the source actually applies the wording as a characterization."
    ),
    "VERB": (
        "Cover every materially distinct source-level lexical predicate relation. Split matrix/embedded, coordinated, or sequential predicate material when the pieces express different represented relations. "
        "Keep support/negation/particles with the relation when needed, and keep true multiword predicates together. Do not over-merge distinct recoverable relations because they occur in one sentence or episode."
    ),
    "LOCATOR": (
        "Cover independently useful setting, position, path, direction, origin/destination, containment, movement, proximity, and situational-context relations using the smallest complete source construction. "
        "PLACE stores a site; LOCATOR stores the relation to/through/from/within a site or context. Do not retain isolated prepositions or routine argument marking."
    ),
}

COMPOUND_ATTENTION = (
    "Build a source-level reassembly spine covering materially distinct represented propositions/situations. "
    "For each material proposition, use the retained participant/predicate/object/place/time/label/locator coordinates that actually belong to it, in semantic/source order. "
    "Split separate represented propositions; do not create grammatical fragments, arbitrary subsets, quality-only noise, or every possible recombination."
)


def _bounded_request(payload: dict) -> dict:
    # Neutral apparatus rules/class rules are part of the admitted task contract and
    # must reach the worker. Gold/evaluator/holdout material is never accepted here.
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
            "Read the complete source before answering this class. Inventory all materially represented class coordinates, not only salient ones. "
            "Run a second end-to-end omission pass, then a class-boundary pass. Remove only unsupported inference, grammatical debris, wrong-class-only material, and true same-class duplicates. "
            "Do not substitute synonyms, invent qualifications, or require physical naming/clock dating for represented unnamed PLACE/TIME coordinates. "
            "Cross-class overlap is permitted when the same source span performs different class jobs. "
            + CLASS_ATTENTION.get(cls, "")
        )
    if task == "researcher_inventory_build_lightweight_compounds":
        return COMPOUND_ATTENTION
    return "Apply the installed V17 durable contract and the supplied neutral apparatus rules exactly to this bounded task."


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
        "Execute only this bounded request under your installed durable V17 contract and the supplied neutral apparatus rules. "
        "Return ONLY the JSON value required by response_schema. Do not infer or reconstruct any archetype, expected answer, expected count, evaluator preference, prior scored output, or holdout content.\n\n"
        "TASK ATTENTION:\n" + attention + "\n\n"
        "REQUEST JSON:\n" + json.dumps(bounded, ensure_ascii=False)
    )
    provisional = _session(agent_id, initial_prompt, "researcher_inventory_v17_initial")

    verify_prompt = (
        "Perform a separate stateless coverage-and-boundary verification under your installed durable V17 contract and the supplied neutral apparatus rules. "
        "The provisional output is unscored and non-authoritative. Re-read the complete source and rebuild the requested result from the contract. "
        "Use the provisional only as a checklist: add any source-grounded materially distinct class coordinate it omitted; retain rows that pass the class rule; delete only unsupported inference, grammatical debris, wrong-class-only material, or true same-class duplicates. "
        "Do not collapse separate lexical predicate relations merely because they share a sentence or event. Do not delete unnamed PLACE/TIME coordinates merely because the site/time is not explicitly named. "
        "Preserve exact/source-near language, source posture, and material source order. Return ONLY the complete replacement JSON required by response_schema.\n\n"
        "TASK ATTENTION:\n" + attention + "\n\n"
        "REQUEST JSON:\n" + json.dumps(bounded, ensure_ascii=False) + "\n\n"
        "PROVISIONAL_UNSCORED_OUTPUT:\n" + json.dumps(provisional, ensure_ascii=False)
    )
    verified = _session(agent_id, verify_prompt, "researcher_inventory_v17_verification")
    sys.stdout.write(json.dumps(verified, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
