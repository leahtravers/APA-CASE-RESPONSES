#!/usr/bin/env python3
"""V12 adapter: keep the durable agent contract authoritative.

The apparatus may carry legacy per-request helper prose for provider-neutral
adapters. V12 calibration must not let that transport prose override or conflict
with the durable contract installed on the saved agent. This adapter therefore
passes only bounded task data/schema plus mechanical retry corrections.

It also re-focuses each bounded call on the relevant *existing* V12 contract
gates. These attention directives contain no archetype examples, expected
answers, expected counts, evaluator findings, prior outputs, or holdout material.
They are execution scaffolding for the installed contract, not a new contract.
"""
from __future__ import annotations

import json
import sys

# This file is executed by path from the repository root. In that mode Python puts
# researcher_inventory/ itself on sys.path, so import the sibling module directly.
from openai_agents_adapter import AGENT_ID_FILE, final_answer, request, wait


CLASS_ATTENTION = {
    "PLACE": (
        "Apply the installed PLACE rules as a functional scene/occurrence-position inventory, not a place-word list. "
        "A named surface, container, geographic phrase, or setting-like noun is not automatically a PLACE. "
        "Retain it only when it independently locates represented material. Conversely, retain an unnamed PLACE when a materially distinct wait, encounter, conversation, object position, origin/destination, remembered occurrence, or present telling needs its own place handle. "
        "Physical overlap does not collapse distinct occurrence positions. Do a final excess pass: delete every PLACE whose removal loses no distinct where/position function."
    ),
    "TIME": (
        "Apply the installed TIME rules as an episode/frame inventory, not a temporal-expression list. "
        "A duration, frequency word, sequence marker, tense/aspect marker, clock phrase, or time-like wording is not automatically a TIME. "
        "Conversely, a materially distinct response, departure, wait, later conversation, remembered period, recurring period, present reflection, or prospective frame may require an unnamed TIME. "
        "Do a final excess pass: delete every TIME whose removal loses no distinct when/frame function."
    ),
    "PERSON": (
        "Apply the installed PERSON rules after resolving aliases/coreference. Return one coordinate per represented actor/group, not one per mention or description. "
        "The speaker canonical_key is B. For every other actor, order_cue must be the exact first source cue of independent participation. A merely possessive/beneficiary/descriptive actor that never independently participates must have order_cue null. "
        "Do not let an earlier possessive mention outrank an actor who independently participates earlier."
    ),
    "OBJECT": (
        "Apply the installed OBJECT rules to source-treated independently trackable referents, not noun phrases. "
        "Do not manufacture an OBJECT by nominalizing a clause or predicate; do not retain incidental nouns, grammatical complements, pronouns/placeholders, or words whose only job is PLACE or LABEL. "
        "Retain concrete or abstract material only when the source treats it as a thing/referent the researcher could independently select later. "
        "Do a final excess pass: delete every OBJECT whose removal loses no distinct referent."
    ),
    "LABEL": (
        "Apply the installed LABEL rules to source-applied characterizations/states/comparisons/identity/evaluation/contrast/correction, not descriptive-looking vocabulary. "
        "Do not create a LABEL merely because a noun has a modifier, a quantity appears, a place/object has an ordinary name, or a predicate contains an adjective/copula. "
        "A characterization may be a short phrase or represented state when that characterization itself is independently selectable. Preserve exact posture. "
        "Do a final excess pass: delete every LABEL whose removal loses no distinct characterization job."
    ),
    "VERB": (
        "Apply the installed VERB rules to materially distinct lexical happenings/states, not grammatical verb tokens. "
        "Return the smallest complete predicate construction that preserves the happening. Do not split auxiliaries, aspect/support material, control/raising scaffolding, or an infinitival construction into separate rows unless each part contributes a genuinely different researcher-selectable happening. "
        "Do not retain a restatement/coreferential repeat as a new happening, and do not merge genuinely distinct happenings. Preserve negation/question/intention/hypothetical posture. "
        "Do a final excess pass: delete every VERB whose removal loses no distinct happening/state."
    ),
    "LOCATOR": (
        "Apply the installed LOCATOR rules to independently useful where/position/path/containment/context relations, not prepositional or relational attachments. "
        "Do not retain routine possession, recipient, source, topic, argument, comparison support, or complement marking when the relation itself supplies no independently selectable location/path/context function. "
        "Retain physical or figurative position/path/context only when that relation materially reconnects represented material. "
        "Do a final excess pass: delete every LOCATOR whose removal loses no distinct locating/path/context job."
    ),
}

COMPOUND_ATTENTION = (
    "Apply the installed COMPOUND rules only after accepting the supplied units as fixed for this request. "
    "Build one lightweight compound for each materially distinct represented proposition/situation that reconnects retained units. "
    "Do not create a compound merely because a unit exists, do not create lexical/background fragments, do not invent semantics, and do not use any ref not supplied in units. "
    "Split materially different propositions; keep grammatical fragments together when they jointly express one proposition."
)


def _bounded_request(payload: dict) -> dict:
    """Strip legacy behavioral prose; preserve task data and mechanical feedback."""
    keep = {
        "task",
        "class",
        "response_schema",
        "source",
        "units",
        "candidate",
        "researcher_interest",
        "created_by_ref",
        "correction",
    }
    return {k: v for k, v in payload.items() if k in keep}


def _attention_for(bounded: dict) -> str:
    task = bounded.get("task")
    if task == "researcher_inventory_extract_one_class":
        cls = bounded.get("class")
        directive = CLASS_ATTENTION.get(cls, "")
        return (
            "Before returning, do both installed V12 checks: (1) a whole-source omission pass for missing functional coordinates, then "
            "(2) an excess pass removing lexical/grammatical candidates whose deletion loses no materially distinct class function. "
            "Return one row per functional researcher coordinate, not one row per word, noun phrase, adjective, verb token, preposition, or clause. "
            + directive
        )
    if task == "researcher_inventory_build_lightweight_compounds":
        return COMPOUND_ATTENTION
    return "Apply the installed durable contract exactly to this bounded task."


def main() -> int:
    payload = json.load(sys.stdin)
    agent_id = AGENT_ID_FILE.read_text(encoding="utf-8").strip()
    bounded = _bounded_request(payload)
    attention = _attention_for(bounded)
    prompt = (
        "Execute only this bounded request under your installed durable contract. "
        "The durable contract remains the sole behavioral authority; the following task attention only tells you which installed gates to apply now. "
        "Return ONLY the JSON value required by response_schema. "
        "Do not infer any expected answer, expected count, archetype, evaluator preference, prior output, or holdout content.\n\n"
        "TASK ATTENTION:\n" + attention + "\n\n"
        "REQUEST JSON:\n" + json.dumps(bounded, ensure_ascii=False)
    )
    session = request(
        "/agents/sessions",
        method="POST",
        body={
            "agent_id": agent_id,
            "environment": {"type": "none"},
            "input": prompt,
            "metadata": {"apa_session_type": "researcher_inventory_semantic_subroutine_v12"},
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
    value = json.loads(raw)
    sys.stdout.write(json.dumps(value, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
