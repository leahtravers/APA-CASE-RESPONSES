#!/usr/bin/env python3
"""V49 harness-isolated adapter. Durable V49 contract is sole semantic authority."""
from __future__ import annotations

import json
import sys
from pathlib import Path

from openai_agents_adapter import AGENT_ID_FILE
import v32_openai_agents_adapter as recovery

recovery.RECOVERY_DIR = Path("researcher_inventory/runtime/v49_session_recovery")


def _bounded_request(payload: dict) -> dict:
    bounded = recovery._bounded_request(payload)
    bounded.pop("rules", None)
    bounded.pop("class_rule", None)
    return bounded


def _attention_for(bounded: dict) -> str:
    correction = recovery._mechanical_correction(bounded.get("correction"))
    correction_note = ""
    if correction:
        correction_note = (
            "\nMECHANICAL VALIDATOR CORRECTION FROM THE PRIOR UNSCORED ATTEMPT: "
            + correction
            + " Rebuild the complete requested result under the installed V49 contract; "
              "do not patch only the named field. This is mechanical validation feedback, "
              "not evaluator or gold guidance."
        )
    if bounded.get("task") == "researcher_inventory_extract_one_class":
        return (
            "UNIT PASS. Apply the installed durable V49 contract to the complete source. "
            "Build the whole-source research-role map before selecting the requested class. Resolve scene/occurrence-position roles, episode/period "
            "frames, people, source-treated referents, source-native relation spans, characterization values, and orientation/context relations. "
            "Select distinct RESEARCH ROLES rather than grammatical atoms. Preserve supported unnamed scene/time roles, local/relational/figurative "
            "roles, and genuine cross-class second functions; merge only true coreference or same-role restatements. Do not create proposition wrappers, "
            "lexical-census rows, umbrella time frames the source does not distinguish, every-physical-noun PLACE rows, every-PP LOCATOR rows, or "
            "dictionary-head VERB fragments. For VERB preserve the smallest source-native relation span that remains recognizable, including "
            "relation-bearing multiword structure, particles, reflexives, or pronoun/complement material when needed. For LABEL preserve distinct "
            "source-presented characterization values regardless of part of speech. Run role-coverage and excess passes. Follow response_schema exactly "
            "and never infer expected counts or hidden archetypes."
            + correction_note
        )
    if bounded.get("task") == "researcher_inventory_build_lightweight_compounds":
        return (
            "COMPOUND PASS. Apply the installed durable V49 contract to the complete source and supplied frozen units. Reconstruct materially distinct "
            "source-presented RELATION PROPOSITIONS at research scene/event grain. Emit one smallest-complete compound per represented relation instance: "
            "carrier/participant, operative predicate or characterization/orientation carrier, connected participants/referents, then only the retained "
            "LABEL/TIME/PLACE/LOCATOR anchors actually used to establish, qualify, situate, or orient that relation. Distinct reporting/carrier and "
            "embedded/content relations may both survive when separately represented. Do not create/retype units, emit every pair, combinatorial subsets, "
            "broad sentence bundles, nested variants, or alternate decompositions. qualities_available is quality availability, not a question marker. "
            "Follow response_schema exactly and never infer hidden gold."
            + correction_note
        )
    return "Apply the installed durable V49 contract exactly to this bounded request." + correction_note


def main() -> int:
    payload = json.load(sys.stdin)
    agent_id = AGENT_ID_FILE.read_text(encoding="utf-8").strip()
    bounded = _bounded_request(payload)
    attention = _attention_for(bounded)
    core_key = recovery._core_key(bounded)
    state_path, trace_path = recovery._paths(core_key)

    if not bounded.get("correction") and state_path.exists():
        recovery._trace(trace_path, "new_request_supersedes_local_recovery_state", "researcher_inventory_v49_contract_isolated", detail="prior local state preserved in trace; new request starts fresh")
        state_path.unlink()

    initial_prompt = (
        "Execute only this bounded request under your installed durable V49 contract. The durable contract is the sole semantic "
        "selection/grain authority. Return ONLY the JSON value required by response_schema. Do not infer or reconstruct archetypes, "
        "expected answers/counts, evaluator preferences, prior scored outputs, case-specific gold corrections, sealed holdout source, "
        "or holdout output.\n\nTASK ATTENTION:\n" + attention + "\n\nREQUEST JSON:\n" + json.dumps(bounded, ensure_ascii=False)
    )
    try:
        provisional = recovery._session(agent_id, initial_prompt, "researcher_inventory_v49_contract_isolated_extract", state_path, trace_path, "provisional")
        verify_prompt = (
            "Perform a separate adjudication in a new session under the SAME installed durable V49 contract. Re-read the complete source and independently "
            "rebuild the requested result before comparing with the provisional output. Reconstruct the research-role map and check role coverage versus "
            "grammatical inflation. Preserve supported unnamed scene/time roles and source-native relation spans; reject proposition wrappers, cue/action "
            "inflation, every-PP behavior, dictionary-head fragmentation, and unjustified class duplication. Return the complete replacement JSON, not a "
            "critique. Do not infer or reconstruct archetypes, expected counts, evaluator preferences, scored prior output, case-specific gold corrections, "
            "sealed holdout source, or holdout output.\n\nTASK ATTENTION:\n" + attention + "\n\nREQUEST JSON:\n" + json.dumps(bounded, ensure_ascii=False)
            + "\n\nPROVISIONAL_UNSCORED_OUTPUT:\n" + json.dumps(provisional, ensure_ascii=False)
        )
        verified = recovery._session(agent_id, verify_prompt, "researcher_inventory_v49_contract_isolated_adjudication", state_path, trace_path, "verified")
    except recovery.SessionUncertain:
        raise
    except Exception:
        if state_path.exists():
            state_path.unlink()
        raise
    if state_path.exists():
        state_path.unlink()
    sys.stdout.write(json.dumps(verified, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
