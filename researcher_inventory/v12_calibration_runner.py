#!/usr/bin/env python3
"""V12 calibration entry point with evaluator-only normalization and safe diagnostics.

This module preserves the V11/V12 evaluator-alignment repairs. It does not alter
worker input, the V12 durable contract, gold archetypes, or holdout handling.
Cross-class type diagnostics are deliberately non-consuming: they may describe an
exact-tag class disagreement, but they never steal a gold coordinate from the
same-class alignment used for missing/extra/order/Q/compound evaluation.
"""
from __future__ import annotations

import json
import re

from researcher_inventory import apparatus_calibration_runner as base


_EXTRA_WEAK = {"when", "where", "who", "whose", "which", "while"}


def _lemma(token: str) -> str:
    """Tiny deterministic normalizer for source/evaluator inflection mismatches."""
    t = token
    if len(t) > 5 and t.endswith("ies"):
        return t[:-3] + "y"
    if len(t) > 4 and t.endswith("ied"):
        return t[:-3] + "y"
    if len(t) > 4 and t.endswith("ed"):
        stem = t[:-2]
        # explained -> explain, moved -> move; walked -> walk
        if stem.endswith(("at", "it", "iz", "ur")):
            return stem + "e"
        return stem
    if len(t) > 4 and t.endswith("es") and not t.endswith(("ses", "xes", "zes")):
        return t[:-1]
    if len(t) > 3 and t.endswith("s") and not t.endswith(("ss", "us", "is")):
        return t[:-1]
    return t


def tokens(v):
    raw = re.findall(r"[a-z0-9$]+(?:'[a-z0-9]+)?", base.norm(v))
    out = set()
    for token in raw:
        if token in base.WEAK_TOKENS or token in _EXTRA_WEAK or len(token) <= 1:
            continue
        out.add(_lemma(token))
    return out


# Evaluator-only lexical patch. The worker never imports this module.
base.tokens = tokens


def evaluate(payload, fixture):
    """Evaluate without allowing cross-class diagnostics to mutate alignment.

    Same-class semantic alignment is the only alignment that can participate in
    pass/fail structure, Q, ordering, or compound translation. A cross-class
    TYPE_MISMATCH is emitted only for an exact normalized tag collision and is
    purely diagnostic. This avoids cascading a fuzzy source-cue resemblance into
    false type, order, and compound mappings.
    """
    findings = []
    expected_units, expected_compounds = base.load_archetype(fixture["name"])
    actual_units = list(payload["units"])

    expected_order = list(expected_units)
    actual_to_expected, expected_to_actual, unmatched_actual, unmatched_expected = base.align_units(
        actual_units, expected_units
    )

    # Diagnostic only. Never consume either side of the same-class mapping pool.
    # Exact tag identity is intentionally required because source cues can overlap
    # across legitimate cross-class coordinates (e.g. a scene, episode and verb).
    for i in sorted(unmatched_actual):
        actual = actual_units[i]
        atag = base.norm(actual.get("researcher_short_tag"))
        if not atag:
            continue
        exact_cross = [
            ref for ref in expected_order
            if ref in unmatched_expected
            and expected_units[ref]["c"] != actual.get("unit_class")
            and base.norm(expected_units[ref].get("g")) == atag
        ]
        if len(exact_cross) == 1:
            ref = exact_cross[0]
            expected = expected_units[ref]
            findings.append((
                "TYPE_MISMATCH",
                f"{actual['unit_ref']} tag {actual['researcher_short_tag']!r} typed {actual.get('unit_class')} but archetype types the exact tag {expected['c']} ({ref})",
            ))

    for ref in expected_order:
        if ref in unmatched_expected:
            expected = expected_units[ref]
            findings.append(("MISSING_UNIT", f"missing {ref} [{expected['c']}] {expected['g']}"))

    for i in sorted(unmatched_actual):
        actual = actual_units[i]
        findings.append(("EXTRA_UNIT", f"extra {actual['unit_ref']} [{actual['unit_class']}] {actual['researcher_short_tag']}"))

    # Q is evaluated only on same-class semantically aligned coordinates.
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
        expected_cls = [
            ref for ref in expected_order
            if expected_units[ref]["c"] == cls and ref in expected_to_actual
        ]
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

    # Translate compounds only through same-class semantic alignment.
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

    searchable = base.norm(json.dumps(payload, ensure_ascii=False))
    for phrase in fixture.get("must_preserve", []):
        if base.norm(phrase) not in searchable:
            findings.append(("SOURCE_FLATTENING", f"missing source phrase {phrase!r}"))
    for phrase in fixture.get("must_not_introduce", []):
        if base.norm(phrase) in searchable:
            findings.append(("OVER_NORMALIZATION", f"introduced forbidden normalization {phrase!r}"))
    return findings


# Evaluator-only structural patch. Worker input and contract remain unchanged.
base.evaluate = evaluate


if __name__ == "__main__":
    base.main()
