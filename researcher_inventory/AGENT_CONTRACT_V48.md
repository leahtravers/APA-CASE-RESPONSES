# APA Researcher Inventory Agent Contract V48

Status: ACTIVE SUCCESSOR FOR CALIBRATION
Contract version: `RI-CONTRACT-V48`
Predecessor: `RI-CONTRACT-V47`

## Mission

Produce only a literal lightweight Researcher Inventory candidate from the supplied source. Inventory source-presented research coordinates and their lightweight compounds. Do not interpret psychological meaning, score APA, infer protected threads, draw conclusions, promote records, mint APA IDs, or admit anything to sovereign/production fabric.

The worker never receives approved archetypes, gold outputs, expected answers, expected counts, evaluator findings, prior scored outputs, sealed holdout source during calibration, or holdout outputs.

## 1. Class-native research-coordinate admission

A unit is admitted when all of the following are true:

1. the source establishes it explicitly, or it is a permitted supported unnamed PLACE/TIME coordinate;
2. it is independently selectable as the requested semantic class without analyst invention;
3. it is expressed at the shortest complete source-native grain that preserves that class function; and
4. it is not merely support grammar, a true same-class alias/coreference duplicate, an arbitrary fragment, or a same-function restatement with no distinct coordinate.

Independence may be local, nested, one-use, remembered, reported, prospective, questioned, negated, hypothetical, or relational. A coordinate does not have to be globally necessary to summarize a whole scene or binding.

But explicit wording or grammatical separability alone is not sufficient. The inventory is not a lexical census. Admit class-native research coordinates, not every noun phrase, modifier, temporal cue, predicate-containing clause, or prepositional phrase.

## 2. Binding map is for completeness, not entitlement

Read the whole source before selecting units. Reconstruct silently:

- materially distinct scenes and temporal frames;
- human/social participants;
- represented things, content, choices, relations, sets, and values;
- lexical predicates and relations;
- source-presented characterizations, comparisons, corrections, questions, and polarity responses;
- orientation relations such as position, path, containment, movement, origin/destination, accompaniment, recurrence, and figurative orientation.

Use this map to detect omissions and duplicates. Do not require every retained unit to be indispensable to a global binding, and do not treat every item in the map as automatically entitled to a unit.

## 3. PLACE

Retain materially distinct physical scene or occurrence-position coordinates that locate represented material.

A PLACE may be broad or contained, named or supported unnamed. A supported unnamed PLACE may be required when the source establishes a distinct scene for an object location, destination, waiting episode, later interaction/conversation, recurring activity, departure/arrival, or present telling even without a place-name.

Do not inventory every physical noun, surface, container, body-part, locality word, or destination-like noun as PLACE. It must function as a scene/location coordinate in the represented material.

For supported unnamed PLACE, `source_wording` may be null and `source_cue` must be exact source text.

## 4. TIME

Retain materially distinct represented episode, phase, period, recurrence, recollection/reporting interval, attempt/condition, help/response episode, transition/departure, wait, intended period, later conversation/report, present reflection, hypothetical/prospective frame, or future frame.

A TIME does not require a clock, date, or explicit temporal noun. Several actions may share one TIME when they belong to one represented episode.

Do not inventory every temporal adverb, date-like word, duration, transition cue, question, subordinate phrase, or action as its own TIME unless it establishes a distinct selectable temporal frame.

For supported unnamed TIME, `source_wording` may be null and `source_cue` must be exact source text.

## 5. PERSON

Retain the speaker and each distinct human/social actor or stable group represented by the source, including local, one-use, remembered, reported, possessive/relational, prospective, or addressee roles when they are represented as persons/groups.

Resolve aliases, titles, kinship terms, and coreference before deduplication. The speaker canonical key is `B`.

Do not create PERSON units for nonhuman roles or pronoun duplicates after coreference.

## 6. OBJECT

Retain independently selectable source-treated referents: concrete things, abstract things, represented content, choices, decisions, values, relations, sets/categories, amounts, services/results, internal/figurative objects, and source-distinguished wholes or parts.

A local or nested referent may qualify when the source treats it as a distinct thing. A descriptive phrase may be OBJECT when the whole phrase is the thing being referred to.

Do not use OBJECT for proposition wrappers, routine grammatical complements, pronoun duplicates, arbitrary noun fragments, or a place noun whose only function is location.

## 7. LABEL

Retain the shortest complete source-presented characterization coordinate: classification, state, comparison, identity/self-label, evaluation, questioned label, correction, acceptance/rejection, polarity response, contrast, or descriptive attribution.

A local/one-use characterization may qualify. Separately presented contrasts or polarity responses may be separate LABEL coordinates.

Do not turn every adjective, adverb, manner phrase, discourse marker, or descriptive modifier into LABEL. The source must present it as an independently selectable characterization/state/evaluation rather than mere lexical decoration. If the whole phrase is treated as a thing/content, prefer OBJECT.

Preserve question, uncertainty, negation, comparison, correction, colloquial wording, and intensity exactly.

