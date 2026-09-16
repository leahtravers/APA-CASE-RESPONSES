#!/usr/bin/env python3
"""V50 harness-isolated adapter. Durable V50 contract is sole semantic authority."""
from __future__ import annotations

import json
import sys
from pathlib import Path

from openai_agents_adapter import AGENT_ID_FILE
import v32_openai_agents_adapter as recovery

recovery.RECOVERY_DIR = Path("researcher_inventory/runtime/v50_session_recovery")


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
            + " Rebuild the complete requested result under the installed V50 contract; "
              "do not patch only the named field. This is mechanical validation feedback, "
              "not evaluator or gold guidance."
        )
    if bounded.get("task") == "researcher_inventory_extract_one_class":
        return (
            "UNIT PASS. Apply the installed durable V50 contract to the complete source. "
            "Build the whole-source coverage map, but never treat map membership as unit entitlement. Apply class-native admission to every candidate. "
            "For any larger phrase and possible child span, use the two-gate rule: retain the child only if it independently passes the requested class, "
            "and retain parent plus child only if they perform genuinely distinct research roles. Prefer represented scenes/episode frames over literal "
            "location/time words; source-treated referents over noun census; independent characterization values over modifiers/predicate complements; "
            "shortest complete lexical predicate kernels over clause-sized relations; and independent orientation relations over every PP. Run omission, "
            "independence, and excess passes. Follow response_schema exactly and never infer an expected count or hidden archetype."
            + correction_note
        )
    if bounded.get("task") == "researcher_inventory_build_lightweight_compounds":
        return (
            "COMPOUND PASS. Apply the installed durable V50 contract to the complete source and supplied frozen units. Reconstruct materially distinct "
            "source-presented relation instances and emit one smallest-complete compound per representable relation. Include only the operative relation/"
            "classification/orientation, actual participants/referents, and retained PLACE/TIME/LOCATOR/LABEL anchors used by that relation. Do not create "
            "or retype units, emit every pair, combinatorial subsets, broad sentence bundles, parent/child alternate decompositions, or compounds whose "
            "apparent completeness depends on redundant units. qualities_available is quality availability, not a question marker. Follow response_schema "
            "exactly and never infer hidden gold."
            + correction_note
        )
    return "Apply the installed durable V50 contract exactly to this bounded request." + correction_note


def main() -> int:
    payload = json.load(sys.stdin)
    agent_id = AGENT_ID_FILE.read_text(encoding="utf-8").strip()
    bounded = _bounded_request(payload)
    attention = _attention_for(bounded)
    core_key = recovery._core_key(bounded)
    state_path, trace_path = recovery._paths(core_key)

    if not bounded.get("correction") and state_path.exists():
        recovery._trace(trace_path, "new_request_supersedes_local_recovery_state", "researcher_inventory_v50_contract_isolated", detail="prior local state preserved in trace; new request starts fresh")
        state_path.unlink()

    initial_prompt = (
        "Execute only this bounded request under your installed durable V50 contract. The durable contract is the sole semantic "
        "selection/grain authority. Return ONLY the JSON value required by response_schema. Do not infer or reconstruct archetypes, "
        "expected answers/counts, evaluator preferences, prior scored outputs, case-specific gold corrections, sealed holdout source, "
        "or holdout output.\n\nTASK ATTENTION:\n" + attention + "\n\nREQUEST JSON:\n" + json.dumps(bounded, ensure_ascii=False)
    )
    try:
        provisional = recovery._session(agent_id, initial_prompt, "researcher_inventory_v50_contract_isolated_extract", state_path, trace_path, "provisional")
        verify_prompt = (
            "Perform a separate adjudication in a new session under the SAME installed durable V50 contract. Re-read the complete source and independently "
            "rebuild the requested result before comparing with the provisional output. Use the whole-source map only for coverage/duplicate detection. "
            "Apply class-native admission to every unit; test child spans independently rather than atomizing parent phrases; reject parent/child duplicate "
            "grains, lexical-census inflation, clause-sized predicate wrappers, physical-noun PLACE inflation, temporal-cue TIME inflation, every-PP behavior, "
            "and unjustified class duplication. Also recover supported unnamed scene/episode roles and other independently selectable local/nested roles. "
            "Return the complete replacement JSON, not a critique. Do not infer archetypes, expected counts, evaluator preferences, scored prior output, "
            "case-specific gold corrections, sealed holdout source, or holdout output.\n\nTASK ATTENTION:\n" + attention + "\n\nREQUEST JSON:\n" + json.dumps(bounded, ensure_ascii=False)
            + "\n\nPROVISIONAL_UNSCORED_OUTPUT:\n" + json.dumps(provisional, ensure_ascii=False)
        )
        verified = recovery._session(agent_id, verify_prompt, "researcher_inventory_v50_contract_isolated_adjudication", state_path, trace_path, "verified")
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
