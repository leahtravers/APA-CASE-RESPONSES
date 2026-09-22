# APA Researcher Inventory Agent Contract V150

Status: `ACTIVE SUCCESSOR FOR CALIBRATION — NOT CERTIFIED`  
Contract version: `RI-CONTRACT-V150`  
Predecessor: `RI-CONTRACT-V149`  
Effective date: 2026-09-21  
Authority: Leah's standing Researcher Inventory calibration instruction

## 1. Mission

Given one source case and the researcher interest `lightweight researcher inventory only`, return a source-faithful candidate Researcher Inventory that preserves the source's represented coordinates and source-native primitive roles at the grain needed to reconstruct the presented material.

This is a representational inventory. It is not a word census, clause parse, proposition inventory, event extraction, summary, diagnosis, interpretation, or ontology-building exercise.

The target lies between two errors:

- **undercoverage:** dropping a genuine source-staged coordinate because it is unnamed, low-salience, one-use, relation-bound, remembered, reported, recurrent, intended, questioned, prospective, figurative, or part of present telling;
- **overcoverage:** promoting every lexical predicate, modifier, temporal/spatial cue, descriptive quality, discourse shell, syntactic relation, or sub-fragment into its own primitive merely because it can be assigned a class meaning.

V150 preserves V149's class-local reasoning and complete-source-atom rule. It corrects the remaining ambiguity in `inventory-coordinate identity`: a source fragment is not a primitive merely because it can be tracked or semantically interpreted. The source must promote it into a distinct class coordinate that makes a nonredundant local reconstructive contribution.

## 2. Controlling V150 principle — promoted coordinate plus local reconstructive contribution

For every primitive candidate, apply the following tests in order.

### Test A — represented class function

Does the source actually present this candidate as a PLACE, TIME, PERSON, OBJECT, LABEL, VERB, or LOCATOR function under the class rules below?

If no, exclude it.

### Test B — primary represented role

What role is the source using this material to perform at this occurrence?

Choose the class that best preserves that represented role. Surface vocabulary, part of speech, and the fact that another class could also describe the words do not create another primitive.

Cross-class duplication is exceptional. The same exact span may be retained in more than one class only when the source separately stages both functions as distinct coordinates, not because the analyst can parse it two ways.

### Test C — promoted-coordinate test

Has the source promoted this material into a distinct coordinate at that class's own grain, or is it only evidence, wording, quality, argument, support, or context inside another retained coordinate or binding?

A candidate is promoted when at least one is true:

- it is itself a distinct represented setting, temporal frame, actor, or source-treated referent;
- it carries a distinct characterization, relation, or orientation that cannot be reconstructed from another retained primitive plus the source-presented binding in which it participates;
- the source separately points to, contrasts, questions, revisits, corrects, reuses, or otherwise treats the candidate as a distinct represented unit;
- for unnamed PLACE/TIME, the source distinctly stages the position or frame as an organizing coordinate needed to reconstruct the scene or phase.

A candidate is **not** promoted merely because it is grammatically predicated, lexically meaningful, temporally/spatially suggestive, descriptive, metaphorical, or available as a possible semantic label.

### Test D — local nonredundancy

If this candidate were removed while all other retained primitives, exact source cues, qualities, and minimal compounds remained, would a distinct source-presented coordinate or relation/state/orientation/reference be lost?

- If yes, retain it, even if it is one-use, low-salience, local, generic, or relation-bound.
- If no, exclude it as redundant evidence/cue/quality/wording rather than promote it to a primitive.

This is a **local class-grain** test. It must never be converted into a requirement for global importance, recurrence, cross-context reuse, research salience, or a scaffold-level distinction. V147's global relation ceiling remains rejected.

## 3. Mandatory whole-source construction order

Perform one coherent whole-source pass.

### Pass A — map represented scenes, frames, actors, referents, and transitions

Read the entire source in source order. Track current, remembered, reported, recurrent, intended, hypothetical, questioned, prospective, figurative, and present-telling material. Notice scene changes, phases, positions, recurrences, recollections, later explanations, and transitions without yet turning every cue into a primitive.

### Pass B — positive candidate capture by class

Build broad candidate sets for all seven classes by represented source function:

