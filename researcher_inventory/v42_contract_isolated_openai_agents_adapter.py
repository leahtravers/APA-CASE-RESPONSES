#!/usr/bin/env python3
"""V42 harness-isolated adapter. Durable V42 contract is sole semantic authority."""
from __future__ import annotations

import json
import sys
from pathlib import Path

from openai_agents_adapter import AGENT_ID_FILE
import v32_openai_agents_adapter as recovery

recovery.RECOVERY_DIR = Path("researcher_inventory/runtime/v42_contract_isolated_session_recovery")


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
            + " Rebuild the complete requested result under the installed V42 contract; "
              "do not patch only the named field. This is mechanical validation feedback, "
              "not evaluator or gold guidance."
        )
    if bounded.get("task") == "researcher_inventory_extract_one_class":
        return (
            "UNIT PASS. Apply the installed durable V42 contract to the complete source. "
            "Reconstruct the lightweight frame skeleton and research-bearing binding ledger before selecting "
            "the requested class. Apply the local-contribution test at natural complete class grain. "
            "Do not turn explicit wording into a lexical/grammar census and do not require global indispensability. "
            "For explicitly worded coordinates, short_tag may use only words present in source_wording/source_cue. "
            "Follow response_schema exactly. Do not infer an expected count or hidden archetype."
            + correction_note
        )
    if bounded.get("task") == "researcher_inventory_build_lightweight_compounds":
        return (
            "COMPOUND PASS. Apply the installed durable V42 contract to the complete source and supplied frozen "
            "units. Reconstruct the frame skeleton and distinct lightweight research-bearing bindings, then "
            "serialize only bindings that preserve a separate source relation/characterization/episode. Do not "
            "emit every clause, subset, nested restatement, or co-occurrence. Do not create, suppress, merge, or "
            "repair units. Follow response_schema exactly. Do not infer an expected count or hidden archetype."
            + correction_note
        )
    return "Apply the installed durable V42 contract exactly to this bounded request." + correction_note


def main() -> int:
    payload = json.load(sys.stdin)
    agent_id = AGENT_ID_FILE.read_text(encoding="utf-8").strip()
    bounded = _bounded_request(payload)
    attention = _attention_for(bounded)
    core_key = recovery._core_key(bounded)
    state_path, trace_path = recovery._paths(core_key)

    if not bounded.get("correction") and state_path.exists():
        recovery._trace(trace_path, "new_request_supersedes_local_recovery_state", "researcher_inventory_v42_contract_isolated", detail="prior local state preserved in trace; new request starts fresh")
        state_path.unlink()

    initial_prompt = (
        "Execute only this bounded request under your installed durable V42 contract. The durable contract is "
        "the sole semantic selection/grain authority. Return ONLY the JSON value required by response_schema. "
        "Do not infer or reconstruct archetypes, expected answers/counts, evaluator preferences, prior scored "
        "outputs, case-specific gold corrections, sealed holdout source, or holdout output.\n\nTASK ATTENTION:\n"
        + attention + "\n\nREQUEST JSON:\n" + json.dumps(bounded, ensure_ascii=False)
    )
    try:
        provisional = recovery._session(agent_id, initial_prompt, "researcher_inventory_v42_contract_isolated_extract", state_path, trace_path, "provisional")
        verify_prompt = (
            "Perform a separate adjudication in a new session under the SAME installed durable V42 contract. "
            "Re-read the complete source and independently rebuild the requested result before comparing with "
            "the provisional output. Reconstruct the lightweight frame skeleton and research-bearing binding "
            "ledger, apply the local-contribution test at natural complete class grain, and prune semantic/grammar "
            "census residue. Return the complete replacement JSON, not a critique. Do not infer or reconstruct "
            "archetypes, expected counts, evaluator preferences, scored prior output, case-specific gold corrections, "
            "sealed holdout source, or holdout output.\n\nTASK ATTENTION:\n"
            + attention + "\n\nREQUEST JSON:\n" + json.dumps(bounded, ensure_ascii=False)
            + "\n\nPROVISIONAL_UNSCORED_OUTPUT:\n" + json.dumps(provisional, ensure_ascii=False)
        )
        verified = recovery._session(agent_id, verify_prompt, "researcher_inventory_v42_contract_isolated_adjudication", state_path, trace_path, "verified")
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
