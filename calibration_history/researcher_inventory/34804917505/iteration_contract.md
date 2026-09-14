# RESEARCHER INVENTORY WORKER CONTRACT v22

Status: ACTIVE CALIBRATION SUCCESSOR — NOT CERTIFIED  
Effective date: 2026-09-13  
Contract version: RI-CONTRACT-V22  
Mission: RESEARCHER INVENTORY ONLY  
Predecessor: `researcher_inventory/AGENT_CONTRACT_V21.md` (RI-CONTRACT-V21)  
Authority: Leah's standing Researcher Inventory calibration directive.

## Successor effect

V21 remains preserved as historical calibration evidence. V22 supersedes V21 for forward calibration behavior because workflow run `34800603953`, attempt 2, demonstrated a generalizable over-resolution failure after the immutable archetype and deterministic apparatus gates passed.

V20 demonstrated the opposite failure: global marginality/minimality pressure removed valid local coordinates. V21 corrected that by using class-local closure, but made material representation plus a plausible class job too close to a sufficient admission rule. The result was broad extraction of incidental predicate detail, excessive nested relations, over-framed PLACE/TIME rows, and compound cascades.

V22 therefore uses one balanced rule:

> **ADMISSION FIRST. BOUNDED CLOSURE SECOND. PRUNE THIRD. A coordinate is retained only when it independently earns lightweight researcher-index status for its class. Then scan the whole source for every other coordinate that independently passes the same gate. Do not optimize for either fewer rows or more rows.**

Retained unchanged:

- exactly seven inventory classes;
- literal/source-near lexical preservation and no synonym substitution;
- full-source reading before any class return;
- approved archetype, evaluator, scored-output, and sealed-holdout isolation;
- candidate-only status;
- mechanical apparatus ownership of canonical IDs, deterministic validation, retries, and SQL shaping;
- no APA parsing, scoring, promotion, APA-ID creation, or Oval Office research writing.

## Isolation

The worker never receives approved archetypes, gold outputs, expected answers, expected counts, evaluator findings, prior scored outputs, sealed holdout source, or holdout outputs.

The worker receives only this durable contract, one bounded source story, neutral task rules/schema, and, when explicitly supplied by the apparatus, an unscored provisional output from another stateless pass under this same contract.

Never infer or reconstruct a hidden expected answer.

## Job

Read the whole source. Build a lightweight Researcher Inventory in exactly seven classes:

1. `PLACE`
2. `TIME`
3. `PERSON`
4. `OBJECT`
5. `LABEL`
6. `VERB`
7. `LOCATOR`

Then build lightweight compounds from the retained units.

This is an index of researcher-selectable semantic coordinates, not a token inventory, grammar parse, clause inventory, summary, psychological analysis, or exhaustive ontology.

`Lightweight` is a semantic-grain constraint. It means retain every distinct coordinate needed to navigate and reconnect the represented material at useful research grain, while excluding incidental linguistic detail that does not deserve independent index status.

## Independent lightweight admission gate

For every candidate in the requested class, require all of the following before admission:

1. **Source grounding** — the coordinate is materially represented by the source, or is one of the narrowly permitted unnamed PLACE/TIME coordinates required by the source.
2. **Positive class job** — it genuinely performs this class's job rather than merely being describable in class-like language.
3. **Independent coordinate status** — a researcher could meaningfully select/reconnect this coordinate on its own at the intended lightweight grain. It is not merely a syntactic fragment, modifier, support word, incidental argument detail, or mechanically derivable restatement of another retained coordinate.
4. **Reconnective value** — omitting it would erase a distinct semantic coordinate needed to navigate or reconstruct at least one material proposition, situation, relation, characterization, episode, or location at lightweight grain.
5. **No same-class duplicate** — after alias/coreference resolution, it is not the same semantic coordinate doing the same class job as an already retained row.

Material representation by itself is not enough. A phrase does not become a unit merely because it can be assigned a semantic description, appears in a nested clause, is spatially/temporally imaginable, or overlaps another class.

Locality is not a reason to reject a candidate. A coordinate that appears in only one episode or proposition is valid when it independently passes the admission gate.

Cross-class overlap is allowed only when the same source span independently passes the admission gate for each class. Do not suppress a valid coordinate because another class carries related meaning, and do not duplicate it across classes merely because overlap is allowed.

## Required extraction sequence

For the requested class, perform three silent passes in this order.

### Pass A — admission

Read the complete source and identify candidates. Apply the independent lightweight admission gate to each candidate. Reject candidates that fail any gate element.

### Pass B — bounded closure

Re-scan the complete source specifically for omitted candidates that independently pass the same admission gate. Include valid local/single-episode coordinates and valid cross-class overlaps. Do not widen the gate during closure.

### Pass C — pruning and exactness

Remove only:

- same-class aliases/coreferential duplicates;
- duplicate rows doing the identical class job at the identical semantic coordinate;
- bare grammatical/support fragments;
- invented or weakly inferred coordinates;
- candidates that on review fail independent lightweight coordinate status.

Then repair exact source copying and semantic ordering.

Do not use expected row count, aesthetic sparsity, exhaustive coverage, or provisional-output size as a target.

## Source language

Never substitute a synonym for source language.

For an explicit coordinate:

- `source_wording` is a character-for-character contiguous substring of the source;
- `source_cue` is a character-for-character contiguous substring of the source;
- preserve punctuation, apostrophes, hyphens, capitalization, spelling, and dialect;
- copy from the source rather than reconstructing from memory;
- keep `researcher_short_tag` compact and source-near.

For a materially required unnamed PLACE or TIME only, `source_wording = null` is permitted. Its `source_cue` must still be an exact source substring and the short tag must neutrally describe the class job without inventing a named location or date.

`researcher_note` is normally null. Use it only for neutral coreference, an unnamed PLACE/TIME explanation, or required mechanical bookkeeping.

Preserve negation, questions, uncertainty, correction, comparison, recurrence, intention, hypothetical posture, reported speech, and futurity. Do not convert represented possibility into asserted occurrence.

## PLACE — independently indexable where-coordinate

PLACE indexes an independently researcher-selectable **where-coordinate** for a represented situation, actor/object location, origin, or destination.

Keep, when they independently pass the admission gate:

- explicit broad and contained settings that organize represented material;
- materially distinct situation/occurrence positions;
- origins and destinations that function as semantic coordinates for a represented movement or relation;
- unnamed positions of distinct occurrences when the source requires a separate where-coordinate but does not name it;
- a materially distinct present telling/reporting position when it functions as its own represented situation.

Do not create PLACE merely for:

- every entity's incidental position inside an already indexed scene;
- accompaniment, possession, instrument, or object association that does not establish a where-coordinate;
- every movement predicate or spatially imaginable action;
- a hypothetical-only pseudo-place;
- generic recurrence without a distinct represented position;
- a direction/path phrase whose independent job is LOCATOR;
- a mental/state metaphor whose primary job is not spatial situation.

Two situations may share physical space yet remain distinct PLACE coordinates when the discourse makes their where-frames independently selectable. Conversely, different wording in one undifferentiated where-frame does not require multiple PLACE rows.

## TIME — independently indexable episode/frame/span

TIME indexes a materially distinct **episode, period, span, recurrence, transition, intended period, reported period, reflection frame, or prospective frame** that organizes represented content.

No clock or date is required.

Keep a separate TIME when the source establishes a temporal frame that a researcher could meaningfully reselect: for example a broader episode, a genuine subepisode boundary, a standing span, a recurrence, a later report, a changed-state period, an intention period, present reflection, or a prospective/future frame.

A subepisode earns its own TIME only when it functions as a distinct frame, not merely because another verb/action occurs inside the broader episode.

Do not create TIME from:

- each verb, clause, action, purpose, question, or micro-step;
- tense/aspect alone;
- duration wording that does not itself establish a separate temporal frame;
- a hypothetical action without an independently represented intended/prospective frame;
- wording that merely occurs later in sentence order while remaining inside the same frame.

## PERSON — human actor/group coordinate

PERSON is a materially represented human or stable social group that is independently selectable in the story.

Keep the speaker plus materially represented actors and human endpoints/owners/sources/beneficiaries/participants whose identity matters to retained propositions or relations.

Resolve pronouns, aliases, kinship expressions, and stable groups before counting. Do not create PERSON from a generic audience, grammatical person, or hypothetical role with no distinct represented human actor.

## OBJECT — independently referable thing/relation/choice

OBJECT is an independently selectable represented referent.

It may be concrete, abstract, relational, internal, or figurative, but it must be treated by the source as something a researcher could reconnect as a thing: an entity, value, set/category, choice, decision, alternative, explicitly reified relation, or internal/figurative object.

Keep source-distinguished wholes/parts only when each independently matters. A relation/state may be OBJECT only when the source treats it as a referent in its own right, not merely because every proposition can be nominalized.

Do not create OBJECT for:

- every noun phrase;
- every clause, complement, predicate, action, or state;
- pronoun repeats after coreference resolution;
- metadiscourse wrappers;
- generic abstract labels mechanically derived from a VERB/LABEL;
- incidental descriptive content with no independent referent status.

An OBJECT may coexist with a VERB or LABEL carrying related content when each independently passes its own class gate.

## LABEL — independently retrievable characterization

LABEL is a source-applied characterization that a researcher could meaningfully retrieve independently from the action/relation carrying it.

Keep the shortest **complete** source phrase carrying a material quality, state, identity, evaluation, comparison, correction, rejection, or negated characterization. Preserve polarity, qualification, and comparison when removing them changes the characterization.

