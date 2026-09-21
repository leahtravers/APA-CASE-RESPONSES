# APA Researcher Inventory Agent Contract V134

Status: `ACTIVE SUCCESSOR FOR CALIBRATION — NOT CERTIFIED`  
Contract version: `RI-CONTRACT-V134`  
Predecessor: `RI-CONTRACT-V133`  
Effective date: 2026-09-21  
Authority: Leah's standing Researcher Inventory calibration instruction

## Prospective correction basis

V133 demonstrated that source-faithful semantic pruning can still become too aggressive when one primitive class is allowed to substitute for another, when related referents are over-merged, when relation kernels absorb arguments/complements, or when co-located/overlapping occurrence anchors are collapsed. V134 keeps the semantic floor and ceiling but treats the seven primitive classes as orthogonal researcher lenses at source-native grain.

No gold rows, expected counts, evaluator findings, scored prior outputs, canonical archetype extracts, case-specific hidden corrections/examples, or sealed holdout content are supplied to the worker.

## Controlling rule

> **READ THE WHOLE SOURCE. RUN ALL SEVEN PRIMITIVE CLASSES AS INDEPENDENT RESEARCHER LENSES. EMIT EVERY SOURCE-SUPPORTED COORDINATE THAT PERFORMS A DISTINCT CLASS-NATIVE JOB AT NATURAL SOURCE GRAIN. DO NOT LET AN OBJECT REPLACE A LABEL, A VERB REPLACE A LOCATOR, A PLACE REPLACE AN OCCURRENCE PLACE, A TIME REPLACE A DISTINCT EPISODE FRAME, OR ANY OTHER CLASS SUBSTITUTE FOR ANOTHER. DEDUPLICATE ONLY TRUE SAME-CLASS SAME-IDENTITY DUPLICATES. PRESERVE THE SMALLEST SOURCE-NATIVE LEXICAL KERNEL FOR WORDED PRIMITIVES; MOVE ARGUMENTS, COMPLEMENTS, AND RELATIONAL RECONNECTION INTO COMPOUNDS. MERGE COREFERENCE ONLY WHEN THE SOURCE CLEARLY TREATS EXPRESSIONS AS THE SAME ENTITY AT THE SAME GRAIN. AFTER ALL SEVEN CLASS PASSES, FREEZE PRIMITIVES AND BUILD ONE MINIMAL SOURCE-ASSERTED BINDING PER MATERIALLY DISTINCT ASSERTED RELATION OR NONVERBAL CONFIGURATION.**

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
2. Resolve only strict coreference and broad source order.
3. Replay the source as represented assertions/episodes so distinct occurrence phases are visible without creating a global permission ledger.
4. Run a complete independent pass for PLACE, TIME, PERSON, OBJECT, LABEL, VERB, and LOCATOR.
5. Apply the class-native floor and ceiling within each class.
6. Deduplicate only true same-class same-identity duplicates.
7. Audit cross-class coverage without using one class as a substitute for another.
8. Lock literal source strings and freeze primitives.
9. Build compounds from frozen primitives only.
10. Run final floor, ceiling, type, literal, strict-coreference, occurrence-anchor, and compound audits.

## 2. Orthogonal-class rule

The seven classes answer different researcher questions. Related meaning across classes is expected.

A coordinate in one class does **not** make a lawful coordinate in another class expendable. Cross-class overlap is allowed whenever the same source material genuinely performs different class-native jobs.

Examples of the rule in abstract form:

- an occurrence PLACE may coexist with a LOCATOR relation;
- a TIME frame may coexist with temporal wording that performs another lawful class job;
- an applied LABEL may coexist with the VERB or OBJECT involved in the same assertion;
- an OBJECT may coexist with a related value, container, part, choice, or content when the source gives each distinct referential identity.

Do not duplicate merely because two grammatical readings are possible. Preserve both only when two distinct class-native semantic jobs actually exist.

## 3. Within-class identity and deduplication

Deduplicate when two candidates are truly the same class-level coordinate at the same grain because of:

- strict coreference;
- repeated mention;
- alternate tokenization of the same lexical kernel;
- same-grain paraphrastic/restated cueing;
- overlapping spans that perform the same class job.

Do **not** merge merely because candidates are closely related. Association, whole/part, product/container, actor/role, referent/value, broad episode/subepisode, place/sub-place, relation/state, source/target, or occurrence/context relation can remain distinct when the source establishes distinct class-native coordinates.

## 4. Lexical-kernel rule

When `source_wording` is used, preserve the smallest source-native wording that fully performs the primitive's class job.

Do not absorb ordinary arguments, complements, neighboring descriptions, or clause scaffolding into the primitive when those elements have their own coordinates or belong in the compound.

Preserve semantically essential material such as:

