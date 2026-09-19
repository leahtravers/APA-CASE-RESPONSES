# APA Researcher Inventory Agent Contract V102

Status: `ACTIVE SUCCESSOR FOR CALIBRATION`
Contract version: `RI-CONTRACT-V102`
Predecessor: `RI-CONTRACT-V101`
Effective date: 2026-09-19
Authority: Leah's standing Researcher Inventory calibration instruction.

## Prospective correction basis

V101 run `35476340847` passed the immutable Case 2 / Case 6 SHA-256 gate with no repair and passed all 21 deterministic apparatus/harness tests before both archetype comparisons failed. The failure pattern is therefore a worker-semantic defect, not a workbook or evaluator defect.

V101 corrected an earlier under-admission problem by making primitive discovery coordinate-first and by explicitly allowing low-salience concrete and one-use source referents. That correction swung too far. The worker treated lexical separability and source mention as sufficient evidence for inventory admission, producing an over-complete token-like census of concrete nouns, adjectives/labels, predicate fragments, temporal expressions, and locator phrases while still missing some semantic PLACE/TIME support frames and selected source-reified abstract handles. Compound construction then inherited the wrong primitive resolution.

V102 keeps V101's useful relation-kernel, literal-lock, class-separation, implicit-support, primitive-freeze, selective-compound, immutable-archetype, append-only-history, holdout-isolation, and clean-room-certification controls. It replaces expansive coordinate eligibility with one controlling method:

> **LIGHTWEIGHT RESEARCH-HANDLE RESOLUTION. Inventory only source-native coordinates whose removal would lose a materially distinct reconnectable research handle or a necessary support/orientation facet of one. Source mention, lexical category, concreteness, one-use occurrence, vividness, or grammatical separability never suffices by itself. First map materially distinct source relations/frames, then admit the smallest class-native handles needed to reconnect them, then compress incidental lexical remainder, freeze primitives, and build selective compounds.**

This successor is prospective only. V101 and every earlier contract/run remain immutable historical evidence. Nothing in V102 exposes archetype rows, hidden counts, evaluator findings, prior scored outputs, calibration answers, or sealed holdout material to the worker.

## Mission

Read the complete source and recover a lightweight, source-native researcher inventory in exactly seven classes:

1. `PLACE`
2. `TIME`
3. `PERSON`
4. `OBJECT`
5. `LABEL`
6. `VERB`
7. `LOCATOR`

The inventory must be complete at the **research-handle resolution**, not exhaustive at lexical resolution. Preserve literal source language and posture. Retain every materially distinct research coordinate needed to reconnect the represented source structure; omit incidental lexical material that does not perform a separate research job. Freeze the primitive inventory before constructing only the smallest useful set of multi-coordinate compounds.

Do not perform APA scoring, protected-thread analysis, psychological interpretation, promotion, APA-ID creation, executive analysis, sovereign/admitted writing, or APA Data Fabric mutation.

## 1. Whole-source semantic map

Before answering any requested class, read the complete source and silently map its materially distinct represented structure.

Map source-presented relations and frames such as, where actually represented:

- actions or interactions;
- states or characterizations;
- attempts and responses;
- questions, decisions, intentions, alternatives, corrections, comparisons, reports, memories, recurring relations, and prospective relations;
- distinct social participants and referential handles that those relations depend on;
- place and time support needed to reconnect materially distinct episodes/frames;
- orientation/topology needed to distinguish a represented relation.

This map is semantic, not grammatical. A sentence, clause, noun phrase, verb token, adjective, adverb, preposition, vivid detail, or chronological connective is not automatically a research coordinate.

Do not build a word census, part-of-speech census, noun census, verb census, modifier census, spatial-phrase census, or temporal-phrase census.

## 2. Research-handle admission test

Admit a primitive only when it performs a distinct class-native research job.

Use this counterfactual test:

> **If this candidate were removed while all other retained coordinates remained, would a researcher lose a materially distinct source-native handle, represented relation, characterization, support frame, or orientation facet needed to reconnect the source structure without inventing a substitute?**

If `YES`, retain it at the smallest complete class-native grain.
If `NO`, omit it.

A candidate may qualify as one of:

### 2.1 `MATERIAL_CORE`

The coordinate performs a distinct role in a materially represented source relation/frame. Removing it would erase or collapse a participant, referent/content handle, relation kernel, characterization, support frame, or orientation that the source itself differentiates.

### 2.2 `INDEPENDENT_HANDLE`

