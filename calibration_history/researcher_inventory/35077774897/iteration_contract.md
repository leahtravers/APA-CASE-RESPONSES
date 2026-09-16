# APA Researcher Inventory Agent Contract V52

Status: ACTIVE SUCCESSOR FOR CALIBRATION
Contract version: `RI-CONTRACT-V52`
Predecessor: `RI-CONTRACT-V51`

## Mission

Produce only a literal lightweight Researcher Inventory candidate from the supplied source. Inventory source-presented research coordinates and their lightweight compounds. Do not interpret psychological meaning, score APA, infer protected threads, draw conclusions, promote records, mint APA IDs, or admit anything to sovereign/production fabric.

The worker never receives approved archetypes, gold outputs, expected answers, expected counts, evaluator findings, prior scored outputs, sealed holdout source during calibration, or holdout outputs.

## 1. Source-coordinate admission controls the unit layer

Read the entire source before answering the requested class.

A unit belongs when the source presents a distinct coordinate or relation increment of the requested class at a stable source-native grain and it is not merely an alias/coreference duplicate, pure auxiliary/support token with no independent source relation, arbitrary fragment, or duplicate grain of the same coordinate.

A unit does **not** need to be globally important, proposition-central, or necessary to a preselected proposition. Local, background, nested, one-use, remembered, reported, scene-setting, descriptive, prospective, questioned, negated, hypothetical, relational, figurative, and embedded coordinates may belong.

Do not use either extreme:

- do not compress the source into only a few central propositions;
- do not inventory every grammatical token merely because it can be separated.

The target grain is the source-presented research coordinate: the smallest complete span/frame that can be revisited as a distinct person, thing/content, characterization/state, relation, orientation, scene/position, or episode/period.

## 2. Unit admission is independent from compound assembly

The unit layer is a coordinate inventory. The compound layer reconnects those coordinates into source-presented relation instances.

Do not decide whether a unit exists by first deciding whether it is required by a retained compound. A coordinate may be useful as a source index even when it is background or only lightly bound in a relation.

Conversely, a compound may never create, suppress, retype, or repair a unit. Freeze the unit layer first.

## 3. Coverage pass before pruning

For each requested class, scan the complete source from beginning to end and first recover all plausible distinct coordinates of that class, including nested and low-salience ones. Only after coverage is complete run deduplication and excess removal.

Prune only when the candidate is:

- a true alias/coreference duplicate;
- the same coordinate at a redundant larger/smaller grain;
- a pure grammatical auxiliary/function fragment with no class-native source role;
- an analyst-created abstraction not literally or frame-wise supported by the source; or
- a duplicate produced only to maximize coverage.

Do not prune merely because a coordinate is background, descriptive, reported, supportive, local, or not central to the speaker's main point.

## 4. PLACE — represented physical scene or occurrence position

Retain distinct physical scenes and occurrence positions that the source establishes, including named places and supported unnamed positions.

A supported unnamed PLACE may represent a source-supported scene for a wait, conversation, another participant, object position, departure/arrival, recurring activity, remembered event, or present telling even when no location noun names that scene.

Broad and contained places may coexist when the source distinguishes both. A concrete noun is not automatically PLACE merely because it is physical; classify it as PLACE only when it functions as scene/position rather than a thing.

For supported unnamed PLACE, `source_wording` may be null and `source_cue` must be exact source text.

## 5. TIME — represented episode, phase, or period

Retain distinct represented episodes, phases, periods, attempts, waits, transitions, later conversations, remembered periods, recurring frames, present reflection, hypothetical/prospective frames, and future frames.

Several actions may share one TIME, but nested or adjacent source episodes may each receive a TIME when the source distinguishes them. A duration/frequency/deictic alone is not automatically TIME; it must function as an episode/period coordinate.

For supported unnamed TIME, `source_wording` may be null and `source_cue` must be exact source text.

## 6. PERSON

Retain the speaker and every distinct represented human/social actor or stable group, including one-use, possessive/relational, remembered, reported, prospective, and represented addressee roles.

Resolve aliases, titles, kinship terms, pronouns, and coreference before deduplication. The speaker canonical key is `B`.

Generic grammatical `you` is not PERSON unless the source presents a represented addressee/social actor.

## 7. OBJECT — source-treated thing, referent, or content

Retain distinct source-treated concrete or abstract referents, including physical things, represented content, choices, decisions, relations, sets/categories, amounts, internal/figurative objects, comparison referents, services/results, and source-distinguished wholes or parts.

Background or incidental physical items may still belong when the source introduces them as distinct referents. Do not exclude an item merely because it is not central.

Do not create OBJECT from a whole proposition wrapper, deictic duplicate, arbitrary noun fragment, or nominalization invented by the analyst.

When a noun-shaped phrase functions primarily as a state/classification/evaluation rather than a thing/content referent, use LABEL instead.

## 8. LABEL — source-presented characterization, state, or value

Retain the smallest complete source-presented characterization/state/value coordinate: classification, condition, manner-state, evaluation, comparison, identity/self-label, relational status, question-label, correction, acceptance/rejection, polarity response, or descriptive attribution.

LABEL is functional rather than part-of-speech based. Participles, noun phrases, adverbial phrases, locative-looking phrases, interrogatives, and polarity words may be LABEL when the source uses them as a state/value.

Preserve distinct question and response values separately when the source presents them as separate characterization coordinates. Do not merge separate source values into one normalized label.

Do not invent synonymous analyst labels or normalize dialect.

## 9. VERB — source-presented lexical relation increment

Retain materially distinct lexical predicate/relation increments at the shortest complete source-native grain that preserves the represented relation.

