# APA RESEARCHER INVENTORY — DURABLE AGENT CONTRACT V33

Status: ACTIVE CALIBRATION SUCCESSOR — NOT CERTIFIED
Date: 2026-09-14
Predecessor: `researcher_inventory/AGENT_CONTRACT_V32.md`
Authority: Leah’s standing Researcher Inventory calibration directive
Promotion authority: NONE

## 1. Mission

Produce a lightweight, literal Researcher Inventory of the supplied source and only the requested class.

`LIGHTWEIGHT` means preserve the source's available research coordinates without analyst invention, duplicate aliases, or grammatical debris. It does **not** mean sparse summary and it does not authorize collapsing separately available source coordinates into one larger paraphrastic package.

The inventory has two distinct layers:

1. **UNIT LAYER** — source-available coordinates at the approved class grain.
2. **COMPOUND LAYER** — larger source-presented bindings assembled only after the unit layer is final.

Never use compound convenience to decide that a source-available unit should disappear.

## 2. Unit-availability gate

Retain a candidate unit when all are true:

1. **Source availability** — the source literally presents the coordinate, or for an unnamed PLACE/TIME clearly establishes the scene/frame.
2. **Positive requested-class job** — the coordinate performs the requested class's job in the source.
3. **Distinctness inside the class** — it is not merely an alias/coreference duplicate of another unit in the same class.
4. **Class grain** — it is neither an isolated meaningless fragment nor an analyst-created whole-clause paraphrase when a smaller complete source coordinate is available.
5. **Literal/posture fidelity** — wording and posture remain source-grounded.

Do not require narrative importance, centrality, salience, foregrounding, or exclusive semantic ownership. A small concrete thing, local quality, embedded predicate, local time/scene, or orienting phrase may still be a valid coordinate when the source independently makes it available at that class grain.

When uncertain, ask:

> Can a researcher point back to this as a distinct source-presented coordinate of THIS class without inventing meaning?

If yes, retain it unless it is a within-class alias/duplicate or pure grammatical debris.

Do not target an expected count.

## 3. Cross-class availability

Classes are different views of source structure, not mutually exclusive bins.

The same source material may legitimately support more than one class when it independently performs more than one class job. Do not suppress an otherwise valid unit solely because another class is a plausible or primary semantic home.

Cross-class overlap must still be source-grounded. Do not manufacture a second-class unit by paraphrase, nominalization, or inference merely to create overlap.

Within a class, resolve aliases/coreference and remove true duplicates.

## 4. Whole-source procedure

For the requested class:

1. Read the complete source.
2. Identify every source-presented candidate for THIS class at the class grain.
3. Resolve aliases/coreference within the class.
4. Split bundled candidates when the source presents multiple independently available class coordinates.
5. Merge only true same-coordinate aliases/repetitions.
6. Run an omission pass from beginning to end of the source.
7. Run an excess pass for analyst invention, meaningless fragments, and same-class duplicates.
8. Apply literal-source, posture, and source-order checks.

Do not build or suppress units to make compounds easier.

## 5. Literal source lock

Never substitute synonyms, normalize dialect, repair punctuation, silently expand contractions, or rewrite quotation marks.

For every returned row:

- every non-null `source_wording` must be a character-for-character contiguous substring of `source`;
- every `source_cue` must be a character-for-character contiguous substring of `source`;
- every non-null `order_cue` must be a character-for-character contiguous substring of `source`;
- if a proposed phrase is not literally present, choose a shorter or longer exact source substring carrying the coordinate;
- only a supported unnamed PLACE or TIME may use `source_wording = null`.

Preserve question, negation, uncertainty, intention, hypothetical, report, recurrence, comparison, correction, rejection, dialect, and prospective posture.

Short tags are navigation aids only and may not introduce a source claim absent from the evidence.

## 6. Class-specific resolution

### PLACE — source scene/location coordinates

Retain source-presented settings and scene positions that locate represented material. This includes broad and contained settings when separately available, and supported unnamed locations for represented conversations, waits, encounters, recollections, present telling, or other scenes whose physical location is unspecified.

Do not require a PLACE to organize the whole story. Local scene positions can be valid when the source makes them independently available. Do not turn every object surface or figurative expression into PLACE when it has no locating job.

For unnamed PLACE use `source_wording = null` and an exact source cue.

### TIME — source when/frame coordinates

Retain source-presented episodes, phases, periods, dates/durations, recurrences, recollection/report frames, intended periods, present-telling/reflection frames, and materially represented future/prospective frames when they are independently available as when-coordinates.

Do not collapse several separately presented temporal frames merely because they belong to one larger episode. Do not create TIME from tense alone or from a temporal implication absent from source.

For unnamed TIME use `source_wording = null` and an exact source cue.

### PERSON — resolved represented actor coordinates

Retain the speaker and every source-represented human/social actor or actor group that is independently represented, including kinship/role mentions. Resolve pronouns, aliases, and coreference before duplicate removal.

Generic discourse `you` is not automatically a PERSON, but a source-represented addressee/actor is. Do not omit an actor merely because the actor is peripheral.

### OBJECT — source referent coordinates

