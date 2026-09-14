#!/usr/bin/env python3
"""V27 bounded adapter using independent-coordinate and grain adjudication.

The worker sees only its durable V27 contract, neutral task rules, the bounded
source/request, and one unscored provisional output from another stateless pass.
No archetype, evaluator finding, expected count, scored output, or sealed holdout
material is supplied.
"""
from __future__ import annotations

import json
import sys

from openai_agents_adapter import AGENT_ID_FILE, final_answer, request, wait


def _bounded_request(payload: dict) -> dict:
    keep = {
        "task", "rules", "class", "class_rule", "response_schema", "source",
        "units", "candidate", "researcher_interest", "created_by_ref", "correction",
    }
    return {k: v for k, v in payload.items() if k in keep}


def _attention_for(bounded: dict) -> str:
    if bounded.get("task") == "researcher_inventory_extract_one_class":
        return (
            "INDEPENDENT-COORDINATE PASS. Read the whole source before deciding rows. "
            "Lightweight means story-coordinate resolution, not sparse summary and not grammatical decomposition. "
            "For every candidate ask whether the source presents one independently selectable coordinate whose primary job answers THIS requested class at story/workbook grain. "
            "Retain full source coverage, but reject rows created only from auxiliaries, copulas, predicate fragments, arbitrary prepositional arguments, nominalized clauses, nested noun pieces, or class-parallel redescriptions that fail that independent-job test. "
            "Use dominant source job. Permit cross-class overlap only when the exact source material genuinely performs each job independently. "
            "PLACE/TIME may be unnamed scene/frame roles established by narrative progression, so do not collapse distinct later/waiting/destination/present-telling roles merely because their physical name or clock time is absent. "
            "VERB must be one complete meaningful predicate construction rather than grammatical fragments; pure copular characterization/location is not an extra VERB. "
            "LOCATOR must be a genuine orienting position/path/context relation, not merely any to/for/with/about/of/at/on/in phrase. "
            "OBJECT must stay one conceptual referent rather than being split into internal sub-objects or nominalized clause content. "
            "Preserve source posture and exact contiguous wording. Finish with both an omission scan and a grain/over-splitting scan. Do not target an expected count."
        )
    if bounded.get("task") == "researcher_inventory_build_lightweight_compounds":
        return (
            "STORY-BINDING COMPOUND PASS. Units are final. Re-read the source and emit a compound only for an independently source-presented story proposition/event/state/question/report/reflection/intention that binds retained units. "
            "Use all and only participating retained units. Do not create units, sentence-wide graphs, arbitrary subsets, or nested subcompounds that add no separately source-presented proposition/event/state."
        )
    return "Apply the installed V27 durable contract exactly to this bounded request."


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
        "Execute only this bounded request under your installed durable V27 contract and supplied neutral apparatus rules. "
        "Return ONLY the JSON value required by response_schema. Do not infer or reconstruct any archetype, expected answer, expected count, evaluator preference, prior scored output, sealed holdout source, or holdout output.\n\n"
        "TASK ATTENTION:\n" + attention + "\n\n"
        "REQUEST JSON:\n" + json.dumps(bounded, ensure_ascii=False)
    )
    provisional = _session(agent_id, initial_prompt, "researcher_inventory_v27_extract")

    verify_prompt = (
        "Perform a separate stateless V27 adjudication. Re-read the complete source and independently rebuild the requested result BEFORE looking for agreement with the provisional output. "
        "Apply four checks in order: "
        "(1) STORY COVERAGE — identify all source-presented story coordinates doing the requested class job, including unnamed PLACE/TIME scene roles when narrative progression establishes them; "
        "(2) ADMISSION — for each candidate decide whether it independently answers this requested class at story/workbook grain rather than merely being grammatical material; "
        "(3) GRAIN — merge predicate/preposition/noun fragments into the correct complete coordinate, use dominant source job, and remove class-parallel duplicates that do not independently perform this class; "
        "(4) REPAIR — add genuine omitted coordinates and remove unsupported/over-split coordinates. "
        "For VERB prefer one complete meaningful predicate construction and reject pure copular characterization/location as an extra verb. For LOCATOR reject arbitrary argument/topic/recipient prepositions. For OBJECT keep one conceptual referent. "
        "Preserve question/negation/hypothetical/report/intention/recurrence/prospect posture and exact contiguous source wording. "
        "Never target a count. Return the complete replacement JSON, not a critique.\n\n"
        "TASK ATTENTION:\n" + attention + "\n\n"
        "REQUEST JSON:\n" + json.dumps(bounded, ensure_ascii=False) + "\n\n"
        "PROVISIONAL_UNSCORED_OUTPUT:\n" + json.dumps(provisional, ensure_ascii=False)
    )
    verified = _session(agent_id, verify_prompt, "researcher_inventory_v27_adjudication")
    sys.stdout.write(json.dumps(verified, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
