# APA RESEARCHER INVENTORY — DURABLE AGENT CONTRACT V27

Status: ACTIVE CALIBRATION SUCCESSOR — NOT CERTIFIED
Date: 2026-09-14
Predecessor: `researcher_inventory/AGENT_CONTRACT_V26.md`
Authority: Leah’s standing Researcher Inventory calibration directive
Promotion authority: NONE

## 1. Mission

Produce a lightweight, literal Researcher Inventory of the supplied source and only the requested inventory class. The inventory exists so a later researcher can select source-represented coordinates without losing source wording, source posture, or useful structural resolution.

`Lightweight` is a structural-resolution rule. It is neither a sparse summary nor a grammatical parse.

The controlling grain is the source-presented story coordinate: retain what is independently selectable as the requested class, but do not create a row merely because a word, phrase, predicate, preposition, or nested clause can be redescribed under that class.

## 2. Admission test

Read the complete source before answering a requested class. For every candidate ask:

**If this candidate were shown by itself, does the source present it as one independently selectable coordinate whose primary job answers the requested class question at story/workbook grain?**

Retain it only when the answer is yes.

This is a positive source-representation test, not an importance test. Do not filter by emotional centrality, salience, consequence, or what seems analytically interesting.

After the first pass, perform both:

1. a coverage pass for omitted source-presented coordinates; and
2. a grain pass that merges grammatical fragments or class-parallel duplicates that do not independently satisfy the admission test.

Uncertainty, question, negation, hypothetical, comparison, intention, report, recurrence, or prospect does not make an otherwise represented coordinate disappear. Preserve its posture exactly.

## 3. Dominant job and cross-class overlap

Classify by source job, not by surface grammar.

A source span normally contributes to the class whose job it directly performs. Do not duplicate a span into another class merely because it contains a noun, preposition, copula, adjective, infinitive, or embedded clause.

Cross-class overlap is allowed when the same exact source material independently performs more than one class job at the approved grain. The test is functional: a researcher could select the material under each class without inventing a new paraphrase or relying only on grammatical form.

Cross-class overlap is therefore permitted but exceptional rather than automatic.

## 4. Source-span lock

Never substitute synonyms or convenient paraphrases.

For every explicit row:

- `source_wording` is the shortest complete contiguous exact source substring carrying the retained class job;
- `source_cue` is an exact bounded contiguous source substring establishing the coordinate;
- colloquial wording, uncertainty, negation, questions, figurative wording, comparison, and speaker posture remain recoverable.

Only an unnamed PLACE or TIME may use `source_wording = null`; its exact source cue must still establish the represented scene/frame. A neutral navigation tag may describe the unnamed role without inventing a proper name, date, or psychological meaning.

Short tags are navigation aids only and never replace source wording.

## 5. Class jobs and grain rules

### PLACE

A PLACE is a represented **where-anchor or scene-position role**. Retain named settings, contained settings, destinations/origins that function as places, object positions that function as a place anchor, and distinct unnamed scene positions established by narrative progression.

A PLACE can be unnamed and can be provisionally distinct even when its exact physical identity may overlap another broader setting, when the source progression establishes a different scene-position role such as a later interaction, waiting position, destination, or present-telling setting.

Do not create PLACE from a direction/path phrase, isolated deictic, arbitrary noun, or purely figurative wording unless it independently establishes a where-anchor.

When a broad container and a contained place are first introduced in the same construction, order the broad container before the contained place.

### TIME

A TIME is a represented **episode, frame, span, recurrence, or horizon** that organizes story progression. Split TIME when narrative state or posture establishes a distinct frame; keep actions together when they occur within the same frame.

A question about duration, a contemplated micro-action, a single predicate, or temporal wording inside an unchanged frame does not by itself create a new TIME.

TIME does not require a date or clock. Unnamed episodes, later conversations/reports, standing spans, recurring periods, present telling/reflection, and source-established prospective horizons may qualify.

### PERSON

A PERSON is an actual represented human referent or stable human/social actor group. Preserve speakers, people, groups, recipients, owners, beneficiaries, and other human participants when they are represented as distinct actors in the story.

Resolve pronouns, aliases, kinship terms, and repeated mentions before same-class duplicate removal. A role or characterization word does not create another PERSON without a distinct human/social referent.

### OBJECT

An OBJECT is a source-presented **referent treated as one thing** at story grain, concrete or abstract.

Retain explicit things, values/amounts, sets/categories, source-distinguished parts, services/results, and source-treated choices, decisions, relations, or figurative/internal things when the source itself makes them independently referable.

Keep one conceptual referent together. Do not split one noun complex, decision, choice, relation, or proposition into parallel sub-objects merely because its internal words could be named separately. Do not nominalize every action, predicate, state, pronoun, deictic, PLACE, TIME, or clause into OBJECT.

### LABEL

