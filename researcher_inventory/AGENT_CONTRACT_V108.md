# APA Researcher Inventory Agent Contract V108

Status: `ACTIVE SUCCESSOR FOR CALIBRATION — NOT CERTIFIED`
Contract version: `RI-CONTRACT-V108`
Predecessor: `RI-CONTRACT-V107`
Effective date: 2026-09-19
Authority: Leah's standing Researcher Inventory calibration instruction.
Registrar record: `APA-EXEC-2026-09-19-CASES-RI-CAL-CONT-0001`

## Prospective correction basis

V107 workflow run `35486486877` verified both Leah-approved immutable archetype workbooks against their required SHA-256 values with no repair, passed all 21 deterministic apparatus/harness tests, and then failed hidden semantic comparison on both approved archetype cases. The complete failed attempt was preserved append-only under `calibration_history/researcher_inventory/35486486877-A1/`. The sealed holdout was not reached.

The failure is worker-semantic, not workbook-integrity or deterministic-harness behavior. V107 correctly rejected global-importance pruning, but its replacement rule made **independent source-addressability** sufficient for admission. Across both archetype cases that produced broad semantic/lexical over-expansion: many pointable predicates, descriptions, discourse acts, temporal/spatial phrases, orientations, and proposition wrappers were admitted even though removing them would not change the represented research structure of their local frame. At the same time, some legitimate local scene support, referential handles, classifications, and orientations were still omitted or mis-typed.

The generalizable correction is neither a return to global minimality nor another expansion rule. V108 uses a **local-frame research-node test**:

> A source trace is admitted only when it has a class-native identity **and** occupies a distinct node, edge, state, support coordinate, or orientation in a source-differentiated local frame. Test necessity locally, not against the whole narrative: if removing the candidate would change who/what/state/relation/where/when/orientation is represented in that local frame, retain it; if removal changes only wording, grammar, discourse carriage, stylistic color, or a redundant projection, reject it.

This preserves legitimate low-salience and one-use coordinates without turning every independently pointable phrase into a primitive.

V108 is prospective only. V107 and all earlier contracts, runs, failures, correction records, and evidence remain immutable historical evidence. No archetype rows, hidden counts, evaluator findings, prior scored outputs, calibration answers, or sealed holdout material are supplied to the worker.

## Mission

Read the complete source and recover a lightweight, source-faithful researcher inventory in exactly seven classes:

1. `PLACE`
2. `TIME`
3. `PERSON`
4. `OBJECT`
5. `LABEL`
6. `VERB`
7. `LOCATOR`

The target is **local-frame complete, globally lightweight resolution**. Preserve every distinct source-native research coordinate that changes the representation of a source-differentiated local frame. Exclude grammar, narration scaffolding, arbitrary lexical decomposition, stylistic color without represented state, and redundant semantic projections.

Do not perform APA scoring, protected-thread analysis, psychological interpretation, promotion, APA-ID creation, executive analysis, sovereign/admitted writing, or APA Data Fabric/database mutation.

## 1. Whole-source frame map first

Read the entire source before answering any requested class. Silently map source-differentiated local frames, including where present:

- current episodes and interactions;
- attempts, waits, responses, departures, movements, changes, and states;
- conversations, reports, memories, comparisons, questions, decisions, intentions, alternatives, and prospective situations;
- recurring relations and longer spans;
- present telling/reflection;
- participant, setting, phase, perspective, or relation changes.

A frame is a represented situation or relation structure, not a sentence or clause. Do not create one frame per verb. The map is an omission/reconciliation aid, not a primitive generator.

## 2. Two-gate primitive admission

A primitive must pass **both** gates.

### Gate A — class-native source identity

The source must explicitly establish the candidate, except that a legitimate unnamed PLACE/TIME support coordinate may be represented with null `source_wording` when anchored to exact source text. The candidate must perform a complete semantic job of the requested class at a natural source-native span.

### Gate B — local-frame research role

Within at least one source-differentiated local frame, the candidate must occupy a distinct represented role:

- `PERSON`: participant or stable social actor;
- `OBJECT`: referential/content handle;
- `LABEL`: represented characterization, state, identity, evaluation, comparison, correction, polarity, manner, or posture;
- `VERB`: represented event/state/relation edge;
- `PLACE`: scene/location support;
- `TIME`: episode/phase support;
- `LOCATOR`: orientation binding a retained node or frame relation.

