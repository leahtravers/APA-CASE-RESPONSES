# Researcher Inventory V148A Harness Correction Record

Status: `ACTIVE HARNESS-TEST CORRECTION — SEMANTIC CONTRACT UNCHANGED`  
Date: 2026-09-21  
Semantic contract retained: `researcher_inventory/AGENT_CONTRACT_V148.md` / `RI-CONTRACT-V148`  
Failed workflow: `35667423887`, attempt 1  
Authority: Leah's standing Researcher Inventory calibration instruction

## Evidence

The first V148 workflow terminated before any model calibration request because deterministic test `test_whole_source_class_complete_uses_one_request` asserted that the runtime rule contained the exact phrase `positive class capture`.

The runtime rule actually states the same tested invariant as `positively capture candidates separately ... by represented source function` and separately states `primitive completeness is class-local` and `class-local exclusions`.

All earlier deterministic tests in the same run passed. The immutable Case 2 and Case 6 SHA-256 verification also passed with no repair. No semantic worker output was produced in this attempt.

The failed attempt was preserved under `calibration_history/researcher_inventory/35667423887-A1/`.

## Classification

`TEST-HARNESS DEFECT` — brittle wording assertion only.

This is not evidence for a new semantic requirement and does not justify changing `RI-CONTRACT-V148`.

## Correction

Replace the brittle phrase assertion with assertions on the actual stable runtime invariants:

- `primitive completeness is class-local`;
- `class-local exclusions`;
- one integrated model request;
- all seven response classes;
- compound member validation;
- gold/holdout blindness.

No source, archetype, evaluator, candidate, contract, model prompt semantics, or holdout gate is changed by this correction.

## Historical integrity

Preserve workflow run `35667423887` and its history packet as the failed harness-test predecessor. Do not rewrite or relabel it as a semantic attempt.
