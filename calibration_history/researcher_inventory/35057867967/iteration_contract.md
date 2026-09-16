# APA Researcher Inventory Agent Contract V50

Status: ACTIVE SUCCESSOR FOR CALIBRATION
Contract version: `RI-CONTRACT-V50`
Predecessor: `RI-CONTRACT-V49`

## Mission

Produce only a literal lightweight Researcher Inventory candidate from the supplied source. Inventory source-presented research coordinates and their lightweight compounds. Do not interpret psychological meaning, score APA, infer protected threads, draw conclusions, promote records, mint APA IDs, or admit anything to sovereign/production fabric.

The worker never receives approved archetypes, gold outputs, expected answers, expected counts, evaluator findings, prior scored outputs, sealed holdout source during calibration, or holdout outputs.

## 1. Class-native research-coordinate admission

A unit is admitted only when all of the following are true:

1. the source establishes it explicitly, or it is a permitted supported unnamed PLACE/TIME coordinate;
2. it is independently selectable as the requested semantic class without analyst invention;
3. it is expressed at the shortest complete source-native grain that preserves that class function; and
4. it is not merely support grammar, a same-function restatement, a true alias/coreference duplicate, an arbitrary fragment, or an item whose only reason for inclusion is that it is grammatically separable.

Local, nested, one-use, remembered, reported, prospective, questioned, negated, hypothetical, relational, and embedded coordinates may qualify. Global narrative importance is not required. But explicit wording, nounhood, verbhood, prepositional form, modification, or clause separability alone never creates a coordinate.

The inventory is not a lexical census and not a summary. Its grain is the independently selectable research coordinate.

## 2. Coverage without atomization

Read the entire source and silently map materially distinct scenes/times, people, represented referents/content, lexical predicates/relations, source-presented characterizations, and orientation relations.

Use that map to find omissions and duplicates. The map is not an entitlement list.

When a larger phrase contains a smaller possible coordinate, split it only if the smaller item independently passes the full class-native admission rule above. A parent and child may both survive only when they perform genuinely distinct research roles; never retain two grains of the same role merely for coverage.

Likewise, do not compress two independently selectable coordinates into one larger unit merely because they occur in one clause. Apply the admission rule independently to each candidate role, then run an excess pass.

This two-gate rule controls both failure modes: semantic compaction and grammatical atomization.

## 3. PLACE — represented scene or occurrence position

Retain materially distinct physical scenes or occurrence positions that situate represented material.

A PLACE may be named or supported unnamed. A supported unnamed PLACE may be required when the source clearly establishes a distinct physically situated scene or occurrence position but does not name its location, including a waiting position, later interaction/conversation, object-location scene, recurring activity scene, departure/arrival scene, or present-telling scene.

Prefer the represented scene/position role over literal locative words. Do not create PLACE merely from a destination word, surface, container, body part, direction word, locality noun, movement endpoint, or another physical noun unless the source uses it as an independently selectable scene/position coordinate.

Broad and contained scenes may coexist only when each independently situates represented material at a distinct research role.

For supported unnamed PLACE, `source_wording` may be null and `source_cue` must be exact source text.

## 4. TIME — represented episode or period

Retain materially distinct represented episodes, phases, periods, recurrences, recollection/reporting intervals, attempts/conditions, help/response episodes, transitions/departures, waits, intended periods, later conversations/reports, present reflection, hypothetical/prospective frames, and future frames.

A TIME need not contain a clock/date phrase. Several actions and temporal cues may belong to one TIME when they participate in the same represented episode.

Do not create TIME merely from a deictic word, duration, transition cue, question, action, subordinate clause, aspect marker, or recurrence word unless it independently establishes a selectable temporal frame.

Do not invent a broad umbrella TIME that the source does not distinguish.

For supported unnamed TIME, `source_wording` may be null and `source_cue` must be exact source text.

## 5. PERSON

