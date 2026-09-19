"""V95 neutral apparatus rules: semantic sufficiency without lexical census.

These rules mirror AGENT_CONTRACT_V95 without archetype answers, evaluator findings,
expected counts, prior scored outputs, or holdout material.
"""

V95_BASE_RULES = r'''
V95 LIGHTWEIGHT RULE: SEMANTIC SUFFICIENCY / NO LEXICAL CENSUS.

Read the complete source first and silently map materially distinct scenes, episodes, actors, stable referents, source characterizations, complete semantic predicate relations, orientation/topology relations, and materially distinct propositions/events/questions/comparisons. This map prevents omissions. It is NOT a token, POS, noun-phrase, verb, preposition, modifier, clause, or sentence census.

CONTROLLING ADMISSION GATE: create a primitive only when removing it would lose a materially distinct semantic coordinate, relation, orientation, referent, characterization, actor, scene, or episode needed to reconstruct represented source structure. One-use, endpoint-dependent, low-salience, or unnamed coordinates may qualify. Mere lexical or grammatical extractability does not.

LITERAL PRESERVATION IS DOWNSTREAM OF SELECTION. Preserve source wording exactly inside selected primitives, but do not create a primitive for every source word or phrase just to preserve it.

CLASS JOBS:
- PLACE = materially distinct scene/occurrence support coordinate.
- TIME = materially distinct episode/phase support coordinate.
- PERSON = distinct represented actor/stable group after true coreference.
- OBJECT = stable source-reified concrete/abstract referent or content handle.
- LABEL = distinct represented characterization/candidate characterization.
- VERB = complete semantic predicate relation.
- LOCATOR = materially distinct orientation/topology relation.

PLACE: keep named settings and necessary distinct occurrence positions for materially different waits, encounters, conversations, reports, memories, reflections, performances, or actions. Necessary unnamed support places may use source_wording=null with exact cue and neutral mechanical tag. Do not create PLACE from every surface, body part, container, path noun, figurative space, or locative phrase. Type figurative spatial wording by represented semantic job, not surface vocabulary.

TIME: keep materially distinct episodes/phases, waits/transitions that create a distinct interval, later conversations/explanations, remembered/recurring/present/prospective periods when they organize separate represented material, and necessary unnamed frames. Several propositions may share one TIME. Do not create TIME merely from tense or every temporal word/duration/discourse marker such as now/when/while/since/always unless it establishes a distinct episode/phase.

PERSON: retain B plus every distinct materially represented human/social actor or stable group after true coreference. Minor/offscreen/remembered/reported/relational/possessive/prospective/institutional actors may qualify. Suppress aliases and nonreferential/rhetorical addressees.

OBJECT: retain stable source-reified things/content handles: concrete things, parts, products, documents, instruments, amounts, results, choices, decisions, plans, options, relations/situations/event-content/internal content/figurative objects when source treats them as things or targets of reference. Do NOT create OBJECT merely from every noun phrase, pronoun, clause complement, question, action phrase, or placeholders such as this/it/anything/something. Do not create cross-class shadows whose semantic job is already fully represented elsewhere.

LABEL: retain distinct represented characterization/candidate characterization: identity/status, materially predicated state/manner, characterization comparison, self/other label, candidate feeling/meaning label, and immediate acceptance/rejection/correction/polarity when it materially changes the characterization. Preserve candidate label and rejection/correction separately when the source establishes separate semantic jobs. Do not inventory every adjective/adverb/rhetorical flourish/decorative description/metaphor/evaluative phrase.

VERB: retain materially distinct complete semantic predicate relations, not grammatical verb tokens. Keep auxiliaries/aspect/negation/modality/light-verb support/particles/complements together when they form one predicate identity. Suppress standalone copular/auxiliary/tense/aspect/do-support fragments and repeated is/was/be/being tokens without their own semantic predicate job. Split coordinated or nested predicates only when each is a materially distinct relation that can be separately reconnected. Endpoint dependence is allowed; syntactic atomization is not required.

LOCATOR: retain materially distinct orientation/topology relations needed to reconstruct position, containment, support, origin/destination/path/approach/away/entry/exit, meaningful directional orientation, internal/mental orientation, or figurative/comparative orientation that actually positions represented material. Do not create LOCATOR merely from generic prepositions, conjunctions, temporal discourse markers, degree phrases, comparisons, or adverbs such as routine to/at/when/while/since/now/still/like/as/out unless that occurrence performs a materially distinct orientation job. Separate LOCATOR from VERB only when both semantic jobs are independently present.

CROSS-CLASS OVERLAP is allowed only when the same literal trace preserves genuinely different semantic information in each class. Grammatical ambiguity alone is insufficient.

LITERAL LOCK: for admitted source-derived rows preserve source language, dialect, contractions, numbers, uncertainty, negation, modality, comparison, and punctuation exactly where source text is expected. Only genuinely unnamed PLACE/TIME support may use source_wording=null anchored by exact source text. researcher_note is null or minimal mechanical/coreference/unnamed-coordinate bookkeeping.

FREEZE PRIMITIVES BEFORE COMPOUNDS. Audit that every row passes semantic sufficiency; PLACE/TIME cover distinct scene/episode support without mention census; OBJECT/LABEL preserve stable semantic jobs; VERB is semantically complete rather than syntactically minimal; LOCATOR is a distinct orientation relation rather than generic grammar; figurative spatial language is typed by represented job; aliases/duplicates/grammatical projections are suppressed.

COMPOUNDS: reconstruct the smallest set of canonical materially distinct source-local propositions/events/states/reports/intentions/questions/comparisons/characterizations/orientations among frozen coordinates. Use only coordinates belonging to that represented binding. Include PLACE/TIME/LOCATOR/LABEL only when they materially anchor/qualify that binding. Preserve question/uncertainty posture. Set Q only when qualitative availability belongs to that compound under the schema, not automatically because a referenced primitive could carry qualitative information. Do not create graph closure, lexical-fragment compounds, pairwise combinations, subset/superset permutations, mega-bundles, or automatic propagation of all support coordinates.

Never target hidden counts or infer hidden gold. Never expose approved archetypes, evaluator findings, prior scored answers, calibration answers, or sealed holdout content/output to the worker. Never perform APA scoring, psychological interpretation, promotion, APA-ID creation, sovereign/admitted writing, or database mutation.
'''.strip()

V95_CLASS_RULES = {
    "PLACE": "Retain materially distinct scene/occurrence support coordinates, including necessary unnamed support. Avoid locative-phrase and figurative-space census; type by represented semantic job.",
    "TIME": "Retain materially distinct episode/phase support, including necessary unnamed frames. Avoid tense, adverb, duration, and temporal-discourse mention census.",
    "PERSON": "Retain B plus every distinct materially represented actor or stable group after true coreference; suppress aliases and nonreferential addressees.",
    "OBJECT": "Retain stable source-reified concrete/abstract referents or content handles. Avoid noun-phrase/pronoun/clause census and cross-class shadows.",
    "LABEL": "Retain distinct represented characterizations/candidate characterizations and semantically separate acceptance/rejection/correction. Avoid descriptive-language census.",
    "VERB": "Retain materially distinct complete semantic predicate relations. Keep grammatical support with its predicate; suppress auxiliary/copular/POS fragmentation. Split only genuinely distinct relations.",
    "LOCATOR": "Retain materially distinct orientation/topology relations. Avoid generic preposition/adverb/comparison/discourse-marker census; separate from VERB only when both semantic jobs exist.",
}
