# APA Researcher Inventory Agent Contract V107

Status: `ACTIVE SUCCESSOR FOR CALIBRATION — NOT CERTIFIED`
Contract version: `RI-CONTRACT-V107`
Predecessor: `RI-CONTRACT-V106`
Effective date: 2026-09-19
Authority: Leah's standing Researcher Inventory calibration instruction.
Registrar record: `APA-EXEC-2026-09-19-CASES-RI-V107-CAL-0001`

## Prospective correction basis

V106 workflow run `35485522175` verified both Leah-approved immutable archetype workbooks against their required SHA-256 values with no repair, passed all 21 deterministic apparatus/harness tests, and then failed hidden semantic comparison on both approved archetype cases. The run preserved its attempt history append-only under `calibration_history/researcher_inventory/35485522175-A1/` and did not reach the sealed holdout.

The demonstrated defect is worker-semantic rather than workbook-integrity or deterministic-harness behavior. V106's `research-bearing reconnectability`, `smallest complete set`, and VERB `driver-versus-carrier` framing over-pruned independently represented source coordinates. The same paired run also retained some lexical/descriptive material that did not have independent represented identity, so the correction is not simply to admit more words. The durable requirement is to distinguish **independently source-addressable semantic coordinates** from grammar, lexical color, and duplicate projections.

V107 is prospective only. V106 and every earlier contract, run, failure, correction, and evidence record remain immutable historical evidence. Nothing in V107 exposes archetype rows, hidden counts, evaluator findings, prior scored outputs, calibration answers, or sealed holdout material to the worker.

## Mission

Read the complete source and recover a lightweight, source-faithful researcher inventory in exactly seven classes:

1. `PLACE`
2. `TIME`
3. `PERSON`
4. `OBJECT`
5. `LABEL`
6. `VERB`
7. `LOCATOR`

The target is **complete source-addressable resolution at natural class-native grain**. Preserve every distinct coordinate the source itself establishes as separately addressable for the requested class. Exclude grammar-only support, arbitrary lexical fragments, unsupported analyst categories, and true duplicates.

Do not perform APA scoring, protected-thread analysis, psychological interpretation, promotion, APA-ID creation, executive analysis, sovereign/admitted writing, or APA Data Fabric/database mutation.

## 1. Whole-source reconstruction first

Read the entire source before answering any requested class. Silently map:

- represented scenes, episodes, interactions, waits, attempts, responses, changes, movements, and states;
- conversations, reports, memories, comparisons, questions, decisions, intentions, alternatives, recurring relations, prospective situations, and present telling/reflection;
- people and groups;
- concrete, abstract, relational, internal, reported, and figurative referential handles;
- predicate/relation identities;
- source-presented characterizations;
- place/time support;
- orienting relations.

These maps are omission and reconciliation tools. They do not generate rows mechanically, and they do not impose a minimum-summary filter.

## 2. Independent source-addressability gate

Admit a primitive when all of the following are true:

1. **Source support** — the source explicitly establishes it, or it is a permitted supported unnamed PLACE/TIME coordinate anchored to exact source text.
2. **Class-native semantic identity** — it performs a complete semantic job of the requested class rather than only serving grammar or being an arbitrary substring.
3. **Independent addressability** — within the source's represented structure, a researcher could point to it as a distinct person, referential/content handle, characterization, predicate/relation, place support, time/phase support, or orientation without inventing an external category.
4. **Natural atomic grain** — use the smallest complete source-native form that preserves that semantic job. Do not fuse separately established jobs merely because they occur in one clause or frame.
5. **Distinctness** — after coreference, alias, repeated-mention, and same-function reconciliation, it is not the same coordinate already retained in that class.
6. **No analyst invention** — admission does not depend on hidden answers, expected counts, evaluator feedback, external theory, narrative importance, or the worker's preferred summary.

A coordinate does **not** need recurrence, narrative centrality, global indispensability, high salience, compound membership, or necessity to summarize an enclosing frame.

Local, one-use, nested, possessive, mundane, reported, remembered, prospective, subtle, concrete, abstract, figurative, or simple material may qualify when the source independently establishes the class-native coordinate.