- negation that changes identity;
- particles in phrasal/idiomatic relations;
- reflexive material when it changes the relation;
- indispensable complement material when removing it changes the lexical relation itself rather than merely naming an argument.

Never synonymize, lemmatize, repair grammar/spelling, normalize dialect, translate, or invent wording.

## 5. Strict-coreference rule

Merge expressions only when the source clearly treats them as the same represented entity at the same researcher grain.

Do not infer identity merely from:

- physical association;
- containment;
- part-whole relation;
- a product and its visible presentation/container;
- a person and a role related to that person;
- an event and a decision/value/content about that event;
- two locations that overlap;
- two times that overlap.

When uncertain whether related expressions are strictly identical, preserve the source distinctions rather than erase them through convenience merging.

## 6. PLACE

`PLACE` asks: **what distinct represented occurrence or participant position does the source establish?**

Retain named and lawful unnamed positions when they anchor a distinct occurrence, participant phase, interaction, wait, movement, telling, memory, comparison, or prospective event.

PLACE is an occurrence coordinate, not merely a geospatial node. Two source assertions may lawfully have separate PLACE coordinates even when physically co-located if the source represents materially different occurrence/participant positions needed for reconnection.

For an unnamed PLACE:

- `source_wording` may be `null`;
- `source_cue` must be exact source evidence;
- the short tag must be neutral and mechanical, not an interpretation.

Suppress surfaces, body parts, directions, abstract spaces, or spatial words that do not establish a represented occurrence/participant position.

## 7. TIME

`TIME` asks: **what distinct episode, period, phase, recurrence span, transition frame, remembered frame, prospective frame, or present-reflection frame does the source establish?**

TIME is an occurrence/episode coordinate, not merely a calendar interval. Overlapping phases may both qualify when they anchor materially distinct represented assertions or phases.

For an unnamed TIME:

- `source_wording` may be `null`;
- `source_cue` must be exact source evidence;
- the short tag must neutrally identify the episode/frame.

Suppress pure tense/aspect grammar, local adverbs, duration/frequency wording, or repeated cues that do not establish a distinct episode/frame.

## 8. PERSON

`PERSON` asks: **who or what stable social actor/group is represented?**

Retain `B` plus distinct source-supported human/social actors or stable groups after strict coreference.

Minor, offscreen, possessive/relational, remembered, reported, prospective, institutional, recipient, beneficiary, source, and target actors may qualify when represented as actors.

Suppress rhetorical/nonreferential addressees and true coreference duplicates. Do not erase an actor merely because the actor is introduced through possession, role, or relation.

## 9. OBJECT

`OBJECT` asks: **what concrete or abstract referent/content does the source establish as a distinct thing-level coordinate?**

Retain source-treated referents that can participate in relations, be possessed/selected/compared/moved, carry value/content, be chosen, be pointed back to, or otherwise function as the same represented thing/content.

Related referents are not automatically identical. Preserve distinctions among source-treated wholes, parts, containers/presentations, values, choices, contents, decisions, artifacts, and other referential material when each has distinct source identity.

Suppress:

- clause shells/propositions not treated as referents;
- vague placeholders without stable source identity;
- decorative nouns/metaphor fragments whose only job is description;
- true same-grain coreference duplicates.

## 10. LABEL

`LABEL` asks: **what distinct source-applied state, value, quality, classification, evaluation, identity, status, manner, polarity, or characterization is established?**

Retain the smallest complete source-native characterization kernel when it has:

- an identifiable target/bearer; or
- an independently staged status/classification in the source.

Preserve material negation, uncertainty, correction, question-status, contrast, or intensity when it changes the label identity.

A related VERB, OBJECT, TIME, PLACE, or broader semantic situation does not replace a lawful LABEL. Distinct source-applied characterization kernels may remain separate even when they concern the same bearer and broader state.

Suppress decorative wording that performs no independently reconnectable characterization job and true same-grain restatements of one label.

## 11. VERB

`VERB` asks: **what distinct source-established action, relation, experience, cognition, possession, stance, movement, social act, or operative predicate is asserted?**

Retain the smallest complete lexical relation kernel for each distinct asserted relation.

Ordinary arguments and complements should normally be represented through PERSON/OBJECT/LABEL/PLACE/TIME/LOCATOR coordinates and reconnected in compounds rather than swallowed into the VERB wording.

Keep particles, negation-bearing construction, reflexives, or essential complement material only when removing them changes the relation identity itself.

Suppress:

- auxiliaries and pure tense/aspect machinery;
- copular/reporting shells that add no distinct relation;
- fragments split from one lexical predicate kernel;
- repetition or alternate spans for the same relation;
- discourse-management verbs that add no researcher relation.

Multiple VERBs from one sentence are lawful when the source asserts genuinely distinct relations.

