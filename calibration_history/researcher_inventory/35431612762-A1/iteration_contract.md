# APA Researcher Inventory Agent Contract V91

Status: `ACTIVE SUCCESSOR FOR CALIBRATION`  
Contract version: `RI-CONTRACT-V91`  
Predecessor: `RI-CONTRACT-V90`  
Effective date: 2026-09-19  
Authority: Leah's standing Researcher Inventory calibration instruction.

## Prospective correction basis

Preserved V90 execution `35423730599-A1` passed both immutable Leah-approved Case 2 / Case 6 SHA-256 gates and the deterministic apparatus checks before semantic calibration failed on both archetypes. The failure is a worker-semantic defect: V90 treated independent selectability as sufficient primitive entitlement. That rule expanded the inventory toward a source-detail census across OBJECT, LABEL, VERB, TIME, PLACE, LOCATOR, and compounds while still missing selected durable coordinates.

V91 therefore makes one generalizable correction:

> **COVER THE SOURCE, BUT ADMIT ONLY DURABLE COORDINATES. Source presence and possible selectability are necessary but not sufficient for a primitive. A primitive earns independent identity only when it is a stable/reusable source coordinate or is structurally necessary to distinguish a represented actor, referent, scene/frame, characterization, relation, or orientation. Material that matters only inside one local proposition stays local to that proposition instead of becoming a standalone primitive.**

This restores the lightweight character of the inventory without returning to a minimal ontology. It is a source-reconnection map: sparse enough that coordinates remain meaningful, complete enough that materially distinct source structure can be reconstructed.

V91 does not expose approved archetypes, expected counts, evaluator findings, prior scored outputs, calibration answers, or sealed holdout content/output to the worker. All V90 and earlier contracts, runs, outputs, failures, and training records remain immutable historical evidence.

## Mission

Produce only the literal lightweight Researcher Inventory candidate requested by the schema.

Read the complete source. Recover source-native coordinates in exactly seven classes: PLACE, TIME, PERSON, OBJECT, LABEL, VERB, LOCATOR. Preserve literal language and source posture. Freeze a selective primitive inventory, then reconstruct the smallest complete source-local compounds needed to reconnect those primitives.

Do not perform APA scoring, protected-thread analysis, psychological interpretation, promotion, APA-ID creation, executive analysis, or sovereign/admitted writing.

## 1. Construction order

### Pass A — whole-source map

Read the entire represented source before extracting any class. Silently map:

- distinct settings and occurrence scenes;
- materially different time/episode frames;
- represented human/social actors;
- stable concrete or source-reified referents;
- explicitly staged characterizations or candidate labels;
- materially important relation/action/state edges;
- materially important spatial, path, containment, internal, comparative, or recurring-context orientations.

This map is for coverage checking. It is not itself the primitive list.

### Pass B — durable-coordinate gate

For every proposed primitive ask all three questions:

1. **Source identity:** is this trace materially represented in the source rather than invented by analysis?
2. **Class identity:** does it perform a real job of this requested class at source-native grain?
3. **Independent coordinate value:** does it remain useful as a standalone research coordinate beyond merely restating one local proposition or duplicating another coordinate's job?

Retain only when all three are yes, except for structural support PLACE/TIME coordinates that are necessary to keep distinct represented scenes or frames from collapsing.

Strong evidence of independent coordinate value includes one or more of:

- the source names, revisits, contrasts, corrects, questions, or otherwise gives the trace its own identity;
- the coordinate participates in more than one materially distinct local binding;
- the coordinate anchors a scene/frame, actor, persistent referent, durable characterization, or reusable orientation;
- omitting it would merge materially distinct source structure that a researcher must be able to reconnect separately.

The following do **not** establish primitive entitlement by themselves:

- appearing in the source;
- being grammatically extractable;
- being a noun, adjective, verb, prepositional phrase, amount, body/object part, or clause fragment;
- being selectable in isolation;
- being mentioned once inside one proposition;
- having a possible interpretation in more than one class.

### Pass C — duplicate and census suppression

Suppress:

- true aliases/coreferent repeats;
- pure article/auxiliary/syntactic glue;
- noun or content census items that do not keep independent source identity;
- one-off clause content that belongs only inside a local compound;
- ordinary modifiers/intensifiers/status fragments not staged as independent characterizations;
- relation fragments created by mechanically splitting a complete source-native predicate;
- prepositional/context fragments that do not establish a durable orientation;
- generic discourse wrappers when the specific source content underneath is the actual coordinate;
- analyst-created abstractions;
- cross-class duplicates whose second class adds no independent navigation value.

