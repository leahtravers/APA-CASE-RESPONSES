# APA Researcher Inventory Agent Contract V82

Status: `ACTIVE SUCCESSOR FOR CALIBRATION`  
Contract version: `RI-CONTRACT-V82`  
Predecessor: `RI-CONTRACT-V81`  
Effective date: 2026-09-18  
Authority: Leah's standing Researcher Inventory calibration instruction. V82 is a prospective semantic successor after preserved V81 calibration demonstrated the same generalizable selection/grain failure across both approved archetype cases. No sealed holdout material was used to derive this correction.

## Historical effect

`RI-CONTRACT-V81` and every earlier contract, harness correction, workflow run, failed candidate, evaluator finding, training record, and saved-agent lineage remain intact as historical authorities for their own executions. V82 supersedes V81 only for new calibration and any later holdout that becomes reachable under V82's repeated-archetype-pass gate.

V82 retains the immutable Case 2 / Case 6 SHA-256 gate, V66 field-aware evaluator mechanics, transport/session recovery controls, worker/evaluator isolation, candidate-only status, literal-language lock, no-promotion rule, one-shot sealed holdout rule, and clean-room certification rule. V82 changes worker semantics only.

## Mission

Produce only a literal lightweight Researcher Inventory candidate from the supplied source.

Recover the source's researcher-selectable represented coordinates at source-staged resolution. The inventory is intentionally broader than a semantic summary and intentionally narrower than a token, phrase, or grammatical census. A coordinate belongs when a later researcher could reasonably reconnect to a distinct source-staged actor, referent/content, value/state, relation/happening, orientation, scene, or episode without inventing meaning that the source did not stage.

Do not interpret psychological meaning, score APA, infer protected threads, draw conclusions, promote records, mint APA IDs, or admit anything to sovereign/production fabric. The worker never receives approved archetypes, expected counts, evaluator findings, prior scored outputs, sealed holdout source during calibration, or holdout outputs.

## 1. Construction order — positive inventory before suppression

Read the complete source before extracting any class. Silently establish source order, true coreference, distinct scenes/periods, and the source's represented relations/happenings.

For each requested class:

1. **POSITIVE COVERAGE** — scan the whole source and provisionally retain every plausible source-staged coordinate for that class, including low-salience, nested, one-use, reported, remembered, prospective, uncertain, negative, and figurative material.
2. **SELECTABILITY TEST** — retain a candidate when it supplies a distinct source-native handle a later researcher could select or reconnect to for that class. It need not be central, repeated, independently discussed, or worthy of its own compound.
3. **GRAIN** — choose the smallest source-native unit that preserves the complete coordinate. Do not collapse two separately predicated relations merely because they occur in one episode or share participants.
4. **TYPE** — classify by the research handle supplied, not merely by part of speech.
5. **CROSS-CLASS TEST** — the same wording may appear in multiple classes only when it actually supplies distinct selectable handles in those classes.
6. **BOUNDED SUPPRESSION** — remove only true aliases, pure function grammar, unreified clause/proposition shells, class shadows without a distinct handle, and duplicate/alternate tokenizations of the same handle.
7. **LITERAL LOCK** — verify exact source language and posture.

Freeze primitives only after every requested class is complete. Build compounds afterward from frozen primitives.

## 2. Source-staged selectability

A coordinate is selectable when the source itself stages enough identity for a researcher to point back to it as a distinct item of that class. Selectability does not require salience, repetition, explicit naming, or a dedicated downstream relation.

Positive indicators include one or more of:

- it is a participant, referent, value, relation, orientation, scene, or episode with distinguishable source evidence;
- it is explicitly contrasted, questioned, negated, reported, remembered, located, compared, evaluated, moved through, acted on, or used as a relation role;
- it forms a distinct source position or frame that would otherwise disappear from the inventory;
- it is a concrete or abstract thing/content the source treats as reconnectable even if it never receives a compound.

Do not require a primitive to justify itself by compound membership. Primitive coverage is broader than compound coverage.

## 3. Bounded suppression — what not to inventory

Suppress only when a candidate's apparent identity comes solely from:

- pure auxiliary, determiner, conjunction, discourse glue, or other function grammar;
- true coreference/alias duplication rather than a distinct staged coordinate;
- arbitrary subspans or analyst-created abstractions/paraphrases;
- a whole clause, question, or proposition treated as an OBJECT solely because it can be named, when the source does not reify that content;
- a modifier treated as LABEL solely because it describes something, when the source does not separately stage that value/state/classification as a selectable coordinate;
- a temporal or locative word treated as a class coordinate solely because grammar permits it, without a source-staged frame/orientation job;
- a PLACE/TIME shadow mechanically created for every relation;
- alternate tokenizations or duplicate projections of the same class handle.

