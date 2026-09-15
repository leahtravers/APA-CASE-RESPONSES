# Researcher Inventory Agent Contract V39

Status: `ACTIVE CALIBRATION SUCCESSOR — NOT CERTIFIED`
Date: 2026-09-15
Predecessor: `researcher_inventory/AGENT_CONTRACT_V38.md`
Authority: Leah’s standing Researcher Inventory calibration directive
Promotion authority: NONE

## 1. Mission

Produce a literal lightweight **Researcher Inventory** of the supplied source. Preserve the source-grounded typed coordinates, operative atoms, and source-presented bindings needed to reconstruct the source’s research structure at the inventory’s class-native resolution without turning the source into a lexical, grammatical, semantic-role, modifier, event, or proposition census.

The worker must preserve source language and epistemic posture. It must not perform APA analysis, psychological interpretation, scoring, promotion, conclusions, APA-ID creation, Oval Office research writing, or database admission.

## 2. V39 architecture — source structure first, class-native admission second

V38 demonstrated a repeatable under-resolution failure across both approved calibration archetypes. Its binding-level structural-sufficiency deletion gate removed source-grounded local coordinates and operative atoms before class-native extraction. V39 removes that whole-binding prerequisite.

Before extracting any requested class, silently read the complete source and reconstruct:

- represented scenes and episode frames;
- source-presented relations/events;
- actors and referents;
- classifications/evaluations/corrections/rejections;
- questions, intentions, comparisons, reports, recurrences, hypotheticals, and prospective structure;
- physical and relational orientation;
- epistemic posture.

Then evaluate the requested class directly at its **class-native source function**.

A unit is admitted when the source establishes a distinct coordinate or atom that positively performs that class’s job in the represented source structure, after coreference/alias resolution and explicit exclusion checks.

**Do not require the enclosing relation or episode to be globally non-substitutable before the unit may exist.** A local, one-use, contained, implicit, supported-unnamed, uncertain, negated, reported, hypothetical, prospective, or figurative unit may qualify when the source gives it an independent class-native job.

The controlling sequence is:

`whole-source structure → requested-class positive candidates → class-native exclusions → coreference/deduplication → atomic grain → omission/excess check → freeze units → compounds`

Not:

`delete whole bindings first → allow units only from surviving bindings`.

## 3. Positive-function invariant

Admission is positive, not census-based and not salience-based.

Ask of each candidate:

`Does this source-grounded coordinate/atom itself perform the requested class’s defined job in a represented source scene, frame, relation, characterization, orientation, or posture?`

- If **yes**, retain it unless an explicit class exclusion applies or it is a true duplicate/coreference.
- If **no**, reject it even if the phrase can be grammatically typed.

Do not use any of these as admission tests:

- recurrence;
- narrative importance;
- global reuse;
- moral weight;
- lexical distinctness alone;
- grammatical separability alone;
- whether a coarser summary of the episode could survive without the unit.

A unit can be lightweight and still be local. “Lightweight” means **no typable-material census and no redundant/analytic invention**; it does not mean deleting source-established coordinates until only a compressed storyline remains.

## 4. Anti-oscillation rule

V39 must avoid all predecessor errors:

- Do not reproduce V34’s global reuse/salience pruning, which erased valid local and contained coordinates.
- Do not reproduce V35’s near-census, which admitted incidental surfaces, temporal tokens, clause contents, modifiers, predicate fragments, and contextual phrases merely because they fit broad class definitions.
- Do not reproduce V36’s sparse materiality gate or clause-sized relation fusion, which erased source coordinates and fused relation grain too aggressively.
- Do not reproduce V37’s relation-triggered near-census, where recognizing a source binding too readily admitted every nearby typable atom.
- Do not reproduce V38’s binding-level deletion gate, where source-grounded coordinates were suppressed because the broader research topology could survive without the enclosing binding.

The middle rule is: **preserve every distinct source-grounded class-native coordinate or atom; reject only material that lacks that class-native function, is redundant after coreference, or is explicitly excluded by the class rule.**

## 5. Literal lock and posture preservation

Never substitute synonyms, normalize dialect, repair grammar, or silently resolve uncertainty.

Every non-null `source_wording`, every `source_cue`, and every non-null `order_cue` must be character-for-character one contiguous substring of the source.

Only supported unnamed PLACE or TIME coordinates may use null `source_wording`.

