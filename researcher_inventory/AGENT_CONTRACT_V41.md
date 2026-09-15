# Researcher Inventory Durable Worker Contract V41

Status: `ACTIVE CALIBRATION SUCCESSOR — NOT CERTIFIED`
Contract ref: `RI-CONTRACT-V41`
Predecessor: `RI-CONTRACT-V40`
Effective for new calibration only: 2026-09-15

## 1. Scope

Produce the lightweight Researcher Inventory candidate only. Inventory the source; do not interpret it, score APA, infer psychological meaning, draw conclusions, promote records, mint APA IDs, or admit anything to sovereign/production fabric.

This successor preserves V40’s literal lock, hidden-evaluator isolation, immutable archetype gate, candidate-only boundary, one-shot holdout gate, and clean-room certification requirements. It changes only the semantic admission/grain rule prospectively.

## 2. Why V41 exists

V40’s binding-role indispensability filter remained too restrictive: a source-presented coordinate could be omitted when it was locally nested, dependent, one-use, or not globally necessary to distinguish the enclosing binding. V41 replaces that threshold with a source-coordinate ledger plus linkage test. The repair is general and is not based on giving the worker any archetype row, expected count, evaluator finding, scored output, or holdout content.

## 3. Source-coordinate ledger

Read the complete source before extracting any class.

Reconstruct a SOURCE COORDINATE LEDGER containing source-presented coordinates that participate in represented material. A candidate belongs in the ledger when the source itself presents it as one of the following at a natural selectable grain:

- a scene/location coordinate;
- an episode/frame coordinate;
- a represented human/social actor;
- a concrete or abstract referent, content, choice, relation, set, or internal represented object;
- a characterization, correction, classification, comparison, state, manner, evaluation, or questioned label;
- a predicate/action/state/relation kernel;
- an orienting span for location, path, destination, containment, accompaniment, recurrence, or other source-presented orientation.

A candidate need not be globally indispensable, independent of every other unit, repeated, salient, or the primary subject of a clause. Local, nested, peripheral, one-use, possessive/relational, questioned, hypothetical, prospective, reported, recurring, and colloquial coordinates may qualify when they are source-presented and linked to represented material.

Supported unnamed PLACE/TIME coordinates may qualify when a represented episode or scene requires a selectable frame even though the source does not name the coordinate. For those only, `source_wording` may be null and `source_cue` must be exact source text.

## 4. Linkage test

After generating a class candidate, ask:

1. Is this coordinate presented by the source, or is it a permitted supported unnamed PLACE/TIME frame?
2. Does it participate in, characterize, locate, orient, contain, relate, or provide content for at least one represented source relation/state/frame?
3. Is it at the smallest COMPLETE NATURAL source grain for its class?
4. Is it not merely support grammar, an untracked wrapper, a duplicate/coreferent mention, an isolated function word, or an analyst-created abstraction?

If yes, retain it. Do not add a separate requirement that omitting it would collapse the whole binding.

## 5. Loss control without census behavior

V41 is not a lexical census, part-of-speech census, modifier census, semantic-role census, proposition census, event census, or grammatical parse.

Reject:

- auxiliaries/copulas that are only support for a larger natural predicate rather than the represented relation kernel;
- isolated prepositions/deictics when the complete orienting span is the natural unit;
- duplicate mentions after true coreference/alias merge;
- discourse wrappers or clause/proposition wrappers with no independently represented content/referent role;
- grammatical person marking without a represented actor;
- modifier fragments that only decorate a retained natural characterization and have no separately presented characterization role;
- analyst-created labels, categories, causal explanations, summaries, or inferred psychological concepts;
- arbitrary splitting of coordinated or multiword predicates when the source presents one natural relation kernel.

Do not reject a source-presented coordinate merely because it is nested, dependent, locally descriptive, possessive, one-use, or already participates in a broader compound.

## 6. Class rules

### PLACE
Retain each source-presented or supported physical scene/location coordinate that locates a represented actor, object, state, conversation, encounter, wait, departure/destination, recollection, present telling, or other represented material. Broad and materially contained coordinates may both exist. Do not require a location to host a unique independent event. Reject surfaces/object parts that merely describe an object and do not function as a scene/location coordinate.

### TIME
Retain each source-presented or supported episode/frame coordinate needed to place represented material in source progression or posture, including reported/recollected, intended, hypothetical, prospective, recurring, waiting, interaction, transition, and present-reflection frames. A TIME need not contain an explicit temporal noun. Reject wording that is only grammatical tense/aspect support and does not provide or delimit a frame.

### PERSON
Retain the speaker plus every represented human/social actor or stable actor group that participates in or is materially related to represented content. Relational, possessive, prospective, reported, and one-use actors may qualify. Resolve aliases/coreference before deduplication. Do not require independent action as a condition of existence.

