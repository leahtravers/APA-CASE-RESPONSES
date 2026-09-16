#!/usr/bin/env python3
"""V52 harness-isolated adapter. Durable V52 contract is sole semantic authority."""
from __future__ import annotations

import json
import sys
from pathlib import Path

from openai_agents_adapter import AGENT_ID_FILE
import v32_openai_agents_adapter as recovery

recovery.RECOVERY_DIR = Path("researcher_inventory/runtime/v52_session_recovery")


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
            + " Rebuild the complete requested result under the installed V52 contract; "
              "do not patch only the named field. This is mechanical validation feedback, "
              "not evaluator or gold guidance."
        )
    if bounded.get("task") == "researcher_inventory_extract_one_class":
        return (
            "UNIT PASS. Apply the installed durable V52 contract to the complete source. "
            "Unit admission is SOURCE-COORDINATE based, not proposition-necessity based. Begin with a complete coverage pass for the requested class, "
            "including local, low-salience, background, nested, reported, descriptive, scene-setting, prospective, questioned, and figurative coordinates. "
            "Then choose the smallest complete source-native grain, resolve class by source function, and remove only true aliases/coreference duplicates, "
            "redundant grains, pure auxiliary/function fragments, invented abstractions, and same-coordinate restatements. Do not prune a coordinate merely "
            "because it is not central to a proposition. Follow response_schema exactly and never infer an expected count or hidden archetype."
            + correction_note
        )
    if bounded.get("task") == "researcher_inventory_build_lightweight_compounds":
        return (
            "COMPOUND PASS. Apply the installed durable V52 contract to the complete source and supplied frozen units. Scan source relations in order and emit "
            "one smallest COMPLETE compound for each materially distinct source-presented relation instance. Use the frozen participants, relation, referent/content, "
            "state/value, orientation, and scene/time refs actually bound in that relation. Completeness preserves the source binding rather than minimizing ref count. "
            "Do not create or retype units. Do not emit subset alternatives, nested duplicate decompositions, sentence-wide bags, every pair, or combinatorial variants. "
            "qualities_available is quality availability, not a question marker. Follow response_schema exactly and never infer hidden gold."
            + correction_note
        )
    return "Apply the installed durable V52 contract exactly to this bounded request." + correction_note


def main() -> int:
    payload = json.load(sys.stdin)
    agent_id = AGENT_ID_FILE.read_text(encoding="utf-8").strip()
    bounded = _bounded_request(payload)
    attention = _attention_for(bounded)
    core_key = recovery._core_key(bounded)
    state_path, trace_path = recovery._paths(core_key)

    if not bounded.get("correction") and state_path.exists():
        recovery._trace(trace_path, "new_request_supersedes_local_recovery_state", "researcher_inventory_v52_contract_isolated", detail="prior local state preserved in trace; new request starts fresh")
        state_path.unlink()

    initial_prompt = (
        "Execute only this bounded request under your installed durable V52 contract. The durable contract is the sole semantic "
        "selection/grain authority. Return ONLY the JSON value required by response_schema. Do not infer or reconstruct archetypes, "
        "expected answers/counts, evaluator preferences, prior scored outputs, case-specific gold corrections, sealed holdout source, "
        "or holdout output.\n\nTASK ATTENTION:\n" + attention + "\n\nREQUEST JSON:\n" + json.dumps(bounded, ensure_ascii=False)
    )
    try:
        provisional = recovery._session(agent_id, initial_prompt, "researcher_inventory_v52_contract_isolated_extract", state_path, trace_path, "provisional")
        verify_prompt = (
            "Perform a separate adjudication in a new session under the SAME installed durable V52 contract. Re-read the complete source and independently "
            "rebuild the requested result before comparing with the provisional output. For units, begin with broad source-coordinate coverage, then fix grain, "
            "type by source function, and deduplicate; do not use proposition necessity as an admission threshold and do not discard low-salience/background/source-setting "
            "coordinates merely because they are not central. For compounds, reconstruct one complete source relation instance from frozen refs, preserving all co-bound "
            "coordinates without subset alternatives. Return the complete replacement JSON, not a critique. Do not infer archetypes, expected counts, evaluator preferences, "
            "scored prior output, case-specific gold corrections, sealed holdout source, or holdout output.\n\nTASK ATTENTION:\n" + attention + "\n\nREQUEST JSON:\n" + json.dumps(bounded, ensure_ascii=False)
            + "\n\nPROVISIONAL_UNSCORED_OUTPUT:\n" + json.dumps(provisional, ensure_ascii=False)
        )
        verified = recovery._session(agent_id, verify_prompt, "researcher_inventory_v52_contract_isolated_adjudication", state_path, trace_path, "verified")
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
