"""Run the sealed Case 5 holdout only after archetype calibration passes.

This file is deliberately not called by the calibration runner. The agent receives
only the case text and finalized contract, never the external evaluation rubric.
"""
from __future__ import annotations

import json
import os
import re
import time
from pathlib import Path

from test_runner import (
    AGENT_ID_FILE,
    CONTRACT_VERSION,
    MODEL_REF,
    final_answer,
    norm,
    request,
    validate_exact_schema,
    wait_for_terminal,
)

SEALED = Path("researcher_inventory/tests/holdout/CASE_5.sealed.txt")
RUBRIC = Path("researcher_inventory/tests/holdout/CASE_5.eval.json")
RESULT = Path("researcher_inventory/runtime/holdout_result.json")


def case_text() -> str:
    text = SEALED.read_text(encoding="utf-8")
    start = text.index("Ugh,")
    return text[start:].strip()


def prefix_ok(ref: str, unit_class: str) -> bool:
    if unit_class == "PERSON":
        return ref == "B" or re.fullmatch(r"H[1-9][0-9]*", ref or "") is not None
    prefix = {
        "PLACE": "P", "TIME": "T", "OBJECT": "O", "LABEL": "L",
        "VERB": "V", "LOCATOR": "R",
    }[unit_class]
    return re.fullmatch(prefix + r"[1-9][0-9]*", ref or "") is not None


def evaluate(payload: dict, rubric: dict, source: str):
    fixture = {
        "candidate_ref": rubric["candidate_ref"],
        "case_text": source,
    }
    failures = list(validate_exact_schema(payload, fixture, 1))
    if failures:
        return failures

    units = payload["units"]
    refs = set()
    counts = {}
    for unit in units:
        ref = unit["unit_ref"]
        if ref in refs:
            failures.append(("SCHEMA_VIOLATION", f"duplicate unit_ref: {ref}"))
        refs.add(ref)
        cls = unit["unit_class"]
        counts[cls] = counts.get(cls, 0) + 1
        if not prefix_ok(ref, cls):
            failures.append(("SCHEMA_VIOLATION", f"noncanonical ref {ref} for {cls}"))

    for cls, minimum in rubric["minimum_class_counts"].items():
        if counts.get(cls, 0) < minimum:
            failures.append(("UNDER_GRANULARITY", f"holdout {cls} count {counts.get(cls,0)} < minimum {minimum}"))

    for compound in payload["compounds"]:
        for ref in compound["referenced_unit_refs"]:
            if ref not in refs:
                failures.append(("BAD_COMPOUND", f"compound {compound['compound_ref']} references unknown unit {ref}"))

    searchable = norm(json.dumps(payload, ensure_ascii=False))
    for phrase in rubric["must_preserve"]:
        if norm(phrase) not in searchable:
            failures.append(("SOURCE_FLATTENING", f"holdout missing preserved phrase/cue: {phrase}"))
    for cue in rubric["required_uncertainty_cues"]:
        if norm(cue) not in searchable:
            failures.append(("SOURCE_FLATTENING", f"holdout lost uncertainty/hypothetical cue: {cue}"))
    for phrase in rubric["must_not_introduce"]:
        if norm(phrase) in searchable:
            failures.append(("OVER_NORMALIZATION", f"holdout introduced forbidden assertion/normalization: {phrase}"))
    return failures


def main():
    agent_id = AGENT_ID_FILE.read_text(encoding="utf-8").strip()
    rubric = json.loads(RUBRIC.read_text(encoding="utf-8"))
    source = case_text()
    prompt = (
        "Prepare researcher inventory. This is a new case. Return ONLY the exact JSON object required by your contract. "
        "Silently make a complete second source pass before answering. Preserve uncertainty, negation, comparison, "
        "hypothetical language, speaker labels, independently selectable objects/happenings/locators, and provisional places/times.\n\n"
        f"Candidate ref: {rubric['candidate_ref']}-R1\n"
        f"Researcher interest: {rubric['researcher_interest']}\n\n"
        "CASE TEXT:\n" + source
    )
    started = time.time()
    session_id = None
    raw = None
    payload = None
    failures = []
    try:
        session = request(
            "/agents/sessions",
            method="POST",
            body={
                "agent_id": agent_id,
                "environment": {"type": "none"},
                "input": prompt,
                "metadata": {
                    "apa_session_type": "researcher_inventory_sealed_holdout",
                    "fixture": "case_5_holdout",
                    "contract_version": CONTRACT_VERSION,
                },
            },
        )
        session_id = session["id"]
        wait_for_terminal(session_id)
        raw = final_answer(session_id)
        payload = json.loads(raw)
        failures = evaluate(payload, rubric, source)
    except Exception as exc:
        failures = [("OTHER", f"runtime/parse failure: {type(exc).__name__}: {exc}")]

    result = {
        "training_run_ref": f"HOLDOUT-case5-{int(started)}",
        "contract_version_ref": CONTRACT_VERSION,
        "fixture": "case_5_holdout",
        "model_ref": MODEL_REF,
        "session_ref": session_id,
        "run_status": "COMPLETED" if not failures else "FAILED",
        "raw_output_text": raw,
        "raw_output": payload,
        "findings": [
            {
                "finding_class": kind if kind in {
                    "SCHEMA_VIOLATION", "SOURCE_FLATTENING", "OVER_NORMALIZATION",
                    "UNDER_GRANULARITY", "BAD_COMPOUND"
                } else "OTHER",
                "observed_behavior": message,
            }
            for kind, message in failures
        ],
        "pass": not failures,
        "started_unix": started,
        "finished_unix": time.time(),
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({k:v for k,v in result.items() if k not in ("raw_output_text","raw_output")}, ensure_ascii=False))
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
