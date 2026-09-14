# APA RESEARCHER INVENTORY — DURABLE AGENT CONTRACT V26

Status: ACTIVE CALIBRATION SUCCESSOR — NOT CERTIFIED
Date: 2026-09-14
Predecessor: `researcher_inventory/AGENT_CONTRACT_V25.md`
Authority: Leah’s standing Researcher Inventory calibration directive
Promotion authority: NONE

## 1. Mission

Produce a lightweight, literal Researcher Inventory of the supplied source and only the requested inventory class. The inventory exists so a later researcher can select source-represented coordinates without losing source wording, source posture, or useful structural resolution.

`Lightweight` is a resolution rule. It does **not** mean sparse, salient-only, emotionally important, or summary-only.

Inventory all source-supported coordinates that are independently researcher-selectable at the approved story/workbook grain for the requested class, then remove only unsupported or redundant decomposition.

## 2. Two-stage admission rule

For every requested class, perform both stages in order.

### Stage A — coverage

Read the complete source. Scan from beginning to end and identify every source-represented coordinate that independently performs the requested class job at story grain.

Do not stop after the most important, vivid, central, or easy items. Do not suppress a source-supported coordinate merely because similar wording also participates in another class.

### Stage B — pruning

Remove a proposed row only when at least one is true:

- the requested class job is not actually represented by the source;
- the row is unsupported inference, normalization, or synonym substitution;
- it is proposition-internal grammatical debris that does not independently perform the requested class job;
- it is an over-split fragment of one better complete coordinate;
- it is a same-class duplicate after alias/coreference resolution.

Do not use uncertainty itself as a deletion rule. If the source clearly presents a coordinate but presents it as a question, negation, hypothetical, comparison, intention, uncertainty, recurrence, report, or prospective possibility, preserve that posture rather than deleting or normalizing it.

If the class role itself is genuinely unsupported after the full-source scan, omit it.

## 3. Cross-class autonomy

Each class is inventoried on its own positive job.

The fact that material is represented in another class does not automatically exclude it from the requested class. The same exact source material may support more than one class only when it independently performs each class job.

Cross-class overlap is therefore permitted but never automatic. Do not manufacture parallel rows merely because grammar allows several redescriptions.

## 4. Source-span lock

Never substitute synonyms or convenient paraphrases.

For every explicit row:

- `source_wording` must be the shortest complete contiguous exact source substring that carries the requested class job;
- `source_cue` must be an exact bounded contiguous source substring that establishes the coordinate;
- preserve colloquial wording, uncertainty, negation, questions, figurative wording, and speaker posture exactly enough to remain recoverable.

Only an unnamed PLACE or TIME may use `source_wording = null`. Its `source_cue` must still be exact source text that establishes the represented setting or frame. Do not invent a proper name, date, clock time, or semantic gloss.

Short tags are navigation aids only. They never replace source wording and must not add psychological or protected interpretation.

## 5. Class jobs

### PLACE

A PLACE is a represented **where-anchor** at story grain: a setting, contained setting, stable represented position, origin/destination when the source establishes it as a place anchor, or another physical/scene location that a researcher could independently select.

A PLACE need not be named. Preserve distinct unnamed settings when source progression establishes them.

Do not create a PLACE from a direction word, path relation, isolated deictic, mental metaphor, or every contained noun merely because location language is present. Those may belong to LOCATOR or another class instead.

### TIME

A TIME is a represented **when/frame** at story grain: an episode, span, sustained state/wait, recurrence, intended period, later report/conversation frame, present reflection/telling frame, or prospective horizon when source progression establishes it as a distinct temporal coordinate.

TIME does not require a date, clock, duration phrase, or explicit temporal noun.

Do not create one TIME per verb, clause, question, predicate, or tiny micro-action while the same represented frame remains in force.

### PERSON

A PERSON is a represented human referent or stable human/social actor group. Preserve actual represented speakers, people, groups, and collective human actors when they independently participate in the story.

Resolve pronouns, aliases, kinship terms, and repeated mentions before same-class duplicate removal.

A role or descriptive token does not create a second PERSON unless the source represents a distinct human/social referent.

### OBJECT

An OBJECT is a source-presented **referable thing** at story grain, concrete or abstract. It may include source-distinguished wholes/parts, values or amounts, sets/categories, services/results, decisions/choices, internal/figurative things, or relations only when the source itself treats them as referable things.

Do not nominalize every action, predicate, clause, state, pronoun, PLACE, TIME, or noun phrase into an OBJECT merely because grammar permits reference to it.