- PLACE: represented where-coordinates;
- TIME: represented when/period/phase/frame coordinates;
- PERSON: stable represented human/social endpoints;
- OBJECT: source-treated referents;
- LABEL: source-applied promoted characterizations/states/qualities/statuses/evaluations;
- VERB: source-native promoted action/state/relation moves;
- LOCATOR: source-native promoted orientation/path/context/relative-position moves.

Positive capture is intentionally permissive. Final primitive membership is decided only after the promotion, primary-role, and local-nonredundancy audits.

### Pass C — primary-role and promotion audit

For every candidate apply Tests A through D from Section 2.

Exclude material that is only:

- unsupported inference or analyst paraphrase;
- true same-class alias/coreference/repetition already represented at the same grain;
- a dependent lexical/syntactic fragment inside another complete source-native atom;
- an incidental descriptive quality that can remain source evidence or set `qualities_available` without becoming a LABEL;
- an incidental temporal/spatial cue that does not organize a distinct TIME/PLACE or promoted LOCATOR coordinate;
- grammar, support, discourse management, quotation framing, or rhetorical packaging with no distinct inventory role;
- an argument/content shell whose identity is fully recoverable from another retained primitive or compound;
- an alternate class parse when one primary represented role already accounts for the occurrence;
- a redundant broader/narrower span that adds no distinct class coordinate.

Do not use `not globally important`, `only appears once`, or `not independently reusable` as exclusion reasons.

### Pass D — complete-source-atom reconciliation

For LABEL, VERB, and LOCATOR, use the **smallest complete exact contiguous source-native span** that expresses one promoted class unit.

`Smallest complete` is not the same as `fewest words`.

Keep the words needed to preserve the unit's identity, including as applicable predicate head, complement, particle, polarity, modality, degree, aspect, comparison, path, or orientation.

Do not emit as standalone primitives:

- dependent intensifiers or degree words whose identity belongs to a host characterization;
- bare support/copular/auxiliary/control fragments when the same relation is completed by adjacent wording;
- bare particles/prepositions/deictics whose meaning is only syntactic attachment;
- quotation/reporting scaffolding when it contributes no separate promoted relation beyond the represented content or reporting relation already retained;
- a shortened sub-fragment when removing neighboring words changes which source relation, characterization, or orientation is represented.

Split genuinely independent coordinated or serial moves only when each separately passes the promoted-coordinate and local-nonredundancy tests.

### Pass E — structural PLACE/TIME recall

Replay the source specifically for PLACE and TIME after relation-like lexical grain is stable.

Restore distinct source-staged structural coordinates lost because they were unnamed or implied by scene/phase rather than named by a location/time noun.

An unnamed structural coordinate may be retained when the source distinctly stages its reconstructive identity through a scene, participant position, phase, recurrence, memory, intended period, later explanation, present-telling frame, or other bounded frame cue.

Do not manufacture a PLACE/TIME for every predicate. A structural coordinate must organize a represented scene/position or temporal phase, not merely be inferable from the fact that something happened somewhere/sometime.

### Pass F — PERSON/OBJECT recall and class arbitration

Replay for stable human/social endpoints and source-treated referents. Merge only true same-class aliases/coreference/repetition at the same represented grain.

When an expression could superficially fit more than one class, return to its primary source role. Do not duplicate an OBJECT as PLACE, a LABEL as OBJECT, or a LOCATOR as TIME merely because the words permit that reading.

### Pass G — quality-channel audit

Review descriptive material attached to retained coordinates.

A description can support `qualities_available = true` without becoming its own LABEL. Promote a LABEL only when the characterization itself passes Tests B through D as a distinct represented coordinate.

This prevents ordinary adjectives, incidental descriptions, quoted naming modifiers, and scene texture from becoming a characterization census.

Freeze primitive membership after this audit.

### Pass H — compound replay

Replay the source and emit minimal source-presented bindings among two or more frozen primitives. Compounds reuse primitives only. They never create, merge, delete, retype, split, or repair primitives.

## 4. PLACE — represented settings and staged positions

PLACE inventories distinct physical or institutional settings and represented positions/sites.

Retain:

- named settings;
- contained/local positions inside a broader setting when separately staged;
- participant/referent positions when the source distinctly stages them;
- remembered, reported, prospective, or present-telling settings;
- unnamed settings/positions when the scene or transition gives them distinct reconstructive identity.

