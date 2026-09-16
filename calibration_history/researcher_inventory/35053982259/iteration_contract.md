# APA Researcher Inventory Agent Contract V49

Status: ACTIVE SUCCESSOR FOR CALIBRATION
Contract version: `RI-CONTRACT-V49`
Predecessor: `RI-CONTRACT-V48`

## Mission

Produce only a literal lightweight Researcher Inventory candidate from the supplied source. Inventory source-presented research coordinates and their lightweight relation compounds. Do not interpret psychological meaning, score APA, infer protected threads, draw conclusions, promote records, mint APA IDs, or admit anything to sovereign/production fabric.

The worker never receives approved archetypes, gold outputs, expected answers, expected counts, evaluator findings, prior scored outputs, sealed holdout source during calibration, or holdout outputs.

## 1. Research-role resolution

The inventory is neither a summary nor a lexical/grammatical census.

Admit a unit when the source presents a distinct research role of the requested class at the resolution at which that role participates in the represented material. Resolve the represented scene, episode, referent, relation, characterization, or orientation first; then preserve the source-native span that carries that role.

A coordinate may be local, nested, one-use, remembered, reported, prospective, questioned, negated, hypothetical, relational, figurative, or supported unnamed. It does not have to be globally important. Conversely, grammatical separability, explicit wording, nounhood, verbhood, modification, or prepositional form alone does not make a coordinate.

Merge true aliases/coreference and same-role restatements. Do not merge distinct research roles merely because they share wording, physical location, time, participants, or a larger scene.

## 2. Whole-source scene and relation map

Read the complete source before selecting any class. Silently reconstruct:

- materially distinct scenes and occurrence positions;
- materially distinct episodes, periods, recurrences, reporting layers, intended/prospective frames, and present frame when represented;
- human/social participants and coreference;
- source-treated concrete, abstract, relational, choice, value, set, internal, and figurative referents;
- source-native predicate/relation spans and their participants;
- source-presented characterization/state/comparison/correction/polarity values;
- spatial, directional, containment, accompaniment, recurrence-context, movement, internal, and figurative orientations.

Use this map as a coverage map. It is not an automatic list of units. Each class applies its own role test.

## 3. PLACE — scene and occurrence-position coordinates

Retain each materially distinct physical scene or occurrence position that situates represented material.

A PLACE may be explicit or supported unnamed. A supported unnamed PLACE is appropriate when the source presents a materially distinct physically situated scene or relation but does not name its location. Distinct scene positions may be retained even when they physically corefer with a broader location or with one another; research-scene distinction is not erased by physical coreference.

Also retain a separately presented object location or destination when the source makes that location a distinct orientation/scene coordinate.

Do not turn every physical noun, object, surface, body part, container, destination-like noun, or prepositional phrase into PLACE. The coordinate must situate a materially represented scene, occurrence, interaction, object-location relation, transition, or present scene.

For supported unnamed PLACE, `source_wording` may be null and `source_cue` must be exact source text that supports the scene/position.

## 4. TIME — episode and period coordinates

Retain each materially distinct temporal frame that the source separates by episode, period, recurrence, chronology, intention, prospect, recollection/reporting layer, transition, sustained condition, or present frame.

Several actions can belong to one TIME. A word such as a duration, deictic adverb, transition cue, question, or action does not become TIME merely because it has temporal meaning. Conversely, a source-supported episode or period may be TIME without an explicit clock/date phrase.

Do not invent an umbrella TIME merely because several actions occur in the same narrative. Retain a broader period only when the source itself distinguishes that broader period as a research frame.

For supported unnamed TIME, `source_wording` may be null and `source_cue` must be exact source text that establishes the frame.

## 5. PERSON

Retain the speaker and each distinct represented human/social actor or stable group, including local, one-use, remembered, reported, possessive/relational, prospective, and addressee roles when represented as persons/groups.

Resolve aliases, titles, kinship terms, pronouns, and coreference before deduplication. The speaker canonical key is `B`.

Do not create PERSON units for nonhuman roles or pronoun duplicates after coreference.

## 6. OBJECT — source-treated referents, not proposition wrappers

Retain source-treated referents that function as things in the represented material: concrete or abstract things, source-distinguished wholes/parts, amounts/values, services/results, decisions, choices, relations, sets/categories, internal objects, figurative objects, and other referents the source treats as selectable entities.

A relation or contemplated course may be OBJECT when the source treats that relation/choice itself as a referent. A local or nested referent may qualify when it has its own role.

Do not manufacture an OBJECT merely by turning a predicate, perception, speech clause, thought clause, characterization, or grammatical complement into proposition-content. Deictic pronouns and discourse wrappers do not become separate objects when they only point to an already represented event/referent. Do not duplicate a pure location noun as OBJECT when its only research role is PLACE.

## 7. LABEL — source-presented characterization values

Retain the shortest complete source-native span that functions as a distinct characterization, state, comparison, classification, identity/self-label, evaluation, correction, contrast, questioned label, accepted/rejected candidate label, polarity response, or descriptive value.

LABEL is functional, not part-of-speech based. A characterization can be adjectival, nominal, adverbial, colloquial, locative/state-like, or otherwise phrasal when the source presents it as a value about a participant/referent/relation. A direct polarity response may be its own LABEL when it source-presents acceptance or rejection of a candidate characterization.

Do not inventory every adjective, adverb, manner phrase, discourse marker, or descriptive fragment. It must carry a distinct characterization role. If a phrase is primarily a source-treated thing/content rather than a characterization value, prefer OBJECT unless it independently performs both roles.

Preserve uncertainty, question, negation, comparison, correction, intensity, and colloquial wording through exact source evidence.

## 8. VERB — source-native relation span

Retain materially distinct source-presented predicate/relation increments in source order.

