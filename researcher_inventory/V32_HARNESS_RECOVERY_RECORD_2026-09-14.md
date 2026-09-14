# V32 RESEARCHER INVENTORY HARNESS RECOVERY RECORD

Status: `HARNESS / RUNTIME CORRECTION — NO SEMANTIC CONTRACT CHANGE`
Date: 2026-09-14
Durable semantic contract: `RI-CONTRACT-V32` / `researcher_inventory/AGENT_CONTRACT_V32.md`
Predecessor calibration run: GitHub Actions `34897950946`
Registrar filing: `APA-EXEC-RI-CALIBRATION-V32-RETRY-20260914T1823-0001`

## 1. Evidence

The latest V32 calibration run passed immutable archetype verification for both Leah-approved workbooks:

- Case 2 SHA-256 `d47915552fdbdd23adc8c3f66ab06f94e022ab0bfd93faa5faabb53fdf9c9193`
- Case 6 SHA-256 `50d646aad08b33051b93c1f3b3538d59ff78386558473b71a906a94213635070`

The run then failed before semantic adjudication. In both fixtures, the V32 model adapter timed out while waiting for the `TIME` class agent session. The apparatus retried the failed class request, but the adapter did not preserve the backend session identity across retry attempts. A local timeout therefore could cause a new semantic session to be created while the predecessor backend session's actual state was unknown.

That is a harness/recovery defect. It is not evidence that the V32 semantic contract is wrong.

## 2. Correction

`researcher_inventory/v32_openai_agents_adapter.py` is corrected prospectively so that:

1. each bounded V32 request receives a deterministic recovery key that excludes validator-correction text;
2. provisional and adjudication session IDs and last-known states are persisted in per-request runtime recovery state;
3. a local wait timeout triggers a direct backend status check;
4. if the backend session remains nonterminal or cannot be resolved, the adapter preserves the state and the apparatus retry resumes that same session rather than silently creating another session;
5. a completed provisional result may be reused only inside recovery of that same bounded attempt;
6. a confirmed non-timeout failure remains eligible for a fresh corrected semantic attempt;
7. runtime/harness failure text is never injected into the worker as semantic validator guidance; and
8. successful completion clears active recovery state while preserving the session trace.

The workflow now copies V32 session-recovery evidence into the calibration-history directory so failures remain reconstructable.

## 3. Historical predecessor limitation

Run `34897950946` predates this instrumentation. Its timed-out backend session IDs were not durably recorded, so those particular sessions cannot now be directly reconciled by ID. Their agent environment was `none`, and no semantic output from the timed-out attempts was admitted as a candidate or used to advance the calibration gate. The predecessor remains preserved as failed evidence.

## 4. Contract boundary

No change is made to `AGENT_CONTRACT_V32.md`, V32 task semantics, hidden gold evaluation, approved workbook contents, canonical extracts, pass criteria, or holdout criteria.

A timeout alone cannot authorize a V33 semantic successor.

## 5. Holdout boundary

The sealed Case 5 source remains unopened and unexecuted. This correction does not alter the requirement for repeated Case 2 and Case 6 archetype passes under the same finalized durable contract before any holdout execution.

## 6. Forward test

The next calibration execution is a successor runtime test of the unchanged V32 semantic contract under the corrected recovery harness. Its semantic outcome must be evaluated independently from this harness correction.
