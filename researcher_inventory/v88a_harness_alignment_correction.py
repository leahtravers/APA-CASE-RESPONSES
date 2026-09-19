#!/usr/bin/env python3
"""V88A evaluator-only alignment correction.

This layer is additive to the retained V66 field-aware alignment. It exists only
inside the hidden evaluator path and never changes worker instructions, source
text, gold rows, expected counts, or sealed-holdout handling.
"""
from __future__ import annotations

from difflib import SequenceMatcher
import re
from typing import Any


_LEADING_ARTICLE = re.compile(r"^(?:a|an|the)\s+", re.IGNORECASE)
_TOKEN = re.compile(r"[a-z0-9$]+(?:'[a-z0-9]+)?")


def _editor_key(base, value: Any) -> str:
    """Return a bounded evaluator-only key for short editor shorthand."""
    s = base.norm(value)
    s = _LEADING_ARTICLE.sub("", s, count=1).strip()
    return s


def _tokens(value: str) -> set[str]:
    return set(_TOKEN.findall(value.lower()))


def editor_shorthand_score(base, actual: dict[str, Any], expected: dict[str, Any]) -> float:
    """Score very-near same-class source wording vs hidden editor shorthand.

    The ordinary evaluator remains authoritative for exact, containment, token,
    type, order, Q and compound checks. This signal only resolves a narrow class
    of editorial alignment misses: a leading article and/or a small orthographic
    difference in a short phrase. It intentionally cannot create a cross-class
    type match.
    """
    if expected.get("c") != actual.get("unit_class"):
        return 0.0

    expected_key = _editor_key(base, expected.get("g"))
    if not expected_key or len(expected_key) < 5 or len(expected_key) > 72:
        return 0.0

    expected_tokens = _tokens(expected_key)
    best = 0.0
    for field in (actual.get("researcher_short_tag"), actual.get("source_wording")):
        actual_key = _editor_key(base, field)
        if not actual_key or len(actual_key) < 5 or len(actual_key) > 72:
            continue

        # This correction is for compact editor shorthand, not sentence-level
        # semantic similarity.
        actual_tokens = _tokens(actual_key)
        if len(actual_tokens) > 6 or len(expected_tokens) > 6:
            continue

        if actual_key == expected_key:
            best = max(best, 990.0)
            continue

        ratio = SequenceMatcher(None, actual_key, expected_key).ratio()
        shared = actual_tokens & expected_tokens

        # Multi-token phrases need at least one exact lexical anchor unless the
        # strings are virtually identical. Single-token spellings must be even
        # closer. These thresholds are deliberately much stricter than ordinary
        # semantic alignment so vaguely similar coordinates cannot be forced.
        if len(actual_tokens) == 1 and len(expected_tokens) == 1:
            if ratio >= 0.95:
                best = max(best, 930.0 + min(50.0, (ratio - 0.95) * 1000.0))
            continue

        if ratio >= 0.92 and (shared or ratio >= 0.97):
            best = max(best, 930.0 + min(50.0, (ratio - 0.92) * 600.0))

    return best


def install_editor_shorthand_alignment(base) -> None:
    """Install V88A on top of the currently installed evaluator alignment."""
    prior = base.alignment_score
    if getattr(prior, "_v88a_editor_shorthand_alignment", False):
        return

    def corrected(actual, expected):
        return max(prior(actual, expected), editor_shorthand_score(base, actual, expected))

    corrected._v88a_editor_shorthand_alignment = True
    corrected.__name__ = "v88a_editor_shorthand_alignment_score"
    base.alignment_score = corrected
