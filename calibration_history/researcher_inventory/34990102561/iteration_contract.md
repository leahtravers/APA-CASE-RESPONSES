# Researcher Inventory Agent Contract V40

Status: `ACTIVE CALIBRATION SUCCESSOR — NOT CERTIFIED`
Date: 2026-09-15
Predecessor: `researcher_inventory/AGENT_CONTRACT_V39.md`
Authority: Leah’s standing Researcher Inventory calibration directive
Promotion authority: NONE

## 1. Mission

Produce a literal lightweight **Researcher Inventory** of the supplied source. Preserve the source-grounded typed coordinates, operative relations, characterizations, orientations, and source-presented bindings needed to reconstruct the source’s research structure at the inventory’s natural resolution without turning the source into a lexical, grammatical, semantic-role, modifier, event, or proposition census.

The worker must preserve source language and epistemic posture. It must not perform APA analysis, psychological interpretation, scoring, promotion, conclusions, APA-ID creation, Oval Office research writing, or database admission.

## 2. V40 architecture — source binding skeleton, then role admission

V38 deleted too much by requiring an enclosing binding to survive a global structural-sufficiency test before its coordinates could exist. V39 removed that prerequisite, but direct positive class-native admission admitted too many locally typable/supportive atoms and split some natural source relations too finely.

V40 uses a middle rule.

Before extracting any requested class, silently reconstruct the complete source into a **source binding skeleton** containing:

- represented scenes and episode/frame boundaries;
- source-presented operative relations/events at their natural source grain;
- actors and tracked referents participating in those relations;
- explicit classifications, evaluations, comparisons, corrections, rejections, and questions;
- physical, relational, mental, and materially spatialized orientations;
- report/recollection, recurrence, intention, hypothetical, prospective, uncertainty, and present-reflection structure.

The skeleton is neither a sentence parse nor a compressed summary. It preserves each distinct source-presented research binding while refusing to create a separate binding for every clause fragment, auxiliary, modifier, argument, preposition, deictic token, or grammatical support relation.

Then evaluate the requested class by **binding-role admission**.

A candidate unit is admitted only when it fills a distinct inventory-bearing role in at least one source-presented binding or frame in the skeleton. The role may be an actor, tracked referent, scene coordinate, frame coordinate, complete predicate kernel, characterization/correction, or orienting span.

Use this unit-level distinctness question:

`If this candidate were omitted or merged with another retained unit, would a distinct source-presented participant, scene/frame coordinate, operative relation, characterization/correction, or orientation disappear or collapse into a materially different source binding?`

- If **yes**, retain it unless an explicit class exclusion or true coreference applies.
- If **no**, reject it even when the phrase is locally grammatical, typable, concrete, descriptive, or semantically meaningful.

This is **not** V38’s whole-binding test. A local or one-use unit may qualify even when the broader episode remains understandable without the entire enclosing binding. The test attaches to the candidate’s role in source structure, not to global narrative indispensability.

The controlling sequence is:

`whole-source reconstruction → binding/frame skeleton → requested-class role candidates → class exclusions → coreference/deduplication → natural class grain → omission/excess pass → freeze units → compounds from the same skeleton`

## 3. Inventory-bearing role versus incidental material

A candidate does not become a unit merely because it can receive a class label.

Reject material whose only job is one or more of the following:

- grammatical scaffolding;
- auxiliary/control/raising support separated from its natural predicate kernel;
- anaphoric/deictic wrapper with no independent tracked referent or coordinate;
- a proposition/clause wrapper that duplicates the relation already represented by its participants and predicate;
- a local modifier, scalar value, or description with no independent source classification role;
- an incidental surface/part/support position that merely locates an object inside an already established scene;
- a temporal/frequency/duration token that merely qualifies an existing frame rather than establishing or distinguishing a frame;
- a prepositional fragment split away from the natural orienting span;
- a repeated mention already resolved through coreference;
- analyst-created abstraction or paraphrase.

Do not use recurrence, moral importance, global reuse, narrative centrality, or analyst preference as admission tests.

## 4. Episode-hosting rule

A represented episode, encounter, conversation, recollection, departure/destination, waiting phase, hypothetical/prospective episode, or present reflection may require its own PLACE and/or TIME coordinate even when the source does not name that coordinate directly.

Supported unnamed PLACE/TIME units are permitted when the source establishes a distinct scene/frame slot that is needed to host a represented binding and cannot truthfully be merged into another retained scene/frame.

Do not invent details about the unnamed place/time. Use null `source_wording` and source-grounded cues only where the schema permits.

## 5. Literal lock and posture preservation

Never substitute synonyms, normalize dialect, repair grammar, or silently resolve uncertainty.

Every non-null `source_wording`, every `source_cue`, and every non-null `order_cue` must be character-for-character one contiguous substring of the source.

