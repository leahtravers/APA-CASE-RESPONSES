"""Calibrate the Researcher Inventory agent against Leah-approved archetypes.

The approved archetype extracts, not loose unit-count ranges, define the expected
resolution. Every attempt is retained as training data, including failures.
"""
from __future__ import annotations

import json
import os
import re
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

API = "https://api.openai.com/v1"
AGENT_ID_FILE = Path("researcher_inventory/runtime/agent_id.txt")
FIXTURES = Path("researcher_inventory/tests/fixtures.json")
RESULTS = Path("researcher_inventory/runtime/test_results.json")
ARCHETYPES = Path("researcher_inventory/tests/archetypes")
CONTRACT_VERSION = os.environ.get("CONTRACT_VERSION", "RI-CONTRACT-V2")
MODEL_REF = os.environ.get("OPENAI_MODEL", "gpt-5.6-sol")
ALLOWED_CLASSES = {"PLACE", "TIME", "PERSON", "OBJECT", "LABEL", "VERB", "LOCATOR"}
TOP_KEYS = {"candidate", "units", "compounds", "validation"}
VALIDATION_KEYS = {
    "source_language_preserved",
    "lightweight_resolution_preserved",
    "all_compound_refs_registered",
    "forbidden_work_avoided",
    "notes",
}

ARCHETYPE_FILES = {
    "coupon_case": [ARCHETYPES / "coupon_case_archetype.ndjson"],
    "oil_change_case": [
        ARCHETYPES / "oil_change_case_archetype_part1.ndjson",
        ARCHETYPES / "oil_change_case_archetype_part2.ndjson",
    ],
}


def request(path: str, method: str = "GET", body=None):
    key = os.environ.get("OPENAI_API_KEY", "").strip()
    if not key:
        raise RuntimeError("OPENAI_API_KEY is required")
    headers = {
        "Authorization": f"Bearer {key}",
        "Content-Type": "application/json",
        "Accept": "application/json",
        "OpenAI-Beta": "agents=v1",
    }
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(API + path, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=180) as response:
            raw = response.read()
            return json.loads(raw) if raw.strip() else None
    except urllib.error.HTTPError as exc:
        detail = f"HTTP {exc.code}"
        try:
            raw = exc.read(4096)
            payload = json.loads(raw) if raw else {}
            err = payload.get("error", {}) if isinstance(payload, dict) else {}
            detail += ": " + (err.get("message") or "")[:350]
        except Exception:
            pass
        raise RuntimeError(f"OpenAI request failed with {detail}") from None


def wait_for_terminal(session_id: str, timeout_seconds: int = 360):
    deadline = time.time() + timeout_seconds
    while time.time() < deadline:
        state = request(f"/agents/sessions/{session_id}")
        status = state.get("status")
        if status == "idle":
            return
        if status in ("failed", "requires_action"):
            raise RuntimeError(f"Session terminal status: {status}")
        time.sleep(2)
    raise RuntimeError("Session did not return to idle before timeout")


def final_answer(session_id: str) -> str:
    query = urllib.parse.urlencode({"order": "asc", "limit": 100})
    page = request(f"/agents/sessions/{session_id}/items?{query}")
    answers = []
    for item in page.get("data", []):
        if item.get("type") != "message" or item.get("role") != "assistant":
            continue
        if item.get("status") != "completed" or item.get("phase") != "final_answer":
            continue
        for part in item.get("content", []):
            if part.get("type") == "output_text":
                answers.append(part.get("text", ""))
    if not answers:
        raise RuntimeError("No completed assistant final answer found")
    return "\n".join(answers).strip()


def norm(value) -> str:
    if value is None:
        return ""
    s = unicodedata.normalize("NFKC", str(value)).lower()
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    s = re.sub(r"\s+", " ", s).strip()
    return s


def load_archetype(name: str):
    units = {}
    compounds = {}
    for path in ARCHETYPE_FILES[name]:
        for line in path.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            row = json.loads(line)
            if row["t"] == "u":
                units[row["r"]] = row
            elif row["t"] == "c":
                compounds[row["e"]] = row
    return units, compounds


def finding(kind: str, message: str):
    return (kind, message)