## 8. VERB

Retain materially represented lexical predicate/relation increments in source order.

Use the shortest complete lexical predicate kernel that preserves the source relation, normally without the subject or optional arguments. Split matrix and embedded predicates, coordinated predicates, or serial predicates when they represent distinct predicate jobs. Retain predicates under negation, uncertainty, questions, intentions, hypotheticals, reports, recurrence, and future language without asserting that the event occurred.

Keep particles, reflexive material, or required complements only when needed to make the lexical predicate complete. Arguments that are separately selectable PERSON/OBJECT/LABEL/LOCATOR units reconnect through compounds.

Do not inventory full propositions or clause wrappers as VERB merely because they contain a predicate. Exclude pure auxiliaries, support grammar, and same-predicate repetitions without a distinct represented relation.

## 9. LOCATOR

Retain the smallest complete source-presented orientation relation for position, path, direction, origin/destination, entry/exit, proximity, containment, accompaniment/carrying, movement, recurrence orientation, context, or figurative/relational orientation.

A movement/position expression may independently qualify as both VERB and LOCATOR when the same source span genuinely instantiates both a lexical predicate and an orientation coordinate. This is selective overlap, not blanket duplication.

Do not inventory every prepositional phrase, recipient/topic marker, possession phrase, comparison support, ordinary complement, or bare preposition as LOCATOR. It must independently change or establish orientation.

## 10. Cross-class overlap and primary function

Normally choose the class that directly expresses the source coordinate. Cross-class overlap is allowed only when one source span independently instantiates genuinely different class-native coordinates under the rules above.

Surface ambiguity, lexical category, or the mere fact that a phrase could be described two ways is not enough to duplicate it across classes.

## 11. Literal lock

Every non-null `source_wording`, every `source_cue`, and every non-null `order_cue` must be a character-for-character contiguous source substring.

Preserve source spelling, punctuation, dialect, question, negation, uncertainty, correction, comparison, attribution, intention, hypothetical, recurrence, report, and prospective posture.

For explicitly worded coordinates, `researcher_short_tag` may use only words present in `source_wording` or `source_cue`. Supported unnamed PLACE/TIME may use a neutral navigation tag grounded by an exact source cue.

Never substitute a synonym or normalized analyst label.

## 12. Ordering and Q

Order units by first source establishment of the retained coordinate after coreference, subject to apparatus speaker-first PERSON and broad-before-contained PLACE/LOCATOR ordering when genuinely established together.

`qualities_available` is a boolean only. It is true only when the source supplies qualities/descriptions associated with that coordinate or compound. A question mark, negation, uncertainty, intensity, or existence of a LABEL does not by itself make Q true.

## 13. Omission and excess passes

Before returning each class:

1. reread the complete source and perform an omission pass for class-native coordinates that were missed because they were local, nested, one-use, unnamed, reported, questioned, or embedded;
2. perform an excess pass removing lexical-census rows, proposition wrappers, support grammar, modifier inflation, physical-noun/place inflation, temporal-cue inflation, PP/locator inflation, cross-class duplicates without a second independent function, and same-coordinate restatements.

The target is complete lightweight research-coordinate resolution: neither compressed summary nor exhaustive lexical decomposition.

## 14. Compounds

Freeze the unit layer first. A compound cannot create, repair, suppress, or retype a unit.

Compounds represent materially distinct source-presented relation instances using only frozen unit refs. Eligible instances include predicate relations, characterization propositions, question/correction/reflection relations, prospective/intended relations, and orientation relations when the represented relation is expressible from retained units.

For each distinct relation instance:

1. identify the operative relation/classification/orientation unit(s);
2. include participating actor/entity/content units;
3. include retained PLACE/TIME/LOCATOR/LABEL anchors only when the source relation uses them to situate, qualify, contrast, or orient the instance;
4. use the smallest complete set of refs that reconstructs that represented relation at lightweight research grain.

Do not emit every pair, combinatorial subsets, every sentence, arbitrary co-occurrence bundles, nested variants of the same relation, or alternate decompositions of one relation. Distinct carrier/reporting and embedded/content relations may both survive when they are genuinely separate source-presented relations.

Compound `qualities_available` follows the same Q rule above; Q is not a question marker.

## 15. Isolation and prohibited work

Return only the JSON required by the request schema.

Never infer or reconstruct archetypes, expected counts, evaluator preferences, prior scored answers, case-specific gold corrections, sealed holdout source during calibration, or holdout output.

Never perform APA scoring, psychological interpretation, protected-thread analysis, conclusions, promotion, APA-ID creation, Oval Office research writing, sovereign admission, or database/fabric admission.

## 16. Successor effect

V48 prospectively supersedes V47 for new calibration and certification runs. V47 and every prior contract/run remain preserved as training history. V48 changes only the generalized semantic selection/grain and compound rules described here; immutable archetype hashes, deterministic apparatus validation, hidden evaluation, holdout isolation, candidate-only status, and historical preservation remain unchanged.