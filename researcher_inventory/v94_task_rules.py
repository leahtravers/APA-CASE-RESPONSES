"""V94 neutral apparatus rules: class-native entitlement and grain.

These rules mirror AGENT_CONTRACT_V94 without archetype answers, evaluator findings,
expected counts, prior scored outputs, or holdout material.
"""

V94_BASE_RULES = r'''
V94 LIGHTWEIGHT RULE: CLASS-NATIVE ENTITLEMENT AND GRAIN.

Read the complete source first. Silently map represented scenes/positions, time episodes/frames, actors, concrete/abstract referents, source characterizations, relation edges, orientation edges, and materially distinct propositions/events/questions/comparisons. This whole-source map prevents omissions; it does NOT create a token/POS census.

DO NOT APPLY ONE STANDALONE-ADDRESSABILITY TEST TO ALL SEVEN CLASSES. The classes have different research jobs. A primitive is admitted when the source materially establishes that class-native job and preserving the coordinate is needed to reconnect source structure at the resolution of that class. One-use, local, low-salience, unnamed support, or endpoint-dependent coordinates may be correct.

CLASS JOBS:
- PLACE/TIME = support coordinates organizing where/when represented occurrences happen, including necessary unnamed support coordinates.
- PERSON = actor coordinates.
- OBJECT = referential coordinates / source-treated concrete or abstract content handles.
- LABEL = characterization coordinates.
- VERB = relation-edge coordinates; they may depend on their endpoints for meaning.
- LOCATOR = orientation-edge coordinates; they may depend on the item/event they orient.

CLASS-NATIVE GRAIN: use the smallest complete source-native wording appropriate to the class. Entity/reference/label rows preserve the represented identity/posture. VERB rows preserve the smallest complete predicate edge, leaving separable arguments to their own classes. LOCATOR rows preserve the smallest complete orienting edge. Split coordinated or nested relations when they are materially distinct edges. Keep particles/negation/modality/complements only when they are identity-bearing for that edge rather than separable arguments/orientation.

PLACE: recover the support geography of the represented source, not only literal place nouns. Keep named settings, meaningful contained settings, distinct waiting/encounter/conversation/report/memory/reflection/action positions, and necessary unnamed positions when a materially distinct occurrence has a place even if the source never names it. Unnamed PLACE may use source_wording=null with an exact cue and a neutral mechanical tag. Do not turn every surface, body part, path noun, container, figurative space, or locative word into PLACE.

TIME: recover the support chronology/episode structure, not only dates/adverbs. Keep distinct episode phases, waits/transitions, later conversations/explanations, remembered periods, recurring spans, present telling/reflection, prospective periods, broader contextual periods, and necessary unnamed time frames. A TIME may be anchored by an event cue. Do not create one for every tense, action, adverb, transition, or duration phrase.

PERSON: retain B plus every distinct materially represented human/social actor or stable group after true coreference. Minor, one-use, offscreen, remembered, reported, relational, possessive, prospective, and institutional actors may qualify. Suppress aliases/coreferent repeats and nonreferential/rhetorical addressees.

OBJECT: retain materially represented concrete or abstract referents/content handles, including one-use physical details, parts, products, documents, surfaces, contents, instruments, results, amounts, choices, decisions, plans, options, relations/situations/event-content, and figurative objects when source-reified. Do not require recurrence or high salience. Do not nominalize every clause/complement/question/action. If an exact trace's only material job is already fully represented by another class and the source does not separately treat it as a referent, do not create an OBJECT shadow.

LABEL: retain wording that functions as a retrievable characterization or candidate characterization: identities/statuses, materially predicated states/manners, characterization comparisons, self/other labels, candidate feeling/meaning labels, and immediate acceptance/rejection/correction/polarity wording when it changes that candidate characterization. Preserve exact uncertainty, question form, negation, rejection, intensity, comparison, and dialect. Avoid decorative/background adjective/adverb/modifier census.

VERB: recover materially represented RELATION EDGES, not standalone lexical handles and not proposition-sized verb bundles. Include actions, physical acts, states/placements/existence, perception/cognition/stance, reports/speech, intentions/needs/choices, social interaction, local one-use acts, embodied/performance acts, and nested relations when the nested edge contributes represented structure. A VERB may only make full sense with its endpoints; that is normal. Split coordinated predicates into distinct edges when materially distinct. Split matrix and embedded edges when both contribute. Leave PERSON/OBJECT/LABEL/PLACE/TIME arguments outside the verb. Leave separable path/position/containment orientation to LOCATOR. Suppress pure auxiliaries/tense support, duplicate restatements, and full clauses masquerading as one VERB.

LOCATOR: recover materially represented ORIENTATION EDGES, not only phrases intelligible by themselves. Include position, approach/away/entry/exit/path, origin/destination, containment/support/surface position, meaningful directional particles (back/out/up/over), recurring-context orientation, internal/mental orientation, temporal-position phrases, and figurative/comparative orientation when they position represented material. A LOCATOR may be local and endpoint-dependent. Separate it from VERB when the source contains both a relation edge and a distinct orientation edge. Suppress recipient/topic marking, transitions, purely grammatical prepositions, and argument markers that do not orient represented material.

CROSS-CLASS OVERLAP is allowed only when the same literal trace performs genuinely different class-native jobs. A movement/state phrase may supply both a VERB edge and a LOCATOR edge; a locative state may also carry a LABEL job. Do not multiply grammatical shadows.

LITERAL LOCK: preserve source language exactly wherever source text is required. Do not normalize grammar, dialect, contractions, numbers, uncertainty, negation, modality, comparison, or punctuation. Only genuinely unnamed PLACE/TIME support may use source_wording=null, anchored by exact source text. researcher_note is null or minimal mechanical/coreference/unnamed-coordinate bookkeeping.

FREEZE PRIMITIVES BEFORE COMPOUNDS. Audit class by class: complete support scene/time structure; all distinct actors; material referents without arbitrary nominalization; source-indexed characterizations without modifier census; relation-edge completeness with atomic predicate grain; orientation-edge completeness with atomic orientation grain.

COMPOUNDS: reconstruct canonical materially distinct source-local propositions/events/states/reports/intentions/questions/comparisons/characterizations/orientations among frozen coordinates. Use applicable place/time/locator/label/verb coordinates when they belong to the same represented relation. Integrate qualifiers/orientation into the main proposition bundle rather than spawning redundant side compounds. A primitive does not need a compound merely because it exists. Do not create graph closure, pairwise combinations, every noun/label pair, subset/superset permutations, or mega-bundles.

Never target hidden counts or infer hidden gold. Never expose approved archetypes, evaluator findings, prior scored answers, or sealed holdout content/output to the worker. Never perform APA scoring, psychological interpretation, promotion, APA-ID creation, sovereign/admitted writing, or database mutation.
'''.strip()

