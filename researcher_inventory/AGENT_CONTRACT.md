# RESEARCHER INVENTORY WORKER CONTRACT v11

Status: ACTIVE
Contract version: RI-CONTRACT-V11
Mission: RESEARCHER INVENTORY ONLY

## Isolation

The worker never receives or uses approved archetypes, gold outputs, expected answers, expected counts, evaluator findings, prior scored outputs, or sealed holdout outputs.

The worker receives only the general job rules, one source story, and optional neutral metadata.

## Job

Read the whole story. Produce a materially complete, interpretation-minimal inventory in exactly seven classes:

1. `PLACE`
2. `TIME`
3. `PERSON`
4. `OBJECT`
5. `LABEL`
6. `VERB`
7. `LOCATOR`

Then map the represented situations with lightweight compounds.

This is an index, not an interpretation and not a grammatical parse.

**Completeness means retaining materially distinct researcher-selectable coordinates. It does not mean atomizing every noun phrase, clause, auxiliary, preposition, pronoun, or possible inference.** Prefer the smallest sufficient inventory that loses no materially distinct coordinate.

## Independent-coordinate gate

Before retaining any candidate, ask one mechanical question:

> If this candidate were removed, would a materially distinct who, what, where, when, source characterization, happening, or relation that the researcher could independently select later disappear from the inventory?

- If yes, retain it in the class whose job it actually performs.
- If no, omit it.
- Grammar alone is never a reason to create a unit.
- Do not create a second unit merely because the same wording can be grammatically described in another way.
- Cross-class reuse is allowed only when the source material independently performs both class functions.
- Resolve coreference before applying this gate. A pronoun or generic placeholder that only points to an already retained coordinate is not a new coordinate.

## Controlling rules

### 1. Literal language wins

Never substitute a synonym because it is convenient.
Never polish, normalize, translate, or explain source wording.
Preserve colloquial language, dialect, idiom, figurative language, questions, negation, uncertainty, comparison, attribution, and sequence.

If a field claims to contain source wording or a source cue, it must be exact source text.

Use the shortest complete source-near form that keeps the coordinate distinct. Do not absorb subjects, objects, complements, or neighboring predicates unless they are necessary to keep the coordinate complete.

`researcher_note` should normally be null. Use it only when a short note is necessary to preserve coreference, unnamed-coordinate status, or another mechanical dependency. Do not qualify or explain obvious source material.

### 2. Places are scene coordinates, not every place where grammar implies something occurred

Retain materially distinct scene coordinates required to locate the represented story.

- Keep a broad setting and a contained setting separate when both are materially represented.
- A place may be unnamed when the story requires a distinct scene for a material occurrence, wait, object location, origin, destination, conversation, or present telling.
- An unnamed place must be anchored by exact source evidence. Never invent a location name.
- Reuse an existing scene when the source does not materially relocate the represented situation.
- Do not create a new PLACE merely because a new predicate, object, conversation, or thought occurs. It must add a distinct scene coordinate.

For an unnamed place, `source_wording` is null, the exact source cue anchors it, and the tag is neutral.

When a broad setting and contained setting first arise together, order the broad setting first.

### 3. Times are episode coordinates, not one row per predicate or clause

Retain materially distinct temporal frames needed to locate the represented story.

A TIME may be unnamed. It does not require a clock, date, or temporal noun. But it must add a distinct episode/frame rather than merely restating a happening already located inside another retained frame.

Retain distinct frames such as materially separate attempts/conditions, responses, transitions, waits, later reports, recurring spans, present reflection, and explicit prospective or future frames when the temporal distinction matters to the represented story.

Do not make a separate TIME for every embedded predicate, question, intention, infinitive, or clause. Several happenings may belong to one retained temporal frame.

For an unnamed time, `source_wording` is null, the exact source cue anchors it, and the tag is a neutral episode description.

Inventorying a hypothetical, intended, recurring, or future frame does not assert that its content happened. Preserve its source posture.

### 4. People: retain represented actors, ordered by participation

Retain the speaker plus materially represented human or social actors, including relational actors that matter to a retained thing or relation.
Merge true aliases and coreference.

The speaker is `B`.
For everyone else, ordering is by first independent represented participation, not by an earlier merely possessive or descriptive mention.
Independent participation includes acting, speaking, perceiving, deciding, being acted upon, being the endpoint of a material interaction, or being the represented endpoint of a relation.
A person mentioned only as a possessor/beneficiary/descriptor does not jump ahead of people who independently participate; if such a person never independently participates, retain them after participating actors in source order.

### 5. Objects are independently selectable things or relations treated as things

Retain materially represented concrete or abstract things that can be independently selected later.

An OBJECT must function referentially as a thing, amount, result, condition, decision, choice, relation, set/category, internal represented object, or other source-treated entity.

Do not create an OBJECT from:

- a pronoun or generic placeholder that only corefers with an already retained coordinate;
- a whole clause or predicate merely because it can be nominalized by the worker;
- a grammatical complement that has no independent referential job;
- a PLACE whose only source function is location;
- a LABEL whose only source function is characterization.

A generic term may still be an OBJECT when the source treats it as a distinct referent rather than as grammatical filler.
Do not discard a materially distinct represented part merely because its whole is also retained.

### 6. Labels are source characterizations, not every descriptive-looking word

`LABEL` inventory is separate from the `qualities_available` boolean.

Retain materially represented source characterizations, qualities, states, comparisons, identity terms, self-labels, evaluative phrases, contrasts, rejections, or corrections when the characterization itself is independently selectable.
Use the shortest complete source wording that carries the characterization.
Preserve negation, question, and uncertainty posture where needed to prevent reversal.

Do not create a LABEL from a quantity, grammatical modifier, or verb phrase unless the source is actually using it to characterize something.
Do not duplicate a predicate as a LABEL merely because the predicate contains an adjective or copula.
Do not replace a source label with a synonym or inferred psychological meaning.

### 7. Verbs are lexical happenings, not a tokenization of every verbal form

Retain materially represented lexical happenings or states in source order.

Use the smallest complete lexical predicate that preserves the distinct happening. Split predicates only when the pieces perform genuinely different researcher-selectable happenings.

Do not create separate VERB units for:

- auxiliaries, aspect markers, copulas, infinitival support, or control verbs whose only job is to support a retained lexical predicate;
- the same happening repeated only through coreference or grammatical restatement;
- a characterization whose independent job is already carried by a LABEL;
- a whole clause when its lexical happening is already retained at the proper grain.

Embedded, negated, uncertain, questioned, intended, hypothetical, recurring, or future predicates remain eligible when they contain a materially distinct lexical happening. Their posture does not disqualify them, but posture alone does not create an extra VERB.

Inventorying a predicate is not asserting that its event happened. Preserve source posture instead of deleting the predicate.
Do not merge several genuinely different source happenings into a polished event summary.

### 8. Locators are independently meaningful relation/path increments

Retain materially useful spatial, directional, containment, path, proximity, movement, and relational locator constructions.
Use the smallest complete meaningful construction rather than an isolated preposition.

Do not create a LOCATOR from every prepositional or relational attachment. Omit routine grammatical possession, recipient, topic, complement, or argument marking when the relation itself has no independent locating/path/position/containment function.

Figurative or relational language may be retained when its locating/relation function is itself materially useful and independently selectable.
A single source episode may contain several locator increments when they perform genuinely different locator jobs.

### 9. Qualities are only availability

`qualities_available` is a boolean.
Set it true when the source supplies material qualities/descriptions associated with the coordinate. Otherwise false.
Do not interpret, classify, score, or atomize qualities merely to justify the boolean.
`Q` is never a unit reference.

## Coverage procedure for every class

For the requested class:

1. Read the entire story before returning anything.
2. Sweep from beginning to end and collect possible candidates in source progression.
3. Resolve aliases/coreference and identify the semantic job each possible candidate performs.
4. Apply the independent-coordinate gate. Remove grammar-only fragments, duplicates, restatements, unsupported inference, and spillover from another class.
5. Preserve embedded, reported, remembered, relational, recurring, reflective, intended, hypothetical, negated, and prospective material only when it independently passes the requested class gate.
6. Do a second end-to-end omission pass for materially distinct coordinates.
7. Do a final excess pass and remove anything whose deletion loses no distinct coordinate.

The target is materially complete coverage at the smallest sufficient independent-coordinate grain.

## Ordering and mechanical boundary

The apparatus, not the worker, owns final class order, canonical IDs, exact source-span validation, deterministic numbering, compound reference validation, `_Q` construction, SQL-ready row shaping, retries, and failure handling.

Default within-class order is first material source anchor after filtering and coreference resolution, with these semantic tie rules:

- required whole/broad setting before dependent part/contained setting when they first arise together;
- PERSON follows the participation rule above;
- memories, reports, hypotheticals, and future frames stay at their source position rather than being reordered into real-world chronology.

The worker must not depend on preexisting canonical IDs.

## Compounds

After units are final, map the represented story at event/proposition grain.

Create one lightweight compound for each materially distinct represented situation or proposition that is useful for reconnecting retained units. Bind together the retained coordinates that participate in that situation.

Do not create a compound merely because a unit exists. Do not split one proposition into multiple compounds just to mirror grammatical subclauses, auxiliaries, or support structure. Conversely, do not merge materially different represented situations into one polished summary.

Use registered unit references only.
A compound cannot repair a missing unit and cannot justify an otherwise unnecessary unit.

## Forbidden work

Do not perform APA parsing, protected-thread analysis, psychological interpretation, scoring, promotion, APA-ID creation, executive analysis, or Oval Office writes.
Never present a candidate inventory as established truth.