Do not promote every spatial noun, surface, container, object location, body part, path phrase, or orientation cue to PLACE. A spatial referent may instead be OBJECT; a path/context expression may be LOCATOR; an incidental surface may remain only source evidence.

A PLACE may be provisional when two source-staged positions could physically coincide. Preserve distinct source staging rather than collapsing them by analyst inference.

For genuinely unnamed PLACE use null `source_wording`, an exact source cue, and neutral mechanical tag/note wording only.

## 5. TIME — organizing temporal frames, not temporal vocabulary or every event

TIME inventories distinct represented temporal coordinates: periods, spans, phases, episodes, recurrence frames, intended/anticipated periods, remembered/reported periods, future-similar horizons, and present-telling/reflection frames.

A TIME does not require a date, duration, clock expression, or explicit temporal noun.

Retain a TIME when it organizes one or more represented relations as a distinct phase/frame or materially separates one source stage from another.

A temporal adverb, frequency word, duration phrase, tense cue, recurrence marker, or event occurrence is not automatically a TIME. It may simply be source evidence for a broader retained frame.

A source-staged action/interaction may anchor an unnamed TIME when the source presents it as a distinct phase through sequencing, transition, recurrence, intended duration, later reflection, or grouping of relations.

Do not make every predicate its own TIME. Retain broad and contained frames only when each independently organizes source material.

For genuinely unnamed TIME use null `source_wording`, an exact source cue, and neutral mechanical tag/note wording only.

## 6. PERSON — stable represented human/social endpoints

PERSON inventories `B` plus every distinct stable human or social actor/group represented by the source after strict coreference.

A PERSON may qualify through acting, speaking, perceiving, being acted upon, possession, accompaniment, benefit, relation to another actor, remembered/reported presence, or prospective social standing. Prominent dialogue is not required.

Possessive or relational mention may establish a PERSON when it clearly identifies a stable represented endpoint rather than a generic grammatical possessor.

Exclude rhetorical/generic addressees, unstable pronouns without resolvable endpoints, hypothetical placeholders without stable represented standing, and true aliases/coreference duplicates.

Order non-speakers by first material represented participation.

## 7. OBJECT — source-promoted referents, not noun census

OBJECT inventories concrete or abstract things that the source itself treats as distinct referents.

Retain a source-native nominal, deictic, possessive, decision, choice, relation, internal, or abstract handle when the source gives it referential standing: it can be tracked, selected, possessed, compared, evaluated, questioned, revisited, acted on, pointed back to, or distinguished as a thing.

Do not promote a noun merely because it denotes something. Exclude:

- analyst-created noun phrases summarizing a clause/relation;
- propositions/reports converted into objects without source reification;
- discourse shells or generic content handles fully recoverable from another relation/compound;
- abstract words whose primary source role is characterization rather than referent;
- a setting whose primary represented function is PLACE;
- a spatial expression whose primary role is orientation/LOCATOR;
- incidental noun-like texture with no promoted referential standing;
- unstable pronouns/demonstratives that resolve entirely to another retained coordinate.

Use the smallest complete referential atom, not the shortest noun-like fragment.

## 8. LABEL — promoted characterizations, not every quality

LABEL inventories source-applied states, qualities, statuses, identities, classifications, evaluations, comparisons, manners, intensities, polarities, corrections, rejections, uncertainty-marked characterizations, and characterization questions **only when the characterization itself is promoted as a distinct represented coordinate**.

A descriptive word or phrase may remain source evidence and make `qualities_available = true` without becoming a LABEL.

Promote a LABEL when the source separately treats the characterization as a state/evaluation/classification/comparison that contributes a distinct reconstructive relation to a retained coordinate, including when it is questioned, corrected, contrasted, revisited, or explicitly applied as a characterization.

Do not create LABEL rows for incidental attributive texture, naming modifiers, degree words, discourse adverbs, or descriptions whose only role is to supply qualities of another coordinate.

Use the smallest complete exact characterization atom and preserve wording/posture exactly.

## 9. VERB — promoted source-native relation moves, not predicate census

VERB inventories distinct represented actions, processes, states, perceptions, cognitions, reports, intentions, possessions, comparisons, movements, waiting relations, question-bearing relations, negated relations, and other predicate/relation moves **when the source promotes the relation itself as a distinct local reconstructive unit**.

The presence of a verb or predication is necessary evidence, not sufficient admission.

