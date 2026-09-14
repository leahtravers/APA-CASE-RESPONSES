#!/usr/bin/env python3
"""V30 bounded adapter: source-distinguished semantic coordinates, then bindings.

The worker sees only its durable V30 contract, neutral task rules, the bounded
source/request, and one unscored provisional output from another session. No
archetype, evaluator finding, expected count, scored output, case-specific
correction example, or sealed holdout material is supplied.
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
            "UNIT PASS. Read the whole source first. Inventory the smallest COMPLETE SOURCE-DISTINGUISHED SEMANTIC COORDINATES of THIS class. "
            "Do not require a coordinate to be proposition-sized, summary-worthy, or independently tellable as a whole story fact; a small coordinate qualifies when the source distinguishes a real semantic job for THIS class. "
            "Also do not atomize grammar: articles, bare auxiliaries/copulas/support fragments, generic wrappers, duplicated aliases, and proposition-internal pieces with no separate semantic job are not units. "
            "Use this sequence: coverage -> positive class function -> minimal complete grain -> reject grammar/reification -> coreference/duplicates -> exact span/order. "
            "For VERB, extract minimal complete relation edges and split nested/coordinated/report/perception/purpose/control constructions when they contain genuinely distinct represented edges; do not collapse several edges into one predicate family and do not split support words from one edge. "
            "For PLACE and TIME, retain source-established scene-positions and event/frame phases, including legitimate unnamed coordinates; a distinct deictic position or event phase may qualify when it actually establishes where/when represented material occurs. "
            "For OBJECT require a source-treated referent and reject mere clause/predicate/proposition nominalization. For LABEL require source-applied characterization, including brief qualified/corrective/questioned formulations, not ordinary actions restated as states. "
            "For LOCATOR retain a source-distinguished orientation/context relation, including path/movement/context when orientation itself is represented; do not promote every prepositional phrase. "
            "Allow cross-class overlap only for genuine distinct positive functions. Preserve exact contiguous wording, posture, coreference, and first-establishment order. Never target an expected count."
        )
    if bounded.get("task") == "researcher_inventory_build_lightweight_compounds":
        return (
            "COMPOUND PASS. Units are final. Re-read the source and identify each SOURCE-PRESENTED BINDING: proposition/event/state/question/report/reflection/intention/characterization/relation cluster presented together. "
            "For each binding use all and only final units materially participating, in source/semantic order. Multiple VERB refs may belong in one binding when the source presents their edges as one event cluster. Make separate compounds only for separately presented bindings. "
            "Do not create/repair units here, hide missing units in larger compounds, graph every sentence, emit arbitrary subsets/every recombination, or duplicate nested subsets unless separately source-presented."
        )
    return "Apply the installed V30 durable contract exactly to this bounded request."


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
        "Execute only this bounded request under your installed durable V30 contract and supplied neutral apparatus rules. "
        "Return ONLY the JSON value required by response_schema. Do not infer or reconstruct any archetype, expected answer, expected count, evaluator preference, prior scored output, case-specific correction, sealed holdout source, or holdout output.\n\n"
        "TASK ATTENTION:\n" + attention + "\n\n"
        "REQUEST JSON:\n" + json.dumps(bounded, ensure_ascii=False)
    )
    provisional = _session(agent_id, initial_prompt, "researcher_inventory_v30_extract")

    verify_prompt = (
        "Perform a separate V30 adjudication in a new session. Re-read the complete source and independently rebuild the requested result BEFORE comparing with the provisional output. "
        "Use this order: (1) COVERAGE — find every source-distinguished candidate genuinely doing THIS class job; "
        "(2) POSITIVE FUNCTION — state internally what class job each candidate performs; "
        "(3) MINIMAL COMPLETE GRAIN — split genuinely distinct semantic coordinates even when nested, but keep required words of one coordinate together; "
        "(4) ANTI-DEBRIS/ANTI-REIFICATION — remove grammar-only fragments, aliases, unsupported nominalizations, proposition-sized substitute rows, and class-parallel copies without a distinct positive job; "
        "(5) LITERAL/ORDER — preserve exact source wording/posture, coreference, and first referential establishment; "
        "(6) REPAIR — add genuine omissions and remove only demonstrated debris/inference/duplicates. "
        "For VERB rebuild minimal relation edges rather than broad predicate families or token fragments. For PLACE/TIME require source-established scene-position/frame coordinates, including legitimate unnamed ones. For OBJECT require source-treated referents rather than mere nominalized clauses. For LABEL require source-applied characterization. For LOCATOR require represented orientation/context. "
        "Do not target a count. Return the complete replacement JSON, not a critique.\n\n"
        "TASK ATTENTION:\n" + attention + "\n\n"
        "REQUEST JSON:\n" + json.dumps(bounded, ensure_ascii=False) + "\n\n"
        "PROVISIONAL_UNSCORED_OUTPUT:\n" + json.dumps(provisional, ensure_ascii=False)
    )
    verified = _session(agent_id, verify_prompt, "researcher_inventory_v30_adjudication")
    sys.stdout.write(json.dumps(verified, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
