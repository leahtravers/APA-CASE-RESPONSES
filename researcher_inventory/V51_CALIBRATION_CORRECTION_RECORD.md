# V51 CALIBRATION CORRECTION RECORD

Status: `PROSPECTIVE SUCCESSOR CORRECTION`
Date: 2026-09-16
Predecessor: `RI-CONTRACT-V50`
Successor: `RI-CONTRACT-V51`
Authority: Leah's standing Researcher Inventory calibration directive
Registrar record: `APA-EXEC-CASES-RI-CAL-V51-20260916-0131`

## Evidence basis

Two preserved V50 calibration runs used the same finalized V50 contract and saved-agent calibration apparatus and failed before the holdout gate:

- push run `35054075161`;
- scheduled run `35057867967`, preserved at repository head `cb8c2b8406d8d85a8cdf40f9c07668d96f55a079`.

The latest run's immutable-workbook gate verified Leah's approved archetypes before semantic calibration:

- `Case_2_Lightweight_Researcher_Inventory.xlsx` = `d47915552fdbdd23adc8c3f66ab06f94e022ab0bfd93faa5faabb53fdf9c9193`
- `Case_6_Lightweight_Researcher_Inventory_v2_with_Verbs_and_Locators.xlsx` = `50d646aad08b33051b93c1f3b3538d59ff78386558473b71a906a94213635070`
- integrity status: `VERIFIED`
- repaired: none

Deterministic source-span, literal-language, semantic-order, ID, quality-flag, and reference checks passed. Hidden semantic calibration failed on both archetypes. Case 5 was not attempted and remains unavailable to calibration.

## Defect classification

`AGENT-BEHAVIOR / GENERALIZABLE ROLE-RESOLUTION AND COMPOUND-GRAIN DEFECT`

The evidence does not show a corrupted workbook, SHA verifier defect, source-span validator defect, output-schema defect, evaluator-translation defect, or holdout leak.

V50's class-native independent-coordinate rule remains too atom-oriented for the approved lightweight inventory. Across both archetypes it can omit source-supported scene/time/referent/state/orientation roles or assign the wrong class to a source span, while also retaining many lexical predicates, descriptive fragments, discourse/support relations, local physical nouns, temporal cues, and orientation fragments that do not carry an independent lightweight research role. The same atom-oriented bias appears in compounds: the worker often emits smaller alternative decompositions instead of one complete lightweight source proposition and therefore misses the complete binding expected from the frozen role ledger.

The cross-case recurrence demonstrates a generalizable requirement: **unit admission is governed by participation in a materially distinct role-bearing source proposition, not by lexical separability or isolated semantic plausibility.**

## V51 correction

V51 introduces `role-bearing proposition resolution`:

1. First map materially distinct source-presented propositions/events/states/orientations at lightweight grain, without turning the map into an answer key.
2. Admit a unit only when it fills a necessary class-native role in at least one retained proposition: participant/person, referent/content, characterization/state/polarity, operative relation, orientation, place frame, or time frame.
3. Explicit wording does not entitle a unit; implicit PLACE/TIME may survive when a proposition requires a distinct source-supported frame even if no location/time noun names it.
4. Incidental modifiers, background nouns, support/reporting/meta predicates, durations/frequency cues, destinations, and prepositional fragments are removed when they do not carry a necessary role in a retained proposition.
5. Class is chosen from the source function inside the proposition, not from surface part of speech. A span functioning as a bound state/value belongs in LABEL even when verbal, adverbial, locative, interrogative, or polarity-shaped; a lexical predicate belongs in VERB only when it is the operative relation carrier.
6. VERB keeps the shortest complete source-native relation carrier that preserves the represented relation, including particles/copular/locative/modal material when necessary, while excluding auxiliary/support/meta/reporting predicates that merely host another retained relation.
7. PLACE and TIME are proposition frames, not lists of physical nouns, hypothetical endpoints, recurrence words, or event clauses.
8. OBJECT is a proposition participant/referent/content role, concrete or abstract; mere discourse wrappers and background mentions are excluded.
9. LOCATOR is retained only when a proposition requires an independently represented orientation relation, using the smallest complete source-native orientation span.
10. After units freeze, emit exactly one smallest **complete** compound for each retained proposition. Include every frozen role needed to reconstruct that proposition's actor/referent/relation/state/orientation/frame, including tightly bound co-predicates or contextual anchors when they jointly constitute the proposition. Do not emit alternative subset decompositions, sentence-wide bags, or combinatorial variants.

These are neutral cross-case rules. No archetype row, expected count, evaluator finding, prior scored answer, case-specific gold correction, or holdout content is placed into worker instructions.

## Retained controls

Unchanged:

- immutable Case 2/Case 6 SHA-256 gate before every use;
- literal source lock and dialect/punctuation/posture preservation;
- hidden evaluator and worker/gold isolation;
- candidate-only status;
- harness defects separated from worker semantic defects;
- every attempt/failure preserved as candidate training history when possible;
- sealed Case 5 prohibited during calibration;
- repeated Case 2/Case 6 archetype passes required under the same finalized contract and lineage before holdout;
- calibrated-lineage Case 5 may run exactly once only after that gate;
- successful calibrated lineage must be retired before a brand-new saved agent performs clean-room Case 5 verification in a new session;
- no Oval Office promotion, APA IDs, or APA database/fabric writes.

## Forward effect

V51 prospectively supersedes V50 for new calibration/certification runs only. V50 and all predecessor contracts, adapters, runs, findings, and preserved evidence remain immutable history. No prior run is relabeled or deleted.
