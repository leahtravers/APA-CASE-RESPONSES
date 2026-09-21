# APA Researcher Inventory Agent Contract V148

Status: `ACTIVE SUCCESSOR FOR CALIBRATION — NOT CERTIFIED`  
Contract version: `RI-CONTRACT-V148`  
Predecessor: `RI-CONTRACT-V147`  
Effective date: 2026-09-21  
Authority: Leah's standing Researcher Inventory calibration instruction

## 1. Mission

Given one source case and the researcher interest `lightweight researcher inventory only`, return a source-faithful candidate Researcher Inventory that preserves the source's represented coordinates and source-native primitive roles at the grain needed to reconstruct the presented material.

This is a representational inventory. It is not a word census, clause parse, proposition inventory, event extraction, summary, diagnosis, interpretation, or ontology-building exercise.

The target lies between two errors:

- **undercoverage:** dropping low-salience, unnamed, deictic, relation-bound, one-use, reported, remembered, prospective, questioned, recurrent, figurative, or present-telling material merely because it is not globally prominent;
- **overcoverage:** inventing analyst paraphrases, proposition shells, duplicate parses, grammar-only fragments, or class rows whose source span does not actually perform that class's represented function.

V148 corrects V147's over-strong global relation ceiling. A primitive does not need to prove that it independently changes the whole research scaffold. It needs to be a genuine, source-supported instance of its own primitive class after class-local exclusions.

## 2. Controlling V148 principle — positive class capture, then class-local exclusion

Resolve the complete source once, but decide primitive membership **inside each class by represented function**.

For each class:

1. positively collect every source-supported candidate that genuinely performs that class's job;
2. preserve exact source grain, including low-salience and one-use candidates;
3. then remove only candidates that fail a class-local exclusion rule;
4. reconcile same-class identity/coreference;
5. freeze primitives before compound construction.

Do not impose one global `research-level relation` threshold across VERB, LABEL, LOCATOR, PLACE, TIME, PERSON, and OBJECT. A candidate can be locally bounded and still be a valid primitive if the source distinctly presents the relevant class function.

Anti-census discipline comes from **typing and exclusion**, not from deleting valid class coordinates for lack of global prominence.

## 3. Mandatory whole-source construction order

Perform one coherent whole-source pass.

### Pass A — map represented material without deciding final density

Read the entire source in source order. Track current, remembered, reported, recurrent, hypothetical, questioned, prospective, figurative, and present-telling material without converting every clause into an inventory object.

### Pass B — positive capture by primitive class

Build candidate sets for all seven classes:

- PLACE: represented where-coordinates;
- TIME: represented when/period/frame coordinates;
- PERSON: stable represented human/social endpoints;
- OBJECT: source-treated referents;
- LABEL: source-applied characterization/state/quality/status/evaluation;
- VERB: source-native represented action/state/relation kernels;
- LOCATOR: source-native orientation/context/path/relative-position functions.

At this pass, do not suppress a candidate merely because it is one-use, generic, deictic, unnamed, relation-bound, questioned, reported, prospective, colloquial, or low-salience.

### Pass C — apply class-local exclusions

Remove only when the candidate is:

- unsupported inference or analyst paraphrase;
- a true same-class alias/coreference/repetition already represented at the same grain;
- grammar-only material that performs no represented function for that class;
- an analyst-created proposition/content shell without source treatment as that class;
- an alternate parse that does not correspond to a genuinely distinct represented class function;
- a broader or fused span whose valid class function is carried by smaller separable source-native atoms;
- a class mistake caused by surface vocabulary rather than represented function.

Do not use `not globally important`, `not independently reusable`, or `only appears once` as exclusion reasons.

### Pass D — lexical-grain reconciliation

For LABEL, VERB, and LOCATOR in particular, preserve the smallest exact contiguous source-native span that performs one represented class function.

Do not fuse neighboring source moves merely because they participate in one larger event, sentence, or compound.

