# APA Researcher Inventory Agent Contract V121

Status: `ACTIVE SUCCESSOR FOR CALIBRATION — NOT CERTIFIED`
Contract version: `RI-CONTRACT-V121`
Predecessor: `RI-CONTRACT-V120`
Effective date: 2026-09-20
Authority: Leah's standing Researcher Inventory calibration instruction
Registrar record: `APA-EXEC-2026-09-20-CASES-RI-V121-CAL-0001`

## Prospective correction basis

V120 executed only after the immutable Case 2 and Case 6 workbook hashes were verified and the deterministic apparatus/harness gates passed. Its paired-archetype calibration then failed semantically. The attempt and failure evidence remain preserved. No new harness defect was established.

V120 correctly rejected mere source-addressability as an admission rule, but its requirement for a stable material identity was not class-relative enough. That criterion became too restrictive for legitimate one-use occurrence-bound relations while remaining too permissive for some incidental descriptive/rhetorical spans. A relation, orientation, or characterization may be a distinct source-native coordinate even when it occurs only once and has no persistent entity-like identity. Conversely, a literal phrase does not become a coordinate merely because it is descriptive, grammatical, or pointable.

V121 therefore establishes class-relative individuation:

> **REFERENTIAL AND SUPPORT CLASSES ARE INDIVIDUATED AS SOURCE-ESTABLISHED ENTITIES OR SUPPORTS. OCCURRENCE-BOUND RELATIONAL CLASSES ARE INDIVIDUATED AS DISTINCT SOURCE-NATIVE RELATION, ORIENTATION, OR CHARACTERIZATION EVENTS. ONE-USE RELATIONS MAY QUALIFY; INCIDENTAL WORDING DOES NOT.**

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

The inventory is neither a sparse summary nor a surface-span census. Preserve the complete set of researcher-selectable coordinates that the source itself individuates at the intended workbook resolution.

## 1. Read the whole source and map support before extracting

Read the complete source before answering any requested class.

Internally distinguish the represented scenes/places, temporal episodes/frames, participants, things/content, characterizations, operative relations, orientations, reports, memories, questions, choices, comparisons, reflections, and prospective material.

For PLACE and TIME especially, first map materially distinct support frames across the whole source. Do not wait for an explicit place noun, clock, date, or temporal phrase. A source may establish a distinct place or time through the occurrence/interaction it supports.

Then answer only the requested class.

## 2. Primitive admission — class-relative individuation

Admit a primitive only when all applicable conditions hold.

### A. Source grounding

The coordinate is explicitly established by the source, except that PLACE and TIME may be unnamed when the source clearly establishes a distinct support frame. Never invent facts.

### B. Class-relative identity

Do not impose one entity-like identity test on all seven classes.

For `PLACE`, `TIME`, `PERSON`, and `OBJECT`, ask whether the source establishes one distinct support, participant, thing, content handle, or other referential coordinate in that class.

For `LABEL`, `VERB`, and `LOCATOR`, ask whether the source establishes one distinct characterization, relation kernel, orientation, path, containment, contextual relation, or other occurrence-bound relational coordinate. Such a coordinate may be unique, local, and one-use. It does not need to recur, persist through time, or possess an entity-like identity.

The controlling question is:

**Does the source itself differentiate this as one selectable coordinate in the requested class, rather than merely containing words that could be segmented that way?**

### C. Represented contribution, not incidental wording

A coordinate must represent something the source actually establishes in that class. It does not need to be globally salient, repeated, indispensable to a compound, or necessary to summarize the story.

Reject wording that contributes only grammar, narration, discourse management, rhetorical color, incidental description, stylistic emphasis, or an internal fragment of a stronger source-native coordinate.

### D. Natural literal grain

Use the smallest complete source-native unit that preserves the coordinate's represented job.

For occurrence-bound relational classes, prefer the lexical or phrasal nucleus carrying the relation/orientation/characterization. Do not promote an entire clause, proposition, question shell, or rhetorical bundle when a smaller source-native nucleus carries the relevant job.

Keep a natural multiword relation, characterization, idiom, comparison, negation, phrasal verb, bound complement, or orientation construction whole when splitting it would destroy or materially change the source-native job.

### E. Nonduplication

Merge true aliases/coreference and same-class restatements of one coordinate. Do not create new rows for repeated wording, syntactic recasts, or incidental subspans that do not establish a new class-native coordinate.

## 3. Anti-census and anti-compression rule

Literal presence is necessary evidence for explicit primitives, but it is not an admission rule by itself.

Do not inventory every:

- noun phrase;
- lexical verb occurrence;
- adjective or descriptive flourish;
- question shell;
- clause complement;
- temporal phrase;
- prepositional phrase;
- deictic;
- rhetorical fragment;
- discourse marker;
- repeated restatement;
- modifier or intensifier;
- source-local phrase that lacks its own represented class job.

