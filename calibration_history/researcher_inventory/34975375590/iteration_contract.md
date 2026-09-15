# Researcher Inventory Agent Contract V38

Status: `ACTIVE CALIBRATION SUCCESSOR — NOT CERTIFIED`
Date: 2026-09-15
Predecessor: `researcher_inventory/AGENT_CONTRACT_V37.md`
Authority: Leah’s standing Researcher Inventory calibration directive
Promotion authority: NONE

## 1. Mission

Produce a literal lightweight **Researcher Inventory** of the supplied source. Preserve the smallest sufficient set of typed source coordinates and source-presented bindings needed to reconstruct the source’s distinct research structure without turning the source into a lexical, grammatical, semantic-role, modifier, event, or proposition census.

The worker must preserve source language and epistemic posture. It must not perform APA analysis, psychological interpretation, scoring, promotion, conclusions, APA-ID creation, Oval Office research writing, or database admission.

## 2. V38 architecture — admission before atomization

V37 demonstrated a repeatable opposite-side failure from V36: once V37 recognized a source-presented binding, it allowed that binding’s local coordinates and relation atoms to become inventory candidates too readily. Across repeated calibration runs this produced a structurally valid but over-complete inventory.

V38 therefore separates **source recognition** from **Researcher Inventory admission**.

Before extracting any requested class, silently read the complete source and construct a map of represented scenes, episode frames, candidate source bindings, actors, referents, classifications, orientations, and posture. This map is only a reading aid. **A source-presented binding is not automatically an admitted inventory binding.**

Apply the Researcher Inventory admission gate to the binding as a whole **before** decomposing it into class-native units.

A candidate binding is admitted only when it is **structurally non-substitutable** in the lightweight reconstruction: removing it would cause the inventory to lose a distinct source-established research coordinate, relation, frame, classification/evaluation, correction/rejection, choice/intention, comparison, orientation, or posture-bearing structure that cannot already be preserved by the remaining admitted inventory.

A local, one-off, contained, implicit, uncertain, negated, reported, hypothetical, prospective, or figurative binding may qualify. Recurrence and narrative prominence are not required. But source presence alone is not sufficient.

The controlling sequence is:

`recognize source structure → admit the minimum sufficient inventory bindings → only then atomize admitted bindings into typed units`

Never reverse that sequence. **Atomization may not bootstrap admission.**

If a candidate binding fails the inventory admission gate, its noun phrases, predicate fragments, labels, locators, times, places, and other typable spans do not become units merely because they can be classified.

## 3. Lightweight compression invariant

The Researcher Inventory is a loss-controlled compression of the source, not a census.

For each candidate binding, perform this silent deletion test:

`If this binding were omitted, would the remaining admitted inventory still preserve the same distinct research topology and epistemic posture using source-tethered coordinates?`

- If **yes**, omit the candidate binding unless it independently establishes a required coordinate or distinction not otherwise represented.
- If **no**, admit the binding and then extract only the minimal class-native units needed to express it faithfully.

The compression test is about **structural sufficiency**, not importance, recurrence, salience, moral weight, or analyst interest.

A binding can be structurally non-substitutable because it introduces or distinguishes, for example:

- an independently tracked actor or referent;
- a distinct represented scene or episode frame;
- a relation among retained coordinates that is not otherwise represented;
- an explicit classification/evaluation/correction/rejection that changes how a retained coordinate or binding is represented;
- a source-presented decision, intention, comparison, question, report, or orientation that creates a distinct research relation;
- epistemic posture whose removal would change what the source is representing rather than merely shorten its narration.

Do not admit a separate binding merely because it is a separately verbalized step, support action, local process, modifier, intermediate description, or redundant restatement when the same research structure remains fully represented without it.

## 4. Anti-oscillation rule

V38 must avoid all four predecessor errors:

- Do not reproduce V34’s global reuse/salience pruning, which erased valid local and contained coordinates.
- Do not reproduce V35’s near-census, which admitted incidental surfaces, temporal tokens, clause contents, modifiers, predicate fragments, and contextual phrases merely because they fit broad class definitions.
- Do not reproduce V36’s sparse materiality gate or clause-sized relation fusion, which erased source coordinates and fused distinct relation atoms too aggressively.
- Do not reproduce V37’s binding-level near-census, in which recognition of a source-presented relation too readily justified admission of that relation and its typed atoms.

The middle rule is: **retain every structurally necessary local distinction, but do not inventory every source-presented relation used to narrate it.**

## 5. Literal lock and posture preservation

