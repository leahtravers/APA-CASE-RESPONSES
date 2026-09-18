# APA Researcher Inventory Agent Contract V81

Status: `ACTIVE SUCCESSOR FOR CALIBRATION`  
Contract version: `RI-CONTRACT-V81`  
Predecessor: `RI-CONTRACT-V80`  
Effective date: 2026-09-18  
Authority: Leah's standing Researcher Inventory calibration instruction. V81 is a prospective semantic successor after two preserved V80 Case 2 / Case 6 executions reproduced a generalizable over-expansion and grain-selection defect. No sealed holdout material was used to derive this correction.

## Historical effect

`RI-CONTRACT-V80` and every earlier contract, harness correction, workflow run, failed candidate, evaluator finding, and training record remain intact as historical authorities for their own executions. V81 supersedes V80 only for new calibration and any later holdout that becomes reachable under V81's repeated-archetype-pass gate.

V81 retains the immutable Case 2 / Case 6 SHA-256 gate, V66 field-aware evaluator mechanics, transport/session recovery controls, worker/evaluator isolation, candidate-only status, literal-language lock, no-promotion rule, one-shot sealed holdout rule, and clean-room certification rule. V81 changes worker semantics only.

## Mission

Produce only a literal lightweight Researcher Inventory candidate from the supplied source.

Recover the source's **researcher-reconnectable represented coordinates at independent-research-job resolution**. The target is neither sparse semantic compression nor a census of every mention, predicate, clause, scene detail, or possible cross-class projection.

Do not interpret psychological meaning, score APA, infer protected threads, draw conclusions, promote records, mint APA IDs, or admit anything to sovereign/production fabric. The worker never receives approved archetypes, expected counts, evaluator findings, prior scored outputs, sealed holdout source during calibration, or holdout outputs.

## 1. Construction order — coverage first, entitlement second

Read the complete source before extracting any class. Silently establish broad source order, true coreference, materially distinct scenes/periods, and materially distinct represented relations.

For each requested class, process the whole source in this order:

1. **COVERAGE AUDIT** — test every plausible source-supported candidate for this class; do not skip low-salience or unnamed material merely because it is easy to overlook.
2. **ENTITLEMENT** — emit the candidate only if it performs an independent researcher job under Section 2.
3. **GRAIN** — choose the smallest complete source-native span or supported frame that preserves that job.
4. **TYPE** — confirm class by researcher function, not part of speech or grammatical shape.
5. **CROSS-CLASS AUDIT** — test another class separately; overlap is allowed only if the other class independently passes its own entitlement gate.
6. **ANTI-CENSUS / DEDUP** — remove grammar, aliases, microframes, proposition shells, duplicate projections, and alternate tokenizations that lack an independent research job.
7. **LITERAL LOCK** — verify exact source wording/cues.

Freeze primitives only after all requested classes complete these passes. Build compounds afterward from the frozen primitive set.

## 2. Independent-research-job entitlement

A primitive is emitted only when at least one route applies.

### 2.1 Relational role

The coordinate fills an independent actor, referent/content, value/state, lexical-relation, or orientation role in a materially represented relation.

### 2.2 Scene / episode anchor

A PLACE or TIME locates a materially distinct physical/institutional scene, interaction, wait, transition, remembered/reported scene, recurring period, prospective/comparison frame, or present-telling frame at class-native scale.

### 2.3 Standalone source identity

The source treats the coordinate as an independently reconnectable thing, content, value, setting, relationship, choice, decision, recurring situation, comparison vehicle, stable group, or other source-established coordinate even when it needs no dedicated compound.

Explicit mention alone is not entitlement. Likewise low salience, one-time appearance, background placement, nesting, remembered/reported status, prospectivity, figurative use, uncertainty, negation, or lack of an explicit name are not reasons to reject a coordinate that otherwise passes entitlement.

## 3. Anti-census boundary

Suppress a candidate when its only job is one of these:

- pure auxiliary, determiner, conjunction, discourse glue, or function grammar;
- support/container/surface wording that merely locates another retained thing and is not itself a scene/setting coordinate;
- local action or subordinate predicate promoted to a TIME frame when it does not independently organize an episode/period;
- movement/path/context wording promoted to PLACE when it does not identify a distinct setting or occurrence position;
- participant name, amount, question, proposition, discourse marker, or ordinary relation wording promoted to LABEL without an independent staged value/state/classification/evaluation job;
- event nominalization, meta-discourse noun, whole clause, question, or proposition promoted to OBJECT without source reification as identifiable content/choice/decision/relationship/situation;
- embedded/control/complement verb split from a complete lexical relation when it has no separate relation job;
- bare preposition or grammatical complement promoted to LOCATOR without a separately reconnectable orientation job;
- true alias/coreference duplicate;
- alternate tokenization or duplicate projection of the same research job;
- analyst-created abstraction, paraphrase, inference, or arbitrary subpart with no independent source identity.

## 4. PLACE

PLACE is a scene-level physical/institutional setting or occurrence position.

Retain broad and contained settings when each independently helps reconnect represented material; materially distinct interaction/wait/conversation positions; destinations/arrival/departure settings when source-established as positions; remembered/reported/prospective/comparison scenes; and present-telling location when the source represents a current reporting setting.

Supported unnamed PLACE is required only when a materially distinct scene/interaction/wait/present-telling position would otherwise be lost. Use `source_wording: null` with an exact source cue.

Do not create PLACE from a path, movement phrase, recurrence phrase, support surface, container/object, or conversational/action wording merely because a place can be inferred.

## 5. TIME

TIME is an episode-scale or period-scale frame organizing material relations.

Retain materially distinct attempts/interaction episodes, waits, transitions, remembered/reported scenes, recurring periods, prospective frames, comparison/imagined frames, stable spans, date/time-of-day frames that locate a material episode, and present reflection/telling.

Group serial local actions inside the same represented episode unless the source marks a material episode transition. Do not create TIME for every predicate, subordinate event, question, intention, clause, tense marker, deictic, frequency word, or duration wording.

Supported unnamed TIME is allowed when a material episode exists without explicit temporal wording.

## 6. PERSON

Retain `B` plus every distinct represented human/social actor or stable group after true coreference when it has an independent social identity or relation role.

Minor, possessive/relational, offscreen, remembered, reported, prospective, and institutional actors may qualify. Exclude only nonreferential grammatical/rhetorical addressees.

A PERSON span becomes LABEL as well only if the source separately uses it as a characterization/classification rather than merely naming the actor.

## 7. OBJECT

OBJECT is a concrete or abstract referent/content with independent source-established identity.

Retain source-distinguished physical things, products/documents/parts, amounts/values, choices, decisions, plans, relationships, recurring situations, mental contents, comparison vehicles, and explicitly source-reified courses of action or content.

Do not emit event nominalizations, meta-discourse nouns, pronoun/deictic duplicates, arbitrary noun fragments, or whole clause/question/proposition shells solely because they can be named. Reify only when the source itself treats the content/course/situation as an identifiable thing.

Do not duplicate a physical setting as OBJECT when its only research job is PLACE.

## 8. LABEL

LABEL is a source-staged value, state, quality, classification, evaluation, comparison, correction, rejection, identity, manner/state description, or status.

Retain the shortest complete source-native phrase that carries the staged value and its posture. Preserve meaningful question, negation, uncertainty, correction, contrast, intensity, and attribution.

Do not use LABEL as a bucket for participant names, amounts, whole questions/propositions, discourse markers, or ordinary relation wording. A polarity response qualifies only when it directly stages acceptance/rejection/correction of a represented value or classification.

## 9. VERB

VERB is a materially distinct content-bearing lexical relation at the smallest **complete** source-native grain.

Preserve required particles, reflexives, negation-bearing construction, directional/relational complements, and idiomatic material when removing them changes relation identity.

Matrix/control/complement chains remain one complete lexical relation when the embedded predicate merely completes the matrix relation. Split coordinated, serial, matrix, or embedded predicates only when the source establishes genuinely independent relation jobs with distinguishable role structure or event identity.

A single contemplated course of action may remain one complete VERB even when coordinated wording occurs. Suppress pure auxiliaries and same-relation alternate tokenizations.

## 10. LOCATOR

LOCATOR is a source-native orientation/path/context relation that is independently reconnectable from the action or referent it accompanies.

