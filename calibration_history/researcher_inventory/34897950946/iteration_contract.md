# APA RESEARCHER INVENTORY — DURABLE AGENT CONTRACT V32

Status: ACTIVE CALIBRATION SUCCESSOR — NOT CERTIFIED
Date: 2026-09-14
Predecessor: `researcher_inventory/AGENT_CONTRACT_V31.md`
Authority: Leah’s standing Researcher Inventory calibration directive
Promotion authority: NONE

## 1. Mission

Produce a lightweight, literal Researcher Inventory of the supplied source and only the requested class.

This is a **research-coordinate index**, not a grammatical parse and not an inventory of every phrase that could satisfy a broad semantic definition.

`Exhaustive` means every materially distinct coordinate at the approved **research grain**. It does not mean maximal lexical coverage.

The inventory has two layers:

1. **UNIT LAYER** — stable source-grounded researcher coordinates.
2. **COMPOUND LAYER** — source-presented bindings among already-final units.

## 2. Research-coordinate gate

A candidate becomes a unit only when all are true:

1. **Source grounding** — the source presents it, or for an unnamed PLACE/TIME clearly establishes the corresponding scene/frame.
2. **Positive class function** — it performs the requested class’s job.
3. **Material research identity** — it is a distinct coordinate a researcher would reasonably need to reconnect material source structure, not merely a phrase that can be semantically described as belonging to the class.
4. **Class-appropriate grain** — it has the resolution defined below.
5. **Independent contribution** — removing it would erase a distinct material coordinate rather than only remove grammatical detail, a local modifier, a support relation, or a redundant cross-class restatement.
6. **No debris / no analyst manufacture** — it is not grammar debris, an incidental local noun/phrase, unsupported inference, an alias duplicate, or a proposition/quality/place re-created in another class without an independent source-level job.

When uncertain between `retain` and `omit`, ask:

> What distinct reusable research coordinate disappears if this row is omitted?

If the answer is only “this phrase itself,” “a grammatical relation,” or “a possible semantic classification,” omit it.

Do not target an expected count.

## 3. Default semantic home; overlap is exceptional

Choose the **primary semantic home** of source material first.

- setting/scene location → PLACE;
- episode/frame → TIME;
- human/social actor → PERSON;
- independently tracked thing/content → OBJECT;
- characterization → LABEL;
- research-significant predicate/relation → VERB;
- spatial/orienting relation → LOCATOR.

Do not duplicate a span into several classes merely because it can grammatically perform several descriptions.

Cross-class overlap is allowed only when the source independently uses the same material to establish **two distinct researcher jobs**, each of which would lose material structure if omitted. Overlap is an exception, not a coverage strategy.

## 4. Whole-source procedure

For the requested class:

1. Read the complete source.
2. Segment the source mentally into material scenes, frames, actors, tracked referents, source characterizations, research-significant relations, and orientations.
3. Generate candidates for THIS class.
4. Apply the research-coordinate gate before writing rows.
5. Resolve aliases/coreference and merge duplicate mentions.
6. Run an omission pass for missing material coordinates.
7. Run an excess pass asking whether every retained row has independent research identity rather than mere lexical validity.
8. Apply literal-source and source-order checks.

Do not build units in order to make compounds richer.

## 5. Literal source lock

Never substitute synonyms, normalize dialect, repair punctuation, silently expand contractions, or rewrite quotation marks.

For every returned row:

- every non-null `source_wording` must be a character-for-character contiguous substring of `source`;
- every `source_cue` must be a character-for-character contiguous substring of `source`;
- every non-null `order_cue` must be a character-for-character contiguous substring of `source`;
- if a proposed phrase is not literally present, choose a shorter or longer exact source substring carrying the retained coordinate;
- only a supported unnamed PLACE or TIME may use `source_wording = null`.

Preserve question, negation, uncertainty, intention, hypothetical, report, recurrence, comparison, correction, rejection, dialect, and prospective posture.

Short tags are navigation aids only and may not introduce a synonym absent from the source evidence.

## 6. Class-specific resolution

### PLACE — material scene-location grain

A PLACE is a material setting or scene-position needed to locate a represented episode, participant, or materially significant positioned thing.

Retain:

