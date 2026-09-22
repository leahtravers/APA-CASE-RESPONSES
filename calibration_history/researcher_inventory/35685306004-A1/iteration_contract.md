# APA Researcher Inventory Agent Contract V151

Status: `ACTIVE SUCCESSOR FOR CALIBRATION — NOT CERTIFIED`  
Contract version: `RI-CONTRACT-V151`  
Predecessor: `RI-CONTRACT-V150`  
Effective date: 2026-09-21  
Authority: Leah's standing Researcher Inventory calibration instruction

## 1. Mission

Given one source case and the researcher interest `lightweight researcher inventory only`, return a source-faithful candidate Researcher Inventory that preserves the source's represented settings, frames, actors, referents, characterizations, relations, orientations, and minimal bindings at the source's own grain.

This is a representational inventory. It is not a summary, diagnosis, ontology, topic list, word census, clause parse, or proposition inventory.

The inventory is **class-complete rather than salience-filtered**. A source-presented occurrence does not need to be important, recurrent, independently reusable, contrasted, revisited, or irreducible to other primitives in order to belong. If an occurrence positively performs one of the seven inventory class functions at a complete source-native grain, retain it unless a specific exclusion below applies.

V151 preserves V149's complete-source-atom correction and exact-source lock. It supersedes V150's `promoted-coordinate`, `local-nonredundancy`, and single-primary-role filters because those filters can erase valid source-presented class occurrences merely because another primitive, quality, cue, or compound also helps reconstruct them.

## 2. Controlling V151 principle — source-presented class occurrence plus complete atom

For each candidate ask three questions.

### Test A — positive class function

Does the source itself present this occurrence as at least one of these functions?

- PLACE — a represented setting, position, site, or scene location;
- TIME — a represented period, episode, phase, recurrence, sequence frame, remembered/reported/intended/prospective frame, or present-telling frame;
- PERSON — a stable represented human or social endpoint;
- OBJECT — a source-treated concrete, abstract, deictic, relational, decision-like, proposition-like, or internal referent;
- LABEL — a source-applied characterization, quality, status, identity, classification, evaluation, comparison, manner, intensity, polarity, correction, rejection, question, or named condition;
- VERB — a source-native action, process, state, perception, cognition, report, intention, possession, comparison, movement, waiting, question-bearing, negated, modal, or other relation move;
- LOCATOR — a source-native orientation, path, position, containment, movement-direction, source-to-target relation, relative position, situational context, or figurative/comparison orientation.

If no class function is actually source-presented, exclude it.

### Test B — complete occurrence grain

Is the candidate a complete source-native occurrence for that class rather than a dependent lexical fragment?

For LABEL, VERB, and LOCATOR use the smallest **complete** exact contiguous source span that preserves the represented move. Keep polarity, modality, degree, particle, complement, comparison, path, aspect, or orientation wording when removing it changes the source-presented identity.

Do not emit a bare auxiliary, copula, control word, intensifier, particle, preposition, or deictic when its identity exists only inside a larger complete atom.

### Test C — same-class identity

Is this a distinct occurrence/coordinate in this class after strict same-class coreference and true repetition are reconciled?

Merge only true same-class aliases/coreference/repetition that represent the same coordinate at the same grain. Do not merge merely because two occurrences are semantically similar or participate in the same event.

## 3. No semantic-redundancy exclusion

Do **not** exclude a valid primitive because:

- another primitive already carries related information;
- a compound could reconstruct the same event;
- the occurrence is an argument, modifier, descriptive phrase, subordinate relation, local context, or one-use detail;
- it appears only once;
- it is low-salience or small;
- it is generic or unnamed;
- it is remembered, reported, intended, prospective, hypothetical, questioned, figurative, negated, or part of present telling;
- it is semantically recoverable from surrounding material.

A Researcher Inventory preserves source-presented class roles themselves. Compounds bind primitives; they do not make those primitives redundant.