Retain source-presented concrete or abstract referents that are independently identifiable at object grain: things, parts, documents, amounts, values, decisions, choices, relations/content treated as things, internal represented objects, and other distinct referents.

A referent need not be central or repeatedly tracked. A locally mentioned concrete thing can be a valid OBJECT if the source presents it as a distinct referent. Omit only alias duplicates, pure grammatical wrappers/pronouns, unsupported analyst nominalizations, or material whose source job is not referential at all.

Do not suppress an OBJECT solely because it also participates in PLACE, LABEL, VERB, or another class.

### LABEL — source characterization coordinates

Retain source-applied identities, qualities, states, evaluations, comparisons, corrections, rejections, and characterization questions/responses at the shortest complete source formulation that carries the characterization.

Foregrounding or reuse is not required. Local predicative/adjectival/idiomatic characterizations are valid when the source distinctly applies them. Do not create LABEL from wording that carries no characterization job, and do not paraphrase a clause into a new label.

Preserve separately presented candidate/rejection/correction characterizations.

### VERB — atomic source relation coordinates

Retain each independently source-presented predicate/relation increment at the shortest complete literal grain that still expresses the relation.

**Unit resolution is atomic relative to compound construction.** When one clause contains multiple predicate heads or relation steps that are separately available in the source, retain them separately rather than packaging the whole chain into one VERB unit.

Split, as source permits, perception from embedded action, control/intent from infinitival action, serial/coordinated actions, movement from purpose/action, state from subsequent action, and other separately available relation increments. Keep auxiliaries/negation/particles with the predicate only as needed for a complete literal relation and posture.

Do not emit isolated auxiliaries or meaningless syntactic fragments. Do not merge several source relations merely because they form one event; their event-level binding belongs in COMPOUNDS.

### LOCATOR — source locating/orienting relation coordinates

Retain independently source-presented relations that locate, orient, position, move, contain, connect, or situate a participant/thing/event relative to an anchor, path, destination, setting, context, or figurative orientation.

Use the smallest complete meaningful source construction. Spatial relations are central, but source-presented situational/recurring/figurative/contextual orientations may also qualify when they independently locate or orient represented material.

Do not suppress a LOCATOR merely because its wording also contains a VERB, TIME, OBJECT, or LABEL. Do not create one from an isolated preposition or unsupported inferred relation.

## 7. `qualities_available`

`qualities_available` is a boolean only. Set true when the source supplies descriptive/qualifying language materially associated with the retained coordinate; otherwise false.

It never creates or splits a unit.

## 8. Ordering

Resolve coreference before ordering.

Order by first source establishment of the resolved coordinate, preserving source progression.

Mechanical exceptions only:

- speaker-first PERSON where the apparatus requires it;
- broad-before-contained PLACE/LOCATOR when established together;
- aliases do not move a coordinate later than first establishment.

Do not order by importance, ontology, emotional force, or evaluator expectation.

## 9. Compounds — assemble, never substitute

Build compounds only after all class units are final.

A compound is a larger source-presented binding among already-retained units at proposition/event/state/question/report/reflection/intention/characterization/relation-cluster grain.

- include all and only final units materially participating in that binding;
- preserve semantic/source reference order;
- several atomic VERBs and LOCATORs may occur in one compound;
- separate independently presented bindings;
- never invent a unit to complete a compound;
- never collapse multiple atomic units into one unit because the compound needs a larger relation;
- do not emit arbitrary subsets/every recombination or redundant nested graphs unless separately source-presented.

The unit layer supplies the coordinates. The compound layer supplies the larger binding.

## 10. Final omission/excess adjudication

Before return:

1. re-read the complete source from beginning to end;
2. ensure locally small but source-distinct coordinates were not dropped for lack of salience;
3. ensure multi-relation clauses were not packaged into one unit where smaller complete source relations are independently available;
4. ensure cross-class exclusivity was not used to suppress a valid requested-class coordinate;
5. merge same-class aliases/coreference duplicates;
6. remove unsupported inference, paraphrase, meaningless syntactic fragments, and analyst-manufactured units;
7. verify unnamed PLACE/TIME support;
8. verify literal spans, posture, ordering, and `qualities_available`;
9. build/rebuild compounds only from the final unit set.

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

For forward Researcher Inventory calibration behavior only, V33 supersedes V32 where V32 required material-centrality/independent-contribution/primary-semantic-home exclusions or VERB relation packaging that suppress separately source-available atomic inventory coordinates.

V33 replaces those narrow rules with source availability, within-class distinctness, nonexclusive cross-class availability, atomic unit resolution, and strict separation between UNIT construction and COMPOUND assembly.

Retained unchanged from V32: complete-source reading; literal character-for-character span lock; source-posture preservation; coreference discipline; `qualities_available` boolean semantics; source ordering; candidate-only status; archetype/evaluator/holdout isolation; no promotion/no APA IDs; repeated Case 2/Case 6 pass gate; exactly-once calibrated-lineage Case 5 gate; fresh-agent clean-room Case 5 certification sequence; predecessor/failure preservation.

V32 remains preserved as historical calibration evidence.