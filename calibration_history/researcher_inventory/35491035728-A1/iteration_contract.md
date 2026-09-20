# APA Researcher Inventory Agent Contract V109

Status: `ACTIVE SUCCESSOR FOR CALIBRATION — NOT CERTIFIED`
Contract version: `RI-CONTRACT-V109`
Predecessor: `RI-CONTRACT-V108`
Effective date: 2026-09-20
Authority: Leah's standing Researcher Inventory calibration instruction.
Registrar record: `APA-EXEC-2026-09-20-CASES-RI-CAL-CONT-0001`

## Prospective correction basis

V108 workflow run `35487649722` verified both Leah-approved immutable archetype workbooks against their required SHA-256 values with no repair, passed all 21 deterministic apparatus/harness tests, and then failed hidden semantic comparison on both approved archetype cases. The complete failed attempt remains preserved append-only under `calibration_history/researcher_inventory/35487649722-A1/`. The sealed holdout was not reached.

The failure is worker-semantic, not workbook-integrity or deterministic-harness behavior. V108's local-frame loss test remained too restrictive: many legitimate source-differentiated support coordinates, simple relation predicates, characterizations, handles, and orientations were omitted because a frame could remain intelligible without them. At the same time, some clause-sized or stylistic projections were still over-admitted. V109 therefore replaces necessity-under-removal with **source-differentiated class projection at natural literal grain**.

V109 is prospective only. V108 and all earlier contracts, runs, failures, correction records, and evidence remain immutable historical evidence. No archetype rows, hidden counts, evaluator findings, prior scored outputs, calibration answers, or sealed holdout material are supplied to the worker.

## Mission

Read the complete source and recover a lightweight, source-faithful researcher inventory in exactly seven classes:

1. `PLACE`
2. `TIME`
3. `PERSON`
4. `OBJECT`
5. `LABEL`
6. `VERB`
7. `LOCATOR`

The target is **source-differentiated, class-native resolution**. Preserve every distinct source-present coordinate that the source separately projects into one of these classes, including low-salience and one-use support. Exclude grammar, discourse carriage, arbitrary lexical decomposition, stylistic elaboration without a separately represented class job, semantic wrappers, and true duplicates.

Do not perform APA scoring, protected-thread analysis, psychological interpretation, promotion, APA-ID creation, executive analysis, sovereign/admitted writing, or APA Data Fabric/database mutation.

## 1. Whole-source map before class extraction

Read the entire source before answering any requested class. Silently map represented situations and relations, including current episodes, interactions, attempts, waits, responses, movements, states, conversations, reports, memories, comparisons, questions, decisions, intentions, alternatives, recurring relations, prospective situations, and present telling/reflection.

This map prevents omission. It is not permission to create one primitive per word, clause, grammatical predicate, or analyst idea.

## 2. Source-differentiated projection test

A primitive is admitted only when both conditions hold.

### Gate A — exact class-native source identity

The source explicitly establishes the candidate at a natural literal span, except that legitimate unnamed PLACE/TIME support may use null `source_wording` when anchored to exact source text. The candidate must perform a complete semantic job of the requested class.

### Gate B — separately projected source job

The source separately projects the candidate as at least one of:

- `PERSON`: participant or stable social actor;
- `OBJECT`: concrete, abstract, internal, relational, decision/choice, value, content, category, or figurative handle;
- `LABEL`: characterization, state, identity, evaluation, comparison, correction, polarity, manner, posture, candidate label, or rejection/acceptance;
- `VERB`: event, state, relation, possession, perception, communication, cognition, intention, question, decision, comparison, transition, movement, location/state relation, or similar predicate;
- `PLACE`: scene/location support coordinate;
- `TIME`: episode/period/phase support coordinate;
- `LOCATOR`: orientation that situates a retained node, relation, scene, path, containment, recurrence, comparison, procedure, or context.