Characterizations embedded in questions, reports, or reflections remain eligible. Strip subject/question/reporting/copular scaffolding only when it is not part of the characterization itself.

Do not create LABEL for:

- every modifier, quantity, intensifier, or descriptive fragment;
- pure action/relation/reporting wording;
- a whole clause whose only characterization is already captured by a smaller complete phrase;
- a failure/action predicate merely because it implies a state.

A LABEL may overlap another class only if its characterization is independently retrievable.

## VERB — independently reconnectable action/relation edge

VERB indexes a materially distinct **action or relation edge** that independently contributes to reconstructing a proposition or relation network.

Use the shortest complete source-near predicate expression that preserves the semantic edge.

Keep a nested, embedded, modal, locative, reporting, perception, thought, state, or purpose relation only when it establishes its own independently reconnectable edge with material participants/referents or proposition-level content.

Do not create separate VERB rows for every syntactically nested predicate when they are merely support, control, aspect, modality, purpose scaffolding, or elaboration of one retained semantic edge.

Do not split bare auxiliaries, tense support, negation particles, infinitive markers, or coordination syntax into rows.

Do not collapse two genuinely distinct semantic edges merely because one clause contains the other.

A VERB may overlap LABEL or LOCATOR when the same wording independently earns both class jobs.

## LOCATOR — independently indexable locating/context relation

LOCATOR is a source phrase that independently expresses a locating/context relation useful for reconnecting retained coordinates.

Keep, when independently indexable:

- setting/position relations;
- path, direction, origin/destination relations;
- movement/trajectory relations whose locating job matters beyond the action verb;
- containment and proximity;
- recurring-context relations;
- genuine figurative/mental location/path relations when the source treats the location/path itself as a coordinate.

Do not create LOCATOR from:

- isolated prepositions;
- routine possession, accompaniment, instrument, recipient, or topic marking;
- purely temporal wording;
- every spatially flavored predicate;
- characterization-only wording whose location metaphor is not independently indexable.

Overlap with VERB/LABEL/PLACE is allowed only when the locating relation independently passes the admission gate.

## qualities_available

`qualities_available` is a boolean only.

Set it true when material qualifying/descriptive language is associated with the coordinate in the source. Otherwise false.

Do not enumerate qualities. `Q` is not a unit reference and never creates a row by itself.

## Ordering

The apparatus owns final IDs and numbering.

Within each class, order by the earliest material source anchor of the resolved semantic coordinate after alias/coreference resolution.

When later wording refers back to an already established coordinate, keep the coordinate at its earliest material anchor. Where broad and contained coordinates are introduced at the same anchor, broad precedes contained. Keep reported, intended, hypothetical, and prospective material in source-discourse order rather than reconstructing real-world chronology.

## Stateless verification

If the apparatus supplies an unscored provisional output, rebuild from the complete source and this contract. Treat the provisional output only as a candidate checklist.

Verification uses the same three-stage rule:

1. **Admission audit:** test every provisional row against the independent lightweight admission gate; remove any row that fails it.
2. **Bounded closure:** scan the complete source for omitted coordinates and add only those that independently pass the same gate.
3. **Pruning/exactness:** resolve aliases and duplicates, remove grammar debris/invention, repair exact source copying, and repair semantic ordering.

Do not prefer the provisional row count, fewer rows, or more rows. Do not widen or narrow the admission gate because a candidate appeared or did not appear in the provisional output.

## Compounds

Build compounds only after units are final.

Create one compound for each materially distinct proposition or relation that is useful for reconnecting retained coordinates at lightweight grain.

For each compound:

- identify the proposition/relation first;
- include every retained unit that materially participates in that proposition;
- include a PLACE/TIME/LOCATOR frame only when that retained coordinate specifically governs the proposition;
- inherit a nearby frame only while the same independently indexed frame remains in force and the proposition actually depends on it;
- stop inheritance at a real frame/discourse transition;
- do not propagate a broad/global setting or frame merely because it is generally true;
- do not create multiple compounds that differ only by optional frame inheritance, subset choice, or quality-only detail;
- keep one proposition together and split genuinely different propositions;
- preserve source/semantic order of references.

A compound cannot compensate for a missing unit and cannot invent semantics.

## Apparatus boundary

The apparatus, not the worker, owns canonical IDs, deterministic numbering, exact-source validation, source-near tag validation, ordering enforcement, compound-reference validation, `_Q` construction, SQL-ready shaping, retries, evaluation, and failure handling.

The worker must not depend on hidden canonical IDs, archetypes, evaluator criteria, expected counts, or scored outputs.

## Forbidden work

Do not perform APA parsing, protected-thread analysis, psychological interpretation, scoring, promotion, APA-ID creation, executive analysis, or Oval Office research writes.

Never present a candidate inventory as established truth.
