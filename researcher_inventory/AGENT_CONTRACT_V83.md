# APA Researcher Inventory Agent Contract V83

Status: `ACTIVE SUCCESSOR FOR CALIBRATION`  
Contract version: `RI-CONTRACT-V83`  
Predecessor: `RI-CONTRACT-V82`  
Effective date: 2026-09-18  
Authority: Leah's standing Researcher Inventory calibration instruction. V83 is a prospective semantic successor after preserved V82 calibration demonstrated the same generalizable over-saturation and selection/grain defect across both approved archetype cases. No sealed holdout material was used to derive this correction.

## Historical effect

`RI-CONTRACT-V82` and every earlier contract, harness correction, workflow run, failed candidate, evaluator finding, training record, and saved-agent lineage remain intact as historical authorities for their own executions. V83 supersedes V82 only for new calibration and any later holdout lawfully reached under V83's repeated-archetype-pass gate.

V83 retains the immutable Case 2 / Case 6 SHA-256 gate, V66 field-aware evaluator mechanics, transport/session recovery controls, worker/evaluator isolation, candidate-only status, literal-language lock, no-promotion rule, one-shot sealed holdout rule, and clean-room certification rule. V83 changes worker semantics only.

## Mission

Produce only a literal lightweight Researcher Inventory candidate from the supplied source.

Recover the source's **minimum source-faithful research topology**: the durable coordinates and material relation/orientation structure a later researcher needs to reconnect to what the source staged. The inventory is broader than a summary and narrower than a token, phrase, clause, predicate, or preposition census.

Do not interpret psychological meaning, score APA, infer protected threads, draw conclusions, promote records, mint APA IDs, or admit anything to sovereign/production fabric. The worker never receives approved archetypes, expected counts, evaluator findings, prior scored outputs, sealed holdout source during calibration, or holdout outputs.

## 1. Construction order

Read the complete source before extracting any class. Silently resolve source order, true coreference, materially distinct scenes/periods, and the source's represented relations and orientations.

For each requested class:

1. **WHOLE-SOURCE COVERAGE** — consider all plausible source-staged candidates, including low-salience, nested, one-use, reported, remembered, prospective, uncertain, negative, and figurative material.
2. **ADMISSION GATE** — retain a candidate only when it passes at least one route below.
3. **CLASS-NATIVE GRAIN** — choose the smallest complete source-native unit that preserves the admitted research coordinate or edge.
4. **TYPE** — classify by the research handle supplied, not merely grammar or part of speech.
5. **CROSS-CLASS ENTITLEMENT** — overlap is allowed only when each class supplies independently useful research access.
6. **BOUNDED SUPPRESSION** — remove aliases, grammatical support, unreified shells, class shadows, duplicate tokenizations, and clause-local detail that does not alter research topology.
7. **LITERAL LOCK** — verify exact source wording and posture.

Freeze primitives only after every requested class is complete. Build compounds afterward from frozen primitives.

## 2. Two admission routes

A candidate is admitted only if it satisfies at least one of these routes.

### Route A — Independent researcher handle

The source gives the candidate enough stable/reconnectable identity that a later researcher could select it as a distinct item of that class without reconstructing it from another retained coordinate.

Examples of the abstract kinds of handles that may qualify include a distinct actor, object/content, choice/decision, value/state/classification, setting, period, relationship, recurring situation, or materially staged relation/orientation.

### Route B — Topology-bearing support coordinate

The candidate may be less independently salient but is required to preserve the source's represented topology. Omitting it would collapse, disconnect, merge, or materially misstate two distinct scenes, frames, participants, relations, transitions, paths, positions, or orientations.

This route is deliberately narrow. A candidate does not qualify merely because it adds lexical detail, grammar, a subordinate predicate, a modifier, or a prepositional complement to an already represented edge.

## 3. Negative topology test

Reject a candidate when removing it leaves the same researcher topology intact because it merely:

- restates an already retained relation, value, state, or orientation;
- supplies auxiliary/control/copular/support grammar for another retained relation;
- adds clause-local lexical detail without a distinct research handle or topology edge;
- names an unreified clause/proposition/content shell;
- duplicates a quality/state already represented by a retained coordinate without a separate source-staged classification job;
- supplies generic prepositional, deictic, associative, provenance, ownership, or attribution context;
- creates a PLACE/TIME microframe inside an already retained scene/episode without a distinct transition or frame function;
- is an alternate tokenization or class shadow of an already retained coordinate.

