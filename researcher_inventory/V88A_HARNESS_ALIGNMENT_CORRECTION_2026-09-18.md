# V88A Researcher Inventory Harness Alignment Correction

Status: `HARNESS-ONLY CORRECTION — ACTIVE FOR V88 EVALUATION`  
Effective date: 2026-09-18  
Authority: Leah's standing Researcher Inventory calibration instruction  
Semantic worker contract: `RI-CONTRACT-V88` — **UNCHANGED**  
Predecessor harness: V66 field-aware evaluator correction, retained unchanged except for this additive evaluator alignment layer

## Correction basis

Preserved calibration attempt `35412578650-A1` passed the immutable Case 2 / Case 6 SHA-256 gate and deterministic apparatus checks, then failed both hidden archetype evaluations under V88.

Before interpreting those failures as worker-semantic evidence, the evaluator exposed a mechanical alignment defect. A source-faithful worker coordinate can be reported as both `EXTRA_UNIT` and a semantically corresponding hidden editor shorthand as `MISSING_UNIT` when the difference is only bounded editorial normalization. The preserved Case 6 evidence includes source-faithful wording `a tractor tailer` while the hidden editor shorthand is `tractor trailer`. The source itself contains `tractor tailer`; the worker's literal-language lock therefore must not be weakened to force editor spelling.

This is a test-harness defect, not a demonstrated semantic-contract defect.

## Additive correction

V88A adds a same-class, evaluator-only short-tag alignment signal after the retained V66 alignment logic:

1. compare only actual `researcher_short_tag` / `source_wording` against the hidden editor short tag;
2. remove a leading English article only for evaluator comparison;
3. permit a high-confidence bounded orthographic/editorial near-match only for short phrases;
4. require very high character similarity and either shared lexical evidence or an even stronger single-token/string match;
5. never use this fuzzy signal across classes;
6. retain the predecessor alignment score as an independent floor rather than replacing it;
7. do not alter gold rows, gold hashes, source text, worker instructions, semantic task rules, Q evaluation, ordering checks, or compound comparison semantics.

## Isolation

The correction lives only in the hidden evaluator path. The semantic extractor receives neither this correction's hidden alignment targets nor any archetype rows, expected counts, evaluator findings, prior scored outputs, or sealed-holdout material.

`researcher_inventory/AGENT_CONTRACT_V88.md` and `researcher_inventory/v88_task_rules.py` remain unchanged for the rerun.

## Acceptance test

The deterministic test must prove both:

- bounded editor shorthand such as leading-article removal plus a minor orthographic difference aligns strongly within the same class; and
- unrelated or merely vaguely similar wording does not receive that high-confidence alignment signal.

## Forward decision gate

Rerun V88 against immutable Case 2 and Case 6 with V88A installed. Only the findings that remain after this harness correction may support a prospective semantic successor contract.

Case 5 remains sealed and must not run unless the same finalized semantic contract first achieves the required repeated archetype passes.

## Historical integrity

All V66/V82/V88 predecessor code, runs, failures, findings, contracts, and calibration history remain preserved. This record does not rewrite any earlier attempt and does not retroactively change how it was evaluated at execution time.
