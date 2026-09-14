# APA RESEARCHER INVENTORY — DURABLE AGENT CONTRACT V23

Status: ACTIVE CALIBRATION SUCCESSOR — NOT CERTIFIED
Date: 2026-09-14
Predecessor: `researcher_inventory/AGENT_CONTRACT_V22.md`
Authority: Leah’s standing Researcher Inventory calibration directive
Scope: semantic extraction worker only
Promotion authority: NONE

## Forward-control effect

`AGENT_CONTRACT_V22.md` remains immutable historical evidence for the V22 lineage and its failed calibration attempts.

V23 supersedes V22 only for forward Researcher Inventory calibration behavior. The evaluator, immutable Case 2/Case 6 gold workbooks, holdout boundary, candidate-only status, no-promotion rule, and clean-room certification gate remain unchanged.

## 1. Mission

Produce a lightweight literal inventory of represented coordinates in the supplied source.

This is inventory, not interpretation. Read the complete source before answering a requested class, then scan it again from beginning to end for omissions.

The worker has no archetype, gold-answer, expected-count, evaluator-finding, prior-scored-output, sealed-holdout-source, or holdout-output access.

## 2. Mechanical admission rule

For the requested class, retain a row when all of the following are true:

1. the coordinate is represented by the source;
2. it performs the positive job of the requested class;
3. it is not invented from background knowledge or merely grammatically possible;
4. it is not a true same-class duplicate after alias/coreference resolution; and
5. it is not grammatical debris with no coordinate of its own.

There is **no additional importance, salience, researcher-selectability, reconnective-value, or material-loss test**.

Do not discard a represented class member because it is local, unnamed, ordinary, nested, repeated in another class, or seems less important than a nearby row.

Do not create rows merely because a word or clause could theoretically be described as belonging to the class. The source must actually represent the coordinate doing that class job.

## 3. Exact-source lock

Never substitute synonyms or convenient paraphrases.

For every explicit row:

1. identify the coordinate in the source;
2. select the shortest complete **contiguous** source substring that carries it;
3. copy that substring exactly into `source_wording`;
4. copy an exact bounded source substring into `source_cue`;
5. only then create the short tag.

Preserve original punctuation, apostrophes, hyphens, capitalization, spelling, dialect, questions, negation, comparison, and attribution as needed by the coordinate.

Never construct `source_wording` by deleting words from the middle of a phrase or stitching non-contiguous source fragments together.

Only an unnamed PLACE or TIME may use `source_wording = null`. Its `source_cue` must still be an exact source substring that proves the represented scene/frame, and its tag must remain a neutral description rather than an invented place name or date.

## 4. Cross-class overlap

Classes are independent inventories.

Do not suppress a valid row because the same source span or represented material also performs a different class job. A source phrase may legitimately support more than one class when each class’s positive job is actually present.

Cross-class overlap is not same-class duplication.

## 5. Alias and duplicate rule

Resolve aliases, pronouns, repeated mentions, kinship references, and true coreference before counting same-class coordinates.

Merge repeated mentions only when they are the same represented coordinate. Do not merge merely because two coordinates occur in the same scene, time, sentence, or proposition.

## 6. PLACE

Positive job: a represented **where-coordinate**.

Inventory distinct represented settings, contained settings, scene positions, object positions that are themselves represented as locations, origins, destinations, waiting/interaction positions, later-conversation/report settings, and present-telling settings.

A place need not be physically named. If a represented occurrence, interaction, relation, or report has a distinct where-slot but the source does not name the location, retain an unnamed PLACE with `source_wording = null` and an exact source cue.

Do not create PLACE from a purely figurative or grammatical phrase when no represented where-coordinate exists.

## 7. TIME

Positive job: a represented **episode, frame, span, recurrence, or prospective temporal coordinate**.

Inventory temporal coordinates in source progression, including distinct attempts, response/help episodes, transitions/departures, waits, intended periods, later conversations/reports, standing or recurring spans, changed-state periods, present reflection, and represented future/prospective frames.

TIME does not require a clock, date, duration word, or explicit temporal noun.

Do not create a separate TIME for every verb. Keep actions together when the source represents them inside the same episode/frame; split when source progression or represented posture establishes a distinct episode/frame.

For unnamed TIME use `source_wording = null` and an exact source cue.

## 8. PERSON

Positive job: a represented human actor or stable human/social group.

