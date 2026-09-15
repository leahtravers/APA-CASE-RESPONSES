# Researcher Inventory Durable Worker Contract V43

Status: `ACTIVE CALIBRATION SUCCESSOR — NOT CERTIFIED`
Contract ref: `RI-CONTRACT-V43`
Predecessor: `RI-CONTRACT-V42`
Effective for new calibration only: 2026-09-15

## 1. Scope

Produce the lightweight Researcher Inventory candidate only. Inventory the source; do not interpret it, score APA, infer psychological meaning, draw conclusions, promote records, mint APA IDs, or admit anything to sovereign/production fabric.

This successor preserves V42's literal lock, hidden-evaluator isolation, immutable-archetype gate, candidate-only boundary, frame reconstruction, one-shot holdout gate, and clean-room certification requirements. It changes only the semantic grain used to select units and compounds prospectively.

## 2. Why V43 exists

V42 correctly rejected a lexical/grammar census and introduced useful frame and binding reconstruction, but repeated cross-case calibration evidence showed a systematic new defect: the worker often let a broad binding or complete phrase stand in for smaller research-bearing components that the source separately establishes. At the same time, some discourse or narrative wrappers were retained even when their only job was to carry already-represented content. The result was substantial under-resolution plus selected extras and downstream compound mismatch.

The general correction is **component-preserving binding reconstruction**.

A lightweight inventory is not a word census, but it is also not a sentence/binding summary. Within every represented binding, preserve each source-supported semantic component that performs a distinct research function and could vary independently from the other components of that binding.

## 3. Three-level reconstruction

Read the complete source before extracting any class.

### 3.1 Frame skeleton

Reconstruct the source's lightweight frame skeleton: episodes, interactions, periods, scenes, reported/recollected frames, intended/hypothetical/prospective frames, recurring frames, and present-reflection/telling frames needed to navigate represented material.

This is not an event census. Several lexical cues may locate one frame. Broad and contained frames may both exist when they organize different represented material.

### 3.2 Binding map

Reconstruct the source-presented bindings: who/what is related, characterized, located, acted on, contemplated, compared, questioned, reported, possessed, selected/rejected, or oriented.

Do not yet decide that a whole clause or phrase is one unit. A binding may contain several separately inventory-worthy components.

### 3.3 Component ledger

For each binding, identify the smallest complete **research-bearing components** by class.

A component qualifies when all are true:

1. **Source support** — it is literally source-presented, or it is a permitted supported unnamed PLACE/TIME frame.
2. **Distinct function** — it performs a separate participant, referent/content, characterization, relation/action, orientation, scene, episode, or period role.
3. **Independent-variation test** — the component could change, disappear, or be compared while the rest of the binding remained materially intelligible, changing a plausible research coordinate.
4. **Natural completeness** — it is the smallest complete span for that function, not an arbitrary grammatical fragment.
5. **Non-duplication** — after coreference/alias and function reconciliation, it is not merely another wording of the same retained component with the same class/function.

Nestedness does not make a component duplicate. A broad binding does not suppress a smaller component when the smaller component does a distinct job.

## 4. Decompose meaning, not grammar

Use semantic decomposition rather than either extreme:

- **Do not census grammar.** Do not inventory every auxiliary, copula, preposition, modifier, complementizer, tense marker, reporting shell, pronoun, or clause merely because it appears.
- **Do not flatten semantic components.** Do not merge distinct source-presented actions, relations, characterizations, referents, orientations, or frame coordinates merely because they occur inside one clause or can be paraphrased by one larger phrase.

A useful test is: **if two parts of the same clause could receive different values in a research comparison, and each has a complete source-supported function, preserve both.**

A wrapper that only introduces or packages already represented content is not retained merely because it is explicit. A reporting, thinking, knowing, wishing, perceiving, or saying relation is retained when that act/relation itself is represented as a distinct event or relation, not when it is only a carrier with no separate research role.

## 5. Class rules

### PLACE

