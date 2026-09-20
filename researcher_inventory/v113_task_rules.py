"""V113 neutral apparatus rules: class-local representation-bearing coordinate threshold.

These rules contain no archetype answers, evaluator findings, expected counts,
prior scored outputs, calibration answers, or holdout material.
"""
from researcher_inventory.inventory_apparatus import BASE_RULES as APPARATUS_BASE_RULES, CLASS_RULES as APPARATUS_CLASS_RULES

V113_CORRECTION = r'''
V113 PROSPECTIVE CORRECTION — CLASS-LOCAL REPRESENTATION-BEARING COORDINATES.

READ THE WHOLE SOURCE FIRST. Silently map the represented situation: differentiated scenes/episodes, participants, stable referential content, characterizations/states, represented relation instances, orientations, memories, reports, questions, intentions, alternatives, recurring relations, prospective situations, and present reflection.

THE SEVEN CLASSES REMAIN ORTHOGONAL. Judge each candidate inside its own class. Never prune a valid class-native coordinate merely because another class or a future compound carries related meaning. Cross-class overlap is not by itself redundancy. Deduplicate only true same-class aliases/coreference/restatements.

THREE-GATE PRIMITIVE ADMISSION:
A) EXACT CLASS-NATIVE SOURCE IDENTITY: source-established, smallest complete natural literal span for the requested class. Legitimate unnamed PLACE/TIME support may use null source_wording with an exact source_cue and neutral tag.
B) REPRESENTATION-BEARING COORDINATE: the candidate must index a distinct part of WHAT THE SOURCE REPRESENTS, not merely a piece of language used to carry the telling. Ask what stable represented thing, participant, characterization/state, relation, scene/episode support, or orientation a researcher could point back to through this entry.
C) CLASS-LOCAL DISTINCTNESS: the coordinate must be distinct from already retained coordinates in the same class; merge only true aliases/coreference/inflection-only same-relation realizations/restatements.

A word or phrase is NOT admitted merely because it can be semantically or grammatically typed as one of the seven classes. Reject narration/discourse carriage, auxiliaries/tense/aspect machinery, generic connective wording, incidental modifiers/scene color, non-reified noun mentions, lexical predicates that do not establish a distinct represented relation, prepositional/adverbial fragments that do not establish a distinct orientation, and temporal/spatial wording that does not establish a separate support coordinate.

LIGHTWEIGHT DOES NOT MEAN HIGH-SALIENCE ONLY. A valid coordinate may be local, one-use, mundane, neutral, nested, remembered, reported, prospective, uncertain, corrective, negated, figurative, or low-salience. The distinction is represented coordinate versus language census, not important versus unimportant.

ANTI-CENSUS + ANTI-PRUNING BALANCE:
- Remove a candidate if its only justification is that the wording fits a class definition.
- Keep a candidate if it independently establishes a represented coordinate in its class, even when another class or compound overlaps it.
- Never make one oversized primitive do several class jobs.

FUNCTION BEATS SURFACE GRAMMAR:
- represented human/social participant -> PERSON
- stable represented thing/content/referential handle -> OBJECT
- represented characterization/state/identity/evaluation/comparison/posture -> LABEL
- represented scene/location support coordinate -> PLACE
- represented episode/period/phase support coordinate -> TIME
- represented event/state/relation predicate coordinate -> VERB
- represented orientation situating retained structure -> LOCATOR
A nominal, spatial, comparative, adjectival, verbal, or clause-shaped phrase is typed by its represented job, not its syntax.

PLACE LEDGER: retain each distinct source-established location/scene support coordinate required by represented material. Broad and contained/local support may coexist when they are genuinely different represented scene coordinates. Legitimate unnamed support may represent differentiated occurrence/object-location/destination/waiting/later-interaction/remembered/present-telling scenes. For unnamed support use null source_wording, exact source_cue, neutral tag. Reject physical nouns, possessions, surfaces/containers, and spatial wording that do not establish a distinct scene/location support coordinate.

TIME LEDGER: retain each distinct source-established episode/period/phase support coordinate. A separate TIME can represent a differentiated condition/attempt, response/help episode, transition/departure, wait, intended period, later report/conversation, recurring span, remembered phase, prospective/future situation, or present reflection. TIME need not contain temporal vocabulary. For unnamed support use null source_wording, exact source_cue, neutral tag. Reject tense/aspect, isolated duration/recurrence/sequencing tokens, and action-by-action proliferation where no separate represented phase exists.

PERSON LEDGER: retain speaker plus every distinct source-established human/social actor or stable group functioning as a represented participant after true coreference. Direct, offscreen, remembered, reported, institutional, relational, possessive-within-a-material-relation, and prospective participation may qualify. Reject rhetorical/generic/nonreferential addressees and incidental human mentions that never become represented participants.

OBJECT LEDGER: retain each source-established concrete/abstract/internal/relational/decision/value/set/category/content/figurative handle treated as a separately represented thing/content coordinate. It may be acted on, possessed, exchanged, checked, contrasted, questioned, remembered, reported, selected, decided about, located, valued, contemplated, or otherwise reified. One mention can qualify when it has a stable represented role. Reject noun census, generic pronouns/deixis, incidental nouns decorating another coordinate, arbitrary nominalizations, discourse wrappers, and non-reified clause content. A phrase functioning as represented content/thinghood may be OBJECT regardless of surface form. LABEL precedence applies when the primary represented job is characterization/state/evaluation/comparison/identity.

LABEL LEDGER: retain each smallest complete source-native characterization/quality/state/identity/evaluation/comparison/correction/acceptance-rejection/polarity/manner/candidate-question label/posture that is itself represented about a person, thing, relation, or situation. Local, one-use, idiomatic, colloquial, negated, uncertain, figurative, comparative, and corrective labels may qualify. Reject adjectives/modifiers/intensifiers/rhetorical color that merely phrase another coordinate without establishing a separately represented characterization/state.

VERB LEDGER: retain a lexical predicate only when it establishes a distinct represented event/state/relation coordinate. It may be action, response, movement, possession, perception, communication/report, cognition, intention, question, decision, comparison, evaluation, transition, or location/state relation. Do not inventory every lexical verb. Qualifying predicates establish or materially update represented relations among participants/content/support coordinates. Use the smallest complete lexical predicate and preserve only bound particle/reflexive/negation/modal/complement material required for relation identity. Do not swallow separately typed subjects, objects, labels, locators, places, or times. Split matrix/embedded/coordinated predicates only when each establishes a different represented relation coordinate. Reject auxiliaries, tense/aspect support, bare copular carriage, generic narration/telling scaffolding, discourse organizers, conversational fillers, and same-relation restatements.

LOCATOR LEDGER: retain each smallest complete exact source span that establishes a distinct represented orientation for a retained node/relation/scene by position, containment, path, direction, origin/destination, proximity, accompaniment, recurrence, procedure/relation, internal/mental context, temporal position, or figurative/comparative orientation. Do not inventory every prepositional phrase, adverbial, deictic, temporal phrase, destination word, comparison, or context phrase. Reject bare prepositions, ordinary purpose/beneficiary/topic/argument markers, discourse connectors, degree/intensifier phrases, generic deictics, bare duration/how-long wording, aspectual words, and duplicated TIME support when they do not independently orient retained structure. LABEL precedence applies when the phrase characterizes/evaluates rather than orients.

ATOMIC SPAN + LITERAL LOCK: use the smallest complete exact contiguous source-native span for every admitted primitive. Preserve required particles/prepositions, reflexives, bound complements, negation, modality, uncertainty, questions, attribution, comparison, idiom/dialect, and hypothetical/prospective/reported/corrective posture. Never normalize, paraphrase, clean up, lemmatize into a different form, translate, diagnose, euphemize, or substitute synonyms. Every non-null source_wording/source_cue/order_cue must be exact source text. Neutral mechanical tags are reserved only for legitimate unnamed PLACE/TIME support.

FREEZE AUDIT:
1) walk each differentiated represented scene/episode and detect omitted representation-bearing coordinates in each class;
2) for every proposed primitive silently state what represented coordinate it indexes; if the answer is only a grammatical/semantic category, reject it;
3) anti-census pass: remove grammar, narration carriage, generic discourse, incidental scene color, non-reified noun mentions, non-coordinate modifiers, purpose/topic fragments, support wording without separate scene/phase identity, and same-class duplicates;
4) anti-pruning pass: restore any valid class-native coordinate removed only because another class or compound overlaps it;
5) functional type audit;
6) atomic-span + literal-lock audit;
7) repeat coverage once and freeze only when omission and over-admission audits are both stable.

RELATION-INSTANCE COMPOUNDS: only after all seven ledgers freeze, reread relation by relation. For each retained VERB relation coordinate, emit the smallest complete compound linking frozen coordinates that actually participate in that exact represented relation. Include participant, content/object, characterization, support, and orientation refs only when they participate. Do not create a compound merely because several primitives occur in one sentence, clause, scene, or episode. Additional non-VERB compounds are allowed only for represented relation/state structure that cannot be carried by a retained VERB relation and that still passes the representation-bearing threshold. Do not emit graph closure, arbitrary co-occurrence bundles, singleton equivalents, generic question closure, duplicate restatements, subset/superset permutations, scene mega-bundles, or compounds containing rejected non-coordinate detail. Compounds never substitute for missing primitives and never justify deleting valid primitives.

Never target hidden counts or infer hidden gold. Never expose approved archetypes, evaluator findings, prior scored outputs, calibration answers, or sealed holdout material. Never perform promotion, Oval Office admission, APA-ID creation, sovereign/admitted writing, or database mutation.
'''.strip()

