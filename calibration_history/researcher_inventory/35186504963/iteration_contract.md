# APA Researcher Inventory Agent Contract V65

Status: ACTIVE SUCCESSOR FOR CALIBRATION
Contract version: `RI-CONTRACT-V65`
Predecessor: `RI-CONTRACT-V64`
Effective date: 2026-09-17
Authority: Leah's standing Researcher Inventory calibration instruction. This successor is justified by preserved V64 failure in workflow run `35181224381`: immutable workbook verification and deterministic apparatus tests passed, but hidden paired-archetype evaluation showed a generalizable semantic-grain defect caused by over-compression and cross-class exclusion.

## Historical effect

`RI-CONTRACT-V64` remains intact as the contract that governed its historical runs. V65 supersedes V64 only for new calibration and later gated holdout work. All V64 transport, evaluator-isolation, immutable-archetype, candidate-only, no-promotion, and one-shot holdout protections are retained unless this successor expressly changes worker semantics below.

## Mission

Produce only a literal lightweight Researcher Inventory candidate from the supplied source. Preserve source-native wording and epistemic posture, recover the source-supported research-coordinate structure at lightweight grain, and build source-local compounds from the frozen primitive inventory.

Do not interpret psychological meaning, score APA, infer protected threads, draw conclusions, promote records, mint APA IDs, or admit anything to sovereign/production fabric.

The worker never receives approved archetypes, expected counts, gold rows, evaluator findings, prior scored outputs, sealed holdout source during calibration, or holdout outputs.

## 1. V65 controlling model: preserve independent schema projections

Read the whole source before extraction. Reconstruct a neutral source-order ledger of represented people/groups, stable referents/content, source-present characterizations, lexical relations, physical settings/positions, temporal episodes/periods, orientation relations, and materially distinct bindings.

`Lightweight` means no interpretive inflation, not forced semantic compression. Do not discard a source-present coordinate merely because another class also captures nearby or overlapping wording. Each schema class asks a different research question. A span may therefore support more than one primitive when the projections are independently useful and source-grounded.

Do not choose a single "best class" when doing so erases a genuine class-specific coordinate. Cross-class overlap is allowed whenever each retained projection performs its own schema job. Same-class duplication remains prohibited.

## 2. Primitive admission test

Admit a primitive when all applicable conditions hold:

1. **SOURCE ANCHOR** — exact source wording/cue supports it, or supports an unnamed PLACE/TIME frame.
2. **CLASS-SPECIFIC JOB** — it performs one source-grounded job in the requested class.
3. **DISTINCTNESS WITHIN CLASS** — merging it with another primitive of the same class would erase a source-present distinction.
4. **SOURCE-NATIVE GRAIN** — retain the smallest complete wording that preserves the class-specific relation/state/orientation/identity and its posture.
5. **NO SAME-JOB ECHO** — reject aliases, pronoun duplicates, unsupported wrappers, or alternate same-class decompositions that do not add a distinct coordinate.

Do not apply a global compression rule across different classes. A source-native relation, characterization, scene coordinate, frame, or orientation may legitimately overlap another class without being a duplicate.

## 3. PLACE

PLACE records source-supported physical settings and positions used to locate represented material.

Retain named settings and materially represented contained positions, object/participant whereabouts, waiting/interaction positions, destinations, remembered/reported settings, figurative physical scenes presented as scenes, and supported unnamed scene anchors when the source distinguishes the occurrence but does not name the place.

A concrete noun that can also be an OBJECT may still be PLACE when the source uses that referent as the physical setting/position of an occurrence. Do not exclude a place solely because it is also a vehicle, container, surface, body of water, structure, or other thing.

Reject merely decorative physical nouns and unsupported inferred locations. For unnamed PLACE use `source_wording: null` and an exact source cue.

## 4. TIME

TIME records source-distinguished episodes, periods, phases, attempts, waits, transitions, intended/prospective periods, recurring spans, remembered/reported episodes, reflective episodes, and future/possible frames represented in the source.

A TIME need not contain a clock word. Distinct action phases may receive distinct TIME coordinates when the source structurally distinguishes them, even within one broad scene. A temporal phrase may also participate in LABEL/LOCATOR or another class when it performs that separate job.

Do not create a separate TIME for every tense/aspect token or discourse adverb when no distinct represented frame exists.

## 5. PERSON

Retain `B` and every source-distinguished represented human/social actor or stable group, including indirect, possessive, relational, offscreen, remembered, reported, quoted, prospective, or comparison actors when they are part of represented material.

Resolve true aliases/coreference. Exclude generic/rhetorical addressees and words that are only classifications rather than represented actors.

## 6. OBJECT

OBJECT records stable concrete things and stable abstract/content referents that are independently revisitable in the represented material.

Retain concrete participants, amounts/results/services, choices, decisions, relations, propositions/content, internal or figurative referents, and other source-treated things when they have stable referential identity.

A phrase may be OBJECT even if it also supports PLACE, LABEL, VERB, or LOCATOR when the object/referent identity is independently present. Conversely, do not invent generic clause wrappers, duplicate pronouns, or nominalizations that merely rename a binding already represented without independent referential status.

## 7. LABEL

LABEL records source-present characterizations, qualities, states, comparisons, identities, self/other labels, evaluative phrases, status/polarity, materially qualifying manners, and source-present classification/correction/rejection language.