Retain a VERB when its removal would erase a distinct source-presented relation among represented coordinates or a distinct state/action that the source separately stages. Exclude predicate wording whose entire representational contribution is already carried as an incidental quality, a primary LABEL, an OBJECT naming phrase, a LOCATOR orientation, grammatical support, discourse/reporting scaffolding, or another complete retained relation.

Lexical grain:

- use the smallest complete exact contiguous span preserving one promoted relation move;
- keep matrix/control/support wording with its predicate/complement when together they form one relation identity;
- do not emit bare auxiliaries/copulas/support/control fragments;
- keep polarity, modality, aspect, particle, and required complement wording when removing it changes relation identity/posture;
- split coordinated/serial moves only when each independently passes the promoted-coordinate test;
- do not absorb separable participants, referents, sites, times, characterizations, or orientations that are their own primitives;
- do not normalize to lemmas, analyst synonyms, or conventional predicate names.

A sentence may yield zero, one, or several VERBs. Never treat clause count or verbal-token count as a target.

## 10. LOCATOR — promoted orientation/context atoms, not spatial-language census

LOCATOR inventories source-native wording that distinctly locates, directs, orients, positions, contains, moves, approaches, departs, enters, exits, accompanies, carries, relates source-to-target, marks situational placement, or supplies a represented figurative/comparison orientation.

A spatial/temporal/context-like phrase is not automatically a LOCATOR. Promote it only when the orientation itself contributes a distinct local reconstructive coordinate or binding.

Exclude:

- routine prepositions/recipient/topic marking/possessive syntax;
- isolated deictics without their complete orientation identity;
- figurative or descriptive wording whose primary source role is LABEL rather than orientation;
- reported slogans/content merely containing location language without actually orienting a represented coordinate;
- shortened path fragments whose meaning exists only inside a larger complete atom;
- temporal cues whose primary role is evidence for a TIME frame rather than orientation.

Use the smallest complete exact orientation atom. LOCATOR does not replace a distinct PLACE/TIME coordinate.

## 11. Cross-class arbitration and legitimate multiplicity

Type by represented source role, never by vocabulary shape or part of speech.

When one occurrence appears class-compatible in several ways, choose the **primary represented role** that preserves what the source is doing with it.

Cross-class duplication requires positive evidence that the source separately stages both functions as distinct coordinates. Ambiguity, analyst convenience, or semantic possibility is insufficient.

No class absorbs another, but no class should duplicate another without distinct source staging.

## 12. Literal, contiguity, and posture lock

Every source-derived non-null string must preserve source language character-for-character where the schema requires source text.

Never synonymize, lemmatize, repair spelling/grammar, normalize dialect, expand contractions, translate, polish, diagnose, standardize a category name, change number, or substitute a conventional expression.

Never add a word not present in the exact contiguous source span. Never concatenate noncontiguous fragments. `source_wording`, `source_cue`, and `order_cue` must be exact source text where applicable. Only genuinely unnamed PLACE/TIME may use null `source_wording`.

If validation rejects a proposed source string, choose an exact contiguous source span or an allowed unnamed structural coordinate. Never invent a near-source repair.

Questions, uncertainty, hypotheticals, negations, corrections, remembered possibilities, reported material, attribution, and proposed future actions remain in source posture. Inventorying does not assert truth or realization.

## 13. `qualities_available`

`qualities_available` is mechanical. True means the source supplies material qualities/descriptions associated with that coordinate; false otherwise.

A source description may justify `qualities_available = true` without becoming a LABEL primitive. Do not split or create primitives merely to represent descriptive texture already available through this channel.

`Q` is never a primitive.

## 14. Ordering

Default within-class order is first material source anchor after filtering/coreference.

Tie rules:

- broad/whole setting before dependent/contained setting when introduced together;
- whole before dependent part at the same anchor unless source order stages the part first;
- PERSON follows first material represented participation;
- remembered/reported/hypothetical/future material stays at source position rather than external chronology.

The apparatus owns canonical IDs and deterministic numbering.

## 15. Promoted-coordinate completeness audit

Before compounds, replay the source separately for each class.

For every proposed primitive ask:

1. Does it actually perform this class function?
2. What is its primary represented role at this occurrence?
3. Has the source promoted it into a distinct coordinate, or is it only evidence/quality/cue/argument/support inside another retained coordinate?
4. If removed while the remaining primitives, qualities, source cues, and compounds remain, what distinct local reconstructive information is lost?
5. Am I keeping it only because it is lexically meaningful, grammatically predicated, spatial/temporal sounding, or available as a semantic parse?
6. Did I miss an unnamed PLACE/TIME because its frame is staged structurally rather than lexically?
7. Did I create cross-class twins without separately staged functions?
8. Did I drop a genuine local coordinate merely because it is one-use, low-salience, relation-bound, generic, or not globally important?

Correct both structural omissions and semantic-census inflation before compounds.

## 16. Complete-atom audit

For every LABEL, VERB, and LOCATOR ask:

- Is this exact contiguous span source-native?
- Is it complete enough to preserve one whole promoted characterization/relation/orientation identity?
- Is any part merely separable participant/referent/site/time wording?
- Is the candidate only an auxiliary, intensifier, support word, particle, preposition, deictic, naming modifier, or discourse shell whose identity belongs elsewhere?
- Did I split one promoted relation into dependent lexical pieces?
- Did I fuse two independently promoted moves?
- If duplicated across classes, does the source separately stage both roles?

Prefer the smallest complete promoted atom, not the shortest possible fragment.

## 17. Anti-reification and anti-census audit

A complete inventory is not a transcription and not an inventory of every interpretable semantic fragment.

Remove:

- pure grammar;
- incidental descriptive qualities that belong only to source evidence/`qualities_available`;
- dependent lexical fragments already carried by a complete retained atom;
- analyst paraphrases/inferred categories;
- true aliases/coreference duplicates;
- alternate class parses without distinct source staging;
- proposition/discourse shells without source reification;
- temporal/spatial cues that do not become organizing coordinates;
- every-event-as-TIME and every-spatial-noun-as-PLACE errors;
- every-predicate-as-VERB, every-adjective-as-LABEL, and every-preposition/path-word-as-LOCATOR errors;
- scene-wide or clause-wide fused primitives that should be separate promoted atoms.

Do not remove a genuine coordinate solely because it appears once, is locally bounded, generic, small, or not globally important.

Never aim for a hidden count.

## 18. Compound construction

Freeze all primitives first.

A compound represents one minimal source-presented binding among two or more frozen primitives that co-participate in a reconstructively distinct relation, characterization, orientation, state, transition, or other source-staged connection.

Create a compound only when:

1. at least two frozen primitives are actively bound by the source in one distinct connection;
2. preserving that binding adds reconstructive information beyond isolated primitives;
3. the member set contains only primitives active in that connection; and
4. the compound is not an alternate parse, duplicate/subset alias, pairwise/transitive closure, clause census, or scene-wide mega-bundle.

One clause may yield zero, one, or several compounds. Several clauses may contribute to one compound when they clearly continue the same binding.

VERB/LABEL/LOCATOR participate when active. PLACE/TIME participate when they actually locate or temporally organize the binding.

A compound cannot create, delete, merge, split, retype, or substitute for primitives.

## 19. Isolation and candidate boundary

The worker must never receive:

- Leah-approved archetype rows or workbooks;
- expected counts;
- evaluator findings;
- scored predecessor outputs;
- canonical archetype extracts;
- case-specific hidden corrections/examples;
- sealed holdout source or output;
- prior holdout sessions.

The worker receives only this durable contract, the bounded runtime request, and the source case authorized for that run.

All calibration output remains candidate research. Worker completion, repeated passes, evaluator success, or certification does not itself promote any record to admitted APA data, Oval Office records, or sovereign fabric.

## 20. Calibration and certification gate

Before any sealed holdout becomes eligible:

1. immutable Case 2 and Case 6 workbook bytes must match their separately governed expected hashes;
2. both approved archetypes must repeatedly pass under the same finalized durable contract and saved-agent lineage;
3. all deterministic harness tests must pass;
4. all failed/partial attempts must remain preserved.

After that gate, the calibrated lineage may run the sealed holdout exactly once. No repair to that lineage may be learned from the holdout result.

If the one-shot holdout is archetypal, retire the calibrated lineage. Create a brand-new saved agent containing only this finalized durable contract, with no access to prior agent sessions or holdout output, and run the holdout once as clean-room verification.

Certification requires that fresh agent to succeed.

No worker, harness, or calibration action may promote records to Oval Office, mint APA IDs, or mutate APA database/fabric.
