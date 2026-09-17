# Researcher Inventory V64 Harness Correction Record

Status: `EVALUATOR-ONLY HARNESS CORRECTION — V64 WORKER CONTRACT UNCHANGED`
Date: 2026-09-17
Authority: Leah's standing Researcher Inventory calibration instruction
Executive filing: `APA-EXEC-2026-09-17-CASES-RI-V64-HARNESS-0001`
Preserved evidence run: `35178931620`
Worker contract retained: `researcher_inventory/AGENT_CONTRACT_V64.md` (`RI-CONTRACT-V64`)

## Immutable archetype integrity

Run `35178931620` completed the immutable workbook gate successfully before calibration:

- `Case_2_Lightweight_Researcher_Inventory.xlsx`: `d47915552fdbdd23adc8c3f66ab06f94e022ab0bfd93faa5faabb53fdf9c9193`
- `Case_6_Lightweight_Researcher_Inventory_v2_with_Verbs_and_Locators.xlsx`: `50d646aad08b33051b93c1f3b3538d59ff78386558473b71a906a94213635070`

No workbook repair was required. Sealed Case 5 was not reached or consumed.

## Defect classification

`TEST-HARNESS DEFECT — EVALUATOR-ONLY`

The hidden evaluator correctly maps worker unit references to archetype semantic unit references before compound comparison, but then serializes mapped compound references in the worker-returned internal order and compares that ordered string directly against the archetype compound expression. `RI-CONTRACT-V64` requires a materially complete compound containing all and only the primitives co-bound in the represented binding. It does not impose a canonical internal unit-reference serialization order.

The preserved run contains a direct order-only example: an expected semantic compound with membership `B`, `V1`, `P1` was simultaneously reported missing while the same mapped membership serialized as `P1_B_V1` was reported extra. The membership is identical; only serialization order differs.

This is analogous to the earlier V34 evaluator-only correction that stopped treating hidden editor row ordering as a semantic worker requirement. It is not evidence for changing the durable Researcher Inventory worker contract.

## Harness correction

Prospectively, V64 calibration uses `researcher_inventory/v64_compound_order_calibration_runner.py`.

The wrapper:

1. invokes the existing hidden V64 evaluator unchanged;
2. considers only `BAD_COMPOUND` findings explicitly reported as `missing semantic compound ...` or `extra semantic compound ...`;
3. canonicalizes each expression to its mapped primitive-reference multiset plus its Q state;
4. removes only count-matched missing/extra pairs whose canonical membership and Q state are identical;
5. preserves unmatched-reference errors, Q differences, true primitive-membership differences, primitive/type/literal findings, and all unpaired compound findings;
6. never supplies evaluator findings, gold rows, expected counts, or archetype content to the worker.

A deterministic unit test covers order-only equivalence, Q separation, true membership differences, unmatched-reference preservation, and count-preserving duplicate pairing.

## Durable worker authority

`RI-CONTRACT-V64` remains controlling and unchanged. `researcher_inventory/v64_task_rules.py` and `researcher_inventory/v64_openai_agents_adapter.py` remain unchanged.

The extensive primitive-resolution, type-assignment, lexical-grain, and compound-membership findings in run `35178931620` remain preserved as predecessor evidence. They must be reassessed after this evaluator-only repair. A later durable behavior successor is permitted only if the corrected paired-archetype run independently demonstrates a generalizable agent-behavior requirement.

## Holdout boundary

`researcher_inventory/tests/holdout/CASE_5.sealed.txt` remains closed to calibration agents and was not read for this correction. Holdout execution remains gated on repeated Case 2 + Case 6 passes under one finalized contract and lineage, followed by the existing one-shot calibrated-lineage and fresh-agent clean-room procedure.

## Historical integrity

Run `35178931620`, its evaluator findings, `RI-CONTRACT-V64`, and all prior contracts/runs remain unchanged. This record changes only the forward hidden-evaluator mechanics. No failed evidence is deleted or relabeled as a worker success.

No promotion, Oval Office research admission, sovereign APA identity, APA ID minting, or APA Data Fabric write is authorized.
