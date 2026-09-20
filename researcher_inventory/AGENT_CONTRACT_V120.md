# APA Researcher Inventory Agent Contract V120

Status: `ACTIVE SUCCESSOR FOR CALIBRATION — NOT CERTIFIED`
Contract version: `RI-CONTRACT-V120`
Predecessor: `RI-CONTRACT-V119`
Effective date: 2026-09-20
Authority: Leah's standing Researcher Inventory calibration instruction
Registrar record: `APA-EXEC-2026-09-20-CASES-RI-V120-CAL-0001`

## Prospective correction basis

V119 executed only after the immutable Case 2 and Case 6 workbook hashes were verified and all deterministic apparatus/harness tests passed. Two paired-archetype V119 runs then failed semantically under the same durable contract. The attempts and failure evidence were preserved. No new harness defect was established.

V119 correctly separated primitive admission from compound necessity, but it made `source-addressable` and `independently selectable` too permissive. That allowed many incidental surface spans to become primitives merely because a researcher could point to them, while some source-established support frames and stable semantic coordinates were still omitted.

V120 therefore establishes the middle grain:

> **A PRIMITIVE IS A SOURCE-INDIVIDUATED, CLASS-NATIVE COORDINATE WITH A STABLE MATERIAL ROLE. IT NEED NOT BE COMPOUND-INDISPENSABLE, BUT MERE SOURCE ADDRESSABILITY IS NOT ENOUGH.**

No archetype rows, expected counts, evaluator findings, prior scored outputs, calibration answers, canonical gold extracts, or sealed holdout material are supplied to the worker.

## Mission

Produce a literal, lightweight Researcher Inventory of the complete supplied source in exactly seven primitive classes:

1. `PLACE`
2. `TIME`
3. `PERSON`
4. `OBJECT`
5. `LABEL`
6. `VERB`
7. `LOCATOR`

Then build lightweight compounds only from frozen registered primitives.

The inventory is neither a sparse summary nor a surface-span census. Preserve the set of stable researcher-selectable coordinates that the source itself individuates at the intended workbook resolution.

## 1. Read the whole source and map support before extracting

Read the complete source before answering any requested class.

Internally distinguish the represented scenes/places, temporal episodes/frames, participants, things/content, characterizations, operative relations, orientations, reports, memories, questions, choices, comparisons, reflections, and prospective material.

For PLACE and TIME especially, first map materially distinct support frames across the whole source. Do not wait for an explicit place noun, clock, date, or temporal phrase. A source may establish a distinct place or time through the occurrence/interaction it supports.

Then answer only the requested class.

## 2. Primitive admission — stable class-native coordinate

Admit a primitive only when all applicable conditions hold.

### A. Source grounding

The coordinate is explicitly established by the source, except that PLACE and TIME may be unnamed when the source clearly establishes a distinct support frame. Never invent facts.

### B. Class-native individuation

The source represents one stable coordinate in the requested class: a support frame, actor, thing/content handle, characterization, relation kernel, or orientation/context.

Ask:

**Does this candidate have a stable identity in this class beyond merely being a phrase I can point to?**

If the answer is no, reject it.

### C. Material role without indispensability

The coordinate participates in materially represented source structure or, for PLACE/TIME, materially supports that structure.

It does **not** need to be indispensable to a compound, globally salient, repeated, or necessary to make the story understandable. But it must do more than carry grammar, narration, rhetorical color, or incidental wording.

### D. Natural literal grain

Use the smallest complete source-native unit that preserves the coordinate's identity. Keep a natural multiword relation, characterization, idiom, comparison, negation, question-label, or bound construction whole when splitting it would destroy identity.

### E. Nonduplication

Merge true aliases/coreference and same-class restatements of one coordinate. Do not create new rows for repeated wording, syntactic recasts, or incidental subspans that do not establish a new class-native identity.

## 3. Anti-census rule

Source addressability is necessary evidence, not an admission rule by itself.

Do not inventory every:

- noun phrase;
- predicate occurrence;
- adjective or descriptive flourish;
- question shell;
- clause complement;
- temporal phrase;
- prepositional phrase;
- deictic;
- rhetorical fragment;
- discourse marker;
- repeated restatement;
- source-local phrase that is meaningful but lacks its own stable class-native identity.

A researcher must be able to reconnect to a coordinate, but the inventory should not reproduce the text as a lexical census.

## 4. Functional typing — primary represented job

Type by the source's represented job, not grammar or lexical shape:

- spatial support -> `PLACE`
- temporal episode/support -> `TIME`
- represented human/social actor -> `PERSON`
- independently represented thing/content/referential handle -> `OBJECT`
- source-applied characterization/state/status/evaluation/comparison/identity -> `LABEL`
- operative happening/action/state/relation kernel -> `VERB`
- independently represented orientation/path/direction/containment/proximity/context -> `LOCATOR`

Use the **primary represented job** when one span could be grammatically analyzed several ways. Cross-class duplication is allowed only when the source genuinely establishes two independently selectable jobs, not merely because a phrase can be described in two linguistic categories.

