# Researcher Inventory V66 Harness Correction Record

Status: ADDITIVE HARNESS CORRECTION — WORKER CONTRACT UNCHANGED  
Date: 2026-09-17  
Worker contract retained: `RI-CONTRACT-V66`  
Evidence predecessor: workflow run `35197255415`  
Executive filing: `APA-EXEC-2026-09-17-CASES-RI-V66-HARNESS-0001`

## Purpose

Separate mechanical evaluator/task defects from Researcher Inventory agent-behavior defects before considering any new durable worker-contract successor.

The latest V66 run passed immutable workbook verification and deterministic apparatus tests, then failed hidden semantic evaluation. The preserved evidence contains both repeatable worker-selection errors and two harness behaviors capable of producing false or structurally conflicting findings. This record corrects only those harness behaviors first.

## Immutable archetype integrity

The repository copies of the Leah-approved Case 2 and Case 6 workbooks passed the workflow SHA-256 gate before the failed calibration run. Required hashes remain:

- Case 2: `d47915552fdbdd23adc8c3f66ab06f94e022ab0bfd93faa5faabb53fdf9c9193`
- Case 6: `50d646aad08b33051b93c1f3b3538d59ff78386558473b71a906a94213635070`

No archetype content is changed by this correction.

## Harness defect 1 — pooled alignment evidence

The evaluator alignment predecessor pooled the worker's short tag, exact source wording, exact source cue, and neutral researcher note into one evidence bag. A long neutral note could therefore alter whether a strong same-class source cue aligned with the hidden archetype.

Correction:

- preserve the existing alignment score;
- add an evaluator-only same-class score that compares source-bearing fields separately;
- take the strongest bounded field match rather than allowing unrelated note tokens to dilute source evidence;
- do not use this additional score across classes;
- do not expose archetype wording, counts, scores, or findings to the worker.

This is evaluator-only. It changes no worker instruction or gold record.

## Harness defect 2 — exhaustive compound task wording

The common apparatus compound task instructed the model to create a compound for every represented predicate relation, characterization proposition, question/correction/reflection, and prospective relation. That requirement is broader than the durable V66 compound rule, which permits selective source-local bindings and prohibits exhaustive closure.

Correction:

For the V66 harness only, the compound task now states that:

- compounds are materially useful multi-coordinate research bindings;
- a primitive may remain unbundled;
- a compound must not be manufactured merely because a primitive exists;
- several retained relations may share one materially complete source-local binding;
- splitting occurs only for a separately useful binding such as a changed argument, target, attribution, comparison, question, position, or materially distinct frame;
- pairwise/exhaustive closure and alternate decomposition remain prohibited.

This correction does not modify predecessor apparatus behavior for historical runs.

## Deterministic verification

A synthetic unit-test module accompanies the correction. It tests:

1. strong same-class source-cue evidence remains alignable despite a long unrelated note;
2. the new field score does not boost a cross-class match; and
3. the V66 compound task expressly allows unbundled primitives and no longer carries the predecessor exhaustive-predicate instruction.

Synthetic tests contain no approved archetype rows, gold counts, evaluator answers, prior scored outputs, or sealed holdout material.

## Worker contract status

`RI-CONTRACT-V66` remains the controlling worker contract for the immediate successor calibration. No V67 contract is created by this correction.

Only residual failures that remain after the corrected harness runs may justify a durable worker-contract successor, and then only if the preserved evidence demonstrates a generalizable worker requirement rather than another harness defect.

## Holdout boundary

Sealed Case 5 was not reached in run `35197255415` and remains closed. The V66 harness correction supplies a matching protected holdout entry point so, if repeated Case 2 / Case 6 passes are eventually achieved, the holdout uses the same non-exhaustive compound task semantics without exposing sealed source/output.

No holdout source or output is included here.

## Candidate-only boundary

All calibration outputs remain candidate/training material. No Oval Office promotion, APA Data Fabric admission, sovereign identity, APA ID minting, or database mutation is authorized by this record.

## Historical integrity

All predecessor contracts, runners, workflow runs, failed candidates, findings, and training history remain intact. This file and the new V66-specific harness modules are additive forward corrections only.