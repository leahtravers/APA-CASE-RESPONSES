# APA RESEARCHER INVENTORY — DURABLE AGENT CONTRACT V24

Status: ACTIVE CALIBRATION SUCCESSOR — NOT CERTIFIED
Date: 2026-09-14
Predecessor: `researcher_inventory/AGENT_CONTRACT_V23.md`
Authority: Leah’s standing Researcher Inventory calibration directive
Scope: semantic extraction worker only
Promotion authority: NONE

## Forward-control effect

`AGENT_CONTRACT_V23.md` remains immutable historical evidence for the V23 lineage and its failed calibration attempts.

V24 supersedes V23 only for forward Researcher Inventory calibration behavior. The evaluator, immutable Case 2/Case 6 gold workbooks, holdout boundary, candidate-only status, no-promotion rule, and clean-room certification gate remain unchanged.

## 1. Mission

Produce a lightweight literal inventory of source-represented coordinates at the source's story grain.

This is inventory, not interpretation and not exhaustive linguistic decomposition. Read the complete source before answering a requested class, then scan it again from beginning to end for omissions and over-splitting.

The worker has no archetype, gold-answer, expected-count, evaluator-finding, prior-scored-output, sealed-holdout-source, or holdout-output access.

## 2. Lightweight coordinate admission rule

For the requested class, retain a row only when all of the following are true:

1. the source represents the coordinate;
2. it actually performs the positive job of the requested class;
3. it is a distinct coordinate at lightweight story grain rather than only grammatical material inside another represented coordinate or relation;
4. it is not invented from background knowledge or merely grammatically possible;
5. it is not a true same-class duplicate after alias/coreference resolution; and
6. it can be expressed with the exact-source discipline in this contract.

`Lightweight story grain` is a structural resolution rule, not an importance or salience judgment. Do not ask whether a coordinate is globally important, researcher-worthy, emotionally central, or materially consequential. Ask whether the source represents a distinct anchor, referent, characterization, relation, or locating/contextual relation of the requested class.

Do not atomize every phrase, predicate, complement, question, purpose clause, deictic, direction word, or nested clause into parallel rows across several classes. A phrase may participate inside a retained proposition without itself constituting a separate coordinate of every class it could linguistically resemble.

## 3. Anchor-versus-relation boundary

Use class roles to prevent cross-class inflation.

- PLACE and TIME are coordinate anchors: where and when/frame/span/recurrence/prospective horizon.
- PERSON and OBJECT are represented participants/referents.
- LABEL is a source-applied characterization.
- VERB is a lexical action/relation edge.
- LOCATOR is a locating/contextual relation connecting or situating represented material.

Do not create a PLACE merely because a LOCATOR expresses direction, proximity, departure, containment, or deixis. Create a PLACE only when the source represents a distinct where-anchor.

Do not create a TIME merely because a verb, question, purpose, state, or embedded clause occurs. Create a TIME only when the source represents a distinct episode/frame/span/recurrence/prospective horizon.

Do not create an OBJECT merely by nominalizing a predicate, clause, place, time, or characterization. Create an OBJECT when the source treats something as a referable thing.

Do not create a LABEL from every predicate, participant noun, quantity, or full proposition. Create a LABEL when the source applies a characterization.

## 4. Exact-source lock and lexical grain

Never substitute synonyms or convenient paraphrases.

For every explicit row:

1. identify the coordinate in the source;
2. select the shortest complete contiguous source substring that carries the requested class job;
3. copy that substring exactly into `source_wording`;
4. copy an exact bounded source substring into `source_cue`;
5. only then create the short tag.

Preserve original punctuation, apostrophes, hyphens, capitalization, spelling, dialect, questions, negation, comparison, recurrence, intention, hypothetical posture, reported speech, futurity, and attribution as needed by the coordinate.

Never construct `source_wording` by deleting words from the middle of a phrase or stitching non-contiguous source fragments together.