Retain physical scene/location coordinates that locate represented episodes, interactions, conversations, waits, departures/destinations, recollections, recurring activities, or present telling/reflection. Broad and materially contained places may coexist when they locate different frame levels.

Supported unnamed PLACE coordinates are permitted when a distinct represented interaction/episode has a physical setting even though the source does not name it. For supported unnamed PLACE, `source_wording` may be null and `source_cue` must be exact source text.

Do not turn every surface, object part, container, counter, wall, floor, line, or spatial noun into PLACE. Such material may instead be OBJECT or LOCATOR when it performs those functions.

### TIME

Retain episode/period/frame coordinates that organize represented material. Separate TIME units may coexist for broad and contained periods when they distinguish different represented phases or episodes.

Temporal wording is evidence, not automatic unithood. Consolidate multiple cues that locate the same frame. Preserve distinct temporal components when they locate materially different frames, recurrence structures, intended/prospective episodes, recollected periods, or present reflection.

For supported unnamed TIME, `source_wording` may be null and `source_cue` must be exact source text.

### PERSON

Retain the speaker plus every represented human/social actor or stable actor group that participates in or is materially related to represented content. Relational, possessive, prospective, reported, and one-use actors may qualify. Resolve aliases/coreference before deduplication. Independent action is not required.

Do not create PERSON from grammatical person marking alone or from analyst-invented categories.

### OBJECT

Retain concrete, abstract, internal, relational, choice-like, set/category, figurative, or represented-content referents when the source treats them as distinct content that is tracked, possessed, located, transferred, evaluated, contemplated, selected/rejected, compared, acted on, reported about, or used as the content of a represented relation.

Do not let a larger predicate/binding suppress a distinct object merely because the object appears only once or is embedded. Preserve source-presented choices, decisions, relations, values, sets, contents, and figurative referents when they function as separately trackable content.

Reject bare anaphoric/discourse wrappers, unspecified placeholders, and clause/proposition packaging that adds no separately tracked content.

### LABEL

Retain each source-presented characterization, correction, classification, comparison, state, manner, evaluation, questioned label, or explicit acceptance/rejection response when it independently characterizes a retained participant, referent, relation, or frame.

When several characterizations occur together, split them into separate LABEL components if each could vary independently. Do not preserve one sentence-sized characterization wrapper merely to contain several smaller labels.

Preserve colloquial form, uncertainty, question, correction, comparison, and negation.

A bare copular assignment does not require a duplicate VERB when LABEL fully owns that semantic content.

### VERB

Retain each smallest complete source-supported predicate/relation kernel that performs a distinct research-bearing edge: action, relation, state transition, possession, perception, communication, cognition, report, modal/questioned relation, or other operative predicate.

**Decompose multi-edge clauses.** If a source span contains an outer relation and an embedded/nested relation, preserve both when each independently connects participants/content or changes what is represented. Do not let a broad complete predicate replace its distinct internal relation components.

Keep particles, negation, or required complements with the kernel when needed for completeness or meaning. Do not split auxiliaries or grammatical support into fake units. Do not duplicate a characterization already fully represented by LABEL unless a separate operative relation remains.

### LOCATOR

Retain each smallest complete source-presented orienting span that materially locates or orients a retained participant, referent, relation, or frame by position, path, origin/destination, entry/exit, containment/proximity, accompaniment/carrying, recurrence orientation, or other spatial/relational direction.

Several LOCATOR components may coexist within one larger clause when they establish different orientations or paths. Do not collapse them merely because one larger phrase contains them.

Reject prepositional/argument-marking phrases that only identify recipient, possessor, complement, or grammatical relation and add no independent orientation. Reject isolated function-word fragments when a complete orienting span is natural.

## 6. Wrapper suppression rule

After the component ledger is built, inspect every broad or discourse-level candidate.

Suppress a candidate when its only contribution is to package, introduce, hedge, announce, or restate other retained content and it adds no distinct research-bearing relation/characterization/referent/frame/orientation of its own.

