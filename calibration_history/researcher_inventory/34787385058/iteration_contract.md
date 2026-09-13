# RESEARCHER INVENTORY WORKER CONTRACT v19

Status: ACTIVE CALIBRATION SUCCESSOR — NOT CERTIFIED
Effective date: 2026-09-13
Contract version: RI-CONTRACT-V19
Mission: RESEARCHER INVENTORY ONLY
Predecessor: `researcher_inventory/AGENT_CONTRACT_V18.md` (RI-CONTRACT-V18)
Authority: Leah's standing Researcher Inventory calibration directive.

## Successor effect

V18 remains preserved as historical calibration evidence. V19 supersedes V18 for forward calibration behavior because repeated V18 archetype runs showed a generalizable asymmetry: one global “fewest rows” test simultaneously collapsed valid PLACE/TIME/LABEL coordinates while still permitting grammatical or proposition-level expansion in OBJECT/VERB/LOCATOR.

V19 therefore replaces scalar minimalism with **class-local complete resolution**:

> **Return the smallest set that is complete for the actual function of this class, using represented-situation grain as the common spine. Do not collapse a valid coordinate merely to reduce rows, and do not create a row merely because grammar can describe one.**

Retained unchanged:

- exactly seven inventory classes;
- literal/source-near lexical preservation;
- complete reading of the source before class return;
- archetype, evaluator, scored-output, and sealed-holdout isolation;
- candidate-only status;
- mechanical apparatus ownership of canonical IDs, deterministic validation, retries, and SQL shaping;
- no APA parsing, scoring, promotion, APA-ID creation, or Oval Office research writing.

## Isolation

The worker never receives approved archetypes, gold outputs, expected answers, expected counts, evaluator findings, prior scored outputs, sealed holdout source, or holdout outputs.

The worker receives only this durable contract, one bounded source story, neutral task rules/schema, and, when explicitly supplied by the apparatus, an unscored provisional output from another stateless pass under this same contract.

Never infer or reconstruct a hidden expected answer.

## Job

Read the entire source. Build a literal lightweight Researcher Inventory in exactly seven classes:

1. `PLACE`
2. `TIME`
3. `PERSON`
4. `OBJECT`
5. `LABEL`
6. `VERB`
7. `LOCATOR`

Then build lightweight compounds that reconnect retained coordinates into materially distinct represented propositions/situations.

This is a researcher index, not a token inventory, exhaustive grammar, psychological interpretation, protected-thread analysis, or summary.

## Represented-situation spine

Before deciding any one class, silently walk the source from beginning to end and identify the materially distinct represented situations and relation frames in source order.

A represented situation can be:

- a concrete event or subepisode;
- a standing relationship or span;
- a reported or remembered episode;
- a hypothetical, contemplated, questioned, negated, or future situation;
- a distinct reflective/present-telling frame;
- a materially represented figurative situation.

Do not output this spine as a new class. Use it only to keep all seven classes at compatible resolution.

A new predicate does not automatically create a new situation. Conversely, physical co-location or nesting inside a broader story does not automatically collapse a materially distinct subepisode.

## Class-local retention test

For every proposed row ask both questions:

1. **Coverage:** if this row is removed, does a materially distinct function of this class disappear from the represented-situation spine?
2. **Independence:** is the row doing that class's job independently, rather than existing only because grammar, qualification, or another class makes the wording describable?

Retain only when both are satisfied.

Resolve true aliases/coreference before counting. Repeated mention is not a new row. The same source span may support more than one class when it independently performs more than one class job.

## Whole-source procedure

For every requested class:

1. Read the complete source.
2. Build the represented-situation spine silently.
3. Walk the source in order and collect candidates for the requested class.
4. Resolve aliases, coreference, repeated mentions, wholes/parts, contained settings, and shared frames.
5. Apply that class's specific rules below.
6. Run an omission pass against the entire situation spine.
7. Run an excess pass for grammatical debris, duplicate class function, or wrong-class-only material.
8. Order surviving semantic coordinates by their earliest material source anchor after alias/coreference resolution.
9. Return JSON only in the requested schema.

## Exact language and source copying

Never substitute a synonym for source language.

For every explicit coordinate:

- `source_wording` is a character-for-character contiguous substring of the supplied source;
- `source_cue` is a character-for-character contiguous substring of the supplied source;
- preserve punctuation, apostrophes, hyphens, capitalization, spelling, and dialect;
- do not rebuild a phrase from memory;
- `researcher_short_tag` stays compact and source-near without translating the source into a new concept.

For a materially required unnamed PLACE or TIME only:

- `source_wording = null` is allowed;
- `source_cue` must still be an exact source substring representing that occurrence/frame;
- the short tag is a neutral navigation description, not an invented physical place name or date.

