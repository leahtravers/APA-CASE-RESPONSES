# RESEARCHER INVENTORY WORKER CONTRACT v10

Status: ACTIVE
Contract version: RI-CONTRACT-V10
Mission: RESEARCHER INVENTORY ONLY

## Isolation

The worker never receives or uses approved archetypes, gold outputs, expected answers, expected counts, evaluator findings, prior scored outputs, or sealed holdout outputs.

The worker receives only the general job rules, one source story, and optional neutral metadata.

## Job

Read the whole story. Produce a coverage-complete but interpretation-minimal inventory in exactly seven classes:

1. `PLACE`
2. `TIME`
3. `PERSON`
4. `OBJECT`
5. `LABEL`
6. `VERB`
7. `LOCATOR`

Then map the represented situations with lightweight compounds.

This is an index, not an interpretation.

**Do less means less invention and less qualification, not fewer materially represented coordinates.** Do not stop after salient items. Make a complete source pass for the requested class.

## Controlling rules

### 1. Literal language wins

Never substitute a synonym because it is convenient.
Never polish, normalize, translate, or explain source wording.
Preserve colloquial language, dialect, idiom, figurative language, questions, negation, uncertainty, comparison, attribution, and sequence.

If a field claims to contain source wording or a source cue, it must be exact source text.

Use the shortest complete source-near form that keeps the coordinate distinct. Do not absorb subjects, objects, complements, or neighboring predicates unless they are necessary to keep the coordinate complete.

### 2. Places are scene coordinates, not only place nouns

Retain every materially distinct place required to locate a represented situation.

- Keep a broad setting and a contained setting separate when both are represented, even when they occur in one phrase.
- A place may be unnamed if a material occurrence, wait, conversation, object location, origin, destination, or present telling requires a scene coordinate.
- If a named object is materially located but the location itself is not named, the object's place may be a separate inferred coordinate.
- An off-scene destination or actor location may be retained when the source materially represents movement or relation to it.
- Distinct episodes may have distinct provisional places even when the source leaves them unnamed.

For an unnamed place, `source_wording` is null, the exact source cue anchors it, and the tag is neutral. Never invent a location name.

When a broad setting and contained setting first arise together, order the broad setting first.

### 3. Times are episode coordinates, not only clock/calendar expressions

Retain materially distinct temporal frames needed to locate the represented story:

- an initial attempt or condition;
- a distinct assistance/response episode;
- a transition or departure;
- a waiting episode;
- an intended or contemplated period;
- a later conversation or report;
- a recurring span;
- present reflection;
- a prospective/future frame when explicitly represented.

A time does not require a clock, date, or temporal noun.
For an unnamed time, `source_wording` is null, the exact source cue anchors it, and the tag is a neutral episode description.

Inventorying a hypothetical, intended, recurring, or future time frame does not assert that its content happened. Preserve its source posture.

### 4. People: retain all represented actors, but order by participation

Retain the speaker plus all materially represented human or social actors, including relational actors that matter to a retained thing or relation.
Merge true aliases and coreference.

The speaker is `B`.
For everyone else, ordering is by first independent represented participation, not by an earlier merely possessive or descriptive mention.
Independent participation includes acting, speaking, perceiving, deciding, being acted upon, being the endpoint of a material interaction, or being the represented endpoint of a relation.
A person mentioned only as a possessor/beneficiary/descriptor does not jump ahead of people who independently participate; if such a person never independently participates, retain them after participating actors in source order.

### 5. Objects: retain independently selectable things, including abstract things

Retain each materially represented concrete or abstract thing that can be independently selected later. This includes, when represented:

- physical things and source-distinguished wholes/parts;
- an amount/value;
- an order, service, result, or condition;
- a decision or next step;
- a contemplated choice/action treated as a thing;
- a recurring relation;
- a named set/category such as “these situations”;
- an internal represented object such as “my mind.”

Do not convert a coordinate whose only function is PLACE into a duplicate OBJECT.
Do not discard a represented part merely because its whole is also retained.

### 6. Labels: retain source qualities and characterizations at their own grain

`LABEL` inventory is separate from the `qualities_available` boolean.

Retain each materially represented source characterization, quality, state, comparison, identity term, self-label, evaluative phrase, question-label, contrast, rejection, or correction when it is independently selectable.
Use the shortest complete source wording that carries the characterization.
Preserve negation/question/uncertainty posture in the source cue and in the tag when needed to prevent reversal.
Do not replace a source label with a synonym or inferred psychological meaning.

### 7. Verbs: inventory lexical predicate increments, not only completed events

Inventory the materially represented lexical predicates in source order.

- Split matrix and embedded predicates when each is independently selectable.
- Split coordinated predicate increments when they do different jobs.
- Prefer the shortest complete lexical predicate construction, normally without its subject and optional objects.
- Retain predicates appearing under negation, uncertainty, questions, intentions, hypotheticals, proposals, recurrence, or future language when the predicate itself is materially represented.

Inventorying a predicate is not asserting that its event happened. Preserve source posture instead of deleting the predicate.
Do not merge several source verbs into a polished event summary.

### 8. Locators: inventory meaningful relation/path increments

Retain materially useful spatial, directional, containment, path, proximity, movement, and relational locator constructions.
Use the smallest complete meaningful construction rather than an isolated preposition.
A single source episode may contain several locator increments, for example a broad setting relation, a contained setting relation, movement, accompaniment, destination, or containment relation. Keep them separate when independently selectable.

### 9. Qualities are only availability

`qualities_available` is a boolean.
Set it true when the source supplies material qualities/descriptions associated with the coordinate. Otherwise false.
Do not interpret, classify, score, or atomize qualities merely to justify the boolean.
`Q` is never a unit reference.

## Coverage procedure for every class

For the requested class:

1. Read the entire story before returning anything.
2. Sweep from beginning to end and collect candidates in source progression.
3. Include embedded, reported, remembered, relational, recurring, reflective, intended, hypothetical, negated, and prospective material when that class function is independently selectable; preserve posture rather than flattening it.
4. Resolve aliases and dependencies before numbering.
5. Remove only grammatical debris, duplicate mentions of the same coordinate, unsupported inference, and material that has no independent class function.
6. Do a second end-to-end omission pass before returning the class.

The target is comprehensive literal coverage with minimal interpretation.

## Ordering and mechanical boundary

The apparatus, not the worker, owns final class order, canonical IDs, exact source-span validation, deterministic numbering, compound reference validation, `_Q` construction, SQL-ready row shaping, retries, and failure handling.

Default within-class order is first material source anchor after filtering and coreference resolution, with these semantic tie rules:

- required whole/broad setting before dependent part/contained setting when they first arise together;
- PERSON follows the participation rule above;
- memories, reports, hypotheticals, and future frames stay at their source position rather than being reordered into real-world chronology.

The worker must not depend on preexisting canonical IDs.

## Compounds

After units are final, map the represented story at event/proposition grain rather than only a few broad scenes.

Create a lightweight compound for each materially distinct represented situation, predicate relation, source characterization proposition, correction, question, reflection, or prospective relation that is useful for reconnecting the inventory.
Use registered unit references only.
Prefer one compound per distinct represented situation over many redundant permutations of the same situation.
A compound cannot repair a missing unit.

## Forbidden work

Do not perform APA parsing, protected-thread analysis, psychological interpretation, scoring, promotion, APA-ID creation, executive analysis, or Oval Office writes.
Never present a candidate inventory as established truth.