- broad and contained settings when each organizes source structure;
- an unnamed location for a materially represented conversation, wait, encounter, remembered episode, present telling, or other distinct scene when its physical location is unspecified;
- a distinct origin/destination or positioned thing only when that position itself has material source significance.

Do **not** create PLACE from:

- every surface, container, object anchor, wall/floor/counter, geographic word, deictic token, path phrase, or figurative spatial expression;
- a descriptive location whose only job is already captured by a LOCATOR or OBJECT;
- a generic context phrase that does not establish a scene.

Two episodes may have separate unnamed PLACE coordinates even if they may physically overlap. Conversely, multiple local positions inside one scene do not automatically become separate PLACE rows.

For unnamed PLACE use `source_wording = null` and an exact source cue.

### TIME — material episode/frame grain

A TIME is a source-organizing episode, phase, period, recurrence, recollection/report frame, intended period, present-telling/reflection frame, or materially represented future/prospective frame.

Retain a new TIME when the source materially changes **when-frame** or explicitly foregrounds a period that organizes represented material.

Do **not** create TIME merely from:

- every action, state, tense change, adverb, duration phrase, frequency token, question, or prospective clause;
- a temporal modifier that only qualifies one existing proposition and does not establish an independent frame;
- repeated verbal steps inside one stable episode.

A single source episode may contain many VERBs. An explicit date/duration may still be omitted as TIME when it is only a local modifier; an unnamed episode may be retained when it materially organizes the story.

For unnamed TIME use `source_wording = null` and an exact source cue.

### PERSON — resolved represented actor grain

A PERSON is a materially represented human or social actor/group.

Retain the speaker plus represented people/groups that act, speak, perceive, are materially acted upon, or are stable relation endpoints.

Resolve aliases, kinship terms, role descriptions, and pronouns before duplicate removal.

Do not create PERSON for:

- generic `you`/listener language without an independently represented participant;
- hypothetical/generic roles that are not source actors;
- duplicate pronoun/case variants of the same actor.

### OBJECT — independently tracked referent grain

An OBJECT is a concrete or abstract referent the source treats as a materially independent thing/content/choice/value/relation/result at research grain.

Retain when the referent is independently trackable in the source structure, materially participates in retained relations, or is itself a source focus/choice/content object.

Possible OBJECTs include concrete things, materially distinguished parts, amounts/values, decisions/next steps, contemplated choices treated as whole options, named sets/categories, internal represented objects, and source-treated abstract content.

Do **not** create OBJECT merely because a noun phrase exists. Omit:

- a PLACE whose only independent job is location;
- a LABEL whose only job is characterization;
- a bare wrapper, pronoun, incidental local noun, surface/anchor, or discourse phrase with no independent research identity;
- a proposition, utterance, predicate, relation, condition, or clause merely because an analyst can nominalize or refer to it;
- descriptive wording that belongs inside another retained referent rather than standing as its own thing.

Abstract or proposition-like content requires clear source treatment as a distinct object of attention, decision, report, or selection — not merely grammatical complement status.

### LABEL — salient source characterization grain

A LABEL is a materially reusable source-applied characterization: identity, quality, state, evaluation, comparison, correction, rejection, or characterization question/response.

Retain the shortest complete exact formulation that carries the characterization.

Prefer characterizations the source **foregrounds as a handle** for a person, thing, situation, or relation.

Do **not** create LABEL from every adjective, participle, modifier, locative phrase, ordinary predicate, descriptive clause, negated proposition, intensifier, or noun modifier. A phrase can describe something without becoming an independent LABEL coordinate.

Preserve explicit candidate/rejection/correction sequences as separate characterization coordinates when the source presents them separately.

A quality-bearing VERB or OBJECT does not automatically create a LABEL; overlap requires an independent characterization job.

### VERB — lightweight research-relation package grain

A VERB is a materially distinct source-presented predicate/relation package useful for reconnecting the source.

The target grain is **larger than a verb token but smaller than a whole scene**.

Keep together words that jointly express one research relation, including auxiliaries, negation, idiomatic material, control/raising structure, selected complements, or coordinated action when separating them would create grammatical/internal machinery rather than a new research relation.

Examples of general packaging behavior:

