# APA RESEARCHER INVENTORY — DURABLE AGENT CONTRACT V30

Status: ACTIVE CALIBRATION SUCCESSOR — NOT CERTIFIED
Date: 2026-09-14
Predecessor: `researcher_inventory/AGENT_CONTRACT_V29.md`
Authority: Leah’s standing Researcher Inventory calibration directive
Promotion authority: NONE

## 1. Mission

Produce a lightweight, literal Researcher Inventory of the supplied source and only the requested inventory class.

The inventory has two layers:

1. **UNIT LAYER** — source-distinguished semantic coordinates of the requested class.
2. **COMPOUND LAYER** — source-presented bindings among already-final units.

`Lightweight` means preserve the source’s usable semantic resolution without turning it into either a grammatical/token parse or a sparse summary.

A UNIT may be small. It does not need to be important enough to summarize or large enough to form a proposition by itself. It must, however, do a real semantic job of the requested class rather than exist only because grammar can be subdivided.

## 2. Unit admission rule

Read the complete source before deciding rows.

Retain a candidate when all are true:

1. **Source distinction** — the source explicitly presents the candidate, or for an unnamed PLACE/TIME establishes the corresponding scene-position/frame.
2. **Positive class function** — the candidate genuinely performs the requested class job.
3. **Semantic separability** — the candidate contributes a distinct semantic coordinate that can participate in a source-presented binding, or is itself a directly source-applied referent, characterization, scene/frame, person, or orientation.
4. **No grammatical debris** — it is not merely an article, connector, bare auxiliary, generic wrapper, support fragment, duplicated alias, or proposition-internal fragment with no separate semantic job.

The correct grain is the **smallest complete source-distinguished semantic coordinate**, not the largest independently tellable story unit and not the smallest grammatically labelable fragment.

Do not target an expected count.

## 3. Coverage and grain procedure

For every requested class perform these passes in order:

1. **Coverage pass** — identify every source-grounded candidate that may perform the class job, including brief, negated, questioned, hypothetical, prospective, recurring, colloquial, or uncertain material.
2. **Positive-function pass** — ask what semantic job the candidate performs in THIS class.
3. **Minimal-complete-grain pass** — split when the source presents distinct semantic coordinates; keep together words required to express one coordinate.
4. **Debris/reification pass** — remove rows created only by grammatical possibility, unsupported nominalization, generic discourse wrappers, or proposition-sized re-description.
5. **Coreference/duplicate pass** — resolve aliases before duplicate removal.
6. **Literal-span/order pass** — verify exact source wording, posture, and first referential establishment.

A small coordinate is not debris merely because it occurs inside a larger proposition. A larger phrase is not automatically a coordinate merely because it can be paraphrased as a thing, state, event, or relation.

## 4. Cross-class overlap

The same source wording may appear in more than one class when it genuinely performs more than one positive semantic function.

Classify each requested class positively. Do not use a winner-takes-all rule.

But do not create a parallel row merely because the same grammar can be redescribed under another class name. For each overlap ask:

`What distinct semantic job does this source wording perform in THIS class?`

If there is no positive class-specific job, omit that class use.

## 5. Source-span lock

Never substitute synonyms or convenient paraphrases.

For every explicit row:

- `source_wording` is the shortest complete contiguous exact source substring that carries the retained coordinate;
- `source_cue` is exact bounded contiguous source text establishing it;
- question, negation, hypothetical, intention, comparison, report, recurrence, uncertainty, colloquial form, and prospective posture remain recoverable.

Only an unnamed PLACE or TIME may use `source_wording = null`; its exact `source_cue` must establish the scene-position/frame.

Short tags are navigation aids only. They do not replace source evidence.

## 6. Class functions

### PLACE

A PLACE is a represented setting, physical/scene position, destination/origin position, or where-slot.

Retain named/contained settings and distinct unnamed scene positions established by source events, interactions, waiting/standing positions, later conversations, transitions, present telling, or positioned people/things even when the exact physical place is unspecified.

A deictic or movement phrase can support PLACE when it actually establishes where a represented person, thing, or occurrence is positioned. Do not create PLACE from a direction/path word or spatial metaphor that does not establish a place/position role.

A single broad physical setting may contain more than one separately represented scene-position. Order broad before contained when established together.

### TIME

A TIME is a represented episode, phase, frame, span, recurrence, intended period, present-telling period, or prospective horizon.

Retain source-distinguished changes of episode/phase when an action, interaction, waiting/state period, report/recollection, recurring context, intended period, or future situation establishes a new temporal coordinate. Consecutive event phases may each be TIME when the source distinguishes them.

Do not create TIME from every verb, bare temporal token, property/date mention, or question about duration unless that material itself establishes a represented time/frame.

### PERSON

A PERSON is an actual represented human referent or stable human/social actor group.

Resolve pronouns, aliases, kinship terms, role descriptions, and repeated mentions before duplicate removal. A prospective/requested actor qualifies when the source represents that actor as a distinct participant, not merely because a generic role word appears.

Order non-speaker people by first referential establishment after resolution. Speaker-first remains a mechanical apparatus rule where supplied.

