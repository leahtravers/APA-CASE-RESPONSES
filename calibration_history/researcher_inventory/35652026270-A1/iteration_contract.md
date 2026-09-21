# APA Researcher Inventory Agent Contract V146

Status: `ACTIVE SUCCESSOR FOR CALIBRATION — NOT CERTIFIED`  
Contract version: `RI-CONTRACT-V146`  
Predecessor: `RI-CONTRACT-V145`  
Effective date: 2026-09-21  
Authority: Leah's standing Researcher Inventory calibration instruction

## 1. Mission

Given one source case and the researcher interest `lightweight researcher inventory only`, return a source-faithful candidate Researcher Inventory that preserves the distinct represented coordinates and relations needed to reconstruct what the source actually presents.

This is a representational inventory, not a word census, clause parse, summary, diagnosis, interpretation, or ontology-building exercise.

The target lies between two failures:

- **too sparse:** conceptually summarizing the case and dropping low-salience, unnamed, deictic, questioned, reported, prospective, or one-use distinctions that the source actually presents;
- **too dense:** inventorying every noun phrase, predicate token, modifier, preposition, temporal phrase, discourse scaffold, or proposition merely because it can be classified.

V146 changes the construction order. Do **not** decide primitive membership first and then try to rebuild relations afterward. Resolve bounded source-native research relations first, then derive the primitive slots that those relations require.

## 2. Controlling V146 principle — relation first, slots second

A primitive is eligible because it performs a represented **functional slot** in a retained source relation/frame, or because it is a stable source-established coordinate/referent that remains available across relations.

A primitive does **not** need to be independently meaningful outside its relation.

The decisive question is:

> If this source-native slot were removed, would reconstruction erase a distinction the source explicitly presents about who/what, where, when, characterization, relation, or orientation?

If yes, retain the smallest faithful primitive that performs that slot. If removal would lose only grammar, prose fluency, an analyst paraphrase, or redundant local wording, do not retain it.

This relation-slot rule supersedes V145's stronger `independent research handle` prerequisite for primitive admission.

## 3. Mandatory construction order

Perform the work in this order for the whole source regardless of which class the apparatus requests first.

### Pass A — resolve represented frames

Identify the bounded represented frames in which source material is staged. Frames may be current, past, remembered, reported, recurrent, hypothetical, questioned, prospective, figurative, or present-telling/performance frames.

A frame is not every clause. Retain a frame when it materially groups, separates, nests, transitions, or contextualizes represented material.

### Pass B — build a source-native relation ledger

Within and across those frames, identify the bounded relations the source actually stages. A relation may be an action, state, transition, perception, cognition, report, intention, possession, comparison, characterization, orientation, movement, waiting relation, question, negated relation, correction, or other source-presented connection.

Do not create one ledger item per token or automatically one per clause. A single relation may span a short multiword kernel; coordinated or embedded wording may contain more than one relation only when the source presents distinguishable relation roles.

Do not paraphrase relation identity. Preserve source posture, including uncertainty, negation, quotation posture, question, hypothetical status, correction, attribution, and colloquial form.

### Pass C — derive functional primitive slots

For each retained relation, resolve the source-presented slots that materially distinguish it:

- PERSON participants/social endpoints;
- OBJECT referents/content things that the source itself treats as objects of tracking;
- PLACE where-coordinates;
- TIME when/frame-coordinates;
- LABEL characterization slots;
- VERB relation kernels;
- LOCATOR orientation/context slots.

Retain a slot when removing it would collapse a source-presented representational difference in the relation or frame.

A one-use slot may be valid. A brief/generic/deictic slot may be valid. An unnamed PLACE/TIME slot may be valid. None is invalid merely because it is not useful outside its host relation.

### Pass D — reconcile identity and duplicates

Merge only true same-class coreference/aliases/repetitions of the same represented coordinate. Preserve distinct grain when broad/contained, earlier/later, remembered/current, source/reported, or other represented distinctions are materially different.

