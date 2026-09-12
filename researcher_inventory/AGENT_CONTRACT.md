# RESEARCHER INVENTORY WORKER CONTRACT v9

Status: ACTIVE
Contract version: RI-CONTRACT-V9
Mission: RESEARCHER INVENTORY ONLY

## Isolation

The worker never receives or uses approved archetypes, gold outputs, expected answers, expected counts, evaluator findings, prior scored outputs, or sealed holdout outputs.

The worker receives only the general job rules, one source story, and optional neutral metadata.

## Job

Read the whole story. Inventory only these seven coordinate classes:

1. `PLACE`
2. `TIME`
3. `PERSON`
4. `OBJECT`
5. `LABEL`
6. `VERB`
7. `LOCATOR`

Then make a lightweight map of obvious represented situations using the retained coordinates.

This is an index, not an interpretation.

## Controlling rules

### 1. Literal language wins

Never substitute a synonym because it is convenient.
Never polish, normalize, translate, or explain source wording.
Preserve colloquial language, dialect, idiom, figurative language, questions, negation, uncertainty, comparison, attribution, and sequence.

If a field claims to contain source wording or a source cue, it must be exact source text.

### 2. A place can be unnamed

If an actual represented occurrence happened, it happened somewhere.
A `PLACE` may therefore exist even when no physical place noun or proper name appears.

For an unnamed place:

- `source_wording` is null;
- anchor it with an exact source cue from the occurrence;
- use a neutral descriptive tag only;
- never invent a location name.

### 3. A time can be unnamed

If an actual represented occurrence happened, it happened during an episode.
A `TIME` may therefore exist even when no clock time, date, or explicit temporal phrase appears.

For an unnamed time:

- `source_wording` is null;
- anchor it with an exact source cue from the occurrence;
- use a neutral episode tag only;
- never invent a date or clock time.

### 4. Qualities are only availability

`qualities_available` is a boolean.

Set it true when the source supplies material qualities or descriptions associated with the coordinate. Otherwise set it false.

Do not classify, interpret, score, or atomize those qualities merely to justify the boolean.
`Q` is never a unit reference.

### 5. Prefer actual represented people and happenings

Retain the speaker and actual represented human or social actors.
Merge true aliases and coreference.
Do not manufacture people from generic categories or rhetorical possibilities.

For `VERB`, prioritize materially represented happenings and lexical predicates that actually occur in the represented case.
Do not convert a negated, hypothetical, proposed, conditional, future, or merely possible action into a completed happening.

### 6. Sparse beats clever

Prefer fewer strong coordinates over speculative, redundant, decorative, grammatical, or interpretive coordinates.
When uncertain, do less.
Do not inventory every noun, adjective, clause, preposition, particle, auxiliary, or descriptive fragment.
Do not split one obvious thing into several grains unless the source represents independently selectable things.

## Class rules

### PLACE
Retain materially represented settings and supported inferred scene places. A place need not be physically named. Do not emit bare prepositions.

### TIME
Retain materially distinct occurrence or episode times. A time need not be a point on a clock or calendar. Do not emit tense alone.

### PERSON
Retain the speaker plus actual represented people or social actors. Merge aliases/coreference. The speaker is `B`; code assigns other `H#` references.

### OBJECT
Retain materially represented concrete or abstract things that are independently useful. Prefer stronger wholes over incidental descriptive fragments.

### LABEL
Retain independently useful source characterizations, identities, comparisons, questions, contrasts, proposals, rejections, and corrections. Preserve posture exactly. Do not translate labels into synonyms or inferred meanings.

### VERB
Retain materially represented lexical happenings/predicates. Preserve source lexical wording. Do not invent event summaries.

### LOCATOR
Retain materially useful spatial, directional, containment, path, proximity, or relational locator constructions. Preserve exact wording. Do not emit isolated prepositions.

## Mechanical boundary

The apparatus, not the worker, owns:

- final class ordering;
- canonical IDs;
- source-span validation;
- alias survivor mechanics;
- deterministic ordering;
- compound reference validation;
- `_Q` construction;
- SQL-ready row shaping;
- retries and failure handling.

The worker must not depend on any preexisting canonical IDs.

## Compounds

After units are final, map only obvious major represented situations.
Use registered unit references only.
Prefer fewer useful situation bundles over many overlapping pairs.
A compound cannot repair a missing unit.

## Forbidden work

Do not perform APA parsing, protected-thread analysis, psychological interpretation, scoring, promotion, APA-ID creation, executive analysis, or Oval Office writes.

Never present a candidate inventory as established truth.
