# Researcher Inventory Agent Contract V37

Status: `ACTIVE CALIBRATION SUCCESSOR — NOT CERTIFIED`
Date: 2026-09-15
Predecessor: `researcher_inventory/AGENT_CONTRACT_V36.md`
Authority: Leah’s standing Researcher Inventory calibration directive
Promotion authority: NONE

## 1. Mission

Produce a literal lightweight **Researcher Inventory** of the supplied source. Preserve enough typed source coordinates and source-presented bindings to reconstruct the research-relevant structure of the source without turning the source into a lexical, grammatical, semantic-role, modifier, or proposition census.

The worker must preserve source language and epistemic posture. It must not perform APA analysis, psychological interpretation, scoring, promotion, conclusions, APA-ID creation, Oval Office research writing, or database admission.

## 2. V37 architecture — source-binding backchaining

V36 demonstrated that a sparse event-map / material-coordinate-necessity gate can under-admit real source coordinates and fuse relation grain too aggressively. V37 replaces that admission architecture prospectively.

Before extracting any requested class, silently read the complete source and construct a **source-binding map**. A source binding is one source-presented relation, event, classification, correction/rejection move, comparison, orientation, report, question, intention, recurrence, hypothetical/prospective frame, or other represented binding that matters to the source’s research structure.

Do not make a binding merely because a clause exists. Do not omit a binding merely because it is local, one-off, peripheral, implicit in scene/time, uncertain, negated, reported, hypothetical, prospective, figurative, or contained.

For each admitted source binding, backchain to the **minimal typed source coordinates needed to express that binding faithfully**. A unit is admitted when it performs the requested class job as an independently tracked coordinate in at least one admitted source binding, or when it is a supported unnamed PLACE/TIME coordinate needed to situate a distinct represented scene or episode.

The controlling question is:

`Is this a source-grounded typed coordinate required to preserve a source-presented binding at the class-native grain?`

Not:

- `is this narratively important?`
- `will this recur?`
- `can this phrase be classified somehow?`
- `is this a separate grammatical constituent?`

## 3. Anti-oscillation rule

V37 must avoid all three predecessor errors:

- Do not reproduce V34’s global reuse/salience pruning, which erased valid local and contained coordinates.
- Do not reproduce V35’s near-census, which admitted incidental surfaces, temporal tokens, clause contents, modifiers, predicate fragments, and contextual phrases merely because they fit broad class definitions.
- Do not reproduce V36’s sparse materiality gate or clause-sized relation fusion, which erased source-binding atoms needed to reconstruct the archetypal relation structure.

A local atomic unit may qualify if an admitted source binding needs it. A lexically available phrase does not qualify merely because it can be typed.

## 4. Literal lock and posture preservation

Never substitute synonyms, normalize dialect, repair grammar, or silently resolve uncertainty.

Every non-null `source_wording`, every `source_cue`, and every non-null `order_cue` must be character-for-character one contiguous substring of the source.

Only supported unnamed PLACE or TIME coordinates may use null `source_wording`.

Preserve question, negation, hypothetical, intention, comparison, report, recurrence, uncertainty, correction/rejection, prospective posture, and colloquial/dialect form.

`qualities_available` is boolean only and never creates a unit.

## 5. Binding-first / unit-second procedure

For the complete source:

1. identify represented scenes and episode frames;
2. identify source-presented relation/event/classification/orientation bindings inside those frames;
3. identify the typed coordinates needed to express each admitted binding;
4. for the requested class, admit each qualifying coordinate once after coreference/alias resolution;
5. preserve atomic grain where separate source atoms perform separate jobs in bindings;
6. perform an omission pass by replaying the bindings and asking whether any required coordinate is absent;
7. perform an excess pass and remove material that has no independent class job in any admitted binding and no required unnamed PLACE/TIME scene role;
8. freeze units before compounds.

Do not target an expected count or infer a hidden archetype.

## 6. Cross-class rule

Cross-class overlap is permitted only when the same source wording independently performs distinct class jobs in source bindings.

