#!/usr/bin/env python3
"""V64 evaluator-only correction for semantic compound membership ordering.

The hidden evaluator maps worker unit references to archetype semantic references.
Compound identity is defined by the mapped primitive membership plus the compound Q
state, not by the worker's internal serialization order.  This wrapper removes only
paired missing/extra compound findings whose mapped reference multisets and Q state
are identical.  It does not alter worker instructions, primitive evaluation, Q
semantics, unmatched-reference findings, or genuine compound membership errors.
"""
from __future__ import annotations

from collections import defaultdict, deque
import re

from researcher_inventory import v64_calibration_runner as v64

base = v64.v52.v34.base
_OriginalEvaluate = base.evaluate

_MISSING = re.compile(r"^missing semantic compound (.+)$")
_EXTRA = re.compile(r"^extra semantic compound (.+)$")


def canonical_semantic_compound(expression: str) -> tuple[tuple[str, ...], bool]:
    """Return order-insensitive semantic membership while preserving multiplicity/Q."""
    expression = str(expression or "").strip()
    q = expression.endswith("_Q")
    stem = expression[:-2] if q else expression
    refs = tuple(sorted(ref for ref in stem.split("_") if ref))
    return refs, q


def filter_order_only_compound_findings(findings):
    """Drop only missing/extra pairs that differ solely by internal ref order.

    Count-preserving pairing matters: if two missing findings share a membership key
    but only one matching extra finding exists, only one pair is removed.
    """
    missing_by_key = defaultdict(deque)
    extra_by_key = defaultdict(deque)

    for index, finding in enumerate(findings):
        kind, message = finding
        if kind != "BAD_COMPOUND":
            continue
        m = _MISSING.match(message)
        if m:
            missing_by_key[canonical_semantic_compound(m.group(1))].append(index)
            continue
        m = _EXTRA.match(message)
        if m:
            extra_by_key[canonical_semantic_compound(m.group(1))].append(index)

    drop = set()
    for key in missing_by_key.keys() & extra_by_key.keys():
        missing = missing_by_key[key]
        extra = extra_by_key[key]
        while missing and extra:
            drop.add(missing.popleft())
            drop.add(extra.popleft())

    return [finding for index, finding in enumerate(findings) if index not in drop]


def v64_order_insensitive_evaluate(payload, fixture):
    return filter_order_only_compound_findings(_OriginalEvaluate(payload, fixture))


base.evaluate = v64_order_insensitive_evaluate


if __name__ == "__main__":
    base.main()