- a stance/control predicate plus its infinitive may be one relation package when the source presents one action/intention;
- a speech/thought/perception predicate plus required content-selecting material may be one package when the embedded predicate is not independently useful;
- coordinated actions may stay together when source presents them as one option/package;
- a copular predicate whose only material content is an independently retained LABEL normally does not need a separate VERB;
- a locative copula whose only material content is an independently retained PLACE/LOCATOR normally does not need a separate VERB unless the relation itself is material.

Split only when the source presents independently useful relation edges with distinct participants/content/jobs.

Do not emit:

- every lexical verb token;
- bare support/copula/auxiliary edges;
- grammatical embedding machinery;
- whole questions/clauses when a smaller relation package carries the material job;
- characterization-only or locator-only restatements without an independent predicate job.

Preserve posture exactly and apply the literal lock.

### LOCATOR — spatial/orienting relation grain

A LOCATOR is a materially useful relation that places or moves a represented participant/thing relative to an anchor.

Retain setting relation, position/proximity, path, origin, destination, containment, movement direction, or materially spatialized figurative orientation when it independently reconnects source structure.

Use the smallest complete meaningful orienting construction, not an isolated preposition.

Do **not** create LOCATOR from:

- ordinary time/date/duration/frequency expressions simply because they provide context;
- discourse context, topic, possession, recipient, beneficiary, or generic argument structure;
- every accompaniment phrase;
- every metaphor containing a spatial word;
- a relation whose only material job belongs to TIME, LABEL, or VERB.

A recurring/situational phrase may qualify only when it independently anchors a repeated relation to a setting/position rather than merely stating when something happens.

## 7. qualities_available

`qualities_available` is a boolean only. Set true when the source supplies descriptive/qualifying language materially associated with the retained coordinate; otherwise false.

It never creates or splits a unit.

## 8. Ordering

Resolve coreference before ordering.

Order by first material establishment of the resolved coordinate, preserving source progression.

Mechanical exceptions only:

- speaker-first PERSON where the apparatus requires it;
- broad-before-contained PLACE/LOCATOR when established together;
- aliases do not move a coordinate later than first establishment.

Do not order by importance, ontology, emotional force, or evaluator expectation.

## 9. Compounds

Build compounds only after final units are fixed.

A compound is a materially distinct source-presented binding among retained units at proposition/event/state/question/report/reflection/intention/characterization/relation-cluster grain.

- include all and only retained units materially participating in that binding;
- preserve semantic/source reference order;
- several VERBs may occur in one compound when they belong to one source-presented event cluster;
- separate independently presented bindings;
- never invent a unit to complete a compound;
- do not emit every sentence, arbitrary subsets, every recombination, or redundant nested graphs;
- do not create a compound only because a unit exists.

## 10. Final excess/omission adjudication

Before return:

1. re-read the complete source;
2. ask whether each retained row is a stable material research coordinate rather than a merely valid phrase;
3. remove cross-class restatements lacking an independent job;
4. ensure materially organizing unnamed PLACE/TIME frames were not lost merely because explicit wording is absent;
5. ensure PERSON excludes generic discourse addressees;
6. ensure OBJECT excludes incidental nouns/nominalizations;
7. ensure LABEL excludes ordinary description not foregrounded as characterization;
8. ensure VERB uses research-relation packages, not token/predicate atomization;
9. ensure LOCATOR is orienting rather than generic temporal/context relation;
10. verify literal spans, posture, coreference, ordering, and compounds.

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

For forward Researcher Inventory calibration behavior only, V32 supersedes V31 where V31's broad positive-function and overlap language can be read to admit every semantically plausible phrase or lexical predicate. V32 replaces that behavior with the material research-coordinate gate, primary semantic-home rule, stricter class boundaries, lightweight VERB relation-package grain, and spatial/orienting LOCATOR boundary.

Retained unchanged from V31: complete-source reading; literal character-for-character span lock; source-posture preservation; class-specific resolution; coreference discipline; candidate-only status; archetype/evaluator/holdout isolation; no promotion/no APA IDs; repeated Case 2/Case 6 pass gate; exactly-once calibrated-lineage Case 5 gate; fresh-agent clean-room Case 5 certification sequence; predecessor/failure preservation.

V31 remains preserved as historical calibration evidence.