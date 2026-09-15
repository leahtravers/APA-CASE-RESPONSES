# Researcher Inventory Durable Worker Contract V42

Status: `ACTIVE CALIBRATION SUCCESSOR — NOT CERTIFIED`
Contract ref: `RI-CONTRACT-V42`
Predecessor: `RI-CONTRACT-V41`
Effective for new calibration only: 2026-09-15

## 1. Scope

Produce the lightweight Researcher Inventory candidate only. Inventory the source; do not interpret it, score APA, infer psychological meaning, draw conclusions, promote records, mint APA IDs, or admit anything to sovereign/production fabric.

This successor preserves V41’s literal lock, hidden-evaluator isolation, immutable-archetype gate, candidate-only boundary, one-shot holdout gate, and clean-room certification requirements. It changes only the semantic selection, class-grain, and compound-grain rules prospectively.

## 2. Why V42 exists

V41’s source-coordinate ledger corrected under-inclusion but remained too close to a semantic/lexical census. In repeated calibration evidence across both approved archetypes, mechanically valid outputs simultaneously over-admitted many grammar-level or phrase-level coordinates and under-represented broader episode/scene frames. Compound differences then cascaded from the wrong unit ledger.

The general correction is to inventory **research-bearing frames and bindings**, not every source-presented semantic coordinate and not only globally indispensable coordinates.

A unit may be local, nested, one-use, peripheral, relational, hypothetical, questioned, prospective, reported, or figurative. It still needs a distinct lightweight research role inside a represented frame or binding. Conversely, a word or phrase is not a unit merely because it is semantically meaningful or can be named by a linguistic category.

## 3. Two-level reconstruction: frame skeleton, then binding ledger

Read the complete source before extracting any class.

### 3.1 Frame skeleton

First reconstruct the source’s lightweight FRAME SKELETON: the episodes, interactions, periods, scenes, reported/recollected frames, intended/hypothetical/prospective frames, recurring frames, and present-reflection/telling frames needed to navigate represented material across the source.

The frame skeleton is not an event census. Several lexical time expressions may belong to one frame. A frame may be supported even when the source does not explicitly name a place or time.

### 3.2 Research-bearing binding ledger

Then reconstruct a BINDING LEDGER of the source-presented relations, characterizations, choices, orientations, participants, and referents that materially populate or distinguish those frames.

A binding is the smallest useful source relation/characterization structure that preserves a separate research fact about who/what is related, characterized, located, acted on, contemplated, compared, questioned, reported, or oriented.

Do not turn every clause, predicate, modifier, prepositional phrase, temporal expression, or referential wrapper into a separate binding.

## 4. Local contribution test

For every candidate unit, ask:

1. **Source basis** — Is it source-presented, or is it a permitted supported unnamed PLACE/TIME frame?
2. **Research-bearing role** — Does it preserve a distinct participant, referent/content, characterization, action/relation, orientation, scene, episode, or period that belongs to at least one represented binding/frame?
3. **Local distinctness** — Does it contribute something beyond the grammatical or lexical realization of another retained unit/binding? It need not be globally indispensable, but it must do a separate local job.
4. **Natural grain** — Is this the smallest complete natural unit for that research role rather than an arbitrary fragment or a sentence-sized wrapper?
5. **Non-duplication** — After coreference/alias and function reconciliation, is it genuinely distinct from an already retained unit of the same class/function?

Retain only if all five are satisfied.

Do **not** add a global rule that omission must collapse the whole source relation. Do **not** weaken the local-distinctness test merely because wording is explicit in the source.

## 5. Anti-census and anti-flattening controls

V42 is not a lexical census, part-of-speech census, modifier census, semantic-role census, proposition census, event census, tense/aspect census, preposition census, or named-entity census.

Reject candidates whose only justification is one of the following:

- the wording is explicitly present;
- the phrase has semantic content in ordinary language;
- a parser could assign it a grammatical role;
- it is a temporal expression, prepositional phrase, copular predicate, reporting wrapper, relative clause, or complement;
- it is nested inside a retained binding but contributes no distinct research coordinate;
- it restates the semantic content already owned by another retained class without a separate function.

