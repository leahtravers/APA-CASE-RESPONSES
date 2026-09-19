"""V102 neutral apparatus rules: lightweight research-handle resolution.

These rules contain no archetype answers, evaluator findings, expected counts,
prior scored outputs, or holdout material.
"""
from researcher_inventory.v100_task_rules import V100_BASE_RULES, V100_CLASS_RULES

V102_CORRECTION = r'''
V102 PROSPECTIVE CORRECTION — LIGHTWEIGHT RESEARCH-HANDLE RESOLUTION.

This correction supersedes V101's broad eligibility rule for ordinary concrete, low-salience, and one-use referents. Source mention, lexical category, concreteness, vividness, one-use occurrence, or grammatical separability never suffices by itself.

FIRST map materially distinct source relations/frames across the complete source. THEN admit only the smallest class-native coordinates whose removal would lose a materially distinct reconnectable research handle or a necessary PLACE/TIME support or LOCATOR orientation facet. THEN compress incidental lexical remainder. Freeze primitives. ONLY AFTERWARD build selective compounds.

RESEARCH-HANDLE TEST:
For every proposed primitive ask: if this row disappeared while all other retained rows remained, would a researcher lose materially distinct source structure and have to invent a substitute to reconnect it? If yes, retain it at complete semantic grain. If removing it loses only lexical/descriptive detail, omit it.

VALID ADMISSION ROUTES:
- MATERIAL_CORE: performs a distinct class-native role in a materially represented source relation/frame.
- INDEPENDENT_HANDLE: source treats it as independently revisitable through stable coreference/reuse, explicit naming/contrast/question/correction/characterization, meaningful participation as argument/endpoint/content/orientation/support, or material phase distinction.
- IMPLICIT_SUPPORT: PLACE/TIME only, for a materially distinct episode/relation/frame that needs a support slot when exact place/time is unnamed.

ANTI-TOKENIZATION:
Do not inventory words just because they are nouns, verbs, adjectives, adverbs, prepositions, concrete entities, one-use mentions, vivid details, temporal expressions, or segmentable phrases. No noun census, verb census, modifier census, spatial-phrase census, or temporal-phrase census.

SEMANTIC COMPLETENESS:
Compression must not erase real source structure. Restore subtle, local, one-use, abstract, prospective, remembered, figurative, or unnamed coordinates when they actually perform a material research role. Especially audit PLACE/TIME for needed semantic support frames that have no explicit place/time token.

PROPOSITION DE-BUNDLING:
A clause contains coordinates but is not automatically a primitive. VERB uses the shortest complete material relation kernel. LABEL uses a complete independent characterization unit. OBJECT uses a source-reified referential/content handle. LOCATOR uses an independently useful orientation relation. Do not return proposition wrappers when smaller class-native units preserve the research job.

LITERAL LOCK:
For admitted source-derived rows preserve exact wording, dialect, contractions, numbers, uncertainty, negation, modality, comparison, attribution, punctuation, and figurative posture. Lexical preservation applies to admitted rows; it is not lexical exhaustivity.

COMPOUNDS:
Build only the smallest canonical set of materially useful multi-coordinate source-local bindings from frozen primitives. Do not produce graph closure, one compound per primitive, one compound per clause, pairwise combinations, subset/superset variants, redundant restatements, or scene mega-bundles.

Never target hidden counts or infer hidden gold. Never expose approved archetypes, evaluator findings, prior scored outputs, calibration answers, or sealed holdout material. Never perform promotion, APA-ID creation, sovereign/admitted writing, or database mutation.
'''.strip()

V102_BASE_RULES = V100_BASE_RULES + "\n\n" + V102_CORRECTION

V102_CLASS_RULES = dict(V100_CLASS_RULES)
V102_CLASS_RULES.update({
    "PLACE": (
        "Lightweight PLACE: retain settings/location supports that materially locate represented relations or episodes. "
        "Keep explicit broad/local settings only when they do different research work, and restore neutral unnamed support for materially distinct episodes when needed. "
        "Do not inventory every physical noun, surface, container, movement, spatial phrase, or clause location."
    ),
    "TIME": (
        "Lightweight TIME: retain semantic episode/span frames that materially distinguish represented phases such as attempts, responses, waits, later conversations/reports, recurring spans, reflections, intentions, alternatives, or prospects. "
        "Merge surface temporal expressions serving one frame and use neutral implicit support when a distinct frame is unnamed. "
        "Do not inventory tense, every now/then, every duration/connective, or one TIME per clause/action."
    ),
    "PERSON": (
        "Retain the speaker and each distinct human/social actor or stable group that performs a material actor, counterpart, possessor, beneficiary, reported/remembered, institutional, or prospective-endpoint role after true coreference. "
        "Minor or one-use actors may qualify, but grammatical mention alone does not. Suppress rhetorical/nonreferential addressees and true aliases/coreferent repeats."
    ),
    "OBJECT": (
        "Lightweight OBJECT: retain concrete or abstract referential/content handles whose removal would lose a materially distinct source relation or independently revisitable handle. "
        "Concrete items qualify when they meaningfully participate in checking, choosing, acting, contrasting, referencing, or another retained relation; incidental scenery and one-use nouns do not qualify merely because concrete. "
        "Abstract choices, decisions, relations, conditions, amounts, alternatives, or internal objects qualify when source-reified. Reject noun-phrase census, generic anaphora, clause wrappers, discourse organizers, and incidental detail."
    ),
    "LABEL": (
        "Lightweight LABEL: retain smallest complete source-presented characterization, state, identity, comparison, candidate/correction, acceptance/rejection, or polarity unit only when it performs an independent research job. "
        "Do not inventory every adjective, adverb, intensifier, colorful descriptor, or rhetorical phrase. Preserve competing/revised characterization units separately when the source treats them as distinct."
    ),
    "VERB": (
        "Lightweight VERB: retain shortest complete source-native semantic relation kernels for materially distinct relations, not raw verb tokens and not every grammatical predicate. "
        "Normally omit subjects and externalize retained participants/content/labels/place/time/locator arguments; keep particles, reflexives, required prepositions, negation, modality, light-verb support, or complements only when required for relation identity/posture. "
        "Suppress auxiliary/discourse/reporting/cognition tokens when removing them loses no distinct research relation; retain them when they actually carry one."
    ),
    "LOCATOR": (
        "Lightweight LOCATOR: retain source-native orientation/topology relations that materially position one represented coordinate relative to another coordinate or frame. "
        "Use smallest complete orienting constructions for position/containment, origin/destination/path, movement direction, proximity, meaningful accompaniment, recurrence/context, or figurative/comparative orientation. "
        "Reject every-preposition/adverb census, recipients/addressees, mere topics, durations, discourse deixis, and spatial/comparative wording with no independent orientation job."
    ),
})
