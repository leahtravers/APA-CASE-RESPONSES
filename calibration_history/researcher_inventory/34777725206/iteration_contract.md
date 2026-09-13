# RESEARCHER INVENTORY WORKER CONTRACT v16

Status: ACTIVE SUCCESSOR CANDIDATE
Contract version: RI-CONTRACT-V16
Mission: RESEARCHER INVENTORY ONLY
Predecessor: `researcher_inventory/AGENT_CONTRACT.md` (RI-CONTRACT-V15)

## Isolation

The worker never receives or uses approved archetypes, gold outputs, expected answers, expected counts, evaluator findings, prior scored outputs, or sealed holdout outputs.

The worker receives only this durable contract, one source story, optional neutral metadata, a bounded task schema, and when the apparatus explicitly supplies it, an unscored provisional output from another stateless pass under this same contract.

## Job

Read the whole source. Build a lightweight researcher inventory in exactly seven classes:

1. `PLACE`
2. `TIME`
3. `PERSON`
4. `OBJECT`
5. `LABEL`
6. `VERB`
7. `LOCATOR`

Then build lightweight compounds from the retained coordinates.

This is an index, not an interpretation, not a token inventory, and not a grammatical parse.

The target is the smallest set of source-grounded coordinates that preserves the materially represented structure a researcher may need later.

## The universal retention gate

A candidate survives only when all of these are true:

1. **Represented:** the source itself represents the candidate explicitly or necessarily implies the corresponding place/time position needed for a represented occurrence.
2. **Class job:** removing it would remove a materially distinct job of the requested class, not merely a word, grammatical role, qualifier, or subpart.
3. **Independent use:** the coordinate can be selected later without requiring the researcher to reconstruct a different coordinate of the same class.
4. **Not already carried:** the same class job is not already preserved by another retained coordinate, by `qualities_available`, or by a compound binding.

If the case for a separate coordinate is doubtful, omit it. The burden is on retention, not on splitting.

Do not count grammatical pieces. Do not retain something merely because it can be named, classified, nominalized, paraphrased, or described.

A source span may support more than one class only when it performs genuinely different jobs in those classes. Cross-class reuse never justifies duplicate rows inside one class.

## Whole-source procedure

For each requested class:

1. Read the entire source before producing rows.
2. Mark the materially represented source situations from beginning to end.
3. Resolve aliases, coreference, repeated mentions, and dependent phrases.
4. Propose only candidates that pass the universal retention gate.
5. Merge candidates that perform the same class job.
6. Run an omission pass for genuinely missing class jobs.
7. Run an excess pass and delete grammatical debris, support detail, duplicate framing, and overqualified variants.
8. Return the minimal complete class inventory in source order.

Completeness means no materially distinct class job is lost. It does not mean keeping every possible candidate.

## Literal language

Do not substitute synonyms. Do not polish, normalize, translate, diagnose, or psychologically explain source wording.

- `source_wording` must be exact source text when the coordinate itself is explicitly worded.
- `source_cue` must be exact source text that anchors the coordinate.
- `researcher_short_tag` must stay source-near. It may shorten for navigation but may not replace the source meaning with a convenient synonym.
- A materially required unnamed PLACE or TIME may use `source_wording = null`, an exact source cue, and a neutral source-near tag.
- `researcher_note` should normally be null. Use it only when necessary for coreference or an unnamed coordinate. Do not use notes to justify weak candidates.

Preserve negation, questions, uncertainty, correction, comparison, hypothetical posture, recurrence, intention, and futurity where the wording would otherwise reverse or overstate what the source represents.

## PLACE

PLACE is a scene, site, container, or occurrence-position that is independently needed to locate represented material.

Retain:

- broad and contained settings when each independently locates the story;
- an independently represented origin or destination;
- an independently represented object position when the position matters as a location handle;
- an unnamed location for a materially distinct encounter, relationship, conversation, remembered occurrence, or present telling when losing the location coordinate would lose where that situation belongs.

Do not create PLACE for every spatial noun or phrase.

A surface, part, path, distance expression, local relation, figurative spatial expression, or movement phrase is not a PLACE merely because it answers a loose “where” question. If its job is a relation or path, use LOCATOR. If its job is a thing, use OBJECT. If it is only descriptive, use Q or nothing.

A movement may imply an unnamed destination PLACE when a distinct destination site is necessarily represented even though it is not named.

Do not create a new PLACE for every action occurring inside an already retained scene.

## TIME

TIME is an independently reusable represented episode, span, or temporal frame.

Retain:

- materially distinct event episodes;
- broader spans that independently organize other represented material;
- explicit temporal anchors when they independently locate material in time;
- unnamed episodes when the occurrence is materially distinct even without a clock/date phrase;
- present-telling and prospective frames when the source separately represents them as frames.

Do not create TIME from tense, aspect, every action, every clause, a frequency word, a duration modifier, a subordinate temporal phrase, or a question about duration merely because it contains temporal language.

Merge dependent substeps into the same TIME when they belong to one represented episode. Split only when the source establishes a separately reusable frame.

A contemplated action does not create a future TIME unless a distinct prospective frame is represented.

## PERSON

PERSON is a materially represented human or social actor.

Retain the speaker and every actor that independently acts, speaks, perceives, is acted upon, or is a materially represented endpoint of a relation.

Resolve aliases and collective references before counting. Mentions that refer to the same actor or stable group are one PERSON unless the source itself distinguishes materially different groups.

The speaker canonical key is `B`.

Order non-speakers by first independent represented participation. Relation-only people who never independently participate follow participating actors in source order.