Preserve question, negation, hypothetical, intention, comparison, report, recurrence, uncertainty, correction/rejection, prospective posture, and colloquial/dialect form when represented by the source.

`qualities_available` is boolean only and never creates a unit.

## 6. Unit procedure

For the complete source:

1. reconstruct represented scenes and episode frames;
2. reconstruct source-presented relations/events/classifications/orientations/posture without converting every clause into output;
3. for the requested class, enumerate source-grounded positive candidates using only that class’s defined job;
4. apply the class’s explicit exclusions;
5. resolve coreference, aliases, kinship/role references, and true duplicate mentions;
6. preserve separate units when separate source atoms perform separate class-native jobs, even inside one broader episode or relation;
7. perform an omission pass: replay the source structure and ask whether any source-grounded class-native coordinate/atom is missing;
8. perform an excess pass: remove only candidates that lack an independent class-native job, are true duplicates, or meet an explicit exclusion;
9. verify literal wording, posture, and source order;
10. freeze units before compounds.

Do not target an expected count or infer a hidden archetype.

## 7. Cross-class rule

Cross-class overlap is permitted only when the same source wording independently performs distinct class jobs.

Do not manufacture overlap by:

- nominalizing an entire clause into OBJECT;
- duplicating a PLACE as OBJECT without separate referential work;
- turning every modifier into LABEL;
- turning every prepositional phrase into LOCATOR;
- turning every temporal word into TIME;
- splitting support grammar into VERB units.

But do not suppress a real second class merely because another class also uses nearby or identical wording.

## 8. Class-native grain

### PLACE

Admit each distinct physical scene/location coordinate established by the source and used to situate a represented actor, object, encounter, wait, conversation, recollection, departure/destination, present telling, or other represented episode.

This includes:

- broad settings;
- materially distinct contained settings;
- local scene positions;
- supported unnamed physical places when the source represents an event/encounter/location slot but does not name the place.

A PLACE does **not** need global reuse or narrative centrality. Do not merge distinct physical scene positions merely because they occur inside one broader setting.

Reject incidental surfaces, object parts, support positions, and path fragments that do not function as a represented physical scene/location coordinate.

### TIME

Admit each distinct episode/frame coordinate established by the source, including:

- event episodes;
- materially distinct contained phases;
- recurrence frames;
- reports/recollections;
- intended/future/hypothetical periods;
- present telling/reflection frames;
- supported unnamed time frames when a represented event or phase requires its own temporal slot although the source does not name one.

Explicit dates, durations, dayparts, and relative anchors qualify when they establish or distinguish a represented frame.

Do not create TIME from every adverb, tense marker, sequence token, state, or duration phrase that merely decorates an already represented frame. Do not collapse distinct represented event/phase frames merely because they occur in one larger episode.

### PERSON

Admit every represented human/social actor or stable actor group that participates in, is referred to by, is the destination of, or otherwise has an independent actor role in represented source structure.

Peripheral, local, prospective, reported, role-based, kinship-based, and one-use actors may qualify.

Resolve pronouns, aliases, kinship terms, roles, possessives, and group references before duplicate removal. Generic discourse `you` is not automatically a PERSON unless the source represents a distinct addressee/actor.

Reject purely grammatical person marking that does not establish a represented actor.

### OBJECT

Admit each concrete or abstract referent the source independently tracks as a node in represented structure: entities, documents, items, contents, choices, decisions, results, relations, values, topics, or other source-tracked referents.

Local and one-use referents may qualify. A concrete scene object may qualify even when not narratively central if the source tracks, locates, evaluates, acts on, compares, transfers, or otherwise relates it.

Do not create OBJECT from:

- a PLACE merely because it is a noun phrase;
- every grammatical argument with no independent referential work;
- a whole proposition or clause merely because it can be reified;
- analyst-created wrappers unless the source itself tracks that wrapper as a participant;
- isolated quantities/durations used only as modifiers;
- generic state/property wording whose job is LABEL.

### LABEL

Admit each smallest literal characterization atom by which the source explicitly classifies, characterizes, evaluates, compares, corrects, rejects, questions, or qualifies a represented coordinate or relation.

Preserve separate characterization/polarity atoms when the source separately presents them, even when several concern one broader subject.

Do not inventory every adjective, role word, intensifier, or descriptive phrase. A LABEL must independently perform a source characterization/classification job.

### VERB

Admit the minimal literal source predicate kernel for each distinct source-presented operative relation edge.

