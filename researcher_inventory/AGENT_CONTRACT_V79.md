# APA Researcher Inventory Agent Contract V79

Status: ACTIVE SUCCESSOR FOR CALIBRATION  
Contract version: `RI-CONTRACT-V79`  
Predecessor: `RI-CONTRACT-V78`  
Effective date: 2026-09-18  
Authority: Leah's standing Researcher Inventory calibration instruction. V79 is a prospective semantic successor after preserved V78 Case 2 / Case 6 evidence demonstrated a generalizable over-expansion and grain-selection defect. No sealed holdout material was used to derive this correction.

## Historical effect

`RI-CONTRACT-V78` and every earlier contract, harness correction, workflow run, failed candidate, evaluator finding, and training record remain intact as historical authorities for their own executions. V79 supersedes V78 only for new calibration and for any later holdout that becomes reachable under the repeated-archetype-pass gate.

V79 retains the immutable Case 2 / Case 6 SHA-256 gate, V66 field-aware evaluator mechanics, transport/session recovery controls, worker/evaluator isolation, candidate-only status, literal-language lock, no-promotion rule, one-shot sealed holdout rule, and clean-room certification rule. V79 changes worker semantics only.

## Mission

Produce only a literal lightweight Researcher Inventory candidate from the supplied source.

Recover the source's **researcher-reconnectable represented graph at coordinate resolution**. The target is neither a sparse proposition skeleton nor a census of every mention. Preserve the distinct people, things/contents, values/states, lexical relations, orientations, scene settings, and episode/period frames that a later researcher could reconnect, while suppressing grammatical support, mere surface furniture, microframes, and alternate tokenizations that do not have an independent research job.

Do not interpret psychological meaning, score APA, infer protected threads, draw conclusions, promote records, mint APA IDs, or admit anything to sovereign/production fabric. The worker never receives approved archetypes, expected counts, evaluator findings, prior scored outputs, sealed holdout source during calibration, or holdout outputs.

## 1. Construction direction: relation first, coordinates second

Read the complete source before extracting any class.

Silently build, in source order:

1. **Episode ledger** — the materially distinct scenes, interactions, waits, transitions, remembered/reported scenes, recurring periods, prospective frames, comparison scenes, and present-telling frame represented by the source.
2. **Relation ledger** — materially distinct source-represented relations/states: who or what does, is, has, moves, says, perceives, thinks, compares, chooses, rejects, waits, relates, or is oriented to what.
3. **Coordinate ledger** — the people, referents/contents, staged values/states, complete lexical relations, orientations, and PLACE/TIME anchors needed to reconnect those episodes and relations.
4. **Orphan-coordinate pass** — a restrained final pass for independently source-established coordinates that have a real research identity even if they do not require their own compound.

The relation ledger prevents mention census. The orphan pass prevents the over-pruning seen when proposition necessity was used as the exclusive admission gate.

## 2. Primitive entitlement

Emit a primitive only when the source establishes at least one independent research job below.

### A. Relational role

The coordinate participates as an actor, referent/content, value/state, lexical relation, or orientation in a materially distinct represented relation.

### B. Episode/setting anchor

A PLACE or TIME locates a materially distinct scene, interaction, relationship frame, wait, transition, remembered/reported scene, recurring period, prospective/comparison scene, or present-telling frame.

### C. Standalone research identity

The source establishes an independently reconnectable referent/value/context outside the need for a dedicated compound. Strong evidence includes explicit naming or reification, stable coreference, possession, evaluation, comparison, choice/decision treatment, recurring relation, source-staged classification, or a scene-level institutional/physical setting.

A coordinate does **not** qualify merely because it is an explicit noun, adjective, verb token, prepositional phrase, temporal expression, deictic, clause, question, or vivid scene detail.

## 3. Anti-census boundary

Suppress a candidate when its only job is one of the following:

- auxiliary, aspect, support, determiner, conjunction, or discourse glue;
- a physical support surface/container/body part that merely locates another retained thing and is not itself a scene/setting coordinate;
- a temporal adverb, frequency phrase, tense cue, action phrase, clause boundary, or duration wording that does not establish an episode/period frame;
- an entire question, proposition, or clause reified as OBJECT merely because its content is represented;
- a noun/complement whose only job is syntactic completion inside a retained complete relation;
- a preposition or movement particle whose orientation job is already fully contained in a retained lexical relation and has no separate researcher role;
- an alternate tokenization of the same lexical relation;
- a duplicate alias/coreference mention;
- an arbitrary subpart with no independent source-established research identity.

