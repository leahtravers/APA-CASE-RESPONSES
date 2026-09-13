# RESEARCHER INVENTORY WORKER CONTRACT v12

Status: ACTIVE
Contract version: RI-CONTRACT-V12
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

**Inventory coordinates are functional researcher handles, not a list of every lexical item.** A word or phrase is evidence for a coordinate only when retaining that coordinate lets the researcher later select a materially distinct who, what, where, when, characterization, happening, or relation.

**Completeness means retaining all materially distinct researcher-selectable coordinates at that functional grain. It does not mean atomizing every noun phrase, clause, auxiliary, modifier, temporal word, preposition, pronoun, or possible inference.**

## Independent-coordinate gate

Before retaining any candidate, ask one mechanical question:

> If this candidate were removed, would a materially distinct who, what, where, when, source characterization, happening, or relation that the researcher could independently select later disappear from the inventory?

- If yes, retain it in the class whose job it actually performs.
- If no, omit it.
- Grammar alone is never a reason to create a unit.
- An explicit noun, adjective, temporal expression, or preposition is not automatically an inventory coordinate.
- Do not create a second unit merely because the same wording can be grammatically described in another way.
- Cross-class reuse is allowed when the source material independently performs both class functions. Do not suppress a legitimate coordinate merely because the same source span already supports another class.
- Resolve coreference before applying this gate. A pronoun or generic placeholder that only points to an already retained coordinate is not a new coordinate.

## Coordinate-versus-wording rule

The coordinate and its wording are different things.

- `source_wording` records exact source language when the coordinate itself is explicitly worded.
- `source_cue` is exact source evidence anchoring the coordinate.
- A materially required PLACE or TIME may be unnamed. In that case `source_wording` is null and the exact source cue anchors a neutral researcher tag.
- Do not promote an explicit word into the wrong class merely because unnamed coordinates feel less concrete.
- Do not substitute an explicit nearby noun, time word, or adjective for the actual functional coordinate.

## Controlling rules

### 1. Literal language wins

Never substitute a synonym because it is convenient.
Never polish, normalize, translate, or explain source wording.
Preserve colloquial language, dialect, idiom, figurative language, questions, negation, uncertainty, comparison, attribution, and sequence.

If a field claims to contain source wording or a source cue, it must be exact source text.

Use the shortest complete source-near form that keeps the coordinate distinct. Do not absorb subjects, objects, complements, or neighboring predicates unless they are necessary to keep the coordinate complete.

`researcher_note` should normally be null. Use it only when a short note is necessary to preserve coreference, unnamed-coordinate status, or another mechanical dependency. Do not qualify or explain obvious source material.

### 2. Places are scene and occurrence-position coordinates

PLACE is not a vocabulary list of place nouns and is not limited to unique physical venues.

Retain the materially distinct place coordinates needed to locate the represented story:

- broad and contained settings when both independently locate represented material;
- an object's materially represented position when that position matters independently;
- an actor's materially represented origin, destination, or off-scene position;
- the position of a materially distinct wait, encounter, conversation, remembered episode, or present telling when that occurrence needs its own place handle;
- an unnamed scene or occurrence-position when the source requires one even if the physical venue overlaps another retained place.

Two PLACE coordinates may physically overlap. Reuse an existing PLACE only when no distinct scene/occurrence position would be lost by doing so.

Do not create a PLACE merely from a geographic or setting-like phrase that supplies background description but does not independently locate retained story material.
Do not convert an object into PLACE unless the source uses it as a setting/position coordinate.

For an unnamed place, `source_wording` is null, the exact source cue anchors it, and the tag is neutral.
When a broad setting and contained setting first arise together, order the broad setting first.

### 3. Times are episode coordinates, not temporal-expression inventory

TIME identifies materially distinct story frames. An explicit temporal word or phrase is evidence, not an automatic TIME row.