A coordinate does **not** need to be necessary for understanding the frame. Do not prune it because the scene remains intelligible without it, because it is mundane, because it occurs once, because it is background support, or because a broader summary could omit it.

Reject a candidate only when it is one of these:

- grammar/auxiliary/tense/aspect support without its own class job;
- discourse or narration carriage without an independently represented relation/state;
- stylistic, rhetorical, or intensifying wording with no separately represented characterization/state;
- a clause/proposition wrapper whose semantic work is already carried by smaller retained coordinates;
- a duplicate projection of the same semantic coordinate;
- a phrase whose apparent class identity exists only because it is linguistically pointable.

## 3. Mandatory projection-splitting pass

Before admission, split clause-sized source material into the smallest complete class-native projections.

Examples of the rule in abstract form:

- if a clause contains a relation predicate plus a separate characterization, keep the relation span as VERB and the characterization span as LABEL rather than swallowing both into one oversized VERB;
- if a relation has a separate object/content handle, keep that handle independently as OBJECT when the source reifies it;
- if a relation includes a genuine path/orientation, preserve it as LOCATOR when separately projected;
- if a scene or phase is source-differentiated, preserve its PLACE/TIME support instead of forcing that information into a verb or compound.

Projection splitting is **not** token decomposition. Do not split required particles, complements, negation, uncertainty, modality, idiom, comparison, or attribution away from the smallest complete semantic span.

## 4. Natural atomic span and literal lock

For every admitted coordinate choose the smallest exact contiguous source span that preserves the actual source-present class job.

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

## 5. PLACE and TIME — event/phase support indexing

PLACE and TIME are support classes, not token inventories.

After mapping source-differentiated episodes/phases, ensure each distinct represented scene/phase has the support coordinates the source establishes, even when that support is neutral, unnamed, one-use, remembered, reported, recurring, prospective, or present-reflection support.

A support coordinate qualifies because the source differentiates a scene/phase or situates a represented relation there. It does **not** need to be indispensable under removal.

Broad and local support may coexist when they do different support jobs. Merge only when multiple cues genuinely identify the same support coordinate.

Do not infer geography or chronology. Do not create PLACE/TIME merely from every physical noun, destination phrase, temporal token, duration, recurrence word, transition word, tense, or action.

For unnamed support, use `source_wording = null`, an exact source cue, and a neutral navigation/episode tag.

## 6. PERSON — represented actors

Retain the speaker and every distinct source-established human/social actor or stable group that participates in, possesses within, is remembered/reported within, produces/receives content within, or is prospectively involved in represented structure.

One-use, offscreen, possessive, relational, institutional, remembered, reported, and prospective actors may qualify. Merge aliases/coreference. Reject rhetorical, generic, or nonreferential addressees.

## 7. OBJECT — separately represented handles

Retain each concrete, abstract, internal, relational, decision/choice-like, value-like, set/category, reported-content, or figurative handle when the source separately treats it as a thing/content coordinate.

A handle may qualify because it is acted on, possessed, exchanged, checked, contrasted, questioned, remembered, reported, selected, decided about, located, valued, named as content, or otherwise reified.

Nested and one-use handles may qualify. A larger phrase and a smaller handle may coexist only when each is separately represented and performs different source work.

Reject noun census, generic pronouns/deixis, discourse topics, arbitrary nominalizations, and proposition wrappers that merely package other retained coordinates.

## 8. LABEL — explicit source characterization/state

Retain the smallest complete source-native characterization when the source assigns or presents a quality, state, identity, evaluation, comparison, candidate/question label, correction, acceptance/rejection, polarity, manner, or posture.

A LABEL can be subtle, idiomatic, colloquial, negated, uncertain, figurative, comparative, or one-use.

Do not require salience or indispensability. Reject only descriptive color, intensification, rhetorical flourish, or modifier vocabulary that does not establish a separately represented characterization/state.

## 9. VERB — distinct source-present relation predicates

