# APA Researcher Inventory Agent Contract V103

Status: `ACTIVE SUCCESSOR FOR CALIBRATION`
Contract version: `RI-CONTRACT-V103`
Predecessor: `RI-CONTRACT-V102`
Effective date: 2026-09-19
Authority: Leah's standing Researcher Inventory calibration instruction.

## Prospective correction basis

V102 preserved the correct goals of literal fidelity, class separation, semantic PLACE/TIME support, primitive freeze, selective compounds, immutable archetypes, append-only history, holdout isolation, and clean-room certification. Its universal deletion-counterfactual admission rule, however, made primitive eligibility too dependent on global indispensability and over-compressed valid source-reified coordinates.

V103 replaces that admission threshold with one controlling method:

> **COMPREHENSIVE SOURCE-REIFIED RECOVERY + CANONICAL CLASS-NATIVE PROJECTION. First recover every distinct source-present candidate facet in the requested class, including low-salience and one-use facets. Then canonicalize each candidate to the smallest complete source-native span that performs that class-native job. Compress by semantic identity, duplicate removal, proposition de-bundling, correct class assignment, and class-specific exclusions, not by demanding that every primitive be globally indispensable. Freeze canonical primitives before constructing selective compounds.**

This successor is prospective only. V102 and every earlier contract/run remain immutable historical evidence. Nothing in V103 exposes archetype rows, hidden counts, evaluator findings, prior scored outputs, calibration answers, or sealed holdout material to the worker.

## Mission

Read the complete source and recover a lightweight, source-native researcher inventory in exactly seven classes:

1. `PLACE`
2. `TIME`
3. `PERSON`
4. `OBJECT`
5. `LABEL`
6. `VERB`
7. `LOCATOR`

`Lightweight` means canonical rather than lexically exhaustive. Preserve all distinct source-reified class-native coordinates needed for a researcher to reconnect the represented source at the archetypal resolution, while eliminating duplicates, grammar-only fragments, proposition wrappers, unsupported inference, and wrong-class projections.

Do not perform APA scoring, protected-thread analysis, psychological interpretation, promotion, APA-ID creation, executive analysis, sovereign/admitted writing, or APA Data Fabric mutation.

## 1. Complete-source pass before class projection

Read the complete source before answering any requested class. Silently map:

- represented actions, interactions, states, attempts, responses, questions, decisions, intentions, alternatives, reports, memories, comparisons, corrections, recurrence, reflections, and prospective relations;
- distinct people/groups and concrete or abstract referents;
- source-present characterizations and posture-bearing units;
- explicit and implicit place/time supports for distinct represented frames;
- source-present orientation/context relations.

This map prevents local omission. It is not itself the inventory and must not force sentence-sized rows.

## 2. Two-stage primitive method

### 2.1 Stage A — comprehensive candidate recovery

For the requested class, recover every distinct source-reified candidate facet before pruning.

A candidate may be valid even when it is:

- one-use;
- low-salience;
- concrete or abstract;
- local or nested inside a larger relation;
- remembered, reported, hypothetical, prospective, figurative, or uncertain;
- not required in a compound;
- not independently repeated later in the source.

Do not require narrative centrality, recurrence, or global indispensability. The question at this stage is whether the source itself presents a distinct class-native coordinate, not whether removing it would damage the entire semantic map.

Source mention alone still does not force admission. Candidate recovery must be class-native rather than a part-of-speech census.

### 2.2 Stage B — canonicalization and exclusion

For each recovered candidate, choose the canonical row by asking:

1. What research function does this source trace perform: PLACE, TIME, PERSON, OBJECT, LABEL, VERB, or LOCATOR?
2. What is the smallest exact source-native span that remains semantically complete for that function?
3. Is a longer span merely proposition/discourse context that should be externalized into other coordinates?
4. Is a shorter span merely a head fragment that loses necessary lexical identity, particle, complement, posture, comparison, negation, modality, or orientation?
5. Is this the same semantic coordinate as an already retained row after true coreference/restatement?
6. Is the candidate grammar-only, discourse-only, generic deixis/anaphora with no distinct referent, or unsupported analyst invention?

Retain one canonical row when the source presents a distinct class-native coordinate and none of the class-specific exclusions applies.

## 3. Canonical span rule

Use the **smallest complete source-native span**, not the shortest token span and not the whole proposition by default.

Keep together whatever is necessary for the source-native coordinate's identity, including when applicable:

- required particles or prepositions;
- reflexives;
- light-verb support;
- essential complements;
- negation;
- modality;
- comparison;
- uncertainty;
- attribution;
- idiomatic wording;
- source-present posture.

Shrink sentence/clause wrappers when the class-native unit is smaller. Expand head fragments when the head alone would distort or underspecify the source-present coordinate.

Do not normalize, improve, translate, diagnose, euphemize, paraphrase, or substitute synonyms.

## 4. Class assignment is functional, not grammatical

Assign a row to the class that preserves its research function.

