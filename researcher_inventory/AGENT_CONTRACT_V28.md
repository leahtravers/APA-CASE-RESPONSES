# APA RESEARCHER INVENTORY — DURABLE AGENT CONTRACT V28

Status: ACTIVE CALIBRATION SUCCESSOR — NOT CERTIFIED
Date: 2026-09-14
Predecessor: `researcher_inventory/AGENT_CONTRACT_V27.md`
Authority: Leah’s standing Researcher Inventory calibration directive
Promotion authority: NONE

## 1. Mission and two-layer architecture

Produce a lightweight, literal Researcher Inventory of the supplied source and only the requested inventory class.

The inventory has two distinct layers:

1. **UNIT LAYER** — preserve source-represented selectable coordinates at the smallest complete function-bearing grain for the requested class.
2. **COMPOUND LAYER** — reconnect already-retained units into source-presented propositions, events, states, questions, reports, reflections, intentions, or relations.

Do not make the unit layer proposition-sized merely because compounds will later bind it. Do not make the unit layer token-sized merely because individual words can be grammatically labeled.

`Lightweight` means enough resolution to preserve materially distinct source coordinates without grammatical debris, paraphrase, or invented structure.

## 2. Unit admission test

Read the complete source before answering a requested class.

Retain a candidate when all are true:

1. the source itself represents the candidate or, for an unnamed PLACE/TIME, establishes the corresponding scene/frame;
2. the candidate performs a genuine function of the requested class;
3. the candidate is independently useful as a selectable coordinate even if it is not a complete proposition by itself; and
4. the candidate is not merely a grammatical fragment of a better single coordinate, a same-class duplicate, or unsupported inference.

A unit does **not** need to stand alone as a full story proposition. Proposition assembly belongs to compounds.

After the first pass perform both:

- a **coverage pass** for omitted source-presented coordinates; and
- a **grain pass** to remove only unsupported fragments, duplicated referents, or spans that improperly absorb other independently represented coordinates.

Do not target an expected row count.

## 3. Atomicity without atomization

Use the shortest complete source-near span that carries the retained class function.

Split two source spans into separate units when each contributes a distinct represented class function that a later researcher may need to select independently, even when grammar embeds, coordinates, governs, or sequences one inside the other.

Keep words together when they jointly form one lexical/function-bearing coordinate, such as a phrasal predicate, required particle, fixed relation, or inseparable characterization.

Do not:

- split auxiliaries, articles, connectors, or bare prepositions that have no independent class function;
- absorb a second independently represented relation or coordinate merely to make the first unit read like a complete sentence;
- use compounds as a substitute for missing unit extraction.

## 4. Cross-class autonomy

Classify by positive class function, not by a winner-takes-all dominant-job rule.

The same source material may appear in more than one class when it independently performs each requested function. A valid VERB relation is not suppressed merely because the same wording also establishes PLACE, LABEL, TIME, or LOCATOR; likewise, another class is not created merely because grammar permits it.

Cross-class overlap is functional and source-grounded, never automatic.

## 5. Source-span lock

Never substitute synonyms or convenient paraphrases.

For every explicit row:

- `source_wording` is the shortest complete contiguous exact source substring carrying the retained class function;
- `source_cue` is an exact bounded contiguous source substring establishing the coordinate;
- colloquial wording, polarity, uncertainty, negation, question posture, comparison, hypothetical, intention, report, recurrence, and prospect remain recoverable.

Only an unnamed PLACE or TIME may use `source_wording = null`. Its exact `source_cue` must still establish the scene/frame. A neutral navigation tag may describe the role without inventing a proper name, date, clock time, or psychological meaning.

Short tags are navigation aids only and never replace source wording.

## 6. Class functions

### PLACE

A PLACE is a represented **where-anchor or scene-position role**.

Retain named settings, contained settings, represented positions, place-function origins/destinations, and distinct unnamed scene positions when source progression establishes them as separately selectable settings or positions.

A later interaction, waiting position, transition/destination position, or present-telling position may be a distinct unnamed PLACE even when its precise physical identity is not named.

Do not create PLACE from mere path wording, isolated deixis, or a spatial metaphor whose operative source job is only characterization rather than a represented scene/position.

When a broad container and contained place are established together, order the broad container before the contained place.

### TIME

A TIME is a represented **episode, frame, span, recurrence, intended period, or horizon** organizing source progression.

Retain distinct event/interaction frames, waiting or sustained-state frames, later report/reflection frames, recurring contexts, present telling/reflection, intended periods, and prospective horizons when the source establishes them as separately selectable temporal coordinates.

TIME does not require explicit dates or clocks.

Do not create one TIME for every verb, clause, duration question, or micro-action when the same represented frame remains in force.

### PERSON

A PERSON is an actual represented human referent or stable human/social actor group.

Resolve pronouns, aliases, kinship terms, and repeated mentions before duplicate removal.

A lexical mention of a role inside a request, hypothetical, anticipation, or generic reference does not establish that role as a participating PERSON earlier than the point at which the source actually represents that actor as a participant. Order resolved PERSON coordinates by first referential establishment, subject to speaker-first apparatus rules.

### OBJECT

An OBJECT is a source-presented **referent treated as one selectable thing**, concrete or abstract.

Retain explicit things, amounts/values, sets/categories, source-distinguished parts, services/results, choices, decisions, relations, and internal/figurative things when the source treats them as independently referable.

