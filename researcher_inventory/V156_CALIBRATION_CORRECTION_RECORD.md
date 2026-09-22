# Researcher Inventory V156 Calibration Correction Record

Status: `PROSPECTIVE SEMANTIC SUCCESSOR — CALIBRATION ONLY`  
Date: 2026-09-22  
Successor contract: `researcher_inventory/AGENT_CONTRACT_V156.md` / `RI-CONTRACT-V156`  
Predecessor contract: `researcher_inventory/AGENT_CONTRACT_V155.md` / `RI-CONTRACT-V155`  
Authority: Leah's standing Researcher Inventory calibration instruction  
Executive Registrar record: `APA-EXEC-RI-CALIBRATION-20260922T052904-0400-S1`

## 1. Evidence gate

Latest completed V155 workflow inspected: GitHub Actions run `35707571998`, conclusion `FAILURE`.

Before semantic execution, that run verified both Leah-approved repository workbooks byte-for-byte and required no repair:

- Case 2 SHA-256: `d47915552fdbdd23adc8c3f66ab06f94e022ab0bfd93faa5faabb53fdf9c9193`
- Case 6 SHA-256: `50d646aad08b33051b93c1f3b3538d59ff78386558473b71a906a94213635070`

All 49 deterministic apparatus/harness tests passed before model semantic adjudication.

The V155 attempt is preserved under `calibration_history/researcher_inventory/35707571998-A1/` by history commit `32bcfe52d177d2899237f72d212cc8ad9eeccf06`.

V155 worker contract SHA-256 from the run: `99e5849bbeb0d303f8d9946a496afad91e66e2fba09222718c653cab57fd284f`.

The sealed Case 5 holdout was not opened or deployed.

## 2. Separate failure classifications

### Agent / durable semantic contract evidence

The Case 2 archetype completed and produced a semantic candidate. The candidate failed evaluator comparison.

The error pattern demonstrates that V155's admission-before-span correction was directionally useful but over-constrained relation admission and over-minimized phrase grain:

- source-presented relation occurrences were omitted when they were ordinary state, cognition, report, intention, speech, modal, or possession-like relations rather than physically material changes;
- admitted VERB relations were sometimes shortened below researcher-handle grain, losing bound relation wording needed to identify the relation;
- admitted LOCATOR relations were frequently reduced to generic prepositions/adverbs rather than retaining the source-native orientation phrase;
- source-staged qualitative phrases were sometimes split or typed too narrowly;
- temporary discourse/wrapper object formulations were sometimes multiplied while distinct source-treated choices/relations remained missing;
- compound mismatch remained downstream from primitive selection/type/span mismatch.

This is a semantic-contract defect, not a deterministic evaluator or canonicalization defect.

### Harness / runtime evidence

The Case 6 attempt did not reach semantic adjudication. It ended with `RuntimeError: no final answer` after the adapter created multiple replacement sessions.

Recovery traces show the Case 2 extraction/adjudication sessions completed successfully, while the Case 6 trace contains three separate extract-session creation events without a completed-result event. The adapter's result reader only inspects one `limit=100` page and treats `no final answer` as a non-transient exception. The V55 lineage then deletes local recovery state, allowing apparatus retry to create a new session.

That is a distinct harness/session-recovery defect. No Case 6 semantic failure is inferred from it.

## 3. Generalizable semantic requirement demonstrated

The approved archetype design across both calibration cases uses phrase-level researcher handles, not lexical-head atomization. It also permits source-staged relations such as reporting, cognition, speech, possession, state, comparison, and intention when those occurrences are independently represented.

Therefore V156 establishes two general rules:

1. **researcher-addressable relation admission is broader than materially changing the world** — an occurrence qualifies when the source distinctly stages that relation/stance and a researcher would lose an addressable represented relation if it were omitted; and
2. **relation span must preserve relation identity** — the shortest correct span is the shortest source-native phrase that still identifies the represented relation or orientation, not the shortest grammatical head/preposition.

These rules are case-independent and do not encode any gold row, expected count, or fixture-specific answer.

## 4. V156 semantic effect

V156 retains V155's order of operations but changes `source-native span` to `complete researcher-handle span`.

For VERB:

- retain source-presented action/state/process/speech/cognition/perception/intention/possession/relation occurrences when independently represented;
- keep required particles, complements, bound relation material, polarity, modality, aspect, and participant-facing wording needed for relation identity;
- do not reduce a relation to a generic verb head merely because the head is contiguous and grammatical.

For LOCATOR:

- retain source-presented positioning/orientation phrases, including spatial, movement, containment, recurrence/context, temporal-orienting, figurative, and comparison positioning when independently represented;
- keep the complement/context required to identify the orientation;
- do not prefer a bare preposition/adverb that erases what is being located or oriented.

For LABEL:

- preserve phrase-level source characterizations when relation/comparison/posture belongs to the characterization;
- do not assume labels must reduce to single descriptive heads.

For OBJECT:

- preserve independently source-treated choices, decisions, relations, and event-like referents;
- reconcile temporary discourse/wrapper formulations that merely point to another retained referent/relation.

For PLACE/TIME:

- retain V155 structural recall;
- do not create a separate TIME merely because a cognition/action occurs inside an already represented episode.

## 5. Worker-isolation boundary

The V156 worker receives no archetype rows/workbooks, expected counts, evaluator findings, canonical extracts, scored predecessor outputs, case-specific examples/corrections, or sealed holdout material.

This correction record may contain evaluator-side evidence because it governs the calibration apparatus. None of that case-specific evidence is copied into `AGENT_CONTRACT_V156.md` as an answer/example.

## 6. Compound effect

No independent compound-harness defect is established by V155. Compounds must continue to replay the frozen primitive graph. Primitive correction comes first.

## 7. Historical-integrity effect

`RI-CONTRACT-V155` remains preserved as the contract governing run `35707571998`.

V155 is partially superseded for forward calibration only to the extent stated in V156 Section 20. All retained controls remain active through the successor.

No predecessor is deleted or rewritten.

## 8. Holdout state

The sealed Case 5 holdout remains closed.

V156 must repeatedly pass both immutable Case 2 and Case 6 archetypes under the same finalized contract and saved-agent lineage before the one-shot calibrated-lineage holdout becomes eligible.