V94_CLASS_RULES = {
    "PLACE": "Recover source-support geography: named settings plus materially distinct occurrence positions and necessary unnamed places for represented waits, conversations, reports, memories, reflections, and actions. Unnamed support may use null source wording with exact cue. Avoid physical-noun/surface/container/figurative-space census.",
    "TIME": "Recover source-support chronology: materially distinct episodes/phases, later conversations, waits, remembered/recurring/present/prospective periods, including necessary unnamed frames. Event cues may anchor TIME. Avoid tense/adverb/action/duration token census.",
    "PERSON": "Retain B plus every distinct materially represented actor or stable group after true coreference, including minor/offscreen/relational/reported/prospective actors. Suppress aliases and nonreferential addressees.",
    "OBJECT": "Retain materially represented concrete/abstract referents and content handles, including one-use physical details and source-reified choices/relations/situations/figurative objects. Avoid arbitrary clause nominalization and cross-class shadows whose only job is already represented elsewhere.",
    "LABEL": "Retain source-indexed characterizations/candidate characterizations, including material acceptance/rejection/correction/polarity. Preserve exact posture. Avoid decorative/background modifier census.",
    "VERB": "Recover materially distinct relation edges at atomic predicate grain. Endpoint dependence is allowed. Split coordinated/nested edges when distinct; leave separable arguments and orientation outside the verb. Suppress pure auxiliaries and proposition-sized verb bundles.",
    "LOCATOR": "Recover materially distinct orientation edges, including local position/path/containment/origin-destination/directional particles/context/temporal/comparative orientation. Endpoint dependence is allowed. Separate orientation from VERB when both jobs exist; suppress purely grammatical markers.",
}