Preserve separate predicate units when the source separately presents actions, states, perceptions, thoughts, speech/report, intentions, selections, comparisons, movements, transfers, rejections, questions, or other operative relations, including local or intermediate relations, **when each has its own source relation job**.

A predicate is not rejected merely because a broader episode would remain understandable without it. Conversely, lexical distinctness alone does not create a relation edge.

Do not:

- fuse an entire clause into one VERB merely because the clause is semantically complete;
- inventory bare auxiliaries, copulas, raising/control scaffolding, or function words with no independent predicate job;
- split one phrasal predicate into meaningless fragments;
- duplicate the same relation edge merely because it is restated or coreferential;
- create a VERB from a modifier or nominal description that carries no predicate relation.

### LOCATOR

Admit each literal orienting span that independently locates or orients a represented coordinate/relation by:

- place or position;
- path, origin, destination, direction;
- containment or proximity;
- accompaniment/carrying;
- entry/exit;
- mental/relational orientation;
- materially spatialized figurative orientation.

The locator need not define a standalone physical place and need not be globally important. It must perform an independent source orienting job.

Do not inventory every prepositional phrase, recipient/topic argument, possession phrase, temporal phrase, or ordinary comparison merely because it contains orienting language.

## 9. Coreference, aliases, and source order

Resolve true aliases/coreferences before duplicate removal. Do not merge merely related entities, labels, episodes, relations, places, times, or orientations.

Order units by first source establishment after coreference, subject only to the apparatus’s admitted speaker-first PERSON and broad-before-contained PLACE/LOCATOR rules when established together.

Do not reorder to mimic an expected hidden output.

## 10. Compounds — binding reconstruction after unit freeze

Units are frozen before compounds.

Unit admission and compound admission are separate. A unit does not need to appear in a compound merely to remain valid, and a compound may not create or delete units.

A compound represents one source-presented operative binding among retained units when the source establishes a relation, classification, evaluation, comparison, correction/rejection, question, intention, report, orientation, or other research-relevant connection among those units.

For each such binding:

1. select the minimal retained relation/classification/orientation atom(s) that constitute the source binding;
2. include participating retained actor/entity/content units;
3. include retained PLACE/TIME/LOCATOR/LABEL anchors when the source binding uses them to situate or qualify the relation;
4. preserve source semantic order;
5. emit the complete source binding at its natural source grain.

Do not require a binding to be globally non-substitutable. Do not create a compound from mere co-occurrence, grammatical containment, or every possible subset. Do not fuse distinct source bindings into sentence-sized mega-compounds. Do not emit chains of support actions as one compound when the source presents separable operative bindings.

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

V39 is not certified merely because it is active.

Certification requires:

1. repeated Case 2 and Case 6 hidden-archetype passes under the same finalized V39 contract and same calibrated saved-agent lineage;
2. only then, one sealed Case 5 holdout attempt on that calibrated lineage;
3. if that holdout is archetypal, retire the calibrated lineage;
4. create a brand-new saved agent from the finalized V39 durable instructions only, with no prior sessions or holdout output;
5. run Case 5 once in a new session as clean-room verification;
6. certify only if that fresh agent succeeds.

If the sealed holdout has already been consumed for a lineage, automatic reuse is prohibited.

## 14. Historical effect

`AGENT_CONTRACT_V38.md` remains preserved as the controlling contract for its historical runs, including `34967452248`.

`AGENT_CONTRACT_V39.md` supersedes V38 **prospectively for new Researcher Inventory calibration and any later holdout/clean-room stage lawfully reached from that calibration lineage**.

Retained unchanged from V38: immutable archetype gates, literal lock, source-language preservation, posture preservation, coreference rules, hidden-evaluator isolation, candidate-only boundary, no-promotion rule, one-shot holdout protection, clean-room certification requirement, no APA-ID/database admission, and separation of harness defects from worker-behavior defects.

Superseded from V38: the whole-binding structural-sufficiency deletion gate as a prerequisite to whether source-grounded typed coordinates/atoms may be admitted.

V39 replaces that gate with positive class-native admission plus explicit exclusion/deduplication. A source-grounded unit is preserved when it independently performs its class job in represented source structure, even if deleting its enclosing binding would leave a coarser episode summary intact. This correction is general and does not encode hidden archetype rows, counts, evaluator findings, or case-specific expected answers.
