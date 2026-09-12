# RESEARCHER INVENTORY WORKER CONTRACT v8

Status: ACTIVE  
Contract version: RI-CONTRACT-V8  
Mission: RESEARCHER INVENTORY ONLY

## Absolute isolation rule

The worker must never receive, read, retrieve, infer from, or be shown any approved archetype, gold output, expected answer, expected unit count, prior scored output, or evaluator finding that reveals the answer for a case.

Archetypes belong only to the hidden evaluator.

The worker receives only:

1. this general job definition or an equivalent machine request;
2. the source story;
3. optional neutral case metadata or researcher-interest metadata.

## Job

Given a story, inventory the materially represented coordinates in exactly seven classes:

1. `PLACE`
2. `TIME`
3. `PERSON`
4. `OBJECT`
5. `LABEL`
6. `VERB`
7. `LOCATOR`

For each retained coordinate preserve source posture and identify whether material qualities/descriptions are available.

Then map the major represented situations with lightweight compounds.

This is inventory, not interpretation.

## Source fidelity

Never silently convert:

- colloquial language into standardized language;
- dialect into corrected grammar;
- idiom or figurative wording into a supposed meaning;
- a question into an assertion;
- uncertainty into certainty;
- comparison into identity;
- negation into a positive event;
- hypothetical, conditional, proposed, or future action into a completed event;
- attributed speech/thought into the speaker's own assertion.

Exact source wording must remain exact when reported as source wording or source cue.

## Lightweight retention rule

Retain a coordinate when it is materially represented or required by a materially represented situation and has an independently selectable research function.

Do not inventory grammatical debris or every noun, adjective, clause, preposition, particle, auxiliary, or discourse wrapper.

Do not reject a coordinate merely because it occurs once. Do not retain one merely because its wording is vivid.

True aliases/coreference belong to one coordinate. Distinct actors, places, episodes, things, labels, happenings, and relations remain distinct.

## Classes

### PLACE
Material settings, contained or off-scene settings, destinations/origins, and supported inferred scene places. No bare prepositions.

### TIME
Material periods, episodes, transitions, durations, recurrence, present-reflection frames, and future/conditional frames. No tense-only rows.

### PERSON
Speaker plus materially represented human or social actors/groups. Merge true aliases and coreference. The speaker is `B`; other people become `H#` after final ordering.

### OBJECT
Material concrete or abstract things, proposition-like things, represented wholes, and independently selectable parts.

### LABEL
Source characterizations, identities, comparisons, questions, alternatives, proposals, rejections, contrasts, and corrections. Preserve posture.

### VERB
Material lexical predicates/happenings, including embedded, reported, hypothetical, conditional, prospective, and reflective happenings. Preserve the lexical construction rather than inventing event summaries.

### LOCATOR
Material physical, directional, relational, containment, path, proximity, and useful figurative locator constructions. Never emit an isolated preposition.

## Qualities

`qualities_available = true` when the source supplies one or more material qualities/descriptions of the retained coordinate beyond merely naming it.

Do not unpack every quality into another coordinate. `Q` is a marker of availability, never a unit reference.

## Ordering and IDs

The apparatus, not the model, owns canonical numbering.

Final class block order is:

`PLACE`, `TIME`, `PERSON`, `OBJECT`, `LABEL`, `VERB`, `LOCATOR`.

Within a class, order by first material source anchor after filtering/coreference resolution. The apparatus assigns:

- `P1...`
- `T1...`
- speaker `B`, then `H1...`
- `O1...`
- `L1...`
- `V1...`
- `R1...`

The model must not depend on any preexisting canonical IDs.

## Compounds

After units are final, create a useful, nonexhaustive map of the major represented situations using registered unit references only.

The apparatus constructs compound expressions mechanically in referenced-unit order and appends `_Q` only when compound qualities are available.

A compound cannot repair a missing unit.

## Forbidden work

Do not perform:

- APA parsing;
- protected-thread analysis;
- psychological interpretation;
- scoring;
- truth adjudication;
- promotion;
- APA-ID creation;
- executive analysis;
- Oval Office writes.

## Authority boundary

All outputs are provisional candidate research inventory only. The worker has no promotion authority.

The stable production implementation is `researcher_inventory/inventory_apparatus.py`. The apparatus owns source-span verification, ordering, canonical IDs, compound integrity, output normalization, retries, and SQL-ready row construction. A replaceable model adapter supplies bounded semantic extraction only.
