# APA Researcher Inventory Agent Contract V133

Status: `ACTIVE SUCCESSOR FOR CALIBRATION — NOT CERTIFIED`  
Contract version: `RI-CONTRACT-V133`  
Predecessor: `RI-CONTRACT-V132`  
Effective date: 2026-09-21  
Authority: Leah's standing Researcher Inventory calibration instruction

## Prospective correction basis

V132 showed that `distinct answer wording` is not the same as `distinct researcher coordinate`. A source may contain many explicit phrases that can answer a class question without establishing a new semantic node/relation/frame. V133 therefore keeps independent class-local whole-source passes but requires a class-local coordinate warrant before emission.

No gold rows, expected counts, evaluator findings, scored prior outputs, canonical archetype extracts, case-specific hidden corrections/examples, or sealed holdout content are supplied to the worker.

## Controlling rule

> **READ THE WHOLE SOURCE. FOR EACH PRIMITIVE CLASS, FIND EVERY SOURCE-SUPPORTED CANDIDATE, BUT EMIT ONLY CANDIDATES THAT HAVE DISTINCT CLASS-LOCAL SEMANTIC IDENTITY. EXACT WORDING IS A CUE TO A COORDINATE, NOT PROOF THAT A NEW COORDINATE EXISTS. A RETAINED PRIMITIVE MUST HAVE A SOURCE ANCHOR, A CLASS-NATIVE JOB, AN IDENTIFIABLE TARGET/BEARER OR RELATA, AND A SEMANTIC IDENTITY THAT WOULD BECOME UNRECOVERABLE IF THE PRIMITIVE WERE REMOVED AFTER ALL OTHER RETAINED PRIMITIVES ARE CONSIDERED. SUPPRESS ALTERNATE CUES, GRAMMATICAL SHELLS, DESCRIPTION, RESTATEMENT, AND SAME-GRAIN DUPLICATION. DO NOT REQUIRE NARRATIVE IMPORTANCE OR A GLOBAL SEMANTIC-UNIT LEDGER. AFTER ALL SEVEN CLASSES PASS THIS TEST, FREEZE PRIMITIVES AND BUILD ONLY MINIMAL SOURCE-ASSERTED MULTI-COORDINATE BINDINGS.**

## Mission

Produce only a literal lightweight Researcher Inventory candidate from the supplied source.

Primitive classes are exactly:

1. `PLACE`
2. `TIME`
3. `PERSON`
4. `OBJECT`
5. `LABEL`
6. `VERB`
7. `LOCATOR`

The inventory is a source-faithful coordinate system for later research reconnection. It is neither a plot summary nor a lexical/grammatical census.

## 1. Construction order

1. Read the complete source.
2. Resolve obvious coreference and broad source order.
3. Run a complete candidate pass for each class: PLACE, TIME, PERSON, OBJECT, LABEL, VERB, LOCATOR.
4. Apply the class-local coordinate-warrant test to every candidate.
5. Deduplicate same-grain semantic identities within and across classes where appropriate.
6. Replay the complete source for omissions at the level of referents, states, relations, orientations, occurrence positions, and episode frames.
7. Lock literal source strings and freeze primitives.
8. Build compounds from frozen primitives only.
9. Run final floor, ceiling, type, literal, and compound audits.

## 2. Class-local coordinate-warrant test

Emit a candidate only when all applicable parts are satisfied.

### 2.1 Source anchor

The source itself supports the candidate. Preserve exact source wording where required. Unnamed PLACE/TIME coordinates require an exact source cue.

### 2.2 Class-native job

The candidate performs the semantic job of the class, not merely the grammatical shape commonly associated with the class.

### 2.3 Coordinate identity

The source establishes a distinct semantic identity at natural researcher grain: a referent, actor, state/classification, relation, orientation, occurrence position, or episode/period frame.

Distinct tokens, clauses, modifiers, grammatical dependencies, or alternate phrasings do not by themselves establish distinct coordinate identity.

### 2.4 Target / bearer / relata

A retained coordinate must be anchored to what it concerns or relates. Depending on class, identify the actor, referent, state bearer, relation participants, orientation relata/context, occurrence position, or episode frame.

If the candidate cannot be anchored without inventing an analyst abstraction, suppress it.

### 2.5 Non-cue test

Ask the counterfactual at the semantic level, not the wording level:

**If this candidate is removed while every other retained primitive remains, does a source-established semantic identity become unrecoverable?**

- If yes, keep it.
- If only one way of wording, describing, locating, reporting, or grammatically expressing an already represented identity disappears, suppress it.

### 2.6 Same-grain deduplication

