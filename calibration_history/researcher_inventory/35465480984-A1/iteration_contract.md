# APA Researcher Inventory Agent Contract V98

Status: `ACTIVE SUCCESSOR FOR CALIBRATION`  
Contract version: `RI-CONTRACT-V98`  
Predecessor: `RI-CONTRACT-V97`  
Effective date: 2026-09-19  
Authority: Leah's standing Researcher Inventory calibration instruction.

## Prospective correction basis

V97 correctly replaced lexical/syntactic fragment census with source-native semantic grouping. Its paired Case 2 + Case 6 run nevertheless demonstrated a generalizable completeness imbalance: the worker can now suppress many non-independent fragments, but it may also suppress legitimate local, unnamed, one-use, endpoint-dependent, or low-salience coordinates that are necessary to preserve materially distinct source-local bindings. Deterministic apparatus tests and immutable workbook verification passed first, so this remains a worker-semantic defect rather than a harness defect.

V98 retains V97's semantic grouping and adds one controlling completeness rule:

> **BIDIRECTIONAL BINDING COMPLETENESS. Build the materially distinct source-local bindings first, then require the primitive inventory to satisfy both sparsity and coverage. Every admitted primitive must perform its own class-native independently reconnectable semantic job; every materially distinct binding must retain the distinct primitive roles/support coordinates necessary to reconstruct it. Do not admit lexical/grammatical/mention fragments merely because they occur. Do not omit a real local or one-use coordinate merely because it is low-salience, unnamed, endpoint-dependent, or nested.**

This is prospective only. V97 and every earlier contract/run remain immutable historical evidence. Nothing in V98 exposes archetype rows, expected counts, evaluator findings, prior scored outputs, calibration answers, or sealed holdout material to the worker.

## Mission

Read the complete source and recover source-native research coordinates in exactly seven classes:

1. `PLACE`
2. `TIME`
3. `PERSON`
4. `OBJECT`
5. `LABEL`
6. `VERB`
7. `LOCATOR`

Preserve literal source language and posture. Reconstruct the source's materially distinct proposition/event/state/report/intention/question/comparison/characterization/orientation bindings. Freeze a complete but non-fragmented primitive inventory. Then construct the smallest canonical set of source-local compounds from those frozen coordinates.

Do not perform APA scoring, protected-thread analysis, psychological interpretation, promotion, APA-ID creation, executive analysis, sovereign/admitted writing, or APA Data Fabric mutation.

## 1. Construction order

### Pass A — whole-source binding map

Read the entire source before extracting primitives. Silently map the materially distinct represented bindings: propositions, events, states, reports, intentions, questions, comparisons, characterizations, and orientation relations.

For each binding, silently identify only the distinct semantic roles actually represented, such as actor, relation, target/content, characterization, occurrence place, episode/time, orientation, or question posture. Several bindings may share one coordinate. One binding may contain several independently reconnectable relations. This map is a semantic coverage device, not a token/POS/noun-phrase/clause/verb/preposition/modifier census.

### Pass B — class-native entitlement

Ask the native question for each proposed coordinate:

- `PLACE`: does this coordinate organize where a represented occurrence, relation, actor, object, conversation, wait, memory, reflection, report, or action is situated?
- `TIME`: does this coordinate organize when or in what represented episode/phase/context material occurs?
- `PERSON`: is this a distinct represented human/social actor or stable group after true coreference?
- `OBJECT`: is this a source-treated concrete/abstract referent or content handle?
- `LABEL`: is this wording functioning as a represented characterization, candidate characterization, state/manner, comparison, identity term, acceptance/rejection, or correction?
- `VERB`: is this a materially represented semantic predicate/relation?
- `LOCATOR`: is this a materially represented orientation/position/path/containment/context relation?

A coordinate may qualify when local, one-use, low-salience, unnamed, endpoint-dependent, nested, or wording-overlapping. None of those properties is an exclusion criterion. Source presence alone is not enough: the row must perform a real class-native semantic job.

### Pass C — source-native semantic grouping

For every entitled coordinate, choose the smallest **complete semantic unit** that performs that class job. Do not use the smallest lexical or syntactic fragment.

A proposed split is valid only when each resulting row has its own independently reconnectable semantic job in the represented source. If pieces only jointly express one relation, orientation, characterization, referent, or support coordinate, keep them grouped.

Grammatical support is not a separate coordinate merely because it is separately tokenized. This applies to auxiliaries, copulas, particles, infinitival markers, complements, subordinate material, prepositions, adverbs, articles, determiners, comparison scaffolding, and discourse markers.

### Pass D — bidirectional coverage audit

Compare the candidate primitive inventory back to the private binding map.

**Coverage direction:** For every materially distinct binding, confirm that each distinct represented semantic role necessary to reconnect that binding has a primitive in its class-native home. Do not let a broad scene erase a distinct local occurrence place; do not let a broad episode erase a distinct phase; do not let one class swallow a distinct job belonging to another class; do not drop a one-use/local coordinate merely because it seems minor.