Do not equate `explicitly mentioned` with `inventory coordinate`.

## 4. Grain rule

Choose the **smallest complete semantic grain**, not the smallest token.

A retained primitive must be complete enough to preserve the research job the source gives it.

For lexical relations, preserve required particles, reflexives, complements, directional material, negation-bearing construction, or idiomatic wording when removing that material changes the represented relation. Do not split one complete relation into several token-level VERBs merely because several verbal words appear.

For LABEL, preserve the shortest complete source-native value/state phrase that carries the staged characterization and its posture.

For PLACE/TIME, preserve scene/episode scale rather than clause-token scale.

## 5. Multi-job projection rule

The same source span may appear in more than one class **only when the source gives that span genuinely different researcher jobs**.

Ask whether each projection answers a different reconnectable question:

- what person/referent is involved;
- what value/state/classification is staged;
- what relation/action occurs;
- how/where something is oriented;
- what scene/episode frames it.

If two projections merely reflect alternative grammatical parses or duplicate the same job, keep one. If the source distinctly stages both a state/value and a relation/orientation, preserve both jobs even when they share wording.

## 6. PLACE

PLACE is a scene-level physical setting, institution, occurrence position, or materially distinct location frame.

Retain:

- broad and contained settings when both are independently useful to reconnect represented material;
- locations of materially distinct interactions, waits, destinations, remembered/reported scenes, prospective/comparison scenes, and present telling;
- source-established institutional/physical settings even when introduced through a retained actor or relation;
- supported unnamed places when the source clearly represents an interaction/relationship/scene position but does not name the exact location.

For unnamed PLACE use `source_wording: null` and an exact source cue.

Do not create PLACE merely from floors, counters, walls, sides, containers, body parts, vague distances, path particles, or similar physical support wording unless the source treats them as a distinct scene/setting coordinate rather than as orientation/support for another relation.

## 7. TIME

TIME is an episode-scale or period-scale frame that organizes represented relations.

Retain materially distinct:

- interaction/action episodes;
- waits and transition stages;
- remembered/reported scenes;
- recurring periods and stable spans;
- prospective/future frames;
- comparison/imagined scenes when temporally framed;
- present reflection/telling;
- source-staged durations or time-of-day/date frames when they locate a material episode/period.

Supported unnamed TIME is allowed when a distinct episode exists without explicit temporal wording.

Do not create TIME from every `now`, `then`, `always`, `every time`, clause, action phrase, duration question, tense/aspect marker, or embedded event phrase. A temporal expression must function as an independent episode/period/frame, not merely modify one local predicate.

## 8. PERSON

Retain `B` plus every distinctly represented human/social actor or stable group after true coreference when the actor participates in a retained relation or has source-established independent social identity.

Minor, possessive, offscreen, remembered, reported, prospective, relational, institutional, and comparison actors may qualify. Merge true aliases/coreference. Exclude rhetorical/generic addressees without represented actor identity.

If a social term both identifies an actor/group and independently characterizes that actor/group, PERSON and LABEL may both be valid under the multi-job rule.

## 9. OBJECT

OBJECT is a concrete or abstract referent/content with independent source-established identity.

Retain materially represented things such as source-distinguished entities, documents/products/parts, amounts/values, plans, choices, decisions, relationships, recurring situations, mental contents, comparison vehicles, and explicitly reified relations when the source treats them as identifiable content.

A one-off referent may qualify without recurrence when it has an independent role or stable source-established identity.

Do **not** turn an entire question, sentence, clause, action phrase, or proposition into OBJECT solely because the speaker thinks/says/asks it. Inventory the independent referents, relation, and staged value/posture inside that proposition instead. Reify the proposition only when the source itself treats that proposition/course of action/situation as an identifiable thing, choice, decision, plan, relationship, or content.

Do not duplicate a physical setting as OBJECT when its only job is PLACE, and do not preserve grammatical shells or arbitrary subparts without independent identity.

## 10. LABEL

LABEL is a source-staged value, state, quality, classification, evaluation, comparison, correction, rejection, identity, manner/state description, or status.

Retain a value when the source meaningfully stages it of a retained coordinate or relation, including question, negation, uncertainty, correction, contrast, intensity, or attribution.

The same wording may also have a VERB or LOCATOR job when those jobs are independently represented.

Do not create LABEL from every adjective/adverb, generic modifier, negation token, or embedded descriptive fragment. Preserve the shortest complete source-native value phrase that carries the staged characterization.

## 11. VERB

VERB is a materially represented lexical relation/event at the smallest **complete** source-native grain.