A phrase treated by the source as a thing/content node is OBJECT even when its words sound descriptive. A phrase applied by the source as a characterization of a target is LABEL even when it is noun-like. A relation kernel is VERB only when the relation itself is a stable inventory coordinate, not merely because a clause contains a verb.

## 5. PLACE — spatial support ledger

Retain each materially differentiated source-established spatial support frame.

A PLACE may be:

- a broad explicit setting;
- a distinct contained/local setting;
- an unnamed location of a represented object, interaction, participant configuration, wait, or event;
- a destination or later setting;
- a remembered/reported setting;
- a present-telling setting when source structure establishes one.

Several relations may share one PLACE when the source does not differentiate their support. Conversely, two unnamed PLACE rows may both be required when the source establishes materially different support frames even though neither is named.

For unnamed PLACE use null `source_wording`, an exact source cue, and a neutral mechanical tag. Never invent where.

Do not convert every physical noun or locator phrase into PLACE.

## 6. TIME — temporal support ledger

Retain each materially differentiated source-established temporal episode/frame.

TIME is primarily an episode/support coordinate, not a list of temporal expressions. It may include:

- an attempt/condition episode;
- help/response phase;
- transition/departure phase;
- waiting interval;
- intended period;
- remembered/reported period;
- later conversation/report episode;
- recurring span;
- present-reflection frame;
- explicitly represented future/prospective frame.

A TIME does not require a clock, date, or temporal noun. Several relations may share one TIME when their support is the same. An explicit temporal expression is not automatically a TIME if it functions only as orientation/context inside a larger episode.

For unnamed TIME use null `source_wording`, an exact source cue, and a neutral mechanical tag.

## 7. PERSON — participant ledger

Retain the speaker and each distinct represented human/social actor or stable group after true coreference.

An actor may be direct, offscreen, relational, possessive/beneficiary, institutional, remembered, reported, prospective, peripheral, or one-use when the source represents that actor as a stable participant or relation endpoint.

Reject rhetorical, generic, hypothetical-person wording that never becomes a represented actor coordinate.

## 8. OBJECT — thing/content ledger

Retain source-individuated concrete or abstract things/content handles.

Qualifying OBJECT coordinates may include concrete things and source-distinguished parts, amounts/values, services/results, decisions or next steps treated as things, contemplated alternatives treated as choices, named sets/categories, remembered/reported content, and internal represented content handles.

Do not create OBJECT from every argument, noun phrase, pronoun, generic `this/that/it`, clause complement, question content, explanation, proposition wrapper, discourse point, or action merely because it can be nominalized.

The source must treat the candidate as a stable thing/content node.

## 9. LABEL — characterization ledger

Retain source-individuated characterizations, qualities/states, statuses, identities, evaluations, comparisons, self-labels, candidate labels, rejections, corrections, contrasts, and materially expressed postures.

A LABEL must characterize a target or represented state. Preserve colloquial, idiomatic, uncertain, questioned, negated, corrected, rejected, and figurative labels when that characterization is itself represented.

Use the shortest complete exact source form that carries the characterization.

Reject decorative/rhetorical color, incidental description, manner wording, isolated intensifiers, repeated restatement, and phrases that are meaningful but are not applied as a characterization.

## 10. VERB — operative relation-kernel ledger

Retain source-individuated happenings and relation kernels at natural predicate grain.

A VERB may express action, state, cognition, perception, report/communication, intention, decision, possession, comparison, evaluation, movement, transition, gesture, existence/location, obligation, recurrence, or another represented relation **when that relation is itself a stable selectable coordinate**.

Do not create one VERB for every lexical verb or every clause. Reject:

- auxiliary/support verbs;
- discourse/filler predicates;
- question shells whose stable coordinate belongs elsewhere;
- copular or reporting scaffolding when the stable content is a LABEL/OBJECT/other coordinate;
- repeated restatements of the same relation;
- whole-clause wrappers;
- subfragments nested inside a stronger natural relation kernel.

Preserve particles, reflexives, negation, modality, and bound complements when required for the relation's source identity. Preserve questioned, negated, hypothetical, intended, reported, remembered, recurring, and prospective posture without asserting occurrence.

## 11. LOCATOR — orientation/context ledger

Retain source-individuated orientation/context coordinates such as position, path, direction, containment, proximity, movement orientation, accompaniment, origin/destination, entry/exit, recurrence/context, internal/relational orientation, and materially spatialized figurative orientation.

A LOCATOR is an orientation coordinate, not every prepositional or adverbial phrase. Use the smallest complete meaningful exact source construction.

An explicit spatial or temporal phrase may be LOCATOR rather than PLACE/TIME when it orients a larger support frame instead of constituting the support frame itself.

Reject recipient/topic/purpose/possession/degree complements, generic adverbials, isolated here/there, and rhetorical location wording without independent orientation identity.

## 12. Literal lock and source posture

For every explicit primitive, preserve exact source-native wording. Every non-null `source_wording`, `source_cue`, and `order_cue` must be character-for-character source text.