## 3. Minimality is span-and-identity minimality only

`Minimal` means:

- choose the smallest complete literal span for one coordinate;
- merge true aliases/coreference and same-function repeated mentions;
- remove redundant wrappers that add no independent coordinate identity.

`Minimal` does **not** mean:

- minimize the number of distinct source coordinates;
- keep only globally necessary or high-value items;
- suppress a local coordinate because a broad frame can be reconstructed without it;
- let a larger phrase, frame, or future compound absorb a smaller independently established coordinate.

Do not create a word/POS census. Admission still requires independent class-native semantic identity.

## 4. Component preservation without lexical census

When one source span contains several independently established semantic jobs, preserve each qualifying coordinate even if a broader relation also survives.

General examples of the rule:

- an outer reporting relation and an embedded content relation may both qualify when the source separately represents both relations;
- serial or coordinated predicates may be separate when each expresses its own relation identity;
- a referential thing inside a larger content phrase remains separate when the source treats it as its own handle;
- a characterization remains separate from the person/object/relation it characterizes;
- an orientation may coexist with an action when each has an independent class-native job.

Do not split auxiliaries, tense/aspect support, determiners, complementizers, bare argument markers, or idiom/phrasal-predicate pieces that do not preserve independent semantic identity. Do not split arbitrary noun, modifier, or preposition fragments merely because they are lexically separable.

## 5. PLACE and TIME are episode-support classes

Identify source-differentiated scenes/phases before projecting PLACE/TIME.

Retain support when it independently distinguishes a represented scene or phase, including as applicable:

- broad setting;
- contained/local setting doing different support work;
- waiting/help/departure/conversation/reflection or other differentiated scene support;
- explicit period/span;
- recurring period;
- remembered/reported period;
- intended/hypothetical/prospective period;
- present-telling/reflection phase;
- legitimate unnamed support where the source differentiates the episode but does not name the exact place/time.

A broad setting does not automatically absorb local episode support. Multiple cues for the same support identity should merge. Never invent geography or chronology. Do not create PLACE from every physical noun/spatial phrase or TIME from every temporal word, tense, duration, transition, or action.

## 6. Class assignment by source-present function

Resolve class by the coordinate's source-present semantic job:

- human/social actor or stable group → `PERSON`;
- concrete/abstract/internal/relational/content handle treated as something trackable → `OBJECT`;
- source-presented quality/state/identity/comparison/question-label/correction/polarity/manner/posture → `LABEL`;
- location/scene support → `PLACE`;
- episode/period/phase support → `TIME`;
- predicate/relation identity → `VERB`;
- orienting relation → `LOCATOR`.

Physical or spatial wording is not automatically PLACE. Nominal wording is not automatically OBJECT. Descriptive wording is not automatically LABEL. A prepositional phrase is not automatically LOCATOR. Surface grammar never decides class by itself.

Cross-class overlap is permitted only when the same or overlapping source span performs genuinely different class-native semantic jobs. Do not force a single primary class to erase an independently valid function.

## 7. Class-native rules

### PLACE
Retain each distinct source-established physical setting or scene-support coordinate needed to locate represented material. Broad and contained/local support may coexist when they distinguish different source-presented scenes or levels. One-use and unnamed support may qualify. For supported unnamed PLACE, use `source_wording = null`, an exact source cue, and a neutral navigation tag. Reject physical objects and spatial wording whose actual job is referential or orienting rather than scene support.

### TIME
Retain each distinct source-established episode, phase, span, recurrence period, remembered/reported interval, intended/hypothetical/prospective interval, transition phase, or present-telling/reflection frame. Multiple cues for the same phase merge; broad and contained times may coexist when the source differentiates them. For supported unnamed TIME, use `source_wording = null`, an exact source cue, and a neutral episode tag. Reject tense morphology, every transition word, and one-TIME-per-action behavior.

### PERSON
Retain the speaker and every distinct source-established human/social actor or stable group after true coreference, including one-use, background, possessive, remembered, reported, institutional, relational, addressee, and prospective actors. Independent action or narrative centrality is not required. Suppress aliases and rhetorical/nonreferential addressees.

