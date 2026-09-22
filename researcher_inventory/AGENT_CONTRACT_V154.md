# APA Researcher Inventory Agent Contract V154

Status: `ACTIVE SUCCESSOR FOR CALIBRATION — NOT CERTIFIED`  
Contract version: `RI-CONTRACT-V154`  
Predecessor: `RI-CONTRACT-V153`  
Effective date: 2026-09-22  
Authority: Leah's standing Researcher Inventory calibration instruction

## 1. Mission

Given one source case and the researcher interest `lightweight researcher inventory only`, return a source-faithful candidate Researcher Inventory that preserves the source's represented settings, temporal frames, actors, referents, characterizations, relations, orientations, and minimal bindings at the source's own represented grain.

This is a **researcher-addressable representational inventory**. It is not a summary, diagnosis, ontology, topic list, word census, clause parse, proposition census, or inventory of every class-compatible surface phrase.

The unit layer preserves one source-native researcher handle for each distinct represented coordinate or relation role that the source stages. A primitive may be local, one-use, low-salience, unnamed, reported, questioned, negative, prospective, figurative, or bound to one relation. It does not need global importance or independent reuse.

V154 preserves V153's whole-source source graph, scene/episode lattice, exact-source lock, candidate boundary, worker isolation, structural recall, cross-class multiplicity, deterministic apparatus controls, and holdout/certification gates. It supersedes V153 only where V153's broad `role-complete lexical envelope` rule absorbed separable arguments, complements, scene material, and contextual wording into relation primitives while structural coordinates remained undercomplete.

## 2. Controlling principle — distinct researcher address plus class-native grain

Build the inventory by asking what **distinct represented addresses and relation roles** the source gives a researcher, then express each at the grain native to its class.

A primitive survives when all four tests pass.

### Test A — represented function

The source actually establishes the candidate as one of the seven class functions:

- PLACE — a represented where-coordinate, scene, interaction position, relationship position, or situated participant/referent position;
- TIME — a represented when-coordinate, episode, phase, period, span, recurrence frame, remembered/reported/prospective frame, or present-telling frame;
- PERSON — a stable represented human or social endpoint;
- OBJECT — a source-treated concrete, abstract, deictic, decision-like, relational, internal, figurative, event-like, or proposition-like referent when the source itself treats it as a thing;
- LABEL — a source-applied characterization, category, state, identity, classification, evaluation, comparison, manner, intensity, polarity, correction, rejection, or named/questioned condition;
- VERB — a source-native action, process, state, perception, cognition, report, intention, possession, movement, waiting, modal, negative, or other relation expression;
- LOCATOR — a source-native orientation, path, relative position, movement-direction, containment, situational positioning, or comparison/figurative orientation.

If the source does not establish the class function, exclude it.

### Test B — researcher address

A candidate has a researcher address when an analyst can point back to the same represented who/what/where/when/characterization/relation/orientation without making the host sentence's grammar itself the identity.

This does **not** require recurrence, salience, standalone usefulness, or cross-context reuse. A one-use relation-bound slot may qualify. Repeated wording may represent more than one primitive when the source stages distinct occurrences with different participants, frames, or relation roles.

### Test C — class-native source grain

For PERSON, OBJECT, PLACE, and TIME, preserve the smallest source-faithful handle or neutral unnamed coordinate that identifies the distinct represented endpoint/referent/scene/frame.

For LABEL, preserve the smallest exact contiguous source span that expresses the complete characterization act without unrelated clause material.

For VERB and LOCATOR, preserve a **minimal source-native relation nucleus**: the lexical relation head plus only the source wording required for that relation's identity. Retain particles, polarity, modality, aspect, fixed relation markers, phrasal-verb material, and other function wording when removing it changes the relation itself. Exclude separable participants, objects, independent scene coordinates, temporal frames, labels, and open-clause complements when the relation remains identifiable without them. Those elements belong in their own primitives and, where source-bound, in compounds.

The test is not “shortest possible string.” It is “smallest exact contiguous string that preserves the class-native identity of this primitive.”

Do not emit a bare auxiliary, copula, intensifier, particle, preposition, discourse marker, or deictic when it has no independent class function. Do not retain an entire clause merely because the clause is meaningful when a smaller class-native primitive exists.

### Test D — identity reconciliation

Reconcile within each class only aliases, coreferences, repetitions, nested restatements, or overlapping spans that instantiate the **same represented role occurrence**.

If two spans express the same same-class occurrence at different widths, keep the smallest class-native span that preserves the role.

Do not collapse distinct source-staged relation moves merely because they use identical wording. Do not collapse legitimate cross-class overlap merely because the source span is identical.

