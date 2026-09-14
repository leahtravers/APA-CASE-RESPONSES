# RESEARCHER INVENTORY V28 CALIBRATION CORRECTION RECORD

Status: ACTIVE BOUNDED SUCCESSOR — CALIBRATION ONLY
Date: 2026-09-14
Authority: Leah’s standing Researcher Inventory calibration directive
Predecessor contract: `researcher_inventory/AGENT_CONTRACT_V27.md`
Successor contract: `researcher_inventory/AGENT_CONTRACT_V28.md`
Predecessor evidence: workflow run `34850021918`
Registrar record: `APA-EXEC-RI-CALIBRATION-V28-20260914T1020-0001`

## 1. Classification

`IN-SCOPE BOUNDED CORRECTION / GAP CLOSURE`

This successor changes worker-visible durable/task behavior and version-specific runtime timeout handling only. It does not change immutable gold workbooks, canonical extracts, evaluator answers, evaluator pass criteria, source fixtures, holdout isolation, candidate-only status, promotion authority, or APA identity rules.

## 2. Preconditions verified

Workflow run `34850021918` verified both Leah-approved repository workbooks before calibration:

- Case 2: `d47915552fdbdd23adc8c3f66ab06f94e022ab0bfd93faa5faabb53fdf9c9193`
- Case 6: `50d646aad08b33051b93c1f3b3538d59ff78386558473b71a906a94213635070`

The workflow step `Verify immutable Leah-approved archetype workbooks` completed successfully with `status: VERIFIED` and `repaired: []`.

All deterministic apparatus tests passed. The diagnostic calibration stage failed. Sealed Case 5 and clean-room verification were skipped. The failed attempt was preserved under `calibration_history/researcher_inventory/34850021918/`.

## 3. Defect classification

### A. Worker-behavior / durable-rule defect — generalizable

V27 moved too far from lexical/selectable unit resolution toward proposition-sized predicate construction. Its dominant-job rule also allowed a valid class function to suppress another valid class function performed by the same source material.

The diagnostic Case 2 output therefore showed a general pattern of:

- omitted source-presented units across multiple classes;
- larger governed/coordinated predicate spans replacing distinct lexical action/relation edges;
- valid state/location relations being suppressed as VERBs because other classes also represented them;
- contextual/orienting relations being pruned too narrowly;
- source-treated abstract choices/relations being lost while weaker discourse wrappers survived;
- compound mismatch downstream because compounds cannot repair missing units.

The generalizable requirement is that the **unit layer and compound layer must remain distinct**: units preserve the smallest complete function-bearing selectable coordinates; compounds assemble those units into proposition/event/state bindings.

### B. Harness/runtime defect — separate

The Case 6 diagnostic did not produce semantic evidence. The V27 adapter raised `RuntimeError("session timeout")` after an OpenAI Agent session remained non-idle beyond its fixed 360-second wait.

That state is a runtime/session timeout, not a demonstrated semantic Case 6 failure. The predecessor attempt remains preserved. V28 therefore increases version-specific session and command wait bounds without changing semantic evaluator criteria.

## 4. V28 corrective rule

V28 restores unit/compound separation and cross-class functional autonomy while retaining anti-invention and anti-grammatical-debris controls:

- a UNIT need not be a full proposition; it must be a genuine independently selectable function-bearing coordinate;
- a COMPOUND is where complete source-presented propositions/events/states are reassembled from retained units;
- VERB returns to distinct lexical action/relation edges, splitting coordinated/governed/embedded predicates when each contributes a separate represented relation, while keeping inseparable phrasal/support material together;
- state, locative, and copular relations are not automatically suppressed as VERBs merely because LABEL/PLACE/LOCATOR also applies;
- PLACE/TIME preserve source-established unnamed scene/frame coordinates when progression makes them separately selectable;
- LOCATOR may be physical, contextual, associative, recurring, target/path, deictic, or materially spatialized when it genuinely orients source material, but is not every prepositional phrase;
- OBJECT preserves source-treated abstract choices/decisions/relations while preventing bare discourse wrappers from replacing content-bearing referents;
- ordering uses first referential establishment after coreference/role resolution rather than raw first lexical occurrence;
- compounds cannot compensate for missing units.

No case-specific gold row, expected count, evaluator finding, scored output, or holdout content is placed in worker-visible instructions.

## 5. Runtime correction

V28 uses longer version-specific internal Agent-session and outer subprocess timeout bounds so a still-running session is not prematurely relabeled as a semantic failure.

If a V28 session still exceeds the extended bound, the run must preserve the timeout/uncertainty as runtime evidence. It must not fabricate a semantic verdict or automatically expose/run the holdout.

## 6. Historical-integrity effect

`AGENT_CONTRACT_V27.md`, V27 code, workflow run `34850021918`, and all V27 calibration history remain preserved.

`PARTIALLY SUPERSEDED — 2026-09-14`

For forward Researcher Inventory calibration behavior only, V28 supersedes V27’s proposition-sized VERB/dominant-job grain to the extent it collapsed distinct function-bearing units. V27 remains historical evidence.

## 7. Holdout state

SEALED CASE 5: `NOT DEPLOYED`

It remains closed until the unchanged external harness demonstrates the required repeated Case 2 and Case 6 passes under one finalized V28 contract.

## 8. Acceptance sequence

V28 must pass the unchanged sequence:

1. immutable workbook hash verification;
2. deterministic apparatus tests;
3. one diagnostic Case 2/Case 6 batch;
4. two further repeated Case 2/Case 6 batches under the same finalized contract and saved-agent lineage;
5. sealed Case 5 exactly once on that calibrated lineage;
6. retirement of that lineage;
7. a brand-new saved agent created only from finalized V28 instructions;
8. one fresh-session clean-room Case 5 pass with no prior-session or holdout-output access.

Only then may the apparatus be marked certified.