## 4. Cross-class multiplicity

Class membership is **not globally exclusive**.

The same exact source wording or same occurrence may legitimately appear in more than one primitive class when it independently performs more than one class function. For example, wording can simultaneously characterize something and orient it, or express a movement relation and a directional relation.

Do not force a single `primary role` when doing so would erase another actually source-presented class function.

Cross-class multiplicity is allowed only when each retained class independently passes Tests A through C. Semantic possibility alone is not enough, but simultaneous source function is enough. Each class remains separately evaluated at its own grain.

## 5. Mandatory whole-source construction order

Perform one coherent whole-source pass, then class-by-class recall.

### Pass A — map the represented source

Read the complete source in source order. Track scenes, positions, temporal phases, actors, referents, qualities, relation moves, orientations, recurrences, recollections, reports, intentions, questions, corrections, figurative material, and present-telling material.

### Pass B — broad positive capture in all seven classes

Capture every plausible source-presented class occurrence before exclusion. Prefer recall first. Do not decide that material is unnecessary because another class or compound already covers it.

### Pass C — complete-atom and same-class audit

Apply Tests A through C. Remove unsupported inference, non-source paraphrase, incomplete hosted fragments, and true same-class aliases/coreference duplicates. Do not apply a promotion, salience, irreducibility, or nonredundancy test.

### Pass D — PLACE/TIME structural recall

Replay the source for settings/positions and temporal frames. Restore unnamed coordinates staged by scene, participant position, sequence, recurrence, memory, report, intended period, later explanation, prospective recurrence, or present telling.

### Pass E — PERSON/OBJECT recall

Replay for stable people/social endpoints and source-treated referents, including concrete, abstract, internal, choice-like, decision-like, relation-like, and deictic referents.

### Pass F — LABEL/VERB/LOCATOR recall

Replay the source separately for every characterization, relation move, and orientation/context move at complete source-native grain. Treat overlap across these three classes as permissible when the same wording actually performs multiple functions.

### Pass G — literal/posture audit

Verify every non-null source-derived string is exact contiguous source text and preserves dialect, uncertainty, question, negation, correction, attribution, comparison, hypothetical status, and temporal posture.

### Pass H — freeze primitives, then construct compounds

Only after all seven classes are complete may compounds be built. Compounds reuse frozen primitives only.

## 6. PLACE — represented settings and positions

PLACE inventories distinct physical, institutional, interactional, or source-staged settings and positions.

Retain named places and unnamed settings/positions when the source stages them distinctly, including:

- whole settings and contained positions;
- participant or referent positions;
- remembered/reported/prospective settings;
- later-explanation settings;
- present-telling settings;
- positions whose exact geography is unspecified but whose scene role is distinct.

Do not require a location noun. Do not collapse two source-staged positions merely because they might physically coincide.

Exclude a spatial noun only when the source does not actually use it as a represented setting/position. A spatial referent may instead or additionally qualify as OBJECT or LOCATOR under its own class rule.

For genuinely unnamed PLACE use null `source_wording`, an exact source cue, and neutral mechanical tag/note wording only.

## 7. TIME — represented frames and phases

TIME inventories distinct temporal coordinates, including:

- episodes and phases;
- earlier/later periods;
- action/interaction frames;
- recurrence spans;
- intended or anticipated periods;
- remembered/reported periods;
- broader life or relationship spans;
- future-similar horizons;
- present reflection/telling frames.

A TIME does not require explicit clock/date vocabulary. A source-staged action or interaction can anchor a TIME when the source presents it as a distinct phase or episode.

Do not create a separate TIME for every verbal token. Create TIME coordinates for distinct source-staged phases/frames, including contained frames when each has separate reconstructive identity.

Temporal wording may also qualify as LOCATOR or another class when it independently performs that role.

For genuinely unnamed TIME use null `source_wording`, an exact source cue, and neutral mechanical tag/note wording only.

