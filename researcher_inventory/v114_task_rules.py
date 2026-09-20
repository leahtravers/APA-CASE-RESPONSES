"""V114 neutral apparatus rules: represented-denotatum/relation coverage with support closure.

These rules contain no archetype answers, evaluator findings, expected counts,
prior scored outputs, calibration answers, or holdout material.
"""
from researcher_inventory.inventory_apparatus import BASE_RULES as APPARATUS_BASE_RULES, CLASS_RULES as APPARATUS_CLASS_RULES

V114_CORRECTION = r'''
V114 PROSPECTIVE CORRECTION — REPRESENTED DENOTATA, RELATIONS, SUPPORT, AND ORIENTATIONS.

READ THE WHOLE SOURCE FIRST. Segment differentiated scenes, episodes, periods, interactions, memories, reports, questions, intentions, alternatives, recurring situations, prospective situations, and present reflection/telling before class extraction.

LIGHTWEIGHT MEANS DEDUPLICATED REPRESENTED COVERAGE, NOT HIGH-SALIENCE PRUNING. Retain each distinct class-native represented coordinate once. Do not require recurrence, thematic importance, later reuse, independent salience, or narrative emphasis. A valid coordinate may be mundane, one-use, background, local, low-salience, remembered, reported, prospective, uncertain, negated, corrective, figurative, or colloquial.

THREE-GATE ADMISSION:
A) SOURCE GROUNDING: the source explicitly establishes the class-native denotatum/relation/state/orientation, or a represented occurrence necessarily supplies legitimate unnamed PLACE/TIME support.
B) REPRESENTED CLASS-NATIVE FUNCTION: the candidate denotes or performs a distinct represented job in the requested class, not merely grammar/discourse carriage.
C) CLASS-LOCAL DISTINCTNESS: merge only true aliases/coreference/inflection-only same-relation realizations/restatements. Never prune because another class or future compound overlaps the content.

REJECT ONLY LANGUAGE-CARRIAGE MATERIAL WITH NO DISTINCT REPRESENTED CLASS JOB: determiners/articles, inflection-only material, auxiliaries/tense-aspect machinery with no lexical relation, generic connective wording, fillers, discourse scaffolding, nonreferential/generic pronouns after coreference, and fragments that are merely pieces of a larger natural coordinate.

ORDINARY REPRESENTED CONTENT IS NOT SCENE COLOR MERELY BECAUSE IT IS ORDINARY. Concrete things, minor participants, one-use predicates/gestures, local states, implicit scene/episode supports, and low-salience orientations belong when they are distinctly represented.

FUNCTION BEATS SURFACE FORM:
- human/social participant -> PERSON
- thing/content/referential handle -> OBJECT
- characterization/state/identity/evaluation/comparison/candidate label/correction -> LABEL
- scene/location support -> PLACE
- episode/period/phase support -> TIME
- meaningful lexical event/state/action/relation -> VERB
- position/path/direction/context/orientation relation -> LOCATOR
A spatial-looking phrase may be OBJECT; a noun phrase may be LABEL; an adverbial/comparison may be LABEL or LOCATOR according to represented job. Genuine cross-class projection is allowed.

PLACE SUPPORT CLOSURE: retain every distinct represented spatial scene/location support coordinate, including broad/contained support, represented object-location support, destination/away-place, waiting position, later-interaction/remembered scene, recurring/prospective scene, and present-telling/reflection scene when distinct. Explicit name is not required. Unnamed PLACE uses null source_wording + exact source_cue + neutral tag. Do not treat every physical object as PLACE.

TIME SUPPORT CLOSURE: after source segmentation, check every differentiated represented episode/phase for its own temporal support coordinate. Retain distinct attempt/condition, response/help, transition/departure, waiting, intended, later-report/conversation, recurring, remembered, broader relational, prospective/future, and present-reflection episodes when represented. Explicit temporal words are not required. Unnamed TIME uses null source_wording + exact source_cue + neutral tag. Do not split every action when several share one episode.

PERSON: retain speaker plus every distinct source-established human/social participant or stable group after coreference, including direct, offscreen, remembered, reported, institutional, relational, possessive/beneficiary when part of a represented material relation, and prospective participation. One-use participants qualify. Reject only generic/rhetorical/nonreferential people who never become participants.

OBJECT: retain every distinct represented concrete/abstract/internal/relational/decision/value/set/category/content/figurative handle that is something the source relates to, acts on, possesses, exchanges, checks, contrasts, questions, remembers, reports, values, decides about, contemplates, or locates. One-use ordinary concrete things qualify. Reject generic pronouns/deixis after coreference, arbitrary grammatical nominalizations, and non-reified clause fragments. LABEL takes precedence when the primary represented job is characterization/state/evaluation/comparison, unless the source genuinely supports both jobs.

LABEL: retain every distinct represented characterization, state, identity, evaluation, comparison, correction, acceptance/rejection, polarity, manner, candidate/question label, or posture assigned/entertained about represented material. One-word, one-use, colloquial, idiomatic, figurative, uncertain, negated, corrected, or rejected labels may qualify. Reject pure intensification or modification with no separate represented characterization/state.

VERB: retain every distinct contentful lexical predicate expressing a represented event, action, state, relation, movement, possession, perception, communication/report, cognition, intention, question, decision, comparison, evaluation, transition, gesture, or other predication. DO NOT REQUIRE MATERIAL STORY CHANGE. One-use, mundane, gestural, low-salience, and background predicates qualify. Use the smallest complete lexical predicate and preserve only particles/reflexives/negation/modals/bound complements required for relation identity. Split matrix/embedded/coordinated predicates when they express distinct relations. Exclude auxiliaries/tense-aspect machinery, pure copular carriage where all represented content is the label/state, discourse/filler predicates with no represented relation, and true same-relation restatements. Reporting/thinking/asking/explaining predicates are retained when themselves represented relations.

LOCATOR: retain each smallest exact span that distinctly orients represented material by position, containment, path, direction, origin/destination, proximity, accompaniment, recurrence/context, procedure/relation, internal/mental position, temporal position when orientational, or figurative/comparative relation. A direction/purpose phrase may qualify when it actually orients a represented action/participant. Reject bare prepositions, generic argument markers, degree phrases, conjunctions, and adverbials with no distinct represented orientation. Genuine overlap with LABEL/PLACE/TIME is allowed.

ATOMIC SPAN + LITERAL LOCK: use the smallest complete exact contiguous source-native span for every explicit primitive. Preserve required particles/prepositions, reflexives, bound complements, negation, modality, uncertainty, questions, attribution, comparison, idiom/dialect, and hypothetical/prospective/reported/corrective posture. Never normalize, paraphrase, clean up, translate, diagnose, euphemize, lemmatize into a different surface form, or substitute synonyms. Every non-null source_wording/source_cue/order_cue must be exact source text.

FREEZE AUDIT:
1) walk every differentiated represented scene/episode in source order;
2) perform explicit PLACE/TIME support closure;
3) audit low-salience concrete things, one-use participants, single gestures/actions, minor states/labels, local orientations, and background relations for omissions;
4) remove only grammar/discourse carriage plus true same-class duplicates;
5) audit functional type by represented job, allowing genuine cross-class projections;
6) audit exact literal spans/posture;
7) repeat coverage and freeze only when omission and over-admission checks are stable.

PROPOSITION/RELATION-INSTANCE COMPOUNDS: only after all seven ledgers freeze, reread the source as represented proposition/relation units. For each represented proposition/relation instance that contributes source structure, emit the smallest complete compound linking only the frozen coordinates that actually participate. Use a retained VERB as backbone when one carries the proposition. Include participants, content/objects, labels/states, PLACE/TIME support, and LOCATOR refs only when they participate in that exact instance. Non-VERB label/state/question propositions may form compounds when not already carried by a retained relation. Do not emit graph closure, arbitrary co-occurrence bundles, scene mega-bundles, singleton equivalents, subset/superset permutations, or duplicate restatements.

Never target hidden counts or infer hidden gold. Never expose approved archetypes, evaluator findings, prior scored outputs, calibration answers, or sealed holdout material. Never perform promotion, Oval Office admission, APA-ID creation, sovereign/admitted writing, or database mutation.
'''.strip()