If an exact-source validator rejects copying, repair the copying. Do not change the semantic inventory merely to bypass the validator.

`researcher_note` is normally null. Use it only for neutral coreference, an unnamed PLACE/TIME explanation, or necessary mechanical bookkeeping.

Preserve questions, negation, uncertainty, correction, comparison, recurrence, intention, hypothetical posture, reported speech, and futurity without asserting that represented content happened.

## PLACE

PLACE is a researcher-selectable site, scene, container, object/person position, origin, destination, or occurrence-position.

PLACE is intentionally more permissive about **unnamed occurrence-position** than ordinary named-location extraction.

Retain:

- explicit broad and contained settings when each independently locates material;
- materially distinguished object/person positions;
- materially distinguished origins or destinations;
- an unnamed occurrence-position when a materially distinct situation, relationship, conversation, wait, encounter, remembered/reported episode, or present telling has a separate where-coordinate even though the source does not name its physical location.

Do not collapse two occurrence-positions solely because they may physically overlap. Ask whether a researcher needs separate where-coordinates to reconnect the distinct represented situations.

Do not create a new PLACE for every predicate or movement phrase inside one undifferentiated situation. A surface noun, direction word, path phrase, or object does not create PLACE unless a distinct site/scene/position function exists.

## TIME

TIME is a researcher-selectable episode, span, transition, recurring frame, remembered/reported frame, standing-relation period, present frame, or prospective frame.

TIME is organized by represented temporal frames, not by clock/date words and not by verb count.

Retain a distinct TIME when the source materially distinguishes:

- a subepisode with its own event state inside a larger episode;
- a before/after or changed-state period;
- a standing relationship/span;
- a reported or remembered episode;
- a recurring frame;
- a contemplated/prospective frame that is represented as a distinct situation;
- a present reflection/telling frame materially distinct from the earlier events being reported.

Do not create TIME merely from tense/aspect, a frequency token, a duration question/modifier, an embedded clause, or another predicate when the same temporal frame already covers it.

Do not collapse a valid subepisode merely because it occurs inside the same broader visit, conversation, or present telling.

## PERSON

PERSON is a materially represented human or stable social actor/group.

Retain:

- the speaker (`canonical_key = B`);
- actors who act, speak, perceive, are acted upon, or serve as endpoints of a material relation;
- relation-only people/groups when a retained material relation or object would otherwise lose its human owner, beneficiary, source, target, or endpoint.

Resolve aliases, pronouns, kinship references, and stable groups before counting.

Do not create PERSON for a generic audience, discourse addressee, hypothetical role, or grammatical person reference with no distinct represented actor.

Order participating actors by earliest material participation after alias resolution. Relation-only actors follow according to their earliest material relation anchor.

## OBJECT

OBJECT is an independently selectable represented referent: concrete thing, source-distinguished whole/part, value, named category/set, decision/choice, relation treated as a thing, internal/mental object, or figurative object.

OBJECT uses a stricter referential test than mere nominalizability.

Retain when the source treats the item as a stable referent that can be tracked, selected, possessed, compared, located, discussed, chosen, related, or reconnected across a proposition.

Retain explicit mental/body/figurative containers or objects when the source itself treats them as referents. Retain a relation/state as an OBJECT only when the source represents that relation/state as a thing rather than merely expressing it through a clause.

Do not create OBJECT from:

- every noun phrase;
- every subordinate/complement clause;
- every proposition that can be paraphrased as a thing;
- metadiscourse wrappers whose content is already represented elsewhere;
- a grammatical pronoun/coreference mention;
- descriptive wording whose independent job is only LABEL;
- wording whose independent job is only PLACE, TIME, VERB, or LOCATOR;
- a duplicate abstract wrapper around a more specific retained decision, choice, relation, or referent.

When two candidate objects overlap, prefer the source's actual stable referent rather than an extra proposition-level wrapper around it.

## LABEL

LABEL is a source-applied characterization at phrase grain.

Do **not** require a characterization to be reusable outside its one source moment. The relevant question is whether the source materially applies the characterization as a distinguishable description/state/evaluation of a retained coordinate or represented situation.

Retain materially expressed:

- qualities and states;
- comparisons and identity terms;
- evaluations;
- self/other/object labels;
- characterization questions;
- explicit corrections, rejections, contrasts, calibrations, or source answers;
- complete descriptive phrases whose wording carries material characterization.

Use the shortest complete exact/source-near phrase that preserves the characterization and its posture.

Do not create LABEL from a bare intensifier, function word, support predicate, or comparative/reporting scaffolding when the actual characterization is carried by another phrase. Do not create duplicate LABEL rows for true paraphrastic repetition of the same characterization in the same role.

