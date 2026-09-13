# RESEARCHER INVENTORY WORKER CONTRACT v15

Status: ACTIVE
Contract version: RI-CONTRACT-V15
Mission: RESEARCHER INVENTORY ONLY

## Isolation

The worker never receives or uses approved archetypes, gold outputs, expected answers, expected counts, evaluator findings, prior scored outputs, or sealed holdout outputs.

The worker receives only the durable general job rules, one source story, optional neutral metadata, a bounded task schema, and when explicitly supplied by the apparatus an unscored provisional output from another stateless pass under this same contract.

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

Do less means less invention, less qualification, and less grammatical debris. It does not mean fewer materially represented coordinates.

Completeness means retaining every materially distinct researcher-selectable coordinate at the smallest sufficient functional grain. Do not stop after the salient items, but do not turn the source into a token inventory.

## Class-local independent-coordinate gate

Evaluate every bounded class independently.

For each candidate ask:

> If this candidate were removed from this requested class, would a materially distinct function of this class disappear from the inventory?

- If yes, retain it.
- If no, omit it.
- Grammar alone never creates a coordinate.
- Salience alone never creates a coordinate.
- A source span may independently support more than one class when it performs different jobs in those classes.
- Never omit a legitimate coordinate merely because the same wording or cue already supports another class.
- Never duplicate one job merely because the wording can be grammatically described in several ways.
- Resolve aliases and coreference before applying the gate.
- Remove duplicate mentions and unsupported inference, not materially distinct source jobs.

## Whole-source coverage discipline

For every requested class:

1. Read the entire source before answering.
2. Walk the represented story from beginning to end.
3. Consider actual, remembered, reported, relational, recurring, reflective, intended, questioned, hypothetical, negated, corrected, and prospective material without flattening its posture.
4. For each materially distinct represented situation or relation, ask whether this requested class needs a coordinate.
5. Anchor every retained coordinate to exact source evidence.
6. Resolve aliases, dependencies, and repeated mentions.
7. Run an end-to-end omission pass.
8. Run an end-to-end excess pass.

A situation may contain several coordinates of one class when those coordinates perform different reusable jobs. Conversely, several happenings may share one coordinate when they are merely substeps of the same class function.

## Literal-language rule

Never substitute a synonym because it is convenient. Never polish, normalize, translate, or psychologically explain source wording.

`source_wording` must be exact source text when the coordinate itself is explicitly worded. `source_cue` must be exact source text anchoring the coordinate.

Use the shortest complete source-near form that preserves the coordinate's job. Do not absorb subjects, objects, neighboring predicates, explanations, or qualifiers unless they are needed to keep the coordinate complete.

A materially required unnamed PLACE or TIME may use `source_wording = null`, an exact source cue, and a neutral researcher tag. Lack of a place name or clock/date expression never by itself defeats a PLACE or TIME.

`researcher_note` should normally be null. Use it only for necessary coreference, unnamed-coordinate, or mechanical bookkeeping.

## PLACE

PLACE is a represented site or occurrence-position needed to locate material. It is not merely a list of place nouns and it is not limited to unique physical venues.

Retain when independently useful:

- broad and contained settings;
- a materially represented object's position;
- a materially represented origin or destination;
- the position of a distinct wait, encounter, conversation, remembered occurrence, or present telling;
- an unnamed occurrence-position even when it physically overlaps another retained PLACE.

Different events can require different PLACE coordinates even if the physical venue is the same or unnamed.

Do not create PLACE merely because wording denotes a surface, container, body part, geographic term, figurative phrase, or motion. A contemplated exit or movement is not a new PLACE unless a distinct destination site/position is represented. A recurring activity is not a new PLACE unless its setting is independently distinguished.

For unnamed places, `source_wording` is null. When broad and contained settings arise together, broad precedes contained.

## TIME

TIME is a materially distinct represented episode or frame needed to reconnect the story. It does not require a clock, date, duration, or temporal noun.

Retain distinct frames such as an initial condition/attempt, a response episode, a materially distinct transition/departure episode, a wait, an intended period, a later conversation/report, a recurring span, present reflection, or a separately represented prospective/future frame.

Do not create a TIME merely from tense, aspect, sequence language, frequency wording, a question, or every action inside an existing frame. Several substeps may share one TIME. Split only when a new episode/frame is materially represented.

A contemplated action inside the current frame does not automatically create a prospective TIME. A prospective TIME is warranted only when the source separately represents the future/prospective frame. Likewise, multiple reflective predicates in the same current telling do not automatically create multiple present-reflection TIMES.

For unnamed times, `source_wording` is null and the exact source cue anchors a neutral episode description. Preserve intended, questioned, recurring, hypothetical, and future posture without asserting that the content happened.

## PERSON

Retain the speaker plus every materially represented human or social actor that acts, speaks, perceives, is acted upon, or serves as a materially represented endpoint of a relation.

Merge true aliases and coreference. The speaker canonical key is `B`.

Order non-speakers by first independent represented participation. A person mentioned only as possessor, beneficiary, or descriptor does not outrank independently participating actors. If such a person never independently participates, retain them after participating actors in source order.

Do not create PERSON for a generic audience, generic person, discourse addressee, hypothetical role, or pronoun without a materially represented actor.

## OBJECT

OBJECT is a source-treated independently selectable concrete or abstract thing. It is not every noun phrase and not every clause that can be nominalized.

Retain when represented as independently trackable:

- physical things and materially distinguished wholes/parts;
- amounts and values;
- orders, services, results, or conditions treated as things;
- decisions and next steps;
- contemplated choices treated as whole selectable things;
- recurring relations treated as things;
- named sets/categories;
- internal represented objects;
- source-treated entities inside remembered, questioned, comparative, or hypothetical material.

Do not create OBJECT from a pronoun that only corefers, incidental nouns, discourse wording, a grammatical complement with no independent referential job, a whole proposition merely because it can be nominalized, a PLACE whose only job is location, or a LABEL whose only job is characterization.

Do not let evaluative or descriptive wording hide an independently represented referent. Do not discard a materially distinct part merely because its whole is also retained.

## LABEL

LABEL is an independently selectable source-applied characterization. LABEL is separate from `qualities_available`.

Retain materially represented qualities, states, comparisons, identity terms, self-labels, evaluations, contrasts, rejections, corrections, and characterization-questions when the characterization itself is a reusable source handle.

Use the shortest complete exact source wording that carries the characterization. Preserve negation, question, uncertainty, contrast, rejection, and correction posture when necessary to prevent reversal.

Extract the characterization, not surrounding stance/control wording. Do not create a second LABEL merely from an intensifier or comparative wrapper around an already represented characterization. Do not duplicate an ordinary predicate as LABEL unless the source wording independently performs a characterization job.

Locational or relational wording may also be LABEL when the source independently uses it as a characterization rather than merely as location/context.

## VERB

VERB inventories materially represented lexical predicate increments in source order. It is not a list of every grammatical verb token, but it is also not a list of only broad event summaries.

Use the smallest complete lexical predicate construction that preserves the distinct happening, state, stance, or relation and its source posture.

- Split matrix and embedded predicates when each contributes a different independently selectable predicate relation.
- Split coordinated predicates when they perform different jobs.
- Keep auxiliaries/support/aspect material with the lexical predicate when separating it would create grammatical debris.
- Keep a semantically bound multiword predicate together when its pieces do not independently do different jobs.
- Retain predicates under negation, uncertainty, questions, intentions, hypotheticals, proposals, recurrence, and future language.
- A quality copula whose only semantic content is an independently retained LABEL is normally not a second VERB.
- A locative copula whose only semantic content is an independently retained LOCATOR is normally not a second VERB unless the source independently represents the placement/existence relation itself as a predicate handle.
- Do not create a VERB from an entire question or clause when a shorter lexical predicate carries the job.
- Do not create new rows for repeated/coreferential mentions of the same predicate.

Inventorying a predicate never asserts that its event happened.

## LOCATOR

LOCATOR is an independently useful where/which-position/which-path/which-context relation. It is broader than PLACE and is not limited to prepositions or literal physical space.

Retain materially useful:

- broad and contained setting relations;
- position/proximity relations;
- movement and path relations;
- accompaniment when materially locational;
- destination/origin constructions;
- containment relations;
- recurring or situational context relations when they independently reconnect represented material;
- internal or figurative location relations when the source genuinely uses them as locating/context structure.

Use the smallest complete meaningful construction, not an isolated preposition.

Do not create LOCATOR from routine possession, recipient, topic, argument/complement marking, or comparison support when no independent locating/path/context job would be lost. A temporal or subordinate construction may be a LOCATOR only when its source job independently supplies reusable context rather than merely grammar.

Evaluate LOCATOR independently from PLACE and TIME. When broad and contained setting locators arise together, broad precedes contained.

## qualities_available

`qualities_available` is only a boolean. Set it true when the source supplies material qualities/descriptions associated with the coordinate, otherwise false. Do not create, split, classify, score, or interpret qualities merely to justify the boolean. `Q` is never a unit reference.

## Ordering and apparatus boundary

The apparatus, not the worker, owns final canonical IDs, deterministic numbering, exact-source validation, ordering enforcement, compound reference validation, `_Q` construction, SQL-ready shaping, retries, and failure handling.

Default within-class order is first material source anchor after filtering/coreference resolution, with these tie rules:

- whole/broad setting before dependent part/contained setting when first introduced together;
- PERSON follows participation order;
- remembered/reported/hypothetical/future frames stay at source position rather than being reordered into real-world chronology.

The worker must not depend on preexisting canonical IDs.

## Stateless verification pass

The apparatus may send an unscored provisional output to a separate stateless session under this same contract.

The provisional output is not gold, not evaluator feedback, not an expected answer, and not authoritative. Re-read the whole source and rebuild the requested result. Use the provisional only as an omission/excess checklist. Do not keep a row because the first pass produced it and do not omit a row because the first pass omitted related material.

## Compounds

After units are final, map the represented story at lightweight event/proposition grain using only retained units.

Create a compound for each materially distinct represented proposition, situation, predicate relation, characterization proposition, question, correction, comparison, reflection, or prospective relation that is useful for reconnecting the inventory.

A compound binds already-retained coordinates; it never repairs a missing unit or creates semantics.

- Prefer proposition-level coverage over a few broad scene summaries.
- Split materially different propositions.
- Keep pieces together when they jointly express one proposition.
- Do not create compounds for grammatical fragments or rejected coordinates.
- Do not create a compound merely because a unit exists.
- Use registered unit references only.

## Forbidden work

Do not perform APA parsing, protected-thread analysis, psychological interpretation, scoring, promotion, APA-ID creation, executive analysis, or Oval Office writes. Never present a candidate inventory as established truth.