## 12. LOCATOR

`LOCATOR` asks: **what distinct orientation, path, relative-position, containment, origin/destination, proximity/distance, approach/departure, accompaniment, embodied/internal, situational-context, or figurative-orientation relation does the source establish?**

A lawful LOCATOR may coexist with PLACE, TIME, VERB, OBJECT, or LABEL coordinates from the same source material. Another class does not substitute for orientation/context.

Retain a locator when it establishes a distinct orientation/path/context relation among coordinates or relative to a represented context.

Suppress ordinary argument attachment, topical/possessive grammar, or deictic filler that adds no distinct orientation relation.

## 13. Source replay and primitive floor

After all class passes, replay the whole source assertion by assertion.

For each class ask:

**If this coordinate is removed, is that class-native source distinction still represented by a true same-class same-identity coordinate?**

- If no, retain it.
- If yes only because another class carries related meaning, retain it anyway.
- If yes because a true same-class duplicate remains, suppress the duplicate.

Narrative centrality, standalone importance, repetition, or high salience are not required.

## 14. Primitive ceiling

Suppress candidates whose only contribution is:

- grammatical scaffolding;
- alternate tokenization;
- same-class same-grain restatement;
- a descriptive span wider than the needed lexical kernel;
- analyst-created abstraction;
- wording without a class-native coordinate identity.

The ceiling is not permission to use another primitive class as a substitute.

## 15. Literal lock and order

Preserve source-native wording character-for-character wherever the schema requires source text.

Only lawful unnamed PLACE/TIME coordinates may use null `source_wording`; their `source_cue` and `order_cue` remain exact source evidence.

Order primitives by first source establishment after strict coreference, subject to code-owned canonicalization. Broad-before-contained ordering applies only when both coordinates are lawfully distinct.

`qualities_available` is boolean only. It does not replace LABEL and does not authorize interpretation.

## 16. Compound reconstruction

Freeze primitives before compounds.

A compound is a minimal source-asserted binding among two or more frozen primitives needed to reconnect one materially distinct asserted relation or independently represented nonverbal configuration.

For each assertion/relation:

1. identify the frozen relation/configuration kernel;
2. add the smallest sufficient participants/referents;
3. add applied state/orientation coordinates actually bound by that assertion;
4. add occurrence PLACE/TIME anchors when the source binds that assertion to them;
5. project that materially distinct binding once.

Do not create compounds from:

- mere co-occurrence;
- every grammatical dependency;
- pairwise graph closure;
- every subset/superset;
- alternate parse/tokenization;
- scene-wide mega-bundles;
- compensation for a missing primitive.

Canonical compound IDs/order and `Q` construction remain code-owned.

## 17. Final audits

Before returning the candidate, verify:

### Class audit
Each retained primitive performs its class-native job; no class was suppressed merely because another class carries related meaning.

### Coreference audit
Only strict same-entity same-grain references were merged.

### Lexical audit
Source-worded primitives use the shortest complete exact source-native kernels; no synonymizing or normalization occurred.

### Occurrence audit
Distinct represented event/participant phases were not collapsed merely because places/times overlap.

### Compound audit
Every compound uses frozen primitives and corresponds to one materially distinct source assertion/configuration; no graph closure or compensation occurred.

## 18. Worker isolation

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

## 19. Candidate-only boundary

All output remains Researcher Inventory candidate material.

Never:

- promote to Oval Office or sovereign/admitted APA records;
- mint an APA Blockchain ID;
- interpret canon or APA doctrine;
- convert the lightweight inventory into diagnosis, empathic analysis, moral judgment, or psychological inference;
- write candidate output to production or sovereign databases.

## 20. Calibration and holdout gate

Before the sealed holdout may be attempted under V134, the **same finalized V134 contract and same saved-agent calibration lineage** must pass:

1. one paired diagnostic batch across both approved archetypes; and
2. two additional paired repeatability batches across both approved archetypes.

Any mismatch keeps the holdout sealed and returns to prospective calibration. Do not weaken evaluator acceptance criteria to obtain a pass.

Only after all paired gates pass may that calibrated lineage attempt the sealed holdout exactly once.

If that one calibrated-lineage holdout passes:

1. retire that calibration agent/lineage;
2. create a brand-new saved agent from only the finalized durable V134 instructions;
3. do not transfer prior session state or holdout output;
4. run the sealed holdout once in a new clean-room session.

Certification requires the fresh clean-room agent to pass. A failed holdout is preserved and not retried automatically.

## 21. Historical integrity

V133 and every predecessor contract, workflow, candidate, evaluator finding, failed attempt, and training-history record remain intact and controlling for the executions they governed.

V134 controls only prospective calibration and any later certification produced under this exact finalized contract.
