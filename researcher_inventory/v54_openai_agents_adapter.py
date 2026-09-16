#!/usr/bin/env python3
"""V54 contract-version-correct isolated agent adapter.

The saved agent is bootstrapped from the durable contract named by RI_CONTRACT_FILE.
Session prompts contain only bounded task mechanics; gold archetypes, evaluator findings,
prior scored outputs, and sealed holdout content are never sent to the worker.
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

from openai_agents_adapter import AGENT_ID_FILE
import v32_openai_agents_adapter as recovery

CONTRACT_VERSION = os.environ.get("CONTRACT_VERSION", "RI-CONTRACT-V54").strip() or "RI-CONTRACT-V54"
recovery.RECOVERY_DIR = Path("researcher_inventory/runtime/v54_session_recovery")


def _bounded_request(payload: dict) -> dict:
    """Remove apparatus prose so the installed durable contract is sole semantics."""
    bounded = recovery._bounded_request(payload)
    bounded.pop("rules", None)
    bounded.pop("class_rule", None)
    return bounded


def _normalize_optional_fields(result, task: str):
    """Materialize documented schema defaults without changing semantic choices."""
    if task == "researcher_inventory_extract_one_class" and isinstance(result, list):
        for row in result:
            if isinstance(row, dict) and row.get("scope_rank") is None:
                row["scope_rank"] = 0
    return result


def _attention_for(bounded: dict) -> str:
    """Mechanical task attention only; no second semantic contract in the harness."""
    correction = recovery._mechanical_correction(bounded.get("correction"))
    correction_note = ""
    if correction:
        correction_note = (
            "\nMECHANICAL VALIDATOR CORRECTION FROM THE PRIOR UNSCORED ATTEMPT: "
            + correction
            + " Rebuild the complete requested result under the installed durable contract; "
              "do not patch only the named field. This is mechanical validation feedback, "
              "not evaluator or gold guidance."
        )

    task = bounded.get("task")
    if task == "researcher_inventory_extract_one_class":
        return (
            f"UNIT PASS. Apply the installed durable {CONTRACT_VERSION} contract as the sole semantic selection, grain, and type authority. "
            "Read the complete supplied source and return the complete requested class in the exact response_schema. "
            "Do not infer an expected count, archetype, evaluator preference, prior scored correction, or holdout answer."
            + correction_note
        )
    if task == "researcher_inventory_build_lightweight_compounds":
        return (
            f"COMPOUND PASS. Apply the installed durable {CONTRACT_VERSION} contract as the sole semantic compound authority. "
            "Use only the supplied frozen units and complete source, and return the exact response_schema. "
            "Do not infer an expected count, archetype, evaluator preference, prior scored correction, or holdout answer."
            + correction_note
        )
    return (
        f"Apply the installed durable {CONTRACT_VERSION} contract exactly to this bounded request as the sole semantic authority."
        + correction_note
    )


def main() -> int:
    payload = json.load(sys.stdin)
    agent_id = AGENT_ID_FILE.read_text(encoding="utf-8").strip()
    bounded = _bounded_request(payload)
    attention = _attention_for(bounded)
    core_key = recovery._core_key(bounded)
    state_path, trace_path = recovery._paths(core_key)

    if not bounded.get("correction") and state_path.exists():
        recovery._trace(
            trace_path,
            "new_request_supersedes_local_recovery_state",
            "researcher_inventory_v54_contract_isolated",
            detail="prior local state preserved in trace; new request starts fresh",
        )
        state_path.unlink()

    initial_prompt = (
        f"Execute only this bounded request under your installed durable {CONTRACT_VERSION} contract. "
        "That installed durable contract is the sole semantic selection/grain/type authority. "
        "Return ONLY the JSON value required by response_schema. Do not infer or reconstruct archetypes, expected answers/counts, evaluator preferences, "
        "prior scored outputs, case-specific gold corrections, sealed holdout source, or holdout output.\n\n"
        "TASK ATTENTION:\n" + attention + "\n\nREQUEST JSON:\n" + json.dumps(bounded, ensure_ascii=False)
    )

    try:
        provisional = recovery._session(
            agent_id,
            initial_prompt,
            "researcher_inventory_v54_contract_isolated_extract",
            state_path,
            trace_path,
            "provisional",
        )
        provisional = _normalize_optional_fields(provisional, bounded.get("task", ""))

        verify_prompt = (
            f"Perform a separate adjudication in a new session under the SAME installed durable {CONTRACT_VERSION} contract. "
            "Re-read the complete source and independently rebuild the requested result before comparing with the provisional output. "
            "The installed durable contract remains the sole semantic selection/grain/type authority. Return the complete replacement JSON, not a critique. "
            "Do not infer archetypes, expected counts, evaluator preferences, scored prior output, case-specific gold corrections, sealed holdout source, or holdout output.\n\n"
            "TASK ATTENTION:\n" + attention + "\n\nREQUEST JSON:\n" + json.dumps(bounded, ensure_ascii=False)
            + "\n\nPROVISIONAL_UNSCORED_OUTPUT:\n" + json.dumps(provisional, ensure_ascii=False)
        )
        verified = recovery._session(
            agent_id,
            verify_prompt,
            "researcher_inventory_v54_contract_isolated_adjudication",
            state_path,
            trace_path,
            "verified",
        )
        verified = _normalize_optional_fields(verified, bounded.get("task", ""))
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