### Pass E — freeze primitives, then emit compounds from the same ledger

After the primitive inventory is frozen, emit only the minimal multi-primitive research relations from the ledger that are useful to reconstruct represented structure. A compound reuses frozen primitives; it never creates or repairs them.

Do not use compounds to compensate for missing primitive slots.

## 4. Research-bearing relation test

A relation is research-bearing when the source stages a representational difference worth preserving rather than merely supplying grammar.

Positive signals include one or more of:

- it establishes or changes a participant, referent, place, time, state, characterization, relation, or orientation;
- it connects already represented coordinates in a distinct way;
- it stages an explicit perception, cognition, report, intention, question, negation, correction, comparison, evaluation, or prospective relation;
- it establishes a transition or boundary between frames;
- it supplies source-native wording necessary to preserve the relation's identity or posture;
- later source material refers back to, contrasts with, qualifies, repeats, or depends upon it;
- it is a stage/performance action the source explicitly includes as represented material.

Negative signals:

- purely grammatical support with no representational difference;
- discourse filler or connective wording whose removal changes fluency but not represented structure;
- analyst-created proposition shells;
- alternate parses of an already retained relation;
- redundant re-expression that adds no new source-presented distinction;
- classification driven only by part of speech.

When uncertain, prefer the smallest source-supported relation that preserves the presented distinction without inventing a broader semantic object.

## 5. PLACE — represented where-coordinates

PLACE inventories distinct physical/institutional settings and represented positions required by retained frames/relations.

Retain PLACE when a research-bearing relation requires a distinct where-coordinate to reconstruct where a participant, referent, action, report, remembered interaction, prospective action, or present telling is staged.

Rules:

- Physical naming is not required.
- A source cue may establish an unnamed position.
- Broad and contained sites may both survive when each performs a distinct relation/frame role.
- A reported, remembered, prospective, or present-telling relation may require its own unnamed position when the source distinguishes that occurrence from another setting.
- Do not create PLACE from every surface, container, body part, direction, distance expression, or movement phrase when no distinct where-coordinate is required.
- Do not create PLACE merely because every event must happen somewhere.

For unnamed PLACE use null `source_wording`, an exact source cue, and a neutral mechanical tag/note. Never invent geographic or physical specificity.

## 6. TIME — represented frame/when-coordinates

TIME inventories distinct episodes, periods, phases, attempts, waits, interactions, transitions, recurrence spans, remembered/reported/prospective frames, and present telling/reflection frames required by retained relations.

Retain TIME when it groups, separates, nests, orders, or contextualizes represented relations as a distinct source-presented frame.

Rules:

- No date, clock, duration, tense marker, or temporal word is required.
- A short occurrence may be a TIME coordinate when it organizes a relation as an episode or phase.
- Broad and contained times may both survive when they organize different source material.
- Explicit temporal wording is not automatically TIME.
- Do not convert every action, adverb, tense/aspect shift, discourse transition, or recurrence word into TIME.

For unnamed TIME use null `source_wording`, an exact source cue, and neutral mechanical wording.

## 7. PERSON — represented actors/social endpoints

PERSON inventories `B` plus each distinct stable human/social actor or group after strict coreference when that actor/group occupies a material role in at least one retained relation.

Participation may include acting, speaking, perceiving, being acted upon, possessing, receiving, benefiting, accompanying, being remembered/reported, or serving as another stable relation endpoint. Action or speech is not required.

Exclude rhetorical/generic addressees, hypothetical placeholders with no stable represented referent, unstable pronouns without a resolvable endpoint, and true aliases/coreference duplicates.

Order non-speakers by first material represented participation rather than incidental mention alone.

## 8. OBJECT — source-treated referents, not proposition shells

OBJECT inventories source-established concrete or abstract things that the source treats as referents in retained relations.

