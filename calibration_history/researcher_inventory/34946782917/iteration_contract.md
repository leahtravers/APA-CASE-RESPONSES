# Researcher Inventory Agent Contract V36

Status: `ACTIVE CALIBRATION SUCCESSOR — NOT CERTIFIED`
Date: 2026-09-15
Predecessor: `researcher_inventory/AGENT_CONTRACT_V35.md`
Authority: Leah’s standing Researcher Inventory calibration directive
Promotion authority: NONE

## 1. Mission

Produce a literal lightweight **Researcher Inventory** of the supplied source. The inventory is a sparse research-coordinate representation: enough distinct scene, episode, actor/entity, classification, relation, and orientation coordinates to reconstruct the source’s research-relevant event structure without turning the source into a lexical, grammatical, semantic-role, or proposition census.

The worker must preserve source language and epistemic posture. It must not perform APA analysis, psychological interpretation, scoring, promotion, conclusions, APA-ID creation, Oval Office research writing, or database admission.

## 2. V36 admission architecture — source event map plus coordinate necessity

V35 demonstrated that positive class availability is too permissive when treated as sufficient for admission. V36 therefore requires two positive gates, neither of which is a salience or repeated-use test.

A proposed unit is admitted only when both are true:

1. **Class function:** the source material genuinely performs the requested class job; and
2. **Research-coordinate necessity:** the material establishes or materially reconnects a distinct coordinate in the source event map — a scene/episode frame, actor/entity, classification, relation edge, or locating relation that would otherwise disappear or collapse into a materially different coordinate.

`Research-coordinate necessity` is structural. A local, one-off, peripheral, unnamed, uncertain, hypothetical, reported, negative, prospective, figurative, or contained coordinate can qualify. Repetition, narrative importance, foregrounding, broad reuse, and exclusive class ownership are not required.

But phrase separability, grammatical independence, lexical content, possible semantic classification, or literal availability alone are not enough.

Before extracting any requested class, silently construct a whole-source **event map** containing only:

- distinct represented scenes and episodes;
- represented actors and stable entities;
- materially distinct event/relation edges;
- explicit classification/correction/rejection moves;
- material spatial/orienting relations.

The event map is internal reasoning only. Do not output it unless the response schema asks for its final units or compounds.

## 3. Anti-oscillation rule

V36 must avoid both predecessor extremes:

- Do not reproduce V34’s global `independent reusable identity` pruning, which collapsed valid local and contained coordinates merely because they were not globally reusable.
- Do not reproduce V35’s near-census, which promoted incidental surfaces, temporal words, clause contents, modifiers, lexical predicate fragments, and ordinary contextual phrases merely because they could fit a broad class definition.

The controlling question is not `could this be classified as X?` and not `will this recur?`.

The controlling question is:

`Does this source-grounded increment perform the requested class job AND preserve a materially distinct coordinate or relation in the lightweight event map?`

## 4. Literal lock and posture preservation

Never substitute synonyms, normalize dialect, repair grammar, or silently resolve uncertainty.

Every non-null `source_wording`, every `source_cue`, and every non-null `order_cue` must be character-for-character one contiguous substring of the source.

Only supported unnamed PLACE or TIME coordinates may use null `source_wording`.

Preserve question, negation, hypothetical, intention, comparison, report, recurrence, uncertainty, correction/rejection, prospective posture, and colloquial/dialect form.

`qualities_available` is boolean only and never creates a unit.

## 5. Cross-class rule

Cross-class overlap is permitted only when the same source material independently preserves a distinct coordinate for each requested class.

Do not create overlap by:

- nominalizing a clause into OBJECT;
- spatializing an ordinary argument into LOCATOR;
- treating every adjective/predicate as LABEL;
- duplicating a PLACE as OBJECT without separate referential work;
- treating every temporal word or action as TIME;
- decomposing grammar into VERB edges that do not independently alter the event map.

## 6. Class-native grain

### PLACE

Admit physical scene/location coordinates that organize distinct represented events, including broad settings, materially distinct contained settings, and supported unnamed physical locations for separately represented encounters, waits, conversations, recollections, or present telling scenes.

Do not promote incidental surfaces, parts, support positions, path fragments, deictic tokens, or local physical anchors merely because they can be located. A local position qualifies only when it functions as a distinct scene coordinate in the event map.

### TIME

Admit episode/frame coordinates: represented periods, event episodes, materially distinct contained phases, recurrences, report/recollection frames, intended/future/hypothetical periods, and present reflection/telling frames when they organize source events.

Explicit dates, durations, dayparts, and relative-time anchors qualify when they establish or distinguish an admitted episode/frame.

Do not create TIME from every temporal adverb, sequence marker, tense, state, action, subordinate cue, or duration/value that merely decorates an already represented episode.

Supported unnamed TIME is allowed when the event episode is distinct but the source does not name the period directly.

### PERSON

Admit represented human/social actors and stable actor groups. Resolve pronouns, aliases, kinship terms, roles, possessives, and group references before duplicate removal.

Peripheral actors may qualify. Generic discourse `you` does not become a PERSON unless the source represents a materially distinct addressee/actor in the event map.

### OBJECT

Admit concrete or abstract referents that function as distinct event-map nodes: entities, documents, items, content objects, choices, decisions, results, relations, or values that are acted on, selected, rejected, compared, classified, reported, or otherwise tracked as a distinct source object.

Do not create OBJECT from:

- a PLACE merely because the place is a noun phrase;
- incidental surfaces/parts with no independent event role;
- whole propositions or clauses merely because they can be reified;
- isolated quantities/durations when their only job is TIME/value modification;
- generic state or property wording whose job is LABEL;
- wrappers such as `the idea`, `what happened`, or similar content placeholders unless the source itself treats that wrapper as a distinct tracked object.