At the same time, do not flatten away supported scene/episode coordinates, represented actors, tracked referents, source-presented choices/relations, distinct characterizations, operative relation edges, or material orientations merely because they are unnamed, dependent, local, or appear once.

## 6. Class rules

### PLACE

Retain physical scene/location coordinates that locate a represented episode, interaction, conversation, wait, departure/destination, recollection, recurring activity, or present telling/reflection. A broad setting and a materially contained scene coordinate may both exist when each helps navigate represented material.

Supported unnamed PLACE coordinates are permitted when a distinct represented interaction/episode has a physical setting even though the source does not name it. For supported unnamed PLACE, `source_wording` may be null and `source_cue` must be exact source text.

Do not create PLACE merely from a surface, object part, container, counter, wall, floor, line, distance, or spatial noun that only locates an object/relation. Such wording may still support OBJECT or LOCATOR when those functions are present.

### TIME

Retain episode/period/frame coordinates that organize represented material in source progression or posture. A TIME may be named or supported/unnamed and may cover a recalled period, interaction, waiting episode, recurring span, intended/hypothetical/prospective frame, broader life period, later report, or present reflection/telling.

Temporal wording is evidence for a frame; it is not automatically a separate TIME unit. Do not create one TIME for every date word, adverb, duration phrase, deictic, `when`/`while` span, recurrence word, or tense/aspect marker. Consolidate lexical temporal cues when they locate the same research frame. Retain separate TIME coordinates only when they distinguish separate episode/period/frame roles.

For supported unnamed TIME, `source_wording` may be null and `source_cue` must be exact source text.

### PERSON

Retain the speaker plus every represented human/social actor or stable actor group that participates in or is materially related to represented content. Relational, possessive, prospective, reported, and one-use actors may qualify. Resolve aliases/coreference before deduplication. Independent action is not required.

Do not create PERSON from grammatical person marking alone or from an analyst-invented actor category.

### OBJECT

Retain concrete, abstract, internal, relational, choice-like, set/category, figurative, or represented-content referents when the source treats them as a distinct thing/content that is tracked, possessed, located, transferred, evaluated, contemplated, selected/rejected, compared, acted on, reported about, or used as the content of a represented relation.

A source-presented decision, choice, relation, value, figurative object, or internal object may therefore qualify.

Reject bare anaphoric/discourse wrappers, unspecified placeholders, clause/proposition packaging, or event/predicate nominalizations when they add no separately tracked content beyond a retained binding. Do not create an OBJECT merely because a verb takes a complement. If the source itself treats the content/choice/relation as a distinct referent, retain it; otherwise let the binding carry it.

### LABEL

Retain source-presented characterizations, corrections, classifications, comparisons, states, manners, evaluations, questioned labels, and explicit acceptance/rejection responses when they independently characterize a retained participant/referent/binding.

Preserve colloquial form, uncertainty, question, correction, comparison, and negation.

When copular/state wording merely assigns a characterization and contributes no separate relation beyond that characterization, LABEL owns the semantic content; do not emit a duplicate VERB solely for the copular assignment. A VERB may coexist when a distinct operative relation edge remains.

### VERB

Retain the smallest complete literal predicate kernel for an operative action, relation, state transition, possession, perception, communication, cognition, report, or modal/questioned relation **when that edge itself is research-bearing**: it connects retained participants/content, establishes or changes a frame, advances a represented episode, or preserves a distinct relation not already exhausted by a LABEL/OBJECT/frame.

Use the natural predicate grain. Keep particles, complements, negation, or coordinated material with the kernel when splitting would create support fragments or change the relation. Prefer one complete source relation over auxiliary/main-verb fragments or nested restatements of the same action.

Do not emit a VERB merely because a clause contains a predicate. Reject support auxiliaries, bare copular assignment already represented as LABEL, identifying relative-clause scaffolding, and reporting/thought/complement scaffolding that contributes no distinct research relation. Communication, cognition, report, or perception **is** retained when the act/relation itself is a represented event or relation, rather than merely a carrier for other content.

### LOCATOR

Retain the smallest complete source-presented orienting span that materially locates or orients a retained participant, referent, relation, or frame by position, path, origin/destination, entry/exit, containment/proximity, accompaniment/carrying, recurrence orientation, or other spatial/relational direction.

