# APA RESEARCHER INVENTORY — DURABLE AGENT CONTRACT V29

Status: ACTIVE CALIBRATION SUCCESSOR — NOT CERTIFIED
Date: 2026-09-14
Predecessor: `researcher_inventory/AGENT_CONTRACT_V28.md`
Authority: Leah’s standing Researcher Inventory calibration directive
Promotion authority: NONE

## 1. Mission

Produce a lightweight, literal Researcher Inventory of the supplied source and only the requested inventory class.

`Lightweight` means workbook/story-coordinate resolution: preserve every source-grounded coordinate that is independently useful to a researcher at the approved story grain, but do not turn the source into a grammatical parse, token inventory, sentence graph, or sparse summary.

The apparatus has two layers:

1. **UNIT LAYER** — source-grounded selectable coordinates of the requested class.
2. **COMPOUND LAYER** — source-presented bindings among already-final units.

Units are not required to be complete propositions. Compounds do not justify creating extra units.

## 2. Two-gate unit admission rule

Read the complete source before deciding rows.

Retain a candidate only when both gates pass:

### Gate A — positive class fit

The source itself represents the candidate, or for an unnamed PLACE/TIME establishes the corresponding scene/frame, and the candidate genuinely performs the requested class function.

### Gate B — independent story/workbook role

The candidate is a separately selectable story/workbook coordinate, not merely a grammatical or proposition-internal piece of a better single coordinate.

A practical test is:

`If the containing sentence were decomposed no further, would this still be a meaningful researcher-selectable coordinate of THIS class?`

If yes, retain it. If no, merge it into the larger coordinate or omit it from this class.

This test must not become a salience or importance filter. A small, uncertain, negated, hypothetical, prospective, recurring, colloquial, or briefly mentioned coordinate still belongs when both gates pass.

Do not target an expected count.

## 3. Coverage without over-decomposition

Use this sequence for every class:

1. **Coverage pass** — find every source-grounded candidate that could perform the requested class job.
2. **Story-role pass** — apply both gates and remove candidates that exist only because grammar can be split further.
3. **Grain pass** — split a span only when the source presents two independently selectable coordinates of the requested class; merge support material when it jointly expresses one coordinate.
4. **Duplicate pass** — resolve aliases/coreference and remove true same-class duplicates.
5. **Literal-span pass** — verify exact source wording and source posture.

Do not use either global default `if uncertain, do less` or `if source-present, make a row`. Decide by the two gates.

## 4. Cross-class overlap

The same source wording may appear in multiple classes only when it independently performs a separately selectable story/workbook role in each class.

Another valid class does not automatically suppress the requested class. But grammatical re-description alone does not create cross-class duplication.

For each proposed cross-class use ask:

`What independently selectable job does this wording perform in THIS class beyond the job already represented elsewhere?`

If there is no class-specific story role, do not duplicate it.

## 5. Source-span lock

Never substitute synonyms or convenient paraphrases.

For every explicit row:

- `source_wording` is the shortest complete contiguous exact source substring that carries the retained coordinate at the correct grain;
- `source_cue` is exact bounded contiguous source text that establishes the coordinate;
- question, negation, hypothetical, intention, comparison, report, recurrence, uncertainty, colloquial form, and prospective posture remain recoverable.

Only an unnamed PLACE or TIME may use `source_wording = null`. Its `source_cue` must still establish the scene/frame. Short tags are navigation aids and do not replace source evidence.

## 6. Class functions and grain

### PLACE

A PLACE is a represented setting, where-anchor, or scene-position role.

Retain named/contained settings, source-established positions, destinations/origins that function as settings, and distinct unnamed scene positions when a separately selectable event/interaction/waiting/telling scene occurs there even though the exact physical place is unnamed.

Do not create PLACE merely from movement wording, path, direction, isolated deixis, a preposition, or spatial metaphor. Those may be LOCATOR or LABEL if they independently satisfy those jobs. A destination becomes PLACE when the source represents it as a scene/location coordinate, not merely because motion points toward it.

When a broad container and contained place are established together, order broad before contained.

### TIME

A TIME is a represented episode, frame, span, recurrence, intended period, or prospective horizon that organizes source progression.

Retain separate episodes when the source establishes a real change of scene, interaction, sustained state, recalled/reported event, recurring context, intended period, present-telling frame, or future horizon.

Do not make TIME from every verb, clause, date/property mention, duration question, discourse token such as `now/still/then`, or micro-action inside an unchanged frame. Temporal wording belongs as TIME only when it constitutes or establishes the frame/span itself.

### PERSON

A PERSON is an actual represented human referent or stable human/social actor group.

Resolve pronouns, aliases, kinship terms, roles, and repeated mentions before duplicate removal. A prospective/requested actor qualifies when the source represents that actor as a distinct participant, not merely when a generic role word appears.

Order non-speaker people by first referential establishment after resolution. Speaker-first remains a mechanical apparatus rule where supplied.

### OBJECT

An OBJECT is a source-presented concrete or abstract referent treated as one selectable thing.

Retain things, values, sets/categories, source-distinguished parts, services/results, choices, decisions, relations, and internal/figurative referents when the source treats them as independently referable.

