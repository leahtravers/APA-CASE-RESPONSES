# APA Researcher Inventory Agent Contract V153

Status: `ACTIVE SUCCESSOR FOR CALIBRATION — NOT CERTIFIED`  
Contract version: `RI-CONTRACT-V153`  
Predecessor: `RI-CONTRACT-V152`  
Effective date: 2026-09-22  
Authority: Leah's standing Researcher Inventory calibration instruction

## 1. Mission

Given one source case and the researcher interest `lightweight researcher inventory only`, return a source-faithful candidate Researcher Inventory that preserves the source's represented settings, temporal frames, actors, referents, characterizations, relations, orientations, and minimal bindings at the source's own represented grain.

This is a **researcher-addressable representational inventory**. It is not a summary, diagnosis, ontology, topic list, word census, clause parse, proposition census, or inventory of every class-compatible surface phrase.

The unit layer preserves one source-native researcher handle for each distinct represented coordinate or relation role that the source stages. A primitive may be local, one-use, low-salience, unnamed, reported, questioned, negative, prospective, figurative, or bound to one relation. It does not need global importance or independent reuse. A new surface occurrence is not automatically a new primitive, but a grammatically narrower head is not automatically the correct primitive either.

V153 preserves V152's exact-source, candidate-boundary, worker-isolation, structural-recall, and deterministic-apparatus controls. It supersedes V152 only where V152's canonical-primitive and smallest-kernel language compressed a source-staged researcher role below its role-complete grain or failed to construct a distinct scene/episode coordinate.

## 2. Controlling principle — researcher-addressable role identity

Build the inventory by asking what **distinct represented addresses and relation roles** the source gives a researcher.

A primitive survives when all four tests pass.

### Test A — represented function

The source actually establishes the candidate as one of the seven class functions:

- PLACE — a represented where-coordinate, scene, interaction position, or situated participant position;
- TIME — a represented when-coordinate, episode, phase, period, span, recurrence frame, remembered/reported/prospective frame, or present-telling frame;
- PERSON — a stable represented human or social endpoint;
- OBJECT — a source-treated concrete, abstract, deictic, decision-like, relational, internal, figurative, event-like, or proposition-like referent when the source itself treats it as a thing;
- LABEL — a source-applied characterization, category, state, identity, classification, evaluation, comparison, manner, intensity, polarity, correction, rejection, or named/questioned condition;
- VERB — a source-native action, process, state, perception, cognition, report, intention, possession, movement, waiting, modal, negative, or other relation expression;
- LOCATOR — a source-native orientation, path, relative position, movement-direction, containment, situational frame, contextual positioning, or comparison/figurative orientation.

If the source does not establish the class function, exclude it.

### Test B — researcher address

Ask whether the candidate is a distinct coordinate or relation role in the represented source graph.

A candidate has a researcher address when an analyst can point back to the same represented who/what/where/when/characterization/relation/orientation without making the host sentence's grammar itself the identity.

This does **not** require recurrence, salience, standalone usefulness, or cross-context reuse. A one-use relation-bound slot may qualify. A repeated lexical form may also represent more than one primitive when the source stages separate occurrences with different participants, frames, or relation roles.

### Test C — role-complete source-native grain

Choose the smallest exact contiguous source span that preserves the **complete researcher role the source stages**, not merely the narrowest grammatical head.

For LABEL, VERB, and LOCATOR, exclude unrelated clause material and independently represented participants when they add no identity to the role. But retain particles, complements, polarity, modality, aspect, contextual function words, comparison/path wording, and role-bearing arguments when removing them changes what relation, characterization, or orientation the researcher can address.

The test is semantic-role preservation at source grain, not idiomatic lexicalization. A word or phrase may be grammatically separable yet still belong in the primitive when the source uses it to define the represented role.

Do not emit a bare auxiliary, copula, intensifier, particle, preposition, discourse marker, or deictic when its identity exists only inside a larger role-complete atom. Do not retain an entire clause merely because the clause is meaningful when a smaller contiguous role-complete span exists.

### Test D — identity reconciliation

Reconcile within each class only those aliases, coreferences, repetitions, nested restatements, or overlapping spans that instantiate the **same represented role occurrence**.

If two spans express the same class-role occurrence at different widths, keep the smallest role-complete source-native envelope.

Do not collapse two distinct source-staged relation moves merely because they use the same wording. Do not collapse legitimate cross-class overlap merely because the source span is identical.