def validate_exact_schema(payload: dict, fixture: dict, iteration: int):
    failures = []
    if not isinstance(payload, dict):
        return [finding("SCHEMA_VIOLATION", "top-level output is not a JSON object")]
    keys = set(payload.keys())
    if keys != TOP_KEYS:
        failures.append(finding("SCHEMA_VIOLATION", f"top-level keys {sorted(keys)} != {sorted(TOP_KEYS)}"))
        return failures

    candidate = payload.get("candidate")
    if not isinstance(candidate, dict):
        failures.append(finding("SCHEMA_VIOLATION", "candidate is not an object"))
    else:
        required = {"candidate_ref", "source_case_text", "created_by_ref"}
        missing = required - set(candidate)
        if missing:
            failures.append(finding("SCHEMA_VIOLATION", f"candidate missing fields: {sorted(missing)}"))
        expected_ref = f"{fixture['candidate_ref']}-R{iteration}"
        if candidate.get("candidate_ref") != expected_ref:
            failures.append(finding("SCHEMA_VIOLATION", f"candidate_ref {candidate.get('candidate_ref')!r} != {expected_ref!r}"))
        if candidate.get("source_case_text") != fixture["case_text"]:
            failures.append(finding("SCHEMA_VIOLATION", "candidate.source_case_text is not the supplied case text verbatim"))
        if not str(candidate.get("created_by_ref") or "").strip():
            failures.append(finding("SCHEMA_VIOLATION", "candidate.created_by_ref is empty"))

    units = payload.get("units")
    if not isinstance(units, list):
        failures.append(finding("SCHEMA_VIOLATION", "units is not an array"))
    else:
        for i, unit in enumerate(units):
            if not isinstance(unit, dict):
                failures.append(finding("SCHEMA_VIOLATION", f"units[{i}] is not an object"))
                continue
            required = {"unit_ref", "unit_class", "researcher_short_tag", "qualities_available"}
            missing = required - set(unit)
            if missing:
                failures.append(finding("SCHEMA_VIOLATION", f"units[{i}] missing fields: {sorted(missing)}"))
            if unit.get("unit_class") not in ALLOWED_CLASSES:
                failures.append(finding("SCHEMA_VIOLATION", f"units[{i}] has invalid unit_class {unit.get('unit_class')!r}"))

    compounds = payload.get("compounds")
    if not isinstance(compounds, list):
        failures.append(finding("SCHEMA_VIOLATION", "compounds is not an array"))
    else:
        for i, compound in enumerate(compounds):
            if not isinstance(compound, dict):
                failures.append(finding("SCHEMA_VIOLATION", f"compounds[{i}] is not an object"))
                continue
            required = {"compound_ref", "compound_expression", "referenced_unit_refs", "qualities_available"}
            missing = required - set(compound)
            if missing:
                failures.append(finding("SCHEMA_VIOLATION", f"compounds[{i}] missing fields: {sorted(missing)}"))

    validation = payload.get("validation")
    if not isinstance(validation, dict):
        failures.append(finding("SCHEMA_VIOLATION", "validation is not an object"))
    else:
        if set(validation.keys()) != VALIDATION_KEYS:
            failures.append(finding("SCHEMA_VIOLATION", f"validation keys {sorted(validation.keys())} != {sorted(VALIDATION_KEYS)}"))
        for key in VALIDATION_KEYS - {"notes"}:
            if validation.get(key) is not True:
                failures.append(finding("SCHEMA_VIOLATION", f"self-validation failed: {key}"))
        if not isinstance(validation.get("notes"), list):
            failures.append(finding("SCHEMA_VIOLATION", "validation.notes is not an array"))
    return failures


def validate_archetype(payload: dict, fixture: dict):
    failures = []
    expected_units, expected_compounds = load_archetype(fixture["name"])
    units = payload["units"]
    compounds = payload["compounds"]

    actual_units = {}
    for unit in units:
        ref = unit.get("unit_ref")
        if ref in actual_units:
            failures.append(finding("SCHEMA_VIOLATION", f"duplicate unit_ref: {ref}"))
        actual_units[ref] = unit

    # Exact archetypal coordinate coverage and canonical IDs.
    for ref, expected in expected_units.items():
        actual = actual_units.get(ref)
        if actual is None:
            failures.append(finding("MISSING_UNIT", f"missing archetype unit {ref} [{expected['c']}] {expected['g']}"))
            continue
        if actual.get("unit_class") != expected["c"]:
            failures.append(finding("OTHER", f"class mismatch {ref}: {actual.get('unit_class')} != {expected['c']}"))
        if norm(actual.get("researcher_short_tag")) != norm(expected["g"]):
            failures.append(finding("OTHER", f"tag mismatch {ref}: {actual.get('researcher_short_tag')!r} != archetype {expected['g']!r}"))

    for ref, actual in actual_units.items():
        if ref not in expected_units:
            failures.append(finding("EXTRA_UNIT", f"extra unit outside archetype resolution: {ref} [{actual.get('unit_class')}] {actual.get('researcher_short_tag')}"))

    if len(actual_units) != len(expected_units):
        kind = "UNDER_GRANULARITY" if len(actual_units) < len(expected_units) else "OVER_GRANULARITY"
        failures.append(finding(kind, f"unit count {len(actual_units)} != approved archetype {len(expected_units)}"))

    # Every compound must refer to registered units.
    refs = set(actual_units)
    for compound in compounds:
        for ref in compound.get("referenced_unit_refs", []):
            if ref not in refs:
                failures.append(finding("BAD_COMPOUND", f"compound {compound.get('compound_ref')} references unknown unit {ref}"))

    actual_compounds = {c.get("compound_expression"): c for c in compounds}
    for expression, expected in expected_compounds.items():
        actual = actual_compounds.get(expression)
        if actual is None:
            failures.append(finding("BAD_COMPOUND", f"missing archetype compound {expression}"))
            continue
        if bool(actual.get("qualities_available")) != bool(expected.get("q")):
            failures.append(finding("BAD_Q_FLAG", f"compound Q mismatch {expression}: {actual.get('qualities_available')} != {expected.get('q')}"))

    for expression in actual_compounds:
        if expression not in expected_compounds:
            failures.append(finding("BAD_COMPOUND", f"extra compound outside archetype: {expression}"))

    if len(actual_compounds) != len(expected_compounds):
        failures.append(finding("BAD_COMPOUND", f"compound count {len(actual_compounds)} != approved archetype {len(expected_compounds)}"))

    searchable = norm(json.dumps(payload, ensure_ascii=False))
    for phrase in fixture.get("must_preserve", []):
        if norm(phrase) not in searchable:
            failures.append(finding("SOURCE_FLATTENING", f"missing preserved source phrase: {phrase}"))
    for phrase in fixture.get("must_not_introduce", []):
        if norm(phrase) in searchable:
            failures.append(finding("OVER_NORMALIZATION", f"introduced forbidden normalization: {phrase}"))

    return failures


