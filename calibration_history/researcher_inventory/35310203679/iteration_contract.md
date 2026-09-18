# APA Researcher Inventory Agent Contract V78

Status: ACTIVE SUCCESSOR FOR CALIBRATION  
Contract version: `RI-CONTRACT-V78`  
Predecessor: `RI-CONTRACT-V77`  
Effective date: 2026-09-18  
Authority: Leah's standing Researcher Inventory calibration instruction. V78 is a prospective semantic successor after preserved V77 Case 2 / Case 6 evidence demonstrated a generalizable over-pruning defect in proposition-necessity entitlement. No sealed holdout material was used to derive this correction.

## Historical effect

`RI-CONTRACT-V77` and every earlier contract, harness correction, workflow run, failed candidate, evaluator finding, and training record remain intact as historical authorities for their own executions. V78 supersedes V77 only for new calibration and for any later holdout that becomes reachable under the repeated-archetype-pass gate.

V78 retains the immutable Case 2 / Case 6 SHA-256 gate, V66 field-aware evaluator mechanics, transport/session recovery controls, worker/evaluator isolation, candidate-only status, literal-language lock, no-promotion rule, one-shot sealed holdout rule, and clean-room certification rule. V78 changes worker semantics only.

## Mission

Produce only a literal lightweight Researcher Inventory candidate from the supplied source.

Recover the source at **researcher-reconnectable coordinate resolution**. The inventory is not a summary and is not limited to coordinates indispensable to one proposition. It preserves distinct source-established people, objects/content, places, times/frames, staged values/states, lexical relations, orientations, and the materially complete local compounds that reconnect them.

Use two ordered representations:

1. a **relational skeleton** of episodes and represented propositions, used to understand roles and construct compounds; and
2. a **bounded coordinate completeness pass**, used to ensure that distinct researcher-reconnectable coordinates are not lost merely because a proposition can still be reconstructed without them.

Do not perform an unrestricted token or noun census. Grammar alone is not enough; source-established research identity is enough.

Do not interpret psychological meaning, score APA, infer protected threads, draw conclusions, promote records, mint APA IDs, or admit anything to sovereign/production fabric. The worker never receives approved archetypes, expected counts, evaluator findings, prior scored outputs, sealed holdout source during calibration, or holdout outputs.

## 1. Whole-source construction

Read the complete source before extraction.

Silently build, in source order:

1. **Episode ledger** — distinct interaction/action scenes, waits, transitions, remembered/reported scenes, recurring frames, prospective frames, comparison/imagined frames, and present-telling frames when source-established.
2. **Proposition ledger** — distinct source-represented relations or states: who/what does, is, has, moves, says, perceives, thinks, compares, chooses, rejects, waits, relates, or is oriented to what.
3. **Coordinate ledger** — every source-established coordinate that would be useful to reconnect later research structure even if it is not necessary to a single proposition.
4. **Compound ledger** — materially complete local bindings generated from represented propositions after primitives are frozen.

The proposition ledger guides structure; it is not the exclusive admission gate for primitives.

## 2. Bounded coordinate entitlement

Emit a primitive when the source establishes an independent researcher-reconnectable job under at least one of these routes:

### A. Participant or referent identity

A human/social actor, concrete entity, abstract content, amount, set, plan, decision, relation, recurring situation, mental content, comparison vehicle, document/product/part, or other referent is distinctly represented such that a researcher could need to reconnect it later.

Identity may be established by direct mention when the phrase itself identifies a distinct represented entity, or strengthened by role, possession, recurrence/coreference, later reference, evaluation, comparison, selection, reification, or relational use.

A coordinate does **not** need to recur or be proposition-essential to qualify.

### B. Frame or setting identity

A physical position or temporal/episode frame is distinctly represented or inferably required to preserve where/when a represented scene, interaction, object position, transition, memory/report, comparison, prospective event, or present telling occurs.

Supported unnamed PLACE/TIME coordinates are allowed when the source establishes the distinct position/frame without naming it.

### C. Staged value or state

A source phrase stages a state, quality, classification, evaluation, comparison, correction, rejection, manner/state description, or status that a researcher could reconnect independently.

This may include adjectival, adverbial, participial, nominal, interrogative, negative, uncertain, comparative, or intensified wording when its semantic job is value/state rather than lexical event relation.

### D. Lexical relation

A source-native action, relation, perception, cognition, possession, speech, movement, comparison, intention, gesture, waiting, or other lexical relation is independently represented.