V113_BASE_RULES = APPARATUS_BASE_RULES + "\n\n" + V113_CORRECTION
V113_CLASS_RULES = dict(APPARATUS_CLASS_RULES)
V113_CLASS_RULES.update({
    "PLACE": "Retain only distinct representation-bearing scene/location support coordinates. A physical/spatial expression is not enough. Keep broad/contained or unnamed support when it is genuinely a separate represented scene coordinate; unnamed PLACE uses null source_wording + exact source_cue + neutral tag. Reject physical nouns, containers, surfaces, possessions, and spatial wording that do not independently support a represented occurrence/relation. Do not omit a valid PLACE because another class or compound overlaps it.",
    "TIME": "Retain only distinct representation-bearing episode/period/phase support coordinates. TIME need not contain temporal vocabulary; unnamed TIME uses null source_wording + exact source_cue + neutral tag. Reject tense/aspect, sequencing/duration/recurrence tokens, and action-by-action proliferation when no separate represented phase exists. Do not omit a valid TIME because another class or compound overlaps it.",
    "PERSON": "Retain speaker and each distinct source-established human/social actor or stable group functioning as a represented participant after true coreference. Direct, offscreen, remembered, reported, institutional, relational, possessive-within-a-material-relation, and prospective participants may qualify. Reject rhetorical/generic/nonreferential addressees and incidental mentions that never become participants.",
    "OBJECT": "Retain stable representation-bearing thing/content handles: concrete, abstract, internal, relational, decision/value/set/category/content/figurative coordinates treated as selectable content. One mention may qualify when the source gives it a stable represented role. Reject noun census, generic pronouns/deixis, incidental nouns decorating another coordinate, arbitrary nominalizations, discourse wrappers, and non-reified clause content. Type by represented function; LABEL takes precedence when the span is primarily a characterization/state/evaluation/comparison/identity.",
    "LABEL": "Retain only representation-bearing characterization/state coordinates assigned or entertained about represented material. Local, one-use, idiomatic, colloquial, negated, uncertain, figurative, comparative, and corrective labels may qualify. Reject adjectives/modifiers/intensifiers/rhetorical or scene color that merely phrase another coordinate without establishing a separate represented characterization/state. Type by represented job, not phrase shape.",
    "VERB": "Retain only lexical predicates that establish distinct representation-bearing event/state/relation coordinates. Do not inventory every lexical verb. Qualifying predicates establish or materially update represented relations; use the smallest complete predicate and preserve only bound material needed for relation identity. Split matrix/embedded/coordinated predicates only when each carries a different represented relation. Reject auxiliaries, tense/aspect, bare copular carriage, generic narration/telling scaffolding, discourse organizers, conversational fillers, and same-relation restatements.",
    "LOCATOR": "Retain only smallest exact spans establishing distinct representation-bearing orientations for retained nodes/relations/scenes: position, containment, path, direction, origin/destination, proximity, accompaniment, recurrence, procedure/relation, internal/mental context, temporal position, or figurative/comparative orientation. Reject prepositional/adverbial/deictic/context wording that merely modifies language, plus purpose/beneficiary/topic/argument markers, discourse connectors, degree phrases, bare duration/aspect, and duplicated TIME support. LABEL precedence applies when the source function is characterization/evaluation rather than orientation.",
})
