#!/usr/bin/env python3
"""V29 bounded adapter: story/workbook coordinates, then source bindings.

The worker sees only its durable V29 contract, neutral task rules, the bounded
source/request, and one unscored provisional output from another stateless pass.
No archetype, evaluator finding, expected count, scored output, or sealed holdout
material is supplied.
"""
from __future__ import annotations

import json
import os
import sys

from openai_agents_adapter import AGENT_ID_FILE, final_answer, request, wait

SESSION_WAIT_SECONDS = int(os.environ.get("RI_AGENT_SESSION_TIMEOUT_SECONDS", "600"))


def _bounded_request(payload: dict) -> dict:
    keep = {
        "task", "rules", "class", "class_rule", "response_schema", "source",
        "units", "candidate", "researcher_interest", "created_by_ref", "correction",
    }
    return {k: v for k, v in payload.items() if k in keep}


def _attention_for(bounded: dict) -> str:
    if bounded.get("task") == "researcher_inventory_extract_one_class":
        return (
            "UNIT PASS. Read the whole source first. Use BOTH admission gates: positive class fit and an independently selectable story/workbook role. "
            "Preserve full source-grounded coverage, but do not enumerate grammatical or proposition-internal fragments. "
            "Ask whether each candidate would still be a meaningful researcher-selectable coordinate of THIS class if its containing sentence were decomposed no further. "
            "For VERB, use one source-distinguished predicate family per independently selectable story relation: keep auxiliary/control/light/support material together when it jointly expresses one relation, and split nested material only when it independently introduces another story relation. "
            "For PLACE and TIME, retain actual scene/frame coordinates, including legitimate unnamed ones, but not every path, deictic, temporal token, question, or micro-action. "
            "For LOCATOR, require a genuine orienting relation with something being oriented and an anchor; do not promote every prepositional/context phrase. "
            "For OBJECT require a source-treated referent, not a clause merely because it is a complement. For LABEL require an independently selectable characterization, not an ordinary predicate duplicated as a state label. "
            "Allow cross-class overlap only when the material independently performs a story/workbook role in both classes. Preserve exact contiguous wording, posture, coreference, and source order. Never target an expected count."
        )
    if bounded.get("task") == "researcher_inventory_build_lightweight_compounds":
        return (
            "COMPOUND PASS. Units are final. Re-read the source and emit one binding for each independently source-presented proposition/event/state/question/report/reflection/intention/relation that is materially represented by final units. "
            "Use all and only participating refs in source/semantic order. Do not create or repair units here, make sentence-wide graphs, emit arbitrary subsets/every recombination, or duplicate a nested subset unless the source separately presents both bindings."
        )
    return "Apply the installed V29 durable contract exactly to this bounded request."


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
    wait(session_id, timeout=SESSION_WAIT_SECONDS)
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
        "Execute only this bounded request under your installed durable V29 contract and supplied neutral apparatus rules. "
        "Return ONLY the JSON value required by response_schema. Do not infer or reconstruct any archetype, expected answer, expected count, evaluator preference, prior scored output, sealed holdout source, or holdout output.\n\n"
        "TASK ATTENTION:\n" + attention + "\n\n"
        "REQUEST JSON:\n" + json.dumps(bounded, ensure_ascii=False)
    )
    provisional = _session(agent_id, initial_prompt, "researcher_inventory_v29_extract")

    verify_prompt = (
        "Perform a separate stateless V29 adjudication. Re-read the complete source and independently rebuild the requested result BEFORE comparing with the provisional output. "
        "Use this order: (1) COVERAGE — find every candidate genuinely doing THIS class job; "
        "(2) STORY ROLE — keep only candidates that remain independently selectable story/workbook coordinates rather than grammatical/proposition-internal fragments; "
        "(3) GRAIN — merge support pieces expressing one coordinate and split only independently represented coordinates; "
        "(4) CROSS-CLASS CHECK — overlap only for independently selectable class-specific roles; "
        "(5) REPAIR — add genuine omissions, remove debris/duplicates/inferences, and preserve exact source wording, posture, coreference and order. "
        "For VERB, rebuild predicate families rather than either full propositions or grammatical predicate fragments. For PLACE/TIME require real scene/frame roles. For LOCATOR require an orienting relation with an anchor. For OBJECT require a source-treated referent. For LABEL require a source-applied characterization. "
        "Do not target a count. Return the complete replacement JSON, not a critique.\n\n"
        "TASK ATTENTION:\n" + attention + "\n\n"
        "REQUEST JSON:\n" + json.dumps(bounded, ensure_ascii=False) + "\n\n"
        "PROVISIONAL_UNSCORED_OUTPUT:\n" + json.dumps(provisional, ensure_ascii=False)
    )
    verified = _session(agent_id, verify_prompt, "researcher_inventory_v29_adjudication")
    sys.stdout.write(json.dumps(verified, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
