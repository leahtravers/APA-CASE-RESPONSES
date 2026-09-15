# V34 RESEARCHER INVENTORY HARNESS ORDERING CORRECTION

Status: `HARNESS / EVALUATOR CORRECTION — NO SEMANTIC CONTRACT CHANGE`
Date: 2026-09-15
Authority: Leah's standing Researcher Inventory calibration directive
Durable semantic contract retained: `RI-CONTRACT-V34` / `researcher_inventory/AGENT_CONTRACT_V34.md`
Predecessor calibration run: GitHub Actions `34925334535`
Registrar filing: `APA-EXEC-RI-CALIBRATION-V34-HARNESS-20260915T0107-0001`

## 1. Confirmed defect

The predecessor evaluator treated the physical ordering of rows in the hidden Case 2 / Case 6 archetype extracts as the expected semantic unit ordering and emitted `ORDERING_MISMATCH` when an aligned worker output used a different order.

That is not a valid hidden-gold requirement. The durable Researcher Inventory contract independently requires source-establishment ordering. The approved workbook rows are authoritative for archetypal resolution, lexical/source preservation, class/type assignment, quality flags where encoded, and compound construction, but their editor row sequence is not a substitute for the contract's source-order rule.

Case 6 demonstrates the contradiction directly: some gold PERSON rows are arranged by editor grouping rather than first source establishment. A worker cannot lawfully infer that hidden editor ordering from source alone.

## 2. Classification

This is a deterministic **test-harness/evaluator defect**, not evidence for changing `RI-CONTRACT-V34`.

The semantic failures preserved in run `34925334535` remain evidence and are not erased. This correction removes only the invalid hidden-row-order finding. It does not reclassify the predecessor run as a pass.

## 3. Correction

`researcher_inventory/v34_calibration_runner.py` now wraps the existing hidden evaluator and filters only findings whose class is `ORDERING_MISMATCH`.

Retained unchanged:

- exact Case 2 and Case 6 workbook SHA-256 gates;
- gold unit resolution matching;
- source/literal preservation checks;
- unit type/class adjudication;
- `qualities_available` adjudication;
- compound construction adjudication;
- evaluator isolation from the worker;
- V34 worker contract and task rules;
- calibration repeatability sequence;
- failure/history preservation;
- sealed Case 5 holdout gate and clean-room certification sequence.

The worker is still required by `RI-CONTRACT-V34` to preserve source-establishment ordering. This correction merely stops the hidden evaluator from replacing that public rule with an arbitrary editor-row order.

## 4. Historical integrity

Run `34925334535` remains a failed V34 calibration attempt with its complete findings and raw outputs preserved. No prior finding is deleted or rewritten.

This record and the modified V34 calibration entry point form a bounded successor harness configuration for the next calibration attempt.

## 5. Forward boundary

If the corrected harness still reports failures, distinguish remaining evaluator/alignment defects from actual worker-behavior defects before changing the durable semantic contract. A V35 semantic successor is justified only by generalizable behavior failures that remain after harness defects are removed.

Case 5 remains `NOT_DEPLOYED` until repeated Case 2 and Case 6 archetype passes occur under the same finalized semantic contract. No promotion, APA-ID minting, Oval Office research admission, or database write is authorized.
