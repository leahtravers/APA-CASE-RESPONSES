#!/usr/bin/env python3
"""V48 harness-isolated adapter. Durable V48 contract is sole semantic authority."""
from __future__ import annotations

import json
import sys
from pathlib import Path

from openai_agents_adapter import AGENT_ID_FILE
import v32_openai_agents_adapter as recovery

recovery.RECOVERY_DIR = Path("researcher_inventory/runtime/v48_session_recovery")


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
            + " Rebuild the complete requested result under the installed V48 contract; "
              "do not patch only the named field. This is mechanical validation feedback, "
              "not evaluator or gold guidance."
        )
    if bounded.get("task") == "researcher_inventory_extract_one_class":
        return (
            "UNIT PASS. Apply the installed durable V48 contract to the complete source. "
            "First reconstruct the whole-source scene/time, person, referent/content, lexical-predicate, characterization, and orientation maps. "
            "Then select only CLASS-NATIVE RESEARCH COORDINATES at the shortest complete source-native grain. Do not require a coordinate to be "
            "globally indispensable to a larger binding, but do not turn explicit/separable wording into a lexical census. Preserve local, nested, "
            "one-use, unnamed PLACE/TIME, and embedded coordinates when they independently satisfy the requested class. For VERB prefer lexical "
            "predicate kernels rather than clause wrappers; for LOCATOR retain complete orientation relations rather than every PP; for PLACE/TIME "
            "distinguish actual scene/episode anchors from physical nouns or temporal cues; for LABEL require an independently presented "
            "characterization rather than every modifier. Allow cross-class overlap only for genuinely distinct class functions. Run both omission "
            "and excess passes. Follow response_schema exactly and never infer an expected count or hidden archetype."
            + correction_note
        )
    if bounded.get("task") == "researcher_inventory_build_lightweight_compounds":
        return (
            "COMPOUND PASS. Apply the installed durable V48 contract to the complete source and supplied frozen units. "
            "Rebuild materially distinct source-presented relation instances, then emit one smallest-complete compound for each representable "
            "predicate relation, characterization proposition, question/correction/reflection relation, prospective/intended relation, or orientation "
            "relation. Include only the frozen participants/referents and situating or qualifying PLACE/TIME/LOCATOR/LABEL coordinates used by that "
            "relation. Distinct carrier/reporting and embedded/content relations may both survive when genuinely separate. Do not create or retype "
            "units, emit combinatorial subsets, every pair, every sentence, mere co-occurrence bundles, nested variants of one relation, or alternate "
            "decompositions of the same relation. qualities_available is quality availability, not a question marker. Follow response_schema exactly; "
            "do not infer hidden gold."
            + correction_note
        )
    return "Apply the installed durable V48 contract exactly to this bounded request." + correction_note


def main() -> int:
    payload = json.load(sys.stdin)
    agent_id = AGENT_ID_FILE.read_text(encoding="utf-8").strip()
    bounded = _bounded_request(payload)
    attention = _attention_for(bounded)
    core_key = recovery._core_key(bounded)
    state_path, trace_path = recovery._paths(core_key)

    if not bounded.get("correction") and state_path.exists():
        recovery._trace(trace_path, "new_request_supersedes_local_recovery_state", "researcher_inventory_v48_contract_isolated", detail="prior local state preserved in trace; new request starts fresh")
        state_path.unlink()

    initial_prompt = (
        "Execute only this bounded request under your installed durable V48 contract. The durable contract is the sole semantic "
        "selection/grain authority. Return ONLY the JSON value required by response_schema. Do not infer or reconstruct archetypes, "
        "expected answers/counts, evaluator preferences, prior scored outputs, case-specific gold corrections, sealed holdout source, "
        "or holdout output.\n\nTASK ATTENTION:\n" + attention + "\n\nREQUEST JSON:\n" + json.dumps(bounded, ensure_ascii=False)
    )
    try:
        provisional = recovery._session(agent_id, initial_prompt, "researcher_inventory_v48_contract_isolated_extract", state_path, trace_path, "provisional")
        verify_prompt = (
            "Perform a separate adjudication in a new session under the SAME installed durable V48 contract. Re-read the complete source and "
            "independently rebuild the requested result before comparing with the provisional output. Reconstruct the whole-source coordinate maps; "
            "apply class-native admission at the shortest complete source-native grain; check both compression errors and lexical-census inflation; "
            "for VERB prefer lexical kernels over proposition wrappers; for PLACE/TIME require actual scene/episode roles; for LOCATOR require complete "
            "orientation relations; for LABEL require independently presented characterization roles; allow cross-class overlap only for different "
            "class-native functions. Return the complete replacement JSON, not a critique. Do not infer or reconstruct archetypes, expected counts, "
            "evaluator preferences, scored prior output, case-specific gold corrections, sealed holdout source, or holdout output.\n\nTASK ATTENTION:\n"
            + attention + "\n\nREQUEST JSON:\n" + json.dumps(bounded, ensure_ascii=False)
            + "\n\nPROVISIONAL_UNSCORED_OUTPUT:\n" + json.dumps(provisional, ensure_ascii=False)
        )
        verified = recovery._session(agent_id, verify_prompt, "researcher_inventory_v48_contract_isolated_adjudication", state_path, trace_path, "verified")
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