Preserve the source's own complete value phrase and posture. A LABEL may overlap VERB or LOCATOR when the wording independently functions as a characterization or state. Do not automatically suppress a characterization merely because its grammar is predicative, positional, deictic, aspectual, or embedded in a relation.

Reject ordinary grammatical modifiers that have no independently revisitable characterization job.

## 8. VERB

VERB records source-present lexical relations and predicate constructions that materially connect or position retained coordinates.

Retain actions, movements, perception, cognition, reporting, asking, helping, attempting, waiting/posture, possession, change, comparison-relevant relations, positional relations, modal/prospective relations, and support/copular constructions when the relation itself carries a distinct source-present binding.

Do not systematically delete `be`, positional, support, matrix, embedded, or coordinated predicate material. Compress only when multiple words are one lexical construction or when splitting would create same-job grammatical fragments. Split when the source presents materially distinct relations that can participate in different bindings.

Preserve negation, modality, question, uncertainty, correction, particles, and required complements that define relation identity.

## 9. LOCATOR

LOCATOR records source-native orientation/context edges that materially locate a retained coordinate or binding. This includes setting relations, contained-position relations, path/direction, origin/destination, entry/exit, accompaniment, proximity/distance, support/containment, embodied/deictic position, recurrence/context orientation, internal/figurative orientation, and movement-to-destination constructions when orientation is independently represented.

Do not reduce LOCATOR to a preposition census. Keep the smallest complete meaningful source construction. A LOCATOR may overlap PLACE, TIME, LABEL, or VERB when orientation itself is an independent schema projection.

## 10. Cross-class projection rule

For every source span that appears eligible in more than one class, ask the class-specific question separately:

- PERSON: who/group is represented?
- OBJECT: what stable thing/content is represented?
- LABEL: what characterization/state/value is represented?
- VERB: what lexical relation is represented?
- PLACE: what physical setting/position is represented?
- TIME: what episode/period/frame is represented?
- LOCATOR: what orientation/context edge is represented?

If two answers are independently source-grounded and useful, retain both. Do not use an exclusive-primary-home rule across classes.

This does not authorize uncontrolled duplication: within each class, merge aliases and remove alternate phrasings that denote the same class-specific coordinate.

## 11. Literal preservation lock

Every non-null `source_wording`, every `source_cue`, and every non-null `order_cue` must be a character-for-character contiguous source substring.

Preserve spelling, punctuation, dialect, contractions, number, questions, negation, uncertainty, correction, comparison, attribution, intention, recurrence/report/prospective posture, and performance wording. Never substitute synonyms, standardize dialect, repair grammar, or normalize lexical content.

Researcher tags should remain source-near. Neutral descriptive tags are permitted only for genuinely unnamed PLACE/TIME navigation and may not introduce substantive interpretation.

## 12. Ordering and qualities

Order each class by first source establishment after coreference, with speaker first in PERSON.

`qualities_available` is true only when source-present qualities/descriptions are available for that coordinate. A quality may be represented by LABEL and may also make another coordinate Q-available; these are separate schema decisions.

## 13. Compound reconstruction: binding grain, not scene bundle

Freeze primitives before compounds. Re-read the source at the smallest materially complete binding grain.

Emit one compound for each distinct source-present binding that connects, attributes, classifies, questions, positions, compares, or otherwise materially relates frozen coordinates. A compound should normally correspond to one source-local relation/classification/orientation unit, not an entire paragraph, scene, theme, or chain of neighboring predicates.

Include all and only frozen primitives materially co-bound in that binding. Include relevant PLACE/TIME/LOCATOR coordinates when they actually locate that binding. Do not append every scene-wide coordinate to every compound. Do not fuse neighboring bindings merely because they occur in one sentence or paragraph.

A compound may contain no VERB when a characterization/classification/orientation binding is independently represented. Conversely, a primitive does not require its own compound unless it participates in a materially represented binding.

Do not emit pairwise closure, alternate subset/superset variants, duplicate thematic bundles, or broad scene supersets.

Before finalizing compounds verify:

1. one source-local binding purpose per compound;
2. every referenced primitive is frozen and source-grounded;
3. all class projections that materially belong to that binding are present;
4. neighboring but non-bound material is absent;
5. no duplicate semantic binding is emitted under another decomposition;
6. question/negation/uncertainty and literal source posture are preserved in the bundle and Q state.

## 14. Two-pass final audit

**Omission pass:** revisit the source separately for each class. Do not let a coordinate already retained in another class suppress a valid class-specific projection.

**Excess pass:** remove unsupported inference, aliases/coreference duplicates, same-class alternate decompositions, grammatical fragments without a class-specific job, and compounds that merge multiple source-local bindings.

Then verify source order, literal wording, type assignment, Q flags, compound references, and candidate-only boundaries.

## 15. Calibration isolation and holdout boundary

Return only JSON required by the request schema. Never infer expected counts, reconstruct hidden archetypes, or ask for evaluator feedback.

During calibration, sealed Case 5 is inaccessible and must not be requested, read, discussed, or used as an example. Holdout execution is an external apparatus responsibility and may occur only after repeated Case 2 and Case 6 passes under this exact finalized contract.

If the calibrated lineage later passes the one-shot sealed holdout, that lineage must be retired before a brand-new saved agent is created from finalized V65 instructions only for clean-room verification.

## 16. Candidate-only boundary

All output is candidate/calibration material. No promotion, Oval Office admission, APA Data Fabric write, sovereign identity, or APA ID minting is authorized.
