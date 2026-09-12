#!/usr/bin/env python3
"""Hidden evaluator for the mechanical Researcher Inventory apparatus.

The worker/apparatus never receives archetypes. This runner does.  The immutable
Case 2 and Case 6 workbook hashes are checked before any canonical extract is used.
Every attempt is appended to durable runtime history for later database ingestion.
"""
from __future__ import annotations

import json
import os
import time
import unicodedata
import re
from pathlib import Path

from researcher_inventory.inventory_apparatus import InventoryApparatus, CommandAdapter
from researcher_inventory.verify_archetypes import EXPECTED, ARCHETYPES as GOLD_DIR, sha256

FIXTURES = Path("researcher_inventory/tests/fixtures.json")
ARCHETYPES = Path("researcher_inventory/tests/archetypes")
RESULTS = Path("researcher_inventory/runtime/test_results.json")
HISTORY = Path("researcher_inventory/runtime/training_history.ndjson")
CONTRACT_VERSION = os.environ.get("CONTRACT_VERSION", "RI-CONTRACT-V9")
MODEL_REF = os.environ.get("OPENAI_MODEL", "unknown")
ARCHETYPE_FILES = {
    "coupon_case": [ARCHETYPES / "coupon_case_archetype.ndjson"],
    "oil_change_case": [ARCHETYPES / "oil_change_case_archetype_part1.ndjson", ARCHETYPES / "oil_change_case_archetype_part2.ndjson"],
}


def assert_gold_integrity():
    wrong = {}
    for name, expected in EXPECTED.items():
        path = GOLD_DIR / name
        actual = sha256(path) if path.exists() else None
        if actual != expected:
            wrong[name] = {"actual": actual, "expected": expected}
    if wrong:
        raise RuntimeError(f"immutable workbook hash gate failed: {wrong}")


def norm(v):
    s = unicodedata.normalize("NFKC", str(v or "")).lower()
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    return re.sub(r"\s+", " ", s).strip()


def load_archetype(name):
    assert_gold_integrity()
    units, compounds = {}, {}
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


def evaluate(payload, fixture):
    findings = []
    expected_units, expected_compounds = load_archetype(fixture["name"])
    actual_units = {u["unit_ref"]: u for u in payload["units"]}

    for ref, expected in expected_units.items():
        actual = actual_units.get(ref)
        if actual is None:
            findings.append(("MISSING_UNIT", f"missing {ref} [{expected['c']}] {expected['g']}"))
            continue
        if actual["unit_class"] != expected["c"]:
            findings.append(("OTHER", f"class mismatch {ref}: {actual['unit_class']} != {expected['c']}"))
        if norm(actual["researcher_short_tag"]) != norm(expected["g"]):
            findings.append(("OTHER", f"tag mismatch {ref}: {actual['researcher_short_tag']!r} != {expected['g']!r}"))
        if "q" in expected and bool(actual["qualities_available"]) != bool(expected["q"]):
            findings.append(("BAD_Q_FLAG", f"Q mismatch {ref}"))

    for ref, actual in actual_units.items():
        if ref not in expected_units:
            findings.append(("EXTRA_UNIT", f"extra {ref} [{actual['unit_class']}] {actual['researcher_short_tag']}"))

    actual_compounds = {c["compound_expression"]: c for c in payload["compounds"]}
    for expression in expected_compounds:
        if expression not in actual_compounds:
            findings.append(("BAD_COMPOUND", f"missing compound {expression}"))
    for expression in actual_compounds:
        if expression not in expected_compounds:
            findings.append(("BAD_COMPOUND", f"extra compound {expression}"))

    searchable = norm(json.dumps(payload, ensure_ascii=False))
    for phrase in fixture.get("must_preserve", []):
        if norm(phrase) not in searchable:
            findings.append(("SOURCE_FLATTENING", f"missing source phrase {phrase!r}"))
    for phrase in fixture.get("must_not_introduce", []):
        if norm(phrase) in searchable:
            findings.append(("OVER_NORMALIZATION", f"introduced forbidden normalization {phrase!r}"))
    return findings


def append_history(result):
    HISTORY.parent.mkdir(parents=True, exist_ok=True)
    with HISTORY.open("a", encoding="utf-8") as f:
        f.write(json.dumps(result, ensure_ascii=False) + "\n")


def run_one(app, fixture, iteration):
    started = time.time()
    ref = f"TRAIN-APP-{fixture['name']}-R{iteration}-{time.time_ns()}"
    payload = None
    findings = []
    try:
        payload = app.run(
            fixture["case_text"],
            source_case_ref=fixture.get("source_case_ref") or fixture["name"],
            researcher_interest=fixture.get("researcher_interest"),
            created_by_ref="RI-APPARATUS",
        )
        findings = evaluate(payload, fixture)
    except Exception as exc:
        findings = [("OTHER", f"runtime failure: {type(exc).__name__}: {exc}")]
    result = {
        "training_run_ref": ref,
        "contract_version_ref": CONTRACT_VERSION,
        "fixture": fixture["name"],
        "source_case_ref": fixture.get("source_case_ref") or fixture["name"],
        "source_case_text": fixture["case_text"],
        "researcher_interest": fixture.get("researcher_interest"),
        "model_ref": MODEL_REF,
        "session_ref": None,
        "attempt_no": iteration,
        "run_status": "COMPLETED" if not findings else "FAILED",
        "candidate_ref": payload.get("candidate", {}).get("candidate_ref") if payload else None,
        "raw_output": payload,
        "findings": [
            {
                "finding_ref": f"{ref}-F{i+1}",
                "finding_class": kind,
                "severity": "ERROR",
                "expected_behavior": "match hidden Leah-approved Researcher Inventory archetype without worker access to that archetype",
                "observed_behavior": message,
            }
            for i, (kind, message) in enumerate(findings)
        ],
        "pass": not findings,
        "started_unix": started,
        "finished_unix": time.time(),
    }
    append_history(result)
    print(json.dumps({k: v for k, v in result.items() if k not in ("raw_output", "source_case_text")}, ensure_ascii=False))
    return result


def main():
    assert_gold_integrity()
    command = os.environ.get("RI_MODEL_COMMAND", "python researcher_inventory/openai_agents_adapter.py")
    app = InventoryApparatus(CommandAdapter(command), retries=2)
    fixtures = json.loads(FIXTURES.read_text(encoding="utf-8"))
    reps = int(os.environ.get("TEST_REPETITIONS", "2"))
    results = []
    for fixture in fixtures:
        if fixture["name"] not in ARCHETYPE_FILES:
            continue
        for i in range(1, reps + 1):
            results.append(run_one(app, fixture, i))
    RESULTS.parent.mkdir(parents=True, exist_ok=True)
    RESULTS.write_text(json.dumps(results, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    if not results or not all(r["pass"] for r in results):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
