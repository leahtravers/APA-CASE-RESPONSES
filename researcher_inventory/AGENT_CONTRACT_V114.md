# APA Researcher Inventory Agent Contract V114

Status: `ACTIVE SUCCESSOR FOR CALIBRATION — NOT CERTIFIED`
Contract version: `RI-CONTRACT-V114`
Predecessor: `RI-CONTRACT-V113`
Effective date: 2026-09-20
Authority: Leah's standing Researcher Inventory calibration instruction.
Registrar record: `APA-EXEC-2026-09-20-CASES-RI-V114-CAL-0001`

## Prospective correction basis

V113 workflow run `35500850586` verified both Leah-approved immutable archetype workbooks against their required SHA-256 values without repair and passed all deterministic apparatus/harness tests, then failed hidden semantic comparison on both approved archetype cases. The complete failed attempt remains preserved append-only under `calibration_history/researcher_inventory/35500850586-A1/`. The sealed holdout was not reached.

The failure is worker-semantic. V113 correctly rejected a pure token/grammar census, but its "representation-bearing coordinate" threshold was interpreted too narrowly. The worker repeatedly removed ordinary represented things, one-use participants and predicates, implicit scene/episode supports, low-salience states/orientations, and other source-established content merely because those coordinates were not sufficiently stable, important, or independently emphasized. It also continued to mistype some spans by surface form and built compounds from the wrong primitive ledger.

V114 replaces that over-restrictive threshold with a simpler distinction: **represented denotata, represented relations, represented support, and represented orientations belong in the inventory; grammatical/discourse carriage does not.** A valid coordinate does not need to be salient, recurring, central, later reused, or narratively emphasized.

No archetype rows, hidden counts, evaluator findings, prior scored outputs, calibration answers, or sealed holdout material are supplied to the worker.

## Mission

Read the complete source and recover a **lightweight, source-faithful researcher inventory** in exactly seven classes:

1. `PLACE`
2. `TIME`
3. `PERSON`
4. `OBJECT`
5. `LABEL`
6. `VERB`
7. `LOCATOR`

`Lightweight` means the inventory stores each distinct represented coordinate once per class rather than reproducing grammar, tokenization, or every repeated mention. It does **not** mean high-salience-only, theme-only, or aggressively pruned.

Do not perform APA scoring, psychological interpretation, promotion, APA-ID creation, executive analysis, sovereign/admitted writing, or APA Data Fabric/database mutation.

## 1. Whole-source map before extraction

Read the whole source before extracting any class. Silently segment what is represented into differentiated scenes, episodes, periods, interactions, memories, reports, questions, intentions, alternatives, recurring situations, prospective situations, and present reflection/telling.

Within that map identify:

- human/social participants;
- concrete and abstract things/content handles;
- characterizations, states, identities, evaluations, comparisons, corrections, and candidate labels;
- lexical events, actions, states, communications, cognitions, intentions, gestures, movements, and relations;
- spatial and temporal support;
- orientations such as position, path, direction, containment, accompaniment, context, origin/destination, recurrence, internal position, or figurative relation.

The map is not itself the inventory. It is a coverage device so secondary or low-salience represented material is not lost.

Then perform seven class passes. Judge each class on its own terms. Cross-class overlap is allowed when one source span genuinely performs more than one represented function.

## 2. Primitive admission: three gates

Admit a primitive when all three gates pass.

### Gate A — source grounding

The source establishes the candidate in the requested class.

For explicit coordinates, use the smallest complete exact contiguous source span that preserves the class-native identity.

For a legitimate unnamed `PLACE` or `TIME`, `source_wording` may be null when the source clearly establishes the occurrence/interaction/episode but does not name the support. Use an exact source cue and a neutral mechanical tag. Never invent substantive content.

### Gate B — represented class-native function

Ask:

**Does this candidate denote or perform a distinct represented job in this class, rather than merely serving grammar or discourse?**

If yes, retain it even when it is:

- one-use;
- mundane;
- background;
- low-salience;
- locally relevant;
- remembered or reported;
- uncertain or questioned;
- negated;
- prospective or hypothetical;
- figurative or colloquial;
- implicit spatial/temporal support.

Do not require recurrence, thematic importance, later reuse, causal importance, emotional importance, narrative emphasis, or an independently "stable" role.

Reject only candidates whose class claim comes from linguistic carriage without a distinct represented class-native job, such as:

- determiners/articles;
- inflection-only material;
- auxiliaries and tense/aspect machinery that add no separate represented predicate;
- conjunctions and generic connectives;
- discourse fillers or narration scaffolding with no represented relation;
- generic/nonreferential pronouns after coreference is resolved;
- duplicate mentions of the same class-native coordinate;
- fragments that are merely pieces of a larger natural coordinate and do not themselves perform the class job.

### Gate C — class-local distinctness

Within the same class, merge true aliases, coreference, inflection-only realizations of the same relation, and genuine restatements of the same coordinate.

Do not merge different represented coordinates merely because they are related, physically colocated, occur in the same sentence, or can be reconstructed from each other.

Never use another class or a future compound as a reason to remove an otherwise valid class-native coordinate.

## 3. Coverage principle: represented content is not scene color merely because it is ordinary

A concrete thing, minor participant, single gesture, ordinary relation, small state, or local orientation is not automatically "incidental scene color." If the source represents it as a distinct denotatum/relation/state/orientation in the situation, retain it.

The inventory is comprehensive over represented class-native coordinates but deduplicated over repeated wording and grammatical carriage.

The key contrast is:

- **represented coordinate** -> retain;
- **language needed only to phrase another coordinate** -> do not separately retain.

## 4. Functional typing over surface grammar

Type by what the span is doing in the represented situation, not by part of speech or visual phrase shape.

- represented human/social participant -> `PERSON`
- represented thing/content/referential handle -> `OBJECT`
- represented characterization/state/identity/evaluation/comparison/candidate label/correction -> `LABEL`
- represented spatial scene/location support -> `PLACE`
- represented episode/period/phase support -> `TIME`
- represented lexical event/state/action/relation -> `VERB`
- represented orientation/path/position/context relation -> `LOCATOR`

A spatial-looking phrase can be `OBJECT` when it is represented as content/thinghood. A noun phrase can be `LABEL` when it characterizes. An adverbial or comparative phrase can be `LABEL` when its job is characterization, or `LOCATOR` when its job is orientation. Named physical things are not automatically `PLACE`; a `PLACE` supports a represented scene/location.

When one exact source span genuinely performs multiple class-native jobs, retain the projection in each applicable class rather than forcing one class to absorb the others.

## 5. PLACE — represented scene/location support

Retain every distinct spatial support coordinate established by the represented source situation.

Include, when distinct in the source:

- broad scene locations;
- contained/local scene locations;
- locations of represented objects when that object-location relation is itself represented;
- destinations or places another participant goes;
- waiting positions/places;
- locations of later interactions or remembered conversations;
- locations of recurring or prospective situations;
- the present telling/reflection setting when represented as a distinct scene support.

A place does not need an explicit place name. If the source establishes a differentiated occurrence or interaction but leaves its place unnamed, an unnamed support coordinate may be retained with null `source_wording`, exact `source_cue`, and a neutral mechanical tag.

Do not create a separate PLACE for every noun that happens to be physical. Retain physical things as OBJECT when their represented function is thinghood rather than scene support.

## 6. TIME — represented episode/period/phase support

Retain every distinct episode, phase, period, temporal frame, or prospective/recurring time support established by the represented source situation.

After whole-source segmentation, perform **episode-support closure**: for each differentiated represented episode/phase, ask whether it has its own temporal support coordinate. If yes, retain one TIME even when no explicit temporal words name it.

Distinct TIME coordinates may include:

- an attempt or condition episode;
- a response/help episode;
- a transition/departure episode;
- a waiting episode;
- an intended period;
- a later report/conversation;
- a recurring span;
- a remembered phase;
- a broader relational period;
- a prospective/future situation;
- a present telling/reflection episode.

Do not split every single action into its own TIME when several actions clearly share one represented episode. Do not inventory tense/aspect tokens or temporal grammar as separate TIME coordinates.

## 7. PERSON — represented participants

Retain the speaker and every distinct source-established human/social participant or stable group after true coreference.

Participation can be:

- direct/on-scene;
- offscreen but acted toward, sought, reported, or discussed;
- remembered;
- institutional;
- relational;
- possessive/beneficiary when that person/group is part of a represented material relation;
- prospective.

A participant can appear once and still qualify.

Reject only generic/rhetorical/nonreferential people who never become represented participants.

## 8. OBJECT — represented thing/content handles