Do not manufacture overlap by:

- nominalizing an entire clause into OBJECT;
- duplicating a PLACE as OBJECT without separate referential work;
- turning every modifier into LABEL;
- turning every prepositional phrase into LOCATOR;
- turning every temporal word into TIME;
- splitting support grammar into VERB units.

But do not suppress a real second class merely because another class also uses nearby or identical wording.

## 7. Class-native grain

### PLACE

Admit physical scene/location coordinates used by represented bindings. This includes broad settings, materially distinct contained settings, and **supported unnamed physical places** for separately represented encounters, waits, conversations, recollections, departures/destinations, or present telling scenes when the distinct binding requires a location slot even though the source does not name the place.

A contained or local position may qualify when a binding uses it as a scene/location coordinate. Do not require global reuse.

Reject incidental surfaces, object parts, support positions, and path fragments that do not function as a scene/location coordinate in any admitted binding.

### TIME

Admit episode/frame coordinates used by represented bindings: event episodes, materially distinct contained phases, recurrences, reports/recollections, intended/future/hypothetical periods, and present telling/reflection frames.

A source event can establish a supported unnamed TIME even when no explicit temporal phrase names it. Explicit dates, durations, dayparts, and relative anchors qualify when they establish or distinguish an admitted episode/frame.

Do not create TIME from every adverb, sequence token, tense, state, or duration phrase that merely decorates an already represented episode.

### PERSON

Admit every represented human/social actor or stable actor group that participates in an admitted source binding, including peripheral actors introduced through kinship, role, possession, report, destination, or prospective interaction.

Resolve pronouns, aliases, kinship terms, roles, possessives, and group references before duplicate removal. Generic discourse `you` is not automatically a PERSON unless the source represents a distinct addressee/actor.

### OBJECT

Admit concrete or abstract referents that participate as independently tracked nodes in admitted source bindings: entities, documents, items, contents, choices, decisions, results, relations, values, topics, or other source-tracked referents.

A local or one-use object may qualify. A concrete scene object may qualify even when it is not narratively central if a source binding tracks or locates it.

Do not create OBJECT from:

- a PLACE merely because it is a noun phrase;
- a whole proposition or clause merely because it can be reified;
- analyst-created wrappers such as `my point` or `what happened` unless the source itself tracks that wrapper as a distinct participant;
- isolated quantities/durations used only as modifiers;
- generic state/property wording whose job is LABEL.

### LABEL

Admit the **literal characterization atom** when the source explicitly classifies, characterizes, evaluates, compares, corrects, rejects, questions, or qualifies a retained coordinate or binding.

Preserve separate explicit characterization/polarity moves separately when the source separately presents them. Prefer the smallest literal span that performs the characterization job; do not fuse neighboring relation content into the label merely for readability.

Do not inventory every adjective, role word, intensifier, or descriptive phrase unless it independently performs a source classification/characterization job in an admitted binding.

### VERB

Admit the **minimal source predicate kernel** for each admitted relation edge.

The VERB unit is the smallest literal predicate span that preserves the relation identity while leaving participants, objects, labels, times, places, and locators to their own units when those coordinates are independently retained.

Split multiple relations in one clause when each relation independently participates in the source-binding structure. Preserve phrasal or multiword predicate material together only when splitting it would destroy the predicate’s source meaning or reduce it to support grammar.

Do not:

- fuse an entire clause into one VERB merely because the clause is semantically complete;
- inventory bare auxiliaries, copulas, raising/control scaffolding, or function words that do not carry an independent relation;
- split one phrasal relation into meaningless lexical fragments;
- duplicate the same relation edge merely because it is restated.

Speech, thought, perception, intention, report, stance, movement, possession, state-change, comparison, selection, rejection, and question-answer relations may qualify when source-presented as distinct edges.

### LOCATOR

Admit the literal orienting span that materially locates or orients a retained coordinate in an admitted binding by place, position, path, origin, destination, direction, containment, proximity, accompaniment/carrying, entry/exit, mental/relational orientation, or materially spatialized figurative orientation.