## 8. PERSON — stable human/social endpoints

PERSON inventories `B` plus every distinct stable human or social actor/group represented by the source after strict coreference.

A PERSON may qualify through acting, speaking, perceiving, being acted upon, possession, accompaniment, benefit, remembered/reported presence, relationship, prospective standing, or a clear possessive/social reference.

Prominent dialogue is not required.

Exclude rhetorical/generic addressees, unstable pronouns without a resolvable endpoint, and true aliases/coreference duplicates.

Order non-speakers by first material represented participation.

## 9. OBJECT — source-treated referents

OBJECT inventories distinct source-treated things, including concrete and abstract referents.

Eligible referents include source-native:

- physical things;
- documents, parts, surfaces, containers, and possessions;
- deictic handles;
- choices and decisions;
- relations treated as things;
- internal objects such as mind/thought/content handles;
- proposition-like or event-like material when the source itself refers to it as a thing;
- figurative objects;
- divorce/loss/work/feelings/situations and other abstractions when source-treated referentially.

Do not require recurrence or later reuse. One source-presented nominal/deictic handle can be enough when it has referential standing.

Exclude analyst-created noun phrases not grounded in source wording or source structure, pure grammatical placeholders, and pronouns that are only aliases of an already retained same-class referent.

A referent may also participate in PLACE, LABEL, or another class when that other class function is independently source-presented.

Use the smallest complete referential atom.

## 10. LABEL — source-applied characterizations and qualities

LABEL inventories source-applied qualitative or classificatory material broadly. Retain complete source-native characterizations, including:

- states and qualities;
- identities and classifications;
- evaluations;
- manners and intensities;
- comparisons and figurative characterizations;
- role labels and epithets;
- source questions about a characterization;
- negated/rejected/corrected candidate labels;
- polarity responses that function as characterization adjudication;
- descriptive phrases that qualify a represented coordinate;
- source-native condition phrases.

A LABEL does not need to be globally important or separately revisited. If the source applies a characterization/quality to a represented coordinate, retain it at complete source-native grain.

`qualities_available` does not replace LABEL inventory. The same source description may make qualities available and also be a LABEL when it independently performs the LABEL function.

Do not emit isolated degree/support words when their characterization identity belongs to a larger complete span.

## 11. VERB — source-native relation moves

VERB inventories every distinct complete source-presented action, process, state, perception, cognition, report, intention, possession, comparison, movement, waiting relation, question-bearing relation, negated relation, modal relation, or other predicate/relation move.

A VERB does not need to be narratively central, nonredundant, or independently reusable. If the source presents a complete relation move, preserve it.

Use the smallest complete exact contiguous span that preserves one relation identity. As needed retain:

- particle;
- complement/control wording;
- polarity/negation;
- modality;
- aspect;
- directional wording that is integral to the verb identity.

Split genuinely distinct coordinated or serial relation moves when each independently performs a VERB function. Do not split a single multiword relation into bare hosted fragments.

Do not drop a relation merely because its participant, object, label, locator, or compound also represents related information.

A source occurrence may be both VERB and LOCATOR when the movement/relation wording independently performs both functions.

## 12. LOCATOR — source-native orientation and context moves

LOCATOR inventories complete source-native wording that locates, directs, orients, positions, contains, moves toward/away/from/through/into/out of/over/up/down, accompanies/carries, relates source-to-target, situates a represented coordinate, or creates a figurative/comparison orientation.

Retain complete orientation/context moves even when:

- they are local or one-use;
- they overlap a VERB;
- they overlap a LABEL;
- they use temporal/contextual wording;
- they are figurative;
- the related PLACE/TIME is also separately retained.

Do not turn every preposition into a LOCATOR. The retained span must itself express a complete represented orientation/context relation. Do not emit bare syntax-only prepositions or particles when the complete locator is larger.