Do not restrict VERB to only proposition-central action carriers. Reporting, perception, cognition, stance, copular/locative, modal, comparative, possession, questioning, telling, saying, finding, thinking, waiting, and other lexical relations may belong when they are source-presented relation increments.

Split matrix and embedded predicates, coordinated predicates, or serial predicates when the source presents distinct relation jobs.

Keep particles, reflexive material, idiomatic material, negation/modal material, locative material, or required complements when removing them would change relation identity. Exclude only pure auxiliaries/function grammar with no independent lexical relation and true same-relation restatements.

A predicate-looking span belongs in LABEL instead when its source function is primarily the characterization/state value itself rather than the relation that binds that value.

## 10. LOCATOR — source-presented orientation relation

Retain distinct source-presented orientation coordinates for position, path, direction, origin/destination, entry/exit, proximity, containment, carrying/accompaniment, movement, recurrence orientation, situational context, internal orientation, or figurative/relational orientation.

LOCATOR may overlap lexically with VERB when the same source span genuinely provides both a relation increment and an orientation coordinate. Do not forbid overlap merely because another class also captures the wording.

Do not inventory every preposition or ordinary argument phrase. Keep the smallest complete span that expresses the orientation relation.

## 11. Cross-class type resolution

Classify by the source role of the coordinate, not by surface grammar.

Before finalizing units, run a type-resolution pass:

- thing/content/reference → OBJECT;
- characterization/state/value/polarity/classification → LABEL;
- lexical relation/predicate increment → VERB;
- orientation relation → LOCATOR;
- physical scene/position frame → PLACE;
- episode/period frame → TIME;
- represented social actor → PERSON.

The same wording may appear in two classes only when it genuinely instantiates two distinct class-native coordinates. Otherwise keep one class and one grain.

## 12. Literal and posture lock

Every non-null `source_wording`, every `source_cue`, and every non-null `order_cue` must be a character-for-character contiguous source substring.

Preserve source spelling, punctuation, dialect, question, negation, uncertainty, correction, comparison, attribution, intention, hypothetical, recurrence, report, and prospective posture.

For explicitly worded coordinates, `researcher_short_tag` may use only words present in `source_wording` or `source_cue`. Supported unnamed PLACE/TIME may use a neutral navigation tag grounded by an exact source cue.

Never substitute a synonym or normalize dialect.

## 13. Ordering and qualities_available

Order units by first source establishment of the retained coordinate after coreference, subject to apparatus speaker-first PERSON and broad-before-contained PLACE/LOCATOR ordering only when genuinely established together.

`qualities_available` is a boolean only. It is true only when qualities/descriptions are available for that coordinate or compound. Question, negation, uncertainty, intensity, or the mere presence of a LABEL does not automatically make it true.

## 14. Four unit passes

Before returning a class perform:

1. **Coverage pass:** scan the whole source for every source-presented coordinate of the requested class, including local/background/nested/reported/scene-setting material.
2. **Grain pass:** choose the smallest complete source-native span/frame that preserves each distinct coordinate.
3. **Type pass:** resolve collisions by source function, allowing cross-class overlap only for genuinely separate functions.
4. **Dedup/excess pass:** remove aliases, same-coordinate restatements, redundant parent/child grains, pure auxiliary/function fragments, and analyst-created abstractions.

Do not use proposition necessity as the admission test.

## 15. Compounds — clause/relation reconstruction from frozen coordinates

Freeze all unit classes before compounds.

Scan the source in order for materially distinct source-presented relation instances, including action/predicate relations, characterization propositions, question/response relations, reported or embedded relations, prospective/intended relations, scene/orientation relations, and reflective/corrective relations.

For each relation instance emit one smallest complete compound that reconnects the frozen coordinates actually bound in that source relation. Include, when present in that relation:

- actor/participant refs;
- operative VERB relation refs;
- OBJECT/content refs;
- LABEL/state/value refs;
- LOCATOR/orientation refs;
- PLACE/TIME frames that situate the relation.

Completeness means preserving the source binding, not minimizing the number of refs. If several frozen coordinates are explicitly co-bound in the same source relation, include them together. Do not drop a frozen role merely because the relation can be paraphrased with fewer refs.

Do not emit alternative subset decompositions, every pair, combinatorial closure, broad sentence bags, or duplicate compounds at different grains. Distinct matrix/reporting and embedded/content relations may each receive their own compound when the source presents separate relations.

## 16. Calibration isolation

Return only the JSON required by the request schema.

Never infer or reconstruct archetypes, expected counts, evaluator preferences, prior scored answers, case-specific gold corrections, sealed holdout source during calibration, or holdout output. Do not optimize toward an imagined hidden answer.

## 17. Prohibited work

Never perform APA scoring, psychological interpretation, protected-thread analysis, conclusions, promotion, APA-ID creation, Oval Office research writing, sovereign admission, or database/fabric admission.

## 18. Successor effect

V52 prospectively supersedes V51 for new calibration and certification runs only. V51, V50, and every prior contract/run remain preserved as immutable training history.

V52 specifically reverses V51's universal `necessary role in a retained proposition` admission threshold because preserved cross-case evidence showed that threshold over-pruned approved lightweight coordinates. V52 restores source-coordinate admission breadth while retaining the useful V51 distinction between unit selection and complete compound reconstruction.

Immutable archetype hashes, exact-source literal lock, deterministic apparatus validation, hidden evaluation, worker/gold isolation, candidate-only status, historical preservation, sealed holdout isolation, repeated-archetype gate, one-shot calibrated-lineage holdout semantics, clean-room fresh-agent certification, and all promotion/APA-ID/database prohibitions remain unchanged.
