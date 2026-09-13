# RESEARCHER INVENTORY WORKER CONTRACT v14

Status: ACTIVE
Contract version: RI-CONTRACT-V14
Mission: RESEARCHER INVENTORY ONLY

## Isolation

The worker never receives or uses approved archetypes, gold outputs, expected answers, expected counts, evaluator findings, prior scored outputs, or sealed holdout outputs.

The worker receives only the general job rules, one source story, optional neutral metadata, and the bounded task schema supplied by the apparatus.

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

The inventory is intentionally sparse. A coordinate is retained only when it gives the researcher a distinct reusable handle that would otherwise be lost. Do not turn clauses into their grammatical parts. Do not create a row merely because a word, phrase, verb, noun, adjective, temporal expression, or preposition exists.

## Independent-coordinate gate

For the requested class, ask of every candidate:

> If this row were removed, would a materially distinct researcher-selectable function of this class disappear?

If no, omit it.

A source span may support coordinates in more than one class when it truly performs different independent jobs. But grammatical describability in several classes is not enough. Do not duplicate one semantic job across classes.

Resolve aliases and coreference before applying the gate. Pronouns, restatements, support words, and grammatical fragments are not new coordinates when they only point to already represented material.

## Whole-source procedure

For every class:

1. Read the entire source before answering.
2. Walk the represented story in source order.
3. Consider remembered, reported, recurring, reflective, intended, questioned, hypothetical, negated, and prospective material without flattening its posture.
4. Retain only distinct class functions.
5. Resolve aliases and repeated mentions.
6. Run one omission pass.
7. Run one excess pass and delete anything whose removal loses no distinct requested-class function.

Completeness means complete coverage of functional coordinates, not maximal linguistic decomposition.

## Literal-language rule

Never substitute a synonym because it is convenient. Never polish, normalize, translate, or psychologically explain source wording.

`source_wording` must be exact source text when the coordinate itself is explicitly worded. `source_cue` must be exact source text anchoring the coordinate. A materially required unnamed PLACE or TIME may use `source_wording = null` with an exact source cue and a neutral researcher tag.

Use the shortest complete source-near form that preserves the coordinate's semantic job. `researcher_note` should normally be null and is reserved for necessary coreference or unnamed-coordinate bookkeeping.

## PLACE

PLACE is a site or position at which represented material is situated or occurs. It is not a vocabulary list of place-like phrases and it is not a list of every motion endpoint that can be imagined.

Retain:

- broad and contained settings when each independently locates represented material;
- a materially represented object position when independently useful;
- a represented destination or origin when the source actually establishes a distinct site/position;
- the position of a distinct wait, encounter, later conversation, remembered occurrence, or present telling when that occurrence needs its own scene handle, even if the physical venue is unnamed or overlaps another place.

Do not create PLACE merely from:

- movement wording whose independent job is path/direction;
- a contemplated exit or movement without a separately represented destination site;
- a recurring activity that does not distinguish a separate setting;
- a surface, container, body part, internal state, figurative phrase, or setting-like noun that does not independently locate represented material.

For unnamed places, `source_wording` is null and the tag is neutral. When broad and contained settings first arise together, broad comes first.

## TIME

TIME is a coherent represented episode or frame. It is not a row per action, transition word, question, tense, aspect, frequency phrase, or future-looking predicate.

Several happenings may share one TIME. Several reflections in the current telling may share one present-reflection TIME. An action inside an existing episode does not create another TIME merely because it occurs later within that episode.

Retain a new TIME only when the story establishes a materially distinct frame needed to reconnect the material, such as a distinct earlier/later episode, wait, later conversation/report, recurring period, present reflection, or separately represented prospective/future frame.

A contemplated action inside a current episode does not automatically create a prospective TIME. A transition or departure does not automatically create its own TIME. A reflective predicate does not automatically create its own TIME. Frequency, duration, sequence, tense, and aspect are evidence only.

For unnamed times, `source_wording` is null and the tag is a neutral episode description. Preserve questioned, intended, recurring, hypothetical, and prospective posture without asserting events occurred.

## PERSON

Retain the speaker plus materially represented human or social actors that act, speak, perceive, are acted upon, or serve as materially represented endpoints of relations.

Merge true aliases and coreference. The speaker canonical key is `B`.

For everyone else, ordering follows first independent represented participation. A person mentioned only as possessor, beneficiary, or descriptor does not outrank independently participating actors. If such a person never independently participates, retain them after participating actors in source order.

Do not create PERSON from generic audiences, hypothetical roles, discourse addressees, or pronouns without independent participation.

## OBJECT

OBJECT is a source-treated independently trackable referent, concrete or abstract. It is not every noun phrase and not every clause that can be nominalized.

Retain physical things, source-distinguished wholes/parts, amounts or values, decisions/next steps, independently represented choices treated as things, recurring relations treated as things, named sets/categories, and internal represented objects when the source treats them as independently selectable referents.

Do not create OBJECT solely from:

- an embedded proposition or grammatical complement;
- a whole event restated as a noun phrase;
- an idiomatic slot noun whose meaning belongs to a larger characterization or predicate;
- a predicate complement that only completes a LABEL or VERB;
- a pronoun or generic placeholder that only corefers;
- incidental nouns inside description;
- a PLACE whose only job is location;
- a LABEL whose only job is characterization.

A contemplated choice is an OBJECT only when the choice as a whole is independently represented as something that can be selected later, not merely because its component verbs appear.

## LABEL

LABEL is an independently selectable source-applied characterization. It is not every adjective, state predicate, negation, comparative phrase, or clause containing evaluative language.

Retain a characterization, quality, comparison, identity term, self-label, evaluation, contrast, rejection, correction, or characterization-question when the characterization itself is a distinct reusable handle.

Extract the characterization itself, not the surrounding stance or control predicate. If a source construction expresses wanting, thinking, asking, or appearing plus a characterization, do not turn the entire stance construction into a second LABEL when the characterization is the actual label.

Do not duplicate a VERB state as LABEL unless the wording independently functions as characterization. Do not create a second LABEL merely from comparative or intensifier wording that only modifies an already retained characterization. Conversely, locational or relational wording may also be LABEL when the source independently applies it as a salient characterization rather than merely locating something.

Preserve question, negation, uncertainty, contrast, and correction posture as needed to prevent reversal. Use the shortest complete exact source wording carrying the characterization.

## VERB

VERB is a minimal semantic predicate increment, not a list of grammatical verb tokens.

A single VERB coordinate may contain more than one grammatical verb when those words form one semantic predicate construction. Keep semantically bound support/control/raising/infinitival/copular material together when separating it would create artificial rows. Coordinated actions may remain one VERB when the source presents them as one selectable alternative or action package.

Split predicates only when each contributes a genuinely different researcher-selectable semantic relation or happening.

Do not create separate VERB rows merely for:

- auxiliaries, copulas, support verbs, participles, or infinitival pieces of one predicate construction;
- a complete question clause when the useful predicate can be represented at predicate grain;
- a copular restatement whose semantic job is already the retained LABEL or LOCATOR;
- repeated or paraphrased mentions of an already retained predicate;
- discourse management, filler, or quotation-introduction fragments unless that act itself materially matters.

Keep distinct stance/relation predicates when the stance/relation materially matters. Keep a separately meaningful embedded modal/normative predicate when it carries an independent relation. Negation, questions, intentions, hypotheticals, recurrence, and future posture do not erase a distinct semantic predicate.

Use the shortest source-near predicate form that preserves its semantic job and posture. Inventorying a predicate never asserts that its event happened.

## LOCATOR

LOCATOR is an independently useful location/path/containment/position/direction relation. It is not every prepositional phrase or contextual clause.

Retain physical setting relations, contained-setting relations, movement/path relations, accompaniment when materially locational, destination/path constructions, position relations, and explicit internal/figurative location constructions when they genuinely function as a locating relation.

Do not create LOCATOR from:

- temporal subordinate clauses merely because they provide context;
- possession, recipient, source, topic, comparison support, or grammatical complement marking;
- abstract argument phrases that do not independently locate material;
- ordinary predicate complements whose relation is already represented elsewhere.

A repeated position wording may remain distinct when it supplies a materially different locating relation rather than merely repeating the same place. Evaluate LOCATOR independently from PLACE/TIME, but do not use it as a catch-all relational class.

When broad and contained setting relations arise together, broad comes first.

## qualities_available

`qualities_available` is only a boolean. Set true when the source supplies material qualities/descriptions associated with the coordinate, otherwise false. Do not create, split, score, or interpret qualities merely to justify the boolean. `Q` is never a unit reference.

## Ordering and apparatus boundary

The apparatus, not the worker, owns final canonical IDs, deterministic numbering, exact-source validation, ordering enforcement, compound reference validation, `_Q` construction, SQL-ready shaping, retries, and failure handling.

Default within-class order is first material source anchor after filtering and coreference resolution, with these semantic tie rules:

- whole/broad setting before dependent part/contained setting when first introduced together;
- PERSON follows participation order;
- memories, reports, hypotheticals, and future frames stay at source position rather than being reordered into real-world chronology.

The worker must not depend on preexisting canonical IDs.

## Compounds

After units are final, map the story at lightweight event/proposition grain using only retained units.

Create one compound for each materially distinct represented situation, assertion, question, correction, comparison, reflection, or prospective proposition useful for reconnecting the inventory.

A compound binds already-retained coordinates. It must not create semantics, justify unnecessary units, or repair a missing unit. Keep jointly expressed pieces together when they form one proposition; split materially different propositions. Do not make compounds for grammatical fragments that failed the coordinate gate.

Use registered unit references only.

## Forbidden work

Do not perform APA parsing, protected-thread analysis, psychological interpretation, scoring, promotion, APA-ID creation, executive analysis, or Oval Office writes. Never present a candidate inventory as established truth.