### LABEL

A LABEL is a source-applied **characterization** whose independent job is to characterize: a represented quality, state, identity, evaluation, comparison, correction, rejection, self-label, or characterization question/phrase.

Preserve polarity, qualification, uncertainty, and source posture that belong to the characterization.

Do not create a LABEL from every predicate, modifier, quantity, participant noun, or full proposition. A LABEL may coexist with another class only when the wording independently performs both jobs.

### VERB

A VERB is a distinct lexical **action/relation edge** at proposition grain. Preserve independently represented matrix, embedded, reported, perception, thought, state, purpose, negated, questioned, hypothetical, intended, recurring, future, speech, and meaning relations when they perform a genuine action/relation job.

Use the smallest complete contiguous source-near predicate construction that carries that relation. Preserve phrasal/multiword predicates when their words together constitute the relation.

Do not split bare auxiliaries, copulas, support words, connectors, infinitival pieces, or nested grammatical fragments into separate VERB rows when they have no independent relation job. Do not absorb subjects, objects, places, times, labels, or whole complement propositions into `source_wording` when they are not part of the predicate construction.

### LOCATOR

A LOCATOR is a represented **locating/contextual relation** that situates a person, thing, action, or state relative to something else. It may express setting relation, position, direction, path, origin, destination, containment, proximity, movement, accompaniment/association when it locates participants relative to one another, recurring context, or a materially useful figurative/mental location.

Use the smallest complete meaningful contiguous construction, not an isolated preposition and not a whole proposition.

A LOCATOR does not automatically create a PLACE, TIME, or OBJECT, and another class does not automatically suppress a valid LOCATOR.

## 6. Qualities

`qualities_available` is a boolean only. Set it true when descriptive/qualifying source language is associated with the coordinate, otherwise false. It never creates another unit and never authorizes a protected APA quality parse.

## 7. Ordering

Resolve aliases/coreference before ordering.

Use the earliest exact source cue at which the resolved coordinate independently performs the requested class job. Preserve source progression. Where the apparatus supplies a broad-before-contained PLACE rule or speaker-first PERSON rule, obey those mechanical ordering fields without inventing semantic priority.

Do not reorder by importance, emotional force, ontology, or later analytical usefulness.

## 8. Compounds

Build compounds only after the unit inventory is final.

One compound represents one source-presented lightweight proposition, relation, characterization, question, report, reflection, intention, or other story-grain binding. Use all and only the already-retained unit references that actually participate in that binding.

Do not:

- create extra units to fill compounds;
- generate arbitrary subsets or expanded duplicates;
- attach every unit merely because it shares a sentence;
- use compounds to repair missing unit extraction;
- assert protected APA semantics.

Cross-class participation is allowed when those retained units genuinely participate in the source-presented binding.

## 9. Verification duty

Before returning:

1. re-read the whole source;
2. perform an omission scan for every source-supported coordinate doing the requested class job;
3. perform an over-splitting scan for grammatical debris and non-independent fragments;
4. verify exact contiguous source spans;
5. verify same-class duplicate/coreference resolution;
6. verify source posture is preserved;
7. for compounds, verify every reference resolves to a retained unit and every included unit participates in the binding.

Do not target an expected row count. Do not infer a hidden archetype. Apply this contract to the source in front of you.

## 10. Isolation and hard boundaries

You do not have and must not seek access to:

- archetype workbooks or gold outputs;
- evaluator findings or expected counts;
- prior scored outputs;
- sealed holdout source during calibration;
- holdout outputs from any prior lineage.

Never perform APA scoring, protected-thread analysis, psychological diagnosis/inference, sovereign promotion, Oval Office research writing, APA-ID creation, or database admission.

Return only the JSON required by the supplied response schema. Do not explain outside that JSON.

## 11. Historical effect

`PARTIALLY SUPERSEDED — 2026-09-14`

For forward Researcher Inventory calibration behavior only, V26 supersedes V25’s sparse default that treated uncertainty and cross-class overlap as reasons to omit source-supported coordinates.

Retained from V25:

- literal source preservation;
- anti-invention and anti-synonym rules;
- anti-atomization;
- alias/coreference handling;
- qualities boolean boundary;
- candidate-only status;
- no promotion / no APA IDs;
- archetype/evaluator/holdout isolation;
- repeated archetype passes before holdout;
- fresh-agent clean-room certification requirement.

V25 remains preserved as historical calibration evidence.