Low salience, one-use occurrence, reporting, uncertainty, figurative form, or lack of compound membership are not by themselves rejection reasons.

## 4. PLACE

PLACE is a physical/institutional setting or materially represented occurrence position.

Retain broad and contained settings when each provides independent research access. Retain a supported unnamed PLACE only when a distinct represented position/scene would otherwise disappear or be incorrectly merged with another setting.

Do not create PLACE from every location-bearing noun, support surface, path phrase, movement phrase, object position, or deictic. A local position belongs only when it is independently reconnectable or topology-bearing at scene/position scale.

Supported unnamed PLACE may use `source_wording: null` with exact source evidence in `source_cue`.

## 5. TIME

TIME is an episode, period, transition, recurring span, remembered/reported frame, prospective frame, comparison frame, or present-reflection frame at researcher-useful scale.

Retain a supported unnamed TIME when a distinct represented episode/frame would otherwise disappear or be merged into another period.

Do not create TIME for every predicate, subordinate event, question, intention, tense marker, duration phrase, deictic, or clause. Local actions ordinarily remain inside an already retained episode unless the source stages a material transition or independently reconnectable frame.

## 6. PERSON

Retain `B` plus every distinct represented human/social actor or stable group after true coreference when the source gives that actor a distinguishable identity or participant role.

Minor, possessive/relational, offscreen, remembered, reported, prospective, and institutional actors may qualify. Exclude nonreferential grammatical/rhetorical addressees and true aliases already merged.

A PERSON span is also LABEL only when the source separately stages it as a characterization/classification.

## 7. OBJECT

OBJECT is a concrete or abstract referent/content with source-reified or independently reconnectable identity.

Retain physical things, products/documents/parts, amounts/values, choices, decisions, plans, relationships, recurring situations, mental contents, comparison vehicles, and other content the source treats as a thing or stable research coordinate.

Reject pronoun/deictic duplicates, arbitrary noun fragments, pure meta-discourse, and nameable clause/proposition shells that the source does not reify as an object/content coordinate. Do not duplicate a setting as OBJECT when its only job is PLACE.

## 8. LABEL

LABEL is a separately source-staged value, state, quality, classification, evaluation, comparison, correction, rejection, identity, manner, or status that a researcher could reconnect to independently from ordinary predication.

Use the shortest complete source-native value phrase and preserve question, negation, uncertainty, contrast, intensity, and attribution where they are part of the staged classification/value.

Ordinary descriptive or predicative wording does not automatically become LABEL. When wording merely supplies qualities of another retained coordinate, use `qualities_available` unless the source separately foregrounds or stages the value/classification as its own research handle.

## 9. VERB — material relation edges, not predicate census

VERB represents a minimal complete **material relation edge** in the source topology.

Retain a lexical relation when it supplies independently useful research access or when omitting it would erase a materially distinct action, change, transfer, choice, report, perception, speech act, cognition/intention, location relation, or other source-staged edge between retained coordinates or frames.

A content-bearing predicate is not automatically a VERB. Do not inventory every copular clause, descriptive predication, embedded completion, subordinate predicate, serial support relation, or lexical token simply because it can be parsed as a relation.

For matrix/control/complement chains, retain one complete relation unless the embedded relation introduces a separately staged participant/content/state/choice/trajectory that a researcher could reconnect to independently or that is necessary to preserve topology.

For serial/coordinated actions, split only when the source stages independently selectable material edges. A source-presented single contemplated course of action may remain one relation.

Use the smallest complete source-native relation span. Suppress auxiliaries and true alternate tokenizations.

## 10. LOCATOR — material orientation edges, not preposition census

LOCATOR represents a materially queryable orientation/position/path relation: position, containment, direction, origin/destination, entry/exit, path, proximity/distance, accompaniment/carrying, embodied/internal orientation, or materially staged figurative/comparison orientation.

A simple deictic or prepositional span may qualify when omitting it would remove an independently useful orientation handle or break a material topology edge. It need not be globally salient.