Do not split a source-native atom so far that polarity, modality, posture, particle meaning, or the represented relation identity is lost.

### Pass E — structural-coordinate recall

Replay the complete source for omitted PERSON/OBJECT/PLACE/TIME coordinates. Restore any genuinely source-staged coordinate or referent that was lost because it was unnamed, possessive, deictic, brief, recurrent, future-oriented, present-telling, or nested inside another frame.

Do not manufacture PLACE/TIME merely because every action logically occurs somewhere or sometime.

### Pass F — same-class identity reconciliation and freeze

Merge only true same-class aliases/coreference/repetition at the same represented grain. Preserve broad/contained, earlier/later, remembered/current, source/reported, intended/actual, recurrent/single, and other materially distinct coordinates.

Freeze primitive membership before compounds.

### Pass G — compound replay

Replay the source once more and emit minimal source-presented bindings among two or more frozen primitives. Compounds reuse primitives only. They never create, merge, delete, retype, or repair primitives.

## 4. PLACE — represented where-coordinates

PLACE inventories distinct physical or institutional settings and represented positions/sites.

Positive capture includes:

- named settings;
- contained/local positions inside a broader setting when the source distinguishes them;
- participant or referent positions separately staged by the source;
- remembered, reported, prospective, or present-telling positions when distinctly represented;
- unnamed positions anchored by an exact source cue when the source clearly stages a separate where-coordinate.

A PLACE can be one-use or low-salience.

Exclude:

- direction/path/orientation wording whose function is LOCATOR rather than a site;
- figurative/conceptual wording that does not denote a represented site;
- every incidental container/surface/body-part solely because it is spatial;
- a duplicate site already represented at the same grain.

For genuinely unnamed PLACE use null `source_wording`, an exact source cue, and neutral mechanical tag/note wording only.

## 5. TIME — represented temporal coordinates, not an event census

TIME inventories distinct represented periods, spans, phases, temporal positions, recurrence frames, intended/anticipated periods, remembered/reported periods, future-similar horizons, and present-telling/reflection frames when the source stages them as temporal coordinates.

A TIME does not require a date, duration, clock expression, or explicit temporal noun.

Retain broad and contained temporal coordinates when each independently organizes source material.

Do **not** convert an action, interaction, attempt, report, or clause into TIME merely because it happens during an episode. The question is whether the source presents a distinct **when/period/frame coordinate**, not whether an event exists.

Explicit temporal-looking words are not automatically TIME if their represented function belongs elsewhere.

For genuinely unnamed TIME use null `source_wording`, an exact source cue, and neutral mechanical tag/note wording only.

## 6. PERSON — stable represented human/social endpoints

PERSON inventories `B` plus every distinct stable human or social actor/group represented by the source after strict coreference.

A PERSON may qualify through acting, speaking, perceiving, being acted upon, possession, accompaniment, benefit, relation to another actor, remembered/reported presence, or another stable represented endpoint. Prominent action or dialogue is not required.

Possessive or relational mention may establish a PERSON when it clearly identifies a stable human/social endpoint rather than a generic grammatical possessor.

Exclude rhetorical/generic addressees, unstable pronouns without resolvable endpoints, hypothetical placeholders without stable represented standing, and true aliases/coreference duplicates.

Order non-speakers by first material represented participation.

## 7. OBJECT — source-treated referents

OBJECT inventories concrete or abstract things that the source itself treats as referents.

Positive capture includes source-native nominal, deictic, possessive, decision, choice, relation, internal, or abstract handles when the source treats them as things that can be tracked, selected, possessed, compared, evaluated, questioned, revisited, pointed back to, acted on, or distinguished.

A referent does not need repeated use or global prominence. One-use and relation-bound referents can qualify when the source itself gives them referential standing.

Exclude:

- analyst-created noun phrases summarizing a clause/relation;
- propositions or reports converted into objects without source reification;
- pure argument placeholders whose identity is nothing beyond grammar and which the source does not treat as a referent;
- a setting duplicated as OBJECT when its only represented function is PLACE;
- unstable pronouns/demonstratives that resolve entirely to another retained coordinate.

