# RESEARCHER INVENTORY V27 CALIBRATION CORRECTION RECORD

Status: ACTIVE BOUNDED SUCCESSOR — CALIBRATION ONLY
Date: 2026-09-14
Authority: Leah’s standing Researcher Inventory calibration directive
Predecessor contract: `researcher_inventory/AGENT_CONTRACT_V26.md`
Successor contract: `researcher_inventory/AGENT_CONTRACT_V27.md`
Predecessor evidence: workflow run `34834395445`
Registrar record: `APA-EXEC-RI-CALIBRATION-V27-20260914T0916-0001`

## 1. Classification

`IN-SCOPE BOUNDED CORRECTION / GAP CLOSURE`

This correction changes worker-visible durable/task behavior only. It does not change immutable gold workbooks, canonical extracts, evaluator answers, evaluator pass criteria, source fixtures, holdout isolation, candidate-only status, promotion authority, or APA identity rules.

## 2. Preconditions verified

Workflow run `34834395445` verified both Leah-approved repository workbooks before calibration:

- Case 2: `d47915552fdbdd23adc8c3f66ab06f94e022ab0bfd93faa5faabb53fdf9c9193`
- Case 6: `50d646aad08b33051b93c1f3b3538d59ff78386558473b71a906a94213635070`

The workflow step `Verify immutable Leah-approved archetype workbooks` completed successfully. Durable `archetype_integrity.json` records the exact expected/before/after hashes, `status: VERIFIED`, and `repaired: []`.

Deterministic apparatus verification passed. Calibration failed. Sealed Case 5 and clean-room verification were skipped. The failed attempt was preserved under `calibration_history/researcher_inventory/34834395445/`.

## 3. Defect classification

### Agent-behavior / durable-rule defect — generalizable

V26 corrected V25 undercoverage by emphasizing coverage-first class autonomy, but the worker overgeneralized that permission. The resulting output repeatedly treated proposition-internal grammatical material as independently inventoried coordinates: separate control/auxiliary predicate fragments, pure copular characterizations as extra VERBs, arbitrary prepositional arguments as LOCATORs, clause content as OBJECTs, and nested proposition subsets as independent compounds.

At the same time, some unnamed scene-position PLACE anchors and event/frame TIME anchors remained collapsed even though the controlling archetypal grain preserves them as distinct story coordinates.

The failure therefore demonstrates a missing generalizable grain discriminator: `source-supported` is necessary but not sufficient; a row must independently perform the requested class job at story/workbook grain.

### Test-harness defect — not demonstrated

Immutable workbook verification passed, deterministic tests passed, the evaluator remained bound to unchanged archetypes, and the observed failure pattern follows V26’s broadened worker-visible rules. No evaluator/gold repair is authorized.

## 4. V27 corrective rule

V27 introduces a dominant-job, independent-coordinate admission test while preserving full-source coverage:

- retain a candidate only when the source presents it as one independently selectable coordinate whose primary source job answers the requested class question at story/workbook grain;
- do not create rows from grammatical components merely because they can be redescribed under a class;
- allow cross-class overlap only when the exact source material genuinely performs each job independently;
- PLACE/TIME distinguish narrative scene/frame roles, including unnamed roles, rather than relying only on explicit lexical place/time wording;
- OBJECT keeps one conceptual referent together and does not nominalize every clause/state;
- LABEL keeps source-applied characterization and does not duplicate ordinary operational predicates;
- VERB uses one complete meaningful predicate construction, combining control/light/auxiliary material when it forms one relation and excluding pure copular characterization/location as a separate VERB;
- LOCATOR is an orienting position/path/context relation rather than every prepositional argument;
- compounds represent independently source-presented story bindings and omit redundant nested subsets.

Exact source wording, posture, Q boundary, candidate-only status, no promotion/no APA IDs, archetype isolation, evaluator isolation, and holdout isolation remain unchanged.

No case-specific gold row, expected count, evaluator finding, scored output, or holdout content is placed in worker instructions.

## 5. Historical-integrity effect

`AGENT_CONTRACT_V26.md`, V26 code, workflow run `34834395445`, and all V26 calibration history remain preserved.

`PARTIALLY SUPERSEDED — 2026-09-14`

For forward Researcher Inventory calibration behavior only, V27 supersedes V26’s coverage-first admission language to the extent it permitted grammatical/class-parallel overproduction and insufficient scene/frame distinction.

## 6. Holdout state

SEALED CASE 5: `NOT DEPLOYED`

It remains closed until the unchanged external harness demonstrates the required repeated Case 2 and Case 6 passes under one finalized V27 contract.

## 7. Acceptance sequence

V27 must pass the unchanged sequence:

1. immutable workbook hash verification;
2. deterministic apparatus tests;
3. one diagnostic Case 2/Case 6 batch;
4. two further repeated Case 2/Case 6 batches under the same finalized contract and saved-agent lineage;
5. sealed Case 5 exactly once on that calibrated lineage;
6. retirement of that lineage;
7. a brand-new saved agent created only from finalized V27 instructions;
8. one fresh-session clean-room Case 5 pass with no prior-session or holdout-output access.

Only then may the apparatus be marked certified.