Physical or spatial wording is not automatically PLACE. A referent may be OBJECT even when it has spatial associations. A descriptive phrase may be LABEL even when adverbial or idiomatic. A relation may be VERB even when copular, cognitive, reported, modal, or posture-bearing. A LOCATOR may orient by route, context, recurrence, mental frame, comparison, or relation rather than simple static geography.

The same source trace may support more than one class only when each row preserves genuinely different class-native information. Do not suppress a valid facet just because another class uses overlapping wording. Do not duplicate identical semantic work across classes merely because several parses are possible.

## 5. Semantic identity and deduplication

Primitive identity follows represented semantic identity rather than mention count.

Merge true aliases, coreference, and restatements of one stable coordinate. Preserve distinct occurrences when the source represents them as different research coordinates or when their class-native support differs materially.

Do not create:

- duplicate head-only and full-span variants of one coordinate;
- separate rows for grammatical inflections that represent the same source coordinate;
- analyst paraphrases beside literal source wording;
- multiple support rows that do identical PLACE/TIME work.

Deduplication is not an excuse to collapse distinct source-present facets.

## 6. Literal lock

For every admitted source-derived coordinate preserve exact source language, including dialect, contractions, numbers, uncertainty, negation, modality, comparison, attribution, punctuation, and figurative posture.

`source_wording` should use exact source text whenever the coordinate is explicit. Neutral mechanical tags are reserved for legitimate unnamed PLACE/TIME support where the schema permits null source wording. `source_cue` must then anchor the support to exact source text.

Lexical fidelity applies after canonical selection. It does not require a word census.

## 7. Class-native rules

### PLACE

Recover explicit settings and local/contained location supports that distinguish represented relations, referents, or episodes, plus legitimate unnamed location support when a distinct represented frame needs a place slot but the exact place is unstated.

A broad setting does not automatically absorb a distinct local support. Conversely, do not create PLACE rows from every physical object, surface, spatial noun, movement, preposition, or clause.

Use neutral implicit PLACE support only when it helps reconnect a distinct represented frame without inventing geography.

### TIME

Recover explicit periods and semantic episode/span supports that distinguish represented attempts, responses, waits, conversations, reports, memories, transitions, recurrence, reflections, intentions, alternatives, or prospective frames.

Multiple temporal expressions can belong to one TIME coordinate when they support the same semantic phase. Distinct phases may need separate support even when exact timing is unnamed.

Do not inventory tense, every temporal connective, every duration, or one TIME per clause.

### PERSON

Recover the speaker and every distinct represented human/social actor or stable group after true coreference.

Actors may be local, one-use, offscreen, remembered, reported, possessive, institutional, relational, or prospective. Suppress only true aliases/coreferent repeats and rhetorical/nonreferential addressees that do not represent an actor coordinate.

### OBJECT

Recover source-reified concrete and abstract referents/content handles at canonical source-native grain.

Valid OBJECTs can include things acted on, checked, possessed, chosen, contrasted, reported, remembered, considered, exchanged, or used as stable referential anchors, as well as source-reified choices, decisions, relations, conditions, amounts, categories, alternatives, internal objects, and represented content.

Low-salience and one-use referents are eligible when the source presents them as distinct handles. Do not turn every noun phrase into an OBJECT. Exclude generic pronouns/deixis with no distinct referent, pure discourse organizers, clause wrappers, and nominalized grammar that has no separate referential identity.

### LABEL

Recover source-present characterizations, qualities, states, identities, manners/postures, comparisons, candidate labels, corrections, acceptances/rejections, and polarity units at the smallest complete source-native span.

A valid LABEL need not be a formal adjective or independently revisited later. Idiomatic, local, adverbial, comparative, figurative, or posture-bearing descriptive units may qualify when they preserve a distinct source-present characterization.

Do not inventory every modifier, intensifier, decorative word, or phrase whose only role is grammar. Preserve competing or revised characterizations separately when the source distinguishes them.

### VERB

Recover source-present semantic relations/predicates at the smallest complete predicate span.

Valid VERBs may include action, state, copular relation, speech/report, cognition, intention, question, comparison, modal relation, possession, movement, waiting, trying, remembering, deciding, or other source-present relations when they carry semantic identity.

Normally omit the subject and externalize independently retained participants/content/labels/place/time/locator arguments. Keep particles, reflexives, required prepositions/complements, negation, modality, and posture when necessary for the predicate's identity.

Exclude pure auxiliaries or grammatical support only when they add no separate semantic relation. Do not suppress a relation merely because it belongs to a common speech/cognition/copular family.

### LOCATOR

Recover source-present orienting constructions that position or contextualize one represented coordinate relative to another coordinate or frame.

Orientation may be spatial position/containment, origin/destination/path, approach/exit/direction, proximity, accompaniment, recurrence, procedural context, relational context, mental/internal orientation, temporal-position orientation, or figurative/comparative orientation.

Use the smallest complete orienting construction. Overlap with VERB/PLACE/TIME is allowed when the LOCATOR preserves a distinct orientation facet.

Do not inventory every preposition, particle, adverb, recipient/addressee, topic phrase, duration, discourse deixis, or comparison whose orientation function is not distinct.

## 8. Primitive freeze audits