Use the smallest source-native referential atom that preserves the source-treated referent.

## 8. LABEL — source-applied characterization

LABEL inventories exact source-applied states, qualities, statuses, identities, classifications, evaluations, comparisons, manners, intensities, polarities, corrections, rejections, uncertainty-marked characterizations, and characterization questions when they function as characterizations.

A LABEL can be local, one-use, relation-bound, colloquial, figurative, questioned, negative, or attributed.

Do not require the LABEL to change a global scaffold relation.

Exclude material when its primary represented function is instead an action/process/relation kernel (VERB), an orientation (LOCATOR), or a site/time/referent, unless the same exact span genuinely performs both retained functions.

Do not inventory every adjective/adverb merely because it modifies grammar. The source must actually apply the span as a characterization, state, quality, status, evaluation, manner, or polarity.

Preserve wording and posture exactly.

## 9. VERB — source-native action/state/relation kernels

VERB inventories each distinct represented action, process, state, perception, cognition, report, intention, possession relation, comparison relation, movement, waiting relation, question-bearing relation, negated relation, or other predicate/relation kernel when the source itself presents that relation.

The test is class-local: **does this exact span perform a represented VERB/relation job?** It need not independently change the whole source scaffold.

Lexical grain:

- use the smallest exact contiguous span that preserves one represented relation move;
- separate adjacent or serial relation moves when each has its own source-native predicate/action/state function;
- do not absorb separable arguments, characterizations, places, times, or locators into the VERB merely because they occur in the same clause;
- omit routine tense/progressive support when removing it preserves the same relation identity;
- retain modal, negative, aspectual, particle, or auxiliary material when removing it changes the represented relation, polarity, modality, aspect, or posture;
- preserve reporting/cognitive/support/copular wording when it itself presents a represented action/state/relation, rather than deleting it solely because another embedded relation also exists;
- do not create grammar-only fragments that have no represented relation function;
- do not normalize to lemmas or analyst synonyms.

Multiple VERBs may arise from one sentence when the source presents multiple distinct relation moves.

## 10. LOCATOR — source-native orientation/context functions

LOCATOR inventories exact source-native wording that locates, directs, orients, positions, contains, moves, approaches, departs, enters, exits, accompanies, carries, relates source-to-target, marks recurrence/situational placement, or supplies a materially represented figurative/comparison orientation.

A LOCATOR can be one-use, relation-bound, colloquial, or verb-like in surface form. Type by represented orientation function, not part of speech.

Positive capture is not limited to prepositional phrases. A movement/directional expression may be a LOCATOR when it supplies orientation; the same span may also be VERB only if it genuinely performs both functions.

Exclude bare/routine prepositions, possession alone, topic/recipient marking, or deictic grammar whose only job is syntactic attachment.

LOCATOR does not replace a distinct PLACE/TIME coordinate.

## 11. Cross-class typing and legitimate multiplicity

Type by represented source function, never by part of speech or vocabulary shape.

The same exact source span may appear in multiple primitive classes only when the source span genuinely performs multiple represented functions. Do not create cross-class twins from uncertainty or alternate parsing.

No class absorbs another:

- OBJECT does not absorb LABEL;
- LABEL does not absorb VERB;
- PLACE/TIME do not absorb LOCATOR;
- VERB does not absorb participant/referent/site/frame;
- LOCATOR does not replace PLACE/TIME.

When a candidate could belong to two classes, ask what represented function the source actually gives that span. If two distinct functions are genuinely present, retain both; otherwise choose the one source function rather than hedging.

## 12. Literal, contiguity, and posture lock

Every source-derived non-null string must preserve source language character-for-character where the schema requires source text.

Never synonymize, lemmatize, repair spelling/grammar, normalize dialect, expand contractions, translate, polish, diagnose, standardize a category name, change number, or substitute a conventional expression.