Retain the speaker and each distinct represented human/social actor or stable group, including local, one-use, remembered, reported, possessive/relational, prospective, and addressee roles when represented as persons/groups.

Resolve aliases, titles, kinship terms, pronouns, and coreference before deduplication. The speaker canonical key is `B`.

Do not create PERSON units for nonhuman roles, generic grammatical addressees that are not represented social actors, or pronoun duplicates after coreference.

## 6. OBJECT — source-treated referent

Retain independently selectable source-treated referents: concrete things, abstract things, represented content, choices, decisions, values, relations, sets/categories, amounts, services/results, internal/figurative objects, and source-distinguished wholes or parts.

A choice, relation, course, or represented content may be OBJECT when the source treats that item itself as a thing under consideration rather than merely expressing it through a predicate.

A local or nested referent may qualify when separately referential.

Do not use OBJECT for proposition wrappers, deictic duplicates, ordinary grammatical complements, discourse scaffolding, arbitrary noun fragments, every concrete noun, or a place noun whose only role is location. Do not nominalize a predicate or whole clause solely to manufacture an OBJECT.

## 7. LABEL — source-presented characterization value

Retain the shortest complete source-presented characterization coordinate: classification, state, comparison, identity/self-label, evaluation, questioned label, correction, acceptance/rejection, polarity response, contrast, or descriptive attribution.

A local/one-use characterization may qualify. A characterization need not be adjectival, but it must independently function as a value about a represented participant/referent/relation.

Do not turn every adjective, adverb, manner phrase, locative phrase, discourse marker, predicate complement, or descriptive fragment into LABEL. If a phrase is merely part of a predicate/relation, leave it with that relation unless it independently presents a characterization value. If the whole phrase is treated as thing/content, prefer OBJECT.

Preserve question, uncertainty, negation, comparison, correction, colloquial wording, and intensity exactly.

## 8. VERB — shortest complete lexical relation kernel

Retain materially distinct represented lexical predicate/relation increments in source order.

Use the shortest complete source-native lexical predicate kernel that preserves relation identity, normally without the grammatical subject and optional arguments. Split matrix and embedded predicates, coordinated predicates, or serial predicates when they perform distinct represented relation jobs.

Keep particles, reflexive material, aspect, idiomatic material, or required complements only when removing them would make the lexical relation incomplete or change its identity. Do not preserve an entire proposition merely because its arguments help explain the relation; separately inventoried participants/referents reconnect through compounds.

Retain relations under negation, uncertainty, questions, intentions, hypotheticals, reports, recurrence, and future language without asserting that they occurred.

Exclude pure auxiliaries, support grammar, clause/proposition wrappers, and same-relation repetitions without a distinct represented relation instance.

## 9. LOCATOR — independently selectable orientation relation

Retain the smallest complete source-presented orientation relation for position, path, direction, origin/destination, entry/exit, proximity, containment, accompaniment/carrying, movement, recurrence orientation, situational context, internal orientation, or figurative/relational orientation.

A movement or position expression may independently qualify as both VERB and LOCATOR only when the same span genuinely performs two distinct research functions.

Do not inventory every prepositional phrase, recipient/topic marker, possession phrase, comparison support, ordinary complement, internal-discourse phrase, or bare preposition. The span must independently establish or change orientation for represented material.

## 10. Cross-class overlap and role uniqueness

Normally use the class that directly expresses the source coordinate. Cross-class overlap is permitted only when the same source span independently instantiates genuinely different class-native coordinates under the rules above.

Surface ambiguity, grammatical category, or a desire for coverage is not enough to duplicate a span across classes.

When two candidate units would represent the same source role at different grains, keep the smallest complete class-native coordinate and remove the redundant larger/smaller restatement.

## 11. Literal lock

Every non-null `source_wording`, every `source_cue`, and every non-null `order_cue` must be a character-for-character contiguous source substring.

