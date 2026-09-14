#!/usr/bin/env python3
"""V23 bounded adapter with mechanical enumeration and exact-source verification.

The worker sees only its installed durable V23 contract, neutral apparatus rules, the
bounded source/request, and one unscored provisional output from another stateless
pass under the same contract. No archetype, evaluator finding, expected count,
scored output, or sealed holdout material is supplied.
"""
from __future__ import annotations

import json
import sys

from openai_agents_adapter import AGENT_ID_FILE, final_answer, request, wait


CLASS_ATTENTION = {
    "PLACE": (
        "Scan source order for every distinct represented where-coordinate. Preserve broad and contained settings, distinct scene positions, unnamed scene slots, origins/destinations, interaction/waiting positions, later-report/conversation settings, and present-telling settings when actually represented. Do not require a named place and do not suppress a valid local place because another PLACE or LOCATOR already exists."
    ),
    "TIME": (
        "Scan source progression for every distinct represented episode/frame/span/recurrence/prospective frame. Preserve genuine subepisodes and posture shifts without mechanically making one TIME per verb. Unnamed frames are allowed with source_wording null and exact source cues."
    ),
    "PERSON": (
        "Inventory the speaker and every represented person/stable human group participating in or anchoring represented relations. Resolve aliases/coreference before same-class deduplication."
    ),
    "OBJECT": (
        "Inventory represented referable things, including concrete, abstract, internal, figurative, values, parts/wholes, decisions/choices, sets, and reified relations when the source treats them as things. Do not nominalize every clause or predicate into an object."
    ),
    "LABEL": (
        "Inventory source-applied characterizations rather than every predicate. Preserve qualities, states, identities, evaluations, comparisons, corrections, rejections, and characterization questions. SOURCE-SPAN LOCK is strict: choose an actual contiguous phrase from source; never reconstruct a cleaner phrase by omitting internal words."
    ),
    "VERB": (
        "Inventory each distinct represented lexical action/relation edge at small source-near grain. Preserve nested/embedded/reported/thought/perception/state/purpose/negated/questioned/intended/recurring/future edges when each contributes its own relation. Exclude only auxiliaries/support/connectors with no relation edge of their own."
    ),
    "LOCATOR": (
        "Inventory represented locating/context relations at small meaningful grain: setting, position, path, direction, origin/destination, containment/proximity, movement, participant-relative accompaniment/association, recurring context, and genuine figurative/mental location. Do not suppress a valid LOCATOR merely because the same wording also supports PLACE, TIME, VERB, or LABEL."
    ),
}

COMPOUND_ATTENTION = (
    "Build compounds only after units are final. Map the source at distinct proposition/relation grain: action/relation propositions, characterization propositions, questions, corrections, comparisons, reflections, and prospective relations. Use only supplied unit_ref values. Include all retained units that actually participate in the proposition. Include a retained PLACE/TIME/LOCATOR only when it governs or locates that proposition. Do not create arbitrary subset variants or use compounds to repair missing units."
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
            "MECHANICAL PASS. Read the whole source first. Then scan it from beginning to end and build a ledger of every represented coordinate that performs the requested class's positive job. "
            "There is NO additional importance, salience, researcher-selectability, reconnective-value, or material-loss gate. Do not remove a valid row merely because it is local, ordinary, unnamed, nested, or overlaps another class. "
            "Do not add a row merely because grammar makes a class interpretation possible; the coordinate must actually be represented doing the class job. "
            "SOURCE-SPAN LOCK. For every explicit candidate, select source_wording by copying one exact contiguous substring from the source before writing the short tag. source_cue must also be one exact contiguous substring. Never splice or paraphrase. Only unnamed PLACE/TIME may use null source_wording. "
            "DEDUPE ONLY after the ledger is complete: merge aliases/coreference and true same-class duplicates; remove unsupported invention and grammatical debris. Do not merge different coordinates merely because they share a scene, sentence, time, or proposition. "
            "ORDER by earliest represented-coordinate anchor after coreference resolution. "
            + CLASS_ATTENTION.get(cls, "")
        )
    if task == "researcher_inventory_build_lightweight_compounds":
        return COMPOUND_ATTENTION
    return "Apply the installed V23 durable contract and supplied neutral apparatus rules exactly to this bounded task."


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
        "Execute only this bounded request under your installed durable V23 contract and supplied neutral apparatus rules. Return ONLY the JSON value required by response_schema. Do not infer or reconstruct any archetype, expected answer, expected count, evaluator preference, prior scored output, sealed holdout source, or holdout output.\n\n"
        "TASK ATTENTION:\n" + attention + "\n\n"
        "REQUEST JSON:\n" + json.dumps(bounded, ensure_ascii=False)
    )
    provisional = _session(agent_id, initial_prompt, "researcher_inventory_v23_initial")

    verify_prompt = (
        "Perform a separate stateless V23 verification. The provisional output is unscored and non-authoritative. Re-read the complete source and independently rebuild the requested result from the durable contract before comparing it with the provisional output. "
        "FIRST make your own source-order ledger of every represented member of the requested class. Apply only the class positive job, source grounding, true same-class deduplication, and grammatical-debris/invention exclusions. Do NOT apply an importance/salience/reconnective/material-loss test. "
        "SECOND enforce SOURCE-SPAN LOCK on every explicit row: source_wording and source_cue must each be exact contiguous source substrings; never splice or paraphrase. "
        "THIRD resolve aliases/coreference and remove only true same-class duplicates, unsupported invention, or grammatical debris. Preserve valid local, unnamed, nested, and cross-class-overlapping coordinates. "
        "FOURTH compare your independently rebuilt ledger with the provisional output, recover any omissions, and correct any extras or source-copy errors. Ignore the provisional row count. "
        "Return ONLY the complete replacement JSON required by response_schema.\n\n"
        "TASK ATTENTION:\n" + attention + "\n\n"
        "REQUEST JSON:\n" + json.dumps(bounded, ensure_ascii=False) + "\n\n"
        "PROVISIONAL_UNSCORED_OUTPUT:\n" + json.dumps(provisional, ensure_ascii=False)
    )
    verified = _session(agent_id, verify_prompt, "researcher_inventory_v23_verification")
    sys.stdout.write(json.dumps(verified, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
