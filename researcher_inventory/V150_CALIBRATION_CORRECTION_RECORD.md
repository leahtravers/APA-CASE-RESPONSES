# Researcher Inventory V150 Calibration Correction Record

Status: `PROSPECTIVE SEMANTIC SUCCESSOR — CALIBRATION ONLY`  
Date: 2026-09-21  
Successor contract: `researcher_inventory/AGENT_CONTRACT_V150.md` / `RI-CONTRACT-V150`  
Predecessor contract: `researcher_inventory/AGENT_CONTRACT_V149.md` / `RI-CONTRACT-V149`  
Authority: Leah's standing Researcher Inventory calibration instruction  
Executive Registrar record: `APA-EXEC-2026-09-21-CASES-RI-V150-CAL-0001`

## 1. Evidence gate

Latest completed V149 workflow: GitHub Actions run `35679695596`, conclusion `FAILURE`.

Before semantic execution, that run directly verified both Leah-approved repository workbooks byte-for-byte and required no repair:

- Case 2: `d47915552fdbdd23adc8c3f66ab06f94e022ab0bfd93faa5faabb53fdf9c9193`
- Case 6: `50d646aad08b33051b93c1f3b3538d59ff78386558473b71a906a94213635070`

All 37 deterministic apparatus/harness tests passed before model calibration. The attempt was preserved under `calibration_history/researcher_inventory/35679695596-A1/` on current history lineage.

The sealed Case 5 holdout was not opened or deployed.

Classification: `AGENT / DURABLE SEMANTIC CONTRACT DEFECT`, not `TEST-HARNESS DEFECT`.

## 2. V149 failure pattern

The V149 contract added two important corrections to V148: class-local `inventory-coordinate identity` and smallest complete source-native atoms. Completed V149 evidence nevertheless shows the same unresolved two-sided boundary in both approved archetypes:

1. source-staged structural PLACE/TIME coordinates remain omitted when they are unnamed or are established by the organization of scenes/phases rather than explicit location/time vocabulary;
2. relation-like classes remain inflated by source fragments that are semantically interpretable but not promoted as distinct inventory coordinates;
3. incidental descriptive qualities are promoted into LABEL rows rather than remaining qualities/evidence associated with other coordinates;
4. ordinary predicates, discourse/reporting shells, support relations, and descriptive predications are promoted into VERB rows even when their representational contribution is already carried elsewhere;
5. spatial/temporal language is sometimes typed by lexical appearance rather than primary represented role;
6. cross-class ambiguity creates duplicate or mistyped coordinates; and
7. compound mismatch is overwhelmingly downstream from the wrong primitive membership and typing.

The recurrence across both approved archetypes after deterministic tests passed makes this a generalizable semantic-selection defect.

## 3. Why V149's wording remains too permissive

V149 asks whether a candidate `can be tracked as one source-presented ... unit`. That criterion can still be satisfied by nearly any semantically meaningful clause fragment if the model first invents a tracking frame for it. In effect, `trackable` can collapse back into `interpretable`.

The approved inventory requires a narrower but still class-local distinction: the source must **promote** material into a coordinate that makes a nonredundant local reconstructive contribution. Material may be meaningful, exact, and class-compatible while remaining only evidence, quality, cue, argument, support, or wording inside another retained coordinate/binding.

This correction must not restore V147's global scaffold ceiling. A valid promoted coordinate may still be one-use, low-salience, local, generic, unnamed, relation-bound, reported, remembered, prospective, questioned, figurative, or present-telling.

## 4. V150 corrective principle

V150 uses:

`whole-source frame map → broad positive class capture → primary-role arbitration → promoted-coordinate test → class-local nonredundancy test → complete-source-atom reconciliation → structural PLACE/TIME recall → PERSON/OBJECT recall → quality-channel audit → frozen primitives → minimal compounds`

A primitive must satisfy all of the following:

1. the source actually presents the class function;
2. the chosen class is the primary represented role for that occurrence unless separate source staging justifies multiplicity;
3. the source promotes the candidate into a distinct coordinate rather than using it only as evidence/quality/cue/argument/support inside another coordinate; and
4. removing it would erase distinct local reconstructive information not already preserved by other primitives, qualities, source cues, and minimal bindings.

The fourth test is local, not global. It does not require recurrence, broad research importance, independent reuse, or scaffold-level status.

## 5. Quality-channel correction

V149 preserved `qualities_available` mechanically but did not sufficiently use the distinction between **descriptive evidence** and **LABEL primitive**.

V150 makes that boundary explicit:

- descriptive wording may support `qualities_available = true` without becoming a LABEL;
- LABEL is reserved for characterizations the source itself promotes as distinct represented states/evaluations/classifications/comparisons;
- incidental attributive texture, naming modifiers, and ordinary descriptive predicates remain source evidence when they add no separate promoted coordinate.

This is a general inventory distinction, not a case-specific answer.

