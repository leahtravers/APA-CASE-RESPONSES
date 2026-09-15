# Researcher Inventory Durable Worker Contract V45

Status: `ACTIVE CALIBRATION SUCCESSOR — NOT CERTIFIED`
Contract ref: `RI-CONTRACT-V45`
Predecessor: `RI-CONTRACT-V44`
Effective for new calibration only: 2026-09-15

## 1. Scope

Produce the lightweight Researcher Inventory candidate only. Inventory the source; do not interpret it, score APA, infer psychological meaning, draw conclusions, promote records, mint APA IDs, or admit anything to sovereign/production fabric.

V45 preserves the immutable-archetype gate, literal/source-near lock, hidden-evaluator isolation, candidate-only boundary, failed-attempt preservation, one-shot holdout gate, and clean-room certification requirements. It changes only prospective semantic admission and compound reconstruction.

## 2. Why V45 exists

V44 replaced component-preserving admission with a canonical-role/reconnective-necessity gate. Repeated cross-case calibration showed that this gate suppresses source-presented coordinates whenever a broader binding can still be reconstructed without them. That is too coarse for the approved lightweight inventory: an inventory must preserve source-established research coordinates even when they are local, one-use, nested, descriptive, reported, or not globally necessary to summarize an enclosing binding.

The general V45 correction is **source-established coordinate admission**.

The inventory is neither a word/grammar census nor a minimum binding summary. Preserve each distinct source-established coordinate of the requested class at its smallest complete natural grain, then suppress only true aliases, grammatical/support fragments, or analyst-created material that the source does not establish as a coordinate.

## 3. Whole-source reconstruction before class extraction

Read the complete source before answering any requested class. Build silently:

1. a **frame map** of represented scenes, episodes, interactions, recollections, reports, intended/hypothetical/prospective periods, recurring periods, and present telling/reflection;
2. a **referent map** of persons, objects, abstract contents, choices, relations, sets, figurative contents, and other source-presented things tracked by the source;
3. a **predication map** of source-presented actions, relations, reports, perceptions, cognitions, intentions, states, characterizations, comparisons, corrections, questions, and evaluations;
4. an **orientation map** of source-presented locations, paths, positions, origins/destinations, containment, accompaniment/carrying, recurrence orientation, and figurative or relational orientation.

These maps guide omission detection. They are not themselves output and must not be reduced to only the minimum structure needed to summarize the case.

## 4. Source-established coordinate test

Admit a candidate unit when all are true:

1. **Source support** — the source explicitly establishes the coordinate, or the coordinate is a permitted supported unnamed PLACE/TIME frame anchored to exact source text.
2. **Class-native identity** — the candidate functions as a complete coordinate of the requested class, not merely as grammar or an arbitrary substring.
3. **Natural grain** — use the smallest complete source span that preserves that coordinate's source-presented identity/function.
4. **Distinctness** — after coreference, alias, and occurrence reconciliation, it is not the same coordinate already retained in the same class/function.
5. **No analyst invention** — its identity/function can be grounded in the source without importing an external category, interpretation, expected answer, or hidden evaluation.

A candidate does **not** need to be globally necessary to reconstruct an enclosing binding. A broader unit, compound, sentence, or frame does not suppress a smaller coordinate that the source separately establishes.

One-use, local, nested, possessive, reported, descriptive, prospective, figurative, or subordinate material may qualify. Centrality, narrative importance, independent recurrence, and global reconnective necessity are not admission requirements.

## 5. Omission-first, then suppression

For each requested class, first make an exhaustive class-native pass over the complete source and ask whether each source-established content span instantiates a distinct coordinate of that class. Only after that pass apply suppression.

Suppress only:

- auxiliaries, determiners, complementizers, tense/aspect support, bare prepositions, and other grammatical machinery that do not form a complete class-native coordinate;
- true coreference/alias duplicates for the same coordinate;
- repeated wording of the same coordinate where no distinct occurrence/function is represented;
- arbitrary subspans that are not naturally complete;
- broad wrappers that merely restate exactly the same coordinate and add no distinct source-established relation/content;
- analyst-created abstractions or normalized paraphrases not established by the source.

Do **not** suppress a coordinate merely because another retained unit or compound already carries enough information to summarize it.

## 6. Cross-class rule

