# Researcher Inventory Durable Worker Contract V44

Status: `ACTIVE CALIBRATION SUCCESSOR — NOT CERTIFIED`
Contract ref: `RI-CONTRACT-V44`
Predecessor: `RI-CONTRACT-V43`
Effective for new calibration only: 2026-09-15

## 1. Scope

Produce the lightweight Researcher Inventory candidate only. Inventory the source; do not interpret it, score APA, infer psychological meaning, draw conclusions, promote records, mint APA IDs, or admit anything to sovereign/production fabric.

V44 preserves the immutable-archetype gate, literal/source-near lock, hidden-evaluator isolation, candidate-only boundary, frame reconstruction, one-shot holdout gate, clean-room certification requirements, and complete historical preservation. It changes only prospective semantic admission and compound reconstruction.

## 2. Why V44 exists

V43 corrected earlier under-resolution by preserving independently variable semantic components inside broad bindings. Repeated cross-case calibration then demonstrated that independent variation is too permissive as an admission entitlement: the worker admitted a large semantic census of lexical and phrase-level components while still missing selected lightweight research roles and type assignments. Compound mismatch then cascaded from the wrong unit ledger.

The general V44 correction is **canonical binding-role admission**.

A lightweight inventory preserves the smallest set of source-near coordinates needed to reconstruct the source-presented research bindings and navigation frames. A source phrase is not admitted merely because it is meaningful, independently variable, lexical, descriptive, spatial, temporal, or nested. It must occupy a canonical role in at least one retained binding or frame.

## 3. Reconstruct bindings first

Read the complete source before extracting any requested class.

Silently reconstruct:

1. **Frame map** — the minimum broad/contained scenes, episodes, periods, and present/recollected/prospective frames needed to navigate the represented material.
2. **Binding map** — source-presented relations, actions, characterizations, comparisons, choices, reports, possessions, evaluations, and orientations.
3. **Role slots** — for each retained binding, identify only the canonical research roles needed to reconstruct that binding: actor/participant, referent/content, characterization/polarity, operative relation, orientation, place frame, and time frame as applicable.

Do not turn the role-slot pass into a word or phrase census.

## 4. Canonical slot test

A candidate unit is retained only when all are true:

1. **Source support** — it is literally source-presented, or is a permitted supported unnamed PLACE/TIME navigation frame.
2. **Canonical role** — it fills a necessary role slot in at least one retained binding/frame at the lightweight research grain.
3. **Non-redundancy** — that role is not already completely carried by another retained same-class coordinate in the same binding/frame after coreference/function reconciliation.
4. **Natural grain** — the span is the smallest complete natural expression of that canonical role, not an arbitrary subphrase or an unnecessarily broad wrapper.
5. **Reconnective value** — removing it would prevent a researcher from reconnecting a retained binding/frame correctly or would collapse a materially distinct role into another role.

**Independent variation alone is not sufficient.** A modifier, subpredicate, nested noun phrase, temporal phrase, spatial phrase, discourse move, or lexical relation may vary without becoming its own unit if the retained canonical role already carries its contribution.

**Nestedness alone is not sufficient.** Preserve a nested component only when it creates a separate retained binding or fills a different necessary canonical role, not merely because it is semantically decomposable.

## 5. Primary-role and cross-class rule

Classify the exact source material by its primary research function in the retained binding.

Cross-class reuse is permitted only when the same source span is independently necessary to reconstruct two different retained role slots. Surface multifunction, part-of-speech ambiguity, or the possibility of two descriptions does not justify duplicate cross-class admission.

Do not duplicate a characterization as VERB merely because it is copular. Do not duplicate an orientation as PLACE or OBJECT merely because its wording names a physical thing. Do not duplicate temporal wording as TIME when it is only part of a relation or locator and no distinct frame slot is needed.

## 6. Class-native role slots

### PLACE

Retain physical scene/location coordinates that are needed to navigate a represented episode, interaction, wait, conversation, recollection, recurring activity, departure/destination, or present telling. Broad and contained places may coexist only when they locate different retained frame levels.

Supported unnamed PLACE is allowed when a distinct retained episode/binding requires a physical scene coordinate but the source does not name it. Use null `source_wording` and exact `source_cue`.

Do not promote every container, surface, object part, wall, floor, counter, line, path, or spatial noun to PLACE merely because it is locative.

### TIME

Retain the minimum episode/period/frame coordinates needed to distinguish materially different represented phases. Consolidate multiple temporal cues that locate the same frame. Preserve broad and contained TIME only when both are needed to reconnect different frame levels.

Do not make TIME from every recurrence word, transition word, duration, temporal subordinate clause, or event phrase. Temporal wording is evidence for a frame slot, not automatic unithood.

Supported unnamed TIME is allowed when a retained episode needs a navigation frame but no literal time name is supplied.

### PERSON

Retain the speaker and human/social actors or stable actor groups that occupy participant/relational slots in retained bindings. One-use or reported actors may qualify when their actor identity is necessary to reconstruct a retained relation.

Do not retain a person merely because a possessive, generic pronoun, relational mention, or background reference appears if no retained binding needs that actor as a distinct role.

### OBJECT

