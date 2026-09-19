# Researcher Inventory V98 Calibration Correction Record

Status: `ACTIVE PROSPECTIVE SEMANTIC SUCCESSOR RECORD`  
Date: 2026-09-19  
Successor contract: `RI-CONTRACT-V98` / `researcher_inventory/AGENT_CONTRACT_V98.md`  
Predecessor contract: `RI-CONTRACT-V97` / `researcher_inventory/AGENT_CONTRACT_V97.md`  
Authority: Leah's standing Researcher Inventory calibration instruction.  
Executive Registrar lineage: `APA-EXEC-2026-09-19-CASES-RI-V98-CAL-0001`.

## Immutable archetype gate

Latest completed V97 workflow run `35463810400` verified both repository workbook copies before semantic calibration:

- `Case_2_Lightweight_Researcher_Inventory.xlsx`: SHA-256 `d47915552fdbdd23adc8c3f66ab06f94e022ab0bfd93faa5faabb53fdf9c9193`
- `Case_6_Lightweight_Researcher_Inventory_v2_with_Verbs_and_Locators.xlsx`: SHA-256 `50d646aad08b33051b93c1f3b3538d59ff78386558473b71a906a94213635070`

The verifier reported `VERIFIED` with no repair. All 21 deterministic apparatus/harness tests passed before semantic calibration.

## Predecessor evidence preserved

- GitHub Actions run: `35463810400`
- preserved attempt: `calibration_history/researcher_inventory/35463810400-A1/`
- history-preservation commit: `a105d1c66fb7cf368fffd48ac363d1a16264c8fc`
- contract: `RI-CONTRACT-V97`
- result: `FAILED — CONFIRMED SEMANTIC ARCHETYPE MISMATCH`
- sealed holdout: not reached or consumed

## Failure classification

`AGENT-BEHAVIOR / DURABLE SEMANTIC CONTRACT DEFECT — GENERALIZABLE COMPLETENESS IMBALANCE`

V97 correctly corrected V96's lexical/syntactic over-tokenization by requiring source-native semantic grouping. The paired V97 execution demonstrates that the correction was directionally right but incomplete: the worker now suppresses many fragments that should be suppressed, yet also drops materially distinct local, one-use, low-salience, unnamed-support, and endpoint-dependent coordinates required to preserve the source's distinct proposition/event/state/question/comparison/orientation bindings. Compound failures then inherit the incomplete primitive inventory.

The common cause is not the evaluator, workbook integrity, or the V97 semantic-unit rule. It is that semantic grouping was applied primarily as a sparsity test without an equally explicit coverage test against the source's materially distinct bindings.

## V98 forward correction

V98 retains V97's source-native semantic grouping and adds a **bidirectional binding-completeness gate**.

Before primitive freeze the worker must maintain a private map of materially distinct source-local bindings and their distinct semantic roles/support coordinates. Primitive selection must satisfy both directions:

1. **Sparsity:** every admitted primitive has its own class-native, independently reconnectable semantic job; grammatical or mention-level divisibility alone never creates a row.
2. **Completeness:** every materially distinct binding retains the distinct primitive roles and support coordinates needed to reconstruct it without collapsing a real source role into a broader scene/episode, another class, or an analyst-created abstraction.

A local, unnamed, one-use, endpoint-dependent, or low-salience coordinate is not excluded by those properties. If removing it would make a material binding unreconstructable or merge two distinct source roles, it must be retained in its class-native home. Conversely, a token/phrase remains excluded when it performs no independently reconnectable job even if it appears in a material sentence.

This correction is general across all seven classes and does not target hidden counts, archetype rows, or evaluator answers.

## Harness/runtime status

No harness correction is authorized by run `35463810400`. Immutable workbook verification and all deterministic harness tests passed before semantic mismatch. V98 therefore retains the proven V66 field-aware evaluator, V88A editor-shorthand alignment, V82 append-only attempt history, and V92 same-session transient recovery. Only the durable worker semantics and versioned runtime/workflow identity change.

## Holdout boundary

The sealed Case 5 holdout remains inaccessible to calibration. V98 may not fetch, search, quote, expose, or execute it until repeated Case 2 + Case 6 passes occur under one finalized V98 contract and saved-agent lineage. Any later calibrated-lineage holdout is one-shot. Clean-room certification still requires retirement of that lineage and a brand-new saved agent bootstrapped only from finalized V98 instructions, with no prior holdout output or calibration-session access.

## Candidate-only boundary

All calibration outputs remain candidate/training material. No Oval Office research promotion, sovereign admission, APA ID minting, or APA Data Fabric write is authorized.

## Historical integrity

V97 and all earlier contracts, workflow runs, failed attempts, evaluator findings, recovery traces, and training history remain unchanged and controlling for the executions they governed. V98 is prospective only.
