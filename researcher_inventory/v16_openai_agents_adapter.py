#!/usr/bin/env python3
"""V16 bounded adapter with deletion-biased independent verification.

The worker sees only the durable V16 contract, bounded request, source, and one
unscored provisional output from another stateless pass under the same contract.
No archetype, evaluator finding, expected count, scored output, or holdout output
is ever supplied to the worker.
"""
from __future__ import annotations

import json
import sys

from openai_agents_adapter import AGENT_ID_FILE, final_answer, request, wait


CLASS_ATTENTION = {
    "PLACE": (
        "Build scene/site/occurrence-position handles only. Do not turn every surface, path, distance, spatial phrase, movement phrase, or object-support relation into PLACE. "
        "Unnamed places are allowed when a materially distinct represented occurrence needs a where handle. A distinct movement destination may be unnamed when the destination site is necessarily represented."
    ),
    "TIME": (
        "Build reusable episode/span/frame handles only. Do not turn every action, tense, frequency word, duration phrase, subordinate temporal phrase, or duration question into TIME. "
        "Merge dependent substeps into their containing episode; retain an unnamed frame when a materially distinct occurrence still needs a when handle."
    ),
    "PERSON": (
        "Resolve aliases, pronouns, stable groups, and participation before counting. Keep represented actors/endpoints, not generic audiences or grammatical person mentions."
    ),
    "OBJECT": (
        "Keep particular or reusable referents that do a material source job. Do not inventory every noun phrase, generic filler, quantifier, complement, nominalized proposition, or descriptive abstraction. "
        "A part survives separately only when the source materially treats it as its own referent."
    ),
    "LABEL": (
        "Keep source-applied reusable characterizations only. Do not duplicate a predicate state, locator, intensifier, or stance wrapper as LABEL unless the wording independently functions as a characterization."
    ),
    "VERB": (
        "Inventory source-level predicate relations, not verb tokens. Default to one row for one relation. Keep support/control/complement/multiword material together when splitting would leave non-independent fragments. "
        "Split only when each piece is a different independently selectable relation."
    ),
    "LOCATOR": (
        "Keep independently useful position/path/direction/containment/context relations at the smallest complete source grain. Do not convert routine argument marking, possession, topic, comparison support, or an isolated preposition into a locator."
    ),
}

COMPOUND_ATTENTION = (
    "Build a lightweight reassembly spine, not an exhaustive clause list. Create one compound for one materially distinct represented proposition or situation when binding retained units is useful later. "
    "Prefer a single source-level proposition over grammatical fragments or multiple overlapping recombinations. Do not create compounds merely because units exist."
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
            "Use the V16 universal retention gate. Read the entire source. First identify materially represented situations, then propose only class-local independent coordinates. "
            "Run omission and excess passes. The excess pass is mandatory: remove grammatical debris, duplicate framing, support detail, and candidates whose job is already carried by another coordinate/Q/compound. "
            "When a separate coordinate is doubtful, omit it. Do not substitute synonyms or invent qualifications. "
            + CLASS_ATTENTION.get(cls, "")
        )
    if task == "researcher_inventory_build_lightweight_compounds":
        return COMPOUND_ATTENTION
    return "Apply the installed V16 durable contract exactly to this bounded task."


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
        "Execute only this bounded request under your installed durable V16 contract. Return ONLY the JSON value required by response_schema. "
        "Do not infer or reconstruct any archetype, expected answer, expected count, evaluator preference, prior scored output, or holdout content.\n\n"
        "TASK ATTENTION:\n" + attention + "\n\n"
        "REQUEST JSON:\n" + json.dumps(bounded, ensure_ascii=False)
    )
    provisional = _session(agent_id, initial_prompt, "researcher_inventory_v16_initial")

    verify_prompt = (
        "Perform a separate stateless verification under your installed durable V16 contract. The provisional output is unscored and non-authoritative. "
        "Re-read the entire source and rebuild the requested result from the contract. Use the provisional only to notice possible omissions or excess. "
        "The verification pass is deletion-biased: every row must independently pass the retention gate; merge competing rows that do the same class job; delete grammatical/support/detail rows; add a row only when a materially distinct class job is clearly lost without it. "
        "When uncertain whether a separate row is warranted, omit it. Preserve exact source language and posture. Return ONLY the complete replacement JSON required by response_schema.\n\n"
        "TASK ATTENTION:\n" + attention + "\n\n"
        "REQUEST JSON:\n" + json.dumps(bounded, ensure_ascii=False) + "\n\n"
        "PROVISIONAL_UNSCORED_OUTPUT:\n" + json.dumps(provisional, ensure_ascii=False)
    )
    verified = _session(agent_id, verify_prompt, "researcher_inventory_v16_verification")
    sys.stdout.write(json.dumps(verified, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
