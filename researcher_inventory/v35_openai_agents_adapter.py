#!/usr/bin/env python3
"""V35 bounded adapter: class-native positive capture before narrow pruning.

The worker sees only its durable contract, neutral V35 task rules, the bounded
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

recovery.RECOVERY_DIR = Path("researcher_inventory/runtime/v35_session_recovery")


def _attention_for(bounded: dict) -> str:
    if bounded.get("task") == "researcher_inventory_extract_one_class":
        cls = bounded.get("class")
        grain = {
            "PLACE": "PHYSICAL PLACE/SCENE/POSITION GRAIN: broad settings may coexist with separately established local physical positions and supported unnamed scene locations; do not invent places from abstract context, objects, or purely figurative wording.",
            "TIME": "WHEN-COORDINATE GRAIN: retain broad episodes plus separately established contained phases and explicit temporal anchors; do not collapse local source-established phases into one broad episode, but tense/action alone is not a TIME.",
            "PERSON": "RESOLVED ACTOR GRAIN: retain represented humans/social groups including peripheral actors; resolve aliases/pronouns before true same-class duplicate removal.",
            "OBJECT": "REFERENT GRAIN: default toward source-distinguished concrete referents, parts, surfaces, media, documents, amounts, bodily/mental referents, plus source-treated abstract things/choices/results; do not nominalize arbitrary clauses.",
            "LABEL": "APPLIED CHARACTERIZATION GRAIN: retain local or global source-applied qualities/states/identities/evaluations/comparisons/corrections/rejections at the shortest complete literal span; do not require foregrounding/reuse.",
            "VERB": "LEXICAL RELATION-EDGE GRAIN: keep each lexical predicate increment that contributes its own relation, including matrix/embedded/serial steps; suppress only bare auxiliary/support grammar. Do not package multiple relation edges into one VERB merely because they share a clause.",
            "LOCATOR": "ORIENTING RELATION GRAIN: retain literal position/path/origin/destination/movement/context plus materially represented figurative/mental/social orientation; reject only non-orienting argument grammar or isolated prepositions.",
        }.get(cls, "Use the installed V35 class-specific positive-capture grain exactly.")
        correction = recovery._mechanical_correction(bounded.get("correction"))
        correction_note = ""
        if correction:
            correction_note = (
                "\nMECHANICAL VALIDATOR CORRECTION FROM YOUR PRIOR UNSCORED ATTEMPT: " + correction +
                " Rebuild the complete class result from source and durable V35 principles; do not patch only the named field. "
                "This is mechanical schema/literal validation only, not gold/evaluator scoring guidance."
            )
        return (
            "UNIT PASS. Read the entire source first. Use POSITIVE CAPTURE BEFORE NEGATIVE PRUNING. "
            "Capture every source-grounded coordinate that genuinely performs THIS class job at the installed grain; do not require salience, repeated use, global reuse, foregrounding, or exclusive semantic ownership. "
            + grain + " "
            "After broad capture, resolve coreference and remove only true same-class aliases, unsupported inference/paraphrase, analyst clause-reification, bare grammatical machinery, same-grain duplicates, or material with no THIS-class job. "
            "Cross-class overlap is allowed when wording genuinely performs both jobs. "
            "Run: whole-source read -> broad THIS-class capture -> class grain -> coreference/merge -> omission pass -> narrow negative prune -> exact literal/posture/order check. "
            "Never target an expected count or infer an archetype." + correction_note
        )
    if bounded.get("task") == "researcher_inventory_build_lightweight_compounds":
        correction = recovery._mechanical_correction(bounded.get("correction"))
        correction_note = ""
        if correction:
            correction_note = "\nMECHANICAL VALIDATOR CORRECTION: " + correction + " Rebuild the complete compound set from frozen final units rather than patching one row."
        return (
            "COMPOUND PASS. Units are FROZEN. Build a SELECTIVE SOURCE REASSEMBLY SPINE, not a sentence/clause list and not a graph of every subset. "
            "Create a compound only for a materially distinct source-presented binding among two or more final units when the connectivity would otherwise be lost. "
            "Use all and only final units that actually participate; include frame/place/locator anchors only when they genuinely situate that binding. "
            "Do not create a compound merely because a unit exists, do not create single-unit showcase compounds, and remove redundant nested/subset/expanded variants of the same binding." + correction_note
        )
    return "Apply the installed V35 durable contract exactly to this bounded request."


def main() -> int:
    payload = json.load(sys.stdin)
    agent_id = AGENT_ID_FILE.read_text(encoding="utf-8").strip()
    bounded = recovery._bounded_request(payload)
    attention = _attention_for(bounded)
    core_key = recovery._core_key(bounded)
    state_path, trace_path = recovery._paths(core_key)

    if not bounded.get("correction") and state_path.exists():
        recovery._trace(trace_path, "new_request_supersedes_local_recovery_state", "researcher_inventory_v35", detail="prior local state preserved in trace; new request starts fresh")
        state_path.unlink()

    initial_prompt = (
        "Execute only this bounded request under your installed durable V35 contract and supplied neutral apparatus rules. "
        "Return ONLY the JSON value required by response_schema. Do not infer or reconstruct any archetype, expected answer, expected count, evaluator preference, prior scored output, case-specific correction, sealed holdout source, or holdout output.\n\n"
        "TASK ATTENTION:\n" + attention + "\n\n"
        "REQUEST JSON:\n" + json.dumps(bounded, ensure_ascii=False)
    )

    try:
        provisional = recovery._session(
            agent_id,
            initial_prompt,
            "researcher_inventory_v35_extract",
            state_path,
            trace_path,
            "provisional",
        )

        verify_prompt = (
            "Perform a separate V35 adjudication in a new session. Re-read the complete source and independently rebuild the requested result BEFORE comparing with the provisional output. "
            "Use this order: (1) complete source; (2) broad positive THIS-class capture; (3) class-native grain; (4) coreference and true same-class duplicate merge; (5) second omission pass including small/local/nested coordinates; (6) narrow negative prune for unsupported inference, analyst clause-reification, bare grammar, or same-grain duplicates; (7) exact literal/posture/order check. "
            "Do not suppress a coordinate for lack of salience, repeated use, broad reuse, or because another class also applies. "
            "For VERB, preserve distinct lexical relation edges while rejecting bare auxiliary/support grammar. For compounds, units are frozen and the output is a selective connective spine rather than exhaustive clause coverage. "
            "Do not target a count. Return the complete replacement JSON, not a critique.\n\n"
            "TASK ATTENTION:\n" + attention + "\n\n"
            "REQUEST JSON:\n" + json.dumps(bounded, ensure_ascii=False) + "\n\n"
            "PROVISIONAL_UNSCORED_OUTPUT:\n" + json.dumps(provisional, ensure_ascii=False)
        )
        verified = recovery._session(
            agent_id,
            verify_prompt,
            "researcher_inventory_v35_adjudication",
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