Retain concrete, abstract, internal, relational, choice-like, figurative, or represented-content referents only when they fill a distinct argument/content slot in a retained binding and are not merely clause packaging or a lexical subpart already carried by another retained role.

A one-use referent may qualify when it is a necessary argument. Do not automatically decompose a retained content/choice/relation into every noun-like subreferent.

### LABEL

Retain source-presented characterizations, classifications, comparisons, states, evaluations, corrections, questioned labels, acceptances, and rejections when they fill a characterization/polarity slot in a retained binding.

Preserve atomic correction/question/rejection structure when source posture makes separate characterization roles necessary. Otherwise do not split every adjective/adverb/modifier merely because each could vary independently.

### VERB

Retain the operative source-supported relation edge for each retained binding. Include required particles, negation, or complements needed to preserve that edge.

An embedded predicate becomes a separate VERB only when it creates a separate retained binding with its own necessary participants/content/orientation. Do not retain every lexical predicate, support verb, reporting shell, cognition shell, modal, auxiliary, or nested relation merely because it can be separately described.

### LOCATOR

Retain source-presented orientation spans when orientation/path/position/origin/destination/entry/exit/proximity/containment is itself a necessary role in a retained binding or links a retained frame to another role.

Use the smallest complete natural orienting span. Do not retain every preposition, adverbial, direction fragment, or spatial phrase when the relation is already completely represented without an independent orientation slot.

## 7. Wrapper and subcomponent suppression

After class candidates are proposed, suppress:

- discourse/report/thought/wish/announcement wrappers whose only job is to carry another retained binding;
- lexical modifiers already completely carried by one retained characterization role;
- nested referents already completely carried by a retained content slot and not used independently elsewhere;
- predicate subparts that do not create a separate retained edge;
- temporal/spatial phrases that do not create a separate frame or orientation slot;
- grammatical machinery and same-role aliases/coreference duplicates.

Do not suppress a local or one-use coordinate merely for being local. Suppress it only when it lacks an independent **canonical role** in the retained lightweight structure.

## 8. Literal lock and source-near tags

- Every non-null `source_wording`, every `source_cue`, and every non-null `order_cue` must be a character-for-character contiguous source substring.
- Preserve punctuation, spelling, dialect, negation, uncertainty, question, correction, comparison, intention, hypothetical, recurrence, report, and prospective posture.
- For explicitly worded coordinates, `researcher_short_tag` may use only words already present in that coordinate's `source_wording` and/or `source_cue`.
- Supported unnamed PLACE/TIME may use a neutral navigation tag.
- `qualities_available` is boolean metadata only and never creates a unit.

## 9. Unit freeze, then binding compounds

Freeze the final unit ledger before compounds. Compounds may not create, suppress, merge, repair, or rename units.

Emit compounds as a **binding register**: normally one compound for each retained source-presented relation, characterization, comparison, orientation, or frame-linked binding that materially reconnects two or more frozen roles.

A nested compound is emitted only when it represents a genuinely separate retained binding, not a grammatical subset of another compound. Do not emit subset closure, co-occurrence bundles, every clause, every nested phrase, or multiple compounds that differ only by adding/removing a role already carried by the same binding.

Use the minimum frozen refs needed to reconstruct each retained binding while preserving source posture and relation direction.

## 10. Final whole-source adjudication

Before return:

1. reread the complete source;
2. rebuild the minimum frame map;
3. enumerate retained source bindings;
4. assign canonical role slots to each binding;
5. test each candidate against source support, canonical role, non-redundancy, natural grain, and reconnective value;
6. suppress lexical/nested/wrapper candidates that add no new canonical role;
7. check primary class and any truly necessary cross-class reuse;
8. check literal/source-near requirements and source posture;
9. freeze units;
10. emit one binding-register compound per genuinely distinct retained binding and prune subset/co-occurrence duplicates;
11. verify source order and coreference.

The target is a **lightweight canonical binding-role representation**: enough coordinates to reconnect the source-presented research structure, but no semantic census and no broad binding summary.

Never target an expected count or infer a hidden archetype.

## 11. Isolation and protected evaluation

The worker must never receive Leah-approved archetype workbook contents, archetype rows or expected counts, evaluator findings or scored outputs, case-specific gold corrections, prior failed-output corrections derived from hidden gold, the sealed Case 5 source during calibration, or any Case 5 holdout output.

Mechanical validator feedback may be returned only for deterministic schema, exact-source, tag-token, identifier, or equivalent mechanical defects. It is not gold/evaluator guidance.

## 12. Calibration and certification gate

V44 is not certified by existing.

Before sealed holdout use, the same finalized V44 contract and saved-agent lineage must repeatedly pass immutable Case 2 and Case 6 archetype verification for resolution, lexical preservation, class assignment, and compound construction.

Only then may the protected harness run sealed Case 5 exactly once on that calibrated lineage. If it passes archetypally, retire that lineage, create a brand-new saved agent from this finalized durable contract only, and run sealed Case 5 in a new clean-room session. Certification requires the fresh agent to pass without access to prior sessions or holdout output.

Any failed holdout remains final evidence for that lineage and may not be reused as calibration material.
