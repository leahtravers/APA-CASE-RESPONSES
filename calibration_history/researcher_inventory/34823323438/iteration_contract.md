# APA RESEARCHER INVENTORY — DURABLE AGENT CONTRACT V25

Status: ACTIVE CALIBRATION SUCCESSOR — NOT CERTIFIED
Date: 2026-09-14
Predecessor: `researcher_inventory/AGENT_CONTRACT_V24.md`
Authority: Leah’s standing Researcher Inventory calibration directive
Scope: semantic extraction worker only
Promotion authority: NONE

## Forward-control effect

V24 remains immutable historical evidence for its calibration lineage and failed attempts. V25 supersedes V24 only for forward Researcher Inventory worker behavior. Immutable Case 2/Case 6 gold workbooks, evaluator logic, holdout isolation, candidate-only status, no-promotion rule, and clean-room certification gate are unchanged.

## 1. Mission

Produce a lightweight literal inventory of what the source itself presents as separate coordinates at story grain.

Inventory only. Do not interpret, improve, explain, normalize, or exhaustively decompose the language.

The worker never receives archetypes, gold answers, expected counts, evaluator findings, prior scored outputs, sealed-holdout source, or holdout outputs.

## 2. The one admission test

For the requested class, create a row only when the source itself presents **one separate coordinate whose job is that class**.

If the words merely help express a larger proposition, do not create an additional row for them.

If the same material is already represented by another retained coordinate and does not independently do the requested class job, do not create a class-parallel duplicate.

If uncertain whether a phrase deserves its own row, **do less**: omit the extra row rather than inventing, paraphrasing, qualifying, or decomposing it.

This is not an importance or salience test. Ordinary and emotionally minor coordinates remain eligible when the source actually presents them separately.

## 3. Literal source rule

Never substitute synonyms.

For an explicit row, `source_wording` must be the shortest complete contiguous source substring that performs that row’s class job. Copy it exactly. `source_cue` must also be one exact bounded contiguous source substring.

Do not delete words from the middle. Do not stitch separated source fragments. Do not rewrite dialect, spelling, punctuation, negation, questions, uncertainty, comparison, attribution, or tense.

Only an unnamed PLACE or TIME may use `source_wording = null`. It still requires an exact source cue proving the represented where/when frame.

## 4. Class jobs

### PLACE
A PLACE is **where** a represented occurrence, state, interaction, or thing is situated at story grain.

A place does not need a physical name. If the source clearly establishes that something happened somewhere but leaves the location unnamed, retain the unnamed where-coordinate. Do not create extra PLACE rows from mere direction, deixis, path wording, mental metaphor, or every contained noun.

### TIME
A TIME is **when / the distinct episode, frame, span, recurrence, or prospective period in which something is represented as happening**.

A time does not need a date, clock time, or duration phrase. Do not create one TIME for every action, question, clause, or predicate inside the same episode.

### PERSON
A PERSON is a represented **human referent or stable human group**.

Retain real represented people/groups whether named or unnamed. Resolve pronouns, kinship terms, aliases, and repeated mentions to the same person/group before counting. Do not create a PERSON from a descriptive role word when no separate human referent is represented.

### OBJECT
An OBJECT is a source-presented **thing** that is itself referable at story grain.

It may be concrete or abstract. Do not turn actions, clauses, states, places, times, pronouns, or every noun phrase into separate objects merely because grammar permits referring to them.

### LABEL
A LABEL is a source-applied **characterization** whose primary job is to characterize.

Do not duplicate the same material as LABEL merely because an action/state/predicate can also be described as a quality. Do not turn every modifier, question, comparison, or predicate fragment into a LABEL.

### VERB
A VERB is one source-presented **meaningful action or relation predicate** at proposition grain.

Keep the complete predicate construction needed to express that relation. Do not split auxiliaries, copulas, support words, infinitival pieces, or nested grammatical fragments into separate VERB rows unless the source presents a genuinely separate relation. Do not create multiple VERB rows merely because several verb-shaped words occur inside one predicate construction.

### LOCATOR
A LOCATOR is one source-presented **locating or contextual relation** that situates represented material relative to something else.

Keep one meaningful locating construction. Do not turn each preposition, direction word, deictic, or nested location phrase into its own LOCATOR. A LOCATOR does not by itself create a PLACE, TIME, or OBJECT.

## 5. Coreference and duplication

Read the whole source before finalizing a class.

Resolve repeated mentions and coreference first. Then remove true same-class duplicates.

Do not merge genuinely different coordinates merely because they occur in one sentence or scene. Do not split one coordinate merely because it is mentioned several times.

## 6. `qualities_available`

`qualities_available` is only a boolean.

Set it true when descriptive or qualifying language is associated with the retained coordinate; otherwise false.

Do not create, split, suppress, or retype a row to control this flag. Q is never a unit.

## 7. Ordering

Order retained coordinates by their first source anchor after coreference resolution.

Keep the speaker first in PERSON. When a broad and contained PLACE share the same source anchor, place the broader setting before the contained setting.

## 8. Compounds

Build compounds only after the unit inventories are final.

Create one lightweight compound for one source-presented proposition/relation at story grain. Use only retained units that actually participate in that proposition.

Do not create a unit merely to make a compound fuller. Do not create arbitrary subset variants or expanded duplicates. Do not attach every PLACE/TIME/LABEL/LOCATOR that happens to occur in the same sentence.

## 9. Mechanical final pass

Before returning a class:

1. Read the source from beginning to end.
2. For each proposed row ask only: **Does the source itself present this as one separate coordinate doing this class job?**
3. If no, remove it.
4. If ambiguous, remove it.
5. Resolve aliases/coreference and remove same-class duplicates.
6. Confirm every explicit `source_wording` and every `source_cue` is exact contiguous source text.
7. Confirm no synonym or invented qualification appears.
8. Confirm unnamed PLACE/TIME coordinates were not lost merely because no location/date was stated.

Before returning compounds, confirm every referenced unit already exists and every compound is one source proposition at lightweight grain.

## 10. Posture

Questions, negation, hypotheticals, intentions, comparisons, reported speech, recurrence, and prospective material retain their source posture. Inventorying represented material does not assert that it actually occurred when the source does not assert occurrence.

## 11. Hard boundaries

Never perform APA scoring, protected-thread analysis, psychological interpretation, research conclusions, promotion, Oval Office research writing, APA-ID creation, or sovereign data admission.

Calibration output remains candidate material only.

Never access, request, reconstruct, or infer sealed holdout material during calibration. The holdout may run only after the external harness independently establishes the required repeated archetype passes under this same finalized contract.