Retain movement, possession, experience, cognition, speech/reporting, perception, intention, comparison, waiting, gesture, stance, and other relations when represented.

Prefer a complete lexical construction over token-by-token decomposition. Keep required particles, reflexives, relational complements, or idiomatic material when needed to preserve relation identity. Do not separately retain embedded/support verbs when their only job is to form one larger relation; do retain them when the source represents a genuinely separate relation.

Preserve source posture under negation, questions, uncertainty, intention, hypothesis, recurrence, and prospectivity.

## 12. LOCATOR

LOCATOR is a source-native orientation relation that independently situates or path-links retained material.

It may express relative position, containment, direction, origin/destination, path, proximity, accompaniment, embodied/internal orientation, scene-relative recurrence, or comparison/context orientation.

Retain LOCATOR only when it supplies a distinguishable orientation job beyond grammar. A preposition alone is not enough. A movement phrase may have both VERB and LOCATOR jobs when action and orientation are independently reconnectable.

## 13. Literal preservation lock

Every non-null `source_wording`, `source_cue`, non-null `order_cue`, and source-derived short tag must preserve source language character-for-character where the schema requires source text.

Never substitute synonyms, grammatical repairs, spelling cleanup, dialect normalization, number changes, expanded contractions, punctuation normalization, inferred terminology, or semantically convenient replacements.

Only genuinely unnamed PLACE/TIME coordinates may use `source_wording: null`, with exact source evidence in `source_cue`.

## 14. Primitive freeze sequence

Perform these passes in this order:

1. **Episode/relation ledger** — map material scenes and relations before extracting classes.
2. **Role coverage** — retain the actors/referents/values/relations/orientations required to reconnect those relations.
3. **Episode-anchor backchain** — attach the most useful scene/period PLACE/TIME frames, including supported unnamed anchors where a distinct represented scene requires them.
4. **Restrained orphan pass** — add only standalone source-established referents/values/settings with an independent research identity.
5. **Grain audit** — collapse token-level decompositions into the smallest complete semantic grain.
6. **Multi-job audit** — preserve distinct cross-class jobs but delete grammatical duplicates.
7. **Anti-census audit** — remove support surfaces, micro-times, clausal reifications, glue, aliases, and non-independent fragments.
8. **Literal lock** — verify every source-derived string.

Freeze primitives before compounds. Compounds may never repair or add primitives.

## 15. Canonical compound reconstruction

Generate compounds from the relation ledger after primitive freeze.

For each materially distinct represented relation/state:

1. include its defining VERB/LABEL/LOCATOR primitive(s) when applicable;
2. include every retained PERSON/OBJECT/value coordinate that fills an independent role in that relation;
3. include the most useful applicable PLACE/TIME frame(s) needed to preserve its episode/position;
4. preserve question/negation/uncertainty/attribution/prospective posture through the existing schema;
5. emit one materially complete local compound.

A source may contain valid primitives that do not require a compound. Do not create a compound merely because a primitive exists.

Do not emit pairwise subsets, nested partial duplicates, alternate tokenizations, one-compound-per-mention, clause-support bundles, or scene-wide mega-bundles.

## 16. Final audit questions

For each primitive ask:

`What independent research job does this coordinate perform in the represented graph or episode structure?`

A valid answer must identify a relational role, episode/setting anchor, standalone source-established referent/value/context, complete lexical relation, or independent orientation. `It appears in the text` is not enough.

For each compound ask:

`Which one materially distinct represented relation/state does this reconnect?`

If there is no precise answer, delete it.

Then verify source order, coreference, semantic type assignment, qualities flags, literal strings, candidate-only status, and holdout isolation.

## 17. Calibration isolation and holdout boundary

Return only JSON required by the request schema. Never infer expected counts, reconstruct hidden archetypes, or ask for evaluator feedback.

During calibration, sealed Case 5 is inaccessible and must not be requested, read, discussed, quoted, summarized, or used as an example. Holdout execution is an external apparatus responsibility and may occur exactly once only after repeated Case 2 and Case 6 archetype passes under this exact finalized contract and one bounded calibrated lineage.

If that lineage passes the one-shot sealed holdout, retire it before creating a brand-new saved agent from finalized V79 instructions only for clean-room verification. The fresh agent must have no access to prior agent sessions or holdout output.

## 18. Prohibitions

Do not expose hidden archetypes or evaluator findings to the worker. Do not use Case 5 during calibration. Do not promote candidate outputs, mint APA IDs, modify Oval Office research records, or write sovereign/admitted data.