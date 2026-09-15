#!/usr/bin/env python3
"""V33 bounded adapter: source-available atomic units, then compounds.

The worker sees only its durable V33 contract, neutral V33 task rules, the bounded
source/request, and one unscored provisional output from another session. No
archetype, evaluator finding, expected count, scored output, case-specific
correction example, or sealed holdout material is supplied.

Session-timeout recovery reuses the proven V32 recovery machinery while keeping a
separate V33 runtime state directory.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

from openai_agents_adapter import AGENT_ID_FILE
import v32_openai_agents_adapter as recovery

recovery.RECOVERY_DIR = Path("researcher_inventory/runtime/v33_session_recovery")


def _attention_for(bounded: dict) -> str:
    if bounded.get("task") == "researcher_inventory_extract_one_class":
        cls = bounded.get("class")
        grain = {
            "PLACE": "SOURCE SCENE/LOCATION GRAIN: retain independently available broad/contained settings and local scene positions, including supported unnamed scenes; reject only non-locating material, unsupported inference, and same-class aliases.",
            "TIME": "SOURCE WHEN/FRAME GRAIN: retain independently available episodes, periods, date/duration/recurrence coordinates, recollection/report frames, intended periods, present reflection, and represented future frames; do not collapse separate when-coordinates into one larger episode.",
            "PERSON": "RESOLVED ACTOR GRAIN: retain every independently represented human/social actor or group, including peripheral actors; resolve aliases/pronouns before same-class duplicate removal.",
            "OBJECT": "SOURCE REFERENT GRAIN: retain independently identifiable concrete or abstract referents, including locally mentioned things/parts/content; centrality or repeated tracking is not required.",
            "LABEL": "SOURCE CHARACTERIZATION GRAIN: retain distinct literal identities, qualities, states, evaluations, comparisons, corrections, rejections, and characterization questions/responses; foregrounding or reuse is not required.",
            "VERB": "ATOMIC SOURCE RELATION GRAIN: split independently available predicate/relation steps inside a clause rather than packaging a multi-step event into one VERB; event-level assembly belongs in COMPOUNDS.",
            "LOCATOR": "SOURCE LOCATING/ORIENTING GRAIN: retain independently available position/path/origin/destination/containment/anchor/situational/contextual/figurative orientation; do not exclude a locator solely because other class material is present in the same wording.",
        }.get(cls, "Use the installed V33 class-specific grain exactly.")
        correction = recovery._mechanical_correction(bounded.get("correction"))
        correction_note = ""
        if correction:
            correction_note = (
                "\nMECHANICAL VALIDATOR CORRECTION FROM YOUR PRIOR UNSCORED ATTEMPT: " + correction +
                " Rebuild the complete class result from source and durable V33 principles; do not patch only the named field. "
                "This is mechanical schema/literal validation only, not gold/evaluator scoring guidance."
            )
        return (
            "UNIT PASS. Read the entire source first. Preserve every independently SOURCE-AVAILABLE coordinate of THIS class at the class grain. "
            + grain + " "
            "Do not require narrative salience or exclusive semantic ownership. Classes are not mutually exclusive bins. "
            "Split bundled candidates when the source contains multiple separately available class coordinates; merge only true same-class aliases/coreference duplicates. "
            "Run: whole-source read -> THIS-class candidates -> split available coordinates -> coreference/duplicates -> omission pass -> inference/debris excess pass -> exact-span/order check. "
            "Preserve source posture and literal wording. Never target an expected count or infer an archetype." + correction_note
        )
    if bounded.get("task") == "researcher_inventory_build_lightweight_compounds":
        correction = recovery._mechanical_correction(bounded.get("correction"))
        correction_note = ""
        if correction:
            correction_note = "\nMECHANICAL VALIDATOR CORRECTION: " + correction + " Rebuild the complete compound set from final units rather than patching one row."
        return (
            "COMPOUND PASS. Units are FINAL. Do not merge, split, add, or delete units here. Re-read source and assemble larger SOURCE-PRESENTED BINDINGS among those final coordinates at proposition/event/state/question/report/reflection/intention/characterization/relation-cluster grain. "
            "Multiple atomic VERBs/LOCATORs may participate in one compound. Use all and only final units materially participating, in semantic/source order. "
            "Do not graph arbitrary subsets/every recombination, duplicate nested subsets unless separately source-presented, or invent units to make a compound complete." + correction_note
        )
    return "Apply the installed V33 durable contract exactly to this bounded request."


def main() -> int:
    payload = json.load(sys.stdin)
    agent_id = AGENT_ID_FILE.read_text(encoding="utf-8").strip()
    bounded = recovery._bounded_request(payload)
    attention = _attention_for(bounded)
    core_key = recovery._core_key(bounded)
    state_path, trace_path = recovery._paths(core_key)

    if not bounded.get("correction") and state_path.exists():
        recovery._trace(trace_path, "new_request_supersedes_local_recovery_state", "researcher_inventory_v33", detail="prior local state preserved in trace; new request starts fresh")
        state_path.unlink()

    initial_prompt = (
        "Execute only this bounded request under your installed durable V33 contract and supplied neutral apparatus rules. "
        "Return ONLY the JSON value required by response_schema. Do not infer or reconstruct any archetype, expected answer, expected count, evaluator preference, prior scored output, case-specific correction, sealed holdout source, or holdout output.\n\n"
        "TASK ATTENTION:\n" + attention + "\n\n"
        "REQUEST JSON:\n" + json.dumps(bounded, ensure_ascii=False)
    )

    try:
        provisional = recovery._session(
            agent_id,
            initial_prompt,
            "researcher_inventory_v33_extract",
            state_path,
            trace_path,
            "provisional",
        )

        verify_prompt = (
            "Perform a separate V33 adjudication in a new session. Re-read the complete source and independently rebuild the requested result BEFORE comparing with the provisional output. "
            "Use this order: (1) complete source; (2) THIS-class source-available candidates; (3) split independently available coordinates; (4) class grain; (5) coreference and true same-class duplicate merge; (6) omission pass; (7) unsupported-inference/debris excess pass; (8) exact literal-span/order check. "
            "Do not suppress a coordinate for lack of narrative salience or because another class also applies. VERB units preserve separately available relation increments; larger event packaging belongs in COMPOUNDS. "
            "Do not target a count. Return the complete replacement JSON, not a critique.\n\n"
            "TASK ATTENTION:\n" + attention + "\n\n"
            "REQUEST JSON:\n" + json.dumps(bounded, ensure_ascii=False) + "\n\n"
            "PROVISIONAL_UNSCORED_OUTPUT:\n" + json.dumps(provisional, ensure_ascii=False)
        )
        verified = recovery._session(
            agent_id,
            verify_prompt,
            "researcher_inventory_v33_adjudication",
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