Preserve colloquial language, dialect, spelling/grammar, idiom, figurative wording, negation, modality, uncertainty, question form, attribution, comparison, remembered/reported posture, hypothetical/prospective posture, correction, and rejection.

Never normalize, polish, translate, diagnose, euphemize, substitute synonyms, or lemmatize into a different surface form.

Researcher short tags are navigational only and must remain source-near.

## 13. Qualities flag

`qualities_available` is only a yes/no availability flag showing that source qualities/descriptions exist for the coordinate. Do not explode qualities into a full APA parse merely to support Q. Do not use Q to replace LABEL rows.

## 14. Primitive freeze audit — compression and omission together

Before compounds:

1. replay the whole source in order;
2. verify the scene/place map and temporal episode map, including legitimate unnamed supports;
3. verify each requested class for stable class-native identities;
4. restore low-salience/local/one-use coordinates omitted only because they were not globally important;
5. remove candidates admitted only because they are addressable surface spans;
6. remove grammar/discourse scaffolding, rhetorical color, proposition wrappers, internal fragments, and true duplicates;
7. arbitrate OBJECT/LABEL/VERB/LOCATOR by primary represented job;
8. verify natural literal grain, exact wording, coreference, and first-establishment order; and
9. freeze primitives.

The omission audit and compression audit are equally mandatory. Do not solve over-admission by returning to a sparse summary, and do not solve omission by turning the source into a token/clause census.

## 15. Compounds — selective material bindings

Build compounds only after primitive freeze.

A valid primitive may remain unbundled. Emit a compound only when two or more frozen coordinates jointly form one source-local, materially complete researcher binding.

A compound normally represents one coherent relation/characterization/question/choice/report/reflection binding with its actual participants/content and only the support/orientation coordinates needed to distinguish that binding.

Rules:

- use only registered frozen coordinates actually participating in the binding;
- include enough coordinates for material completeness, but no unrelated scene context;
- split when actor set, target/content, source posture, support frame, or independently represented relation changes materially;
- keep locally joint predicates together only when they jointly form one binding;
- do not create a compound merely to justify a primitive;
- do not create one compound per clause, predicate token, primitive, sentence, or addressable phrase;
- do not serialize alternate subset/superset decompositions of one binding;
- do not create arbitrary co-occurrence, all-pairs links, support chains, scene mega-bundles, singleton equivalents, duplicate restatements, or graph closure.

## 16. Identity and ordering

Primitive identity is class-local source identity, not mention count. Resolve true aliases/coreference before deduplication. Do not merge distinct coordinates merely because they are related or colocated.

Code owns canonical output IDs. Supply only neutral identity keys when the apparatus asks for them. Order by first source establishment after coreference, subject to speaker-first PERSON and genuine broad-before-contained support rules.

## 17. Isolation boundary

The calibration worker must never receive:

- Case 2 or Case 6 gold workbook rows or canonical extracts;
- expected counts;
- evaluator findings;
- scored prior outputs;
- case-specific gold corrections/examples;
- `researcher_inventory/tests/holdout/CASE_5.sealed.txt` during calibration;
- any Case 5 holdout output.

A hidden evaluator may compare output only after execution. Its findings must never be inserted into later worker instructions or examples.

## 18. Archetype integrity and failure separation

Before calibration uses Case 2 or Case 6, repository workbook copies must pass Leah's immutable SHA-256 gates. If a copy is wrong, reconstruct it only from an already authorized source/extract and use it only when the reconstructed digest exactly equals the approved hash.

Preserve every calibration attempt, partial result, failure, transport/recovery record, and successor as durable history. Do not delete failed runs.

Classify harness/apparatus defects separately from worker-semantic defects. A harness correction alone does not justify semantic contract revision, and a semantic failure does not authorize changing evaluator mechanics.

## 19. Certification gate

V120 is not certified merely because it is active for calibration. Certification requires, in order:

1. immutable Case 2 and Case 6 workbook SHA-256 verification;
2. deterministic apparatus/harness tests passing;
3. paired Case 2 + Case 6 calibration passing at approved archetypal resolution, lexical preservation, type assignment, and compound construction;
4. repeated paired archetype passes under the exact same finalized V120 contract and same calibrated saved-agent lineage;
5. only then, exactly one sealed Case 5 holdout attempt by that calibrated lineage;
6. if and only if that holdout is archetypal, retire the calibrated lineage;
7. create a brand-new saved agent using only finalized V120 durable instructions and no prior session/holdout output;
8. run Case 5 once in a new session as clean-room verification; and
9. certify only if that fresh agent succeeds.

If any archetype gate fails, Case 5 remains sealed and `NOT_DEPLOYED`.

## 20. Hard prohibitions

Never perform APA scoring, protected-thread determination, psychological inference, promotion, Oval Office research admission, sovereign/admitted writing, APA-ID creation, or APA database mutation.

Never expose or use the sealed holdout as calibration material.

## Historical integrity

`RI-CONTRACT-V119` and all earlier contracts, attempts, outputs, findings, and histories remain preserved exactly as predecessor evidence. V120 controls only new calibration executions after its activation and does not retroactively relabel prior work.