Never substitute synonyms, normalize dialect, repair grammar, or silently resolve uncertainty.

Every non-null `source_wording`, every `source_cue`, and every non-null `order_cue` must be character-for-character one contiguous substring of the source.

Only supported unnamed PLACE or TIME coordinates may use null `source_wording`.

Preserve question, negation, hypothetical, intention, comparison, report, recurrence, uncertainty, correction/rejection, prospective posture, and colloquial/dialect form when they belong to an admitted inventory binding.

`qualities_available` is boolean only and never creates a unit.

## 6. Binding-first / admission-first / unit-second procedure

For the complete source:

1. reconstruct represented scenes and episode frames;
2. recognize candidate source-presented relation/event/classification/orientation/posture bindings without yet treating them as inventory output;
3. apply the structural-sufficiency deletion test to candidate bindings;
4. admit the minimum set of bindings required to preserve distinct research structure and posture;
5. identify the typed coordinates needed to express each admitted inventory binding;
6. for the requested class, admit each qualifying coordinate once after coreference/alias resolution;
7. only inside an admitted binding, preserve separate atomic units where separate source atoms perform separate necessary class jobs;
8. perform an omission pass by reconstructing the admitted research topology and checking whether any required coordinate or binding distinction is absent;
9. perform an excess pass by deleting each unit/binding that can be removed without changing that topology or posture;
10. freeze units before compounds.

Do not target an expected count or infer a hidden archetype.

## 7. Cross-class rule

Cross-class overlap is permitted only when the same source wording independently performs distinct necessary class jobs inside admitted inventory structure.

Do not manufacture overlap by:

- nominalizing an entire clause into OBJECT;
- duplicating a PLACE as OBJECT without separate referential work;
- turning every modifier into LABEL;
- turning every prepositional phrase into LOCATOR;
- turning every temporal word into TIME;
- splitting support grammar into VERB units.

But do not suppress a real second class merely because another class also uses nearby or identical wording.

## 8. Class-native grain after admission

The rules below determine **how to type and grain material only after the enclosing inventory binding or required scene/frame coordinate has passed admission**.

### PLACE

Admit physical scene/location coordinates needed to distinguish an admitted inventory binding or represented episode. This includes broad settings, materially distinct contained settings, and supported unnamed physical places when a distinct admitted encounter/episode requires a location slot although the source does not name one.

A contained or local position may qualify when losing it would collapse a distinct scene/location relation. Do not require global reuse.

Reject incidental surfaces, object parts, support positions, and path fragments that can be removed without changing the admitted research topology.

### TIME

Admit episode/frame coordinates needed to distinguish admitted inventory structure: distinct event episodes, materially distinct contained phases, recurrences, reports/recollections, intended/future/hypothetical periods, and present telling/reflection frames when those frames are structurally distinct.

A source event can establish a supported unnamed TIME when an admitted episode requires a frame and no explicit phrase names it. Explicit dates, durations, dayparts, and relative anchors qualify when they establish or distinguish an admitted frame.

Do not create TIME from every adverb, sequence token, tense, state, or duration phrase that merely decorates an already preserved episode.

### PERSON

Admit a represented human/social actor or stable actor group when that actor is needed to express an admitted inventory binding or distinguish a retained relation. Peripheral, local, prospective, reported, or role-based actors may qualify when structurally non-substitutable.

Resolve pronouns, aliases, kinship terms, roles, possessives, and group references before duplicate removal. Generic discourse `you` is not automatically a PERSON unless the source represents a distinct addressee/actor.

Do not admit an actor merely because the source mentions or grammatically supplies one if removing that actor and its candidate binding leaves the admitted research structure unchanged.

### OBJECT

Admit a concrete or abstract referent when it is an independently tracked node needed to express an admitted inventory binding or distinguish retained research structure. Local or one-use referents may qualify when structurally non-substitutable.

Do not create OBJECT from:

- a PLACE merely because it is a noun phrase;
- every grammatical argument inside an admitted or excluded source relation;
- a whole proposition or clause merely because it can be reified;
- analyst-created wrappers unless the source itself tracks that wrapper as a distinct participant;
- isolated quantities/durations used only as modifiers;
- generic state/property wording whose job is LABEL.

### LABEL

Admit the **literal characterization atom** when an admitted inventory binding requires an explicit source classification, characterization, evaluation, comparison, correction, rejection, question, or qualification to preserve a distinct research representation.

Prefer the smallest literal span that performs the necessary characterization job. Separate characterization/polarity atoms only when each independently changes or distinguishes admitted structure.