An OBJECT may be physical, documentary, quantitative, relational, situational, decisional, mental-content, comparative, or otherwise abstract when the source itself gives it referential standing.

Positive evidence includes source treatment such as handling, possessing, selecting, positioning, comparing, evaluating, revisiting, deciding about, questioning as a thing, pointing back to, or using a nominal/deictic handle that remains a referent.

Reject:

- a proposition or clause merely because it has semantic content;
- analyst-created noun-like summaries of a relation;
- `what someone meant/wanted/said/did` shells unless the source itself reifies that content as a referent;
- an argument phrase whose identity is exhausted by one host relation and has no source-established object standing;
- a setting duplicated as OBJECT when its only retained function is PLACE;
- unstable pronouns/demonstratives that resolve entirely to another retained coordinate.

A source relation may have both a VERB and an OBJECT only when the source actually distinguishes the relation from a referent involved in or derived from it. Do not manufacture an OBJECT just to give a relation something to point to.

Use the smallest source-native referential atom.

## 9. LABEL — source-applied characterization slots

LABEL inventories source-applied states, qualities, statuses, identities, classifications, evaluations, comparisons, manners, polarities, corrections, rejections, intensifications, and characterization questions when they materially characterize a retained coordinate or relation.

A LABEL does not need to be independently reusable outside its relation. It must, however, preserve a source-presented characterization distinction that would otherwise disappear from reconstruction.

Preserve uncertainty, question, negation, rejection, correction, contrast, attribution, colloquial wording, and material intensity.

Do not inventory every adjective/adverb/modifier. Exclude purely local stylistic modification whose removal does not erase a represented characterization difference.

## 10. VERB — source-native relation kernels

VERB inventories the smallest exact contiguous source-native lexical kernel that expresses a research-bearing relation in the ledger.

A VERB is not required to be independently meaningful outside the relation packet.

Rules:

- retain short, generic, copular, reporting, cognitive, support, control, negative, or colloquial wording when that exact wording is the relation kernel necessary to preserve what the source stages;
- include auxiliary/support material inside the same contiguous kernel when removing it would change polarity, modality, aspect, relation identity, or posture;
- do not split one source-native relation into token-level verb rows merely because several verbal tokens occur;
- split matrix/embedded or coordinated wording only when the source presents distinguishable represented relation roles;
- do not inventory grammar-only auxiliaries or infinitival markers as separate relations;
- do not normalize a relation to a lemma or analyst synonym.

Use the smallest exact contiguous kernel that preserves the relation's represented identity.

## 11. LOCATOR — source-native orientation/context slots

LOCATOR inventories exact source-native wording that materially orients a retained participant, referent, relation, place, or time.

Eligible functions include relative position, containment, direction, path, origin/destination, entry/exit, approach/departure, proximity/distance, accompaniment/carrying, recurrence/situational context, embodied/internal orientation, source/target orientation, and materially organizing figurative/comparison orientation.

A LOCATOR does not need to be independently useful outside its host relation. Retain it when it performs a distinct orientation role whose removal would erase source-presented structure.

Reject bare/routine prepositions, recipient/topic marking, possession alone, and local wrappers that add no distinct orientation beyond the relation they grammatically support.

A locator may overlap wording with PLACE/TIME/LABEL/VERB only when the same exact span performs a genuinely different represented function.

## 12. Cross-class multiplicity and non-substitution

Type by represented function, not part of speech.

The same exact source span may lawfully appear in multiple primitive classes when it performs genuinely different functional slots. Do not suppress one function merely because another class already uses the words.

Do not create cross-class twins merely because multiple grammatical analyses are possible.

No class absorbs another function:

- OBJECT does not absorb LABEL;
- LABEL does not absorb VERB;
- PLACE/TIME do not absorb LOCATOR;
- VERB does not absorb actor/object/site/frame;
- LOCATOR does not replace PLACE/TIME.

## 13. Literal, contiguity, and posture lock

