#!/usr/bin/env python3
"""V11 calibration entry point with evaluator-only lexical normalization.

This module changes only hidden evaluator alignment. It does not alter worker
input, the durable contract, gold archetypes, or holdout handling.
"""
from __future__ import annotations

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


# Evaluator-only patch. The worker never imports this module.
base.tokens = tokens


if __name__ == "__main__":
    base.main()