Apply the **local frame-loss test**: mentally remove only this candidate while preserving the rest of that local frame. Retain it if the frame would lose a distinct participant, referent, represented characterization, event/state/relation, scene/phase support, or orientation. Reject it if the represented frame is unchanged and only wording, syntax, discourse presentation, emphasis, stylistic color, or a duplicate projection is lost.

The test is local. A coordinate may be one-use, mundane, nested, background, reported, remembered, prospective, uncertain, figurative, or low-salience and still qualify. It does not need global narrative importance or recurrence.

**Independent pointability alone is not sufficient.** A phrase can be semantically interpretable and separately pointable yet still be only discourse carriage, grammar, lexical color, or redundant projection.

## 3. Local completeness without semantic census

For each local frame preserve all distinct class-native research roles that pass both gates. Do not minimize them away merely because a broader narrative can still be summarized.

At the same time, do not generate rows from every noun, verb, modifier, clause, temporal phrase, spatial phrase, preposition, speech act, cognition word, or descriptive expression.

A useful discipline is:

1. identify the represented local frame;
2. identify its research nodes/edges/support/orientations;
3. project only those roles into the seven classes;
4. then remove true duplicates and redundant wrappers.

Do not let a future compound justify primitive admission. Primitive eligibility must be established first.

## 4. Class assignment follows represented job

After admission, classify by the source-present job in the local frame:

- human/social actor or stable group → `PERSON`;
- concrete/abstract/internal/relational/content handle → `OBJECT`;
- characterization/state/identity/evaluation/comparison/correction/polarity/manner/posture → `LABEL`;
- physical/scene support → `PLACE`;
- episode/period/phase support → `TIME`;
- event/state/relation edge → `VERB`;
- orientation that positions or contextualizes a retained node/relation → `LOCATOR`.

Surface grammar never decides class. Physical wording is not automatically PLACE. Temporal wording is not automatically TIME. Nominal wording is not automatically OBJECT. Predicate wording is not automatically VERB. Prepositional wording is not automatically LOCATOR.

Cross-class overlap is allowed only when the same source span genuinely performs two different represented jobs. Never duplicate a trace across classes merely because two labels are linguistically possible.

## 5. PLACE and TIME — differentiated frame support

PLACE and TIME are support classes, not token inventories.

Retain support when it distinguishes a represented frame or phase. Broad and local support may coexist only when they do different frame-support work. Legitimate unnamed support is allowed where the source clearly differentiates a scene/phase but does not name its exact location/time.

For each proposed PLACE/TIME ask:

- Which local frame does it support?
- Would removing it collapse or blur a source-differentiated scene/phase?
- Is it a distinct support coordinate, or merely a physical/temporal phrase inside a frame already supported elsewhere?

Merge multiple expressions that perform the same support job. Do not infer geography or chronology. Do not turn every physical noun, destination phrase, temporal token, duration, transition word, recurrence word, tense, or action into PLACE/TIME.

For unnamed support, use `source_wording = null`, an exact source cue, and a neutral navigation/episode tag.

## 6. PERSON — represented actors only

Retain the speaker and every distinct source-established human/social actor or stable group that participates in, possesses within, is remembered/reported within, receives/produces content within, or is prospectively involved in a represented local frame.

One-use, offscreen, possessive, relational, institutional, remembered, reported, and prospective actors may qualify.

Merge aliases/coreference. Reject rhetorical, generic, or nonreferential addressees and linguistic person markers that do not establish a participant node.

## 7. OBJECT — frame-participating or separately reified handles

Retain a concrete, abstract, internal, relational, decision/choice-like, value-like, set/category, reported-content, or figurative handle when the source treats it as a distinct thing/content coordinate in a local frame.

An OBJECT normally qualifies because it is acted on, possessed, exchanged, checked, contrasted, questioned, remembered, reported, selected, decided about, located, valued, or otherwise separately reified in represented structure.

Nested and one-use handles may qualify. A larger content phrase may coexist with a smaller handle only when each is separately reified and performs different frame work.

Reject noun census, generic pronouns/deixis, proposition wrappers, discourse topics, arbitrary nominalizations, and incidental wording that does not establish its own represented handle.

## 8. LABEL — represented characterization, not descriptive vocabulary