At the same time, do not require persistence, recurrence, global importance, or compound indispensability. A legitimate local or one-use relation/orientation/characterization must not be omitted merely because it appears once.

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

A phrase treated by the source as a thing/content node is OBJECT even when its words sound descriptive. A phrase applied by the source as a characterization of a target is LABEL even when it is noun-like. A relation kernel is VERB when the relation itself is distinctly represented, even if unique/one-use; it is not VERB merely because a clause contains a lexical verb. A phrase is LOCATOR when its represented job is orientation/context, not merely because it is prepositional or adverbial.

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

Do not convert every physical noun, destination wording, or locator phrase into PLACE when it does not itself constitute a distinct spatial support.

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

An actor may be direct, offscreen, relational, possessive/beneficiary, institutional, remembered, reported, prospective, peripheral, or one-use when the source represents that actor as a participant or relation endpoint.

Reject rhetorical, generic, hypothetical-person wording that never becomes a represented actor coordinate.

## 8. OBJECT — thing/content ledger

Retain source-individuated concrete or abstract things/content handles.

Qualifying OBJECT coordinates may include concrete things and source-distinguished parts, amounts/values, services/results, decisions or next steps treated as things, contemplated alternatives treated as choices, named sets/categories, remembered/reported content, and internal represented content handles.

Do not create OBJECT from every argument, noun phrase, pronoun, generic `this/that/it`, clause complement, question content, explanation, proposition wrapper, discourse point, descriptive fragment, or action merely because it can be nominalized.

The source must treat the candidate as a distinct thing/content node.

## 9. LABEL — characterization-event ledger

Retain distinct source-applied characterizations, qualities/states, statuses, identities, evaluations, comparisons, self-labels, candidate labels, rejections, corrections, contrasts, and materially expressed postures.

LABEL is occurrence-bound and target-bearing. A legitimate characterization may occur only once. It does not need persistent independent identity outside the characterization event.

A LABEL must actually characterize a target or represented state. Preserve colloquial, idiomatic, uncertain, questioned, negated, corrected, rejected, and figurative labels when that characterization is itself represented.

Use the shortest complete exact source form that carries the characterization. Do not expand the LABEL into the surrounding clause merely to preserve context.

Reject decorative/rhetorical color, incidental description, generic manner wording, isolated intensifiers/modifiers, scene-setting adjectives that are not applied as a represented characterization, and repeated restatements.

## 10. VERB — operative relation-event ledger

Retain each distinct source-individuated operative relation kernel at natural predicate grain.

A VERB may express action, state, cognition, perception, report/communication, intention, decision, possession, comparison, evaluation, movement, transition, gesture, existence/location, obligation, recurrence, or another represented relation.

VERB is occurrence-bound. A legitimate relation may be unique and one-use. It does not need persistent identity, recurrence, global salience, or compound indispensability. Omit it only when it is merely grammatical/support scaffolding, a duplicate restatement, or not itself a represented relation coordinate.

Do not create one VERB for every lexical verb or every clause. Reject:

- auxiliary/support verbs;
- discourse/filler predicates;
- question shells whose relation is carried by a smaller nucleus or whose stable content belongs elsewhere;
- copular/reporting scaffolding when it contributes no distinct represented relation beyond the attached content;
- repeated restatements of the same relation;
- whole-clause or proposition wrappers;
- rhetorical bundles;
- subfragments nested inside a stronger natural relation kernel.

Preserve particles, reflexives, negation, modality, and bound complements when required for the relation's source identity. Preserve questioned, negated, hypothetical, intended, reported, remembered, recurring, and prospective posture without asserting occurrence.

## 11. LOCATOR — orientation-relation ledger

Retain each distinct source-individuated orientation/context relation such as position, path, direction, containment, proximity, movement orientation, accompaniment, origin/destination, entry/exit, recurrence/context, internal/relational orientation, and materially spatialized figurative orientation.

LOCATOR is occurrence-bound. A legitimate orientation may be unique and one-use and need not persist as an entity-like coordinate.

A LOCATOR is not every prepositional or adverbial phrase. Use the smallest complete meaningful exact source construction carrying the orientation relation.

An explicit spatial or temporal phrase may be LOCATOR rather than PLACE/TIME when it orients a larger support frame instead of constituting the support frame itself.

Reject recipient/topic/purpose/possession/degree complements, generic adverbials, isolated deictics that do not establish an orientation relation, and rhetorical location wording without a represented orientation job.

## 12. Literal lock and source posture

For every explicit primitive, preserve exact source-native wording. Every non-null `source_wording`, `source_cue`, and `order_cue` must be character-for-character source text.

Preserve colloquial language, dialect, spelling/grammar, idiom, figurative wording, negation, modality, uncertainty, question form, attribution, comparison, remembered/reported posture, hypothetical/prospective posture, correction, and rejection.

Never normalize, polish, translate, diagnose, euphemize, substitute synonyms, or lemmatize into a different surface form.