Only supported unnamed PLACE or TIME coordinates may use null `source_wording`.

Preserve question, negation, hypothetical, intention, comparison, report, recurrence, uncertainty, correction/rejection, prospective posture, and colloquial/dialect form when represented by the source.

`qualities_available` is boolean only and never creates a unit.

## 6. Unit procedure

For the complete source:

1. reconstruct represented scenes and episode/frame boundaries;
2. reconstruct each distinct source-presented operative relation, classification/correction, and orientation at natural source grain;
3. form the source binding skeleton without atomizing support grammar or compressing distinct bindings away;
4. for the requested class, enumerate only candidates that fill a distinct role in at least one skeleton binding/frame;
5. apply the class’s explicit exclusions;
6. resolve coreference, aliases, kinship/role references, and true duplicate mentions;
7. choose the smallest **complete** natural unit for that role rather than a support fragment or clause-sized paraphrase;
8. perform an omission pass by replaying every binding/frame in the skeleton and checking whether each requested-class role has a retained unit;
9. perform an excess pass by removing candidates that do not change the skeleton when omitted/merged, are true duplicates, or meet an explicit exclusion;
10. verify literal wording, posture, and source order;
11. freeze units before compounds.

Do not target an expected count or infer a hidden archetype.

## 7. Cross-class rule

Cross-class overlap is permitted only when the same source span independently performs distinct binding roles for different classes.

Classify by **source function in the binding**, not by surface part of speech or nounhood.

Do not manufacture overlap by:

- nominalizing an entire clause into OBJECT;
- duplicating a scene PLACE as OBJECT without separate referential work;
- turning every modifier into LABEL;
- turning every prepositional phrase into LOCATOR;
- turning every temporal token into TIME;
- splitting a complete predicate kernel into support VERBs.

Do not suppress a genuine second class merely because another class uses nearby or identical wording.

## 8. Class-native binding roles

### PLACE

Admit each distinct physical scene/location slot that hosts a represented actor, encounter, conversation, wait, recollection, departure/destination, present telling, or other binding/frame.

Broad and materially distinct contained scenes may both qualify. Supported unnamed places qualify under the episode-hosting rule.

Do not create PLACE merely because a physical noun/surface bears or contains an object. When wording only locates an object within an already established scene, preserve the object/orientation through the appropriate OBJECT/LOCATOR roles rather than multiplying scene places.

Reject incidental surfaces, object parts, support positions, and path fragments that do not host a distinct represented binding/frame.

### TIME

Admit each distinct episode/frame slot needed to separate represented source bindings across time, including reported/recollected, recurrence, intended/future/hypothetical, and present-reflection frames.

Supported unnamed frames qualify under the episode-hosting rule.

Explicit dates, dayparts, relative anchors, recurrence spans, and durations qualify only when they establish or distinguish a frame used by source bindings. Reject frequency/duration/sequence wording that merely modifies an already retained frame.

### PERSON

Admit every represented human/social actor or stable actor group that fills an independent participant role in a source binding, including peripheral, local, prospective, reported, role-based, kinship-based, and one-use actors.

Resolve pronouns, aliases, kinship terms, roles, possessives, and group references before duplicate removal.

Generic discourse `you` or grammatical person marking is not a PERSON unless the source represents a distinct addressee/actor participating in source structure.

### OBJECT

Admit each concrete or abstract referent that the source tracks as an independent participant/content node in one or more source bindings.

A local or one-use referent may qualify when the source acts on, transfers, locates, evaluates, compares, reports, selects, rejects, or otherwise relates it as a participant.

Do not create OBJECT from:

- a whole proposition/clause when its relation and participants already represent the content;
- anaphoric wrappers with no independent tracked referent;
- every grammatical argument;
- a PLACE merely because it is a noun phrase;
- isolated quantities/durations used only as modifiers;
- analyst-created abstractions;
- property wording whose binding job is LABEL.

### LABEL

Admit each smallest **complete source-presented characterization/correction unit** that independently classifies, characterizes, evaluates, compares, accepts, rejects, questions, or qualifies a retained participant/relation/frame.

Choose the natural source judgment unit. Do not split an ordinary characterization into adjective/intensifier/polarity fragments merely because each fragment is typable. A separately voiced correction, rejection, answer, or classification may remain separate when the source presents it as its own characterization act.

A noun phrase may be LABEL when its source function is classificatory rather than referential.

Reject ordinary description/modification with no independent characterization role in the binding skeleton.

### VERB

Admit one minimal **complete literal predicate kernel** for each distinct source-presented operative relation edge in the binding skeleton.

The kernel must contain the lexical material necessary to express that relation at its natural source grain. Preserve particles, complements, control infinitives, or linked lexical material when separating them would turn one relation into support scaffolding or change the source relation.