### OBJECT

An OBJECT is a source-presented concrete or abstract referent treated as a selectable thing, content, value, relation, choice, decision, result, category, or distinguished part.

Retain abstract material only when the source treats that material itself as referable. Do not convert a clause, predicate, characterization, event, or whole proposition into OBJECT merely because grammar permits nominalization or because the phrase can be discussed.

Prefer the actual content-bearing referent over a generic wrapper such as a bare `thing`, `point`, `part`, or reporting shell when the wrapper merely introduces richer content.

### LABEL

A LABEL is a source-applied characterization, quality, state, identity, evaluation, comparison, correction, rejection, self-label, or characterization question/response.

Retain the shortest complete source formulation that carries the characterization, including brief or qualified formulations when the source applies them as characterizations.

Do not duplicate an ordinary action/relation as LABEL merely because it contains an adjective, participle, affect word, copula, or status-like wording. The source must be doing characterization work.

### VERB

A VERB is one source-distinguished **relation edge**: an action, state relation, perception, thought, speech/report, meaning relation, possession, location/copular relation, movement, intention, purpose, request, question-governed action, or other predicate relation represented by the source.

Use the smallest complete contiguous predicate span carrying one relation edge.

Split matrix/embedded, coordinated, sequential, perception/complement, report, purpose/infinitival, control, and movement constructions when the source presents more than one distinct relation edge. A relation may be small and still qualify even when nested inside a larger source proposition.

Keep auxiliaries, negation, particles, and required support words with the relation edge they express. Do not emit bare auxiliaries, bare copulas, support fragments, discourse scaffolding, or a longer construction that merely bundles several separately represented relation edges.

A copular/location/state relation can be VERB when the relation itself is source-distinguished; overlap with PLACE/LABEL/LOCATOR does not suppress a genuine relation edge.

### LOCATOR

A LOCATOR is a source-distinguished orienting/context relation that situates a represented person, thing, action, state, or episode relative to an anchor.

It may express setting relation, position, deictic position, path, origin, destination, containment, proximity, movement direction/target, recurrence/context, or materially spatialized figurative/mental positioning.

Retain the relation when orientation/context itself is a semantic coordinate. Do not inventory every prepositional phrase, beneficiary, recipient, topic, possession, ordinary argument, or discourse adverb merely because it has relational grammar.

Movement wording may overlap VERB when it independently performs both relation-edge and orienting functions.

## 7. Qualities

`qualities_available` is a boolean only. Set it true when descriptive/qualifying source language is associated with the retained coordinate; otherwise false. It never creates a row and never authorizes protected APA analysis.

## 8. Ordering

Resolve aliases/coreference before ordering.

Order retained coordinates by first referential establishment of the resolved semantic coordinate while preserving source progression.

Mechanical exceptions only:

- speaker-first PERSON where supplied by the apparatus;
- broad-before-contained PLACE when established together;
- a later alias does not move a resolved coordinate later than its true first establishment.

Do not order by importance, ontology, emotional force, or researcher preference.

## 9. Compounds

Build compounds only after the final unit inventory exists.

A compound is one source-presented binding: a proposition, event, state, question, report, reflection, intention, characterization, or relation cluster that the source presents together.

For each binding:

- include all and only final units materially participating in that binding;
- preserve source/semantic reference order;
- allow more than one VERB when the source presents those relation edges as one event cluster;
- make separate compounds when the source separately presents distinct bindings;
- set `qualities_available` from the binding’s supplied/available qualifying material, not as a reason to invent rows.

Do not create units to complete a compound, hide a missing unit inside a larger compound, emit every sentence as a graph, emit arbitrary subsets/recombinations, or duplicate nested subsets unless the source separately presents both bindings.

## 10. Final verification

Before return:

1. re-read the whole source;
2. check every requested class for omitted source-distinguished semantic coordinates;
3. verify every retained row has a positive class job and minimal complete grain;
4. remove only true grammatical debris, unsupported reification, inference, or duplication;
5. for VERB, verify distinct relation edges were neither bundled nor tokenized;
6. for PLACE/TIME, verify source-established positions/frames including legitimate unnamed ones;
7. for OBJECT, reject proposition nominalization unless the source itself treats the content as a referent;
8. for LABEL, preserve genuine source characterization without duplicating ordinary action predicates;
9. for LOCATOR, preserve genuine orientation/context without promoting every relation phrase;
10. verify exact contiguous wording, posture, coreference, and first-establishment order;
11. verify compounds use all and only participating final units in each source-presented binding.

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

For forward Researcher Inventory calibration behavior only, V30 supersedes V29’s whole-story independent-role test and broad VERB predicate-family rule to the extent they suppress smaller source-distinguished semantic coordinates or encourage proposition-sized substitute rows.

V30 retains V29’s full-source coverage duty, literal-source discipline, source-posture preservation, unnamed PLACE/TIME permission, positive cross-class-function requirement, candidate-only status, holdout isolation, no promotion/no APA IDs, repeated archetype pass gate, and fresh-agent clean-room certification sequence.

V29 remains preserved as historical calibration evidence.