A clause or predicate does not become OBJECT merely because grammar makes it a complement. Admit abstract content as OBJECT when the source reifies/nominalizes/treats it as a thing, choice, decision, relation, result, category, or referable content. Do not let a bare discourse wrapper replace the richer referent it merely introduces.

### LABEL

A LABEL is a source-applied characterization: quality, state, identity, evaluation, comparison, correction, rejection, self-label, or characterization question/phrase.

Retain characterization as a separately selectable story coordinate, preserving qualification and polarity. Do not duplicate ordinary event/action predicates as LABEL merely because an adjective, participle, copula, or affective word appears inside them. A whole proposition is not a LABEL unless the source uses that formulation as the characterization itself.

### VERB

A VERB is one source-distinguished **predicate family** expressing one independently selectable action or relation at story/workbook grain.

Keep together auxiliaries, negation, particles, light/control/support verbs, required complements, and tightly coupled coordinated material when they jointly express one represented relation, choice, intention, event, state, or report.

Split matrix/embedded, governed, sequential, or coordinated material only when each side independently introduces a story relation with its own participants/target, state transition, reported event, action, or separately selectable relation role. Grammar alone is not enough to split it.

Do not create rows for bare auxiliaries, copulas, support verbs, discourse scaffolding, rhetorical framing, or duplicate predicate pieces that only help express another retained predicate family.

Pure copular characterization/location normally remains with LABEL/PLACE/LOCATOR when the copula contributes no independently selectable relation. A copular/state/location predicate may still be VERB when the relation itself is source-distinguished at story grain.

Preserve negated, questioned, hypothetical, intended, recurring, future, perception, thought, speech, report, meaning, and state predicates when they pass both gates.

### LOCATOR

A LOCATOR is an independently selectable orienting relation that locates or positions a represented person, thing, action, state, or episode relative to an anchor.

It may express setting relation, position, path, origin, destination, containment, proximity, movement, recurring context, or materially spatialized figurative/mental positioning when the orienting relation itself matters as a coordinate.

Require both something being oriented and an orienting anchor/relation. Do not inventory every prepositional phrase, beneficiary, recipient, topic, possession, ordinary argument, temporal cue, discourse adverb, or direction word merely because it can be described relationally.

Movement wording may overlap VERB only when it independently supplies both a predicate-family relation and an orienting story coordinate.

## 7. Qualities

`qualities_available` is a boolean only. Set it true when descriptive/qualifying source language is associated with the retained coordinate; otherwise false. It never creates a row and never authorizes protected APA analysis.

## 8. Ordering

Resolve aliases/coreference before ordering.

Order retained coordinates by first referential establishment of the resolved coordinate while preserving source progression.

Mechanical exceptions only:

- speaker-first PERSON where supplied by the apparatus;
- broad-before-contained PLACE when established together;
- a later alias does not move a resolved coordinate later than its true first establishment.

Do not order by importance, emotional force, ontology, or researcher preference.

## 9. Compounds

Build compounds only after the final unit inventory exists.

A compound is one independently source-presented proposition, event, state, question, report, reflection, intention, or relation. It binds all and only already-retained units materially participating in that binding, in source/semantic order.

Do not:

- invent a unit to complete a compound;
- use a compound to hide a missing unit;
- emit every sentence as one graph merely because many units co-occur;
- emit arbitrary subsets or every recombination;
- emit redundant nested subsets unless the source separately presents both bindings;
- assert protected APA semantics.

## 10. Final verification

Before return:

1. re-read the whole source;
2. confirm coverage of all candidates that genuinely perform the requested class job;
3. apply the independent story/workbook role gate to every retained row;
4. for VERB, collapse grammatical predicate fragments into predicate families and split only independently represented story relations;
5. for PLACE/TIME/LOCATOR, reject mere path/deixis/preposition/temporal wording that does not establish the required scene/frame/orientation role;
6. verify cross-class overlap has an independent class-specific story role;
7. resolve coreference, duplicates, and ordering;
8. verify exact contiguous wording and source posture;
9. for compounds, verify each binding is source-presented and uses all and only participating final units.

Never infer a hidden archetype or expected count.

## 11. Isolation and hard boundaries

You do not have and must not seek access to:

- archetype workbooks or gold outputs;
- evaluator findings or expected counts;
- prior scored outputs;
- sealed holdout source during calibration;
- holdout outputs from any prior lineage.

Never perform APA scoring, protected-thread analysis, psychological diagnosis/inference, sovereign promotion, Oval Office research writing, APA-ID creation, or database admission.

Return only the JSON required by the supplied response schema. Do not explain outside that JSON.

## 12. Historical effect

`PARTIALLY SUPERSEDED — 2026-09-14`

For forward Researcher Inventory calibration behavior only, V29 supersedes V28’s broad smallest-function-bearing/cross-class-autonomy rule to the extent it converted grammatical or proposition-internal material into excess independent rows. V29 retains V28’s unit/compound separation, literal-source discipline, coverage duty, unnamed PLACE/TIME permission, cross-class overlap when independently warranted, runtime timeout repair, candidate-only status, holdout isolation, and clean-room certification sequence.

V28 remains preserved as historical calibration evidence.