Do not suppress a genuine relation merely because it is discourse-like. The question is functional: **does the wrapper itself create a separate research coordinate, or does it only carry another coordinate?**

## 7. Literal lock and source-near tags

- Every non-null `source_wording` is a character-for-character contiguous substring of the source.
- Every `source_cue` and non-null `order_cue` is a character-for-character contiguous substring of the source.
- Preserve punctuation, apostrophes, hyphens, capitalization, spelling, dialect, negation, uncertainty, question, comparison, intention, hypothetical, report, recurrence, correction, and prospective posture.
- `researcher_short_tag` is compact and source-near. For an explicitly worded coordinate, build it only from words already present in that coordinate's exact `source_wording` and/or `source_cue`; do not add synonyms, explanatory adjectives, or analyst wording.
- Supported unnamed PLACE/TIME may use a neutral navigation tag because `source_wording` is null.
- Copy literal spans from source; do not reconstruct them from memory.

## 8. Ordering and identity

Code owns canonical IDs. The worker supplies neutral canonical keys only for alias/coreference merge.

Order units by first source establishment after coreference, subject to apparatus rules that place the speaker first and broad-before-contained PLACE/LOCATOR coordinates when established together. Do not reorder by importance.

## 9. Unit freeze, then compound reconstruction

Complete and freeze the unit ledger first. Compounds may not create, suppress, merge, repair, or rename units.

Then rebuild compounds from the binding map using the frozen component ledger.

Emit one compound for each distinct lightweight research-bearing source binding or characterization relation that is useful to preserve. A compound may contain several component units. A broad and nested compound may both exist only when they encode genuinely different relations, not merely subset/superset syntax.

Do not emit:

- every grammatical clause;
- every possible subset of a binding;
- a compound merely because retained units co-occur;
- a wrapper compound whose only function is to package an already represented binding;
- a sentence-sized mega-compound that collapses several different relations.

Do preserve distinct nested relations when the source represents multiple edges in the same clause and each relation has independent research content.

`qualities_available` is a boolean only; it never creates a unit. Q is mechanical output metadata, not a semantic unit.

## 10. Final whole-source adjudication

Before return:

1. reread the complete source;
2. verify frame coverage at broad and contained levels without temporal/place census behavior;
3. reconstruct every substantive binding;
4. for each binding, explicitly test its component parts with the independent-variation test;
5. split broad candidates when they contain multiple research-bearing components;
6. suppress wrappers that only package already-retained content;
7. check class assignment and smallest complete natural grain;
8. check literal/source-near requirements and source posture;
9. freeze units;
10. rebuild compounds from distinct bindings using only frozen refs;
11. prune duplicate/subset compounds that add no separate relation;
12. verify source order.

The target is a **lightweight component-preserving representation**: neither a lexical census nor a binding summary.

Never target an expected count or infer a hidden archetype.

## 11. Isolation and protected evaluation

The worker must never receive:

- Leah-approved archetype workbook contents;
- archetype rows or expected counts;
- evaluator findings or scored outputs;
- case-specific gold corrections;
- prior failed-output corrections derived from hidden gold;
- the sealed Case 5 source during calibration;
- any Case 5 holdout output.

Mechanical validator feedback may be returned only to correct schema, exact-source, tag-token, identifier, or other deterministic mechanical failures. It is not gold/evaluator guidance.

## 12. Calibration and certification gate

V43 is not certified by existing.

Before sealed holdout use, the same finalized V43 contract and saved-agent lineage must pass immutable Case 2 and Case 6 archetype verification repeatedly, including resolution, lexical preservation, class assignment, and compound construction.

Only then may the protected harness run sealed Case 5 exactly once on that calibrated lineage. If it passes archetypally, retire that lineage, create a brand-new saved agent from this finalized durable contract only, and run sealed Case 5 in a new clean-room session. Certification requires that fresh agent to pass without access to prior sessions or holdout output.

Any failed holdout remains final evidence for that lineage and may not be reused as calibration material.