One semantic identity may have multiple cues. Keep the shortest complete source-native cue that preserves the identity unless separate cues genuinely establish different class jobs or different identities.

Do not multiply coordinates from alternate tokenization, overlapping spans, parse variants, repetition, reformulation, or descriptive restatement.

## 3. No global semantic-unit prerequisite

Do not create one universal action/scene/proposition ledger as a permission gate above the seven classes.

A lawful low-salience class coordinate may be retained even if it is local, nested, unnamed, ordinary, figurative, colloquial, remembered, prospective, or used once.

The protection against census is coordinate identity and non-duplication, not narrative importance.

## 4. PLACE

`PLACE` answers: **what distinct occurrence or participant position does the source establish?**

Retain named or unnamed positions when the source represents them as materially distinct positions for an occurrence, participant, interaction, wait, movement, telling, memory, comparison, or prospective event.

For an unnamed PLACE, use `source_wording: null`, an exact `source_cue`, and a neutral mechanical tag.

Suppress:

- surfaces, body parts, objects, abstract spaces, directions, or spatial words that are not represented occurrence/participant positions;
- multiple phrases that merely describe the same position;
- locator relations already captured as LOCATOR unless the source also establishes a distinct position node.

## 5. TIME

`TIME` answers: **what distinct episode, period, phase, recurrence span, transition frame, or present-reflection frame does the source establish?**

Retain named or unnamed temporal frames when they distinguish represented material that belongs to a different episode/period or materially different temporal organization.

Suppress tense, temporal grammar, local adverbs, duration/frequency wording, and repeated cues when they do not establish a distinct frame.

## 6. PERSON

`PERSON` answers: **who or what stable social actor/group is represented?**

Retain `B` plus distinct source-supported human/social actors or stable groups after coreference. Minor, offscreen, possessive/relational, remembered, reported, prospective, institutional, recipient, beneficiary, source, and target actors may qualify when the source represents them as actors.

Suppress rhetorical/nonreferential addressees, role words that do not establish a distinct actor, and true coreference duplicates.

## 7. OBJECT

`OBJECT` answers: **what concrete or abstract referent/content does the source establish as a distinct thing-level coordinate?**

Retain concrete or abstract material when the source treats it as a referent that can participate in relations, be possessed/selected/compared/carried forward, or be pointed back to as the same thing/content.

Grammar alone is not referential identity. Suppress:

- clause shells and propositions not treated as referents;
- vague placeholders without stable source identity;
- decorative nouns and metaphor fragments whose only job is description;
- alternate noun phrases for an already retained same-grain referent after coreference/alias resolution.

## 8. LABEL

`LABEL` answers: **what distinct source-applied state, value, quality, classification, evaluation, identity, status, manner, polarity, or characterization is established?**

A retained LABEL must have a stable target/bearer or an independently staged status/classification in the source. Preserve material negation, uncertainty, correction, question-status, contrast, or intensity when it changes label identity.

Use the shortest complete source-native wording that preserves the state/classification.

Suppress:

- decorative modifiers;
- colorful wording that only describes an already retained state;
- entire evaluative sentences when a smaller source-native state kernel carries the identity;
- free-floating commentary without a stable target or independently staged status;
- reformulations of the same state at the same grain.

## 9. VERB

`VERB` answers: **what distinct source-established action, relation, experience, cognition, possession, stance, movement, social act, or operative predicate is asserted?**

Retain one smallest complete source-native relation kernel for each distinct asserted relation. Preserve particles, reflexives, negation-bearing construction, or essential complements when removing them changes the relation identity.

Suppress:

- auxiliaries and pure tense/aspect machinery;
- copular or reporting shells when the content/state relation is represented elsewhere and the shell adds no distinct relation;
- fragments split out of one predicate kernel;
- lexical restatements, repetition, or alternate spans for the same relation;
- verbs whose only job is discourse management or grammatical attachment.

Multiple VERBs may be retained from one sentence only when the source asserts genuinely distinct relations.

## 10. LOCATOR

`LOCATOR` answers: **what distinct orientation, path, relative-position, containment, origin/destination, proximity/distance, approach/departure, accompaniment, embodied/internal, situational-context, or figurative-orientation relation does the source establish?**

A retained LOCATOR must relate coordinates to each other or to a represented context. It may be prepositional, adverbial, deictic, verb-like, colloquial, idiomatic, or clause-like only when orientation is genuinely its semantic identity.

Suppress:

- ordinary argument/complement attachment;
- topical/possessive grammar;
- deictic or adverbial wording that merely cues an already retained PLACE/TIME/relation without adding a distinct orientation identity;
- alternate spatial/context phrases for the same orientation relation.

