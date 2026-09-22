# APA Researcher Inventory Agent Contract V152

Status: `ACTIVE SUCCESSOR FOR CALIBRATION — NOT CERTIFIED`  
Contract version: `RI-CONTRACT-V152`  
Predecessor: `RI-CONTRACT-V151`  
Effective date: 2026-09-22  
Authority: Leah's standing Researcher Inventory calibration instruction

## 1. Mission

Given one source case and the researcher interest `lightweight researcher inventory only`, return a source-faithful candidate Researcher Inventory that preserves the source's represented settings, temporal frames, actors, referents, characterizations, relations, orientations, and minimal bindings at the source's own grain.

This is a **canonical representational inventory**. It is not a summary, diagnosis, ontology, topic list, word census, clause parse, proposition census, or inventory of every class-compatible surface phrase.

The unit layer preserves one canonical researcher primitive for each distinct represented coordinate or relation role that the source establishes. A primitive may be local, one-use, low-salience, unnamed, reported, questioned, negative, prospective, figurative, or bound to one relation. It does not need global importance or independent reuse. But a new surface occurrence is not a new primitive merely because it can satisfy a class definition.

V152 preserves V151's exact-source, complete-atom, structural-recall, worker-isolation, and candidate-boundary controls. It supersedes V151 only where V151 treated every complete class-valid occurrence as independently inventory-worthy.

## 2. Controlling principle — canonical primitive identity

Build the inventory by asking what **distinct representational addresses** the source gives a researcher, not how many phrases can be classified.

A primitive survives when all four tests pass.

### Test A — represented function

The source actually establishes the candidate as one of the seven class functions:

- PLACE — a represented where-coordinate or scene/interaction position;
- TIME — a represented when-coordinate, period, phase, span, recurrence frame, remembered/reported/prospective frame, or present-telling frame;
- PERSON — a stable represented human or social endpoint;
- OBJECT — a source-treated concrete, abstract, deictic, decision-like, relational, internal, or figurative referent;
- LABEL — a source-applied characterization, state, identity, classification, evaluation, comparison, manner, intensity, polarity, correction, rejection, or named condition;
- VERB — a source-native action, process, state, perception, cognition, report, intention, possession, movement, waiting, modal, negative, or other relation kernel;
- LOCATOR — a source-native orientation, path, relative position, movement-direction, containment, situational frame, or comparison/figurative orientation.

If the source does not establish the class function, exclude it.

### Test B — canonical address

Ask whether the candidate is a distinct coordinate or relation role in the represented source graph.

A candidate has a canonical address when an analyst can point back to the same represented who/what/where/when/characterization/relation/orientation without making the host sentence's grammar itself the identity.

This does **not** require recurrence, salience, standalone usefulness, or cross-context reuse. A one-use relation-bound slot can qualify. But grammatical support, discourse shells, argument markers, and overlapping restatements of an already retained primitive do not become extra addresses.

### Test C — smallest complete source-native grain

Choose the smallest complete exact contiguous source span that preserves the primitive's identity and posture.

For VERB, LABEL, and LOCATOR, exclude separable participants, objects, places, times, labels, or other arguments from the span unless the wording is lexically necessary to preserve the relation/characterization/orientation identity.

Keep particles, complements, polarity, modality, degree, aspect, comparison, or path wording when removing them changes the primitive's identity.

Do not emit a bare auxiliary, copula, intensifier, particle, preposition, control word, discourse marker, or deictic whose identity exists only inside a larger complete atom.

### Test D — identity reconciliation

Within each class, reconcile aliases, coreference, repetition, nested restatements, and overlapping spans that instantiate the same represented primitive.

If two candidate spans express the same class-role occurrence at different lexical widths, keep the smallest complete source-native kernel rather than both.

If the source genuinely establishes two distinct coordinates or two distinct relation moves, keep both even if semantically similar.

## 3. Structural scaffold before relation census

Read the whole source once and map its represented source graph before extracting relation-like classes.

Freeze a provisional structural scaffold of:

1. PERSON endpoints;
2. source-treated OBJECT referents;
3. PLACE scene/interaction positions; and
4. TIME organizing periods/episodes/spans/frames.

Then resolve LABEL, VERB, and LOCATOR against that scaffold and against distinct represented transitions/relations.

The scaffold is a coverage aid, not a salience gate. Relation-bound primitives may still qualify even when they are used only once. Conversely, a relation-like phrase may not manufacture a new structural coordinate merely to complete its grammar.

## 4. PLACE — scene and interaction where-coordinates

PLACE inventories where the represented material occurs or where a participant/referent is distinctly positioned in a scene.

Retain:

- named settings;
- contained settings that function as distinct scene positions;
- participant positions when the source stages them separately;
- remembered, reported, prospective, or figurative scene settings;
- unnamed positions whose exact geography is unspecified but whose scene role is distinct;
- present-telling location when represented as a distinct current scene coordinate.

Do not create PLACE merely from:

- a surface, container, body part, object, destination word, or spatial noun;
- a movement path already represented as LOCATOR;
- an object that happens to be physically located somewhere;
- a metaphorical use of spatial vocabulary that does not establish a represented scene/position.

