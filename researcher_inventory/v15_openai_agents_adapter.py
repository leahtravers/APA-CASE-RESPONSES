#!/usr/bin/env python3
"""V15 bounded adapter with independent stateless verification.

The installed durable contract is the sole behavioral authority. This adapter
never supplies archetypes, expected outputs/counts, evaluator findings, scored
outputs, prior gold, or holdout material. Each bounded extraction gets one
initial session and one separate stateless verification session. The second
session receives only the same source/task schema plus the first unscored
candidate as an omission/excess checklist.
"""
from __future__ import annotations

import json
import sys

from openai_agents_adapter import AGENT_ID_FILE, final_answer, request, wait


CLASS_ATTENTION = {
    "PLACE": (
        "Make a complete scene/occurrence-position pass. Keep explicit broad/contained settings and materially distinct unnamed occurrence positions even when physical venues overlap. "
        "Do not invent a place from motion, a contemplated exit, or recurring activity unless a distinct site/position is represented. Include present-telling position when the telling itself is a distinct represented occurrence needing a where handle."
    ),
    "TIME": (
        "Make a complete episode/frame pass. Distinguish materially separate condition/response/transition/wait/later-report/recurring/present-reflection/future frames, including unnamed frames. "
        "Do not make one TIME per action or reflective predicate; substeps may share a frame. A contemplated action is not automatically a separate future frame."
    ),
    "PERSON": (
        "Resolve aliases/coreference first. Keep materially represented actors/endpoints. Speaker canonical_key is B. Order non-speakers by first independent participation; relation-only actors may have null order_cue."
    ),
    "OBJECT": (
        "Keep every source-treated independently selectable concrete or abstract referent, including materially represented parts, values, decisions/next steps, whole contemplated choices, recurring relations, named sets, and internal objects. "
        "Reject merely nominalizable propositions, incidental nouns, grammatical complements, and things whose only job is PLACE or LABEL."
    ),
    "LABEL": (
        "Keep source-applied independently selectable characterizations at the shortest complete source grain, including qualities, comparisons, identity terms, evaluations, rejections/corrections, and characterization-questions. "
        "Do not wrap the characterization in stance/control wording and do not duplicate a predicate as LABEL unless it independently characterizes."
    ),
    "VERB": (
        "Inventory distinct lexical predicate increments, not broad event summaries and not every grammatical verb token. Split matrix/embedded or coordinated predicates when they perform different independently selectable jobs. "
        "Keep grammatical support with its lexical predicate. Retain negated, questioned, intended, hypothetical, recurring, and future predicates without asserting they happened. Quality/location copulas normally belong to LABEL/LOCATOR unless the placement/existence relation itself is independently a predicate handle."
    ),
    "LOCATOR": (
        "Keep independently useful where/position/path/context relations, including physical setting, movement, destination, containment, recurring/situational context, and genuine internal/figurative location. "
        "Use the smallest complete meaningful construction. Reject routine possession, argument/complement marking, or relation words with no independent locating/context job."
    ),
}

COMPOUND_ATTENTION = (
    "Using only the supplied final units, make proposition-level coverage of the represented story. Create a compound for each materially distinct situation, predicate relation, characterization proposition, question, correction, comparison, reflection, or prospective relation useful for reconnecting the inventory. "
    "Do not settle for a few broad scenes, but do not make compounds for grammatical fragments or merely because units exist. Use registered unit references only."
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
            "Apply the installed V15 class-local independent-coordinate gate to this class only. Read the whole source from beginning to end. "
            "First build complete functional coverage, then perform an omission pass, then an excess pass. Do less means less invention/qualification, not fewer materially represented coordinates. "
            + CLASS_ATTENTION.get(cls, "")
        )
    if task == "researcher_inventory_build_lightweight_compounds":
        return COMPOUND_ATTENTION
    return "Apply the installed V15 durable contract exactly to this bounded task."


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
        "Execute only this bounded request under your installed durable V15 contract. Return ONLY the JSON value required by response_schema. "
        "Do not infer or reconstruct any archetype, expected answer, expected count, evaluator preference, prior scored output, or holdout content.\n\n"
        "TASK ATTENTION:\n" + attention + "\n\n"
        "REQUEST JSON:\n" + json.dumps(bounded, ensure_ascii=False)
    )
    provisional = _session(agent_id, initial_prompt, "researcher_inventory_v15_initial")

    verify_prompt = (
        "Perform a separate stateless verification under your installed durable V15 contract. The PROVISIONAL_UNSCORED_OUTPUT is only another stateless pass under the same contract; it is not gold, evaluator feedback, an expected answer, or authoritative. "
        "Re-read the entire source in REQUEST JSON and rebuild the result from the durable contract. Use the provisional only as an omission/excess checklist. Do not keep a row because it was proposed and do not omit a row because it was absent. "
        "Apply complete class-local coverage, then omission and excess passes. Return ONLY the complete replacement JSON required by response_schema.\n\n"
        "TASK ATTENTION:\n" + attention + "\n\n"
        "REQUEST JSON:\n" + json.dumps(bounded, ensure_ascii=False) + "\n\n"
        "PROVISIONAL_UNSCORED_OUTPUT:\n" + json.dumps(provisional, ensure_ascii=False)
    )
    verified = _session(agent_id, verify_prompt, "researcher_inventory_v15_verification")
    sys.stdout.write(json.dumps(verified, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