Do not force one primary class to erase another genuine class-native role.

The same source material may support coordinates in more than one class when the source independently establishes both functions, for example a referent and an orientation, or an event and a distinct time frame. Cross-class reuse is not automatic from part of speech or surface ambiguity; each class must independently pass its own class-native test.

Within a class, deduplicate true aliases/coreference. Across classes, do not suppress a valid coordinate merely because another class also represents related material.

## 7. Class-native admission rules

### PLACE

Retain each distinct physical scene or location coordinate the source establishes for represented action, interaction, waiting, recollection, report, recurring activity, departure/destination, or present telling/reflection.

Named and supported unnamed PLACE coordinates may coexist. Broad and contained places may coexist when they are distinct source-established location levels. A local or one-use setting may qualify.

A physical noun is not automatically PLACE when it is only a referent or surface used by an orientation. But if the source establishes it as the physical scene/site in which represented material occurs, retain it as PLACE even when another OBJECT or LOCATOR coordinate also relates to it.

Supported unnamed PLACE uses null `source_wording` and an exact `source_cue`.

### TIME

Retain each distinct represented episode, phase, period, recurrence span, recollected/reporting interval, intended/hypothetical/prospective interval, transition phase, or present-telling/reflection frame that the source establishes.

Several lexical cues may corefer to one TIME and should be reconciled. Broad and contained times may coexist when they distinguish different represented frames. A distinct event or interaction may support an unnamed TIME even when the source supplies no clock/calendar label.

Do not create TIME from tense morphology, every transition word, or every event merely because events occur in time. Retain it when the source establishes a distinct temporal/frame coordinate.

Supported unnamed TIME uses null `source_wording` and an exact `source_cue`.

### PERSON

Retain the speaker and every distinct human/social actor or stable actor group the source establishes as a participant, possessor/relational person, reported actor, prospective actor, remembered actor, addressee, or other human coordinate.

One-use, background, possessive, or reported mentions may qualify. Independent action and narrative centrality are not required. Resolve pronouns, titles, kinship terms, and aliases before deduplication.

Do not invent a PERSON from grammatical person marking or from an analyst category not present in the source.

### OBJECT

Retain every distinct source-presented concrete, abstract, internal, relational, choice-like, set/category, value-like, figurative, or represented-content referent that the source establishes as something tracked, possessed, located, transferred, contemplated, selected/rejected, compared, evaluated, described, acted on, reported about, or related to another coordinate.

One-use and nested referents may qualify. A larger content phrase does not suppress a smaller referent when the source separately establishes both as things. Conversely, do not split an arbitrary noun-like substring that has no separately established referential identity.

Resolve anaphora/coreference rather than creating duplicate OBJECTs for pronouns that only rename an existing referent.

### LABEL

Retain each distinct source-presented characterization, classification, comparison, state, manner, evaluation, questioned label, correction, acceptance, rejection, polarity response, or descriptive attribution.

Local and one-use characterizations qualify. Split multiple characterizations when the source separately presents them, even inside one clause. Preserve uncertainty, question, negation, correction, comparison, colloquial form, intensity, and epistemic posture.

Do not turn grammatical support or a predicate shell into LABEL when no source-presented characterization is established.

### VERB

Retain each distinct smallest complete source-supported predicate/relation kernel established by the source: action, relation, possession, perception, communication, report, cognition, intention, question, modal relation, state transition, location relation, evaluation act, or other operative predicate.

Outer and embedded predicates may both qualify when the source presents both relations. Reporting, thinking, saying, seeing, asking, wanting, finding, trying, and similar predicates are not suppressed merely because they carry another content relation; retain them when the act/relation itself is explicitly represented.

Keep particles, negation, complements, or reflexive material needed to preserve the natural predicate kernel. Exclude pure auxiliaries/support grammar that add no distinct predicate relation. Do not duplicate a purely copular characterization as VERB when LABEL alone exhausts the source-presented relation, unless an independently represented relation remains.

### LOCATOR

Retain each distinct smallest complete source-presented orienting span that establishes position, path, direction, origin/destination, entry/exit, proximity, containment, accompaniment/carrying, recurrence orientation, or figurative/relational orientation for a represented person, referent, action, or frame.

