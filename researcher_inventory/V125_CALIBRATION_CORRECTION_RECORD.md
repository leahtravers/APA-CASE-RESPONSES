# Researcher Inventory V125 Calibration Correction Record

Status: `PROSPECTIVE SUCCESSOR CORRECTION — CALIBRATION ONLY`
Date: 2026-09-20
Predecessor contract: `RI-CONTRACT-V124`
Successor contract: `RI-CONTRACT-V125`
Authority: Leah's standing Researcher Inventory calibration instruction
Registrar: `APA-EXEC-2026-09-20-CASES-RI-V125-CAL-0001`

## Predecessor evidence

Workflow run `35537813174` executed V124 from commit `bc7dc8723be43871b45df7d4ea8f3c3a55496e8a` and preserved its complete attempt at commit `9852777eed081a174f939ccc32251626db411ca4` under `calibration_history/researcher_inventory/35537813174-A1`.

Before semantic calibration the immutable workbook gate verified the repository copies directly against Leah's required SHA-256 values with no repair:

- `Case_2_Lightweight_Researcher_Inventory.xlsx` = `d47915552fdbdd23adc8c3f66ab06f94e022ab0bfd93faa5faabb53fdf9c9193`
- `Case_6_Lightweight_Researcher_Inventory_v2_with_Verbs_and_Locators.xlsx` = `50d646aad08b33051b93c1f3b3538d59ff78386558473b71a906a94213635070`

All 21 deterministic apparatus/harness tests passed before the model execution. The paired hidden-archetype diagnostic then failed on both calibration cases. The failure was preserved; repeatability and holdout stages were not reached.

## Defect classification

`WORKER-SEMANTIC / CONTRACT-GENERALIZATION DEFECT`

No independent evidence establishes a comparison, canonicalization, alignment, serialization, isolation, workbook-integrity, or evidence-preservation defect. Accordingly this correction does **not** modify evaluator or canonical archetype mechanics.

The paired failure showed the same broad pattern in both cases:

- legitimate source-established coordinates and local PLACE/TIME supports were omitted;
- some spans with weaker represented entitlement were still over-admitted;
- some surviving spans were assigned the wrong represented class;
- compound mismatch followed from incomplete/mistyped primitive coverage and inconsistent source-local binding.

The defect is generalizable because it appears across two materially different hidden archetypes under the same contract and clean harness.

## V124 defect

V124 replaced V123's overly abstract episode-ledger admission surface with source-anchored entitlement, but it still asked the worker to establish `independent researcher-selectability` and `materially distinct` support too early. Those thresholds became premature pruning criteria.

The worker therefore had to decide whether a coordinate was important enough before it had constructed a complete local coverage map of what the source represented.

## V125 correction

V125 changes the order of operations without changing the seven-class ontology or hidden evaluator:

1. **Coverage first.** Sweep the source in order and provisionally mark every exact source-established coordinate job before applying salience-like pruning.
2. **Prune narrowly.** Remove only pure discourse scaffolding, duplicate identity/restatement, generic nonreferential wording, fragments subsumed by a stronger natural nucleus, or spans with no represented coordinate job.
3. **Local support is lawful.** Reconstruct unnamed PLACE/TIME whenever the source differentiates a where/when frame needed to situate surviving coordinates, even if that support is local, one-use, or ordinary. No invented where/when content is allowed.
4. **Type by represented job.** Surface grammar and lexical category do not determine class.
5. **Preserve exact lexical grain.** Do not normalize colloquial, idiomatic, uncertain, negated, remembered, reported, prospective, or reflective source language.
6. **Freeze before binding.** Build selective compounds only after primitive coverage is stable, using all and only the frozen coordinates participating in each source-local binding, including support/orientation when they actually situate it.

This is a prospective durable correction, not a case-specific answer patch. The worker receives none of the hidden archetype rows, expected counts, evaluator findings, scored predecessor outputs, canonical gold extracts, or case-specific corrections recorded in administrative evidence.

## Harness boundary

V125 retains the proven apparatus/evaluator family unchanged:

- immutable workbook verification;
- deterministic apparatus tests;
- V66 field-aware compound/order correction;
- V88A editor-shorthand alignment correction;
- durable attempt-history preservation;
- same-session transient recovery;
- one-shot holdout isolation and clean-room certification gates.

Runtime wrapper changes are limited to successor contract identity, worker-facing neutral task rules, recovery directory, runner entry points, pipeline labels, and workflow routing.

## Holdout boundary

The sealed Case 5 source was not reached by V124 and remains closed. V125 must first pass the paired diagnostic and all required repeatability batches under the same finalized contract before any calibrated-lineage holdout attempt is lawful.

No Case 5 material is included in this correction record beyond that boundary statement.

## Historical integrity

V124 and all earlier contracts, workflows, runs, candidates, findings, and recovery artifacts remain preserved as predecessor evidence. V125 controls only prospective calibration work after its routing commit. No prior failure is rewritten or deleted.