LOCATOR is not PLACE: a surface/path/position may orient something without being a scene coordinate. Cross-class overlap is allowed when the same wording genuinely performs a distinct orientation function in addition to another class.

Reject prepositional/argument-marking phrases that merely identify a recipient, possessor, complement, or grammatical relation and add no independent orientation. Reject isolated function-word/deictic fragments when the complete orienting span is the natural unit.

## 7. Literal lock and source-near tags

- Every non-null `source_wording` is a character-for-character contiguous substring of the source.
- Every `source_cue` and non-null `order_cue` is a character-for-character contiguous substring of the source.
- Preserve punctuation, apostrophes, hyphens, capitalization, spelling, dialect, negation, uncertainty, question, comparison, intention, hypothetical, report, recurrence, correction, and prospective posture.
- `researcher_short_tag` is compact and source-near. For an explicitly worded coordinate, build it only from words already present in that coordinate’s exact `source_wording` and/or `source_cue`; do not add synonyms, explanatory adjectives, or analyst wording.
- Supported unnamed PLACE/TIME may use a neutral navigation tag because `source_wording` is null.
- Copy literal spans from source; do not reconstruct them from memory.

## 8. Ordering and identity

Code owns canonical IDs. The worker supplies neutral canonical keys only for alias/coreference merge.

Order units by first source establishment after coreference, subject to apparatus rules that place the speaker first and broad-before-contained PLACE/LOCATOR coordinates when established together. Do not reorder by importance.

## 9. Unit freeze, then lightweight compound reconstruction

Complete and freeze the unit ledger first. Compounds may not create, suppress, merge, repair, or rename units.

Then reconstruct compounds from the frame skeleton and binding ledger.

Emit one compound for each distinct lightweight research-bearing source binding that is useful to preserve as a relation/characterization/episode unit. A compound should normally have a clear binding anchor: an operative VERB, a characterization LABEL attached to its bearer/content, or another explicit source relation among retained units.

Do not emit:

- every grammatical clause;
- every possible subset of a larger binding;
- both a broad binding and every nested restatement when they preserve no additional research relation;
- one compound merely because two retained units co-occur in a sentence;
- a compound whose only purpose is to repair or compensate for a bad unit ledger;
- sentence-sized mega-compounds that collapse several distinct source relations.

A larger compound and a nested compound may both exist only when each preserves a genuinely separate source binding. Characterization-only bindings need not invent a duplicate copular VERB.

`qualities_available` is a boolean only; it never creates a unit. Q is mechanical output metadata, not a semantic unit.

## 10. Final whole-source adjudication

Before return:

1. reread the entire source;
2. reconstruct the frame skeleton again from scratch and verify that each distinct represented episode/interaction/period needed for navigation has appropriate PLACE/TIME support;
3. verify that each substantive represented relation/characterization has its materially participating PERSON/OBJECT/LABEL/VERB/LOCATOR units where applicable;
4. run the local-contribution test on every retained unit and remove lexical/grammatical census residue;
5. check class assignment and natural complete grain, especially LABEL-versus-VERB, PLACE-versus-LOCATOR, and frame-TIME-versus-temporal-wording distinctions;
6. check exact literal/source-near requirements and source posture;
7. freeze units;
8. rebuild compounds from distinct research-bearing bindings using only frozen refs;
9. prune duplicate/nested compounds that add no separate binding;
10. verify source order.

The target is a **lightweight, research-bearing representation of the source**, not maximum coverage of words and not minimum unit count.

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

V42 is not certified by existing.

Before sealed holdout use, the same finalized V42 contract and saved-agent lineage must pass immutable Case 2 and Case 6 archetype verification repeatedly, including resolution, lexical preservation, class assignment, and compound construction.

Only then may the protected harness run sealed Case 5 exactly once on that calibrated lineage. If it passes archetypally, retire that lineage, create a brand-new saved agent from this finalized durable contract only, and run sealed Case 5 in a new clean-room session. Certification requires that fresh agent to pass without access to prior sessions or holdout output.

Any failed holdout remains final evidence for that lineage and may not be reused as calibration material.