## 3. Scene/episode lattice before relation census

Read the whole source once and map its represented source graph before finalizing relation-like classes.

Freeze a provisional structural lattice of:

1. PERSON endpoints;
2. source-treated OBJECT referents;
3. PLACE scene, interaction, relationship, and participant-position coordinates; and
4. TIME episodes, phases, periods, spans, recurrence frames, remembered/reported frames, prospective frames, and present-telling frames.

The lattice must follow what the source **stages**, not just explicit spatial or temporal vocabulary.

A distinct interaction, relationship episode, waiting position, remembered/reported scene, or present-telling scene may require an unnamed PLACE even when no location noun is supplied. A distinct action-defined episode, conversation frame, waiting phase, recurrence span, relationship period, or present-telling phase may require a TIME even when no date/adverb is supplied.

The lattice is not an event census. Do not create a new PLACE or TIME for every predicate. Create one when the source organizes material around a distinct represented where/when coordinate.

Then resolve LABEL, VERB, and LOCATOR against this lattice and the distinct represented relation moves.

## 4. PLACE — staged where-coordinates

PLACE inventories where represented material occurs or where a participant/referent is distinctly positioned in a scene.

Retain:

- named settings;
- contained settings that function as distinct scene positions;
- participant positions when the source stages them separately;
- relationship/interaction positions whose exact geography is unspecified;
- remembered, reported, prospective, or figurative scene settings when they function as represented where-coordinates;
- waiting/transition positions when staged as distinct scene coordinates;
- present-telling location when represented as a distinct current scene coordinate.

Do not create PLACE merely from:

- a surface, container, body part, object, destination word, or spatial noun;
- a movement path already functioning only as LOCATOR;
- an object that happens to be physically located somewhere;
- metaphorical spatial vocabulary that does not establish a scene/position;
- a clause that contains motion without staging a separate where-coordinate.

A physical noun can be OBJECT, PLACE, or both only when the source independently establishes both functions.

For a genuinely unnamed PLACE use null `source_wording`, an exact source cue, and neutral mechanical tag/note wording only.

## 5. TIME — staged when-coordinates

TIME inventories the source's distinct temporal organization, not every temporal expression and not every verb occurrence.

Retain a TIME when the source stages a distinct:

- episode or phase;
- earlier/later period;
- interaction, conversation, waiting, or transition phase;
- recurrence span;
- relationship/life span;
- intended or anticipated period;
- remembered/reported frame;
- prospective/future-similar horizon;
- present reflection/telling frame.

An action or relation may define the boundary of a TIME frame. The action is not automatically a TIME, but an episode does not need an explicit time word in order to qualify.

Words such as temporal adverbs, durations, recurrence markers, or event predicates do not create separate TIME rows unless they establish a distinct organizing frame.

Contained phases may each qualify when the source clearly transitions among them.

For a genuinely unnamed TIME use null `source_wording`, an exact source cue, and neutral mechanical tag/note wording only.

## 6. PERSON — stable human/social endpoints

PERSON inventories `B` plus every distinct stable represented human or social actor/group after strict coreference.

A PERSON may qualify through acting, speaking, perceiving, being acted upon, possession, accompaniment, benefit, relationship, remembered/reported presence, or a clear social reference.

Do not create separate PERSON rows for aliases or pronouns that resolve to an existing endpoint. Exclude rhetorical/generic addressees without a stable represented endpoint.

## 7. OBJECT — source-treated referential handles

OBJECT inventories distinct source-treated things or abstractions that have referential standing in the represented graph.

Eligible referents may be concrete, abstract, internal, deictic, relational, decision-like, choice-like, figurative, event-like, or proposition-like **when the source itself treats them as an addressable thing**.

A source phrase has OBJECT standing when the source handles, possesses, selects, points back to, compares as a thing, questions/decides about as a thing, or otherwise gives it a stable referential role.

A relation, choice, event, or internal construct may be an OBJECT when the source reifies it into a referential handle. Do not exclude such a handle merely because its content also participates in VERB, LABEL, TIME, or compound structure.

Exclude:

- pronouns that are only aliases of an existing referent;
- transient discourse placeholders;
- clause/proposition shells created only by analyst paraphrase;
- bare grammatical complements with no source-treated referential standing;
- every noun phrase merely because it is nominal.

One-use referents may qualify. Recurrence is not required.

## 8. LABEL — source-applied characterization roles