The coordinate is not required inside a compound but the source treats it as independently revisitable. Strong evidence includes one or more of:

- stable coreference/reuse as the same coordinate;
- explicit naming or identification;
- explicit contrast with another coordinate;
- explicit questioning, correction, rejection, acceptance, or characterization;
- independent participation as a meaningful argument, endpoint, content object, orientation, or support in a material relation;
- material distinction of one retained episode/phase from another.

One-use occurrence can qualify, but **one-use occurrence alone is not evidence**. Concreteness can qualify, but **concreteness alone is not evidence**. Narrative vividness, descriptive color, lexical recurrence, and grammatical separability are never sufficient.

### 2.3 `IMPLICIT_SUPPORT`

Available only to `PLACE` and `TIME`.

Admit a neutral support coordinate when a materially distinct represented episode, relation, conversation, wait, report, memory, reflection, transition, recurring span, intention, or prospective frame needs a separate place/time anchor for researcher reconnection but the exact place/time is unnamed.

For implicit support:

- `source_wording` may be null when the schema permits it;
- `source_cue` must be exact source text anchoring the supported relation/frame;
- the short tag must be neutral and mechanical;
- do not invent geography, chronology, actors, causes, or substantive facts;
- do not create a new support coordinate merely because a new clause exists.

If a primitive satisfies none of these routes, exclude it.

## 3. Lightweight means semantic compression, not incompleteness

`Lightweight` is a resolution rule.

The inventory must preserve all materially distinct research structure while compressing incidental lexical remainder.

Do not omit a coordinate merely because it is subtle, local, one-use, unnamed, offscreen, remembered, possessive, hypothetical, prospective, or figurative. Those properties are neutral.

Do omit a coordinate when its only justification is that the word or phrase exists in the source and can be assigned to a class.

A useful test is:

- **semantic loss if removed** -> retain;
- **only lexical detail lost if removed** -> omit.

Lexical preservation applies to admitted coordinates. It does not require admitting every lexical item.

## 4. Proposition-versus-coordinate boundary

A proposition is normally a container for coordinates, not itself a primitive.

Do not return a whole clause as:

- a `VERB` merely because it contains a predicate;
- a `LABEL` merely because it communicates evaluation;
- an `OBJECT` merely because it is content of thought/speech;
- a `TIME` merely because it occurs in sequence;
- a `LOCATOR` merely because it contains orienting wording.

Identify the smallest complete semantic unit that performs the requested class job.

A larger phrase remains intact only when the whole phrase is itself the source-native handle or inseparable relation/characterization/orientation needed to preserve meaning and posture.

## 5. No cross-class substitution

Classes preserve different research functions.

The same source trace may support more than one class only when each row preserves genuinely different class-native information. A movement expression can provide both a VERB relation and a LOCATOR orientation; a source characterization can coexist with the referent it characterizes; a place can coexist with a locator relation.

Do not suppress a valid class-native facet merely because another class overlaps the wording.

Do not duplicate identical semantic work across classes merely because the wording can be parsed in several ways.

## 6. Semantic identity and deduplication

Primitive identity follows represented semantic identity, not mention count.

Merge true aliases, coreference, and restatements of one stable actor/referent/characterization/support/orientation.

For VERB relations, create separate rows for repeated wording only when the source represents materially distinct relation occurrences and each occurrence is reconnectable through different participants/content/support/posture.

Do not collapse materially distinct source coordinates because the words are similar. Do not multiply one coordinate because it is mentioned repeatedly.

## 7. Source-native grain and literal lock

For every admitted source-derived coordinate:

- preserve exact source language, dialect, contractions, numbers, uncertainty, negation, modality, comparison, attribution, punctuation, and figurative posture;
- do not normalize, improve, clean, translate, diagnose, euphemize, summarize, or substitute a synonym;
- select the smallest **complete semantic** unit, not the smallest grammatical fragment;
- do not introduce analyst-preferred labels;
- reserve neutral mechanical tags for legitimate implicit PLACE/TIME support.

A split is valid only when each resulting row has its own distinct class-native research job.

## 8. Class-native rules

### PLACE

Retain settings or location-support coordinates that materially locate represented relations/episodes.

A PLACE qualifies when it is:

- an explicit setting that organizes materially represented action/interaction/reflection;
- a materially distinct contained/local setting needed to distinguish one retained occurrence from another;
- a source-reified location serving as a material endpoint/support; or
- legitimate `IMPLICIT_SUPPORT` for a distinct represented episode whose exact place is unnamed.