Retain every distinct source-established thing/content handle that the represented situation treats as something one could point to, act on, possess, exchange, inspect, compare, question, remember, report, value, decide about, contemplate, locate, or otherwise relate to.

OBJECT can be:

- concrete physical things;
- documents/items/products;
- body/environmental things;
- abstract content;
- decisions/choices;
- sets/categories;
- internal content;
- relational content;
- values/amounts;
- figurative things;
- proposition-like content when the source reifies it as something thought/talked/acted about.

Do not suppress an ordinary concrete noun merely because it is background or appears once if the source represents that thing distinctly.

Reject generic pronouns/deixis after coreference, arbitrary grammatical nominalizations, and clause fragments that are not represented as a distinct content handle.

If the span's primary represented job is a characterization/state/evaluation/comparison rather than thinghood/content, type it `LABEL` instead. Cross-class overlap is allowed only when the source truly supports both jobs.

## 9. LABEL — represented characterizations and states

Retain every distinct source-native characterization, state, identity, evaluation, comparison, correction, acceptance/rejection, polarity, manner, candidate label, question label, or represented posture applied to a person, thing, relation, or situation.

Qualifying LABEL coordinates can be:

- one word;
- a phrase;
- colloquial or idiomatic;
- figurative;
- uncertain/questioned;
- negated;
- corrected/rejected;
- low-salience or one-use.

A candidate label and its immediate rejection/correction may each be separately represented coordinates when the source presents them distinctly.

Do not inventory pure intensifiers or modifiers that only decorate another phrase and do not themselves establish a represented characterization/state.

## 10. VERB — meaningful represented lexical predicates

Retain every distinct contentful lexical predicate that expresses a represented event, action, state, relation, movement, possession, perception, communication/report, cognition, intention, question, decision, comparison, evaluation, transition, gesture, or other represented predication.

**Do not require the predicate to materially change the broader story.** One-use, mundane, gestural, low-salience, or background predicates qualify when they are represented.

Use the smallest complete lexical predicate construction that preserves relation identity. Preserve a required particle, reflexive, negation, modal, or bound complement when necessary for the relation itself. Do not swallow separately typed participants, objects, labels, places, times, or locators merely to make the phrase sound like a sentence.

Split matrix/embedded or coordinated predicates when they express different represented relations.

Exclude:

- auxiliaries that only carry tense/aspect/modality and have no separate lexical relation;
- tense/aspect machinery;
- pure copular grammar when all represented content is already the label/state and the copula adds no separate relation identity;
- discourse organizers/fillers with no represented predicate;
- genuine same-relation restatements after class-local deduplication.

Narration/reporting predicates are not automatically excluded. If the source represents a saying, telling, recalling, asking, explaining, reporting, or thinking relation, it is a represented VERB coordinate.

## 11. LOCATOR — represented orientation coordinates

Retain each smallest complete exact source span that orients represented material by:

- position;
- containment;
- path;
- direction;
- origin/destination;
- proximity;
- accompaniment;
- recurrence/context;
- procedure/relation;
- internal/mental position;
- temporal position when it functions as orientation rather than the episode support itself;
- figurative/comparative orientation.

LOCATOR is relational orientation, not simply "a prepositional phrase." A direction/purpose phrase can qualify when it actually orients an action or participant in the represented situation.

Do not inventory bare prepositions, generic argument markers, degree phrases, conjunctions, or adverbials that have no distinct represented orientation.

A phrase may also appear as LABEL when it separately characterizes, or as PLACE/TIME when it supplies support. Cross-class overlap is permitted when those jobs are all genuinely represented.

## 12. Atomic span and literal lock

For every explicit primitive use the smallest complete exact contiguous source-native span that preserves the coordinate's class-native identity.

Preserve source posture exactly when semantically required, including:

- particles/prepositions;
- reflexives;
- bound complements;
- negation;
- modality;
- uncertainty;
- questions;
- attribution;
- comparison;
- idiom/dialect;
- hypothetical/prospective/reported/corrective posture.

Never normalize, improve, translate, diagnose, euphemize, paraphrase, lemmatize into a different surface form, or substitute synonyms.

Every non-null `source_wording`, `source_cue`, and `order_cue` must be character-for-character source text. Neutral mechanical tags are allowed only for legitimate unnamed PLACE/TIME support and ordinary apparatus identity descriptions where the schema permits them.

## 13. Freeze audit

Before compounds, audit each class in five directions.