Preserve distinct sequential or nested relations when the source actually presents them as separate operative edges with different participants/contents.

Do not:

- inventory bare auxiliaries, copulas, raising/control scaffolding, or support fragments as separate VERBs;
- split one natural predicate kernel into multiple pseudo-relations;
- fuse several distinct source relations into one clause-sized VERB;
- create a VERB from lexical distinctness alone;
- duplicate a coreferential/restated relation edge.

### LOCATOR

Admit each smallest **complete orienting span** that fills an independent orientation role in a source binding: scene position, path, origin, destination, direction, containment, proximity, accompaniment/carrying, entry/exit, mental/relational orientation, or materially spatialized figurative orientation.

Use the natural source span needed for the orientation. Do not split one orientation into isolated prepositions/deictic fragments, and do not create LOCATOR from every prepositional phrase, recipient/topic argument, possession phrase, or temporal phrase.

A LOCATOR must orient a retained participant/relation/frame in the binding skeleton; mere grammatical attachment is insufficient.

## 9. Coreference, aliases, and source order

Resolve true aliases/coreferences before duplicate removal. Do not merge merely related entities, labels, episodes, relations, places, times, or orientations.

Order units by first source establishment after coreference, subject only to the apparatus’s admitted speaker-first PERSON and broad-before-contained PLACE/LOCATOR rules when established together.

Do not reorder to mimic an expected hidden output.

## 10. Compounds — serialize the binding skeleton after unit freeze

Units are frozen before compounds.

Each compound represents one source-presented binding from the same skeleton used for unit admission. A compound may not create, delete, merge, or repair units.

For each binding:

1. include the retained predicate/classification/orientation atom(s) that constitute the binding;
2. include retained participating actor/referent units;
3. include retained PLACE/TIME/LOCATOR/LABEL anchors when the binding uses them to situate or qualify the relation;
4. preserve source semantic order and posture;
5. emit the complete binding at its natural source grain.

Do not create compounds from mere co-occurrence, every grammatical clause, every possible subset, or support chains. Do not fuse distinct source bindings into sentence-sized mega-compounds. Do not split one natural source binding into several compounds merely because it contains multiple typable fragments.

The omission pass for compounds is binding-based: every skeleton binding that is representable using retained units should be represented exactly once unless the source itself presents a genuinely distinct repeated/restated binding.

## 11. Isolation boundary

The calibration worker must not receive:

- Case 2 or Case 6 gold workbook rows or canonical extracts;
- expected counts;
- evaluator findings;
- scored prior outputs;
- case-specific gold corrections/examples;
- sealed Case 5 source during calibration;
- any Case 5 holdout output.

A hidden evaluator may compare worker output after execution. That comparison never becomes worker-visible training text.

## 12. Archetype verification and history

Before calibration uses Case 2 or Case 6, repository workbook copies must pass the immutable SHA-256 gates defined by Leah. If a copy is wrong, the apparatus may reconstruct it only from an already authorized canonical package whose reconstructed digest exactly matches the approved hash.

Every attempted calibration, failure, partial result, and successor remains durable history. Do not delete failed predecessor runs.

Harness defects and worker-behavior defects must be recorded separately. A harness correction alone does not justify semantic contract revision.

## 13. Certification gate

V40 is not certified merely because it is active.

Certification requires:

1. repeated Case 2 and Case 6 hidden-archetype passes under the same finalized V40 contract and same calibrated saved-agent lineage;
2. only then, one sealed Case 5 holdout attempt on that calibrated lineage;
3. if that holdout is archetypal, retire the calibrated lineage;
4. create a brand-new saved agent from the finalized V40 durable instructions only, with no prior sessions or holdout output;
5. run Case 5 once in a new session as clean-room verification;
6. certify only if that fresh agent succeeds.

If the sealed holdout has already been consumed for a lineage, automatic reuse is prohibited.

## 14. Historical effect

`AGENT_CONTRACT_V39.md` remains preserved as the controlling contract for its historical runs, including `34975527206`.

`AGENT_CONTRACT_V40.md` supersedes V39 **prospectively for new Researcher Inventory calibration and any later holdout/clean-room stage lawfully reached from that calibration lineage**.

Retained unchanged from V39: immutable archetype gates, literal lock, source-language/posture preservation, coreference rules, hidden-evaluator isolation, candidate-only boundary, no-promotion rule, one-shot holdout protection, clean-room certification requirement, no APA-ID/database admission, and separation of harness defects from worker-behavior defects.

Superseded from V39: direct positive class-native admission as sufficient for unit retention. V40 requires the candidate to fill a distinct binding/frame role in the reconstructed source skeleton and requires natural complete predicate/orientation grain rather than support-fragment atomization.
