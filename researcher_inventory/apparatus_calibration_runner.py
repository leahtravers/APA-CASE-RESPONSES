#!/usr/bin/env python3
"""Hidden evaluator for the mechanical Researcher Inventory apparatus.

The worker/apparatus never receives archetypes. This runner does. The immutable
Case 2 and Case 6 workbook hashes are checked before any canonical extract is used.
Every attempt is appended to runtime history for later database ingestion.

The comparator aligns units by class + normalized tag before checking canonical
ordering. This prevents one early omission from creating a false cascade of tag
mismatches for every later reference while still testing resolution, typing,
ordering, Q, lexical preservation, and compound construction independently.
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
CONTRACT_VERSION = os.environ.get("CONTRACT_VERSION", "RI-CONTRACT-V10")
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
    actual_units = list(payload["units"])

    expected_order = list(expected_units)
    unmatched_expected = set(expected_order)
    unmatched_actual = set(range(len(actual_units)))
    actual_to_expected: dict[str, str] = {}
    expected_to_actual: dict[str, str] = {}

    # First align exact semantic identity: same class + same normalized tag.
    for i, actual in enumerate(actual_units):
        atag = norm(actual.get("researcher_short_tag"))
        candidates = [
            ref for ref in expected_order
            if ref in unmatched_expected
            and expected_units[ref]["c"] == actual.get("unit_class")
            and norm(expected_units[ref]["g"]) == atag
        ]
        if len(candidates) == 1:
            ref = candidates[0]
            actual_to_expected[actual["unit_ref"]] = ref
            expected_to_actual[ref] = actual["unit_ref"]
            unmatched_expected.remove(ref)
            unmatched_actual.remove(i)

    # Then detect class/type errors without turning them into missing+extra cascades.
    for i in list(unmatched_actual):
        actual = actual_units[i]
        atag = norm(actual.get("researcher_short_tag"))
        candidates = [
            ref for ref in expected_order
            if ref in unmatched_expected and norm(expected_units[ref]["g"]) == atag
        ]
        if len(candidates) == 1:
            ref = candidates[0]
            expected = expected_units[ref]
            findings.append((
                "TYPE_MISMATCH",
                f"{actual['unit_ref']} tag {actual['researcher_short_tag']!r} typed {actual.get('unit_class')} but archetype types it {expected['c']} ({ref})",
            ))
            actual_to_expected[actual["unit_ref"]] = ref
            expected_to_actual[ref] = actual["unit_ref"]
            unmatched_expected.remove(ref)
            unmatched_actual.remove(i)

    for ref in expected_order:
        if ref in unmatched_expected:
            expected = expected_units[ref]
            findings.append(("MISSING_UNIT", f"missing {ref} [{expected['c']}] {expected['g']}"))

    for i in sorted(unmatched_actual):
        actual = actual_units[i]
        findings.append(("EXTRA_UNIT", f"extra {actual['unit_ref']} [{actual['unit_class']}] {actual['researcher_short_tag']}"))

    # Q is evaluated only on semantically aligned coordinates.
    by_actual_ref = {u["unit_ref"]: u for u in actual_units}
    for expected_ref, actual_ref in expected_to_actual.items():
        expected = expected_units[expected_ref]
        if "q" in expected and bool(by_actual_ref[actual_ref]["qualities_available"]) != bool(expected["q"]):
            findings.append(("BAD_Q_FLAG", f"Q mismatch {expected_ref} ({expected['g']})"))

    # Ordering is a separate diagnostic, not a cascade of false tag mismatches.
    classes = []
    for ref in expected_order:
        cls = expected_units[ref]["c"]
        if cls not in classes:
            classes.append(cls)
    for cls in classes:
        expected_cls = [ref for ref in expected_order if expected_units[ref]["c"] == cls and ref in expected_to_actual]
        actual_cls_refs = []
        for actual in actual_units:
            mapped = actual_to_expected.get(actual["unit_ref"])
            if mapped and expected_units[mapped]["c"] == cls and actual["unit_class"] == cls:
                actual_cls_refs.append(mapped)
        if actual_cls_refs != expected_cls:
            findings.append((
                "ORDERING_MISMATCH",
                f"{cls} semantic order {actual_cls_refs} != archetype order {expected_cls}",
            ))

    # Translate actual compound refs into archetype semantic refs before comparing.
    mapped_compounds = {}
    for compound in payload["compounds"]:
        refs = compound.get("referenced_unit_refs", [])
        if any(ref not in actual_to_expected for ref in refs):
            missing = [ref for ref in refs if ref not in actual_to_expected]
            findings.append(("BAD_COMPOUND", f"compound {compound.get('compound_ref')} uses unmatched unit refs {missing}"))
            continue
        mapped_refs = [actual_to_expected[ref] for ref in refs]
        expression = "_".join(mapped_refs) + ("_Q" if bool(compound.get("qualities_available")) else "")
        mapped_compounds[expression] = compound

    for expression in expected_compounds:
        if expression not in mapped_compounds:
            findings.append(("BAD_COMPOUND", f"missing semantic compound {expression}"))
    for expression in mapped_compounds:
        if expression not in expected_compounds:
            findings.append(("BAD_COMPOUND", f"extra semantic compound {expression}"))

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