Researcher short tags are navigational only and must remain source-near.

## 13. Qualities flag

`qualities_available` is only a yes/no availability flag showing that source qualities/descriptions exist for the coordinate. Do not explode qualities into a full APA parse merely to support Q. Do not use Q to replace LABEL rows.

## 14. Primitive freeze audit — class-relative coverage and compression

Before compounds:

1. replay the whole source in order;
2. verify the scene/place map and temporal episode map, including legitimate unnamed supports;
3. verify `PLACE`, `TIME`, `PERSON`, and `OBJECT` for source-established referential/support coordinates;
4. verify `LABEL`, `VERB`, and `LOCATOR` for distinct occurrence-bound characterization/relation/orientation coordinates, including legitimate local and one-use instances;
5. restore valid coordinates omitted only because they lacked persistence, recurrence, or global importance;
6. remove candidates admitted only because they are addressable surface spans, incidental descriptions, grammatical constituents, or rhetorical/discourse material;
7. reduce whole-clause relation candidates to the smallest complete source-native lexical/phrasal nucleus that preserves the represented job;
8. arbitrate OBJECT/LABEL/VERB/LOCATOR by primary represented job;
9. verify natural literal grain, exact wording, coreference, class-local distinctness, and first-establishment order; and
10. freeze primitives.

The omission audit and compression audit are equally mandatory. Do not solve over-admission by returning to a sparse summary, and do not solve omission by turning the source into a token/clause census.

## 15. Binding ledger — validation, not primitive entitlement

After primitive extraction and before compound emission, use represented bindings to check whether the extracted coordinates reconnect to the source's material relations, characterizations, choices, reports, questions, reflections, and support frames.

The binding ledger is a validation and compound-construction aid. It is **not** the sole entitlement test for primitive existence. A legitimate primitive may remain unbundled, and a unique one-use relation may still be a valid primitive.

Do not invent a primitive merely to fill a binding. Do not delete a valid primitive merely because it is not required by a compound.

## 16. Compounds — selective material bindings

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

## 17. Identity and ordering

Primitive identity is class-local source identity, not mention count. Resolve true aliases/coreference before deduplication. Do not merge distinct coordinates merely because they are related, colocated, or lexically similar.

For occurrence-bound classes, identity follows the distinct represented relation/orientation/characterization event at natural source grain, not persistence across the narrative.

Code owns canonical output IDs. Supply only neutral identity keys when the apparatus asks for them. Order by first source establishment after coreference, subject to speaker-first PERSON and genuine broad-before-contained support rules.

## 18. Isolation boundary

The calibration worker must never receive:

- Case 2 or Case 6 gold workbook rows or canonical extracts;
- expected counts;
- evaluator findings;
- scored prior outputs;
- case-specific gold corrections/examples;
- `researcher_inventory/tests/holdout/CASE_5.sealed.txt` during calibration;
- any Case 5 holdout output.

A hidden evaluator may compare output only after execution. Its findings must never be inserted into later worker instructions or examples.

## 19. Archetype integrity and failure separation

Before calibration uses Case 2 or Case 6, repository workbook copies must pass Leah's immutable SHA-256 gates. If a copy is wrong, reconstruct it only from an already authorized source/extract and use it only when the reconstructed digest exactly equals the approved hash.

Preserve every calibration attempt, partial result, failure, transport/recovery record, and successor as durable history. Do not delete failed runs.

Classify harness/apparatus defects separately from worker-semantic defects. A harness correction alone does not justify semantic contract revision, and a semantic failure does not authorize changing evaluator mechanics.

## 20. Certification gate

V121 is not certified merely because it is active for calibration. Certification requires, in order:

1. immutable Case 2 and Case 6 workbook SHA-256 verification;
2. deterministic apparatus/harness tests passing;
3. paired Case 2 + Case 6 calibration passing at approved archetypal resolution, lexical preservation, type assignment, and compound construction;
4. repeated paired archetype passes under the exact same finalized V121 contract and same calibrated saved-agent lineage;
5. only then, exactly one sealed Case 5 holdout attempt by that calibrated lineage;
6. if and only if that holdout is archetypal, retire the calibrated lineage;
7. create a brand-new saved agent using only finalized V121 durable instructions and no prior session/holdout output;
8. run Case 5 once in a new session as clean-room verification; and
9. certify only if that fresh agent succeeds.

If any archetype gate fails, Case 5 remains sealed and `NOT_DEPLOYED`.

## 21. Hard prohibitions

Never perform APA scoring, protected-thread determination, psychological inference, promotion, Oval Office research admission, sovereign/admitted writing, APA-ID creation, or APA database mutation.

Never expose or use the sealed holdout as calibration material.

## Historical integrity

`RI-CONTRACT-V120` and all earlier contracts, attempts, outputs, findings, and histories remain preserved exactly as predecessor evidence. V121 controls only new calibration executions after its activation and does not retroactively relabel prior work.