V114_BASE_RULES = APPARATUS_BASE_RULES + "\n\n" + V114_CORRECTION
V114_CLASS_RULES = dict(APPARATUS_CLASS_RULES)
V114_CLASS_RULES.update({
    "PLACE": "Retain every distinct represented scene/location support coordinate, including low-salience, contained/local, waiting, destination, later-interaction, remembered, prospective, and present-telling support. Explicit names are not required; unnamed PLACE uses null source_wording + exact source_cue + neutral tag. A physical object is PLACE only when its represented job is scene/location support. Do not require salience or recurrence.",
    "TIME": "Perform episode-support closure. Retain every distinct represented episode/period/phase support coordinate, including attempts, responses/help, transitions, waits, intended periods, later conversations/reports, recurring spans, remembered/broader relational periods, prospective situations, and present reflection when distinct. TIME need not contain temporal vocabulary; unnamed TIME uses null source_wording + exact source_cue + neutral tag. Do not split actions that clearly share one episode.",
    "PERSON": "Retain speaker and every distinct source-established human/social participant or stable group after coreference, including direct, offscreen, remembered, reported, institutional, relational, possessive/beneficiary participation, and prospective participation. One-use participants qualify. Reject only generic/rhetorical/nonreferential people who never become represented participants.",
    "OBJECT": "Retain every distinct represented thing/content handle, concrete or abstract, including ordinary one-use objects, internal/relational content, decisions/choices, values, sets/categories, proposition-like content when reified, and figurative handles. Do not prune for low salience. Reject generic pronouns after coreference and non-reified grammar. Type by represented function; LABEL precedence applies when the primary job is characterization/state/evaluation/comparison unless both functions are genuinely represented.",
    "LABEL": "Retain every distinct represented characterization/state/identity/evaluation/comparison/correction/acceptance-rejection/polarity/manner/candidate-question label/posture. One-word, one-use, colloquial, idiomatic, uncertain, negated, figurative, corrected, and rejected labels may qualify. Reject only modifiers/intensifiers with no separate represented characterization/state.",
    "VERB": "Retain every distinct contentful lexical predicate expressing a represented event/action/state/relation/movement/possession/perception/communication/cognition/intention/question/decision/comparison/evaluation/transition/gesture. Do not require material story change; one-use and low-salience predicates qualify. Use the smallest complete lexical predicate and preserve bound relation-identity material. Exclude auxiliaries/tense-aspect only, pure copular carriage with no separate relation, discourse/filler predicates with no represented relation, and true same-relation restatements.",
    "LOCATOR": "Retain each smallest exact span that distinctly orients represented material by position, containment, path, direction, origin/destination, proximity, accompaniment, recurrence/context, procedure/relation, internal/mental position, temporal position when orientational, or figurative/comparative relation. Direction/purpose phrases may qualify when they truly orient represented action. Reject only generic argument markers or adverbials with no distinct represented orientation. Genuine overlap with LABEL/PLACE/TIME is allowed.",
})