Inventory the speaker plus represented people/groups who act, speak, perceive, are acted upon, own or source a represented relation, receive an action, or are represented participants/beneficiaries whose identity is part of the story.

Speaker canonical key is `B`. Resolve aliases and pronouns before counting.

## 9. OBJECT

Positive job: a represented referable **thing**.

Inventory concrete things, abstract/internal things, source-distinguished wholes and parts, values/amounts, sets/categories, services/results, decisions/next steps, contemplated choices, and relations that the source itself treats as referable things.

Do not turn every action, predicate, clause, state, or noun phrase into OBJECT merely because it can be nominalized.

A source-distinguished part may remain separate from its whole when both are represented as referents.

## 10. LABEL

Positive job: a source-applied **characterization**.

Inventory represented qualities, states, identities, self-labels, evaluations, comparisons, corrections, rejections, and characterization phrases/questions.

A LABEL answers the source-level characterization job, not merely the action/relation job. Do not create LABEL for every predicate, quantity, or modifier.

Use the shortest complete contiguous source phrase that names the characterization. Preserve polarity or qualification when it belongs to the characterization itself. Do not splice a cleaner phrase out of non-contiguous words.

LABEL is independent from `qualities_available` and may overlap another class when the same source language also performs that other class job.

## 11. VERB

Positive job: a represented lexical **action or relation edge**.

Inventory each distinct lexical predicate increment that contributes its own represented relation/action. Include matrix, embedded, reported, perception, thought, state, purpose, negated, questioned, hypothetical, intended, recurring, and future predicates when they contribute a distinct source relation.

Use the shortest complete contiguous source-near predicate construction. Split coordinated or nested predicates when each contributes a different relation edge. Do not split bare auxiliaries, support markers, or grammatical connectors that do not carry a relation of their own.

Inventorying a VERB preserves source posture; it does not assert that the event happened.

## 12. LOCATOR

Positive job: a represented **locating or contextual relation**.

Inventory source increments that situate a person, thing, action, or state relative to a setting, position, direction, path, origin, destination, containment, proximity, movement, accompaniment/association when it locates participants relative to one another, recurring context, or genuine figurative/mental location relation.

Use the smallest complete meaningful contiguous construction, not an isolated preposition.

Do not create LOCATOR from a phrase that has no locating/contextual job. Temporal/context overlap is allowed when the same source wording independently situates the represented material.

## 13. `qualities_available`

`qualities_available` is a boolean only.

Set it `true` when the source supplies descriptive/qualifying language associated with that coordinate; otherwise set it `false`.

Do not create, suppress, or reinterpret inventory rows merely to control this boolean. `Q` is never a unit.

## 14. Ordering

Order each class by the earliest source anchor of the resolved represented coordinate.

When broad and contained coordinates share one source situation, preserve broad-to-contained order through the supplied ordering fields.

For PERSON, the speaker remains first; other people follow the apparatus’s participation/coreference ordering rule.

## 15. Compounds

Build compounds only after units are final.

Create one lightweight compound for each distinct represented proposition/relation at the source’s story grain, including action/relation propositions, characterization propositions, questions, corrections, comparisons, reflections, and prospective relations.

Use only retained unit references. Include all retained units that materially participate in that proposition. Include a retained PLACE, TIME, or LOCATOR only when it actually governs or locates that proposition.

Do not manufacture compounds from arbitrary subsets or optional variants. A compound never repairs a missing unit and never creates new semantics.

## 16. Final self-check

Before returning a class result:

1. scan the source from start to finish for omitted represented members of that class;
2. verify every explicit `source_wording` is one exact contiguous source substring;
3. verify every `source_cue` is one exact contiguous source substring;
4. remove only aliases, true same-class duplicates, unsupported invention, and grammatical debris;
5. confirm that no row was removed merely for being local, ordinary, cross-class-overlapping, or judged unimportant.

Before returning compounds, verify that every referenced unit exists and that no compound is only a duplicate subset/variant of another.

## 17. Hard boundaries

Never perform APA scoring, protected-thread analysis, psychological interpretation, research conclusions, promotion, Oval Office research writing, APA-ID creation, or sovereign data admission.

Calibration output remains candidate material only.

Never access or infer sealed holdout material during calibration. The sealed holdout may run only after the external harness has independently established repeated archetype passes under this same finalized contract.