### OBJECT
Retain source-presented concrete or abstract referents that are tracked, acted on, possessed, transferred, located, evaluated, contemplated, selected/rejected, related, reported, or otherwise used as represented content. Source-presented choices, relations, sets/categories, decisions, values, and internal represented objects may qualify. Reject analyst abstractions and clause wrappers not presented as referents/content.

### LABEL
Retain the smallest complete source-presented characterization/correction/classification/comparison/state/manner/evaluation/questioned-label unit. Local or one-use characterizations may qualify. Preserve colloquial form. Do not merge two separately voiced characterizations merely because one is broader or semantically related. Do not promote a relation/orientation into LABEL unless the source uses it as characterization.

### VERB
Retain one smallest complete literal predicate kernel for each source-presented operative action, state, possession, perception, report, relation, or modal/questioned relation edge. A complete kernel may include a copular/positional/state form, particle, complement, or coordinated material when splitting would turn the source relation into support fragments or change its natural relation grain. Preserve nested/sequential relation edges that the source separately presents. Reject bare support auxiliaries and arbitrary conjunct fragmentation.

### LOCATOR
Retain the smallest complete source-presented orienting span that independently locates or orients a represented participant/relation/frame by setting, position, path, origin/destination, containment/proximity, accompaniment/carrying, entry/exit, recurrence orientation, or materially spatial/relational direction. Do not require the orientation to create a new scene. Reject isolated preposition/deictic fragments and abstract characterizations whose source function is LABEL rather than orientation.

## 7. Literal lock and source-near tags

- Every non-null `source_wording` is a character-for-character contiguous substring of the source.
- Every `source_cue` and non-null `order_cue` is a character-for-character contiguous substring of the source.
- Preserve punctuation, apostrophes, hyphens, capitalization, spelling, dialect, negation, uncertainty, question, comparison, intention, hypothetical, report, recurrence, correction, and prospective posture.
- `researcher_short_tag` is compact and source-near. For an explicitly worded coordinate, build it only from words already present in that coordinate’s exact `source_wording` and/or `source_cue`; do not add synonyms, explanatory adjectives, or analyst wording. Supported unnamed PLACE/TIME may use a neutral navigation tag because `source_wording` is null.
- Copy literal spans from source; do not reconstruct them from memory.

## 8. Ordering and identity

Code owns canonical IDs. The worker supplies neutral canonical keys only for alias/coreference merge.

Order by first source establishment after coreference, subject to apparatus rules that place the speaker first and broad-before-contained PLACE/LOCATOR coordinates when established together. Do not reorder by importance.

## 9. Unit and compound layers

Complete and freeze the unit ledger first. Compounds may not create, suppress, merge, repair, or rename units.

Then reconstruct source-presented relation/state/characterization bindings and serialize each at natural source grain from frozen unit refs. Include the retained participants, coordinates, labels, predicates, and orientations actually linked by that source binding. Do not emit every subset or grammatical clause, and do not collapse several distinct source bindings into sentence-sized mega-compounds.

`qualities_available` is a boolean only; it never creates a unit. Q is mechanical output metadata, not a semantic unit.

## 10. Final adjudication

Before return:

1. reread the entire source;
2. check each represented source segment against the coordinate ledger for omissions;
3. check every retained unit against the linkage test for excess;
4. check class assignment and natural complete grain;
5. check exact literal/source-near requirements;
6. freeze units;
7. rebuild compounds from the represented bindings using only frozen refs;
8. verify source order and posture.

Never target an expected count or infer a hidden archetype.

## 11. Isolation and protected evaluation

The worker must never receive:

- Leah-approved archetype workbook contents;
- archetype rows or expected counts;
- evaluator findings or scored outputs;
- case-specific gold corrections;
- prior failed-output corrections derived from hidden gold;
- the sealed Case 5 source during calibration;
- any Case 5 holdout output.

Mechanical validator feedback may be returned only to correct schema, exact-source, tag-token, identifier, or other deterministic mechanical failures. It is not gold/evaluator guidance.

## 12. Calibration and certification gate

V41 is not certified by existing.

Before sealed holdout use, the same finalized V41 contract and saved-agent lineage must pass immutable Case 2 and Case 6 archetype verification repeatedly, including resolution, lexical preservation, class assignment, and compound construction.

Only then may the protected harness run sealed Case 5 exactly once on that calibrated lineage. If it passes archetypally, retire that lineage, create a brand-new saved agent from this finalized durable contract only, and run sealed Case 5 in a new clean-room session. Certification requires that fresh agent to pass without access to prior sessions or holdout output.

Any failed holdout remains final evidence for that lineage and may not be reused as calibration material.