Every source-derived non-null string must preserve source language character-for-character wherever the schema requires source text.

Never synonymize, lemmatize, repair spelling/grammar, normalize dialect, expand contractions, translate, polish, diagnose, standardize a group/category name, change number, or substitute a conventional expression.

Do not concatenate noncontiguous fragments. Do not silently add omitted words. Do not broaden a fragment merely so it reads well outside context.

`source_wording`, `source_cue`, and `order_cue` must be exact source text where applicable. Only genuinely unnamed PLACE/TIME may use null `source_wording`.

Questions, uncertainty, hypotheticals, negations, self-corrections, remembered possibilities, reported material, and proposed future actions remain in source posture. Inventorying does not assert truth or realization.

## 14. `qualities_available`

`qualities_available` is mechanical. True means the source supplies material qualities/descriptions associated with that coordinate; false otherwise.

Do not create or split primitives to justify the boolean. `Q` is never a primitive.

## 15. Ordering

Default within-class order is first material source anchor after filtering/coreference.

Tie rules:

- broad/whole setting before dependent/contained setting when introduced together;
- whole before dependent part at the same anchor unless source order stages the part first;
- PERSON follows first material represented participation;
- remembered/reported/hypothetical/future frames remain at source position rather than external chronology.

The apparatus owns canonical IDs and deterministic numbering.

## 16. Relation-completeness audit

After initial selection, replay every retained relation and frame.

For each relation ask:

1. Who/what participates or is the stable endpoint?
2. What source-treated referent is actually involved, if any?
3. Is a distinct where-coordinate required by the source staging?
4. Is a distinct when/frame-coordinate required?
5. What exact source-native relation kernel preserves the connection?
6. What source-applied characterization would be lost if omitted?
7. What orientation/context wording would be lost if omitted?
8. Does any low-salience, unnamed, deictic, questioned, reported, remembered, prospective, figurative, one-use, or present-telling slot disappear merely because it lacks independent prominence?

Restore a missing slot only when it is required to preserve a source-presented distinction in a retained relation/frame. Do not use this audit to harvest all class-shaped wording.

## 17. Anti-census / anti-reification audit

For every primitive ask:

1. Which retained relation/frame licenses this slot?
2. What represented distinction disappears if it is removed?
3. Is its identity source-established rather than analyst-completed?
4. Is it the smallest exact source-native atom that performs this function?
5. Did grammar, part of speech, lexical vividness, or proposition parsing create it instead of the relation ledger?
6. For OBJECT, did I turn a clause/proposition/relation into a noun-like thing without source reification?
7. For VERB, did I split one relation into grammatical fragments?
8. For PLACE/TIME, did I invent a coordinate merely because events require location/time?
9. For LABEL/LOCATOR, is the distinction represented or merely decorative/routine grammar?
10. Is it truly distinct from same-class coreference/repetition?

Remove the primitive when no source-grounded relation/frame and no preserved representational difference supports it.

Never aim for a hidden count.

## 18. Compound construction — relation-ledger replay

Freeze the primitive inventory before compound emission.

A compound represents one minimal source-staged multi-primitive relation from the same relation ledger used to derive primitives.

Create a compound when:

1. the source stages a distinct relation/characterization/position/frame connection among two or more frozen primitives;
2. preserving that connection materially improves reconstruction beyond the isolated primitives;
3. the compound includes the active primitive slots in that minimal relation and excludes inactive neighbors; and
4. it is not an alternate parse, pairwise/transitive closure, duplicate/subset alias, automatic one-compound-per-token artifact, automatic one-compound-per-clause artifact, or scene-wide mega-bundle.

Not every primitive-bearing relation must become a compound. A primitive can be retained because it preserves a source-presented slot even when the relation is too local, redundant, or single-coordinate to warrant a separate compound.

Several clauses may contribute to one compound when they realize one retained relation. One clause may contain more than one compound when it stages multiple distinguishable research relations.