Retain a TIME when removing it would erase a distinct temporal frame needed to reconnect the story, including materially separate earlier periods, attempts, responses, transitions, waits, later reports/conversations, recurring periods, reflective present frames, and prospective/future frames.

Several temporal expressions may belong to one episode. Several happenings may share one TIME. Conversely, a distinct episode may require an unnamed TIME even when it contains no clock/date word.

Do not create a separate TIME solely because the source contains:

- a frequency word;
- a duration phrase;
- a sequencing word;
- a simultaneous-clause marker;
- a tense/aspect marker;
- a hypothetical action;
- a future-looking predicate;

unless that expression identifies a materially distinct frame in its own right.

For an unnamed time, `source_wording` is null, the exact source cue anchors it, and the tag is a neutral episode description.
Inventorying a hypothetical, intended, recurring, or future frame does not assert that its content happened. Preserve its source posture.

### 4. People are represented actors, ordered by participation

Retain the speaker plus materially represented human or social actors, including relational actors that matter to a retained thing or relation.
Merge true aliases and coreference.

The speaker is `B`.
For everyone else, ordering is by first independent represented participation, not by an earlier merely possessive or descriptive mention.
Independent participation includes acting, speaking, perceiving, deciding, being acted upon, being the endpoint of a material interaction, or being the represented endpoint of a relation.
A person mentioned only as a possessor/beneficiary/descriptor does not jump ahead of people who independently participate; if such a person never independently participates, retain them after participating actors in source order.

Do not split one represented actor into separate PERSON coordinates merely because the source uses a later descriptive or temporal name for the same actor/group. Split only when the source materially distinguishes different actors/groups.

### 5. Objects are independently trackable source-treated things

Retain materially represented concrete or abstract things that function as independently selectable referents in the represented story.

An OBJECT may be a physical thing, amount, result, condition, decision, contemplated choice treated as a thing, relation treated as a thing, set/category, internal represented object, or source-treated entity inside a comparison or hypothetical.

The test is not whether a noun phrase exists. The test is whether the source treats the referent as something the researcher may need to select independently later.

Do not create an OBJECT from:

- a pronoun or generic placeholder that only corefers with an already retained coordinate;
- a whole clause or predicate merely because it can be nominalized by the worker;
- an incidental noun inside description that never functions as a represented participant/referent;
- a grammatical complement with no independent referential job;
- a PLACE whose source job is only location;
- a LABEL whose source job is only characterization.

Do not discard a materially distinct represented part merely because its whole is also retained.
When the source treats a decision, choice, relation, category, or internal object as a selectable thing, retain that thing without inventing a synonym for it.

### 6. Labels are source-applied characterizations

`LABEL` inventory is separate from the `qualities_available` boolean.

Retain a LABEL when the source applies a materially selectable characterization, quality, state, comparison, identity term, self-label, evaluative phrase, contrast, rejection, or correction to a represented coordinate or proposition.

A descriptive-looking word is not enough. There must be a characterization job.
Use the shortest complete source wording that carries that characterization.
Preserve negation, question, contrast, and uncertainty posture where needed to prevent reversal.

Do not create a LABEL from:

- the ordinary name/category of a place or object;
- a quantity by itself;
- a plain temporal expression;
- a grammatical modifier with no independent characterization job;
- a predicate duplicated only because it contains an adjective or copula.

Short source characterizations may be independently retained even when the characterized item also has `qualities_available=true`.
Do not replace a source label with a synonym or inferred psychological meaning.

### 7. Verbs are minimal complete lexical happenings or states

Retain materially represented lexical happenings/states in source order.

Use the smallest complete lexical predicate construction that preserves the distinct happening and its source posture. A lexical predicate may include a particle, complement marker, or nearby word when dropping it changes the happening.

Matrix and embedded predicates should be separate only when each contributes a genuinely different researcher-selectable happening. Do not split a single predicate construction into support fragments. Do not merge genuinely different happenings into a polished event summary.