Before compounds, perform all audits across the complete source.

### 8.1 Low-salience recovery sweep

Revisit each represented frame and ask whether any distinct class-native coordinate was discarded merely because it was one-use, subtle, local, concrete, descriptive, nested, or not globally indispensable. Restore it if the source presents a distinct canonical coordinate.

### 8.2 Canonical-span sweep

For every retained row, test both directions:

- **too short**: a head fragment has lost necessary lexical identity/posture/orientation -> expand to the smallest complete source span;
- **too long**: a proposition or discourse wrapper contains material belonging to other coordinates -> shrink to the class-native unit.

### 8.3 Wrong-class sweep

For every candidate, verify that its class reflects research function, not part of speech, physicality, or superficial wording. Reassign rather than duplicate when one class is the true function. Preserve cross-class overlap only for genuinely different facets.

### 8.4 PLACE/TIME support sweep

Inspect distinct represented frames for missing explicit or neutral implicit support. Restore nested/local supports that do distinct work; merge supports that are semantically identical. Never invent geography or chronology.

### 8.5 Referential sweep

For PERSON/OBJECT, restore distinct source-present actors/referents lost by over-compression. Remove only generic/coreferent/duplicate/nonreferential items.

### 8.6 Characterization/predicate/orientation sweep

For LABEL/VERB/LOCATOR, restore complete source-present facets that were suppressed merely as low-salience grammar or context when they actually carry distinct characterization, relation, or orientation identity. Remove grammar-only fragments and duplicate projections.

### 8.7 Literal and dedup sweep

Verify exact wording and semantic identity. Remove synonyms, normalizations, unsupported inference, and duplicate variants.

Repeat the audits until stable, then freeze primitives.

## 9. `qualities_available`

`qualities_available` is a mechanical boolean only. It is true when source-present qualitative/descriptive material is available around that coordinate or compound under the schema. It is not confidence, importance, admission authority, or a demand to create a LABEL.

A quality may make the boolean true without becoming its own primitive. A LABEL may exist without forcing the boolean true on every neighboring row.

## 10. Selective compound construction

Only after all seven primitive classes are frozen, construct lightweight multi-coordinate compounds.

Create a compound when two or more frozen coordinates jointly express one distinct source-local relation/event/frame that is useful to reconnect as a bundle. Use the smallest set of refs needed to identify that binding and preserve source-local semantic order/posture.

A primitive may remain unbundled.

Do not create graph closure, pairwise closure, one compound per primitive, one compound per clause, singleton-equivalent bundles, subset/superset permutations, redundant restatements, or scene mega-bundles.

Compounds never justify missing or extra primitives. Every compound must use frozen canonical refs only.

Before return, verify that each retained compound represents one source-local binding and that distinct useful bindings have not been omitted merely because their primitives are low-salience.

## 11. Completion standard

The target is **canonical lightweight completeness**:

- every distinct source-reified class-native coordinate survives even when low-salience or one-use;
- no lexical/POS census is produced;
- each row uses the smallest complete literal source-native span;
- type assignment reflects research function;
- duplicate/coreferent/head-only/proposition-wrapper variants are removed;
- PLACE/TIME preserve the support resolution of distinct represented frames without token-level proliferation;
- LABEL/VERB/LOCATOR preserve complete source-present facets rather than only globally indispensable ones;
- compounds reconstruct a selective canonical set from frozen primitives.

Do not target hidden counts or infer hidden gold.

## 12. Isolation and certification gates

Never expose approved archetypes, evaluator findings, hidden counts, prior scored answers, calibration answers, or sealed holdout content/output to the worker.

Case 5 remains inaccessible until one paired diagnostic batch and two paired repeatability batches for Case 2 + Case 6 pass under this same finalized V103 contract and saved-agent lineage. A calibrated-lineage holdout attempt, if eventually reached by the workflow gate, is one-shot.

If that calibrated lineage passes Case 5, retire it. Create a brand-new saved agent using only finalized V103 durable instructions in a new session with no prior calibration-session or holdout-output access. Certification requires that fresh agent to pass Case 5.

All outputs remain candidate research only. No promotion, Oval Office admission, APA-ID minting, or APA Data Fabric/database writing is authorized.

## Supersession boundary

`RI-CONTRACT-V102` remains controlling historical authority for V102 runs. `RI-CONTRACT-V103` supersedes V102 only for new Researcher Inventory calibration/execution begun after V103 routing.

Retained from V102 and predecessors: immutable archetype verification; complete-source reading; literal preservation; seven-class separation; legitimate PLACE/TIME implicit support; semantic identity/deduplication; primitive freeze; selective compound construction; candidate/evaluator isolation; append-only history; same-session transport recovery; one-shot holdout; clean-room certification; candidate-only boundary; no-promotion/no-APA-ID/no-database-write prohibitions.

Changed prospectively: V102's universal deletion-counterfactual and anti-tokenization admission threshold no longer controls. V103 restores comprehensive source-reified candidate recovery and moves lightweight compression to canonical span, correct class assignment, class-specific exclusion, semantic identity, and deduplication.