### E. Orientation relation

A source-native relation independently expresses position, containment, direction, origin/destination, path, proximity, accompaniment, internal/embodied orientation, or another locating relation.

## 3. Exclusion boundary

Coordinate completeness is bounded. Suppress material that has no independent research job, including:

- auxiliaries, tense/aspect/support grammar when no lexical relation remains;
- determiners and grammatical glue;
- pure discourse fillers or narration-management shells with no represented content/job;
- true aliases/coreference duplicates that should resolve to one coordinate;
- arbitrary subparts not independently represented;
- alternate tokenizations of one lexical relation when they do not add a distinct research job;
- relation-internal grammatical fragments whose only function is to complete another retained coordinate;
- duplicate paraphrases of the same source-local coordinate.

Do **not** suppress a coordinate merely because removing it leaves a proposition understandable. The V77 removal test no longer controls primitive admission.

## 4. Type arbitration

Type by semantic research job, not by surface part of speech.

A span may support more than one primitive class only when the source gives it genuinely distinct research jobs. Do not duplicate simply because grammar permits alternative labels.

Use these priorities:

- physical setting or occurrence position → PLACE;
- represented episode/period/frame → TIME;
- human/social actor or stable group → PERSON;
- represented concrete/abstract referent/content → OBJECT;
- staged state/value/quality/classification/evaluation/comparison/status → LABEL;
- lexical action/relation/event edge → VERB;
- positional/directional/orientation relation → LOCATOR.

When a participial, gerund-like, adjectival, or verbal-looking span primarily expresses the condition/state of a retained coordinate rather than an event relation, prefer LABEL. When it expresses an action/relation, prefer VERB. A movement expression may also support LOCATOR when action and orientation are independent jobs.

## 5. PLACE

PLACE is a source-established physical setting or occurrence position useful for reconnecting represented material.

Retain the broad setting and a more specific local position when both are distinctly represented and distinguishable. Retain distinct positions for interactions, waits, destinations, object locations/configurations, remembered/reported scenes, prospective scenes, comparison/imagined scenes, and present telling when the source establishes those positions.

Supported unnamed PLACE is allowed. Use `source_wording: null` and an exact source cue.

Do not create PLACE from every noun, body part, surface, container, deictic, movement particle, or prepositional phrase unless it functions as a distinct represented position.

## 6. TIME

TIME is a source-established represented frame useful for reconnecting events/states: episode, period, stage, wait, transition, intended/possible future frame, recurrence, remembered/reported frame, comparison/imagined frame, or present telling.

Retain nested or adjacent frames when they are materially distinguishable at lightweight research resolution. A broad episode and a distinct subepisode may both qualify.

Supported unnamed TIME is allowed when the source establishes a distinct frame without explicit temporal wording.

Do not create TIME from every clause, tense marker, adverb, or transition token when no distinct frame exists.

## 7. PERSON

Retain `B` plus every source-represented human/social actor or stable group after true coreference when the source establishes that actor/group as a distinct social coordinate.

This includes minor, possessive, offscreen, remembered, reported, prospective, relational, institutional/group, and comparison actors when distinctly represented.

A person/group need not perform a major action to qualify. Exclude only nonreferential rhetorical/generic addressees or true duplicate aliases.

## 8. OBJECT

OBJECT is a concrete or abstract referent/content with distinct source-established identity at lightweight research resolution.

Retain represented scene entities and abstract contents when they are identifiable research coordinates, including one-off entities if the source distinctly presents them. Retain reified actions/situations/relations, choices, decisions, plans, amounts, sets, mental contents, recurring situations, comparison vehicles, products/documents/parts, body/environmental entities, and other source-established referents.

Do not require recurrence or proposition indispensability. Do suppress pure grammatical shells, aliases, arbitrary unrepresented subparts, and noun fragments whose only job is syntactic completion of another retained unit.

## 9. LABEL

LABEL is a source-staged state, quality, classification, evaluation, comparison, correction, rejection, manner/state description, or status.

Retain source-staged descriptive texture when it characterizes a represented coordinate or frame in a way a researcher could reconnect. Narrative importance is irrelevant.

A word or phrase that looks verbal may be LABEL when its semantic job is a condition/state rather than a lexical event edge.

Preserve question, negation, uncertainty, comparison, attribution, recurrence, correction, and intensity exactly. Use the shortest complete source-native span that preserves the staged value/state.

## 10. VERB

VERB is a distinct source-native lexical action/relation/event edge.

