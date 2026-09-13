#!/usr/bin/env python3
"""V13 adapter: bounded extraction plus independent stateless contract verification.

The durable saved-agent contract is the sole behavioral authority. This adapter
never supplies archetypes, expected outputs/counts, evaluator findings, scored
outputs, or holdout material. For each bounded extraction it runs one initial
session and one separate stateless verification session under the same saved
agent. The verifier receives only the source/task schema and the first unscored
candidate, then rebuilds the requested result under the durable contract.
"""
from __future__ import annotations

import json
import sys

from openai_agents_adapter import AGENT_ID_FILE, final_answer, request, wait


CLASS_ATTENTION = {
    "PLACE": (
        "Evaluate PLACE locally as scene/occurrence-position handles, not place-like words. "
        "Consider every materially distinct represented occurrence for whether it needs its own where/position handle, including unnamed positions and physically overlapping occurrences. "
        "Reject surfaces, containers, figurative/internal wording, and setting-like nouns that do not independently locate represented material."
    ),
    "TIME": (
        "Evaluate TIME locally as episode/frame handles, not temporal wording. "
        "Consider every materially distinct represented situation for whether it needs its own when/frame handle, including unnamed earlier/later/recurring/reflective/prospective frames. "
        "Reject duration/frequency/sequence/tense/future wording that does not establish a distinct frame."
    ),
    "PERSON": (
        "Resolve aliases/coreference first. Keep materially represented actors/endpoints, not generic audiences, discourse addressees, hypothetical roles, or pronouns with no independent participation. "
        "Speaker canonical_key is B. For others, order_cue is first independent participation; relation-only actors may have null order_cue."
    ),
    "OBJECT": (
        "Keep source-treated independently trackable referents, not noun phrases. "
        "Reject incidental nouns, discourse wording, nominalized clauses, grammatical complements, and material whose only job is PLACE or LABEL. "
        "Do not let descriptive/evaluative wording hide an entity that the source actually treats as a referent."
    ),
    "LABEL": (
        "Keep source-applied independently selectable characterizations, states, comparisons, identity/evaluation/contrast/correction, including characterization-questions. "
        "Reject incidental modifiers, ordinary names/categories, quantities, temporal expressions, discourse decoration, and duplicate descriptive wording with no independent characterization job."
    ),
    "VERB": (
        "Keep distinct lexical happenings/states, not verb tokens. "
        "Fuse grammatical support/control/raising/infinitival/copular material with its lexical predicate unless it creates a separately selectable happening. "
        "Reject discourse management, filler, repeated/restated predicates, and quotation-introduction fragments unless that act independently matters in the represented story."
    ),
    "LOCATOR": (
        "Keep independently useful position/path/containment/movement/relational-context handles, not prepositional attachments. "
        "Reject routine possession, recipient, topic, argument, comparison support, and complement marking when no independent locating/path/context relation would be lost. "
        "Evaluate this class locally even when the same cue also anchors an unnamed PLACE or TIME."
    ),
}

COMPOUND_ATTENTION = (
    "Using only the supplied fixed units, map materially distinct represented propositions/situations at lightweight event/proposition grain. "
    "Do not create semantics or compounds merely because units exist. Split materially distinct propositions; keep jointly expressed fragments together."
)


def _bounded_request(payload: dict) -> dict:
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
        return (
            "Apply the installed V13 class-local independent-coordinate gate. Read the whole source, consider every represented situation for this requested class, then perform an omission pass and an excess pass. "
            "Do not globally type a source span into one exclusive class. Return functional researcher handles, not a lexical inventory. "
            + CLASS_ATTENTION.get(cls, "")
        )
    if task == "researcher_inventory_build_lightweight_compounds":
        return COMPOUND_ATTENTION
    return "Apply the installed V13 durable contract exactly to this bounded task."


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
        "Execute only this bounded request under your installed durable contract. "
        "The durable contract is the sole behavioral authority. Return ONLY the JSON value required by response_schema. "
        "Do not infer or reconstruct any archetype, expected answer, expected count, evaluator preference, prior scored output, or holdout content.\n\n"
        "TASK ATTENTION:\n" + attention + "\n\n"
        "REQUEST JSON:\n" + json.dumps(bounded, ensure_ascii=False)
    )
    provisional = _session(agent_id, initial_prompt, "researcher_inventory_v13_initial")

    verify_prompt = (
        "This is a separate stateless verification pass under your installed durable V13 contract. "
        "The PROVISIONAL_UNSCORED_OUTPUT below came from another stateless session under the same contract. It is not gold, not evaluator feedback, not an expected answer, and not authoritative. "
        "Re-read the entire source in REQUEST JSON and rebuild the requested result from the durable contract. Use the provisional output only as an omission/excess checklist. "
        "Do not keep a row because the first pass produced it. Do not omit a row because the first pass omitted related material. "
        "Apply the class-local gate, then an omission pass, then an excess pass. Return ONLY the complete replacement JSON value required by response_schema.\n\n"
        "TASK ATTENTION:\n" + attention + "\n\n"
        "REQUEST JSON:\n" + json.dumps(bounded, ensure_ascii=False) + "\n\n"
        "PROVISIONAL_UNSCORED_OUTPUT:\n" + json.dumps(provisional, ensure_ascii=False)
    )
    verified = _session(agent_id, verify_prompt, "researcher_inventory_v13_verification")
    sys.stdout.write(json.dumps(verified, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
