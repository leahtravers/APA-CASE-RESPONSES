#!/usr/bin/env python3
"""Hidden evaluator for the mechanical Researcher Inventory apparatus.

The worker/apparatus never receives archetypes. This runner does. The immutable
Case 2 and Case 6 workbook hashes are checked before any canonical extract is used.
Every attempt is appended to runtime history for later database ingestion.

The evaluator must not require the worker to guess a hidden archetype's editor-only
short-tag wording.  It therefore aligns coordinates mechanically from class,
source-near tag wording, and source evidence before it judges type, order, Q, and
compound construction.  Gold rows and evaluator findings never enter worker input.
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

# Generic function words and evaluator-only descriptor words are weak evidence for
# semantic identity.  Removing them prevents a phrase such as "place of ..." from
# matching another place merely because both are places.
WEAK_TOKENS = {
    "a", "an", "the", "and", "or", "but", "of", "to", "for", "from", "in", "on", "at", "with", "by",
    "is", "are", "was", "were", "be", "been", "being", "it", "this", "that", "these", "those",
    "b", "place", "places", "time", "times", "episode", "period", "setting", "scene", "frame",
    "exact", "specified", "unspecified", "not", "source", "represented", "current", "later", "earlier",
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


def tokens(v):
    return {
        t for t in re.findall(r"[a-z0-9$]+(?:'[a-z0-9]+)?", norm(v))
        if t not in WEAK_TOKENS and len(t) > 1
    }


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


def _actual_evidence(unit):
    return " ".join(str(unit.get(k) or "") for k in (
        "researcher_short_tag", "source_wording", "source_cue", "researcher_note"
    ))


def _expected_evidence(row):
    return f"{row.get('g', '')} {row.get('s', '')}"


def alignment_score(actual, expected):
    """Mechanical source-evidence similarity; never shown to the worker.

    Exact tag identity remains strongest.  Containment and shared content-bearing
    source words allow a source-near worker tag to align with an editor shorthand
    or an unnamed coordinate description without teaching the worker that wording.
    """
    atag = norm(actual.get("researcher_short_tag"))
    etag = norm(expected.get("g"))
    if atag and atag == etag:
        return 1000.0
    if atag and etag and min(len(atag), len(etag)) >= 4 and (atag in etag or etag in atag):
        return 850.0

    ae = tokens(_actual_evidence(actual))
    ee = tokens(_expected_evidence(expected))
    if not ae or not ee:
        return 0.0
    shared = ae & ee
    if not shared:
        return 0.0

    # Coverage of the smaller evidence set rewards phrases that refer to the same
    # coordinate even when one side is a longer source cue. Jaccard breaks ties.
    coverage = len(shared) / min(len(ae), len(ee))
    jaccard = len(shared) / len(ae | ee)
    return 500.0 * coverage + 200.0 * jaccard + min(len(shared), 6)


def align_units(actual_units, expected_units):
    """Return actual<->expected mappings without requiring hidden tag phrasing.

    Matching is class-bounded and monotonic enough for duplicate literal tags:
    exact duplicate tags pair in their source order; remaining rows use a unique
    best source-evidence match. Ambiguous weak matches are deliberately left
    unmatched so the evaluator reports them rather than silently guessing.
    """
    expected_order = list(expected_units)
    unmatched_expected = set(expected_order)
    unmatched_actual = set(range(len(actual_units)))
    actual_to_expected: dict[str, str] = {}
    expected_to_actual: dict[str, str] = {}

    # Pair exact class+tag groups in source order, including repeated tags such as
    # repeated speech predicates. This avoids refusing all duplicate exact matches.
    for cls in dict.fromkeys(expected_units[r]["c"] for r in expected_order):
        tags = []
        for ref in expected_order:
            if expected_units[ref]["c"] == cls:
                tag = norm(expected_units[ref]["g"])
                if tag not in tags:
                    tags.append(tag)
        for tag in tags:
            egroup = [r for r in expected_order if r in unmatched_expected and expected_units[r]["c"] == cls and norm(expected_units[r]["g"]) == tag]
            agroup = [i for i in sorted(unmatched_actual) if actual_units[i].get("unit_class") == cls and norm(actual_units[i].get("researcher_short_tag")) == tag]
            for i, ref in zip(agroup, egroup):
                actual_ref = actual_units[i]["unit_ref"]
                actual_to_expected[actual_ref] = ref
                expected_to_actual[ref] = actual_ref
                unmatched_actual.remove(i)
                unmatched_expected.remove(ref)

    # Source-evidence alignment inside the same class. Require meaningful lexical
    # evidence and a clear best candidate; do not force a match on weak ambiguity.
    progress = True
    while progress:
        progress = False
        proposals = []
        for i in sorted(unmatched_actual):
            actual = actual_units[i]
            candidates = []
            for ref in expected_order:
                if ref not in unmatched_expected or expected_units[ref]["c"] != actual.get("unit_class"):
                    continue
                score = alignment_score(actual, expected_units[ref])
                if score > 0:
                    candidates.append((score, ref))
            candidates.sort(reverse=True)
            if not candidates:
                continue
            best_score, best_ref = candidates[0]
            second_score = candidates[1][0] if len(candidates) > 1 else 0.0
            # 260 corresponds to substantial shared source evidence. For a lower
            # score, demand a much larger margin so generic wording cannot align.
            threshold = 260.0
            margin = 35.0
            if best_score >= threshold and best_score - second_score >= margin:
                proposals.append((best_score, -i, i, best_ref))

        # Resolve collisions by strongest evidence first, then source order.
        for _, _, i, ref in sorted(proposals, reverse=True):
            if i not in unmatched_actual or ref not in unmatched_expected:
                continue
            actual_ref = actual_units[i]["unit_ref"]
            actual_to_expected[actual_ref] = ref
            expected_to_actual[ref] = actual_ref
            unmatched_actual.remove(i)
            unmatched_expected.remove(ref)
            progress = True

    return actual_to_expected, expected_to_actual, unmatched_actual, unmatched_expected


def evaluate(payload, fixture):
    findings = []
    expected_units, expected_compounds = load_archetype(fixture["name"])
    actual_units = list(payload["units"])

    expected_order = list(expected_units)
    actual_to_expected, expected_to_actual, unmatched_actual, unmatched_expected = align_units(actual_units, expected_units)

    # Detect class/type errors among still-unmatched rows by strongest tag/evidence
    # match across classes. This remains diagnostic only and never changes worker input.
    for i in list(sorted(unmatched_actual)):
        actual = actual_units[i]
        scored = []
        for ref in expected_order:
            if ref not in unmatched_expected:
                continue
            score = alignment_score(actual, expected_units[ref])
            if score > 0:
                scored.append((score, ref))
        scored.sort(reverse=True)
        if not scored:
            continue
        best_score, ref = scored[0]
        second = scored[1][0] if len(scored) > 1 else 0.0
        expected = expected_units[ref]
        if best_score >= 500 and best_score - second >= 80 and expected["c"] != actual.get("unit_class"):
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