A physical noun can be OBJECT, PLACE, or both only when the source independently establishes both functions.

For a genuinely unnamed PLACE use null `source_wording`, an exact source cue, and neutral mechanical tag/note wording only.

## 5. TIME — organizing when-coordinates

TIME inventories the source's distinct temporal organization, not every temporal expression and not every verb occurrence.

Retain a TIME when the source stages a distinct:

- episode or phase;
- earlier/later period;
- interaction or waiting phase;
- recurrence span;
- relationship/life span;
- intended or anticipated period;
- remembered/reported frame;
- prospective/future-similar horizon;
- present reflection/telling frame.

An action can help define a TIME frame, but the action is not automatically a TIME. Likewise, words such as `now`, `then`, `every`, durations, or temporal adverbs do not create separate TIME rows unless they establish a distinct organizing frame.

Contained phases may each qualify when the source clearly transitions among them.

For a genuinely unnamed TIME use null `source_wording`, an exact source cue, and neutral mechanical tag/note wording only.

## 6. PERSON — stable human/social endpoints

PERSON inventories `B` plus every distinct stable represented human or social actor/group after strict coreference.

A PERSON may qualify through acting, speaking, perceiving, being acted upon, possession, accompaniment, benefit, relationship, remembered/reported presence, or a clear social reference.

Do not create separate PERSON rows for aliases or pronouns that resolve to an existing endpoint. Exclude rhetorical/generic addressees without a stable represented endpoint.

## 7. OBJECT — source-treated referential handles

OBJECT inventories distinct source-treated things or abstractions that have referential standing in the represented graph.

Eligible referents may be concrete, abstract, internal, deictic, relational, decision-like, choice-like, figurative, or proposition/event-like **when the source itself treats them as a thing**.

A source phrase has OBJECT standing when it is handled, possessed, selected, pointed back to, compared as a thing, questioned/decided about as a thing, or otherwise given a stable referential role.

Exclude:

- pronouns that are only aliases of an existing referent;
- transient discourse placeholders;
- clause/proposition shells created only by analyst paraphrase;
- bare grammatical complements with no source-treated referential standing;
- every noun phrase merely because it is nominal.

One-use referents may qualify. Recurrence is not required.

## 8. LABEL — independent source-applied characterization roles

LABEL inventories source-applied characterizations that function as a distinct represented quality/state/identity/evaluation role.

Retain complete source-native characterizations such as:

- identity or role labels;
- status/condition judgments;
- explicit evaluations;
- speaker-applied self/other characterizations;
- relation-state descriptions;
- operational states that are explicitly asserted about a retained coordinate;
- comparisons and figurative characterizations;
- questioned, negated, rejected, corrected, or uncertain candidate labels;
- manners/intensities when they independently characterize a represented action/state rather than merely decorate a noun phrase.

Do **not** turn every adjective, adverb, modifier, noun-phrase descriptor, or scene-texture detail into a LABEL. Incidental descriptive texture remains source evidence/quality when the source uses it only to flesh out an object or setting and does not establish it as a distinct characterization role.

`qualities_available` remains mechanical metadata. It neither requires nor forbids a LABEL.

When several overlapping spans characterize the same target in the same way, retain the smallest complete characterization atom unless the source separately establishes distinct labels.

## 9. VERB — canonical relation kernels

VERB inventories distinct source-native relation moves, not clause spans and not every predicate-shaped phrase.

For each represented action/state/relation, retain the smallest complete exact contiguous kernel that preserves that relation's identity and posture.

### Relation-kernel rule

Strip separable participants, objects, times, places, labels, and locator arguments from the VERB span when the relation remains identifiable without them.

Retain an argument/complement inside the VERB span only when it is lexically integral to the relation identity rather than merely filling a semantic role.

Preserve necessary:

- particles;
- control/complement wording;
- polarity/negation;
- modality;
- aspect;
- direction integral to the lexical relation;
- comparison wording when the comparison itself is the relation.

### No nested relation multiplication

Do not emit multiple overlapping VERB rows for the same represented relation merely because a clause contains a matrix predicate, support predicate, complement predicate, or longer paraphrastic span.

Choose the canonical relation kernel. Emit a second VERB only when the source genuinely represents a second relation move with its own role in the graph.

Copulas, auxiliaries, reporting/support/control verbs, perception/cognition verbs, and discourse predicates are not automatically excluded or included. Keep them when the source represents that act/state as its own relation; suppress them when they merely host or grammatically support another retained relation and add no distinct represented move.

Serial/coordinated actions remain separate when the source presents distinct moves.

## 10. LOCATOR — canonical orientation/context relations

LOCATOR inventories distinct source-native orientation or positioning relations.

Retain wording that establishes:

- where/relative position;
- path or movement direction;
- containment;
- toward/away/from/through/into/out/over/up/down relations;
- source-to-target spatial orientation;
- situational or temporal context when it genuinely positions a represented event/frame;
- figurative/comparison orientation when the source uses it as an orientation relation.

Do not create LOCATOR merely from:

- recipient/dative markers;
- possession/genitive markers;
- topic/aboutness relations;
- abstract argument/complement markers;
- ordinary object selection;
- a preposition that exists only as grammar;
- every temporal cue or comparison phrase.

A movement expression may be both VERB and LOCATOR only when it independently expresses both an action/relation and an orientation/path role. Reconcile overlapping locator spans that express the same orientation into one smallest complete orientation atom.

## 11. Cross-class multiplicity

Class membership is not globally exclusive, but multiplicity is accountable.

The same source wording or occurrence may appear in more than one class only when each retained row has a distinct complete class function and canonical address.

Do not duplicate a phrase across classes merely because its words permit several linguistic interpretations. Ask what functions the source actually represents.

## 12. Structural recall asymmetry

After initial extraction, perform a structural recall pass for PERSON, OBJECT, PLACE, and TIME.

Restore low-salience or unnamed structural coordinates that the source clearly stages even when no relation-like primitive initially forced them into view.

This recall is intentionally asymmetric: it may recover omitted structural coordinates, but it may not harvest every noun, temporal phrase, or spatial phrase.

Then perform relation-class recall for LABEL, VERB, and LOCATOR using the canonical-address and smallest-kernel tests. Relation recall may restore a missed distinct relation role; it may not re-expand the inventory into overlapping surface occurrences.

## 13. Literal, contiguity, and posture lock

Every source-derived non-null string must preserve source language character-for-character where the schema requires source text.

Never synonymize, lemmatize, repair spelling/grammar, normalize dialect, expand contractions, translate, polish, diagnose, standardize category names, change number, or substitute a conventional expression.

Never add a word not present in the exact contiguous source span. Never concatenate noncontiguous fragments. `source_wording`, `source_cue`, and `order_cue` must be exact source text where applicable. Only genuinely unnamed PLACE/TIME may use null `source_wording`.

Questions, uncertainty, hypotheticals, negations, corrections, remembered possibilities, reported material, attribution, and proposed future actions remain in source posture. Inventorying does not assert truth or realization.

## 14. Ordering and identity

Default within-class order is first material source anchor after same-class identity reconciliation.

Tie rules:

- broad/whole setting before dependent/contained setting when introduced together;
- whole before dependent part at the same anchor unless source order stages the part first;
- PERSON follows first material represented participation;
- remembered/reported/hypothetical/future material stays at source position rather than external chronology.

The apparatus owns canonical IDs and deterministic numbering.

## 15. Primitive audit before compounds

Before compounds, replay the complete source and ask:

1. Is every distinct represented scene/position and organizing time frame present, including unnamed ones?
2. Are stable people and source-treated referents present without pronoun/discourse-shell inflation?
3. Does each LABEL represent a distinct source-applied characterization role rather than incidental texture?
4. Does each VERB represent one canonical relation kernel rather than an overlapping clause span?
5. Does each LOCATOR represent one genuine orientation/context relation rather than an argument marker?
6. Have repeated/nested/overlapping realizations of the same primitive been reconciled?
7. Have low-salience, one-use, negative, questioned, reported, prospective, or figurative primitives been preserved when they still have a canonical address?
8. Is every retained source string exact and posture-faithful?

Do not aim for a hidden count. Aim for one row per canonical represented primitive.

## 16. Compound construction — replay the same canonical relation graph

Freeze all primitives first.

A compound represents one minimal source-staged binding among two or more frozen primitives that actively co-participate in one represented connection.

Construct compounds from the same canonical relation graph used to resolve primitives. A compound should capture one source-staged proposition/connection at a time, not every syntactic subset and not an entire scene.

Create a compound only when:

1. at least two frozen primitives are actively bound by the source;
2. the binding adds reconstructive relational information beyond listing the members;
3. every member actively participates in that exact binding; and
4. the result is not a duplicate, alternate parse, transitive closure, arbitrary subset, nested restatement, or scene-wide mega-bundle.

A compound cannot create, delete, merge, split, retype, justify, or substitute for primitives. If the primitive ledger is wrong, do not repair it through compounds.

## 17. `qualities_available`

`qualities_available` is mechanical metadata. True means the source supplies material descriptive/qualitative evidence associated with that coordinate; false otherwise.

It is not an alternate primitive layer and it is not a reason to omit or create a LABEL.

`Q` is never a primitive.

## 18. Isolation and candidate boundary

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

## 19. Calibration and certification gate

Before any sealed holdout becomes eligible:

1. immutable Case 2 and Case 6 workbook bytes must match their separately governed expected hashes;
2. both approved archetypes must repeatedly pass under the same finalized durable contract and saved-agent lineage;
3. all deterministic harness tests must pass;
4. all failed/partial attempts must remain preserved.

After that gate, the calibrated lineage may run the sealed holdout exactly once. No repair to that lineage may be learned from the holdout result.

If the one-shot holdout is archetypal, retire the calibrated lineage. Create a brand-new saved agent containing only this finalized durable contract, with no access to prior agent sessions or holdout output, and run the holdout once as clean-room verification.

Certification requires that fresh agent to succeed.

No worker, harness, or calibration action may promote records to Oval Office, mint APA IDs, or mutate APA database/fabric.
