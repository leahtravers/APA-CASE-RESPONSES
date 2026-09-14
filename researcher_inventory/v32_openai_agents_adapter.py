#!/usr/bin/env python3
"""V32 bounded adapter: material research coordinates, then source bindings.

The worker sees only its durable V32 contract, neutral V32 task rules, the bounded
source/request, and one unscored provisional output from another session. No
archetype, evaluator finding, expected count, scored output, case-specific
correction example, or sealed holdout material is supplied.

Harness note: agent-session timeouts are recovery events, not semantic failures.
A timed-out session is durably identified in runtime state and resumed by the
apparatus retry instead of silently creating a duplicate semantic execution.
"""
from __future__ import annotations

import hashlib
import json
import os
import sys
import time
from pathlib import Path

from openai_agents_adapter import AGENT_ID_FILE, final_answer, request, wait

SESSION_WAIT_SECONDS = int(os.environ.get("RI_AGENT_SESSION_TIMEOUT_SECONDS", "600"))
RECOVERY_DIR = Path("researcher_inventory/runtime/v32_session_recovery")


class SessionUncertain(RuntimeError):
    """The backend agent session may still be running; preserve and recover it."""


def _bounded_request(payload: dict) -> dict:
    keep = {
        "task", "rules", "class", "class_rule", "response_schema", "source",
        "units", "candidate", "researcher_interest", "created_by_ref", "correction",
    }
    return {k: v for k, v in payload.items() if k in keep}


def _mechanical_correction(value) -> str | None:
    """Return validator feedback only; never inject runtime/harness failure text."""
    if not value:
        return None
    text = str(value)
    lowered = text.lower()
    runtime_markers = (
        "model adapter failed",
        "session timeout",
        "v32_session_uncertain",
        "traceback (most recent call last)",
        "runtimeerror",
        "subprocess",
    )
    if any(marker in lowered for marker in runtime_markers):
        return None
    return text


def _attention_for(bounded: dict) -> str:
    if bounded.get("task") == "researcher_inventory_extract_one_class":
        cls = bounded.get("class")
        grain = {
            "PLACE": "MATERIAL SCENE-LOCATION GRAIN: retain source-organizing settings/scene positions, including needed unnamed scenes; reject incidental surfaces, anchors, deictics, paths, and figurative space unless the position itself is materially significant.",
            "TIME": "MATERIAL EPISODE/FRAME GRAIN: retain source-organizing when-frames, not every temporal word, duration, recurrence token, action, or prospective phrase.",
            "PERSON": "RESOLVED ACTOR GRAIN: represented human/social actors only; generic you/listener language is not a person without independent participant identity.",
            "OBJECT": "INDEPENDENT REFERENT GRAIN: retain materially tracked things/content/choices; reject incidental nouns, place-only anchors, characterization-only material, wrappers, and analyst nominalizations.",
            "LABEL": "SALIENT CHARACTERIZATION GRAIN: retain foregrounded reusable source characterizations, not every adjective/modifier/descriptive predicate.",
            "VERB": "LIGHTWEIGHT RESEARCH-RELATION PACKAGE GRAIN: package control/embedded/support material when it jointly expresses one relation; split only independently useful relation jobs; reject predicate-token atomization and characterization/locator-only copulas.",
            "LOCATOR": "SPATIAL/ORIENTING GRAIN: retain materially useful position/path/origin/destination/containment relations; reject ordinary temporal/context/argument relations.",
        }.get(cls, "Use the installed V32 class-specific research grain exactly.")
        correction = _mechanical_correction(bounded.get("correction"))
        correction_note = ""
        if correction:
            correction_note = (
                "\nVALIDATOR CORRECTION FROM YOUR PRIOR UNSCORED ATTEMPT: " + correction +
                " Rebuild the complete class result from source and the durable principles; do not patch only the named field. "
                "This validator correction is mechanical only and is not gold/evaluator scoring guidance."
            )
        return (
            "UNIT PASS. Read the entire source first. A unit is a MATERIAL RESEARCH COORDINATE, not every phrase that can fit the class definition. "
            + grain + " "
            "First choose the primary semantic home of the source material. Cross-class overlap is exceptional and requires an independently material second job. "
            "For every candidate ask what distinct reusable source coordinate would disappear if omitted; if the answer is only a phrase, grammatical relation, local modifier, or possible classification, omit it. "
            "Run: structural read -> THIS-class candidates -> material-coordinate gate -> class grain -> coreference -> omission pass -> EXCESS/CROSS-CLASS pass -> exact-span/order check. "
            "Preserve source posture and literal wording. Never target an expected count or infer an archetype." + correction_note
        )
    if bounded.get("task") == "researcher_inventory_build_lightweight_compounds":
        correction = _mechanical_correction(bounded.get("correction"))
        correction_note = ""
        if correction:
            correction_note = "\nVALIDATOR CORRECTION: " + correction + " Rebuild the complete compound set from final units rather than patching one row."
        return (
            "COMPOUND PASS. Units are final and cannot be repaired here. Re-read source and identify MATERIAL SOURCE-PRESENTED BINDINGS among retained coordinates at proposition/event/state/question/report/reflection/intention/characterization/relation-cluster grain. "
            "For each binding use all and only final units materially participating, in semantic/source order. Make separate compounds only for separately presented bindings. "
            "Do not graph every sentence, emit arbitrary subsets/every recombination, duplicate nested subsets unless separately source-presented, or invent units to make a compound complete." + correction_note
        )
    return "Apply the installed V32 durable contract exactly to this bounded request."


