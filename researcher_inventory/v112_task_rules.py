"""V112 neutral apparatus rules: class-local selectability and orthogonal coverage.

These rules contain no archetype answers, evaluator findings, expected counts,
prior scored outputs, calibration answers, or holdout material.
"""
from researcher_inventory.inventory_apparatus import BASE_RULES as APPARATUS_BASE_RULES, CLASS_RULES as APPARATUS_CLASS_RULES

V112_CORRECTION = r'''
V112 PROSPECTIVE CORRECTION — CLASS-LOCAL SELECTABILITY + ORTHOGONAL CLASS COVERAGE.

READ THE WHOLE SOURCE FIRST. Silently map differentiated scenes/episodes, participants, acted-on or referred-to content, characterizations/states, lexical relation edges, orientations, memories, reports, questions, intentions, alternatives, recurring relations, prospective situations, and present reflection.

THE SEVEN CLASSES ARE ORTHOGONAL LEDGERS OVER THE SAME SOURCE. Inventory the requested class independently. Do not prune a legitimate entry in the requested class because a different class or a future compound carries related meaning. Cross-class overlap is not by itself redundancy. Deduplicate only true same-class aliases/coreference/restatements.

TWO-GATE ADMISSION:
A) EXACT CLASS-NATIVE IDENTITY: source-established, smallest complete natural literal span for the requested class; legitimate unnamed PLACE/TIME support may use null source_wording with exact source_cue and a neutral tag.
B) CLASS-LOCAL SELECTABILITY: if this class were the only inventory being built, does the source establish a distinct selectable entry of this class rather than grammar, decoration, a same-class duplicate, or a fragment of a larger class-native entry?

Do NOT ask whether the candidate is globally indispensable, important, recurring, central, unique across all seven classes, or reconstructable from another unit/compound. Legitimate entries may be local, one-use, mundane, neutral, nested, remembered, reported, prospective, uncertain, corrective, or low-salience.

SAME-CLASS ECONOMY ONLY: merge true aliases/coreference and repeated realizations of the same class-native identity. Never create an oversized unit merely to do several class jobs. When one source span carries different class functions, keep the smallest complete span for the requested class and leave the other jobs to their own class passes.

FUNCTION BEATS SURFACE GRAMMAR:
- human/social participant -> PERSON
- stable thing/content/referential handle -> OBJECT
- characterization/state/identity/evaluation/comparison/posture -> LABEL
- scene/location support -> PLACE
- episode/period/phase support -> TIME
- event/state/relation lexical predicate -> VERB
- orientation situating retained structure -> LOCATOR
A nominal, spatial, comparative, or clause-shaped phrase is LABEL when its represented job is characterization/state/evaluation. OBJECT requires thing/content identity. LOCATOR requires actual orientation, not merely a preposition/adverbial form.

PLACE LEDGER: retain each distinct source-established scene/location supporting represented material. Broad and contained/local support may coexist when they are different scene coordinates. Retain legitimate unnamed support for differentiated occurrence/object-location/destination/waiting/later-interaction/remembered/present-telling scenes when a place coordinate is represented but unnamed. For unnamed support use null source_wording, exact source_cue, neutral tag. Reject mere physical nouns, possessions, and spatial wording that does not establish a distinct scene/location support coordinate.

TIME LEDGER: retain each distinct source-established episode/period/phase in source progression, including materially differentiated attempts/conditions, help/response episodes, transitions/departures, waits, intended periods, later reports/conversations, recurring spans, remembered phases, prospective/future situations, and present telling/reflection. A TIME need not contain a temporal noun. For unnamed support use null source_wording, exact source_cue, neutral tag. Reject tense/aspect grammar, isolated temporal words/durations/recurrence markers, and one-time-per-action proliferation when no separate episode/phase exists.

PERSON LEDGER: retain speaker and each distinct source-established human/social actor or stable group functioning as a participant after true coreference. Direct, offscreen, remembered, reported, institutional, relational, possessive-within-a-material-relation, and prospective participation may qualify. Reject rhetorical/generic/nonreferential addressees and incidental mentions that never become participants.

OBJECT LEDGER: retain each source-established concrete, abstract, internal, relational, decision/choice-like, value-like, set/category, content, or figurative handle treated as a separately selectable thing/content. It may be acted on, possessed, exchanged, checked, contrasted, questioned, remembered, reported, selected, decided about, located, valued, contemplated, or otherwise reified. Reject noun census, generic pronouns/deixis, incidental props, arbitrary nominalizations, discourse wrappers, and clause-sized proposition wrappers. LABEL PRECEDENCE: if the span's represented function is characterization/state/evaluation/comparison/identity rather than thing/content identity, classify it as LABEL even if nominal in form.

LABEL LEDGER: retain each smallest complete source-native characterization, quality, state, identity, evaluation, comparison, correction, acceptance/rejection, polarity, manner, candidate/question label, or posture assigned to represented material. Local, one-use, idiomatic, colloquial, negated, uncertain, figurative, comparative, and corrective labels may qualify. FUNCTION BEATS SHAPE: do not move a characterization to OBJECT or LOCATOR merely because it is a noun phrase, spatial metaphor, or comparison. Reject pure intensification, exclamation, rhetorical flourish, scene color, and modifiers that do not independently characterize represented material.

VERB LEDGER: retain each materially represented lexical predicate increment establishing an action, state, attempt, response, movement, possession, perception, communication/report, cognition, intention, question, decision, comparison, evaluation, transition, or location/state relation. Use the smallest complete lexical predicate construction. Preserve required particle/reflexive/negation/modal/bound complement when needed for predicate identity. Do NOT swallow separately typed subject, object/content handle, label, locator, place, or time. Split matrix/embedded and coordinated predicates when they perform different relation jobs. Retain simple and one-use lexical relations. Reject auxiliaries, tense/aspect support, bare copular grammar with no lexical relation beyond a LABEL/state, discourse organizers, and same-relation restatements.

LOCATOR LEDGER: retain each smallest complete exact source span that genuinely orients a retained node/relation/scene by position, containment, path, direction, origin/destination, proximity, accompaniment, recurrence, procedure/relation, internal/mental context, temporal position, or figurative/comparative orientation. It must perform an orienting relation, not merely be any prepositional/adverbial phrase. Reject ordinary purpose/beneficiary/topic/argument markers, discourse connectors, degree/intensifier phrases, generic deictics, bare duration/how-long wording, aspectual words, and duplicated TIME support when they do not orient retained structure. LABEL PRECEDENCE: if the represented job is characterization/evaluation/comparison rather than orientation, classify it as LABEL.

ATOMIC SPAN + LITERAL LOCK: use the smallest complete exact contiguous source-native span for every admitted primitive. Preserve required particles/prepositions, reflexives, bound complements, negation, modality, uncertainty, questions, attribution, comparison, idiom/dialect, and hypothetical/prospective/reported/corrective posture. Never normalize, paraphrase, clean up, lemmatize into a different form, translate, diagnose, or substitute synonyms. Every non-null source_wording/source_cue/order_cue must be exact source text. Neutral mechanical tags are reserved only for legitimate unnamed PLACE/TIME support.

COVERAGE-MATRIX FREEZE:
1) enumerate each differentiated scene/episode in source order;
2) for each scene/episode, independently ask whether it establishes selectable entries in each requested class; this detects local and low-salience omissions but does NOT require every class in every scene;
3) add legitimate class-native entries;
4) anti-census audit: remove grammar, discourse carriage, incidental props, stylistic color, purpose/topic fragments, and same-class duplicates;
5) functional-precedence audit: correct OBJECT/LABEL/LOCATOR/VERB drift by represented function;
6) atomic-span + literal-lock audit;
7) repeat coverage once and freeze only when stable.

RELATION-INSTANCE COMPOUNDS: after all seven class ledgers freeze, reread relation by relation. For each retained VERB relation instance, emit the smallest complete compound linking the frozen coordinates that actually participate in that exact relation. Include participant, content/object, characterization, support, and orientation refs when they participate. Do not omit a participating class-native unit merely because the relation is intelligible without it. Additional non-VERB compounds are allowed only for represented relation/state structure not already captured by a retained VERB relation. Do not emit graph closure, arbitrary co-occurrence bundles, singleton equivalents, generic question closure, duplicate restatements, subset/superset permutations, scene mega-bundles, or compounds containing rejected non-class-native detail. Compounds never substitute for missing primitives.

Never target hidden counts or infer hidden gold. Never expose approved archetypes, evaluator findings, prior scored outputs, calibration answers, or sealed holdout material. Never perform promotion, Oval Office admission, APA-ID creation, sovereign/admitted writing, or database mutation.
'''.strip()