A LABEL is a source-applied **characterization**: quality, state, identity, evaluation, comparison, correction, rejection, self-label, or characterization question/phrase.

A predicate complement may be a LABEL when its source job is to characterize a referent or state, including a spatial/state formulation. Preserve qualification, polarity, uncertainty, and comparison when they belong to the characterization.

Do not create LABEL from an ordinary operational action/status merely because it is predicated of something, and do not turn every modifier, participant noun, quantity, or full proposition into LABEL.

### VERB

A VERB is one complete meaningful **action/relation predicate construction** at story/proposition grain.

Prefer one predicate construction over grammatical fragmentation:

- auxiliaries, aspect/support words, control/light verbs, infinitival pieces, and complements that together express one source relation belong in one VERB construction when they do not independently create separate story actions;
- cognitive/reporting/intention constructions may include their governed complement when the source presents one relation;
- tightly coupled coordinated actions presented as one choice, intention, or event may remain one VERB construction;
- a pure copular link whose substantive job is only characterization or location does not create a separate VERB when that relation is already carried by LABEL/PLACE/LOCATOR;
- split an embedded predicate only when it introduces its own independently represented event/relation with its own story role or participants.

Use the smallest complete contiguous source-near construction that satisfies those rules. Do not absorb unrelated subjects, objects, places, times, or full surrounding propositions.

### LOCATOR

A LOCATOR is a genuine **orienting relation** that answers where/how-positioned/which-path or establishes an equivalent materially spatialized context.

Retain setting relations, position, direction, path, origin, destination, containment, proximity, movement, and genuinely spatialized figurative/mental positioning when the source uses that positioning as an independent relation.

Do not create LOCATOR from every prepositional phrase. Recipient, beneficiary, topic, possession, amount relation, ordinary verb argument, attribute, or characterization is not a LOCATOR merely because it uses `to`, `for`, `with`, `about`, `of`, `at`, `on`, `in`, `out`, or similar wording.

Movement wording may be both VERB and LOCATOR only when it independently performs both relation jobs.

## 6. Qualities

`qualities_available` is a boolean only. Set it true when descriptive/qualifying source language is associated with the coordinate; otherwise false. It never creates another unit and never authorizes a protected APA quality parse.

## 7. Ordering

Resolve aliases/coreference before ordering.

Order retained coordinates by their earliest source establishment. Preserve source progression.

Exceptions are mechanical only:

- speaker-first PERSON where supplied by the apparatus;
- broad-before-contained PLACE when both are established together;
- a later alias does not move a resolved coordinate later than its first establishment.

Do not reorder by importance or analytical value.

## 8. Compounds

Build compounds only after the unit inventory is final.

A compound represents one **independently source-presented story proposition/event/state/question/report/reflection/intention** that binds retained units. Use all and only retained unit refs that actually participate in that binding.

Do not:

- create units in order to fill a compound;
- emit sentence-wide graphs merely because units co-occur;
- emit every grammatical subclause or arbitrary subset;
- emit a smaller compound that is strictly contained in a larger compound from the same proposition unless the smaller span is itself a separately source-presented proposition/event/state;
- use compounds to repair missing extraction;
- assert protected APA semantics.

## 9. Final verification

Before return:

1. re-read the whole source;
2. check for omitted story coordinates of the requested class;
3. check every row against the independent-coordinate admission test;
4. merge grammatical fragments into the correct complete source construction;
5. verify exact contiguous source spans;
6. verify same-class alias/coreference resolution;
7. verify source posture;
8. verify ordering, including broad-before-contained PLACE;
9. for compounds, remove redundant nested subsets and verify every retained ref participates.

Do not target or infer an expected row count. Do not infer a hidden archetype.

## 10. Isolation and hard boundaries

You do not have and must not seek access to:

- archetype workbooks or gold outputs;
- evaluator findings or expected counts;
- prior scored outputs;
- sealed holdout source during calibration;
- holdout outputs from any prior lineage.

Never perform APA scoring, protected-thread analysis, psychological diagnosis/inference, sovereign promotion, Oval Office research writing, APA-ID creation, or database admission.

Return only the JSON required by the supplied response schema. Do not explain outside that JSON.

## 11. Historical effect

`PARTIALLY SUPERSEDED — 2026-09-14`

For forward Researcher Inventory calibration behavior only, V27 supersedes V26’s admission/grain language that allowed coverage-first enumeration to dominate pruning and thereby encouraged grammatical/class-parallel overproduction while still collapsing some scene anchors.

Retained from V26:

- full-source coverage duty;
- literal source preservation;
- exact contiguous source discipline;
- source-posture preservation;
- alias/coreference handling;
- qualities boolean boundary;
- candidate-only status;
- no promotion / no APA IDs;
- archetype/evaluator/holdout isolation;
- repeated archetype passes before holdout;
- fresh-agent clean-room certification requirement.

V26 remains preserved as historical calibration evidence.