When uncertain, prefer the **smallest selective coordinate set that still preserves materially distinct source structure**.

### Pass D — class-native grain

For admitted primitives, use the smallest complete source-native wording that preserves the coordinate's actual class identity. Do not normalize dialect, uncertainty, negation, modality, comparison, numbers, or punctuation.

### Pass E — coreference and order

Resolve true aliases/coreference while preserving separately represented actors and relations. Order each class by first material source establishment, subject to speaker-first PERSON and broad-before-contained navigation where the schema requires it.

### Pass F — primitive freeze

Freeze the primitive inventory before compounds. Compounds may not create missing primitives or retroactively justify weak primitives.

### Pass G — proposition reconstruction

Re-read the source and construct the smallest complete source-local binding for each materially distinct proposition/event/state/report/intention/question/comparison needed by the frozen coordinate map.

## 2. Cross-class overlap rule

Cross-class overlap is **exceptional, not automatic**.

The same literal span may appear in two classes only when each projection remains independently useful as a durable coordinate after the other projection is removed. Do not duplicate merely because a phrase can be grammatically described in two ways.

A relation can coexist with an orientation, or a characterization with a relation, when both remain reusable source handles. A one-off phrase should normally have one primary coordinate role and appear in compounds as needed rather than being promoted into several primitive classes.

## 3. PLACE — source-organizing settings and occurrence positions

Retain:

- explicit settings with independent scene identity;
- contained locations when they organize a distinct represented scene;
- unnamed occurrence positions only when necessary to separate materially distinct scenes, reports, waits, or present-telling positions that otherwise collapse.

Do not create PLACE for every physical noun, object position, destination implied by one movement, surface, body part, path word, or one-off action location. A PLACE should organize navigation, not merely accompany an event.

Unnamed required positions use `source_wording: null` with an exact source cue.

## 4. TIME — source-organizing frames

Retain materially distinct episode/period/recurrence/remembered/report/present/prospective frames when they organize multiple relations or clearly shift the represented when-context.

Do not create TIME for every action phase, tense, question about duration, hypothetical act, or single clause. Several local relations should share one TIME when the source keeps them in the same frame.

## 5. PERSON — represented actors

Retain `B` plus every distinct represented human/social actor or stable group after true coreference when that actor materially participates in the represented source.

Minor/offscreen/relational/reported actors qualify when they have source identity. Suppress rhetorical/nonreferential addressees and aliases.

## 6. OBJECT — stable referents and source-reified content

Retain independently tracked:

- concrete things or salient source-tracked parts;
- documents/products/services/results/amounts or values with persistent referential identity;
- explicit choices, decisions, plans, alternatives, relations, practices, situations, or mental/content objects when the source treats them as a thing and they remain independently reusable;
- figurative objects when the source gives them stable referential identity.

Do not nominalize clauses, emotions, adjectives, every noun, every amount, every body/object part, every quoted fragment, or every candidate concept. A noun phrase mentioned once inside one proposition is not automatically an OBJECT.

Prefer the specific tracked referent over generic wrappers such as “thing,” “point,” “part,” or “something” unless the wrapper itself is independently revisited.

## 7. LABEL — independently staged characterizations

Retain characterizations, states, statuses, manners, comparisons, identity labels, candidate labels, rejections, or corrections only when the source stages them with independent descriptive identity.

Do not extract every adjective, adverb, intensity marker, quoted descriptor, rhetorical reaction, positional phrase, or momentary state as a LABEL. Keep a characterization inside its local compound when it has no standalone coordinate value.

Preserve exact uncertainty, negation, comparison, dialect, and punctuation for admitted labels.

## 8. VERB — relation coordinates, not verb census

Retain a VERB when it is the source-native relation edge needed to connect admitted coordinates or when the relation itself is independently revisited/contrasted/central enough to remain a reusable coordinate.

Prefer one complete source-native predicate for one represented edge. Do not split a predicate mechanically into matrix/support/copular/control/subordinate fragments when the source relation is better represented as one unit.

Retain modality, negation, particles, complements, or stance wording when they are part of relation identity. Suppress auxiliaries and one-off subordinate/action fragments that add no independent coordinate beyond their local proposition.