V112_BASE_RULES = APPARATUS_BASE_RULES + "\n\n" + V112_CORRECTION
V112_CLASS_RULES = dict(APPARATUS_CLASS_RULES)
V112_CLASS_RULES.update({
    "PLACE": "Inventory PLACE independently of all other classes. Retain each distinct source-established scene/location support coordinate, including legitimate unnamed support for differentiated occurrence, object location, destination, waiting, remembered/later interaction, and present-telling scenes. Broad and contained support may coexist when they are different scenes. For unnamed PLACE use null source_wording + exact source_cue + neutral tag. Reject physical nouns/possessions/spatial wording that do not establish a scene/location support coordinate. Do not omit PLACE because a LOCATOR, OBJECT, TIME, or compound captures related material.",
    "TIME": "Inventory TIME independently of all other classes. Retain each distinct source-established episode/period/phase, including differentiated attempts/conditions, response/help episodes, transitions, waits, intended periods, later reports/conversations, recurring spans, remembered phases, prospective/future situations, and present reflection. TIME need not contain temporal vocabulary; legitimate unnamed TIME uses null source_wording + exact source_cue + neutral tag. Reject tense/aspect, isolated duration/recurrence tokens, and action-by-action proliferation without a separate phase. Do not omit TIME because another class or compound captures related material.",
    "PERSON": "Inventory PERSON independently. Retain speaker plus every distinct source-established human/social actor or stable group functioning as a participant after true coreference, including direct, offscreen, remembered, reported, institutional, relational, possessive-within-a-material-relation, and prospective participants. Reject rhetorical/generic/nonreferential addressees and incidental mentions that never become participants.",
    "OBJECT": "Inventory OBJECT independently. Retain each stable source-established concrete/abstract/internal/relational/decision/value/set/category/content/figurative handle treated as a selectable thing/content. Reject noun census, generic pronouns/deixis, incidental props, arbitrary nominalizations, discourse/proposition wrappers. LABEL precedence: if the span's source function is characterization/state/evaluation/comparison/identity rather than thing/content identity, do not type it OBJECT even if it is nominal.",
    "LABEL": "Inventory LABEL independently. Retain each smallest complete source-native characterization/quality/state/identity/evaluation/comparison/correction/acceptance-rejection/polarity/manner/candidate-question label/posture assigned to represented material. Local, one-use, idiomatic, colloquial, negated, uncertain, figurative, comparative, corrective labels may qualify. Function beats syntax: nominal, locative, comparative, or clause-shaped wording remains LABEL when its represented job is characterization/state/evaluation. Reject pure intensification, rhetoric, scene color, and decorative modifiers.",
    "VERB": "Inventory VERB independently. Retain each materially represented lexical predicate increment establishing a distinct action/state/relation, including simple and one-use relations. Use the smallest complete lexical predicate; preserve only bound particles/reflexives/negation/modality/complements needed for predicate identity. Do not swallow separately typed subjects, objects, labels, locators, places, or times. Split matrix/embedded/coordinated predicates when they perform different jobs. Reject auxiliaries, tense/aspect support, bare copular grammar with no lexical relation beyond a LABEL/state, discourse organizers, and same-relation restatements.",
    "LOCATOR": "Inventory LOCATOR independently. Retain each smallest exact span performing a genuine orientation relation for a retained node/relation/scene: position, containment, path, direction, origin/destination, proximity, accompaniment, recurrence, procedure/relation, internal/mental context, temporal position, or figurative/comparative orientation. Reject ordinary purpose/beneficiary/topic/argument phrases, discourse connectors, degree/intensifier phrases, generic deictics, bare duration/how-long wording, aspectual words, and duplicated TIME support when they do not orient retained structure. LABEL precedence applies when the phrase characterizes/evaluates rather than orients.",
})
