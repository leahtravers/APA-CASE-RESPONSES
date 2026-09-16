#!/usr/bin/env python3
"""V51 harness-isolated adapter. Durable V51 contract is sole semantic authority."""
from __future__ import annotations

import json
import sys
from pathlib import Path

from openai_agents_adapter import AGENT_ID_FILE
import v32_openai_agents_adapter as recovery

recovery.RECOVERY_DIR = Path("researcher_inventory/runtime/v51_session_recovery")


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
            + " Rebuild the complete requested result under the installed V51 contract; "
              "do not patch only the named field. This is mechanical validation feedback, "
              "not evaluator or gold guidance."
        )
    if bounded.get("task") == "researcher_inventory_extract_one_class":
        return (
            "UNIT PASS. Apply the installed durable V51 contract to the complete source. "
            "First reconstruct the materially distinct role-bearing source propositions, then retain only requested-class units that fill a necessary "
            "class-native role in at least one retained proposition. Class each span by its proposition function rather than part of speech. Recover "
            "source-supported unnamed PLACE/TIME frames when a proposition requires them. Remove support/report/meta predicates, incidental modifiers or "
            "background nouns, temporal/location cues, PP fragments, alternate grains, and other lexical-census items that carry no necessary proposition "
            "role. Run role-omission, role-necessity, and excess/collision passes. Follow response_schema exactly and never infer an expected count or hidden archetype."
            + correction_note
        )
    if bounded.get("task") == "researcher_inventory_build_lightweight_compounds":
        return (
            "COMPOUND PASS. Apply the installed durable V51 contract to the complete source and supplied frozen units. Reconstruct each materially distinct "
            "role-bearing source proposition and emit exactly one smallest COMPLETE compound for it. Include all frozen actor/referent/relation/state/"
            "orientation/place/time refs necessary to reconstruct that proposition, including tightly bound co-predicates or values when they jointly form "
            "the source relation. Do not create or retype units. Do not emit subset alternatives, nested decompositions, sentence-wide supersets, every pair, "
            "or combinatorial variants. qualities_available is quality availability, not a question marker. Follow response_schema exactly and never infer hidden gold."
            + correction_note
        )
    return "Apply the installed durable V51 contract exactly to this bounded request." + correction_note


def main() -> int:
    payload = json.load(sys.stdin)
    agent_id = AGENT_ID_FILE.read_text(encoding="utf-8").strip()
    bounded = _bounded_request(payload)
    attention = _attention_for(bounded)
    core_key = recovery._core_key(bounded)
    state_path, trace_path = recovery._paths(core_key)

    if not bounded.get("correction") and state_path.exists():
        recovery._trace(trace_path, "new_request_supersedes_local_recovery_state", "researcher_inventory_v51_contract_isolated", detail="prior local state preserved in trace; new request starts fresh")
        state_path.unlink()

    initial_prompt = (
        "Execute only this bounded request under your installed durable V51 contract. The durable contract is the sole semantic "
        "selection/grain authority. Return ONLY the JSON value required by response_schema. Do not infer or reconstruct archetypes, "
        "expected answers/counts, evaluator preferences, prior scored outputs, case-specific gold corrections, sealed holdout source, "
        "or holdout output.\n\nTASK ATTENTION:\n" + attention + "\n\nREQUEST JSON:\n" + json.dumps(bounded, ensure_ascii=False)
    )
    try:
        provisional = recovery._session(agent_id, initial_prompt, "researcher_inventory_v51_contract_isolated_extract", state_path, trace_path, "provisional")
        verify_prompt = (
            "Perform a separate adjudication in a new session under the SAME installed durable V51 contract. Re-read the complete source and independently "
            "rebuild the requested result before comparing with the provisional output. Reconstruct the role-bearing proposition map, require every unit to "
            "fill a necessary class-native proposition role, classify by proposition function rather than part of speech, recover required unnamed PLACE/TIME "
            "frames, and remove support/meta/background/census items or alternate grains without a necessary role. For compounds, return one smallest COMPLETE "
            "compound per retained proposition, not smaller subset alternatives or nested variants. Return the complete replacement JSON, not a critique. "
            "Do not infer archetypes, expected counts, evaluator preferences, scored prior output, case-specific gold corrections, sealed holdout source, or "
            "holdout output.\n\nTASK ATTENTION:\n" + attention + "\n\nREQUEST JSON:\n" + json.dumps(bounded, ensure_ascii=False)
            + "\n\nPROVISIONAL_UNSCORED_OUTPUT:\n" + json.dumps(provisional, ensure_ascii=False)
        )
        verified = recovery._session(agent_id, verify_prompt, "researcher_inventory_v51_contract_isolated_adjudication", state_path, trace_path, "verified")
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