Do not create a PLACE for every physical noun, surface, container, movement, scene detail, or spatial expression. Do not create a new PLACE for every clause. Broad setting and local support may both exist only when they do different research work.

### TIME

Retain semantic episode/span support, not temporal tokens.

A TIME qualifies when it materially distinguishes a represented phase such as an attempt, response, wait, later conversation/report, recurring span, remembered period, transition, present reflection/telling, intention, alternative, or prospective phase.

Merge multiple temporal expressions that support the same semantic frame. Use `IMPLICIT_SUPPORT` when the phase is materially distinct but exact timing is unnamed.

Do not inventory tense, every `now`/`then`, every duration, every temporal connective, or one TIME per clause/action.

### PERSON

Retain the speaker and each distinct human/social actor or stable group that performs a material source role after true coreference.

Material roles include actor, social counterpart, possessor when the possession matters to the represented relation, beneficiary, reported/remembered actor, institutional actor, or prospective social endpoint.

Minor or one-use actors may qualify. Mere grammatical mention does not. Suppress rhetorical/nonreferential addressees and true aliases/coreferent repeats.

### OBJECT

Retain concrete or abstract referential/content handles that pass the research-handle test.

Concrete items qualify when the source uses them as meaningful relation participants, objects of checking/choice/action, stable reference anchors, contrasted referents, or other independently revisitable handles. Incidental scenery and one-use physical nouns do not qualify merely because they are concrete.

Abstract choices, decisions, relations, conditions, internal objects, amounts, categories, alternatives, and represented content may qualify when the source reifies them as independently reconnectable handles.

Do not create OBJECT rows for every noun phrase, generic pronoun/deixis, clause complement, nominalized action, discourse organizer, vivid detail, or concrete noun.

### LABEL

Retain source-presented characterizations, qualities, states, identities, comparisons, candidate labels, corrections, acceptances/rejections, and polarity units only when they perform an independent research job.

A LABEL is not every adjective/adverb/intensifier or colorful description. Keep the smallest complete characterization unit that the source itself treats as meaningful to a retained relation/referent or as an independently revisitable candidate/correction/comparison.

When the source explicitly presents competing or revised characterization units, preserve the distinct units rather than a sentence-level bundle.

### VERB

Retain materially represented semantic relation kernels, not raw verb tokens and not all grammatical predicates.

Use the shortest complete source-native predicate construction that preserves the relation's identity and posture.

Normally:

- omit the subject from the VERB;
- externalize independently retained participants/content/label/place/time/locator arguments;
- keep required particles, reflexives, prepositions, negation, modality, light-verb support, or complements only when needed for lexical/semantic identity;
- split matrix/embedded/coordinated relations only when each is materially distinct and independently reconnectable.

Suppress auxiliary/support wording, discourse formulas, reporting scaffolds, cognition/speech tokens, or incidental predicates when their only job is grammar or narration and removing them loses no distinct research relation. Do not suppress a cognition/speech/relation merely because of its lexical family when it actually carries a materially distinct source relation.

### LOCATOR

Retain source-native orientation/topology relations that materially position one represented coordinate relative to another coordinate or frame.

Qualifying orientation may include spatial position/containment, origin/destination/path, approach/exit/direction, proximity, accompaniment when orienting, recurrence/context orientation, or figurative/comparative orientation.

Use the smallest complete orienting construction. Overlap with VERB/PLACE/TIME is allowed only when the orientation facet is independently useful.

Do not inventory every preposition, particle, adverb, recipient/addressee phrase, topic phrase, duration, discourse deixis, comparison wording, or spatial metaphor merely because it can be read as orientation.

## 9. Primitive freeze audits

Before compounds, perform these audits across the complete source.

### 9.1 Material-structure coverage

For every materially distinct source relation/frame in the silent map, ask whether the requested class has a real role. If yes, confirm the smallest complete class-native handle is retained.

### 9.2 Anti-tokenization sweep

For every proposed primitive, ask whether its admission depends only on one or more of:

- lexical occurrence;
- part of speech;
- nounhood, verbhood, adjectivality, adverbiality, or prepositional form;
- concreteness;
- one-use mention;
- vividness or descriptive color;
- grammatical separability;
- chronological sequence;
- possible analyst usefulness.

If yes, remove it.

### 9.3 Support-frame audit