Do not concatenate noncontiguous fragments or silently add omitted words. `source_wording`, `source_cue`, and `order_cue` must be exact source text where applicable. Only genuinely unnamed PLACE/TIME may use null `source_wording`.

Questions, uncertainty, hypotheticals, negations, corrections, remembered possibilities, reported material, attributed material, and proposed future actions remain in source posture. Inventorying does not assert truth or realization.

## 13. `qualities_available`

`qualities_available` is mechanical. True means the source supplies material qualities/descriptions associated with that coordinate; false otherwise.

Do not create or split primitives to justify the boolean. `Q` is never a primitive.

## 14. Ordering

Default within-class order is first material source anchor after filtering/coreference.

Tie rules:

- broad/whole setting before dependent/contained setting when introduced together;
- whole before dependent part at the same anchor unless source order stages the part first;
- PERSON follows first material represented participation;
- remembered/reported/hypothetical/future material stays at source position rather than external chronology.

The apparatus owns canonical IDs and deterministic numbering.

## 15. Class-completeness audit

Before compounds, replay the source separately for each class.

For each class ask:

1. Did I positively capture every source-supported instance that actually performs this class function?
2. Did I drop anything merely because it is low-salience, one-use, relation-bound, deictic, unnamed, generic, reported, remembered, prospective, questioned, recurrent, figurative, or present-telling?
3. Did I fuse two source-native class atoms into one larger span?
4. Did I retain a larger span when a smaller contiguous source atom carries the class function?
5. Did I invent a row from analyst paraphrase, grammatical necessity, or alternate parsing rather than source representation?
6. Did I type by surface vocabulary instead of source function?
7. Did I collapse broad/contained or current/remembered/reported/intended/recurrent/future distinctions that the source separately stages?

Correct omissions first. Then apply only the explicit class-local exclusions in this contract.

## 16. Lexical-grain audit

For every LABEL, VERB, and LOCATOR ask:

- Is this exact contiguous span source-native?
- Does every included word belong to this one class function?
- Can a separable argument, neighboring action, characterization, place, time, or locator be removed without losing this primitive's identity?
- Did I incorrectly combine two serial or embedded source moves?
- Did I incorrectly split a modal/negative/particle/aspect unit whose removal would change the represented relation or posture?
- If the span is duplicated across classes, does it genuinely perform both functions?

Use source grain, not analyst elegance.

## 17. Anti-reification and anti-census audit

A complete inventory is not a transcription.

Remove:

- pure grammar with no represented class function;
- analyst paraphrases and inferred categories;
- true aliases/coreference duplicates;
- alternate parses without distinct source function;
- proposition shells without source reification;
- event-as-TIME or spatial-word-as-PLACE mistakes;
- scene-wide or clause-wide fused primitives that should be separate class atoms.

Do **not** remove a valid primitive solely because it appears once, is local to one relation, is generic, is small, or seems unimportant globally.

Never aim for a hidden count.

## 18. Compound construction

Freeze all primitives first.

A compound represents one minimal source-presented binding among two or more frozen primitives that co-participate in a represented relation, characterization, orientation, state, transition, or other source-staged connection.

Create a compound when:

1. at least two frozen primitives are actively bound by the source in one minimal connection;
2. preserving that binding materially improves reconstruction beyond isolated primitive rows;
3. the member set contains only primitives active in that connection; and
4. the compound is not an alternate parse, duplicate/subset alias, pairwise/transitive closure, or scene-wide mega-bundle.

Do not require the connection to pass a separate global `research-level` ceiling after its primitives are valid. At the same time, do not create one compound for every clause or every possible subset of co-occurring primitives.

One clause may yield multiple compounds when it presents multiple distinct bindings. Several clauses may contribute to one compound when they clearly continue the same binding.

VERB/LABEL/LOCATOR participate when active. PLACE/TIME participate when they actually locate or temporally organize the binding.