Stance and relation predicates such as perceiving, recalling, asking, wanting, trying, thinking, finding, feeling, needing, or appearing remain eligible when the stance/relation itself is materially represented. Negation, uncertainty, questions, intentions, hypotheticals, recurrence, and future posture do not erase a represented lexical happening.

Do not create separate VERB units for pure auxiliaries, aspect markers, infinitival support, or copulas whose only job is grammatical support.
Do not duplicate the same happening only through coreference or restatement.
Inventorying a predicate is not asserting that its event happened.

### 8. Locators are independently meaningful position, path, containment, or relation handles

Retain materially useful spatial, directional, containment, path, proximity, movement, position, and relational locator constructions.
Use the smallest complete meaningful construction rather than an isolated preposition.

LOCATOR is functional. A locator may be physical or figurative/relational when the relation itself materially locates or connects represented material.

Retain a locator when removing it would lose an independently useful answer to where/which-position/which-path/which-relational-context. This can include a waiting position, movement path, destination relation, recurring-context relation, internal position, or figurative placement when materially represented.

Do not create a LOCATOR from every prepositional or relational attachment. Omit routine possession, recipient, topic, argument, or complement marking when the relation itself adds no independently selectable locating/path/position/context function.

### 9. Qualities are only availability

`qualities_available` is a boolean.
Set it true when the source supplies material qualities/descriptions associated with the coordinate. Otherwise false.
Do not interpret, classify, score, or atomize qualities merely to justify the boolean.
`Q` is never a unit reference.

## Coverage procedure for every class

For the requested class:

1. Read the entire story before returning anything.
2. Identify the functional coordinates the requested class must provide before choosing wording.
3. Sweep from beginning to end and anchor each coordinate to exact source evidence.
4. Resolve aliases/coreference and distinguish coordinate identity from merely explicit vocabulary.
5. Apply the independent-coordinate gate. Remove grammar-only fragments, duplicates, restatements, unsupported inference, and spillover from another class.
6. Preserve embedded, reported, remembered, relational, recurring, reflective, intended, hypothetical, negated, and prospective material only when it independently passes the requested class gate.
7. Do a second end-to-end omission pass for missing functional coordinates, especially unnamed scene/episode coordinates.
8. Do a final excess pass and remove lexical items whose deletion loses no distinct class function.

The target is materially complete coverage at the smallest sufficient functional-coordinate grain.

## Ordering and mechanical boundary

The apparatus, not the worker, owns final class order, canonical IDs, exact source-span validation, deterministic numbering, compound reference validation, `_Q` construction, SQL-ready row shaping, retries, and failure handling.

Default within-class order is first material source anchor after filtering and coreference resolution, with these semantic tie rules:

- required whole/broad setting before dependent part/contained setting when they first arise together;
- PERSON follows the participation rule above;
- memories, reports, hypotheticals, and future frames stay at their source position rather than being reordered into real-world chronology.

The worker must not depend on preexisting canonical IDs.

## Compounds

After units are final, map the represented story at event/proposition grain.

Create one lightweight compound for each materially distinct represented situation, assertion, question, correction, comparison, reflection, or prospective proposition that is useful for reconnecting retained units.

A compound binds the already-retained coordinates participating in one represented proposition. It must not create new semantics.

- Split coordinated material when it contains materially distinct propositions that a researcher may need separately.
- Keep one compound when several grammatical fragments jointly express one proposition.
- Do not create a compound merely because a TIME, LABEL, or other unit exists.
- Do not create compounds for background lexical fragments that failed the independent-coordinate gate.
- Do not merge materially different represented situations into one polished summary.

Use registered unit references only.
A compound cannot repair a missing unit and cannot justify an otherwise unnecessary unit.

## Forbidden work

Do not perform APA parsing, protected-thread analysis, psychological interpretation, scoring, promotion, APA-ID creation, executive analysis, or Oval Office writes.
Never present a candidate inventory as established truth.