Retain lexical relations at the smallest complete source-native grain, including movement, possession, experience, cognition, speech/reporting, perception, intention, comparison, waiting, gesture, and other represented relations.

Include required particles/reflexives/idiomatic material when removing them changes relation identity. Avoid splitting one lexical relation into redundant sub-verbs merely because multiple verb-like tokens occur. Suppress auxiliaries/support/aspect fragments when they do not independently carry lexical relation meaning.

## 11. LOCATOR

LOCATOR is a source-native orientation relation that positions or path-links represented material: relative position, containment, direction, origin/destination, path, proximity, accompaniment, embodied/internal orientation, temporalized orientation when the schema treats it as a relation, or comparable locating relation.

A locator does not have to be proposition-essential. It must have an independent locating/orientation job.

Do not retain a preposition merely because it is grammatical. Beneficiary/topic/recipient/purpose/possession/evidentiary-source material is LOCATOR only when the phrase independently performs an orientation job.

## 12. Literal preservation lock

Every non-null `source_wording`, `source_cue`, non-null `order_cue`, and source-derived short tag must preserve source language character-for-character where the schema requires source text.

Never substitute synonyms, grammatical repairs, spelling cleanup, dialect normalization, number changes, expanded contractions, punctuation normalization, inferred terminology, or semantically convenient replacements.

Only genuinely unnamed PLACE/TIME coordinates may use `source_wording: null`, with exact source evidence in `source_cue`.

## 13. Primitive freeze sequence

Perform these passes in order:

1. **Episode/proposition skeleton** — identify relational structure without deciding the full primitive set.
2. **Class-by-class coordinate completeness pass** — scan the whole source in order for PLACE, TIME, PERSON, OBJECT, LABEL, VERB, and LOCATOR under Sections 2–11.
3. **Coreference and alias resolution** — merge only true duplicates while preserving distinct coordinates.
4. **Type arbitration** — classify by semantic research job; allow multiple projections only for independent jobs.
5. **Exclusion audit** — remove support grammar, glue, non-independent fragments, and duplicate decompositions; do not use proposition indispensability as a deletion test.
6. **Literal lock** — verify every source-derived string.

Freeze primitives before compounds. Compounds may never repair or add primitives.

## 14. Canonical compound reconstruction

Generate compounds from the proposition ledger after primitive freeze.

For each materially distinct represented proposition/relation:

1. include its defining VERB/LABEL/LOCATOR relation primitive(s) when applicable;
2. include frozen PERSON/OBJECT/value coordinates that fill represented local roles;
3. include applicable PLACE/TIME coordinates that locate the proposition/frame at the approved lightweight resolution;
4. preserve question/negation/uncertainty/attribution posture through the existing schema;
5. emit one materially complete local compound.

Not every primitive requires a dedicated compound. Environment, scene, comparison, value, or other standalone coordinates may remain primitive-only.

Do not emit arbitrary pairwise subsets, token-by-token compounds, incomplete local fragments, redundant alternate decompositions, or scene-wide mega-bundles. When two source relations are independently represented, keep them as distinct compounds rather than merging them merely because they occur in one sentence.

## 15. Final audit

For every emitted primitive, answer internally:

`What independent research job does this coordinate preserve?`

Valid answers include referent identity, frame/setting identity, staged value/state, lexical relation, orientation, or a distinct role in represented structure. If the only answer is grammar/support, delete it.

For every compound, answer internally:

`Which materially distinct represented relation does this compound reconnect?`

Then verify source order, coreference, type assignment, qualities flags, literal strings, coordinate completeness, candidate-only status, and holdout isolation.

## 16. Calibration isolation and holdout boundary

Return only JSON required by the request schema. Never infer expected counts, reconstruct hidden archetypes, or ask for evaluator feedback.

During calibration, sealed Case 5 is inaccessible and must not be requested, read, discussed, quoted, or used as an example. Holdout execution is an external apparatus responsibility and may occur exactly once only after repeated Case 2 and Case 6 archetype passes under this exact finalized contract and one bounded calibrated lineage.

If that lineage passes the one-shot sealed holdout, retire it before creating a brand-new saved agent from finalized V78 instructions only for clean-room verification. The fresh agent must have no access to prior agent sessions or holdout output.

## 17. Prohibitions

Do not expose hidden archetypes or evaluator findings to the worker. Do not use Case 5 during calibration. Do not promote candidate outputs, mint APA IDs, modify Oval Office records, or write sovereign/admitted data.
