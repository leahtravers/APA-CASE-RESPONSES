#!/usr/bin/env python3
"""V34 bounded adapter: research-coordinate admission before compound assembly.

The worker sees only its durable V34 contract, neutral V34 task rules, the bounded
source/request, and one unscored provisional output from another session. No
archetype, evaluator finding, expected count, scored output, case-specific
correction example, sealed holdout material, or holdout output is supplied.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

from openai_agents_adapter import AGENT_ID_FILE
import v32_openai_agents_adapter as recovery

recovery.RECOVERY_DIR = Path("researcher_inventory/runtime/v34_session_recovery")


def _attention_for(bounded: dict) -> str:
    if bounded.get("task") == "researcher_inventory_extract_one_class":
        cls = bounded.get("class")
        grain = {
            "PLACE": "SCENE/LOCATION RESEARCH GRAIN: keep independently reusable settings/scene positions, including supported unnamed scenes; do not turn every anchor, contextual phrase, deictic token, or path wording into PLACE.",
            "TIME": "EPISODE/FRAME RESEARCH GRAIN: keep independently reusable when-frames such as episodes, periods, recurrences, report/recollection, present reflection, or represented future frames; do not turn every action, state, question, modifier, or prospective clause into TIME.",
            "PERSON": "RESOLVED ACTOR GRAIN: retain represented human/social actors or stable groups, including peripheral actors; resolve aliases/pronouns before same-class duplicate removal.",
            "OBJECT": "INDEPENDENT REFERENT RESEARCH GRAIN: retain source-treated trackable things/content/choices/values/relations/results; do not nominalize every phrase, complement, clause, property, or argument into OBJECT.",
            "LABEL": "CHARACTERIZATION RESEARCH GRAIN: retain reusable source-applied identities/qualities/states/evaluations/comparisons/corrections/rejections; local labels may qualify, but ordinary predicates/modifiers do not automatically become LABELs.",
            "VERB": "SMALLEST COMPLETE RESEARCH-RELATION GRAIN: split only when each resulting relation remains an independently reusable source edge. Do not enumerate predicate heads or split support/control/raising/selected infinitival machinery merely because grammar permits it.",
            "LOCATOR": "MATERIAL ORIENTING RELATION GRAIN: retain independently reusable position/path/origin/destination/setting relations; do not convert ordinary argument structure, every preposition, time/context wording, or merely lexical spatial metaphors into LOCATORs.",
        }.get(cls, "Use the installed V34 class-specific research grain exactly.")
        correction = recovery._mechanical_correction(bounded.get("correction"))
        correction_note = ""
        if correction:
            correction_note = (
                "\nMECHANICAL VALIDATOR CORRECTION FROM YOUR PRIOR UNSCORED ATTEMPT: " + correction +
                " Rebuild the complete class result from source and durable V34 principles; do not patch only the named field. "
                "This is mechanical schema/literal validation only, not gold/evaluator scoring guidance."
            )
        return (
            "UNIT PASS. Read the entire source first. A unit must be SOURCE-GROUNDED, perform THIS-class job, and have INDEPENDENT REUSABLE RESEARCH IDENTITY at this class grain. "
            + grain + " "
            "Do not use narrative salience as a gate, but do not confuse phrase/predicate separability with research identity. "
            "Cross-class overlap is allowed only when each class view independently reconnects source structure. "
            "Split a candidate only when the resulting coordinates remain independently reusable; merge true same-class aliases/coreference duplicates. "
            "Run: whole-source read -> THIS-class candidates -> research-coordinate gate -> coreference -> justified split/merge -> omission pass -> excess/grammar/cross-class-restatement pass -> exact-span/order check. "
            "Preserve source posture and literal wording. Never target an expected count or infer an archetype." + correction_note
        )
    if bounded.get("task") == "researcher_inventory_build_lightweight_compounds":
        correction = recovery._mechanical_correction(bounded.get("correction"))
        correction_note = ""
        if correction:
            correction_note = "\nMECHANICAL VALIDATOR CORRECTION: " + correction + " Rebuild the complete compound set from final units rather than patching one row."
        return (
            "COMPOUND PASS. Units are FINAL. Do not merge, split, add, or delete units here. Re-read source and assemble larger SOURCE-PRESENTED BINDINGS among those final research coordinates at proposition/event/state/question/report/reflection/intention/characterization/relation-cluster grain. "
            "Use all and only final units materially participating, in semantic/source order. Do not graph arbitrary subsets/every recombination, duplicate nested subsets unless separately source-presented, or invent/retain invalid units merely to make a compound complete." + correction_note
        )
    return "Apply the installed V34 durable contract exactly to this bounded request."


def main() -> int:
    payload = json.load(sys.stdin)
    agent_id = AGENT_ID_FILE.read_text(encoding="utf-8").strip()
    bounded = recovery._bounded_request(payload)
    attention = _attention_for(bounded)
    core_key = recovery._core_key(bounded)
    state_path, trace_path = recovery._paths(core_key)

    if not bounded.get("correction") and state_path.exists():
        recovery._trace(trace_path, "new_request_supersedes_local_recovery_state", "researcher_inventory_v34", detail="prior local state preserved in trace; new request starts fresh")
        state_path.unlink()

    initial_prompt = (
        "Execute only this bounded request under your installed durable V34 contract and supplied neutral apparatus rules. "
        "Return ONLY the JSON value required by response_schema. Do not infer or reconstruct any archetype, expected answer, expected count, evaluator preference, prior scored output, case-specific correction, sealed holdout source, or holdout output.\n\n"
        "TASK ATTENTION:\n" + attention + "\n\n"
        "REQUEST JSON:\n" + json.dumps(bounded, ensure_ascii=False)
    )

    try:
        provisional = recovery._session(
            agent_id,
            initial_prompt,
            "researcher_inventory_v34_extract",
            state_path,
            trace_path,
            "provisional",
        )

        verify_prompt = (
            "Perform a separate V34 adjudication in a new session. Re-read the complete source and independently rebuild the requested result BEFORE comparing with the provisional output. "
            "Use this order: (1) complete source; (2) THIS-class candidates; (3) research-coordinate admission gate; (4) class grain; (5) coreference and true same-class duplicate merge; (6) split only independently reusable coordinates; (7) omission pass; (8) grammar/wrapper/cross-class-restatement excess pass; (9) exact literal-span/order check. "
            "Do not suppress a valid coordinate for lack of narrative salience, but do not retain wording merely because it is syntactically isolatable or can be assigned to the class. "
            "For VERB, preserve smallest complete research-meaningful relation packages and split only independent source edges; event-level assembly belongs in COMPOUNDS. "
            "Do not target a count. Return the complete replacement JSON, not a critique.\n\n"
            "TASK ATTENTION:\n" + attention + "\n\n"
            "REQUEST JSON:\n" + json.dumps(bounded, ensure_ascii=False) + "\n\n"
            "PROVISIONAL_UNSCORED_OUTPUT:\n" + json.dumps(provisional, ensure_ascii=False)
        )
        verified = recovery._session(
            agent_id,
            verify_prompt,
            "researcher_inventory_v34_adjudication",
            state_path,
            trace_path,
            "verified",
        )
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