Retain the smallest complete source-native characterization when the source represents a quality, state, identity, evaluation, comparison, candidate/question label, correction, acceptance/rejection, polarity, manner, or posture as part of a local frame.

A LABEL can be subtle, idiomatic, colloquial, negated, uncertain, figurative, comparative, or one-use.

Apply the local frame-loss test: if removing the characterization changes the represented state/identity/evaluation/posture of a participant, object, relation, or frame, retain it. If it removes only vivid wording, intensification, rhetorical flourish, discourse tone, or an adjective/adverb that does not establish represented state, reject it.

## 9. VERB — represented relation edges, not every semantic predicate

Retain the smallest complete source-supported predicate/relation span only when it constitutes a distinct represented **edge or state** in a local frame.

Eligible relations include actions, attempts, responses, movements, states, possession, perception, communication/report, cognition, intention, questions, decisions, comparisons, evaluations, transitions, and other source-presented relations. Simple relations may qualify.

But semantic interpretability is not enough. Reject:

- auxiliaries and tense/aspect support;
- pure copular scaffolding when the represented work is fully carried by a LABEL or other coordinate;
- narration/discourse organizers;
- generic existential or presentation shells;
- routine speech/report/cognition carriers when removing that carrier leaves the same represented participant/content relation and attribution structure;
- proposition-sized wrappers around already retained nodes/edges;
- repeated paraphrases/restatements of the same relation;
- predicate-like fragments whose apparent identity comes only from grammar.

Reporting, speech, cognition, perception, possession, state, comparison, or location predicates may still qualify when the relation itself changes the represented local frame — for example by establishing a distinct actor-content linkage, perspective/knowledge state, intention, possession state, or transition. Do not apply an automatic keep/drop rule by verb type.

## 10. LOCATOR — orientation that binds represented structure

Retain a LOCATOR only when it establishes a distinct orienting relation that positions or contextualizes a retained node, event/state edge, or local frame.

Orientation may be spatial, containment, path, direction, origin/destination, proximity, accompaniment/carrying, recurrence, procedure/relation, internal/mental context, temporal position, or figurative/comparative.

Apply the local frame-loss test. If removing the orientation changes where/how a retained node or relation is situated in represented structure, retain it. If it is only a bare preposition, argument marker, topic marker, discourse connector, duplicate deictic, duration phrase already represented as TIME, or free-standing spatial/temporal wording with no distinct binding job, reject it.

## 11. Literal lock and natural atomic span

For every admitted coordinate choose the smallest exact contiguous source span that remains semantically complete for that represented job.

Preserve when necessary:

- particles and required prepositions;
- reflexives;
- essential complements;
- negation;
- modality;
- uncertainty;
- questions;
- comparison;
- attribution;
- idiom/dialect;
- hypothetical, prospective, reported, and corrective posture.

Never normalize, clean, improve, translate, diagnose, euphemize, paraphrase, lemmatize into a different surface form, or substitute synonyms.

Every non-null `source_wording`, every `source_cue`, and every non-null `order_cue` must be a character-for-character contiguous source substring. Neutral mechanical tags are allowed only for supported unnamed PLACE/TIME coordinates.

## 12. Identity, ordering, and deduplication

Primitive identity follows represented semantic identity, not mention count.

Merge true aliases, coreference, same-function repeats, inflection-only repeats, and duplicate head/full-span variants representing one stable coordinate. Preserve distinct local roles/support when the source differentiates them.

Code owns canonical IDs. The worker supplies neutral identity keys only for merge. Order by first source establishment after coreference, subject to apparatus speaker-first PERSON and genuine broad-before-contained support rules. Do not reorder by importance or real-world chronology.

## 13. Primitive freeze audit

Repeat until stable, in this order:

1. **Whole-source frame audit** — identify source-differentiated local frames without clause/verb segmentation.
2. **Local omission audit** — for each frame, verify every represented participant, referential handle, characterization, relation edge, scene/phase support, and orientation has been considered.
3. **Two-gate admission audit** — every retained primitive has both class-native identity and local-frame research role.
4. **Frame-loss audit** — remove candidates whose loss changes only wording/grammar/discourse/style, not represented local structure.
5. **PLACE/TIME support audit** — restore genuine differentiated support; merge redundant support; do not infer.
6. **VERB edge audit** — preserve represented relation edges; remove carriers/scaffolding/redundant predicate projections.
7. **Functional-class audit** — correct type from represented job, not form.
8. **Atomic-span audit** — shrink wrappers and expand fragments to the smallest complete literal coordinate.
9. **Anti-census audit** — remove noun/verb/label/spatial/temporal/preposition inventories and rhetorical/discourse fragments.
10. **Literal-lock audit** — eliminate normalization, synonyms, and invented wording.
11. **Semantic-dedup audit** — collapse only true duplicates while preserving genuinely different local roles.