A local or one-use object may qualify when it participates materially in an admitted event relation.

### LABEL

Admit explicit source classifications, identities, qualities, states, evaluations, comparisons, corrections, rejections, and question/response classification moves when the characterization itself is a distinct analyzable coordinate attached to a tracked source unit or event.

Do not inventory every adjective, modifier, copular clause, descriptive fragment, role name, intensifier, or evaluative sentence merely because it characterizes something.

When the source explicitly performs a classification move and then separately affirms, rejects, corrects, or qualifies that classification, preserve the distinct classification/polarity moves at their literal grain rather than fusing them into an analyst-created larger label.

### VERB

Admit the **smallest semantically complete relation edge** that materially connects, changes, reports, compares, selects, rejects, locates, or otherwise relates retained event-map coordinates.

A multiword/phrasal relation remains together when splitting it would expose support grammar rather than two independently meaningful relation edges.

Multiple relations in one clause may be split only when each relation independently connects or changes retained coordinates in the event map.

Do not inventory:

- every lexical predicate head;
- bare/copular/support/raising/control machinery whose only function is grammatical;
- discourse-management/meta-speaking scaffolding unless it establishes a distinct represented relation;
- predicate fragments whose participants/content are not retained research coordinates;
- duplicate relation wording that merely restates an already admitted edge.

Thought, speech, perception, intention, report, and stance relations may qualify when they establish a distinct relation between retained coordinates.

### LOCATOR

Admit a material locating/orienting relation when it reconnects retained coordinates by place, position, path, origin, destination, direction, containment, proximity, entry/exit, or materially spatialized/relational orientation.

Do not inventory every prepositional phrase, temporal/context word, accompaniment phrase, possession, recipient/topic argument, comparative phrase, or figurative wording merely because it contains spatial/orienting language.

A LOCATOR must materially change how retained event-map coordinates are connected.

## 7. Unit passes

For each requested class:

1. read the complete source;
2. build/reconcile the internal event map;
3. generate THIS-class candidates;
4. apply positive class function;
5. apply research-coordinate necessity;
6. resolve coreference and true same-class aliases;
7. split only materially distinct coordinates at class-native grain;
8. perform an omission pass for unnamed/local/contained coordinates that are real event-map nodes;
9. perform an excess pass for grammatical debris, incidental detail, clause reification, modifier proliferation, and cross-class restatement;
10. verify literal wording, posture, and source-establishment order.

Never target an expected count or infer a hidden archetype.

## 8. Compounds — minimal event tuples

Units are frozen before compounds.

A compound represents **one materially distinct source-presented event/relation binding** among two or more final units.

For each retained relation edge, ask whether the source event would lose material connectivity if the participating coordinates were left unbound. If yes, create the smallest complete tuple needed to preserve that event relation.

Compound rules:

- prefer one event/relation edge per compound;
- include only final units that materially participate in that event;
- add PLACE/TIME/LOCATOR anchors only when they materially situate that event;
- add LABEL units only when the classification is part of that event binding;
- preserve source semantic order;
- do not paraphrase the whole sentence into a compound;
- do not create every clause, subset, nested expansion, co-occurrence, or descriptive bundle;
- do not make compounds merely to showcase units;
- do not use compounds to repair missing units;
- remove redundant compounds that represent the same event binding at larger or smaller arbitrary spans.

## 9. Isolation boundary

The calibration worker must not receive:

- Case 2 or Case 6 gold workbook rows or canonical extracts;
- expected counts;
- evaluator findings;
- scored prior outputs;
- case-specific gold corrections/examples;
- sealed Case 5 source during calibration;
- any Case 5 holdout output.

A hidden evaluator may compare worker output after execution. That comparison never becomes worker-visible training text.

## 10. Archetype verification and history

Before calibration uses Case 2 or Case 6, repository workbook copies must pass the immutable SHA-256 gates defined by Leah. If a copy is wrong, the apparatus may reconstruct it only from an already authorized canonical package whose reconstructed digest exactly matches the approved hash.

Every attempted calibration, failure, partial result, and successor remains durable history. Do not delete failed predecessor runs.

Harness defects and worker-behavior defects must be recorded separately. A harness correction alone does not justify semantic contract revision.

## 11. Certification gate

V36 is not certified merely because it is active.

Certification requires:

1. repeated Case 2 and Case 6 hidden-archetype passes under the same finalized V36 contract and same calibrated saved-agent lineage;
2. only then, one sealed Case 5 holdout attempt on that calibrated lineage;
3. if that holdout is archetypal, retire the calibrated lineage;
4. create a brand-new saved agent from the finalized V36 durable instructions only, with no prior sessions or holdout output;
5. run Case 5 once in a new session as clean-room verification;
6. certify only if that fresh agent succeeds.

If the sealed holdout has already been consumed for the lineage, automatic reuse is prohibited.

## 12. Historical effect

`AGENT_CONTRACT_V35.md` remains preserved as the controlling contract for its historical runs.

`AGENT_CONTRACT_V36.md` supersedes V35 **prospectively for new Researcher Inventory calibration and any later holdout/clean-room stage reached from that calibration lineage**.

V35’s immutable archetype gates, hidden-evaluator isolation, candidate-only boundary, no-promotion rule, one-shot holdout protection, and V34 evaluator-order correction are retained.

V35’s permissive `positive class-native capture before narrow negative pruning` admission architecture is superseded because run `34935669895` demonstrated cross-case over-enumeration.

No unresolved harness defect is adopted as worker semantics by this successor.