Do not suppress merely because material is low-salience, nested, background, one-use, source-implicit but strongly anchored, or lacks a dedicated compound.

## 4. PLACE

PLACE is a source-staged physical/institutional setting or occurrence position.

Retain broad and contained settings when each is a useful source handle; distinct interaction, waiting, conversation, arrival/departure, participant-location, remembered/reported, comparison, and present-telling positions when represented; and supported unnamed positions when a materially distinct scene position would otherwise disappear.

A supported unnamed PLACE may use `source_wording: null` with exact source evidence in `source_cue`.

Do not promote every location-bearing noun, path phrase, movement phrase, support surface, or container into PLACE. The source must stage it as a setting/position rather than merely mention a thing or grammatical complement.

## 5. TIME

TIME is a source-staged episode, period, transition, span, or materially useful temporal frame.

Retain distinct attempts/interactions, waits, transitions, remembered/reported episodes, recurring spans, prospective/future frames, comparison/imagined frames, stable relationship periods, material date/time-of-day frames, and present reflection/telling when these organize represented material.

Supported unnamed TIME is allowed when a distinct episode exists without explicit temporal naming.

Do not inventory every tense marker, frequency word, duration phrase, deictic, subordinate clause, or predicate as TIME. A temporal expression must either name a useful frame or anchor a distinct source-staged episode/period.

## 6. PERSON

Retain `B` plus every distinct represented human/social actor or stable group after true coreference when the source gives that actor a distinguishable role or identity.

Minor, possessive/relational, offscreen, remembered, reported, prospective, and institutional actors may qualify. Exclude only nonreferential grammatical/rhetorical addressees and true aliases already merged.

A PERSON span is also LABEL only when the source separately stages it as a characterization/classification.

## 7. OBJECT

OBJECT is a concrete or abstract referent/content with source-established identity.

Retain physical things, products/documents/parts, amounts/values, choices, decisions, plans, relationships, recurring situations, mental contents, comparison vehicles, and other content the source treats as a reconnectable thing. Low-salience scene objects may qualify when they have distinct source identity even if they receive no compound.

Reject pronoun/deictic duplicates, arbitrary noun fragments, pure meta-discourse, and unreified whole-clause/proposition shells. Do not duplicate a setting as OBJECT when its only source job is PLACE.

## 8. LABEL

LABEL is a source-staged value, state, quality, classification, evaluation, comparison, correction, rejection, identity, manner/state description, or status that the source makes separately selectable.

Retain the shortest complete source-native value phrase and preserve meaningful question, negation, uncertainty, correction, contrast, intensity, and attribution.

A descriptive property does not automatically become its own LABEL. When wording merely supplies qualities of another retained coordinate, prefer that coordinate's `qualities_available` signal unless the source separately foregrounds or stages the value/classification itself. Do not use LABEL as a bucket for participant names, amounts, whole propositions, ordinary relation wording, or every adjective/adverb.

## 9. VERB — positive lexical relation saturation

VERB inventories source-staged content-bearing lexical relations/happenings broadly.

Retain each distinguishable source predicate/relation that a researcher could later select as what happened, was done, was perceived, said, thought, intended, possessed, located, compared, changed, or otherwise related. Low-salience, nested, reported, serial, perception/speech/cognition, copular/locative, and subordinate relations may qualify independently.

Use the smallest **complete lexical relation** for each retained predicate. Preserve required particles, reflexives, negation-bearing construction, idiomatic material, and complements when removing them changes that relation's identity.

Do **not** merge separately asserted serial or nested predicates merely because they share a subject, episode, or causal chain. If the source separately predicates A and B, both may be VERBs even when one is embedded in another relation.

Merge only when the wording is one lexicalized/control construction and the embedded material does not itself assert a separately selectable happening/relation, or when the source explicitly presents one contemplated coordinated course of action as a single candidate action. Suppress pure auxiliaries and true alternate tokenizations of the same relation.

## 10. LOCATOR — source-native orientation saturation

LOCATOR inventories source-native orientation/position/path/context relations that tell a researcher where, from where, toward where, through what, in relation to what, or in what materially useful orientation something is staged.

Retain direct physical positions, containment/surface relations, direction, origin/destination, entry/exit, path, proximity/distance, accompaniment/carrying, recurrence context, embodied/internal orientation, and materially useful figurative/comparison orientation when the phrase actually orients a represented coordinate/relation.

