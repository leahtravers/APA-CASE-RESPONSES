# APA Researcher Inventory Agent Contract V110

Status: `ACTIVE SUCCESSOR FOR CALIBRATION — NOT CERTIFIED`
Contract version: `RI-CONTRACT-V110`
Predecessor: `RI-CONTRACT-V109`
Effective date: 2026-09-20
Authority: Leah's standing Researcher Inventory calibration instruction.
Registrar record: `APA-EXEC-2026-09-20-CASES-RI-V110-CAL-0001`

## Prospective correction basis

V109 workflow run `35491035728` verified both Leah-approved immutable archetype workbooks against the required SHA-256 values with no repair and passed all deterministic apparatus/harness tests, then failed hidden semantic comparison on both approved archetype cases. The complete failed attempt remains preserved append-only under `calibration_history/researcher_inventory/35491035728-A1/`. The sealed holdout was not reached.

The demonstrated defect is worker-semantic rather than workbook-integrity or deterministic-harness behavior. V109 correctly removed an over-restrictive indispensability test, but its replacement rule treated too much source-present wording as an independent coordinate merely because it could be separately interpreted or typed. V110 therefore replaces broad source-differentiated projection with **represented-role admission**.

V110 is prospective only. V109 and all earlier contracts, runs, failures, correction records, and evidence remain historical evidence. No archetype rows, hidden counts, evaluator findings, prior scored outputs, calibration answers, or sealed holdout material are supplied to the worker.

## Mission

Read the complete source and recover a lightweight, source-faithful researcher inventory in exactly seven classes:

1. `PLACE`
2. `TIME`
3. `PERSON`
4. `OBJECT`
5. `LABEL`
6. `VERB`
7. `LOCATOR`

The target is the source's represented research structure at natural class-native grain. Preserve a coordinate when the source gives it a distinct represented role. Do not inventory wording merely because it is lexical, grammatical, descriptive, rhetorically vivid, independently interpretable, or easy to point to.

Do not perform APA scoring, protected-thread analysis, psychological interpretation, promotion, APA-ID creation, executive analysis, sovereign/admitted writing, or APA Data Fabric/database mutation.

## 1. Whole-source represented-structure map

Read the entire source before answering any requested class. Silently map represented situations and relations, including episodes, participants, acted-on or referred-to content, characterizations/states, event/state relations, scene and phase support, orientations, memories, reports, questions, intentions, alternatives, recurring relations, prospective situations, and present telling/reflection.

This map is an omission-control device. It is not a primitive generator and does not authorize one coordinate per word, clause, noun phrase, predicate, modifier, temporal expression, spatial expression, or discourse move.

## 2. Represented-role admission test

A primitive is admitted only when both gates pass.

### Gate A — exact class-native source identity

The source explicitly establishes the candidate at the smallest complete natural literal span for its class, except legitimate unnamed PLACE/TIME support may use null `source_wording` with an exact source cue.

### Gate B — distinct represented role

The candidate must occupy a distinct role in represented structure as one of:

- `PERSON`: a represented participant or stable social actor;
- `OBJECT`: a represented concrete, abstract, internal, relational, decision/choice, value, category, content, or figurative handle;
- `LABEL`: a characterization, state, identity, evaluation, comparison, correction, polarity, manner, posture, candidate label, acceptance, or rejection assigned within represented structure;
- `VERB`: an event, state, or relation edge that represents something occurring, holding, changing, being perceived/reported/thought/intended/decided/compared, or otherwise relating represented coordinates;
- `PLACE`: a scene/location support coordinate for represented material;
- `TIME`: an episode/period/phase support coordinate for represented material;
- `LOCATOR`: an orientation that situates a retained node, relation, scene, path, containment, recurrence, procedure, context, or comparison.

A coordinate may be local, one-use, mundane, neutral, nested, subtle, remembered, reported, prospective, or low-salience. It does **not** need to be indispensable to understanding the scene, and removing it need not make the frame unintelligible.

The decisive question is not “can this wording be separately interpreted?” and not “would the frame fail without it?” The question is: **does the source assign this candidate its own represented role?**

## 3. Reject surface-only candidates

Reject a candidate when its apparent identity is only surface wording rather than a represented role. This includes, as applicable:

- auxiliary, tense, aspect, copular, or grammatical support with no independent relation role;
- narration/discourse carriage, sequencing, filler, or rhetorical organization with no independent represented role;
- intensification, stylistic color, exclamation, or vivid wording that does not establish a distinct characterization/state;
- arbitrary lexical decomposition or token census;
- free-standing temporal or spatial wording that does not support a distinct represented phase/scene or orientation;
- bare prepositions, deictics, discourse adverbs, or connectors without a distinct orienting role;
- clause/proposition wrappers whose represented work is already carried by retained coordinates;
- duplicate projections of the same represented role;
- restatements that do not establish a new represented coordinate.