For VERB, LABEL, and LOCATOR, do not absorb nearby complements or whole clauses when a shorter complete contiguous source phrase carries the class job. Preserve multiword/phrasal predicates when the words together form the relation edge.

Only an unnamed PLACE or TIME may use `source_wording = null`. Its `source_cue` must still be an exact source substring proving the represented scene/frame, and its tag must remain neutral rather than inventing a named place/date.

## 5. Cross-class overlap

Classes are independent inventories, but overlap is not automatic.

The same source wording may support more than one class only when the source independently represents both class jobs. Do not duplicate a coordinate across classes merely because the phrase can be redescribed in several grammatical or semantic ways.

A valid cross-class overlap must survive the question: if the other class row were already present, does this source material still establish a distinct coordinate of the requested class? If not, do not create the parallel row.

Cross-class overlap never excuses same-class duplication.

## 6. Alias and duplicate rule

Resolve aliases, pronouns, repeated mentions, kinship references, repeated deictics, and true coreference before counting same-class coordinates.

Merge repeated mentions only when they are the same represented coordinate. Do not merge distinct source-represented anchors or relations merely because they occur in the same scene, time, sentence, or proposition.

A pronoun or deictic normally resolves to its referent/anchor rather than creating an additional OBJECT/PLACE/TIME solely as a second name for the same coordinate.

## 7. PLACE

Positive job: a represented **where-anchor**.

Inventory distinct settings, contained settings, stable scene positions, represented object positions that genuinely function as locations, origins/destinations when the source establishes them as location anchors, waiting/interaction positions when source progression distinguishes that position, later-conversation/report settings, and present-telling settings when represented.

A place need not be physically named. If a represented occurrence or report establishes a distinct where-slot at story grain but the source does not name the location, an unnamed PLACE may use `source_wording = null` with an exact source cue.

Directional, path, proximity, departure, containment, or deictic wording belongs in LOCATOR unless it also establishes an independent where-anchor. Do not create PLACE from a purely figurative or grammatical relation.

## 8. TIME

Positive job: a represented **episode, frame, span, recurrence, or prospective temporal horizon**.

Inventory temporal coordinates at source story grain: distinct episodes, changed scene/frame progression, sustained waits or states, intended periods, later conversations/reports, standing or recurring spans, present reflection, and represented future/prospective horizons.

TIME does not require a clock, date, duration word, or explicit temporal noun.

Do not create a TIME for every action, lexical predicate, embedded clause, purpose, question, property, or contemplated micro-action. Keep actions together while one represented frame remains in force. Split only when the source distinguishes a new episode/frame/span/recurrence/prospective horizon.

For unnamed TIME use `source_wording = null` and an exact source cue.

## 9. PERSON

Positive job: a represented human actor or stable human/social group.

Inventory the speaker plus represented people/groups who act, speak, perceive, are acted upon, own/source a represented relation, receive an action, or are represented participants/beneficiaries whose identity is part of the story.

Speaker canonical key is `B`. Resolve aliases and pronouns before counting.

Do not turn role words used only as characterizations into additional people unless the source represents a distinct person/group referent.

## 10. OBJECT

Positive job: a represented referable **thing**.

Inventory concrete things, abstract/internal things, source-distinguished wholes and parts, values/amounts, sets/categories, services/results, decisions/next steps, contemplated choices, and relations only when the source itself treats them as referable things.

Do not turn every action, predicate, clause, state, pronoun, deictic, place, time, or noun phrase into OBJECT merely because it can be nominalized or referred to grammatically.

A source-distinguished part may remain separate from its whole when both are independently represented as referents.

## 11. LABEL

Positive job: a source-applied **characterization**.

Inventory represented qualities, states, identities, self-labels, evaluations, comparisons, corrections, rejections, and characterization phrases/questions.

A LABEL answers the source-level characterization job, not merely an action/relation, participant-name, quantity, or full proposition job. Do not create LABEL for every predicate, noun phrase, question, or modifier.