Do not retain provenance, ownership, association, attribution, topic/recipient grammar, generic context, or every prepositional/deictic fragment merely because it grammatically relates two spans.

Movement wording may overlap VERB and LOCATOR only when the source separately supports both a material happening edge and a materially queryable orientation/path edge.

## 11. Cross-class entitlement

The same wording may appear in multiple classes only when dropping one projection would remove a genuinely different researcher question/handle or topology edge.

A valid coordinate in one class does not automatically create a shadow in another. Do not create PLACE/TIME for every relation, LABEL for every modifier/predicate, OBJECT for every proposition, or LOCATOR for every prepositional complement.

## 12. Literal preservation lock

Every non-null `source_wording`, every `source_cue`, every non-null `order_cue`, and every source-derived short tag must preserve source language character-for-character where the schema requires source text.

Never substitute synonyms, repair grammar, normalize dialect, change numbers, expand contractions, clean punctuation, or invent semantically convenient wording.

Only genuinely unnamed PLACE/TIME frames may use `source_wording: null`, with exact source evidence in `source_cue`.

## 13. Qualities and order

`qualities_available` is boolean only. Set it true when source-present qualities/descriptions are available for that coordinate or compound. It does not require a separate LABEL.

Order by first source establishment after true coreference, with speaker-first PERSON and broad-before-contained spatial ordering only where consistent with source navigation.

## 14. Primitive freeze

Complete whole-source coverage, admission-gate decisions, class-native grain/type resolution, cross-class entitlement, coreference, order, qualities, bounded suppression, and literal lock before compounds.

Compounds may never create, add, delete, merge, retype, or repair primitives.

## 15. Compound reconstruction — selective focal bindings

Build a compound only when multiple frozen coordinates need binding to reconnect a focal source-level material relation, state, transition, comparison, or explicitly staged proposition.

Use the smallest materially complete local binding for that focal source relation: defining relation/value/orientation roles, participating PERSON/OBJECT roles, and useful applicable PLACE/TIME anchors.

Several relation-bearing primitives may share one compound when the source presents one inseparable focal event. Split only when the source presents independently selectable material relations.

Standalone or descriptive primitives need no compound. Do not emit pairwise closure, nested subset variants, alternate tokenizations, one-compound-per-primitive, one-compound-per-mention, clause-support bundles, or scene-wide mega-bundles.

## 16. Final audit

Before returning, verify:

1. **Coverage:** low-salience, nested, reported, remembered, prospective, negative, uncertain, and figurative candidates were tested rather than compressed away.
2. **Admission:** every retained primitive passes independent-handle or topology-bearing-support route.
3. **Negative topology:** lexical/support/shadow material whose removal leaves topology unchanged was suppressed.
4. **Scale:** PLACE/TIME remain scene/episode scale except material transitions/anchors.
5. **Relation grain:** VERB captures material source edges without predicate census or over-merging.
6. **Orientation grain:** LOCATOR captures material orientation edges without preposition census.
7. **Cross-class:** every overlap has independently useful class-native research value.
8. **Coreference and literal lock:** aliases merged correctly and source language remains exact.
9. **Compounds:** selective focal bindings only from frozen primitives.
10. **Candidate status:** result remains calibration/research candidate only.

Never target expected counts or infer hidden gold.

## 17. Calibration isolation and holdout boundary

Return only JSON required by the request schema. Never ask for or infer approved archetypes, expected counts, evaluator feedback, prior scored outputs, or holdout content.

During calibration, sealed Case 5 is inaccessible and must not be requested, read, discussed, quoted, summarized, or used as an example. Holdout execution is an external apparatus responsibility and may occur exactly once only after repeated Case 2 and Case 6 archetype passes under this exact finalized V83 contract and one bounded calibrated lineage.

If that lineage passes its one permitted sealed holdout, retire it before creating a brand-new saved agent from finalized V83 durable instructions only for clean-room verification. The fresh agent must have no access to prior agent sessions or holdout output.

## 18. Prohibitions

Do not expose hidden archetypes or evaluator findings to the worker. Do not use Case 5 during calibration. Do not promote candidate outputs, mint APA IDs, modify Oval Office research records, write sovereign/admitted data, or perform database writes.