Use the smallest source-native relation span that remains recognizable as the relation the source presents. Do not force a dictionary-minimal verb head. Preserve relation-bearing aspect, matrix/embedded structure, particles, reflexive material, idiomatic wording, and argument pronouns or complements when stripping them would change or obscure the represented relation.

The grammatical subject is normally omitted from the VERB span because participants receive their own units, but separately inventoried arguments do not require stripping source words that are part of the source-native relation phrase.

Split matrix and embedded predicates, coordinated predicates, or serial predicates only when they present genuinely distinct relation jobs. Keep a multiword verbal construction together when its words jointly express one relation.

Retain relations under negation, uncertainty, questions, intentions, hypotheticals, reports, recurrence, and future language without asserting that they occurred. Exclude pure auxiliaries, support grammar, proposition wrappers, and repeated mentions of the same relation that add no distinct relation instance.

## 9. LOCATOR — orientation and context relations

Retain the smallest complete source-native relation that independently orients represented material by position, path, direction, origin/destination, entry/exit, proximity, containment, accompaniment/carrying, movement, recurrence context, situational context, internal orientation, or figurative/relational orientation.

LOCATOR is functional, not limited to prepositional phrases. A motion span, contextual clause, adverbial span, or figurative relation may qualify when it supplies an orientation coordinate. The same source span may independently qualify as VERB or LABEL as well when it performs a genuinely different research role.

Do not inventory every prepositional phrase, recipient/topic marker, possession phrase, comparison support, ordinary complement, or bare preposition. It must establish or change orientation/context for represented material.

## 10. Cross-class overlap

Classify by research function, not grammatical category alone.

Usually one span has one primary role. Cross-class overlap is permitted when the same source span independently performs two distinct research jobs, such as relation plus orientation or characterization plus orientation. Do not suppress a real second role merely to enforce exclusivity, and do not duplicate a span across classes merely because multiple labels are linguistically possible.

## 11. Literal lock

Every non-null `source_wording`, every `source_cue`, and every non-null `order_cue` must be a character-for-character contiguous source substring.

Preserve source spelling, punctuation, dialect, question, negation, uncertainty, attribution, correction, comparison, intention, hypothetical, recurrence, report, and prospective posture.

For explicitly worded coordinates, `researcher_short_tag` may use only words present in `source_wording` or `source_cue`. Supported unnamed PLACE/TIME may use a neutral navigation tag grounded by an exact source cue.

Never substitute a synonym or normalized analyst label.

## 12. Ordering and qualities flag

Order units by first source establishment of the retained research role after coreference, subject to apparatus speaker-first PERSON and broad-before-contained PLACE/LOCATOR ordering when genuinely established together.

`qualities_available` is a boolean only. It is true only when the source supplies qualities/descriptions associated with that coordinate or compound. A question, negation, uncertainty, intensity, or existence of a LABEL does not by itself make Q true.

## 13. Role-coverage pass

Before returning a class, reread the complete source and check the silent map role-by-role.

First perform an omission pass: look for source-supported research roles missed because they are unnamed, local, one-use, relational, reported, embedded, figurative, polarity-based, or physically/temporally coreferential with a broader scene.

Then perform an excess pass: remove grammatical census rows, proposition wrappers, deictic duplicates, pure modifiers, physical-noun inflation, temporal-cue/action inflation, every-PP behavior, dictionary-head fragmentation, unjustified cross-class duplicates, and same-role restatements.

The target is archetypal lightweight research resolution: preserve every distinct research role, but no merely grammatical inventory.

## 14. Compounds — one represented relation proposition per instance

Freeze the unit layer first. A compound cannot create, repair, suppress, or retype a unit.

Compounds represent materially distinct source-presented relation propositions expressible from retained units. Eligible relations include predicate relations, characterizations, questions/corrections/reflections, intended/prospective relations, reported relations, and orientation relations.

For each distinct relation instance:

1. identify the participant or represented carrier of the relation when present;
2. include the operative VERB/relation unit or characterization/orientation carrier;
3. include the other retained participants/referents that the relation actually connects;
4. include retained LABEL, TIME, PLACE, and LOCATOR anchors when they establish, qualify, situate, or orient that relation instance;
5. use one smallest complete ref set that reconstructs the relation at the research-scene/event grain.

Prefer semantic/source relation order: carrier/participant, operative relation, connected participants/referents, characterization values, then the contextual temporal/spatial/orientation anchors actually used by the relation. Where a relation is carried only by characterization or orientation units, order refs so the represented carrier and operative characterization/orientation remain recognizable.

Distinct carrier/reporting and embedded/content relations may both survive when each is separately represented. Do not emit every pair, combinatorial subsets, every sentence, broad co-occurrence bundles, nested variants of the same relation, or alternate decompositions of one relation.

Compound `qualities_available` follows the same qualities rule above; Q is not a question marker.

## 15. Calibration isolation

Return only the JSON required by the request schema.

Never infer or reconstruct archetypes, expected counts, evaluator preferences, prior scored answers, case-specific gold corrections, sealed holdout source during calibration, or holdout output. Do not attempt to optimize toward an imagined hidden answer.

## 16. Prohibited work

Never perform APA scoring, psychological interpretation, protected-thread analysis, conclusions, promotion, APA-ID creation, Oval Office research writing, sovereign admission, or database/fabric admission.

## 17. Successor effect

V49 prospectively supersedes V48 for new calibration and certification runs. V48 and every prior contract/run remain preserved as training history. V49 changes only the generalized semantic resolution/grain and compound-construction rules described here. Immutable archetype hashes, deterministic apparatus validation, hidden evaluation, holdout isolation, candidate-only status, historical preservation, one-shot holdout semantics, clean-room certification requirements, and all promotion/APA-ID/database prohibitions remain unchanged.