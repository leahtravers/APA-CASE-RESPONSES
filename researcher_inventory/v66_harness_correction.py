#!/usr/bin/env python3
"""V66 harness-only corrections.

These repairs change evaluator/task mechanics, not the durable V66 worker contract.
They contain no gold rows, expected counts, scored outputs, or sealed-holdout text.
"""
from __future__ import annotations

from typing import Any

from researcher_inventory import inventory_apparatus as apparatus


def _field_tokens(base, value: Any) -> set[str]:
    if value is None:
        return set()
    return set(base.tokens(value))


def field_evidence_score(base, actual: dict[str, Any], expected: dict[str, Any]) -> float:
    """Evaluator-only score from bounded worker-visible source fields.

    The predecessor evaluator pooled tag, wording, cue, and researcher note into one
    bag of tokens. A long neutral note could therefore change whether a strong source
    cue aligned. This score compares source-bearing fields separately and takes the
    strongest bounded match. It never enters worker input.
    """
    if expected.get("c") != actual.get("unit_class"):
        return 0.0

    actual_fields = [
        actual.get("researcher_short_tag"),
        actual.get("source_wording"),
        actual.get("source_cue"),
    ]
    expected_fields = [expected.get("g"), expected.get("s")]
    best = 0.0

    for av in actual_fields:
        an = base.norm(av)
        if not an:
            continue
        at = _field_tokens(base, av)
        for ev in expected_fields:
            en = base.norm(ev)
            if not en:
                continue
            if an == en:
                best = max(best, 980.0)
                continue
            if min(len(an), len(en)) >= 8 and (an in en or en in an):
                best = max(best, 900.0)

            et = _field_tokens(base, ev)
            if not at or not et:
                continue
            shared = at & et
            if len(shared) < 2:
                continue
            coverage = len(shared) / min(len(at), len(et))
            jaccard = len(shared) / len(at | et)
            if coverage >= 0.40:
                best = max(
                    best,
                    520.0 * coverage + 180.0 * jaccard + min(len(shared), 8),
                )
    return best


def install_field_aware_alignment(base) -> None:
    """Add the bounded field score on top of the preserved evaluator alignment."""
    prior = base.alignment_score
    if getattr(prior, "_v66_field_aware_alignment", False):
        return

    def corrected(actual, expected):
        return max(prior(actual, expected), field_evidence_score(base, actual, expected))

    corrected._v66_field_aware_alignment = True
    corrected.__name__ = "v66_field_aware_alignment_score"
    base.alignment_score = corrected


class V66HarnessInventoryApparatus(apparatus.InventoryApparatus):
    """V66 apparatus with selective compound construction task semantics."""

    def _extract_compounds(self, source: str, units: list[dict[str, Any]], refmap):
        payload = {
            "task": "researcher_inventory_build_lightweight_compounds",
            "rules": apparatus.BASE_RULES
            + "\nCOMPOUND SELECTION RULE: Build only materially useful multi-coordinate research bindings. "
              "A primitive may remain unbundled; do not manufacture a compound merely because a VERB, LABEL, TIME, PLACE, or other primitive exists. "
              "Use one smallest source-local bundle when several retained relations jointly express one materially complete binding with the same participants/content/frame. "
              "Split only when the source establishes a separately useful binding, such as a changed argument, target, attribution, comparison, question, position, or materially distinct frame. "
              "Do not emit exhaustive predicate closure, pairwise closure, singleton-equivalents, alternate subset/superset decompositions, or broad scene bundles. "
              "Use only supplied unit_ref values. Q is not a unit ref. A compound cannot repair a missing primitive.",
            "source": source,
            "units": units,
            "response_schema": [{
                "refs": "array of at least two existing unit_ref strings in semantic/source order",
                "researcher_bundle": "concise source-near bundle or null",
                "qualities_available": "boolean only",
            }],
        }
        last: Exception | None = None
        for _ in range(self.retries + 1):
            try:
                rows = self.adapter.ask(payload)
                if not isinstance(rows, list):
                    raise apparatus.ApparatusError("compound extraction must return array")
                normalized: list[tuple[int, str, list[str], bool, Any]] = []
                for row in rows:
                    refs = row.get("refs") if isinstance(row, dict) else None
                    if not isinstance(refs, list) or len(refs) < 2 or any(r not in refmap for r in refs):
                        raise apparatus.ApparatusError(f"invalid compound refs: {refs}")
                    refs = list(dict.fromkeys(refs))
                    q = bool(row.get("qualities_available"))
                    expression = "_".join(refs) + ("_Q" if q else "")
                    anchor = min(refmap[r].anchor for r in refs)
                    normalized.append((anchor, expression, refs, q, row.get("researcher_bundle")))
                dedup: dict[str, tuple[int, str, list[str], bool, Any]] = {}
                for item in normalized:
                    dedup.setdefault(item[1], item)
                ordered = sorted(dedup.values(), key=lambda x: (x[0], x[1]))
                return [{
                    "compound_ref": f"C{i}",
                    "compound_expression": expr,
                    "researcher_bundle": bundle,
                    "referenced_unit_refs": refs,
                    "qualities_available": q,
                } for i, (_, expr, refs, q, bundle) in enumerate(ordered, 1)]
            except Exception as exc:
                last = exc
                payload["correction"] = str(exc)
        raise apparatus.ApparatusError(f"compound extraction failed after retries: {last}")