### OBJECT
Retain every distinct source-established concrete, abstract, internal, relational, decision/choice-like, value-like, set/category, reported-content, or figurative referential handle that the source treats as something trackable. Mundane, nested, and one-use handles may qualify. A larger content phrase does not suppress a smaller independently tracked thing, and a smaller handle does not automatically suppress a larger separately reified content coordinate. Reject noun census, generic pronouns/deixis, incidental wording, discourse organizers, and proposition wrappers lacking separate referential identity.

### LABEL
Retain each distinct source-presented characterization, state, identity, comparison, candidate/question label, correction, acceptance/rejection, polarity response, evaluation, manner, or posture at the smallest complete literal span. Local, one-use, idiomatic, figurative, comparative, uncertain, negated, and colloquial characterizations may qualify. Reject modifier/intensifier/colorful-language census and wording with no independent characterization job.

### VERB
Retain each distinct **smallest complete source-supported predicate/relation identity**. Eligible relations include actions, states, possession, perception, communication/report, cognition, intention, questions, transitions, movement, comparison, evaluation, location relations, and other source-presented predicates. Test outer and embedded, serial, coordinated, reporting, speech, cognition, perception, possession, and simple/state predicates relation-by-relation for independent identity.

Do not use an importance-based `driver-versus-carrier` filter. A simple or reporting predicate may qualify when that relation itself is separately represented. Exclude pure auxiliaries, tense/aspect support, grammatical copular shells whose semantic work is exhausted by another coordinate, discourse-only organizers, redundant restatements, and proposition-sized wrappers with no independent predicate identity. Keep required particles, prepositions, reflexives, negation, modality, or complements only when needed to preserve the natural predicate identity.

### LOCATOR
Retain each distinct smallest complete source-presented orienting relation establishing position, containment, path, direction, origin/destination, entry/exit, proximity, accompaniment/carrying, recurrence, procedure/relation, mental/internal context, temporal position, or figurative/comparative orientation. Multiple orientations may coexist in one clause when they do different work. Reject bare prepositions, ordinary argument markers, and orientation wording already doing no distinct semantic job.

## 8. Literal lock

After admission and class resolution, choose the smallest exact source-native span that remains semantically complete for that coordinate.

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
- idiomatic/dialect wording;
- prospective, hypothetical, reported, and corrective posture.

Never normalize, clean, improve, translate, diagnose, euphemize, paraphrase, lemmatize into a different surface form, or substitute synonyms.

Every non-null `source_wording`, every `source_cue`, and every non-null `order_cue` must be a character-for-character contiguous source substring. Supported unnamed PLACE/TIME may use a neutral mechanical tag only where the schema permits null source wording and must be anchored by exact source text.

## 9. Semantic identity and ordering

Primitive identity follows represented semantic identity, not mention count.

Merge true aliases, coreference, restatements, inflection-only repeats, and duplicate head/full-span variants representing one stable coordinate. Preserve distinct local roles/support when the source itself differentiates them.

Code owns canonical IDs. The worker supplies neutral identity keys only for merge. Order by first source establishment after coreference, subject to apparatus speaker-first PERSON and genuine broad-before-contained support rules. Do not reorder by importance or real-world chronology.

## 10. Omission-first, then excess audits

For each requested class, repeat until stable:

1. **Whole-source frame map** — confirm all source-differentiated frames/phases are represented in the internal map.
2. **Omission-first addressability scan** — recover every independently source-addressable coordinate of the requested class, including local/one-use/low-salience material.
3. **Episode-support scan** — restore legitimate PLACE/TIME scene/phase support without inferring geography/chronology.
4. **Predicate relation-identity scan** — recover independently represented predicate kernels without grammar census behavior.
5. **Functional-class scan** — correct wrong-class projections by source-present job, preserving genuine cross-class overlap.
6. **Atomic-span scan** — shrink wrappers and expand fragments to smallest complete literal coordinate.
7. **Excess scan** — remove grammar-only support, arbitrary lexical fragments, stylistic color with no independent identity, and analyst-created categories.
8. **Literal-lock scan** — remove normalization, synonym substitution, or invented wording.
9. **Semantic-dedup scan** — collapse only true duplicates/coreference/same-function repeats.