## 3. Structural lattice must freeze before relation census

Read the whole source once and map its represented source graph before finalizing LABEL, VERB, LOCATOR, or compounds.

Freeze a provisional structural lattice in this order:

1. PERSON endpoints;
2. source-treated OBJECT referents;
3. macro PLACE scenes and interaction/relationship settings;
4. contained or participant/referent PLACE positions that the source stages separately;
5. macro TIME episodes, phases, periods, spans, recurrence frames, remembered/reported frames, prospective frames, and present-telling frames;
6. contained or action-defined TIME frames that organize represented material separately.

The lattice follows what the source **stages**, not merely explicit spatial or temporal vocabulary.

A distinct interaction, relationship position, waiting/transition position, remembered/reported scene, participant position, or present-telling scene may require an unnamed PLACE even when no location noun is supplied. A distinct action-defined episode, conversation frame, waiting phase, recurrence span, relationship period, remembered/reported period, prospective horizon, or present-telling phase may require a TIME even when no date/adverb is supplied.

The lattice is not an event census. Do not create a PLACE or TIME for every predicate, noun, preposition, adverb, or movement. Create a structural coordinate only when it organizes represented material as a distinct where/when address.

After this lattice is frozen, resolve LABEL, VERB, and LOCATOR against the structural coordinates and distinct represented relation moves.

## 4. PLACE — staged where-coordinates

PLACE inventories where represented material occurs or where a participant/referent is distinctly positioned in a scene.

Retain:

- named settings;
- contained settings that function as distinct scene positions;
- participant or referent positions when the source stages them separately;
- relationship/interaction positions whose exact geography is unspecified;
- remembered, reported, prospective, or figurative scene settings when they function as represented where-coordinates;
- waiting/transition positions when staged as distinct scene coordinates;
- present-telling location when represented as a distinct current scene coordinate.

Do not create PLACE merely from a surface, container, body part, object, destination word, spatial noun, movement path, metaphorical spatial wording, or clause containing motion. Explicit location-like language is evidence, not automatic admission.

A physical noun can be OBJECT, PLACE, or both only when the source independently establishes both functions.

For a genuinely unnamed PLACE use null `source_wording`, an exact source cue, and neutral mechanical tag/note wording only.

## 5. TIME — staged when-coordinates

TIME inventories the source's distinct temporal organization, not every temporal expression and not every verb occurrence.

Retain a TIME when the source stages a distinct episode, phase, earlier/later period, interaction/conversation/waiting/transition phase, recurrence span, relationship/life span, intended/anticipated period, remembered/reported frame, prospective/future-similar horizon, or present reflection/telling frame.

An action or relation may define the boundary of a TIME frame. The action is not automatically a TIME, but an episode does not need an explicit time word in order to qualify.

Temporal adverbs, durations, recurrence markers, event predicates, or discourse markers do not create separate TIME rows unless they establish a distinct organizing frame.

Contained phases may each qualify when the source clearly transitions among them.

For a genuinely unnamed TIME use null `source_wording`, an exact source cue, and neutral mechanical tag/note wording only.

## 6. PERSON — stable human/social endpoints

PERSON inventories `B` plus every distinct stable represented human or social actor/group after strict coreference.

A PERSON may qualify through acting, speaking, perceiving, being acted upon, possession, accompaniment, benefit, relationship, remembered/reported presence, or a clear social reference.

Do not create separate PERSON rows for aliases or pronouns that resolve to an existing endpoint. Exclude rhetorical or generic addressees without a stable represented endpoint.

## 7. OBJECT — source-treated referential handles

OBJECT inventories distinct source-treated things or abstractions that have referential standing in the represented graph.

Eligible referents may be concrete, abstract, internal, deictic, relational, decision-like, choice-like, figurative, event-like, or proposition-like **when the source itself treats them as an addressable thing**.

A source phrase has OBJECT standing when the source handles, possesses, selects, points back to, compares as a thing, questions/decides about as a thing, or otherwise gives it a stable referential role.

A relation, choice, event, or internal construct may be an OBJECT when the source reifies it into a referential handle. Do not exclude such a handle merely because its content also participates in VERB, LABEL, TIME, or compound structure.

Exclude:

- pronouns that are only aliases of an existing referent;
- transient deictics or discourse placeholders;
- wh-clause, proposition, or metalinguistic shells that function only as grammar/discourse and lack independent source-treated standing;
- bare grammatical complements with no referential standing;
- every noun phrase merely because it is nominal.

One-use referents may qualify. Recurrence is not required.

## 8. LABEL — source-applied characterization acts

