#!/usr/bin/env python3
"""V36 bounded adapter: sparse event-map coordinate admission.

The worker sees only its durable contract, neutral V36 task rules, the bounded
source/request, and one unscored provisional output from another session. No
archetype, evaluator finding, expected count, scored output, case-specific gold
correction, sealed holdout material, or holdout output is supplied.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

from openai_agents_adapter import AGENT_ID_FILE
import v32_openai_agents_adapter as recovery

recovery.RECOVERY_DIR = Path("researcher_inventory/runtime/v36_session_recovery")


def _attention_for(bounded: dict) -> str:
    if bounded.get("task") == "researcher_inventory_extract_one_class":
        cls = bounded.get("class")
        grain = {
            "PLACE": "SCENE GRAIN: keep physical settings that organize distinct represented events, including supported unnamed settings for distinct scenes; do not promote incidental surfaces, parts, path fragments, or positions unless they themselves define a distinct scene coordinate.",
            "TIME": "EPISODE GRAIN: keep event periods/frames and materially distinct contained phases, including supported unnamed episodes; do not promote every adverb, sequence word, tense, action, or duration/value that only decorates an existing frame.",
            "PERSON": "ACTOR GRAIN: keep represented humans/stable groups; resolve aliases/pronouns/roles before duplicate removal; generic discourse addressees require actual represented actor status.",
            "OBJECT": "EVENT-NODE GRAIN: keep concrete/abstract referents that materially participate as tracked nodes in source events; do not duplicate places, reify arbitrary clauses/propositions, or promote incidental parts/values/properties without a distinct event role.",
            "LABEL": "CLASSIFICATION GRAIN: keep explicit analyzable classifications/qualities/states/evaluations/corrections/rejections attached to tracked units/events; do not inventory every adjective, modifier, role word, copular clause, or evaluative sentence. Preserve separate explicit classification and polarity/correction moves at their literal grain.",
            "VERB": "RELATION-EDGE GRAIN: keep the smallest semantically complete relation edge that materially connects or changes retained event-map coordinates. Do not lexical-census predicate heads or split support/control/copular grammar. Split multiple relations only when each independently binds retained coordinates.",
            "LOCATOR": "MATERIAL ORIENTATION GRAIN: keep orienting relations only when they materially reconnect retained coordinates by location/path/origin/destination/containment/proximity or comparable represented orientation; do not inventory every preposition, context phrase, temporal word, accompaniment, possession, or figurative phrase.",
        }.get(cls, "Use the installed V36 class-specific event-coordinate grain exactly.")
        correction = recovery._mechanical_correction(bounded.get("correction"))
        correction_note = ""
        if correction:
            correction_note = (
                "\nMECHANICAL VALIDATOR CORRECTION FROM YOUR PRIOR UNSCORED ATTEMPT: " + correction +
                " Rebuild the complete class result from source and durable V36 principles; do not patch only the named field. "
                "This is mechanical schema/literal validation only, not gold/evaluator scoring guidance."
            )
        return (
            "UNIT PASS. Read the entire source, silently construct the sparse source event map, and then answer THIS class only. "
            "A candidate must pass both positive class function and RESEARCH-COORDINATE NECESSITY: it must establish or materially reconnect a distinct event-map coordinate/relation. "
            "Local or one-off coordinates may qualify; salience, repetition, and global reuse are not required. But mere literal availability, grammatical separability, or possible classification is not enough. "
            + grain + " "
            "Run: whole-source read -> internal event map -> THIS-class candidates -> class function -> coordinate necessity -> coreference/true aliases -> class grain -> omission pass for real local/unnamed/contained event coordinates -> excess/debris/cross-class-restatement pass -> exact literal/posture/source-order check. "
            "Never target an expected count or infer an archetype." + correction_note
        )
    if bounded.get("task") == "researcher_inventory_build_lightweight_compounds":
        correction = recovery._mechanical_correction(bounded.get("correction"))
        correction_note = ""
        if correction:
            correction_note = "\nMECHANICAL VALIDATOR CORRECTION: " + correction + " Rebuild the complete compound set from frozen final units rather than patching one row."
        return (
            "COMPOUND PASS. Units are FROZEN. Build MINIMAL EVENT/RELATION TUPLES, normally one materially distinct relation edge per compound. "
            "Create a compound only when final units need binding to preserve a source-presented event relation. Use only participating units; add place/time/locator/label anchors only when they materially situate that event. "
            "Do not paraphrase whole sentences, create every clause/co-occurrence/subset, showcase units, or create redundant nested expansions. Preserve semantic source order." + correction_note
        )
    return "Apply the installed V36 durable contract exactly to this bounded request."


def main() -> int:
    payload = json.load(sys.stdin)
    agent_id = AGENT_ID_FILE.read_text(encoding="utf-8").strip()
    bounded = recovery._bounded_request(payload)
    attention = _attention_for(bounded)
    core_key = recovery._core_key(bounded)
    state_path, trace_path = recovery._paths(core_key)

    if not bounded.get("correction") and state_path.exists():
        recovery._trace(trace_path, "new_request_supersedes_local_recovery_state", "researcher_inventory_v36", detail="prior local state preserved in trace; new request starts fresh")
        state_path.unlink()

    initial_prompt = (
        "Execute only this bounded request under your installed durable V36 contract and supplied neutral apparatus rules. "
        "Return ONLY the JSON value required by response_schema. Do not infer or reconstruct any archetype, expected answer, expected count, evaluator preference, prior scored output, case-specific gold correction, sealed holdout source, or holdout output.\n\n"
        "TASK ATTENTION:\n" + attention + "\n\n"
        "REQUEST JSON:\n" + json.dumps(bounded, ensure_ascii=False)
    )

    try:
        provisional = recovery._session(
            agent_id,
            initial_prompt,
            "researcher_inventory_v36_extract",
            state_path,
            trace_path,
            "provisional",
        )

        verify_prompt = (
            "Perform a separate V36 adjudication in a new session. Re-read the complete source and independently rebuild the requested result BEFORE comparing with the provisional output. "
            "First construct the sparse event map; then require both THIS-class positive function and research-coordinate necessity. "
            "Protect real local/unnamed/contained event coordinates from V34-style undercapture, while removing V35-style grammatical, modifier, clause-content, incidental-detail, predicate-fragment, and contextual overcapture. "
            "For VERB, keep smallest semantically complete relation edges that independently bind retained coordinates. For compounds, units are frozen and output minimal one-event relation tuples rather than proposition bundles. "
            "Do not target a count. Return the complete replacement JSON, not a critique.\n\n"
            "TASK ATTENTION:\n" + attention + "\n\n"
            "REQUEST JSON:\n" + json.dumps(bounded, ensure_ascii=False) + "\n\n"
            "PROVISIONAL_UNSCORED_OUTPUT:\n" + json.dumps(provisional, ensure_ascii=False)
        )
        verified = recovery._session(
            agent_id,
            verify_prompt,
            "researcher_inventory_v36_adjudication",
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
