#!/usr/bin/env python3
"""V14 bounded adapter.

The installed durable contract is the sole behavioral authority. This adapter
never supplies archetypes, expected outputs/counts, evaluator findings, scored
outputs, prior gold, or holdout material. V14 performs one bounded session per
requested class/compound task; the prompt itself requires omission and excess
passes. This avoids the V13 two-session adapter exceeding the apparatus process
timeout on long sources while preserving worker isolation.
"""
from __future__ import annotations

import json
import sys

from openai_agents_adapter import AGENT_ID_FILE, final_answer, request, wait


CLASS_ATTENTION = {
    "PLACE": (
        "Return sparse site/position handles only. A motion or contemplated exit is not itself a PLACE unless a distinct destination site is represented. "
        "A recurring activity does not imply a new PLACE unless its setting is independently distinguished. Include required unnamed occurrence positions, including present telling, only when they perform a distinct where job."
    ),
    "TIME": (
        "Return coherent episode/frame handles, not one frame per action or predicate. Actions, questions, transitions, and reflections inside one episode normally share that TIME. "
        "Use one present-reflection frame for the current reflective telling when appropriate. Create a prospective TIME only for a separately represented future/prospective frame, not merely a contemplated action inside a current episode."
    ),
    "PERSON": (
        "Resolve aliases/coreference first. Keep materially represented actors/endpoints. Speaker canonical_key is B. Order non-speakers by first independent participation; relation-only actors may have null order_cue."
    ),
    "OBJECT": (
        "Keep source-treated independently trackable referents, not noun phrases or nominalized clauses. Reject embedded propositions, grammatical complements, idiomatic slot nouns, and predicate complements that only complete a LABEL/VERB. "
        "Keep an abstract decision, choice, recurring relation, set, or internal object only when the source treats that whole as independently selectable."
    ),
    "LABEL": (
        "Keep the minimal independently selectable characterization, not the surrounding stance/control predicate. Do not duplicate ordinary VERB states as LABEL merely because they sound descriptive, and do not create a second label from an intensifier/comparative that only modifies an existing characterization. "
        "A locational phrase may also be LABEL only when independently used as a salient characterization."
    ),
    "VERB": (
        "Return minimal semantic predicate increments, not grammatical verb tokens. Semantically bound verb chains may be one coordinate. Do not atomize auxiliaries, copulas, infinitival pieces, question syntax, or predicate complements. "
        "Do not create a separate copular VERB when the semantic job is already a LABEL/LOCATOR. Split an embedded predicate only when it contributes an independently selectable semantic relation."
    ),
    "LOCATOR": (
        "Keep independently useful physical/internal position, direction, path, containment, or destination relations. Do not treat temporal subordinate clauses, ordinary argument/complement phrases, possession/topic relations, or abstract idioms as LOCATOR merely because they contain relational wording."
    ),
}

COMPOUND_ATTENTION = (
    "Using only supplied final units, map materially distinct propositions/situations at lightweight event/proposition grain. "
    "Do not create compounds for grammatical fragments or rejected coordinates. Keep one proposition together; split genuinely different propositions."
)


def _bounded_request(payload: dict) -> dict:
    keep = {
        "task", "class", "response_schema", "source", "units", "candidate",
        "researcher_interest", "created_by_ref", "correction",
    }
    return {k: v for k, v in payload.items() if k in keep}


def _attention_for(bounded: dict) -> str:
    task = bounded.get("task")
    if task == "researcher_inventory_extract_one_class":
        cls = bounded.get("class")
        return (
            "Apply the installed V14 independent-coordinate gate to this class only. Read the whole source. "
            "First identify distinct researcher handles, then perform an omission pass, then an excess pass. "
            "Functional semantic grain controls over grammatical decomposition. "
            + CLASS_ATTENTION.get(cls, "")
        )
    if task == "researcher_inventory_build_lightweight_compounds":
        return COMPOUND_ATTENTION
    return "Apply the installed V14 durable contract exactly to this bounded task."


def _session(agent_id: str, prompt: str):
    session = request(
        "/agents/sessions",
        method="POST",
        body={
            "agent_id": agent_id,
            "environment": {"type": "none"},
            "input": prompt,
            "metadata": {"apa_session_type": "researcher_inventory_v14_bounded"},
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
    prompt = (
        "Execute only this bounded request under your installed durable V14 contract. "
        "Return ONLY the JSON value required by response_schema. "
        "Do not infer or reconstruct any archetype, expected answer, expected count, evaluator preference, prior scored output, or holdout content.\n\n"
        "TASK ATTENTION:\n" + attention + "\n\n"
        "REQUEST JSON:\n" + json.dumps(bounded, ensure_ascii=False)
    )
    answer = _session(agent_id, prompt)
    sys.stdout.write(json.dumps(answer, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