VERB, LABEL, and LOCATOR participate when active in the represented relation. PLACE/TIME participate when they actually locate or organize it.

A compound cannot create, delete, merge, retype, or substitute for a primitive.

Canonical compound IDs/order and `_Q` construction remain apparatus-owned.

## 19. Final contrast audit

### Too dense / census failure

Warning signs:

- every noun phrase becomes OBJECT;
- every predicate token becomes VERB;
- support/auxiliary material splits into separate rows;
- every modifier becomes LABEL;
- every temporal/spatial phrase becomes TIME/PLACE/LOCATOR;
- clauses are reified into OBJECTs;
- local argument marking is inventoried;
- compounds track nearly every clause.

Correct by returning to the relation ledger and representational-difference test.

### Too sparse / abstraction failure

Warning signs:

- unnamed site/frame coordinates disappear because no noun names them;
- minor stable actors/endpoints disappear because they do not act or speak;
- source-native relation wording disappears because it looks generic, copular, reporting, brief, or one-use;
- source-applied characterization/orientation disappears because it is not independently reusable;
- broad and contained frames collapse when the source stages both;
- reported/prospective/present-telling material loses its own coordinates;
- several distinct source roles are replaced by one conceptual summary.

Correct by replaying relation completeness under the same representational-difference test.

## 20. Final audit

Before return verify:

- **Relation first:** bounded source-native relations/frames were resolved before final primitive membership.
- **Functional slots:** each primitive preserves a represented slot in a retained relation/frame or a stable cross-relation coordinate.
- **No independence prerequisite:** one-use or relation-bound source slots were not suppressed merely for lacking standalone prominence.
- **No proposition shells:** OBJECT was not used to reify clause meaning without source evidence.
- **Relation kernels:** VERB preserves the smallest contiguous source-native relation identity rather than token fragments or analyst lemmas.
- **Structural recall:** unnamed/low-salience/deictic/reported/prospective/present-telling distinctions were not suppressed.
- **Census ceiling:** no primitive exists merely because wording can be grammatically or semantically classified.
- **Typing:** every primitive is typed by represented function.
- **Cross-class:** different represented functions may share wording; alternate parses do not multiply rows.
- **Literal/posture:** wording, dialect, polarity, question, uncertainty, negation, correction, and attribution are preserved.
- **Compounds:** emitted compounds replay minimal relation-ledger connections using frozen primitives.
- **Candidate only:** no promotion, APA identity, database action, or substantive psychological interpretation occurred.

## 21. Worker isolation

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

An unscored provisional output from another stateless pass may be used only when the governing apparatus explicitly allows it; it is never gold/evaluator feedback.

## 22. Apparatus boundary

The apparatus, not the worker, owns canonical IDs, deterministic numbering, exact-source validation, source-order enforcement, alias merge enforcement, compound-reference validation, `_Q` construction, SQL-ready shaping, retries, persistence, evaluator comparison, and failure handling.

The worker must not depend on preexisting canonical IDs or expected outputs.

## 23. Candidate-only boundary

All output remains Researcher Inventory candidate material.

Never promote to Oval Office, admitted research, or sovereign APA records; mint an APA Blockchain ID; write to APA database/fabric systems; perform protected-thread analysis, psychological interpretation, scoring, executive analysis, or policy determination; or present candidate inventory as established truth.

## 24. Holdout boundary

The calibration worker must never receive the sealed holdout source, holdout answer, holdout score, or derivative example.

The sealed holdout may be opened only by the authorized holdout apparatus after the **same finalized contract and saved calibration lineage repeatedly pass both approved archetypes**. If the calibrated lineage passes the one-shot holdout, that lineage is retired. Clean-room certification then requires a brand-new saved agent booted only from this finalized durable contract, with no prior calibration sessions or holdout output, to run the sealed holdout in a new session.

No calibration correction may be made from sealed holdout output.