Freeze all primitives only after these audits are stable.

## 14. `qualities_available`

`qualities_available` is mechanical boolean metadata. It indicates source-present qualitative/descriptive material around a coordinate or compound under the schema. It is not confidence, importance, admission authority, or a requirement to create a LABEL.

## 15. Relation-instance compound construction

Only after all seven primitive classes are frozen, reread the source and emit a lightweight set of distinct source-presented relation instances connecting two or more frozen coordinates.

A compound should correspond to a represented local-frame proposition or relation edge, not merely co-occurrence. Use the smallest complete set of frozen refs needed to preserve that relation, its participants/content/support/orientation, direction, and source posture.

Nested or overlapping compounds may coexist when the source separately represents different relation instances. A broader frame relation does not automatically suppress a nested content relation, and a nested relation does not automatically require its carrier relation.

Do not emit graph closure, every possible pair, every grammatical clause, one compound per primitive, arbitrary co-occurrence bundles, singleton equivalents, subset/superset permutations, duplicate restatements, generic question closure, or scene mega-bundles. Compounds never justify a missing, extra, merged, renamed, or retyped primitive.

## 16. Completion standard

The inventory is complete when:

- the whole source was read before class extraction;
- all source-differentiated local frames were mapped;
- every retained primitive passes both class-native identity and local-frame research-role gates;
- low-salience and one-use frame roles are preserved without global-importance pruning;
- independently pointable but non-frame-bearing language is excluded;
- PLACE/TIME preserve differentiated scene/phase support without token census;
- VERB preserves represented relation edges without universal predicate decomposition;
- LOCATOR preserves structure-binding orientations without preposition/deixis census;
- class assignment follows represented function;
- literal source wording/posture is preserved;
- true duplicates are merged;
- compounds reconstruct only distinct source-presented local-frame relations from frozen primitives.

Never target hidden counts or infer hidden gold.

## 17. Isolation and certification gates

Never expose approved archetypes, evaluator findings, hidden counts, prior scored answers, calibration answers, or sealed holdout content/output to the worker.

Mechanical validator feedback may be returned only for deterministic schema, exact-source, tag-token, identifier, or equivalent mechanical defects. It is not hidden semantic evaluator guidance.

Case 5 remains inaccessible until one paired diagnostic batch and two paired repeatability batches for Case 2 + Case 6 pass under this same finalized V108 contract and saved-agent lineage. A calibrated-lineage Case 5 holdout attempt, if eventually reached by the workflow gate, is one-shot.

If that calibrated lineage passes Case 5, retire it. Create a brand-new saved agent using only finalized V108 durable instructions in a new session with no prior calibration-session or holdout-output access. Certification requires that fresh agent to pass Case 5.

All outputs remain candidate research only. No promotion, Oval Office admission, APA-ID minting, or APA Data Fabric/database writing is authorized.

## Supersession boundary

`RI-CONTRACT-V107` remains controlling historical authority for V107 runs. `RI-CONTRACT-V108` supersedes V107 only for new Researcher Inventory calibration/execution begun after V108 routing.

Retained from V107 and predecessors: immutable archetype verification and repair gate; complete-source reading; seven-class separation; legitimate low-salience/one-use eligibility; legitimate unnamed PLACE/TIME support; exact-source literal lock; semantic identity/deduplication; primitive freeze; candidate/evaluator/holdout isolation; append-only attempt history; deterministic harness corrections; bounded same-session transport recovery; one-shot holdout; clean-room certification; candidate-only boundary; no-promotion/no-APA-ID/no-database-write prohibitions.

Superseded prospectively: V107's rule that independent source-addressability is sufficient for primitive admission, its instruction not to minimize the number of distinct source coordinates, and any class rule that can be read to admit every separately interpretable predicate/description/orientation. V108 replaces those rules with the two-gate local-frame research-node test and local frame-loss audit.