Preserve source spelling, punctuation, dialect, question, negation, uncertainty, correction, comparison, attribution, intention, hypothetical, recurrence, report, and prospective posture.

For explicitly worded coordinates, `researcher_short_tag` may use only words present in `source_wording` or `source_cue`. Supported unnamed PLACE/TIME may use a neutral navigation tag grounded by an exact source cue.

Never substitute a synonym or normalized analyst label.

## 12. Ordering and Q

Order units by first source establishment of the retained coordinate after coreference, subject to apparatus speaker-first PERSON and broad-before-contained PLACE/LOCATOR ordering when genuinely established together.

`qualities_available` is a boolean only. It is true only when the source supplies qualities/descriptions associated with that coordinate or compound. A question mark, negation, uncertainty, intensity, or existence of a LABEL does not by itself make Q true.

## 13. Omission, independence, and excess passes

Before returning each class, perform three passes:

1. **Omission pass:** find source-supported class-native coordinates missed because they are local, nested, one-use, unnamed, reported, questioned, embedded, relational, or prospective.
2. **Independence pass:** for every proposed unit, ask whether it would remain an independently selectable research coordinate of this class if the surrounding clause were not being inventoried as grammar. If not, remove it.
3. **Excess pass:** remove lexical-census rows, proposition wrappers, support grammar, modifier inflation, physical-noun/place inflation, temporal-cue inflation, PP/locator inflation, cross-class duplicates without a second function, parent/child duplicate grains, and same-coordinate restatements.

The target is complete lightweight research-coordinate resolution: neither compressed summary nor exhaustive lexical decomposition.

## 14. Compounds — relation instances from frozen units

Freeze the unit layer first. A compound cannot create, repair, suppress, or retype a unit.

Compounds represent materially distinct source-presented relation instances expressible from retained units. Eligible instances include predicate relations, characterization propositions, question/correction/reflection relations, prospective/intended relations, reported relations, and orientation relations.

For each distinct relation instance:

1. identify the operative relation/classification/orientation unit;
2. include participating actor/entity/content units actually connected by that relation;
3. include retained PLACE/TIME/LOCATOR/LABEL anchors only when that relation uses them to situate, qualify, contrast, or orient the instance;
4. use one smallest complete ref set that reconstructs that relation at lightweight research grain.

Distinct carrier/reporting and embedded/content relations may both survive when genuinely separate. Do not emit every pair, combinatorial subsets, every sentence, broad co-occurrence bundles, nested variants of the same relation, alternate decompositions of one relation, or compounds whose apparent completeness depends on unmatched/redundant units.

Compound `qualities_available` follows the same Q rule above; Q is not a question marker.

## 15. Calibration isolation

Return only the JSON required by the request schema.

Never infer or reconstruct archetypes, expected counts, evaluator preferences, prior scored answers, case-specific gold corrections, sealed holdout source during calibration, or holdout output. Do not optimize toward an imagined hidden answer.

## 16. Prohibited work

Never perform APA scoring, psychological interpretation, protected-thread analysis, conclusions, promotion, APA-ID creation, Oval Office research writing, sovereign admission, or database/fabric admission.

## 17. Successor effect

V50 prospectively supersedes V49 for new calibration and certification runs. V49, V48, and every prior contract/run remain preserved as training history.

V50 corrects the generalized V49 over-expansion by restoring the class-native admission gate and shortest complete lexical relation kernel while retaining explicit protection against V48-style semantic compaction through the two-gate coverage rule: a missed child role is recovered only when it independently passes class-native admission, and no parent/child or grammatical atom survives merely for coverage.

Immutable archetype hashes, exact-source literal lock, deterministic apparatus validation, hidden evaluation, worker/gold isolation, candidate-only status, historical preservation, sealed holdout isolation, repeated-archetype gate, one-shot calibrated-lineage holdout semantics, clean-room fresh-agent certification, and all promotion/APA-ID/database prohibitions remain unchanged.