## 6. Primary-role arbitration correction

V149 allowed legitimate cross-class multiplicity but did not strongly enough prevent ambiguity-driven duplication.

V150 requires primary represented role before promotion. A source occurrence is not duplicated across classes merely because its words can be interpreted spatially, temporally, descriptively, relationally, or referentially in several ways.

Cross-class multiplicity requires positive source evidence that the same exact span is separately staged in both functions.

This correction addresses typing by represented role while preserving the rule that no class absorbs another.

## 7. PLACE/TIME correction

V150 preserves V149's structural recall and sharpens its exclusion side:

- PLACE requires a staged setting/position, not every spatial noun/surface/container;
- TIME requires an organizing frame/phase, not every temporal expression, recurrence word, duration phrase, or event occurrence;
- explicit spatial/temporal wording may be only evidence for another coordinate;
- unnamed positions/frames remain valid when the source structurally stages them as distinct reconstructive coordinates.

This closes both undercoverage and vocabulary-driven overcoverage without making every event a TIME or every spatial referent a PLACE.

## 8. OBJECT/LABEL/VERB/LOCATOR correction

V150 applies the same promoted-coordinate/local-nonredundancy rule within each relation-like or referential class:

- OBJECT requires source-promoted referential standing, not nounhood;
- LABEL requires a promoted characterization, not every descriptive quality;
- VERB requires a promoted relation/action/state, not every predicate or clause-support relation;
- LOCATOR requires a promoted orientation/context relation, not every preposition, spatial phrase, temporal cue, manner phrase, or figurative expression.

Smallest complete exact source-native atoms remain mandatory after promotion.

## 9. Compound determination

No independent deterministic compound-harness defect is demonstrated by run `35679695596`.

Compounds remain downstream of frozen primitive membership. V150 keeps the existing order-insensitive semantic comparison and prohibits compounds from repairing missing primitives or legitimizing excess primitives.

## 10. Harness determination

The V149A harness itself completed immutable-workbook verification, all 37 deterministic tests, one-turn whole-source execution, result evaluation, failure preservation, and history push.

Therefore the new semantic correction belongs in the durable contract and its subordinate operation selector. The V150A harness changes only the contract-subordinate selector/import path and versioned session-recovery namespace needed to execute V150. It does not add gold answers, expected counts, evaluator findings, or case-specific examples.

## 11. Retained controls

V150 retains without weakening:

- exact source wording, contiguity, dialect, polarity, uncertainty, question, negation, correction, attribution, and posture preservation;
- class-local rather than global admission;
- permission for low-salience, one-use, unnamed, local, deictic, remembered, reported, recurrent, intended, prospective, questioned, figurative, and present-telling coordinates when source-promoted distinctly;
- strict same-class coreference/alias reconciliation;
- source-reification boundary for OBJECT;
- complete-source-atom lexical grain;
- deterministic apparatus ownership of IDs, numbering, validation, `_Q`, persistence, evaluator comparison, retry, and failure handling;
- immutable gold-workbook hash verification;
- worker isolation from gold/evaluator/holdout content;
- candidate-only storage and complete failure-history preservation;
- repeated Case 2/Case 6 pass gate;
- one-shot calibrated-lineage holdout and fresh-agent clean-room certification;
- prohibition on Oval Office promotion, APA-ID minting, and APA database/fabric mutation.

## 12. Historical-integrity effect

`RI-CONTRACT-V149` remains preserved as the contract that governed run `35679695596` and earlier V149 attempts.

V149 is `PARTIALLY SUPERSEDED FOR FORWARD CALIBRATION — 2026-09-21` only for:

- using `trackable as one source-presented unit` as sufficient expression of inventory-coordinate identity;
- insufficient separation between descriptive quality/evidence and promoted LABEL coordinates;
- insufficient primary-role arbitration before cross-class multiplicity;
- insufficient exclusion of semantically interpretable but locally redundant predicate/orientation/referential fragments;
- PLACE/TIME wording where structural recall existed but incidental spatial/temporal cues remained too easy to promote.

V149's class-local orientation, complete-source-atom rule, exact-source lock, whole-source topology, candidate boundaries, deterministic apparatus controls, and holdout gates remain controlling unless expressly restated/superseded by V150.

No predecessor is deleted or rewritten.

## 13. Worker-isolation boundary

The V150 worker receives no gold rows, expected counts, evaluator findings, canonical archetype extracts, scored predecessor outputs, case-specific hidden corrections/examples, sealed holdout material, or prior target answers.

This correction record may use evaluator/gold evidence to govern the calibration apparatus. That evidence is not copied into the worker contract as case-specific examples or answers.

## 14. Holdout state

The sealed Case 5 holdout remains closed. V150 must repeatedly pass both immutable Case 2 and Case 6 archetypes under the same finalized contract and saved-agent lineage before the one-shot holdout gate becomes eligible.

No V150 calibration correction may be made from Case 5 output.