def classify(kind: str) -> str:
    if kind in {
        "SCHEMA_VIOLATION", "SOURCE_FLATTENING", "OVER_NORMALIZATION", "OVER_GRANULARITY",
        "UNDER_GRANULARITY", "MISSING_UNIT", "EXTRA_UNIT", "BAD_COMPOUND", "BAD_Q_FLAG",
    }:
        return kind
    return "OTHER"


def run_fixture(agent_id: str, fixture: dict, iteration: int):
    started = time.time()
    training_run_ref = f"TRAIN-{fixture['name']}-R{iteration}-{int(started)}"
    prompt = (
        "Prepare researcher inventory. Return ONLY the exact JSON object required by your contract. "
        "Do not describe your work. Before answering, silently perform a second source pass for omitted "
        "places, times, people, independently selectable objects, labels, verbs, and locators.\n\n"
        f"Candidate ref: {fixture['candidate_ref']}-R{iteration}\n"
        f"Researcher interest: {fixture.get('researcher_interest') or 'none supplied'}\n\n"
        "CASE TEXT:\n" + fixture["case_text"]
    )
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
                    "apa_session_type": "researcher_inventory_calibration",
                    "fixture": fixture["name"],
                    "iteration": str(iteration),
                    "training_run_ref": training_run_ref,
                    "contract_version": CONTRACT_VERSION,
                },
            },
        )
        session_id = session["id"]
        wait_for_terminal(session_id)
        raw = final_answer(session_id)
        try:
            payload = json.loads(raw)
        except json.JSONDecodeError:
            failures = [finding("SCHEMA_VIOLATION", "final answer was not bare valid JSON")]
        else:
            failures.extend(validate_exact_schema(payload, fixture, iteration))
            if not failures:
                failures.extend(validate_archetype(payload, fixture))
    except Exception as exc:
        failures = [finding("OTHER", f"runtime failure: {type(exc).__name__}: {exc}")]

    findings = [
        {
            "finding_ref": f"{training_run_ref}-F{i+1}",
            "finding_class": classify(kind),
            "severity": "ERROR",
            "expected_behavior": "match Leah-approved Researcher Inventory archetype and exact schema",
            "observed_behavior": message,
        }
        for i, (kind, message) in enumerate(failures)
    ]
    finished = time.time()
    candidate_ref = None
    if isinstance(payload, dict) and isinstance(payload.get("candidate"), dict):
        candidate_ref = payload["candidate"].get("candidate_ref")
    return {
        "training_run_ref": training_run_ref,
        "contract_version_ref": CONTRACT_VERSION,
        "fixture": fixture["name"],
        "source_case_ref": fixture.get("source_case_ref"),
        "source_case_text": fixture["case_text"],
        "researcher_interest": fixture.get("researcher_interest"),
        "model_ref": MODEL_REF,
        "session_ref": session_id,
        "attempt_no": iteration,
        "run_status": "COMPLETED" if not failures else "FAILED",
        "candidate_ref": candidate_ref,
        "raw_output_text": raw,
        "raw_output": payload,
        "findings": findings,
        "pass": not failures,
        "started_unix": started,
        "finished_unix": finished,
    }


def main():
    agent_id = AGENT_ID_FILE.read_text(encoding="utf-8").strip()
    fixtures = json.loads(FIXTURES.read_text(encoding="utf-8"))
    repetitions = int(os.environ.get("TEST_REPETITIONS", "2"))
    results = []
    for fixture in fixtures:
        if fixture["name"] not in ARCHETYPE_FILES:
            raise RuntimeError(f"Calibration fixture {fixture['name']} has no approved archetype")
        for iteration in range(1, repetitions + 1):
            result = run_fixture(agent_id, fixture, iteration)
            results.append(result)
            bounded = {k: v for k, v in result.items() if k not in ("raw_output_text", "source_case_text", "raw_output")}
            print(json.dumps(bounded, ensure_ascii=False))
    RESULTS.parent.mkdir(parents=True, exist_ok=True)
    RESULTS.write_text(json.dumps(results, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    if not all(r["pass"] for r in results):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