### A. Scene/episode coverage

Walk every differentiated represented scene/episode in source order and ask whether it establishes any class-native coordinate that has been omitted. Explicitly perform PLACE/TIME support closure.

### B. Low-salience coverage

Check ordinary concrete things, one-use participants, single gestures/actions, minor states/labels, local orientations, and background relations. Do not remove them merely for being mundane.

### C. Grammar/discourse pruning

Remove only grammar/discourse carriage that lacks a distinct represented class-native job, plus true same-class duplicates.

### D. Functional type audit

For every retained span ask what represented job it performs. Correct surface-form typing errors. If it genuinely performs multiple jobs, keep the appropriate cross-class projections.

### E. Literal-lock audit

Ensure exact source wording/posture and atomic resolution.

Repeat coverage after corrections. Freeze only when both omission and over-admission checks are stable.

## 14. Ordering and identity

Primitive identity follows class-local represented identity, not mention count. Merge true aliases/coreference and same-class repeated mentions. Keep genuinely different coordinates even if related or colocated.

Code owns canonical IDs. The worker supplies neutral identity keys only for merge. Order by first source establishment after coreference, subject to apparatus speaker-first PERSON and genuine broad-before-contained support rules. Do not order by importance or real-world chronology.

## 15. Proposition/relation-instance compounds

Only after all seven primitive ledgers are frozen, reread the source in represented proposition/relation units.

For each represented proposition/relation instance that contributes source structure, emit the **smallest complete compound** linking the frozen coordinates that actually participate in that instance.

Use a retained VERB relation as the backbone when one carries the proposition. Include participant, object/content, label/state, PLACE/TIME support, and LOCATOR refs only when they actually participate in that exact relation instance.

A represented label/state/question proposition may form a non-VERB compound when its structure is not already carried by another retained relation.

Do not create compounds merely because entries occur in the same sentence, paragraph, scene, or episode. Do not emit:

- graph closure;
- arbitrary all-pairs links;
- scene mega-bundles;
- singleton equivalents;
- subset/superset permutations of one proposition;
- duplicate restatements;
- compounds containing rejected primitives;
- generic closure around every question or label without a represented proposition.

Compounds never substitute for missing primitives and never justify pruning a valid primitive.

## 16. Completion standard

The inventory is complete when:

- the whole source was read and segmented;
- every represented class-native denotatum/relation/state/orientation/support coordinate has been considered, including low-salience and one-use material;
- implicit but source-established PLACE/TIME support is covered without invention;
- grammar/discourse carriage is not separately inventoried;
- seven-class functional typing is correct;
- cross-class overlap is preserved when genuinely functional;
- exact lexical/postural source fidelity is preserved;
- primitives are frozen before compounds;
- compounds encode smallest represented proposition/relation instances rather than graph closure.

Never target hidden counts or infer hidden gold.

## 17. Isolation and certification gates

Approved archetypes, gold rows, hidden counts, evaluator findings, prior scored outputs, calibration answers, and sealed holdout material are forbidden worker context.

The worker sees only:

- this finalized durable contract;
- the bounded source/request supplied for the current extraction operation;
- the response schema and neutral apparatus task rules required to produce that operation's answer.

Calibration/evaluator code may compare the worker output afterward. Evaluator findings never become retroactive worker context for the same attempt.

Sealed Case 5 must not be opened by the calibration worker and must not appear in examples or tuning material.

Case 5 may be attempted only after one paired diagnostic batch and two paired repeatability batches for Case 2 + Case 6 all pass under this exact finalized V114 contract and the same saved-agent lineage.

If the calibrated lineage passes Case 5 exactly once, retire that saved agent. Create a brand-new saved agent from only this finalized durable contract, with no prior agent sessions or holdout output, then run Case 5 in a new session exactly once for clean-room verification.

Certification requires that fresh agent to pass. Until then the contract is `NOT CERTIFIED`.

## 18. Candidate-only boundary

All outputs remain research/calibration candidates. Do not promote to admitted APA records, Oval Office research records, sovereign fabric, canon, or mathematics. Do not mint APA IDs. Do not write APA databases.

## 19. Historical integrity

V113 and all earlier contracts/runs remain preserved as historical authority for work actually executed under them. V114 controls only new Researcher Inventory calibration/execution routed to V114 after its creation.

Never delete failed attempts, predecessor contracts, training history, or evaluation evidence.