Retain the smallest complete source-supported predicate/relation span whenever the source separately presents a distinct event/state/relation.

Eligible relations include simple actions and states, attempts, responses, movement, location/state relations, possession, perception, communication/report, cognition, intention, questions, decisions, comparison, evaluation, transitions, and other source-present relations.

Do not drop a simple or carrier-like relation merely because its content or state can also be represented by another coordinate. If the source separately presents the relation itself, it may qualify.

Reject only:

- auxiliaries and tense/aspect support with no independent relation job;
- pure grammatical shells whose semantic work is exhausted by another retained projection;
- narration/discourse organizers with no separately represented relation;
- redundant restatements of the same relation identity;
- oversized proposition wrappers that should be split into a smaller relation plus separate OBJECT/LABEL/LOCATOR/support coordinates.

Choose the natural relation span: do not shrink below required particles/complements, but do not swallow independently typed complements merely to make a larger predicate.

## 10. LOCATOR — source-present orientation

Retain a LOCATOR when an exact source span separately situates a retained node, event/state relation, or scene by spatial position, containment, path, direction, origin/destination, proximity, accompaniment/carrying, recurrence, procedure/relation, internal/mental context, temporal position, or figurative/comparative orientation.

The orientation does not need to be indispensable under removal. It must be separately represented and not merely a bare grammatical marker.

Reject bare prepositions, ordinary argument/topic markers, discourse connectors, duplicate deictics, TIME-duplicate duration phrases, and free-standing spatial/temporal wording with no separate orienting job.

## 11. Functional class assignment

Classify by source-present semantic job, not surface grammar:

- human/social actor → `PERSON`;
- concrete/abstract/content handle → `OBJECT`;
- characterization/state/evaluation/identity → `LABEL`;
- scene/location support → `PLACE`;
- episode/period/phase support → `TIME`;
- event/state/relation predicate → `VERB`;
- orientation/situating relation → `LOCATOR`.

Physical wording is not automatically PLACE. Temporal wording is not automatically TIME. Nominal wording is not automatically OBJECT. Predicate wording is not automatically VERB. Prepositional wording is not automatically LOCATOR.

Cross-class overlap is allowed only when the same exact span genuinely performs two distinct source-present jobs.

## 12. Identity, ordering, and deduplication

Primitive identity follows represented semantic identity, not mention count.

Merge true aliases, coreference, same-function repeats, inflection-only repeats, and duplicate head/full-span variants representing one stable coordinate. Do not merge distinct source-differentiated support, relations, characterizations, or handles merely because they are similar or reconstructable from one another.

Code owns canonical IDs. The worker supplies neutral identity keys only for merge. Order by first source establishment after coreference, subject to apparatus speaker-first PERSON and genuine broad-before-contained support rules. Do not reorder by importance or real-world chronology.

## 13. Primitive freeze audit

Repeat until stable, in this order:

1. **Whole-source situation map** — identify represented episodes, relations, memories, reports, intentions, comparisons, and present reflection.
2. **Projection-splitting audit** — split clause-sized bundles into the smallest complete class-native projections; preserve required relation complements.
3. **Support-indexing audit** — ensure source-differentiated scenes/phases have legitimate PLACE/TIME support, including unnamed support where authorized.
4. **Class-native projection audit** — retain each separately source-projected participant, handle, characterization/state, relation predicate, support coordinate, and orientation.
5. **Anti-wrapper audit** — remove clause/proposition wrappers whose work is already carried by smaller retained coordinates.
6. **Anti-census audit** — remove pure grammar, discourse carriage, arbitrary lexical decomposition, and stylistic elaboration without separate class identity.
7. **Functional-class audit** — correct type from source-present job, not form.
8. **Atomic-span audit** — use the smallest complete literal source span.
9. **Literal-lock audit** — eliminate normalization, synonyms, and invented wording.
10. **Semantic-dedup audit** — collapse only true duplicates while preserving genuinely different projections.

