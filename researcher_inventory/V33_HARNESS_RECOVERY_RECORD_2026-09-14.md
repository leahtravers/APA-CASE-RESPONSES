# V33 RESEARCHER INVENTORY HARNESS RECOVERY RECORD

Status: `HARNESS / RUNTIME CORRECTION — NO SEMANTIC CONTRACT CHANGE`
Date: 2026-09-14
Durable semantic contract: `RI-CONTRACT-V33` / `researcher_inventory/AGENT_CONTRACT_V33.md`
Predecessor calibration run: GitHub Actions `34915370918`
Predecessor filing: `APA-EXEC-RI-CALIBRATION-V33-20260914T2048-0001`
Successor registrar filing: `APA-EXEC-RI-CALIBRATION-V33-RETRY-20260914T2100-0001`

## 1. Evidence

Run `34915370918` passed immutable archetype verification and deterministic apparatus tests, then failed before semantic output in both fixtures.

The failure was:

`ModuleNotFoundError: No module named 'researcher_inventory'`

The V33 adapter was invoked directly as:

`python researcher_inventory/v33_openai_agents_adapter.py`

but imported its sibling V32 recovery adapter using package syntax:

`from researcher_inventory import v32_openai_agents_adapter as recovery`

Under direct-script execution, the script directory is on `sys.path`, so the sibling module must be imported through the invocation-compatible local module path.

## 2. Classification

This is a deterministic **harness/import-path defect**. No semantic candidate was produced and no hidden archetype adjudication occurred. Therefore run `34915370918` is not evidence for changing `RI-CONTRACT-V33`.

Case 5 remained `NOT_DEPLOYED`; holdout and clean-room steps were skipped.

## 3. Correction

The V33 adapter changes only the sibling import from package-style import to:

`import v32_openai_agents_adapter as recovery`

All V33 semantic prompts, task rules, contract requirements, recovery behavior, immutable workbook gates, hidden evaluator, pass criteria, calibration sequence, and holdout gates remain unchanged.

The V33 adapter continues to override the inherited recovery directory with:

`researcher_inventory/runtime/v33_session_recovery`

so V33 runtime state remains separate from V32 runtime state.

## 4. Historical integrity

Run `34915370918` remains preserved as failed harness evidence. It is not deleted, rewritten, or relabeled as a semantic attempt.

The next workflow execution is a successor harness-recovery run under the unchanged V33 semantic contract.

## 5. Forward boundary

A successful harness recovery does not certify V33. Certification still requires repeated Case 2 and Case 6 archetype passes under the same finalized V33 contract, followed by exactly one sealed Case 5 run on the calibrated lineage and a fresh-agent clean-room Case 5 success.

No promotion, APA-ID minting, Oval Office research admission, or APA database write is authorized.