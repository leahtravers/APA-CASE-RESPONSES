#!/usr/bin/env python3
"""V46 harness-isolated adapter. Durable V46 contract is sole semantic authority."""
from __future__ import annotations

import json
import sys
from pathlib import Path

from openai_agents_adapter import AGENT_ID_FILE
import v32_openai_agents_adapter as recovery

recovery.RECOVERY_DIR = Path("researcher_inventory/runtime/v46_session_recovery")


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
            + " Rebuild the complete requested result under the installed V46 contract; "
              "do not patch only the named field. This is mechanical validation feedback, "
              "not evaluator or gold guidance."
        )
    if bounded.get("task") == "researcher_inventory_extract_one_class":
        return (
            "UNIT PASS. Apply the installed durable V46 contract to the complete source. "
            "Reconstruct the source binding/frame map first, then identify only independent binding roles of the requested class. "
            "Use primary semantic class assignment; explicit wording, lexical separability, local/nested status, and independent variation "
            "do not by themselves create rows. Check specifically for supported unnamed PLACE/TIME scene or episode roles required by "
            "materially distinct bindings. Prefer complete governing relations over lexical predicate census, and retain LOCATOR only for "
            "binding-relevant orientation. Run both omission and excess passes. Follow response_schema exactly and never infer an expected "
            "count or hidden archetype."
            + correction_note
        )
    if bounded.get("task") == "researcher_inventory_build_lightweight_compounds":
        return (
            "COMPOUND PASS. Apply the installed durable V46 contract to the complete source and supplied frozen units. "
            "Rebuild the retained source binding map and emit one canonical compound per materially distinct binding/frame, using the "
            "smallest complete set of frozen role coordinates needed for that binding. Prefer a complete canonical binding over nested "
            "phrase/subset compounds. Do not create units, retype units, emit combinatorial subsets, every pair, every sentence, every "
            "nested clause, or alternate lexical decompositions of the same binding. Follow response_schema exactly; do not infer hidden gold."
            + correction_note
        )
    return "Apply the installed durable V46 contract exactly to this bounded request." + correction_note


def main() -> int:
    payload = json.load(sys.stdin)
    agent_id = AGENT_ID_FILE.read_text(encoding="utf-8").strip()
    bounded = _bounded_request(payload)
    attention = _attention_for(bounded)
    core_key = recovery._core_key(bounded)
    state_path, trace_path = recovery._paths(core_key)

    if not bounded.get("correction") and state_path.exists():
        recovery._trace(trace_path, "new_request_supersedes_local_recovery_state", "researcher_inventory_v46_contract_isolated", detail="prior local state preserved in trace; new request starts fresh")
        state_path.unlink()

    initial_prompt = (
        "Execute only this bounded request under your installed durable V46 contract. The durable contract is the sole semantic "
        "selection/grain authority. Return ONLY the JSON value required by response_schema. Do not infer or reconstruct archetypes, "
        "expected answers/counts, evaluator preferences, prior scored outputs, case-specific gold corrections, sealed holdout source, "
        "or holdout output.\n\nTASK ATTENTION:\n" + attention + "\n\nREQUEST JSON:\n" + json.dumps(bounded, ensure_ascii=False)
    )
    try:
        provisional = recovery._session(agent_id, initial_prompt, "researcher_inventory_v46_contract_isolated_extract", state_path, trace_path, "provisional")
        verify_prompt = (
            "Perform a separate adjudication in a new session under the SAME installed durable V46 contract. Re-read the complete source and "
            "independently rebuild the requested result before comparing with the provisional output. Reconstruct canonical source bindings, "
            "identify their independent role coordinates, check for supported unnamed PLACE/TIME roles, enforce primary semantic class, and "
            "remove lexical/detail rows that do not fill independent binding roles. For compounds, prefer one canonical binding per retained "
            "frame/relation rather than nested/subset closure. Return the complete replacement JSON, not a critique. Do not infer or reconstruct "
            "archetypes, expected counts, evaluator preferences, scored prior output, case-specific gold corrections, sealed holdout source, or "
            "holdout output.\n\nTASK ATTENTION:\n"
            + attention + "\n\nREQUEST JSON:\n" + json.dumps(bounded, ensure_ascii=False)
            + "\n\nPROVISIONAL_UNSCORED_OUTPUT:\n" + json.dumps(provisional, ensure_ascii=False)
        )
        verified = recovery._session(agent_id, verify_prompt, "researcher_inventory_v46_contract_isolated_adjudication", state_path, trace_path, "verified")
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