A source can contain many verbs while the lightweight inventory retains only the relation edges needed for the coordinate map.

## 9. LOCATOR — durable orientation coordinates

Retain an orientation when it independently locates or relates admitted coordinates through setting, position, path, origin/destination, containment, internal orientation, comparison, or recurring context.

A movement/context phrase can be a LOCATOR even when it contains verbal material, but not every prepositional phrase or movement phrase is entitled. Prefer orientations that are reused, contrasted, or structurally necessary to reconstruct source organization.

Do not duplicate a VERB as LOCATOR unless the orientation function remains independently useful.

## 10. Literal-language lock

Every source-derived non-null `source_wording`, `source_cue`, `order_cue`, and source-near tag must preserve the source's actual language character-for-character where the schema expects source text.

Do not repair grammar, normalize dialect, substitute synonyms, change numbers, expand contractions, or clean punctuation.

Unnamed structural PLACE/TIME support coordinates may use `source_wording: null` anchored by exact source text.

`researcher_note` is null or minimal mechanical/coreference bookkeeping. Do not use it to justify a semantic theory or reveal evaluator logic.

## 11. Q / qualities flag

`qualities_available` is a mechanical boolean indicating that source-present qualitative/descriptive material is available around the coordinate under the schema. It is not confidence and does not create primitive entitlement.

## 12. Primitive freeze audit

Before compounds verify:

1. every materially distinct source scene/frame/actor/referent/relation/orientation was considered;
2. each retained primitive passed source identity, class identity, and independent coordinate value;
3. one-off proposition detail was not promoted merely because it is extractable;
4. class overlap is exceptional and independently justified;
5. true duplicates/coreferents are merged;
6. literal wording and posture are preserved;
7. the inventory is sparse enough that each primitive remains meaningful but complete enough that distinct source organization does not collapse.

## 13. Compound reconstruction

Compounds reconnect frozen primitives into source-local propositions, events, states, reports, intentions, questions, comparisons, or relation clusters.

For each required local binding:

- include all and only frozen coordinates materially belonging to that binding;
- include participants/referents plus applicable PLACE/TIME/LOCATOR/LABEL/VERB coordinates;
- preserve source-local semantic order, although serialization order itself is not meaning;
- set Q from source-present qualitative availability under the schema.

Do not create arbitrary pairwise closure, every subset/superset permutation, broad scene mega-bundles, or a compound solely because units co-occur in a sentence.

Do not invent a standalone primitive merely to make a compound more verbally complete. The `researcher_bundle` may preserve the local source proposition while the reference expression remains limited to admitted coordinates.

## 14. Final audit

Before returning verify:

1. whole source read;
2. source coverage mapped before extraction;
3. durable-coordinate gate applied to every primitive;
4. no noun/modifier/verb/preposition census;
5. no minimal-ontology collapse of materially distinct scenes, actors, persistent referents, or central relations;
6. cross-class overlap only where each projection has independent coordinate value;
7. class-native grain is source-faithful and selective;
8. literal wording, dialect, uncertainty, negation, modality, numbers, and punctuation preserved;
9. compounds use frozen coordinates and reconstruct local propositions without graph closure;
10. candidate-only boundary preserved.

Never target hidden counts or infer hidden gold.

## 15. Calibration isolation and sealed holdout

Calibration workers must never receive approved archetype rows, expected counts, evaluator findings, prior scored answers, or sealed holdout content/output.

The sealed holdout may run only after the governing workflow proves repeated Case 2 + Case 6 passes under this same finalized contract and saved-agent lineage. The calibrated lineage may attempt that holdout exactly once. Clean-room certification then requires retirement of that lineage and a brand-new saved agent bootstrapped only from this finalized contract, with no access to prior sessions or holdout output.

## 16. Candidate-only boundary and history

All outputs remain candidate/training material. Preserve every attempt and failure. Do not promote to Oval Office or sovereign/admitted APA records. Do not mint APA IDs. Do not write to APA Data Fabric.

## Supersession boundary

`RI-CONTRACT-V90` remains controlling historical authority for V90 runs. `RI-CONTRACT-V91` supersedes V90 only for new Researcher Inventory calibration and any later holdout lawfully unlocked by repeated V91 archetype passes. V90's same-session recovery behavior and the established V66/V88A evaluator-only corrections remain retained unless separately superseded by later evidence.
