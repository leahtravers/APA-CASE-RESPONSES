# RESEARCHER INVENTORY V34 — SEALED HOLDOUT ONE-SHOT HARNESS CORRECTION

Status: `HARNESS-ONLY CORRECTION — V34 SEMANTICS UNCHANGED`
Date: 2026-09-15
Authority: Leah’s standing Researcher Inventory calibration directive
Predecessor workflow blob: `339d1ada9a7e38f0853aa4272ff1343f856699a7`
Successor workflow commit: `06047c2fc5574fe657585ffd3416c603c0fd7e18`
Registrar record: `APA-EXEC-RI-CALIBRATION-V34-HOLDOUT-GUARD-20260915T0542Z-0001`

## Defect

The predecessor workflow correctly withheld sealed Case 5 until archetype calibration passed, but its gate was local to one workflow run. If a calibrated-lineage Case 5 attempt occurred and the workflow later failed before certification, a future scheduled run could begin a new calibration lineage and automatically expose the sealed holdout again.

That violates Leah’s exactly-once calibrated-lineage holdout rule.

## Correction

The successor harness now scans durable `calibration_history/researcher_inventory/*/holdout_stage_state.json` records before calibration. If any predecessor history records `calibrated_lineage_holdout_attempted: true`, automatic reuse of the sealed holdout is held. The harness records a durable non-content hold notice rather than reopening the sealed source.

The correction does not read, print, copy, or commit sealed Case 5 source or output.

## Historical state at correction

Before the correction, repository history contained no durable record with `calibrated_lineage_holdout_attempted: true`. Workflow run `34933071423` failed during Case 2/Case 6 calibration and did not reach Case 5. Therefore the sealed holdout remained unconsumed when this guard was installed.

## Boundary

This is a test-harness correction only. It does not amend `AGENT_CONTRACT_V34.md`, reinterpret any archetype, change evaluator semantics, certify V34, create an APA ID, promote research, or authorize a database/Oval Office write.

All predecessor workflow runs remain preserved as historical evidence.