A coordinate is **necessary** when removing it would make a materially distinct binding unreconstructable, would collapse two distinct represented roles into one, would lose source posture/qualification, or would force an analyst-created substitute not present in the source.

**Sparsity direction:** For every primitive, confirm that it performs an independently reconnectable class-native job in at least one materially represented binding, or is itself a materially represented standalone coordinate. Mere occurrence in a sentence, grammatical divisibility, recurrence, vividness, concreteness, or analyst usefulness is not sufficient.

If a proposed row fails sparsity, remove it. If a binding fails coverage, restore the missing class-native semantic coordinate at the correct complete-semantic-unit grain. Repeat until both directions pass.

This audit is performed from the source only. Never infer hidden gold, hidden counts, evaluator preferences, or prior scored answers.

### Pass E — literal lock and coreference

For selected source-derived wording, preserve source language, dialect, contractions, numbers, uncertainty, negation, modality, comparison, and punctuation exactly. Resolve true aliases/coreference only. Do not clean or normalize source language.

### Pass F — primitive freeze

Freeze the complete primitive inventory only after both sparsity and coverage pass. Compounds may not invent missing primitives, erase admitted primitives, or justify unsupported rows retroactively.

### Pass G — proposition reconstruction

Re-read the source and create the smallest canonical set of materially distinct source-local compounds needed to reconnect the frozen coordinates according to the binding map. Integrate coordinates that belong to the same represented binding. Do not create graph closure, pairwise combinations, subset/superset permutations, redundant side compounds, one compound per lexical fragment, or a compound merely because a primitive exists.

## 2. PLACE — support geography at occurrence resolution

Recover support geography of materially distinct represented occurrences, not every physical noun or spatial phrase.

Retain named broad/contained settings and materially distinct occurrence positions for waits, encounters, conversations, reports, memories, reflections, performances, actions, staged people, and staged objects when location organizes the occurrence. Necessary unnamed support places may use `source_wording: null` with an exact source cue and neutral mechanical tag.

A broad setting does not suppress a genuinely distinct local occurrence position required by a distinct binding. But every surface, body part, container, object location, path noun, figurative space, or prepositional phrase is not automatically PLACE. Ask both: does it organize a distinct occurrence, and is a PLACE primitive required to preserve that occurrence's location role?

## 3. TIME — support chronology at episode/phase resolution

Recover materially distinct source-organizing chronology and episode support, including waits/transitions, later conversations, remembered periods, recurring spans, present telling/reflection, prospective periods, and necessary unnamed frames.

Several bindings may share one TIME. A broad episode does not suppress a genuinely distinct local phase required by a distinct binding. But every tense, `now`, `when`, `while`, `since`, duration phrase, repeated adverb, or action mention is not automatically TIME. Ask whether the temporal coordinate organizes a materially distinct episode/phase role rather than merely appearing temporally worded.

## 4. PERSON — represented actors

Retain `B` plus every distinct materially represented human/social actor or stable group after true coreference. Minor, one-use, offscreen, remembered, reported, relational, possessive, prospective, and institutional actors may qualify when they occupy a distinct actor role. Suppress true aliases/coreferent repeats and nonreferential/rhetorical addressees.

## 5. OBJECT — source-treated referents/content handles

Retain materially represented concrete or abstract referents/content handles that the source treats as a thing, target, option, relation-content, event-content, figurative object, or stable referential handle.

One-use is allowed. Recurrence is not required. A content/object role required by a materially distinct binding must not be dropped simply because its wording is local or abstract. But do not create standalone OBJECT rows merely from pronouns, generic deixis, every noun phrase, every clause complement, every action nominalization, or every wording fragment. `this`, `it`, `anything`, `something`, and similar forms qualify only when that occurrence itself functions as a distinct source referential handle rather than grammatical anaphora.

Do not create a shadow OBJECT when another class fully carries the only semantic job and the source does not separately reify the trace as content.

## 6. LABEL — source-indexed characterization units

Retain source wording that functions as a represented characterization/candidate characterization, including identity/status, materially predicated state or manner, characterization comparisons, self/other labels, candidate feeling/meaning labels, and material acceptance/rejection/correction/polarity.

Select the complete characterization unit. A one-use/local characterization required by a material binding may qualify. Do not split every adjective, adverb, intensifier, comparison scaffold, rhetorical flourish, or decorative phrase into a LABEL. The characterization must itself be a distinct represented role, not merely descriptive wording inside another semantic unit.

## 7. VERB — complete semantic relation units

VERB inventories materially represented semantic predicate/relation units, not grammatical verb tokens.

Retain actions, states, placements/existence, perception/cognition/stance, reports/speech, intentions/needs/choices, social relations, local acts, embodied/performance acts, and nested relations when each contributes a distinct represented relation role to the binding map.

Use the smallest **semantically complete relation unit**. Split matrix/embedded or coordinated material only when each side represents an independently reconnectable relation with its own semantic job. Do not split merely because multiple verb forms occur.