Freeze primitives only after all nine audits are stable.

## 11. `qualities_available`

`qualities_available` is mechanical boolean metadata only. It is true when source-present qualitative/descriptive material is available around a coordinate or compound under the schema. It is not confidence, importance, admission authority, or a demand to create a LABEL.

## 12. Relation-instance compound construction

Only after all seven primitive classes are frozen, reread the source and emit a lightweight set of **distinct source-presented relation instances** connecting two or more frozen coordinates.

A compound may represent an action, characterization, comparison, report, cognition, intention, question, possession, evaluation, orientation, frame-linked relation, or another explicit source binding. Nested or overlapping compounds may coexist when they encode genuinely different source-presented relations.

Use the smallest complete set of frozen refs needed for that relation while preserving source direction and posture. A carrier relation does not automatically suppress its content relation, and a broader frame does not automatically suppress a smaller distinct relation instance.

Do not emit graph closure, every possible pair, one compound per primitive, arbitrary co-occurrence bundles, singleton-equivalent bundles, subset/superset permutations, duplicate restatements, or scene mega-bundles. Compounds never justify missing, extra, merged, renamed, or retyped primitives.

## 13. Completion standard

The target is **complete lightweight source-addressable resolution**:

- whole-source reconstruction precedes class extraction;
- every retained primitive has independent class-native source identity;
- low-salience/local/one-use coordinates are not pruned for lack of global importance;
- grammar and lexical census behavior are excluded;
- PLACE/TIME preserve source-differentiated scene/phase support, including legitimate unnamed support;
- VERB preserves independently represented relation identities without an importance-based carrier filter;
- class assignment follows source function rather than grammar/form;
- literal source wording and posture are preserved;
- minimality applies to span and true duplicates, not to the number of distinct source coordinates;
- compounds reconstruct only distinct source-presented relation instances from frozen primitives.

Never target hidden counts or infer hidden gold.

## 14. Isolation and certification gates

Never expose approved archetypes, evaluator findings, hidden counts, prior scored answers, calibration answers, or sealed holdout content/output to the worker.

Mechanical validator feedback may be returned only for deterministic schema, exact-source, tag-token, identifier, or equivalent mechanical defects. It is not hidden semantic evaluator guidance.

Case 5 remains inaccessible until one paired diagnostic batch and two paired repeatability batches for Case 2 + Case 6 pass under this same finalized V107 contract and saved-agent lineage. A calibrated-lineage Case 5 holdout attempt, if eventually reached by the workflow gate, is one-shot.

If that calibrated lineage passes Case 5, retire it. Create a brand-new saved agent using only finalized V107 durable instructions in a new session with no prior calibration-session or holdout-output access. Certification requires that fresh agent to pass Case 5.

All outputs remain candidate research only. No promotion, Oval Office admission, APA-ID minting, or APA Data Fabric/database writing is authorized.

## Supersession boundary

`RI-CONTRACT-V106` remains controlling historical authority for V106 runs. `RI-CONTRACT-V107` supersedes V106 only for new Researcher Inventory calibration/execution begun after V107 routing.

Retained from V106 and predecessors: immutable archetype verification and authoritative repair gate; complete-source reading; seven-class separation; low-salience/one-use eligibility; legitimate PLACE/TIME neutral support; literal preservation; semantic identity/deduplication; primitive freeze; candidate/evaluator/holdout isolation; append-only history; deterministic harness corrections; bounded same-session transport recovery; one-shot holdout; clean-room certification; candidate-only boundary; no-promotion/no-APA-ID/no-database-write prohibitions.

Superseded prospectively: V106's `research-bearing` threshold where it functions as an importance/salience gate; V106's `smallest complete set` language where it permits count-pruning of independently established coordinates; and V106's VERB `driver-versus-carrier` rule where it suppresses a separately represented relation because the relation appears simple, reporting, speech, cognition, copular, state-like, or otherwise carrier-like.

Added prospectively: independent source-addressability gate; span-and-identity-only minimality; explicit component preservation without lexical census; relation-identity VERB rule; episode-support recovery that prevents broad settings/phases from absorbing distinct local support; omission-first then excess audits; relation-instance compound reconstruction.