A phrase is not admitted merely because it can be assigned a semantic type.

## 4. Projection splitting without atom explosion

When one source span contains several different represented roles, split it into the smallest complete class-native coordinates needed to preserve those roles.

For example in the abstract: a relation may have a separate content handle, characterization, orientation, or scene support. Keep those as separate coordinates only when the source actually represents them as distinct roles.

Do not split grammar, particles, complements, modifiers, or incidental wording merely because they are linguistically separable. Preserve particles, prepositions, negation, modality, uncertainty, attribution, comparison, idiom/dialect, and complements when they are required to keep the admitted role semantically complete.

## 5. PLACE and TIME — represented support roles

PLACE and TIME are support classes, not token inventories.

After mapping the source, preserve each distinct scene/location or episode/period/phase that supports represented material when the source differentiates that support role. Broad and local support may coexist when they serve genuinely different support roles.

Unnamed support is allowed when the source clearly establishes the scene/phase but does not name it. Use `source_wording = null`, an exact source cue, and a neutral mechanical tag.

Do not create PLACE from every physical noun, destination phrase, or spatial phrase. Do not create TIME from every temporal token, duration, recurrence word, transition, tense, or action. A support coordinate must support a represented scene/phase as its own role.

## 6. PERSON — represented participants

Retain the speaker and each distinct source-established human/social actor or stable group that has a represented participant role. Participation may be direct, offscreen, remembered, reported, possessive within a material relation, relational, institutional, or prospective.

Merge aliases/coreference. Reject rhetorical, generic, or nonreferential addressees and wording that names no stable represented actor.

## 7. OBJECT — represented handles

Retain each represented concrete, abstract, internal, relational, decision/choice-like, value-like, set/category, reported-content, or figurative handle when the source treats it as a stable thing/content coordinate in represented structure.

A handle may qualify because it is acted on, possessed, exchanged, checked, contrasted, questioned, remembered, reported, selected, decided about, located, valued, or otherwise reified.

Reject noun census, generic pronouns/deixis, arbitrary nominalizations, discourse topics, incidental nouns, and proposition wrappers that merely package other retained roles.

## 8. LABEL — represented characterization or state

Retain the smallest complete source-native characterization when the source actually assigns or presents a distinct quality, state, identity, evaluation, comparison, candidate/question label, correction, acceptance/rejection, polarity, manner, or posture to represented structure.

A LABEL may be subtle, idiomatic, colloquial, negated, uncertain, figurative, comparative, or one-use. Reject descriptive color, intensification, exclamation, rhetorical flourish, and modifiers that do not establish an independently represented characterization/state.

## 9. VERB — represented event/state/relation edges

Retain the smallest complete source-supported predicate span when the source presents a distinct represented event, state, or relation edge.

Eligible relations include actions, states, attempts, responses, movement, possession, perception, communication/report, cognition, intention, questions, decisions, comparison, evaluation, transition, and location/state relations.

A simple relation may qualify even when one-use or low-salience. But grammatical support does not qualify merely because it is verbal. In particular, do not retain a bare auxiliary or copular shell when all represented work is carried by another retained characterization/content/state and the shell adds no distinct relation identity.

Reject narration/discourse organizers with no represented relation, redundant restatements, and oversized proposition wrappers. Preserve required particles/complements for a qualifying relation, but do not swallow independently typed roles into the VERB merely to make a larger phrase.

## 10. LOCATOR — represented orientation roles

Retain a LOCATOR when an exact source span separately orients a retained node, relation, or scene by spatial position, containment, path, direction, origin/destination, proximity, accompaniment, recurrence, procedure/relation, internal/mental context, temporal position, or figurative/comparative orientation.

Reject bare prepositions, ordinary argument/topic markers, discourse connectors, unanchored deictics, duplicated TIME support, and free-standing spatial/temporal wording that does not orient retained structure.

## 11. Functional class assignment

Classify by represented role, not surface grammar:

- human/social actor → `PERSON`
- thing/content/referential handle → `OBJECT`
- characterization/state/evaluation/identity → `LABEL`
- scene/location support → `PLACE`
- episode/period/phase support → `TIME`
- event/state/relation edge → `VERB`
- orientation/situating relation → `LOCATOR`

Cross-class overlap is allowed only when the exact same source span genuinely performs two distinct represented roles. Similar wording alone is not enough.

## 12. Natural atomic span and literal lock

For every admitted coordinate, choose the smallest exact contiguous source span that preserves the represented role.

Preserve when semantically required:

- particles and required prepositions;
- reflexives;
- essential complements;
- negation;
- modality;
- uncertainty;
- questions;
- attribution;
- comparison;
- idiom/dialect;
- hypothetical, prospective, reported, and corrective posture.

Never normalize, clean, improve, translate, diagnose, euphemize, paraphrase, lemmatize into a different surface form, or substitute synonyms.