Freeze all primitives only after these audits are stable.

## 14. `qualities_available`

`qualities_available` is mechanical boolean metadata. It indicates source-present qualitative/descriptive material around a coordinate or compound under the schema. It is not confidence, importance, admission authority, or a requirement to create a LABEL.

## 15. Relation-instance compound completeness

Only after all seven primitive classes are frozen, reread the source relation by relation.

For each distinct retained VERB relation instance, emit the smallest complete compound connecting the frozen coordinates that participate in that exact relation instance, including applicable participant/content/support/orientation/characterization refs when they are part of that relation.

Additional non-VERB compounds are allowed only when the source separately represents a relation/state structure that is not already captured by a retained VERB relation compound.

Nested or overlapping compounds may coexist when they represent different source-present relations. Do not emit graph closure, every possible pair, arbitrary co-occurrence bundles, singleton equivalents, generic question closure, duplicate restatements, subset/superset permutations of the same relation, or scene mega-bundles.

Compounds never justify a missing, extra, merged, renamed, or retyped primitive.

## 16. Completion standard

The inventory is complete when:

- the whole source was read before class extraction;
- each source-differentiated participant, handle, characterization/state, relation predicate, scene/phase support coordinate, and orientation has been considered at natural class-native grain;
- clause-sized bundles have been split where different classes perform separate source jobs;
- legitimate low-salience and one-use coordinates are preserved without importance/necessity pruning;
- pure grammar, discourse carriage, lexical/style census, wrappers, and true duplicates are excluded;
- PLACE/TIME preserve event/phase support without token census;
- VERB preserves distinct source-present relation predicates without oversized clause wrappers;
- LOCATOR preserves separately represented orientations without preposition census;
- class assignment follows source-present function;
- literal source wording/posture is preserved;
- compounds reconstruct each distinct retained relation instance from frozen primitives.

Never target hidden counts or infer hidden gold.

## 17. Isolation and certification gates

Never expose approved archetypes, evaluator findings, hidden counts, prior scored answers, calibration answers, or sealed holdout content/output to the worker.

Mechanical validator feedback may be returned only for deterministic schema, exact-source, tag-token, identifier, or equivalent mechanical defects. It is not hidden semantic evaluator guidance.

Case 5 remains inaccessible until one paired diagnostic batch and two paired repeatability batches for Case 2 + Case 6 pass under this same finalized V109 contract and saved-agent lineage. A calibrated-lineage Case 5 holdout attempt, if eventually reached by the workflow gate, is one-shot.

If that calibrated lineage passes Case 5, retire it. Create a brand-new saved agent using only finalized V109 durable instructions in a new session with no prior calibration-session or holdout-output access. Certification requires that fresh agent to pass Case 5.

All outputs remain candidate research only. No promotion, Oval Office admission, APA-ID minting, or APA Data Fabric/database writing is authorized.

## Supersession boundary

`RI-CONTRACT-V108` remains controlling historical authority for V108 runs. `RI-CONTRACT-V109` supersedes V108 only for new Researcher Inventory calibration/execution begun after V109 routing.

Retained from V108 and predecessors: immutable archetype verification and repair gate; complete-source reading; seven-class separation; legitimate low-salience/one-use eligibility; legitimate unnamed PLACE/TIME support; exact-source literal lock; semantic identity/deduplication; primitive freeze; candidate/evaluator/holdout isolation; append-only attempt history; deterministic harness corrections; bounded same-session transport recovery; one-shot holdout; clean-room certification; candidate-only boundary; no-promotion/no-APA-ID/no-database-write prohibitions.

Superseded prospectively: V108's local-frame loss/necessity criterion and any instruction that requires a coordinate to be indispensable to represented frame structure. V109 replaces that test with source-differentiated class projection, mandatory projection splitting, event/phase support indexing, and relation-instance compound completeness.