Keep one conceptual referent together. If a discourse wrapper such as a generic point/part/thing merely introduces richer content, do not let the bare wrapper replace the content-bearing referent. Do not nominalize every action, predicate, state, pronoun, PLACE, TIME, or clause into OBJECT.

### LABEL

A LABEL is a source-applied **characterization**: quality, state, identity, evaluation, comparison, correction, rejection, self-label, or characterization phrase/question.

Retain exact state/characterization formulations, including spatialized or internal-state wording, when the source uses them to characterize something.

Do not automatically promote every affective modifier, operational status, participant noun, quantity, or entire proposition into its own LABEL. Keep qualification/polarity with the characterization when needed for source fidelity.

### VERB

A VERB is a distinct source-presented **lexical action/relation edge**.

Retain genuine matrix, embedded, reported, perception, thought, speech, state, locative/copular, purpose, negated, questioned, hypothetical, intended, recurring, future, and meaning relations when they are represented as distinct relation edges.

Use the smallest complete contiguous source-near predicate span carrying one relation edge.

Split coordinated, sequential, governed, infinitival, perception/complement, or control constructions when more than one independently represented relation edge is present. A larger proposition-sized construction must not replace its constituent relation edges merely because the grammar links them.

Keep auxiliaries, particles, support words, or complements together only when they are required to express one lexical relation edge. Do not create bare auxiliary/copula fragments. A copular, state, or location relation may still be a valid VERB edge when the source expresses that relation; overlap with LABEL/PLACE/LOCATOR does not suppress it.

Do not absorb unrelated subjects, objects, places, times, labels, or a separately represented complement relation into `source_wording`.

### LOCATOR

A LOCATOR is a genuine **orienting or contextual relation** that situates a person, thing, action, state, or episode relative to something else.

It may express setting, position, direction, path, origin, destination, containment, proximity, movement target, accompaniment/association, deictic position, recurring context, or materially spatialized figurative/mental positioning when that relation is independently useful for locating the story coordinate.

LOCATOR is broader than physical geography but narrower than every prepositional phrase. Recipient, beneficiary, topic, possession, attribute, or ordinary argument is not automatically a locator; retain it only when the source uses the relation to orient or situate the represented material.

Movement wording may overlap VERB when it independently performs both functions.

## 7. Qualities

`qualities_available` is a boolean only. Set it true when descriptive/qualifying source language is associated with the coordinate; otherwise false. It never creates another unit and never authorizes a protected APA quality parse.

## 8. Ordering

Resolve aliases/coreference before ordering.

Order retained coordinates by earliest **referential establishment of that resolved coordinate**, not merely by the first lexical occurrence of a word later used for it.

Preserve source progression.

Mechanical exceptions only:

- speaker-first PERSON where supplied by the apparatus;
- broad-before-contained PLACE when both are established together;
- a later alias does not move a resolved coordinate later than its true first establishment.

Do not reorder by importance, emotional force, ontology, or analytical usefulness.

## 9. Compounds

Build compounds only after the unit inventory is final.

A compound represents one source-presented proposition/event/state/question/report/reflection/intention/relation and binds already-retained units that actually participate.

Use source/semantic order of references. Include all retained units materially participating in that binding and omit unrelated co-occurring units.

Do not:

- create units to fill a compound;
- let a compound compensate for missing unit extraction;
- emit sentence-wide graphs merely because units co-occur;
- emit arbitrary subsets or every possible recombination;
- emit a nested subset that adds no separately source-presented binding;
- assert protected APA semantics.

## 10. Final verification

Before return:

1. re-read the whole source;
2. check for omitted units of the requested class;
3. check that each retained unit performs a genuine class function without needing to be a whole proposition;
4. split spans that improperly absorb a second independently represented coordinate;
5. merge only true grammatical fragments that lack their own class function;
6. verify exact contiguous source spans and source posture;
7. verify coreference and first referential establishment ordering;
8. for compounds, verify all retained refs participate and no missing unit is being hidden by a larger binding.

Never infer a hidden archetype or expected count.

## 11. Isolation and hard boundaries

You do not have and must not seek access to:

- archetype workbooks or gold outputs;
- evaluator findings or expected counts;
- prior scored outputs;
- sealed holdout source during calibration;
- holdout outputs from any prior lineage.

Never perform APA scoring, protected-thread analysis, psychological diagnosis/inference, sovereign promotion, Oval Office research writing, APA-ID creation, or database admission.

Return only the JSON required by the supplied response schema. Do not explain outside that JSON.

## 12. Historical effect

`PARTIALLY SUPERSEDED — 2026-09-14`

For forward Researcher Inventory calibration behavior only, V28 supersedes V27’s proposition-grain/dominant-job rules to the extent they caused larger predicate constructions to replace distinct lexical relation edges or caused one class to suppress another independently represented class function.

Retained from V27:

- full-source coverage duty;
- exact literal source preservation;
- source-posture preservation;
- unnamed PLACE/TIME permission;
- anti-grammatical-debris rule;
- alias/coreference handling;
- qualities boolean boundary;
- candidate-only status;
- no promotion / no APA IDs;
- archetype/evaluator/holdout isolation;
- repeated archetype passes before holdout;
- fresh-agent clean-room certification requirement.

V27 remains preserved as historical calibration evidence.