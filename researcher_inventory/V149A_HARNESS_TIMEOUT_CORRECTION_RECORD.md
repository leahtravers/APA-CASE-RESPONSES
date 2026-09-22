# Researcher Inventory V149A Harness Timeout Correction Record

Status: `HARNESS-ONLY CORRECTION — NO SEMANTIC EFFECT`  
Date: 2026-09-21  
Authority: Leah's standing Researcher Inventory calibration instruction  
Executive Registrar record: `APA-EXEC-2026-09-21-CASES-RI-V149-CAL-0001`

## 1. Demonstrated defect

GitHub Actions run `35667494590` reached the V148 diagnostic archetype batch after immutable workbook verification and all deterministic tests passed, but both model calls were terminated by the outer `CommandAdapter` at 1500 seconds.

The workflow simultaneously configured the saved-agent/session layer with:

- `RI_AGENT_SESSION_TIMEOUT_SECONDS=600`
- `RI_AGENT_SESSION_TOTAL_TIMEOUT_SECONDS=1800`

The established V148A sealed-holdout runner already uses a 2400-second outer `CommandAdapter` timeout.

Therefore the 1500-second calibration command timeout can terminate a bounded model/session operation before the configured 1800-second total session window has completed. That is a runtime/harness timing mismatch, not evidence about Researcher Inventory semantics.

## 2. Correction

V149A calibration uses a 2400-second outer `CommandAdapter` timeout, matching the established holdout-runner outer bound and leaving the internal saved-agent/session limits unchanged.

This gives the existing 1800-second total agent-session budget room to finish or fail on its own terms.

## 3. No semantic effect

This correction does not change:

- durable Researcher Inventory instructions;
- archetype hashes or workbook contents;
- evaluator semantics;
- primitive or compound acceptance criteria;
- retry success criteria;
- source validation;
- gold visibility;
- holdout visibility;
- candidate persistence rules;
- promotion or ID authority.

A longer outer timeout cannot turn a semantic mismatch into a pass.

## 4. Historical integrity

The timed-out V148 attempts remain preserved exactly as historical failures. They are not relabeled as semantic passes or deleted.

The V149 semantic successor is independently justified in `V149_CALIBRATION_CORRECTION_RECORD.md`; this timeout record is not part of that semantic justification.