The locator need not define a standalone physical place. It must perform an orienting relation in a source binding.

Do not inventory every prepositional phrase, recipient/topic argument, possession phrase, temporal context phrase, or ordinary comparison merely because it contains orienting language.

## 8. Coreference, aliases, and source order

Resolve true aliases/coreferences before duplicate removal. Do not merge merely related entities, labels, episodes, or relations.

Order units by first source establishment after coreference, subject only to the apparatus’s admitted speaker-first PERSON and broad-before-contained PLACE/LOCATOR rules when established together.

Do not reorder to mimic an expected hidden output.

## 9. Compounds — replay the source-binding map

Units are frozen before compounds.

Each compound represents **one admitted source binding** using the final units that participate in that binding.

For each binding:

1. select the relation/classification/orientation atom(s) that constitute that binding;
2. include the participating actor/entity/content units;
3. include PLACE/TIME/LOCATOR/LABEL anchors when they materially situate or qualify that binding in the source;
4. preserve source semantic order;
5. emit one complete binding rather than arbitrary subsets or nested expansions.

A compound may contain several atomic VERB units when the source presents them as one binding and separating them would lose the binding structure. Conversely, separate source bindings should not be fused into a sentence-sized mega-compound.

Do not:

- create compounds merely to showcase units;
- create every possible subset or co-occurrence;
- paraphrase a whole sentence when the source binding is narrower;
- use compounds to repair missing units;
- omit a material scene/time/orientation anchor solely to minimize tuple size.

## 10. Isolation boundary

The calibration worker must not receive:

- Case 2 or Case 6 gold workbook rows or canonical extracts;
- expected counts;
- evaluator findings;
- scored prior outputs;
- case-specific gold corrections/examples;
- sealed Case 5 source during calibration;
- any Case 5 holdout output.

A hidden evaluator may compare worker output after execution. That comparison never becomes worker-visible training text.

## 11. Archetype verification and history

Before calibration uses Case 2 or Case 6, repository workbook copies must pass the immutable SHA-256 gates defined by Leah. If a copy is wrong, the apparatus may reconstruct it only from an already authorized canonical package whose reconstructed digest exactly matches the approved hash.

Every attempted calibration, failure, partial result, and successor remains durable history. Do not delete failed predecessor runs.

Harness defects and worker-behavior defects must be recorded separately. A harness correction alone does not justify semantic contract revision.

## 12. Certification gate

V37 is not certified merely because it is active.

Certification requires:

1. repeated Case 2 and Case 6 hidden-archetype passes under the same finalized V37 contract and same calibrated saved-agent lineage;
2. only then, one sealed Case 5 holdout attempt on that calibrated lineage;
3. if that holdout is archetypal, retire the calibrated lineage;
4. create a brand-new saved agent from the finalized V37 durable instructions only, with no prior sessions or holdout output;
5. run Case 5 once in a new session as clean-room verification;
6. certify only if that fresh agent succeeds.

If the sealed holdout has already been consumed for a lineage, automatic reuse is prohibited.

## 13. Historical effect

`AGENT_CONTRACT_V36.md` remains preserved as the controlling contract for its historical runs, including workflow run `34946782917`.

`AGENT_CONTRACT_V37.md` supersedes V36 **prospectively for new Researcher Inventory calibration and any later holdout/clean-room stage lawfully reached from that calibration lineage**.

V36’s immutable archetype gates, literal lock, hidden-evaluator isolation, candidate-only boundary, no-promotion rule, one-shot holdout protection, clean-room certification requirement, and separation of harness defects from worker-behavior defects are retained.

V36’s sparse event-map / material-coordinate-necessity admission architecture, clause-sized `semantically complete relation edge` VERB grain, and overly minimal compound rule are superseded because run `34946782917` demonstrated cross-case under-admission and over-fusion.

No hidden archetype content, evaluator finding, or case-specific correction is adopted into worker-visible V37 semantics.