LABEL inventories source-applied characterizations that function as a distinct represented quality, category, state, identity, evaluation, comparison, manner, polarity, correction, rejection, or questioned condition.

Class membership is functional, not part-of-speech based. A category noun, rejection token, comparison, or multiword state may be a LABEL when the source uses it to characterize a retained coordinate or relation.

Retain identity/role categories, status/condition judgments, explicit evaluations, speaker-applied self/other characterizations, relation-state descriptions, operational states explicitly asserted about a retained coordinate, comparisons/figurative characterizations, questioned/negated/rejected/corrected/uncertain labels, and manners/intensities when they independently characterize a represented action/state.

Do **not** turn every adjective, adverb, modifier, noun-phrase descriptor, scene-texture detail, discourse reaction, or descriptive fragment into a LABEL. Incidental texture remains source evidence/quality unless the source performs a distinct characterization act with it.

When overlapping spans characterize the same target in the same way, retain the smallest class-native characterization span. Preserve separate labels when the source stages separate characterization acts.

`qualities_available` remains mechanical metadata. It neither requires nor forbids a LABEL.

## 9. VERB — minimal source-native relation nuclei

VERB inventories distinct source-native relation moves at the source's staged grain.

For each represented action/state/relation, retain the smallest exact contiguous **relation nucleus** that preserves what the relation itself is and its source posture.

### Relation-nucleus rule

Retain, where required for relation identity:

- the lexical relation head;
- phrasal-verb particles or fixed multiword relation material;
- polarity/negation;
- modality;
- aspect when it distinguishes the represented relation state;
- fixed prepositional/relation markers integral to the predicate;
- direction when it is lexically integral to the relation rather than a separately addressable LOCATOR;
- comparison wording only when the comparison itself is the relation.

Exclude from the VERB span when separable without changing relation identity:

- PERSON participants;
- OBJECT arguments;
- PLACE/TIME coordinates;
- LABEL characterizations;
- independently addressable LOCATOR material;
- open-clause complements that stage a separate relation;
- discourse framing or explanatory clause material.

A complement belongs inside the VERB primitive only when it is lexically/fixed-function material required to identify that relation, not merely because the clause is needed to understand the proposition.

Do not emit multiple overlapping VERB rows for one represented relation merely because a clause contains matrix, support, control, reporting, copular, perception, cognition, or complement structure. Keep a support/reporting/etc. verb only when the source stages that act as its own relation move; keep the hosted relation separately when it is also staged.

Serial/coordinated actions remain separate when the source stages distinct moves. Repeated identical wording may remain separate when it represents distinct occurrences.

## 10. LOCATOR — minimal source-native orientation nuclei

LOCATOR inventories distinct source-native orientation, positioning, path, containment, movement-direction, or figurative/comparison orientation relations.

For each orientation occurrence, retain the smallest exact contiguous span that identifies **that orientation itself**.

Retain genuinely represented relative position, path/direction, containment, source-to-target spatial relation, movement orientation, and figurative/comparison orientation when independently staged.

Decompose adjacent orientations when the source stages them as distinct relations. Do not merge path, accompaniment, destination, waiting context, temporal context, or another orientation merely because they occur in the same clause.

Do not create LOCATOR merely from:

- recipient/dative markers;
- possession/genitive markers;
- topic/aboutness relations;
- abstract argument/complement markers;
- ordinary object selection;
- a preposition that exists only as grammar;
- temporal or discourse framing that belongs in TIME or carries no independent orientation;
- every comparison phrase.

A movement/state expression may be both VERB and LOCATOR, or LABEL and LOCATOR, only when the same occurrence independently supplies both researcher functions. Cross-class overlap is not a defect by itself.

Reconcile overlapping LOCATOR spans only when they express the same orientation occurrence at different widths; keep separate orientations when the source stages separate positioning relations.

## 11. Cross-class multiplicity

Class membership is not globally exclusive.

The same source wording or occurrence may appear in more than one class when each retained row has a distinct complete researcher function and address.

Do not duplicate a phrase across classes merely because its words permit several linguistic interpretations. Ask what functions the source actually stages.

Do not use cross-class de-duplication to erase an independently represented function.

## 12. Structural recall and relation recall

After initial extraction, replay the whole source by scene/episode and perform a structural recall pass for PERSON, OBJECT, PLACE, and TIME.

Restore low-salience, unnamed, relationship-bound, participant-position, reported, prospective, action-defined, or present-telling structural coordinates that the source clearly stages. This recall may recover omitted coordinates but may not harvest every noun, temporal phrase, or spatial phrase.

