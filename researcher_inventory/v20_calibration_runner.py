#!/usr/bin/env python3
"""V20 calibration entry point.

Worker-visible V20 rules are paired with an evaluator-only alignment repair. The
alignment repair is not worker input: it only prevents inflection/editor-shorthand
differences from being misreported as missing+extra coordinates after production.
"""
from __future__ import annotations

from researcher_inventory import v12_calibration_runner as v12
from researcher_inventory import inventory_apparatus as apparatus
from researcher_inventory.v20_task_rules import V20_BASE_RULES, V20_CLASS_RULES

apparatus.BASE_RULES = V20_BASE_RULES
apparatus.CLASS_RULES = V20_CLASS_RULES

base = v12.base
_OriginalCommandAdapter = base.CommandAdapter
_OriginalAlignmentScore = base.alignment_score


class V20CommandAdapter(_OriginalCommandAdapter):
    def __init__(self, command: str, timeout: int = 480):
        super().__init__(command, timeout=timeout)


base.CommandAdapter = V20CommandAdapter


def _fold_token(token: str) -> str:
    t = token
    if len(t) > 5 and t.endswith("ing"):
        stem = t[:-3]
        if len(stem) >= 2 and stem[-1] == stem[-2]:
            stem = stem[:-1]
        return stem
    return t


def _folded_tokens(value) -> set[str]:
    return {_fold_token(t) for t in v12.tokens(value)}


def _overlap_score(a: set[str], b: set[str], base_score: float = 0.0) -> float:
    if not a or not b:
        return base_score
    shared = a & b
    if not shared:
        return base_score
    coverage = len(shared) / min(len(a), len(b))
    jaccard = len(shared) / len(a | b)
    if coverage >= 0.66 and (len(shared) >= 2 or min(len(a), len(b)) == 1):
        return max(base_score, 700.0 + 180.0 * coverage + 80.0 * jaccard + min(len(shared), 6))
    return base_score


def v20_alignment_score(actual, expected):
    """Evaluator-only alignment robust to inflection and editor shorthand.

    Gold coordinates remain immutable. This function does not teach expected rows
    to the worker; it only decides whether an already-produced coordinate is the
    same semantic coordinate before pass/fail findings are generated.
    """
    score = _OriginalAlignmentScore(actual, expected)

    # Tags are intentionally short. A strong content-token overlap should align
    # variants such as inflection or an editor descriptor wrapped around the same
    # source-near semantic coordinate.
    score = _overlap_score(
        _folded_tokens(actual.get("researcher_short_tag")),
        _folded_tokens(expected.get("g")),
        score,
    )

    # For unnamed PLACE coordinates, both sides often use neutral descriptions
    # rather than a literal place name. One unique shared content token in the
    # explanatory evidence is meaningful enough to clear the ordinary threshold;
    # ambiguity is still rejected later by the existing best-match margin rule.
    if (
        actual.get("unit_class") == "PLACE"
        and actual.get("source_wording") is None
        and expected.get("c") == "PLACE"
        and "exact place not specified" in base.norm(expected.get("s"))
    ):
        ae = _folded_tokens(base._actual_evidence(actual))
        ee = _folded_tokens(base._expected_evidence(expected))
        shared = ae & ee
        if shared:
            score = max(score, 430.0 + 20.0 * min(len(shared), 6))

    return score


base.alignment_score = v20_alignment_score


if __name__ == "__main__":
    base.main()
