# Researcher Inventory V101 Calibration Correction Record

Status: `PROSPECTIVE SEMANTIC SUCCESSOR AUTHORIZED BY STANDING CALIBRATION SCOPE`
Date: 2026-09-19
Successor contract: `RI-CONTRACT-V101`
Predecessor: `RI-CONTRACT-V100`
Scope classification: `IN-SCOPE BOUNDED CORRECTION / GAP CLOSURE`

## Preserved evidence

V100 is not edited or deleted. Its contract, runtime wrappers, task rules, workflow executions, model/session evidence, evaluator findings, and failed candidates remain historical calibration evidence.

Two V100 executions establish the correction basis:

- workflow run `35473385926`, attempt 1;
- workflow run `35475057364`, attempt 1.

In both executions:

- Case 2 SHA-256 matched `d47915552fdbdd23adc8c3f66ab06f94e022ab0bfd93faa5faabb53fdf9c9193`;
- Case 6 SHA-256 matched `50d646aad08b33051b93c1f3b3538d59ff78386558473b71a906a94213635070`;
- no archetype repair was required;
- all 21 deterministic apparatus/harness tests passed before semantic calibration;
- Case 2 and Case 6 both failed semantic archetype comparison;
- the sealed holdout was not attempted.

Run `35475057364` preserved its evidence additively in `calibration_history/researcher_inventory/35475057364-A1/` and pushed history commit `517f6ed3ad418b03be195abc03440d9ad67147c2`.

## Defect classification

`AGENT-BEHAVIOR / DURABLE SEMANTIC CONTRACT DEFECT — PRIMITIVE GRAIN AND COORDINATE-ADMISSION INSTABILITY`

The repeated V100 failure demonstrates a generalizable requirement rather than a case-specific answer:

1. V100's whole-source binding ledger still makes primitive admission too dependent on proposition/binding reconstruction.
2. The worker can over-admit proposition-sized VERB, TIME, LABEL, LOCATOR, or abstract-content rows while omitting ordinary source-reified concrete/abstract handles that remain valid standalone research coordinates.
3. The relation grain remains unstable: clause-sized relations can be returned where a smaller source-native predicate kernel is the independently selectable relation.
4. PLACE/TIME support can proliferate from surface sequence instead of semantic episode/frame identity.
5. Compounds inherit these primitive-grain errors even though the V66 compound harness correctly instructs selective, non-exhaustive bundling.

No new harness defect is demonstrated. The immutable workbook gate and deterministic evaluator/apparatus tests passed twice under V100, so V101 leaves the harness/evaluator mechanics unchanged.

## V101 corrective rule

V101 replaces binding-ledger-dependent primitive admission with `COORDINATE-FIRST KERNEL/FRAME INVENTORY`:

- primitives are recovered independently at class-native grain;
- a primitive may remain unbundled;
- source-reified concrete and low-salience handles are not excluded for lack of narrative centrality;
- propositions are decomposed into independently selectable kernels/handles/frames rather than returned wholesale;
- VERB uses the shortest complete relation kernel;
- PLACE/TIME use semantic support-frame identity rather than one frame per clause/event;
- LOCATOR preserves independently selectable orientation while excluding recipient/topic/duration/discourse pseudo-locators;
- LABEL keeps independently selectable characterization/polarity units at their own grain;
- compounds remain selective and occur only after primitive freeze.

The durable worker instructions contain no archetype rows, hidden counts, evaluator answers, prior scored outputs, or holdout content.

## Isolation and holdout boundary

Case 5 remains sealed. V101 must first pass one paired diagnostic batch and two paired repeatability batches for Case 2 + Case 6 under one finalized V101 contract and saved-agent lineage. Only then may the existing one-shot holdout gate execute.

If the calibrated lineage passes Case 5, that saved agent is retired. `session_bootstrap.py` then creates a brand-new saved agent using only `AGENT_CONTRACT_V101.md`; clean-room certification requires that fresh agent to pass Case 5 in a new session without prior calibration-session or holdout-output access.

No candidate promotion, Oval Office admission, APA-ID minting, or APA Data Fabric/database write is authorized.

## Executive filing

Executive Registrar record: `APA-EXEC-2026-09-19-CASES-RI-V101-CAL-0001`
Submission lane: `SUBMITTED - BACKGROUND REGISTRATION`