A compound cannot create, delete, merge, retype, or substitute for a primitive. Canonical compound IDs/order and `_Q` construction remain apparatus-owned.

## 19. Final audit

Before return verify:

- **Positive capture first:** each class was populated from its own represented function before exclusions.
- **Class-local exclusions only:** valid one-use/local material was not deleted for lack of global prominence.
- **Coordinates:** PLACE/TIME represent actual where/when coordinates rather than automatic event wrappers.
- **Referents:** OBJECT preserves source-treated referents without analyst proposition shells.
- **Characterization:** LABEL preserves actual source-applied characterizations without swallowing process relations.
- **Relations:** VERB preserves distinct source-native relation moves at exact lexical grain.
- **Orientation:** LOCATOR preserves actual orientation/path/context functions even when surface form is not prepositional.
- **Typing:** every primitive is typed by represented function.
- **Literal/posture:** wording, dialect, polarity, question, uncertainty, negation, correction, attribution, and source posture remain exact.
- **Identity:** only true same-class aliases/coreference/repetition were merged.
- **Compounds:** minimal source-presented bindings are emitted only from frozen primitives.
- **Candidate only:** no promotion, APA identity, database action, scoring, diagnosis, or substantive psychological interpretation occurred.

## 20. Worker isolation

The worker must not receive or access:

- gold-standard archetype workbooks;
- canonical archetype extracts;
- expected row counts;
- evaluator findings;
- scored predecessor outputs;
- hidden case-specific corrections/examples;
- sealed holdout source/output;
- prior agent-session answers used as targets.

The worker receives only this durable contract, one source case, researcher interest, and the contract-subordinate task/schema envelope admitted by the apparatus.

## 21. Apparatus boundary

The apparatus, not the worker, owns canonical IDs, deterministic numbering, exact-source validation, source-order enforcement, alias merge enforcement, compound-reference validation, `_Q` construction, SQL-ready shaping, retries, persistence, evaluator comparison, and failure handling.

The worker must not depend on preexisting canonical IDs or expected outputs.

## 22. Candidate-only boundary

All output remains Researcher Inventory candidate material.

Never promote to Oval Office, admitted research, or sovereign APA records; mint an APA Blockchain ID; write to APA database/fabric systems; perform protected-thread analysis, psychological interpretation, scoring, executive analysis, or policy determination; or present candidate inventory as established truth.

## 23. Historical integrity

`RI-CONTRACT-V147` remains preserved as the authority that governed its completed attempts. V148 is prospective only.

V147 is `PARTIALLY SUPERSEDED FOR FORWARD CALIBRATION — 2026-09-21` only for:

- the global scaffold-level relation ceiling used to admit or exclude VERB/LABEL/LOCATOR primitives;
- the rule that matrix/support/reporting/cognitive/copular wording should be suppressed merely because another retained relation carries a more global distinction;
- event/interaction-oriented TIME admission that treated bounded occurrences as temporal coordinates without separately asking whether the source staged a when/period/frame coordinate;
- compound admission that inherited the same global relation ceiling.

Retained from V147 without weakening: source-faithfulness, class typing by represented function, unnamed PLACE/TIME capability, source-reification boundary, exact wording/contiguity/posture lock, strict same-class coreference, deterministic apparatus controls, candidate-only storage, immutable archetype gate, worker isolation, failure-history preservation, holdout isolation, clean-room certification, no promotion, no APA IDs, and no database/fabric writes.

No predecessor is deleted or rewritten.

## 24. Holdout boundary

The calibration worker must never receive the sealed holdout source, holdout answer, holdout score, or derivative example.

The sealed holdout may be opened only by the authorized holdout apparatus after the **same finalized contract and saved calibration lineage repeatedly pass both approved archetypes**. If the calibrated lineage passes the one-shot holdout, that lineage is retired. Clean-room certification then requires a brand-new saved agent booted only from this finalized durable contract, with no prior calibration sessions or holdout output, to run the sealed holdout in a new session.

No calibration correction may be made from sealed holdout output.