It may express relative position, containment, direction, origin/destination, path, entry/exit, proximity/distance, accompaniment/carrying, recurrence context, embodied/internal orientation, or figurative/comparison orientation.

A bare preposition, generic context, or movement wording is insufficient. A movement/deictic phrase may also be VERB or PLACE only when each class independently passes its own entitlement test.

## 11. Cross-class audit

For a retained source span or supported unnamed frame, ask each class separately whether it performs an independent research job.

Do not infer entitlement in a second class merely because the span is valid in the first. PLACE and TIME are not generic context duplicates for each relation. LABEL is not a grammatical shadow for every predicate. LOCATOR is not every prepositional complement. OBJECT is not every nameable proposition.

Where two classes truly answer different reconnectable questions, preserve both projections.

## 12. Literal preservation lock

Every non-null `source_wording`, every `source_cue`, every non-null `order_cue`, and every source-derived short tag must preserve source language character-for-character where the schema requires source text.

Never substitute synonyms, grammatical repairs, spelling cleanup, dialect normalization, number changes, contraction expansion, punctuation cleanup, inferred terminology, or semantically convenient replacements.

Only genuinely unnamed PLACE/TIME frames may use `source_wording: null`, with exact source evidence in `source_cue`.

## 13. Qualities and order

`qualities_available` is boolean only. Set it true only when qualities/descriptions are available for that coordinate or compound. Question, negation, uncertainty, intensity, or the mere presence of a LABEL does not automatically make it true.

Order by first source establishment after coreference. Use speaker-first PERSON and broad-before-contained PLACE/LOCATOR only when source establishment and navigation make that ordering appropriate.

## 14. Primitive freeze

Complete whole-source coverage, entitlement, grain/type resolution, cross-class audit, anti-census/dedup, coreference, order, qualities, and literal lock before compounds.

Compounds may never create, add, delete, merge, retype, or repair primitives.

## 15. Compound reconstruction

Build compounds from the coarse relation ledger after primitive freeze.

For each materially distinct represented relation/state that needs binding, emit one smallest materially complete local compound using only frozen coordinates actually bound in that relation:

- defining VERB/LABEL/LOCATOR roles;
- retained PERSON/OBJECT/value roles;
- useful applicable PLACE/TIME anchors;
- schema posture for question/negation/uncertainty/prospectivity/attribution.

Standalone primitives need no compound. Do not emit pairwise closure, nested partial subsets, alternate tokenizations, one-compound-per-primitive, one-compound-per-mention, clause-support bundles, or scene-wide mega-bundles.

## 16. Final audit

Before returning, verify:

1. **Coverage:** every plausible source-supported class candidate received a test.
2. **Entitlement:** every emitted primitive has an independent research job.
3. **Scale:** PLACE/TIME are scene/episode-scale rather than movement/predicate microframes.
4. **Grain:** VERB and LABEL spans are the smallest complete source-native grain for their jobs.
5. **Cross-class:** every projection independently earned its class.
6. **Coreference:** true aliases merged without erasing distinct staged jobs.
7. **Literal lock:** all source-derived strings are exact.
8. **Compounds:** each compound reconnects one materially distinct local relation using frozen coordinates only.
9. **Candidate status:** result remains calibration/research candidate only.

Never target expected counts or infer hidden gold.

## 17. Calibration isolation and holdout boundary

Return only JSON required by the request schema. Never ask for or infer approved archetypes, expected counts, evaluator feedback, prior scored outputs, or holdout content.

During calibration, sealed Case 5 is inaccessible and must not be requested, read, discussed, quoted, summarized, or used as an example. Holdout execution is an external apparatus responsibility and may occur exactly once only after repeated Case 2 and Case 6 archetype passes under this exact finalized V81 contract and one bounded calibrated lineage.

If that lineage passes its one permitted sealed holdout, retire it before creating a brand-new saved agent from finalized V81 instructions only for clean-room verification. The fresh agent must have no access to prior agent sessions or holdout output.

## 18. Prohibitions

Do not expose hidden archetypes or evaluator findings to the worker. Do not use Case 5 during calibration. Do not promote candidate outputs, mint APA IDs, modify Oval Office research records, or write sovereign/admitted data. Do not perform database writes.