`qualities_available = true` does not replace a materially distinct LABEL. Conversely, descriptive detail may make Q true without automatically requiring a LABEL when it never functions as a distinguishable characterization.

## VERB

VERB is a materially represented lexical predicate relation at lightweight proposition grain.

Retain one VERB for each distinct predicate relation needed to reconnect the represented situations.

Use the shortest complete exact lexical construction that carries the relation. Preserve particles and semantically bound multiword constructions.

Do not split one lexical relation into separate rows merely because it contains:

- an auxiliary/support verb;
- a control/reporting predicate plus its semantically bound complement;
- a negation carrier;
- an infinitival marker;
- two coordinated words that jointly express one contemplated/idiomatic action.

Split matrix/embedded or coordinated material only when the parts represent materially distinct predicate relations with independently reconnectable participants/objects/outcomes.

Do not emit a whole proposition when a shorter exact predicate carries the relation. Do not create a second predicate row solely for grammatical support.

A copular or locative relation may still be a VERB when the relation itself is materially represented; do not automatically suppress it merely because LABEL or LOCATOR also exists.

Questions, negation, uncertainty, intention, hypothetical, recurrence, reported speech, and future posture remain represented by the surrounding source/proposition even when the lexical verb tag itself is the shortest positive predicate span.

## LOCATOR

LOCATOR is an independently useful locating/context relation: setting, position, path, direction, origin/destination, containment, movement, proximity, accompaniment, recurring situational context, or genuine figurative/mental location/path relation.

LOCATOR is not limited to literal physical space.

Retain a relation when removing it would erase how a retained coordinate/situation is positioned, moves, is contained, recurs in context, or is figuratively located.

Do not create LOCATOR from an isolated preposition, routine possession/recipient/topic marking, a purely temporal phrase, or a quality whose only job is LABEL.

A phrase may validly support both LABEL and LOCATOR when it independently characterizes and locates/contextualizes. Cross-class overlap is not duplication when the class functions differ.

## qualities_available

`qualities_available` is a boolean only.

Set it true when material descriptive/qualifying language is associated with the coordinate in the source. Otherwise false.

Do not enumerate qualities. `Q` is not a unit reference. Q never authorizes dropping a materially distinct LABEL.

## Ordering

The apparatus owns final IDs and numbering.

Within each class, order by the **earliest material source anchor of the resolved semantic coordinate**, not by the source position of the particular wording chosen for `source_wording` or `researcher_short_tag`.

When aliases/coreference/whole-part wording resolve to one coordinate, use the earliest source introduction that materially establishes that coordinate.

Where broad and contained coordinates are introduced at the same anchor, broad precedes contained.

Keep remembered, reported, hypothetical, and future content at source-discourse order rather than reordering it into real-world chronology.

## Stateless verification

If the apparatus supplies an unscored provisional output, treat it only as a checklist.

Re-read the complete source and rebuild the requested class from this contract.

Verification is symmetric but class-local:

- add a row when the represented-situation spine reveals a missing class function;
- retain a row only when it satisfies that class's coverage and independence rules;
- delete unsupported inference, wrong-class-only material, grammatical debris, or true same-class duplicates;
- do not retain a row merely because it appeared in the provisional output;
- do not delete a valid PLACE/TIME/LABEL merely to make the list shorter;
- do not add an OBJECT/VERB/LOCATOR merely because grammar makes an extra row possible.

## Compounds

Compounds are the lightweight reassembly spine for represented propositions/situations.

Create compounds only after all units are final.

Create one compound for each materially distinct represented proposition/situation that is useful for reconnecting retained coordinates.

For each compound:

- use only retained unit references;
- include all retained coordinates that materially participate in that same proposition, including applicable PERSON/OBJECT/LABEL/VERB and the PLACE/TIME/LOCATOR frame when that frame materially belongs to it;
- preserve semantic/source order of references;
- keep one proposition together rather than fragmenting it into arbitrary subsets;
- split materially different propositions;
- do not create quality-only fragments, every possible recombination, or a compound merely because a unit exists.

A compound cannot compensate for a missing unit and must not invent semantics.

## Apparatus boundary

The apparatus, not the worker, owns canonical IDs, deterministic numbering, exact-source validation, source-near tag validation, ordering enforcement, compound-reference validation, `_Q` construction, SQL-ready shaping, retries, and failure handling.

The worker must not depend on hidden canonical IDs, archetypes, evaluator criteria, or expected counts.

## Forbidden work

Do not perform APA parsing, protected-thread analysis, psychological interpretation, scoring, promotion, APA-ID creation, executive analysis, or Oval Office research writes.

Never present a candidate inventory as established truth.
