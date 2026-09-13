# RESEARCHER INVENTORY V17 CALIBRATION CORRECTION RECORD

Status: CALIBRATION HISTORY / FORWARD CORRECTION RECORD
Date: 2026-09-13
Authority: Leah's standing Researcher Inventory calibration directive
Predecessor calibration contract: `AGENT_CONTRACT_V16.md`
Successor calibration contract: `AGENT_CONTRACT_V17.md`

## Immutable gold gate

Before this correction, the repository archetype copies were verified against Leah's immutable SHA-256 values:

- `Case_2_Lightweight_Researcher_Inventory.xlsx`: `d47915552fdbdd23adc8c3f66ab06f94e022ab0bfd93faa5faabb53fdf9c9193`
- `Case_6_Lightweight_Researcher_Inventory_v2_with_Verbs_and_Locators.xlsx`: `50d646aad08b33051b93c1f3b3538d59ff78386558473b71a906a94213635070`

No archetype repair was required.

## Preserved failed evidence

The V16 failure is preserved under:

`calibration_history/researcher_inventory/34774156090/`

It remains failed calibration evidence and receives no forward certification effect.

## Defect class 1 — worker-behavior contract defect

The V16 contract introduced a generalized deletion/minimality bias. In particular it told the worker to target the smallest set, omit doubtful separate coordinates, use deletion-biased stateless verification, and merge predicate material unless independent reuse was especially clear.

Across both immutable archetypes, that policy systematically collapsed materially represented PLACE/TIME coordinates, source-level lexical predicate increments, source-applied characterizations, OBJECT coordinates, LOCATOR relations, and the compounds that depended on them.

This is a generalizable worker-behavior defect, not a case-specific exception.

Forward correction: `AGENT_CONTRACT_V17.md` replaces deletion bias with complete source-level coverage plus class-boundary filtering. It still rejects invention, grammatical debris, and true duplication.

## Defect class 2 — harness / adapter boundary defect

The V16 adapter accepted the apparatus payload but removed the neutral `rules` and `class_rule` fields before sending the bounded request to the saved worker. Those fields contain general task semantics and are not gold/evaluator/holdout evidence.

The adapter then substituted its own deletion-biased task attention. As a result, the current apparatus's general class rules were not actually available to the worker during V16 calibration.

This is a harness/prompt-boundary defect separate from worker behavior.

Forward correction: `v17_openai_agents_adapter.py` passes the neutral apparatus `rules` and `class_rule` fields while continuing to reject archetypes, expected counts, evaluator findings, scored outputs, and holdout outputs.

## Evaluator classification

The hidden evaluator remains class-bounded and source-evidence based. It checks the immutable workbook hashes before canonical extracts are used and does not place evaluator findings or gold rows into worker input.

No evaluator criterion or gold archetype was changed by the V17 correction.

## Holdout boundary

No sealed Case 5 content or output was used in diagnosing or writing V17.

Case 5 remains unavailable to calibration and may run only after repeated Case 2/Case 6 success under the same finalized successor contract, followed by the separate clean-room rule if the first holdout passes.

## Forward state

V17 is authorized for calibration only and is not certified until the full repeated-archetype, sealed-holdout, and fresh-agent clean-room gates succeed.

No record is promoted to Oval Office and no APA ID is minted by this correction.