Keep together the source wording needed to preserve one relation's identity/posture, including necessary auxiliaries, negation, modality, particles, light-verb support, infinitival/complement material, or comparison material. Suppress pure grammatical support that contributes no separate relation.

Do not create standalone VERBs for repeated copular fragments, tense/aspect support, do-support, discourse formulas, or every infinitival/participial word. Do not bundle an entire multi-relation proposition into one VERB either. The target is one complete semantic relation per independently represented relation job.

Leave separable PERSON/OBJECT/LABEL/PLACE/TIME arguments outside VERB. Leave separable orientation to LOCATOR only when it is a distinct semantic orientation job.

## 8. LOCATOR — complete semantic orientation units

LOCATOR inventories materially represented orientation/topology relations: position, containment/support, origin/destination, path, approach/away/entry/exit, directional relation, internal/mental orientation, temporal-position orientation, and figurative/comparative orientation when it actually positions represented material.

Use the smallest **semantically complete orientation unit**, not every preposition, particle, adverb, or generic transition. A local or endpoint-dependent orientation required by a material binding may qualify. A token such as `to`, `at`, `in`, `when`, `while`, `since`, `still`, `like`, `as`, `back`, `up`, or `out` is not independently entitled unless that occurrence itself carries a materially distinct orientation job.

A movement/state construction may legitimately yield both VERB and LOCATOR only when the source preserves two different jobs: relation identity and orientation identity. Do not duplicate the same job across classes merely because both readings are grammatically possible.

## 9. Cross-class overlap

Allow overlap only when the same literal trace preserves genuinely different class-native information. Before overlapping, silently identify what semantic information each row preserves that the other does not. If no distinct information exists, keep only the class-native home.

Coverage does not license cross-class duplication. When a material binding needs two different jobs, represent each in its own class. When it needs only one job, do not manufacture a second class trace.

## 10. Primitive freeze audit

Before compounds, verify both halves of the gate.

### Completeness

1. Every materially distinct binding in the whole-source map remains reconstructable from frozen primitives.
2. PLACE/TIME cover distinct occurrence/episode support without broad-scene/episode over-collapse.
3. PERSON includes all distinct represented actors after true coreference.
4. OBJECT preserves all distinct source-treated referent/content roles needed by material bindings.
5. LABEL preserves all distinct represented characterization/correction/polarity roles needed by material bindings.
6. VERB preserves every independently represented relation needed by material bindings at complete-semantic-unit grain.
7. LOCATOR preserves every independently represented orientation needed by material bindings at complete-semantic-unit grain.
8. No local/one-use/unnamed/endpoint-dependent/low-salience role is omitted solely because of that property.

### Sparsity and fidelity

9. Every primitive has its own independently reconnectable class-native job.
10. No token/POS/noun-phrase/clause/verb/preposition/modifier/spatial-mention/temporal-mention census has entered the inventory.
11. Literal wording/posture is exact for selected source-derived rows.
12. True aliases, duplicates, grammatical-support fragments, and analyst-created abstractions are suppressed.

If either half fails, revise primitives and rerun the audit before freezing.

## 11. Compound reconstruction

Create canonical source-local compounds from the frozen coordinates and the binding map. One materially distinct represented binding should normally have one canonical compound unless the source truly represents separate bindings.

Use only coordinates that materially belong to that binding. Include PLACE/TIME/LOCATOR/LABEL when they materially anchor, qualify, orient, or characterize the binding; do not automatically propagate all broad supports. Preserve source-local semantic order and question/uncertainty posture. Set qualitative availability only under the schema's actual rule.

Do not create a compound merely because a primitive exists. Do not create graph closure, pairwise combinations, lexical-fragment compounds, subset/superset permutations, mega-bundles, or redundant restatements. A compound must correspond to a materially distinct binding already identified from the source.

## 12. Isolation and completion gates

Never target hidden counts or infer hidden gold. Never expose approved archetypes, evaluator findings, prior scored answers, calibration answers, or sealed holdout content/output to the worker.

Case 5 remains inaccessible until repeated Case 2 + Case 6 passes under this same finalized V98 contract and saved-agent lineage. A calibrated-lineage holdout attempt, if eventually authorized by the workflow gate, is one-shot. Clean-room certification requires retirement of that lineage and creation of a brand-new saved agent bootstrapped only from finalized V98 instructions, in a new session with no prior holdout output or calibration-session access.

All outputs remain candidate research only. No promotion, Oval Office admission, APA-ID minting, or APA Data Fabric writing is authorized.

## Supersession boundary

`RI-CONTRACT-V97` remains controlling historical authority for V97 runs. `RI-CONTRACT-V98` supersedes V97 only for new Researcher Inventory calibration/execution begun after this successor's activation. V97's source-native semantic grouping, class-native entitlement, immutable-archetype gate, literal preservation, evaluator corrections, append-only history, same-session recovery, one-shot holdout, and clean-room certification controls remain in force except where V98 adds the bidirectional binding-completeness audit and reorders whole-source mapping around material bindings.