LABEL inventories source-applied characterizations that function as a distinct represented quality, category, state, identity, evaluation, comparison, manner, polarity, correction, rejection, or questioned condition.

Class membership is functional, not part-of-speech based. A source-applied category noun, rejection token, comparison, or multiword state may be a LABEL when the source uses it to characterize a retained coordinate or relation.

Retain complete source-native characterizations including, where represented:

- identity or role categories;
- status/condition judgments;
- explicit evaluations;
- speaker-applied self/other characterizations;
- relation-state descriptions;
- operational states explicitly asserted about a retained coordinate;
- comparisons and figurative characterizations;
- questioned, negated, rejected, corrected, or uncertain candidate labels;
- manners/intensities when they independently characterize a represented action/state.

Do **not** turn every adjective, adverb, modifier, noun-phrase descriptor, or scene-texture detail into a LABEL. Incidental descriptive texture remains source evidence/quality when it only fleshes out an object or setting and is not staged as an independently addressable characterization.

When several overlapping spans characterize the same target in the same way, retain the smallest role-complete characterization envelope. Preserve separate labels when the source stages separate characterization acts, even when one responds to, qualifies, or rejects another.

`qualities_available` remains mechanical metadata. It neither requires nor forbids a LABEL.

## 9. VERB — role-complete relation expressions

VERB inventories distinct source-native relation moves at the source's staged grain.

For each represented action/state/relation, retain the smallest exact contiguous **role-complete lexical envelope** that preserves what the relation is, its posture, and any relation-defining complement or orientation supplied by the source.

### Relation-envelope rule

Exclude unrelated clause material and independently represented arguments when the relation remains the same researcher-addressable role without them.

Retain source wording when removing it would change or under-specify the relation role, including as applicable:

- particles;
- complement or control wording;
- prepositional/relation markers;
- polarity/negation;
- modality;
- aspect;
- direction integral to the staged relation;
- comparison wording when the comparison itself is the relation;
- role-bearing argument wording needed to distinguish what relation is being represented.

Do not reduce a relation mechanically to its lexical head. Conversely, do not retain a whole proposition or clause when a smaller role-complete contiguous span preserves the same relation.

### No duplicate relation multiplication

Do not emit multiple overlapping VERB rows for the same represented relation merely because a clause contains a matrix predicate, support predicate, complement predicate, or wider paraphrastic span.

Choose the role-complete relation envelope. Emit another VERB when the source genuinely stages another relation move, including when the same lexical wording occurs again as a distinct represented act.

Copulas, auxiliaries, reporting/support/control verbs, perception/cognition verbs, and discourse predicates are not automatically excluded or included. Keep them when the source represents that act/state as its own relation; suppress them when they merely host another retained relation and add no distinct represented move.

Serial/coordinated actions remain separate when the source stages distinct moves, except when the combined contiguous wording itself is the single researcher-addressable action the source presents.

## 10. LOCATOR — role-complete orientation/context relations

LOCATOR inventories distinct source-native orientation, positioning, path, or contextual relations.

Retain role-complete wording that independently establishes:

- where/relative position;
- path or movement direction;
- containment;
- toward/away/from/through/into/out/over/up/down relations;
- source-to-target spatial orientation;
- situational, recurring, or temporal context when it genuinely positions a represented event/frame;
- figurative/comparison orientation when the source uses it as an orientation relation;
- relation-bound contextual positioning that tells the researcher how one represented element is situated relative to another.

Do not create LOCATOR merely from:

- recipient/dative markers;
- possession/genitive markers;
- topic/aboutness relations;
- abstract argument/complement markers;
- ordinary object selection;
- a preposition that exists only as grammar;
- every temporal cue or comparison phrase.

A movement or state expression may be both VERB and LOCATOR, or LABEL and LOCATOR, when the source independently uses the same occurrence for both functions. Cross-class overlap is not a defect by itself.

Reconcile overlapping LOCATOR spans only when they express the same represented orientation occurrence at different widths; keep separate orientations when the source stages separate positioning relations.

## 11. Cross-class multiplicity

Class membership is not globally exclusive.

The same source wording or occurrence may appear in more than one class when each retained row has a distinct complete researcher function and address.

Do not duplicate a phrase across classes merely because its words permit several linguistic interpretations. Ask what functions the source actually stages.

Do not use cross-class de-duplication to erase an independently represented function. Same wording in different classes is lawful when the researcher obtains different coordinate/relation information from each class role.