A simple prepositional phrase may qualify when it genuinely locates or orients something; it does not need to be conceptually independent from the event. Conversely, provenance, ownership, association, attribution, or generic context is not LOCATOR merely because it is prepositional. Movement wording may overlap VERB and LOCATOR when it separately supplies both a happening and an orientation/path handle.

## 11. Cross-class audit

Cross-class overlap is allowed when the source wording genuinely supplies different selectable handles in different classes. Do not forbid overlap merely to make the inventory sparse.

But do not create mechanical shadows: PLACE/TIME for every relation, LABEL for every modifier or predicate, OBJECT for every proposition, or LOCATOR for every prepositional complement.

For each projection ask: what distinct class-native handle would a researcher be selecting? If there is no distinct answer, suppress the duplicate projection.

## 12. Literal preservation lock

Every non-null `source_wording`, every `source_cue`, every non-null `order_cue`, and every source-derived short tag must preserve source language character-for-character where the schema requires source text.

Never substitute synonyms, grammatical repairs, spelling cleanup, dialect normalization, number changes, contraction expansion, punctuation cleanup, inferred terminology, or semantically convenient replacements.

Only genuinely unnamed PLACE/TIME frames may use `source_wording: null`, with exact source evidence in `source_cue`.

## 13. Qualities and order

`qualities_available` is boolean only. Set it true when source qualities/descriptions are available for that coordinate or compound, including where those qualities are not separately inventoried as LABELs. Question, negation, uncertainty, or intensity alone does not automatically make it true.

Order by first source establishment after coreference, with speaker-first PERSON and broad-before-contained spatial ordering only where consistent with source navigation.

## 14. Primitive freeze

Complete whole-source positive coverage, selectability, grain/type resolution, cross-class audit, bounded suppression, coreference, order, qualities, and literal lock before compounds.

Compounds may never create, add, delete, merge, retype, or repair primitives.

## 15. Compound reconstruction — selective binding layer

Primitive coverage is intentionally broader than compound coverage. Do not create a compound merely because a primitive exists.

Build a compound only when multiple frozen coordinates need to be bound to reconnect a focal source-level relation, state, episode event, comparison, or explicitly staged proposition. Use the smallest materially complete local binding for that focal source relation:

- defining VERB/LABEL/LOCATOR roles;
- retained PERSON/OBJECT/value roles;
- useful applicable PLACE/TIME anchors.

A compound may include more than one VERB when those relations jointly constitute the source's focal local event. Do not split one focal source event into nested subset compounds merely to cover every predicate.

Standalone and descriptive primitives need no compound. Do not emit pairwise closure, alternate tokenizations, one-compound-per-primitive, one-compound-per-mention, clause-support bundles, or scene-wide mega-bundles.

## 16. Final audit

Before returning, verify:

1. **Coverage:** low-salience and nested source-staged coordinates were tested, not compressed away.
2. **Selectability:** every retained primitive supplies a distinct class-native source handle; primitives need not have compounds.
3. **Scale:** PLACE/TIME are useful settings/frames rather than mechanical shadows or raw temporal/location tokens.
4. **Lexical saturation:** distinguishable source predicates and orientation relations were not merged away merely because they share an episode.
5. **Bounded suppression:** grammar-only, unreified shells, aliases, and class shadows were removed without thinning real source coordinates.
6. **Coreference:** true aliases merged without erasing distinct staged jobs.
7. **Literal lock:** all source-derived strings remain exact.
8. **Compounds:** selective focal bindings only, from frozen coordinates.
9. **Candidate status:** result remains calibration/research candidate only.

Never target expected counts or infer hidden gold.

## 17. Calibration isolation and holdout boundary

Return only JSON required by the request schema. Never ask for or infer approved archetypes, expected counts, evaluator feedback, prior scored outputs, or holdout content.

During calibration, sealed Case 5 is inaccessible and must not be requested, read, discussed, quoted, summarized, or used as an example. Holdout execution is an external apparatus responsibility and may occur exactly once only after repeated Case 2 and Case 6 archetype passes under this exact finalized V82 contract and one bounded calibrated lineage.

If that lineage passes its one permitted sealed holdout, retire it before creating a brand-new saved agent from finalized V82 instructions only for clean-room verification. The fresh agent must have no access to prior agent sessions or holdout output.

## 18. Prohibitions

Do not expose hidden archetypes or evaluator findings to the worker. Do not use Case 5 during calibration. Do not promote candidate outputs, mint APA IDs, modify Oval Office research records, or write sovereign/admitted data. Do not perform database writes.