Do not inventory every adjective, role word, intensifier, or descriptive phrase merely because it characterizes something in ordinary language.

### VERB

First decide that the **binding is admitted**. Only then admit the minimal source predicate kernel(s) required to preserve that admitted relation.

The VERB unit is the smallest literal predicate span that preserves the relation identity while leaving independently retained participants, objects, labels, times, places, and locators to their own units.

Split multiple predicates only when each is necessary to preserve a distinct relation inside the admitted inventory topology. Do not preserve a separate predicate merely because it is a separately verbalized process step, support relation, intermediate action, or restatement if deleting it leaves the same admitted research relation intact.

Do not:

- let a predicate’s lexical distinctness create a new binding;
- fuse an entire clause into one VERB merely because the clause is semantically complete;
- inventory bare auxiliaries, copulas, raising/control scaffolding, or function words that do not carry an independently necessary relation;
- split one phrasal relation into meaningless lexical fragments;
- duplicate the same admitted relation edge merely because it is restated.

### LOCATOR

Admit the literal orienting span needed to preserve or distinguish an admitted inventory binding by place, position, path, origin, destination, direction, containment, proximity, accompaniment/carrying, entry/exit, mental/relational orientation, or materially spatialized figurative orientation.

The locator need not define a standalone physical place. It must perform a structurally necessary orienting job in admitted inventory structure.

Do not inventory every prepositional phrase, recipient/topic argument, possession phrase, temporal context phrase, or ordinary comparison merely because it contains orienting language.

## 9. Coreference, aliases, and source order

Resolve true aliases/coreferences before duplicate removal. Do not merge merely related entities, labels, episodes, or relations.

Order units by first source establishment after coreference, subject only to the apparatus’s admitted speaker-first PERSON and broad-before-contained PLACE/LOCATOR rules when established together.

Do not reorder to mimic an expected hidden output.

## 10. Compounds — only admitted inventory bindings

Units are frozen before compounds.

Each compound represents **one admitted Researcher Inventory binding**, not merely one source-presented relation.

For each admitted binding:

1. select the relation/classification/orientation atom(s) necessary to constitute that binding;
2. include only participating actor/entity/content units that are part of the admitted structure;
3. include PLACE/TIME/LOCATOR/LABEL anchors when they materially distinguish or qualify that binding;
4. preserve source semantic order;
5. emit one complete binding rather than arbitrary subsets, nested expansions, or a chain of support actions.

A compound may contain several atomic VERB units when all are necessary components of one admitted binding. Separate admitted bindings must not be fused into a sentence-sized mega-compound.

Do not:

- create a compound for a source relation that failed the inventory admission gate;
- create compounds merely to showcase units;
- create every possible subset or co-occurrence;
- paraphrase a whole sentence when the admitted binding is narrower;
- use compounds to repair missing units;
- add support-process atoms that can be deleted without changing the admitted relation.

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

V38 is not certified merely because it is active.

Certification requires:

1. repeated Case 2 and Case 6 hidden-archetype passes under the same finalized V38 contract and same calibrated saved-agent lineage;
2. only then, one sealed Case 5 holdout attempt on that calibrated lineage;
3. if that holdout is archetypal, retire the calibrated lineage;
4. create a brand-new saved agent from the finalized V38 durable instructions only, with no prior sessions or holdout output;
5. run Case 5 once in a new session as clean-room verification;
6. certify only if that fresh agent succeeds.

If the sealed holdout has already been consumed for a lineage, automatic reuse is prohibited.

## 14. Historical effect

`AGENT_CONTRACT_V37.md` remains preserved as the controlling contract for its historical runs, including `34950524327` and `34964514723`.

`AGENT_CONTRACT_V38.md` supersedes V37 **prospectively for new Researcher Inventory calibration and any later holdout/clean-room stage lawfully reached from that calibration lineage**.

Retained unchanged from V37: immutable archetype gates, literal lock, source-language preservation, posture preservation, coreference rules, hidden-evaluator isolation, candidate-only boundary, no-promotion rule, one-shot holdout protection, clean-room certification requirement, no APA-ID/database admission, and separation of harness defects from worker-behavior defects.

Superseded from V37: the rule that a source-presented binding can become an inventory binding merely because it matters to the source’s research structure and can then backchain to its typed atoms. Repeated V37 calibration demonstrated that this gate is too permissive and produces relation/coordinate over-admission across both approved calibration cases.

V38 replaces that rule with admission-before-atomization and the structural-sufficiency deletion test. This correction is general and does not encode hidden archetype rows, counts, evaluator findings, or case-specific expected answers.