## 12. Structural recall and relation recall

After initial extraction, perform a structural recall pass for PERSON, OBJECT, PLACE, and TIME.

Replay the whole source by scene/episode rather than by token. Restore low-salience, unnamed, relationship-bound, reported, prospective, or present-telling structural coordinates that the source clearly stages even when no explicit noun/date initially forced them into view.

This recall is intentionally asymmetric: it may recover omitted structural coordinates, but it may not harvest every noun, temporal phrase, or spatial phrase.

Then perform relation-class recall for LABEL, VERB, and LOCATOR using the represented-function, researcher-address, role-complete-grain, and identity-reconciliation tests.

Relation recall may restore a missed relation role or lawful cross-class function; it may not re-expand the inventory into overlapping restatements of the same role occurrence.

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

1. Is every distinct represented scene/interaction/relationship position present, including unnamed and present-telling positions?
2. Is every distinct organizing episode/phase/period/span/frame present, including action-defined and unnamed frames?
3. Are stable people and source-treated referents present without pronoun/discourse-shell inflation?
4. Does each LABEL represent a distinct source-applied characterization/category/state/evaluation role rather than incidental texture?
5. Does each VERB preserve one complete researcher-addressable relation role at source-staged grain rather than a bare head or an overlapping clause span?
6. Does each LOCATOR represent a genuine orientation/context role rather than an argument marker, while preserving lawful cross-class overlap?
7. Have same-class aliases/repetitions/nested restatements of the same role occurrence been reconciled without collapsing distinct occurrences?
8. Have low-salience, one-use, negative, questioned, reported, prospective, figurative, or relational primitives been preserved when they still have a researcher address?
9. Is every retained source string exact and posture-faithful?

Do not aim for a hidden count. Aim for one row per distinct researcher-addressable class role at the source's staged grain.

## 16. Compound construction — replay the frozen role graph

Freeze all primitives first.

A compound represents one minimal source-staged binding among two or more frozen primitives that actively co-participate in one represented connection.

Construct compounds from the same researcher-addressable relation graph used to resolve primitives. A compound should capture one source-staged proposition/connection at a time, not every syntactic subset and not an entire scene.

Create a compound only when:

1. at least two frozen primitives are actively bound by the source;
2. the binding adds reconstructive relational information beyond listing the members;
3. every member actively participates in that exact binding; and
4. the result is not a duplicate, alternate parse, transitive closure, arbitrary subset, nested restatement, or scene-wide mega-bundle.

A compound cannot create, delete, merge, split, retype, justify, or substitute for primitives. If the primitive ledger is wrong, do not repair it through compounds.

Cross-class overlap inside the primitive ledger is lawful when each member has its own class function; compounds use the frozen unit refs supplied by the apparatus.

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
3. all deterministic harness tests must pass; and
4. all failed/partial attempts must remain preserved.

After that gate, the calibrated lineage may run the sealed holdout exactly once. No repair to that lineage may be learned from the holdout result.

If the one-shot holdout is archetypal, retire the calibrated lineage. Create a brand-new saved agent containing only this finalized durable contract, with no prior agent session, archetype answer, evaluator result, or holdout output available to it, and run the sealed holdout once in a new session.

Certification requires the fresh agent to pass that clean-room holdout. Until then status remains `NOT CERTIFIED`.

Never promote records to Oval Office, mint APA IDs, or write candidate calibration output into admitted APA database/fabric as part of this process.

## 20. Historical-integrity effect

`RI-CONTRACT-V152` remains preserved as the contract governing workflow run `35691176776` and earlier V152 work.

V152 is `PARTIALLY SUPERSEDED FOR FORWARD CALIBRATION — 2026-09-22` only for:

- treating the narrowest canonical/source-native kernel as the default grain when that removes role-defining source wording;
- insufficient construction of unnamed or relation-defined scene/episode coordinates;
- interpreting relation arguments/function words too narrowly when they are part of the source-staged researcher role;
- insufficiently preserving lawful cross-class overlap where distinct researcher functions coexist; and
- compounds replaying an under-specified primitive role graph.

V152's literal/posture lock, source/interpretation separation, candidate boundary, worker isolation, immutable workbook gate, deterministic apparatus controls, failure preservation, holdout one-shot rule, and clean-room certification rule remain controlling as restated here.

No predecessor is deleted or rewritten.