def _core_key(bounded: dict) -> str:
    stable = {k: v for k, v in bounded.items() if k != "correction"}
    raw = json.dumps(stable, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def _paths(core_key: str) -> tuple[Path, Path]:
    RECOVERY_DIR.mkdir(parents=True, exist_ok=True)
    return RECOVERY_DIR / f"{core_key}.json", RECOVERY_DIR / f"{core_key}.ndjson"


def _load_state(path: Path) -> dict:
    if not path.exists():
        return {}
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
        return value if isinstance(value, dict) else {}
    except Exception:
        return {}


def _save_state(path: Path, state: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(".tmp")
    tmp.write_text(json.dumps(state, ensure_ascii=False, sort_keys=True, indent=2) + "\n", encoding="utf-8")
    tmp.replace(path)


def _trace(path: Path, event: str, session_type: str, session_id: str | None = None, status: str | None = None, detail: str | None = None) -> None:
    record = {
        "unix": time.time(),
        "event": event,
        "session_type": session_type,
        "session_id": session_id,
        "status": status,
        "detail": detail,
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n")


def _session(agent_id: str, prompt: str, session_type: str, state_path: Path, trace_path: Path, phase: str):
    state = _load_state(state_path)
    phase_state = state.get(phase) if isinstance(state.get(phase), dict) else {}

    if "result" in phase_state:
        _trace(trace_path, "recovered_completed_result", session_type, phase_state.get("session_id"), "completed")
        return phase_state["result"]

    session_id = phase_state.get("session_id")
    if session_id:
        _trace(trace_path, "resume_existing_session", session_type, session_id, phase_state.get("status"))
    else:
        session = request(
            "/agents/sessions",
            method="POST",
            body={
                "agent_id": agent_id,
                "environment": {"type": "none"},
                "input": prompt,
                "metadata": {"apa_session_type": session_type},
            },
        )
        session_id = session["id"]
        phase_state = {"session_id": session_id, "status": session.get("status") or "created"}
        state[phase] = phase_state
        _save_state(state_path, state)
        _trace(trace_path, "session_created", session_type, session_id, phase_state["status"])

    try:
        wait(session_id, timeout=SESSION_WAIT_SECONDS)
    except RuntimeError as exc:
        if str(exc) != "session timeout":
            _trace(trace_path, "session_terminal_error", session_type, session_id, detail=str(exc))
            raise

        try:
            current = request(f"/agents/sessions/{session_id}")
            status = str(current.get("status") or "unknown")
        except Exception as status_exc:
            phase_state["status"] = "unknown"
            phase_state["last_error"] = f"status check failed: {status_exc}"
            state[phase] = phase_state
            _save_state(state_path, state)
            _trace(trace_path, "timeout_status_unknown", session_type, session_id, "unknown", str(status_exc))
            raise SessionUncertain(f"V32_SESSION_UNCERTAIN session_id={session_id} status=unknown") from exc

        phase_state["status"] = status
        state[phase] = phase_state
        _save_state(state_path, state)
        _trace(trace_path, "timeout_status_checked", session_type, session_id, status)

        if status == "idle":
            pass
        elif status in ("failed", "requires_action"):
            raise RuntimeError(f"session terminal status {status}") from exc
        else:
            raise SessionUncertain(f"V32_SESSION_UNCERTAIN session_id={session_id} status={status}") from exc

    raw = final_answer(session_id)
    if raw.startswith("```"):
        lines = raw.splitlines()
        if lines and lines[0].startswith("```"):
            lines = lines[1:]
        if lines and lines[-1].strip() == "```":
            lines = lines[:-1]
        raw = "\n".join(lines).strip()
    result = json.loads(raw)

    state = _load_state(state_path)
    phase_state = state.get(phase) if isinstance(state.get(phase), dict) else {"session_id": session_id}
    phase_state["status"] = "completed"
    phase_state["result"] = result
    state[phase] = phase_state
    _save_state(state_path, state)
    _trace(trace_path, "session_completed", session_type, session_id, "completed")
    return result


def main() -> int:
    payload = json.load(sys.stdin)
    agent_id = AGENT_ID_FILE.read_text(encoding="utf-8").strip()
    bounded = _bounded_request(payload)
    attention = _attention_for(bounded)
    core_key = _core_key(bounded)
    state_path, trace_path = _paths(core_key)

    # No validator correction means a genuinely new apparatus request. Any state
    # left at this key belongs to an older execution and must not be mistaken for
    # repeatability evidence from the new request.
    if not bounded.get("correction") and state_path.exists():
        _trace(trace_path, "new_request_supersedes_local_recovery_state", "researcher_inventory_v32", detail="prior local state preserved in trace; new request starts fresh")
        state_path.unlink()

    initial_prompt = (
        "Execute only this bounded request under your installed durable V32 contract and supplied neutral apparatus rules. "
        "Return ONLY the JSON value required by response_schema. Do not infer or reconstruct any archetype, expected answer, expected count, evaluator preference, prior scored output, case-specific correction, sealed holdout source, or holdout output.\n\n"
        "TASK ATTENTION:\n" + attention + "\n\n"
        "REQUEST JSON:\n" + json.dumps(bounded, ensure_ascii=False)
    )

    try:
        provisional = _session(
            agent_id,
            initial_prompt,
            "researcher_inventory_v32_extract",
            state_path,
            trace_path,
            "provisional",
        )

        verify_prompt = (
            "Perform a separate V32 adjudication in a new session. Re-read the complete source and independently rebuild the requested result BEFORE comparing with the provisional output. "
            "Use this order: (1) material source structure; (2) primary semantic home; (3) THIS-class material research-coordinate gate; (4) class grain; (5) coreference/duplicates; (6) omission pass; (7) EXCESS and cross-class-restatement pass; (8) exact literal-span/order check. "
            "Do not preserve a candidate merely because it is semantically possible, grammatically valid, concrete, descriptive, temporal, or predicate-like. VERB uses research-relation packages, not lexical predicate atomization. LOCATOR is spatial/orienting, not generic context. "
            "Do not target a count. Return the complete replacement JSON, not a critique.\n\n"
            "TASK ATTENTION:\n" + attention + "\n\n"
            "REQUEST JSON:\n" + json.dumps(bounded, ensure_ascii=False) + "\n\n"
            "PROVISIONAL_UNSCORED_OUTPUT:\n" + json.dumps(provisional, ensure_ascii=False)
        )
        verified = _session(
            agent_id,
            verify_prompt,
            "researcher_inventory_v32_adjudication",
            state_path,
            trace_path,
            "verified",
        )
    except SessionUncertain:
        # Keep state so the apparatus retry resumes the exact backend session.
        raise
    except Exception:
        # A confirmed non-timeout failure is eligible for a fresh corrected attempt.
        if state_path.exists():
            state_path.unlink()
        raise

    if state_path.exists():
        state_path.unlink()
    sys.stdout.write(json.dumps(verified, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