Do not create PERSON for generic audiences, discourse addressees with no represented actor, hypothetical roles, or pronouns without a distinct represented person.

## OBJECT

OBJECT is an independently selectable represented thing, value, relation-as-thing, decision, condition-as-thing, or figurative object.

Retain an item when the source treats it as a particular or reusable referent, for example because it participates in a material relation, bears a material quality/location, is compared/chosen/remembered, or is itself a represented topic or result.

Do not keep every noun phrase.

Reject:

- generic filler nouns or vague mass wording with no independent referential job;
- quantifiers or frequency markers merely because they can be nominalized;
- grammatical complements with no independent referential job;
- whole propositions merely because they can be treated as nouns;
- wording whose only job is PLACE, LABEL, VERB, or LOCATOR;
- a descriptive abstraction that merely restates a quality already carried elsewhere.

Do not split a whole and part unless the source materially treats the part as its own referent.

## LABEL

LABEL is a source-applied characterization that is independently reusable as a characterization.

Retain source-applied qualities, states, comparisons, identity terms, evaluations, corrections, rejections, and characterization-questions when the characterization itself is a distinct handle.

Use the shortest complete exact wording that preserves the characterization and its posture.

Do not create LABEL merely because a predicate contains an adjective or state. If the wording functions only as the happening/state relation itself, keep the VERB and do not duplicate it as LABEL. Likewise, do not turn a locator into LABEL unless the source independently uses that same wording as a characterization.

Do not create separate LABEL rows for intensifiers, stance wrappers, or grammatical support around one characterization. Preserve the complete source characterization instead.

## VERB

VERB is a source-level lexical predicate relation, not every verb token.

Default to **one row for one independently selectable predicate relation**.

Keep words together when they jointly form one relation. This includes support, aspect, negation, control, complement, coordinated action, or multiword predicate material when splitting would leave fragments that are not independently useful researcher relations.

Split only when each resulting predicate expresses a materially distinct relation that could be selected on its own without depending on the other fragment.

Do not split merely because grammar identifies a matrix verb, embedded verb, auxiliary, infinitive, particle, or coordinated token.

Do not create a VERB from discourse-control wording, rhetorical scaffolding, or a whole clause when the actual represented relation is carried by a smaller complete predicate.

A pure quality copula is normally carried by LABEL. A pure location copula is normally carried by PLACE/LOCATOR. Retain a copular VERB only when the placement/existence relation itself is independently useful.

Retain negated, uncertain, questioned, intended, hypothetical, recurring, and future predicate relations without asserting that they happened.

## LOCATOR

LOCATOR is an independently useful location, position, path, direction, containment, or situational-context relation.

Retain the smallest complete source construction that provides that relation.

LOCATOR may preserve:

- setting relations;
- position/proximity relations;
- origin/destination/path relations;
- movement relations;
- containment;
- materially useful recurring/situational context;
- genuine figurative location/context structure.

Do not create LOCATOR from an isolated preposition or from routine possession, recipient, topic, comparison support, or argument marking when no independent locating/path/context job would disappear.

PLACE and LOCATOR are independent classes: PLACE stores the site; LOCATOR stores the relation to a site/path/context. Do not turn a locator phrase into another PLACE merely to preserve it.

## qualities_available

`qualities_available` is only a boolean.

Set it true when the source supplies material descriptive/qualifying information associated with the coordinate. Otherwise set it false.

Do not create extra units merely to explain Q. Do not enumerate or interpret the qualities. `Q` is never a unit reference.

## Ordering

The apparatus owns final IDs and numbering.

Within each class, order by first material source anchor after merging and filtering.

Tie rules:

- broad setting before contained setting when first introduced together;
- PERSON follows participation order;
- remembered, reported, hypothetical, and future material stays at its source position rather than being reordered into real-world chronology.

## Stateless verification

If the apparatus supplies a provisional unscored output, treat it only as a checklist.

Re-read the full source and apply this contract from scratch.

The verification pass is deletion-biased:

- keep a provisional row only if it independently passes the retention gate;
- add a missing row only when a materially distinct class job is clearly lost without it;
- when two rows compete for the same class job, merge or keep the smaller sufficient source-level coordinate;
- when uncertain whether a separate row is warranted, omit it.

The provisional output is not gold, evaluator feedback, or an expected answer.

## Compounds

Compounds are a lightweight reassembly spine, not an exhaustive clause inventory.

Create a compound only when it binds retained coordinates into one materially distinct represented proposition or situation that a researcher may need to reconnect later.

Prefer one source-level proposition over several grammatical fragments.

Merge closely linked predicates when they express one represented event/proposition with the same main participants and frame. Split only when the source materially represents separate propositions.

Do not create a compound:

- merely because a unit exists;
- for a bare quality already preserved by a unit plus Q unless the characterization proposition itself matters;
- for discourse scaffolding;
- for grammatical fragments;
- to compensate for a missing unit;
- for every possible subset or recombination of the same event.

Use registered unit references only. The compound must not invent semantics.

## Apparatus boundary

The apparatus, not the worker, owns canonical IDs, deterministic numbering, exact-source validation, ordering enforcement, compound-reference validation, `_Q` construction, SQL-ready shaping, retries, and failure handling.

The worker must not depend on hidden canonical IDs or expected counts.

## Forbidden work

Do not perform APA parsing, protected-thread analysis, psychological interpretation, scoring, promotion, APA-ID creation, executive analysis, or Oval Office writes.

Never present a candidate inventory as established truth.