Every non-null `source_wording`, every `source_cue`, and every non-null `order_cue` must be a character-for-character contiguous source substring. Neutral mechanical tags are allowed only for legitimate unnamed PLACE/TIME support.

## 13. Identity, ordering, and deduplication

Primitive identity follows represented role identity, not mention count.

Merge true aliases, coreference, same-role repeats, inflection-only repeats, and duplicate head/full-span variants representing one stable coordinate. Do not merge distinct represented roles merely because they are similar or reconstructable from one another.

Code owns canonical IDs. The worker supplies neutral identity keys only for merge. Order by first source establishment after coreference, subject to apparatus speaker-first PERSON and genuine broad-before-contained support rules. Do not reorder by importance or real-world chronology.

## 14. Primitive freeze audit

Repeat until stable, in this order:

1. whole-source represented-structure map;
2. role-admission audit — every retained coordinate has a distinct represented role;
3. omission audit — check local, low-salience, one-use, remembered, reported, prospective, and nested roles;
4. support audit — check source-differentiated PLACE/TIME roles, including legitimate unnamed support;
5. anti-surface audit — remove grammar, auxiliaries, discourse carriage, rhetoric/style, lexical/token census, and unanchored temporal/spatial fragments;
6. projection-splitting audit — split only genuinely different represented roles;
7. functional-class audit;
8. atomic-span audit;
9. literal-lock audit;
10. semantic-dedup audit.

Freeze all primitives only after these audits are stable.

## 15. Relation-instance compound construction

Only after all seven primitive classes are frozen, reread the source relation by relation.

For each distinct retained VERB relation instance, emit the smallest complete compound linking the frozen coordinates that actually participate in that exact represented relation instance. Include participant, content, support, orientation, and characterization refs only when they play a role in that relation.

Additional non-VERB compounds are allowed only when the source represents a relation/state structure not already captured by a retained VERB relation compound.

Do not emit graph closure, every possible pair, arbitrary co-occurrence bundles, singleton equivalents, generic question closure, duplicate restatements, subset/superset permutations of the same relation, or scene mega-bundles. Do not use rejected surface fragments as compound members. Compounds never justify a missing, extra, merged, renamed, or retyped primitive.

## 16. Completion standard

The inventory is complete when:

- the whole source was read before class extraction;
- every retained coordinate has exact class-native source identity and a distinct represented role;
- legitimate local, one-use, low-salience, remembered, reported, prospective, and nested roles are not pruned for lack of importance;
- grammar, auxiliary shells, discourse carriage, lexical/style census, unsupported wrappers, incidental wording, and true duplicates are excluded;
- PLACE/TIME preserve represented scene/phase support without token census;
- VERB preserves represented relation edges without grammar/predicate census;
- LOCATOR preserves represented orientations without preposition/deictic census;
- class assignment follows represented function;
- literal source wording/posture is preserved;
- compounds reconstruct each retained relation instance only from frozen role-bearing coordinates.

Never target hidden counts or infer hidden gold.

## 17. Isolation and certification gates

Never expose approved archetypes, evaluator findings, hidden counts, prior scored answers, calibration answers, or sealed holdout content/output to the worker.

Mechanical validator feedback may be returned only for deterministic schema, exact-source, tag-token, identifier, or equivalent mechanical defects. It is not hidden semantic evaluator guidance.

Case 5 remains inaccessible until one paired diagnostic batch and two paired repeatability batches for Case 2 + Case 6 pass under this same finalized V110 contract and saved-agent lineage. A calibrated-lineage Case 5 holdout attempt, if eventually reached by the workflow gate, is one-shot.

If that calibrated lineage passes Case 5, retire it. Create a brand-new saved agent using only finalized V110 durable instructions in a new session with no prior calibration-session or holdout-output access. Certification requires that fresh agent to pass Case 5.

All outputs remain candidate research only. No promotion, Oval Office admission, APA-ID minting, or APA Data Fabric/database writing is authorized.

## Supersession boundary

`RI-CONTRACT-V109` remains controlling historical authority for V109 runs. `RI-CONTRACT-V110` supersedes V109 only for new Researcher Inventory calibration/execution begun after V110 routing.

Retained from V109 and predecessors: immutable archetype verification and repair gate; complete-source reading; seven-class separation; legitimate low-salience/one-use eligibility; legitimate unnamed PLACE/TIME support; exact-source literal lock; semantic identity/deduplication; primitive freeze; candidate/evaluator/holdout isolation; append-only attempt history; deterministic harness corrections; bounded same-session transport recovery; one-shot holdout; clean-room certification; candidate-only boundary; no-promotion/no-APA-ID/no-database-write prohibitions.

Superseded prospectively: V109's broad source-differentiated projection criterion where it admits a coordinate merely because source wording is separately interpretable or typable. V110 requires a distinct represented role while expressly rejecting both lexical census and indispensability-under-removal pruning.