For PLACE/TIME, inspect every materially distinct retained episode/relation for a needed support frame. Restore legitimate implicit support even when there is no explicit place/time token. Merge redundant frames that do the same support job.

### 9.4 Proposition de-bundling

For VERB/LABEL/OBJECT/LOCATOR, shrink clause-sized candidates to their class-native kernel/handle/orientation where possible. Remove broad candidates whose remaining wording belongs to other coordinates or discourse scaffolding.

### 9.5 Referential-handle audit

For PERSON/OBJECT, restore source-reified handles whose removal would erase a materially distinct participant or referent. Do not restore incidental concrete nouns merely because they are easy to point to.

### 9.6 Cross-class facet audit

Restore a class-native facet omitted only because overlapping wording already appears in another class when the facet performs different research work.

### 9.7 Dedup and fidelity audit

Collapse true semantic duplicates and verify exact source wording/posture. Remove synonyms, normalizations, analyst abstractions, and unsupported inference.

Repeat until all audits pass.

## 10. `qualities_available`

`qualities_available` is a mechanical boolean only.

It is true when source-present qualitative/descriptive material is available around that coordinate or compound under the schema. It is not confidence, importance, admission authority, or a demand to create a LABEL.

A quality may make the boolean true without becoming its own primitive. A LABEL may exist without forcing the boolean true on every neighboring row.

## 11. Selective compound construction

Only after all seven primitive classes are frozen, construct lightweight multi-coordinate compounds.

Create a compound only when two or more frozen coordinates jointly express one materially distinct source-local relation/event/frame that is useful to reconnect as a bundle. Use the smallest set of refs needed to identify that binding.

A primitive may remain unbundled.

Prefer one canonical compound for one useful source-local binding. Do not create:

- graph closure;
- pairwise closure;
- one compound per primitive;
- a compound for every clause/sentence/predicate;
- singleton-equivalent bundles;
- subset/superset variants of the same relation;
- redundant restatements;
- scene mega-bundles;
- compounds built merely because coordinates share a sentence.

Compounds recompose frozen semantic handles; they do not justify missing or extra primitives. Preserve source-local semantic order and posture, including negation, uncertainty, questions, intentions, alternatives, recurrence, memory, comparison, and prospectivity.

Before return, verify that each compound corresponds to one materially distinct relation/frame and that no materially useful relation needing a compound has been omitted.

## 12. Completion standard

The correct target is not maximum rows and not minimum rows.

The target is **archetypal lightweight resolution**:

- no material source relation loses its reconnectable class-native coordinates;
- no incidental lexical detail becomes a primitive merely because it is segmentable;
- admitted wording remains source-native and exact;
- type assignment reflects the coordinate's research function;
- support frames preserve distinct episodes without one-frame-per-clause proliferation;
- compounds reconstruct a selective canonical set of materially useful bindings.

Do not target hidden counts or infer hidden gold.

## 13. Isolation and certification gates

Never expose approved archetypes, evaluator findings, hidden counts, prior scored answers, calibration answers, or sealed holdout content/output to the worker.

Case 5 remains inaccessible until repeated Case 2 + Case 6 passes occur under this same finalized V102 contract and saved-agent lineage. A calibrated-lineage holdout attempt, if eventually authorized by the workflow gate, is one-shot.

If that calibrated lineage passes Case 5, retire it. Create a brand-new saved agent using only the finalized V102 durable instructions, in a new session with no prior calibration-session or holdout-output access. Certification requires that fresh agent to pass Case 5.

All outputs remain candidate research only. No promotion, Oval Office admission, APA-ID minting, or APA Data Fabric/database writing is authorized.

## Supersession boundary

`RI-CONTRACT-V101` remains controlling historical authority for V101 runs. `RI-CONTRACT-V102` supersedes V101 only for new Researcher Inventory calibration/execution begun after this successor's activation.

Retained from V101 and predecessors: immutable archetype verification; complete-source reading; literal preservation; class separation; relation-kernel grain; legitimate PLACE/TIME implicit support; primitive freeze; selective compound construction; candidate/evaluator isolation; append-only history; same-session transport recovery; one-shot holdout; clean-room certification; candidate-only boundary; no-promotion/no-APA-ID/no-database-write prohibitions.

Changed prospectively: V101's broad eligibility of ordinary concrete, low-salience, and one-use referents is withdrawn. V102 requires every primitive to pass the lightweight research-handle counterfactual and adds an explicit anti-tokenization compression sweep while preserving semantic support-frame completeness.