Then perform relation-class recall for LABEL, VERB, and LOCATOR using represented function, researcher address, class-native grain, and identity reconciliation.

Relation recall may restore a missed relation role or lawful cross-class function; it may not re-expand primitives into clause-sized restatements, grammatical scaffolding, or overlapping widths of one occurrence.

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

Repeated identical wording may receive separate units only when it instantiates separate represented role occurrences. The apparatus owns canonical IDs and deterministic numbering.

## 15. Primitive audit before compounds

Before compounds, replay the complete source scene by scene and relation by relation and ask:

1. Is every distinct represented scene/interaction/relationship/participant position present, including unnamed and present-telling positions?
2. Is every distinct organizing episode/phase/period/span/frame present, including action-defined and unnamed frames?
3. Are stable people and source-treated referents present without pronoun/discourse-shell inflation?
4. Does each LABEL represent a distinct source-applied characterization act rather than incidental texture?
5. Does each VERB preserve one minimal source-native relation nucleus rather than a bare incomplete fragment or an argument-heavy clause span?
6. Does each LOCATOR preserve one independent orientation nucleus rather than grammar/context inflation or merged adjacent orientations?
7. Have same-class aliases/repetitions/nested restatements of the same role occurrence been reconciled without collapsing distinct occurrences?
8. Have low-salience, one-use, negative, questioned, reported, prospective, figurative, or relational primitives been preserved when they still have a researcher address?
9. Is every retained source string exact and posture-faithful?

Do not aim for a hidden count. Aim for one row per distinct researcher-addressable class role at its class-native source grain.

## 16. Compound construction — replay the frozen role graph

Freeze all primitives first.

A compound represents one minimal source-staged binding among two or more frozen primitives that actively co-participate in one represented connection.

Construct compounds from the same researcher-addressable graph used to resolve primitives. A compound captures one source-staged proposition/connection at a time, not every syntactic subset and not an entire scene.

Create a compound only when:

1. at least two frozen primitives are actively bound by the source;
2. the binding adds reconstructive relational information beyond listing the members;
3. every member actively participates in that exact binding; and
4. the result is not a duplicate, alternate parse, transitive closure, arbitrary subset, nested restatement, or scene-wide mega-bundle.

A compound cannot create, delete, merge, split, retype, justify, or substitute for primitives. If the primitive ledger is wrong, do not repair it through compounds.

Qualitative/support material can be available around a binding without forcing every support primitive into the compound. `qualities_available` reports that support availability; it is not a graph-closure instruction.

## 17. `qualities_available`

`qualities_available` is mechanical metadata. True means the source supplies material descriptive/qualitative evidence associated with that coordinate or binding; false otherwise.

It is not an alternate primitive layer and it is not a reason to omit or create a LABEL.

`Q` is never a primitive and never a compound member ref.

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
3. all deterministic harness tests must pass; and
4. all failed/partial attempts must remain preserved.

After that gate, the calibrated lineage may run the sealed holdout exactly once. No repair to that lineage may be learned from the holdout result.

If the one-shot holdout is archetypal, retire the calibrated lineage. Create a brand-new saved agent containing only this finalized durable contract, with no prior agent session, archetype answer, evaluator result, or holdout output available to it, and run the sealed holdout once in a new session.

Certification requires the fresh agent to pass that clean-room holdout. Until then status remains `NOT CERTIFIED`.

Never promote records to Oval Office, mint APA IDs, or write candidate calibration output into admitted APA database/fabric as part of this process.

## 20. Historical-integrity effect

`RI-CONTRACT-V153` remains preserved as the contract governing workflow run `35697956250` and earlier V153 work.

V153 is `PARTIALLY SUPERSEDED FOR FORWARD CALIBRATION — 2026-09-22` only for:

- treating separable open-class arguments/complements/context as part of a broad role-complete VERB/LOCATOR envelope when the relation nucleus remains identifiable without them;
- allowing adjacent orientation/context material to merge into one wide LOCATOR span instead of preserving separately staged orientations;
- insufficiently forcing the structural PLACE/TIME lattice to freeze before relation extraction, especially participant/referent positions and action-defined frames;
- permitting source-present descriptive/discourse material to survive as OBJECT/LABEL merely because it is semantically interpretable rather than independently source-treated/addressable; and
- compounds replaying a relation graph destabilized by those primitive-grain errors.

V153's whole-source graph, structural-lattice principle, exact-source and posture lock, candidate boundary, worker isolation, immutable workbook gate, deterministic apparatus controls, failure preservation, one-shot holdout rule, clean-room certification rule, and no-promotion/no-ID/no-database-write boundaries remain controlling as restated here.

No predecessor is deleted or rewritten.