LOCATOR does not replace PLACE or TIME and PLACE/TIME do not replace LOCATOR.

## 13. Literal, contiguity, and posture lock

Every source-derived non-null string must preserve source language character-for-character where the schema requires source text.

Never synonymize, lemmatize, repair spelling/grammar, normalize dialect, expand contractions, translate, polish, diagnose, standardize a category name, change number, or substitute a conventional expression.

Never add a word not present in the exact contiguous source span. Never concatenate noncontiguous fragments. `source_wording`, `source_cue`, and `order_cue` must be exact source text where applicable. Only genuinely unnamed PLACE/TIME may use null `source_wording`.

If validation rejects a source string, choose an exact contiguous source span or an allowed unnamed structural coordinate. Never invent a near-source repair.

Questions, uncertainty, hypotheticals, negations, corrections, remembered possibilities, reported material, attribution, and proposed future actions remain in source posture. Inventorying does not assert truth or realization.

## 14. `qualities_available`

`qualities_available` is mechanical. True means the source supplies material qualities/descriptions associated with that coordinate; false otherwise.

It is not a semantic exclusion channel. A description can both make qualities available and independently qualify as LABEL.

`Q` is never a primitive.

## 15. Ordering

Default within-class order is first material source anchor after same-class coreference/repetition reconciliation.

Tie rules:

- broad/whole setting before dependent/contained setting when introduced together;
- whole before dependent part at the same anchor unless source order stages the part first;
- PERSON follows first material represented participation;
- remembered/reported/hypothetical/future material stays at source position rather than external chronology.

The apparatus owns canonical IDs and deterministic numbering.

## 16. Class-completeness audit

Before compounds, replay the complete source separately for each class.

Ask:

1. Did I retain every distinct source-presented class occurrence at complete grain?
2. Did I incorrectly remove something because another primitive or compound covers related information?
3. Did I force one class to absorb another when the same occurrence legitimately performs multiple class functions?
4. Did I miss unnamed structural PLACE/TIME coordinates?
5. Did I miss one-use, local, low-salience, reported, remembered, prospective, questioned, negated, or figurative material?
6. Did I preserve all source-applied characterizations rather than using `qualities_available` as a substitute?
7. Did I preserve complete relation moves rather than only salient predicates?
8. Did I preserve complete orientation/context moves rather than only named locations?
9. Did I accidentally emit hosted lexical fragments, true same-class aliases, or unsupported paraphrases?

Do not aim for a hidden count. Aim for complete class-role coverage under the source.

## 17. Complete-atom audit

For every LABEL, VERB, and LOCATOR ask:

- Is the span exact and contiguous?
- Does it preserve one complete class occurrence?
- Is any omitted adjacent wording necessary to preserve identity, polarity, degree, modality, comparison, path, complement, or orientation?
- Is it only a dependent intensifier, auxiliary, copula, support word, control word, particle, preposition, or deictic whose identity belongs to a larger atom?
- Did I split one complete occurrence into dependent fragments?
- Did I fuse distinct coordinated/serial occurrences that should be separate?

Prefer the smallest complete atom, not the shortest fragment.

## 18. Compound construction

Freeze all primitives first.

A compound represents one minimal source-presented binding among two or more frozen primitives that actively co-participate in one source-staged connection.

Create a compound when:

1. at least two frozen primitives are actively bound by the source;
2. preserving that binding adds reconstructive relational information beyond listing the primitives alone;
3. the member set contains only primitives active in that connection; and
4. the result is not a duplicate, transitive closure, arbitrary subset, or scene-wide mega-bundle.

Compounds should follow source-presented relational groupings, not clause count. One clause may yield zero, one, or several compounds; several clauses may continue one binding.

VERB/LABEL/LOCATOR participate when active. PLACE/TIME participate when they locate or temporally organize the binding.

A compound cannot create, delete, merge, split, retype, justify, or substitute for primitives.

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