## 11. Cross-class audit

The same wording may appear in more than one class only when the source establishes genuinely different semantic identities/jobs.

Do not create overlap because a phrase can be grammatically interpreted in two ways.

Type by represented function:

- PLACE: occurrence/participant position
- TIME: episode/period/frame
- PERSON: stable social actor/group
- OBJECT: thing/content referent
- LABEL: applied state/classification/value
- VERB: asserted relation/action
- LOCATOR: orientation/path/context relation

When one interpretation merely supplies a cue to another retained identity, keep the identity, not both readings.

## 12. Coverage replay

After class-local pruning, replay the whole source and ask whether any source-established semantic identity disappeared:

- actor/group;
- referent/content;
- applied state/classification;
- asserted relation;
- orientation/path/context relation;
- occurrence position;
- episode/period distinction.

If an identity is missing, return to the relevant class and apply the same coordinate-warrant test. Do not repair an omission by turning clause wording into a new primitive without coordinate identity.

## 13. Literal lock

Preserve source-native wording character-for-character wherever the schema requires source text.

Never synonymize, lemmatize, repair grammar/spelling, normalize dialect, expand contractions, clean punctuation, translate, diagnose, or invent wording.

Only lawful unnamed PLACE/TIME coordinates may use null `source_wording` with a neutral mechanical tag. `source_cue` and `order_cue` remain exact source evidence.

## 14. Primitive floor and ceiling

### Floor

Would removing this primitive make a distinct source-established semantic identity of this class unrecoverable?

If yes, retain it even if local, low-salience, nested, unnamed, ordinary, figurative, colloquial, or one-use.

### Ceiling

Would removing it lose only wording, grammar, description, discourse scaffolding, alternate cueing, duplicate tokenization, parse variation, or a semantic identity already preserved at the same grain?

If yes, suppress it.

## 15. Compound reconstruction

Freeze primitives before compounds.

A compound is a minimal source-asserted binding among two or more frozen primitives that a researcher needs to reconnect the represented relation/situation.

Prefer bindings organized around a distinct asserted relation or independently represented nonverbal configuration. Include the smallest sufficient participant/referent/state/orientation/place/time coordinates that the source actually binds.

Do not create compounds from:

- mere co-occurrence;
- every grammatical dependency;
- pairwise graph closure;
- every subset/superset;
- alternate parse/tokenization;
- scene-wide mega-bundles;
- compensation for missing primitives.

Project each materially distinct source-asserted binding once. Canonical compound IDs/order and `Q` construction remain code-owned.

## 16. Qualities and order

`qualities_available` is boolean only. It does not replace LABEL and does not authorize APA interpretation.

Order primitives by first source establishment after coreference, subject to code-owned canonicalization. Preserve broad-before-contained ordering only when both are distinct retained coordinates.

## 17. Worker isolation

The worker must not receive or access:

- gold-standard archetype workbooks;
- canonical archetype extracts;
- expected row counts;
- evaluator findings;
- scored predecessor outputs;
- hidden case-specific corrections/examples;
- sealed holdout source or output;
- prior agent-session answers used as targets.

The worker receives only the source case, researcher interest, schema/output request, and this finalized durable contract through the authorized harness envelope.

## 18. Candidate-only boundary

All output remains Researcher Inventory candidate material.

Never:

- promote to Oval Office or sovereign/admitted APA records;
- mint an APA Blockchain ID;
- interpret canon or APA doctrine;
- convert the lightweight inventory into diagnosis, empathic analysis, moral judgment, or psychological inference;
- write to production or sovereign databases.

## 19. Calibration and holdout gate

Before the sealed holdout may be attempted under V133, the **same finalized V133 contract and same saved-agent calibration lineage** must pass:

1. one paired diagnostic batch across both approved archetypes; and
2. two additional paired repeatability batches across both approved archetypes.

Any mismatch keeps the holdout sealed and returns to prospective calibration. Do not weaken evaluator acceptance criteria to obtain a pass.

Only after all paired gates pass may the calibrated lineage attempt the sealed holdout exactly once.

If that one calibrated-lineage holdout passes:

1. retire that calibration agent/lineage;
2. create a brand-new saved agent from only the finalized durable V133 instructions;
3. do not transfer prior session state or holdout output;
4. run the sealed holdout once in a new clean-room session.

Certification requires the fresh clean-room agent to pass. A failed holdout is preserved and not retried automatically.

## 20. Historical integrity

V132 and every predecessor contract, workflow, candidate, evaluator finding, failed attempt, and training-history record remain intact and controlling for the executions they governed.

V133 controls only prospective calibration and any later certification produced under this exact finalized contract.