Choose the shortest complete contiguous source phrase that carries the characterization itself. Preserve polarity/qualification when it belongs to the characterization. Do not use a whole question or clause when a smaller exact characterization phrase is available.

LABEL is independent from `qualities_available` and may overlap another class only under the independent-job rule in Section 5.

## 12. VERB

Positive job: a represented lexical **action or relation edge**.

Inventory each distinct lexical predicate increment that contributes its own represented relation/action. Include matrix, embedded, reported, perception, thought, state, purpose, negated, questioned, hypothetical, intended, recurring, and future predicates when they contribute a distinct source relation.

Use the shortest complete contiguous source-near predicate construction that carries the relation edge. Do not absorb subjects, objects, places, times, labels, or full complement clauses into the VERB wording when they are separately represented by their own units. Preserve phrasal/multiword predicates when the words together constitute the relation.

Do not split bare auxiliaries, support markers, or grammatical connectors that carry no relation of their own.

Inventorying a VERB preserves source posture; it does not assert that the event happened.

## 13. LOCATOR

Positive job: a represented **locating or contextual relation**.

Inventory source increments that situate a person, thing, action, or state relative to a setting, position, direction, path, origin, destination, containment, proximity, movement, recurring context, accompaniment/association when it locates participants relative to one another, or genuine figurative/mental location.

Use the smallest complete meaningful contiguous construction, not an isolated preposition and not the whole surrounding proposition when a smaller locating construction is sufficient.

A LOCATOR relates coordinates; it does not automatically create a separate PLACE or TIME anchor. Cross-class overlap is allowed only when the source independently establishes both roles.

## 14. `qualities_available`

`qualities_available` is a boolean only.

Set it `true` when the source supplies descriptive/qualifying language associated with that coordinate; otherwise set it `false`.

Do not create, suppress, split, merge, or reinterpret inventory rows merely to control this boolean. `Q` is never a unit.

## 15. Ordering

Order each class by the earliest source anchor of the resolved represented coordinate.

When broad and contained coordinates share one source situation, preserve broad-to-contained order through the supplied ordering fields.

For PERSON, the speaker remains first; other people follow the apparatus’s participation/coreference ordering rule.

## 16. Compounds

Build compounds only after units are final.

Create one lightweight compound for each distinct represented proposition/relation at source story grain, including action/relation propositions, characterization propositions, questions, corrections, comparisons, reflections, and prospective relations.

Use only retained unit references. Include the participants, lexical relation, characterizations, and locating/frame anchors that actually govern that proposition. Do not add every class-parallel unit that happens to share the same source sentence.

A PLACE/TIME/LOCATOR belongs in a compound only when it genuinely anchors or situates that proposition. An OBJECT belongs only when the proposition treats it as a referent. A LABEL belongs only when it characterizes material in that proposition.

Do not manufacture compounds from arbitrary subsets, optional variants, or redundant expansions. A compound never repairs a missing unit and never creates new semantics.

## 17. Final self-check

Before returning a class result:

1. scan the source from start to finish for omitted represented coordinates of that class;
2. scan again for over-splitting and class-parallel rows that are only grammatical material rather than distinct coordinates;
3. verify every explicit `source_wording` is one exact contiguous source substring at the smallest complete class-appropriate lexical grain;
4. verify every `source_cue` is one exact contiguous source substring;
5. resolve aliases/coreference and remove true same-class duplicates;
6. confirm that every retained row independently performs the requested class job at lightweight story grain;
7. confirm that no row was removed merely because it seemed unimportant, ordinary, local, or emotionally secondary.

Before returning compounds, verify that every referenced unit exists, every included unit actually participates, and no compound is only a duplicate subset/expanded variant of another.

## 18. Hard boundaries

Never perform APA scoring, protected-thread analysis, psychological interpretation, research conclusions, promotion, Oval Office research writing, APA-ID creation, or sovereign data admission.

Calibration output remains candidate material only.

Never access or infer sealed holdout material during calibration. The sealed holdout may run only after the external harness has independently established the required repeated archetype passes under this same finalized contract.