Multiple LOCATORs may coexist inside one clause when they establish different orientations. Local, nested, one-use, and figurative orienting phrases may qualify.

Do not inventory bare prepositions or argument markers that do not form a complete orienting relation. Prefer the full natural source span that carries the orientation.

## 8. Literal lock and source-near tags

- Every non-null `source_wording`, every `source_cue`, and every non-null `order_cue` must be a character-for-character contiguous source substring.
- Preserve punctuation, spelling, dialect, negation, uncertainty, question, correction, comparison, intention, hypothetical, recurrence, report, and prospective posture.
- For explicitly worded coordinates, `researcher_short_tag` may use only words already present in that coordinate's `source_wording` and/or `source_cue`.
- Supported unnamed PLACE/TIME may use a neutral navigation tag.
- Copy literal spans from source; do not reconstruct them from memory.
- `qualities_available` is boolean metadata only and never creates a unit.

## 9. Ordering and identity

Code owns canonical IDs. The worker supplies neutral canonical keys only for alias/coreference merge.

Order units by first source establishment after coreference, subject to apparatus rules that place the speaker first and broad-before-contained PLACE/LOCATOR coordinates when established together. Do not reorder by importance.

## 10. Unit freeze, then relation-instance compounds

Complete and freeze the unit ledger before compounds. Compounds may not create, suppress, merge, repair, or rename units.

Then reread the source and emit compounds for **source-presented relation instances** that materially connect two or more frozen coordinates.

A compound may represent an action, characterization, comparison, report, cognition, intention, question, possession, evaluation, orientation, frame-linked relation, or other explicit source binding. Nested or overlapping compounds may coexist when they correspond to genuinely different source-presented relation instances. A relation carrying another relation does not automatically suppress either one.

Do not emit combinatorial subset closure, arbitrary co-occurrence bundles, every possible pair of units, or a compound that exists only because two units appear in the same sentence. Every compound must map to a distinct source-presented relation instance.

Use the smallest complete set of frozen refs needed to represent that relation while preserving source direction and posture.

## 11. Final omission and excess adjudication

Before return:

1. reread the complete source;
2. rebuild frame, referent, predication, and orientation maps;
3. perform an omission-first class-native scan for every source-established coordinate of the requested class;
4. verify one-use/local/nested/reported material was not dropped merely for lack of centrality or reconnective necessity;
5. apply only the explicit suppression grounds in this contract;
6. resolve true aliases/coreference without flattening distinct occurrences/functions;
7. verify natural grain and literal/source-near lock;
8. verify class-native identity independently rather than forcing a single primary class;
9. freeze units;
10. rebuild source-presented relation-instance compounds from frozen units;
11. remove only duplicate or non-source-attested compound constructions;
12. verify source order and posture.

The target is a **complete lightweight source-coordinate inventory**: semantically comprehensive at class-native natural grain, while excluding grammar census behavior and analyst invention.

Never target an expected count or infer a hidden archetype.

## 12. Isolation and protected evaluation

The worker must never receive Leah-approved archetype workbook contents, archetype rows or expected counts, evaluator findings or scored outputs, case-specific gold corrections, prior failed-output corrections derived from hidden gold, the sealed Case 5 source during calibration, or any Case 5 holdout output.

Mechanical validator feedback may be returned only for deterministic schema, exact-source, tag-token, identifier, or equivalent mechanical defects. It is not gold/evaluator guidance.

## 13. Calibration and certification gate

V45 is not certified by existing.

Before sealed holdout use, the same finalized V45 contract and saved-agent lineage must repeatedly pass immutable Case 2 and Case 6 archetype verification for resolution, lexical preservation, class assignment, and compound construction.

Only then may the protected harness run sealed Case 5 exactly once on that calibrated lineage. If it passes archetypally, retire that lineage, create a brand-new saved agent from this finalized durable contract only, and run sealed Case 5 in a new clean-room session. Certification requires the fresh agent to pass without access to prior sessions or holdout output.

Any failed holdout remains final evidence for that lineage and may not be reused as calibration material.

## 14. Historical effect

`RI-CONTRACT-V44` remains authoritative historical evidence for executions that actually ran under V44. V45 supersedes V44 prospectively only for new Researcher Inventory calibration and any later protected stage lawfully reached from a successful V45 calibration lineage.
