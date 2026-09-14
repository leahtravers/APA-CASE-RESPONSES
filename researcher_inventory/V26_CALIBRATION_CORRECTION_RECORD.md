# RESEARCHER INVENTORY V26 CALIBRATION CORRECTION RECORD

Status: ACTIVE BOUNDED SUCCESSOR — CALIBRATION ONLY
Date: 2026-09-14
Authority: Leah’s standing Researcher Inventory calibration directive
Predecessor contract: `researcher_inventory/AGENT_CONTRACT_V25.md`
Successor contract: `researcher_inventory/AGENT_CONTRACT_V26.md`
Predecessor evidence: workflow run `34823323438`
Registrar record: `APA-EXEC-RI-CALIBRATION-V26-20260914T0629-0001`

## 1. Classification

`IN-SCOPE BOUNDED CORRECTION / GAP CLOSURE`

This correction changes worker-visible durable/task behavior only. It does not change immutable gold workbooks, evaluator answers, evaluator pass criteria, holdout isolation, candidate-only status, promotion authority, or APA identity rules.

## 2. Preconditions verified

Workflow run `34823323438` verified both Leah-approved repository workbooks exactly before calibration:

- Case 2: `d47915552fdbdd23adc8c3f66ab06f94e022ab0bfd93faa5faabb53fdf9c9193`
- Case 6: `50d646aad08b33051b93c1f3b3538d59ff78386558473b71a906a94213635070`

No archetype repair was required. Deterministic apparatus verification passed. V25 calibration failed and its evidence was preserved under `calibration_history/researcher_inventory/34823323438/`. Sealed Case 5 was not deployed.

## 3. Defect classification

### Agent-behavior / durable-rule defect — generalizable

V25 successfully reduced some V24-style over-decomposition but overcorrected by making `if uncertain, do less` and class-parallel suppression too dominant. The result was substantial omission of source-supported researcher-selectable coordinates across both archetypes while some predicate and locator over-splitting still remained.

The unchanged archetype specification states that calibration must inventory all materially useful researcher-selectable coordinates at workbook resolution and must not produce a deliberately sparse summary. V25 therefore placed its ambiguity default in tension with the controlling coverage requirement.

A second generalizable defect is cross-class competition: V25 encouraged deletion when material resembled a coordinate already represented elsewhere, even though the archetypal apparatus permits legitimate cross-class overlap when the source independently performs both class jobs.

### Test-harness defect — not demonstrated

Immutable workbook hashes passed, deterministic tests passed, the evaluator remained bound to the unchanged Leah-approved archetypes, and the failures were semantically coherent with V25’s worker-visible rules. No gold, evaluator, or deterministic harness change is authorized.

## 4. V26 corrective rule

V26 replaces the sparse default with a two-stage class-local rule:

1. **Coverage first** — inventory every source-supported coordinate that independently performs the requested class job at story grain. Lightweight is structural resolution, not salience or sparsity.
2. **Prune second** — remove only unsupported inference, grammatical debris, non-independent fragments, over-split pieces, and same-class duplicates after coreference resolution.

Additional reconciliation:

- uncertainty/question/negation/hypothetical/future posture is preserved rather than used as a deletion reason when the coordinate is source-supported;
- another class never automatically excludes the requested class;
- cross-class overlap is retained only when the source independently performs both jobs;
- exact contiguous source wording remains mandatory;
- class-specific rules restore the broader archetypal coverage semantics while retaining V25 anti-atomization;
- compounds are built only after final unit retention and contain all and only retained units that actually participate in one lightweight source-presented binding.

No case-specific archetype row, expected count, evaluator finding, scored output, or sealed-holdout content is placed in worker instructions.

## 5. Historical-integrity effect

`AGENT_CONTRACT_V25.md`, V25 code, workflow run `34823323438`, and all V25 calibration history remain preserved.

`PARTIALLY SUPERSEDED — 2026-09-14`

For forward Researcher Inventory calibration behavior only, V26 supersedes V25’s sparse ambiguity default and its overly competitive cross-class suppression.

Retained from V25:
- literal source preservation;
- exact contiguous source discipline;
- source-posture preservation;
- alias/coreference handling;
- qualities boolean boundary;
- candidate-only status;
- no promotion / no APA IDs;
- archetype/evaluator/holdout isolation;
- repeated archetype passes before holdout;
- fresh-agent clean-room certification requirement.

## 6. Holdout state

SEALED CASE 5: `NOT DEPLOYED`

It remains closed until the unchanged external harness demonstrates the required repeated Case 2 and Case 6 passes under one finalized V26 contract.

## 7. Acceptance sequence

V26 must pass the existing sequence unchanged:

1. immutable workbook hash verification;
2. deterministic apparatus tests;
3. one diagnostic Case 2/Case 6 batch;
4. two further repeated Case 2/Case 6 batches under the same finalized contract and saved-agent lineage;
5. sealed Case 5 exactly once on that calibrated lineage;
6. retirement of that lineage;
7. a brand-new saved agent created only from finalized V26 instructions;
8. one fresh-session clean-room Case 5 pass with no prior-session or holdout-output access.

Only then may the apparatus be marked certified.