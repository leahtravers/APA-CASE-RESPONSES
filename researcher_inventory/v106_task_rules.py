"""V106 neutral apparatus rules: research-bearing reconnectability.

These rules contain no archetype answers, evaluator findings, expected counts,
prior scored outputs, calibration answers, or holdout material.
"""
from researcher_inventory.v104_task_rules import V104_BASE_RULES, V104_CLASS_RULES

V106_CORRECTION = r'''
V106 PROSPECTIVE CORRECTION — RESEARCH-BEARING RECONNECTABILITY + MINIMAL SUFFICIENT FRAME SET.

V105'S UNIVERSAL RELATION-DECOMPOSITION / CLASS-SLOT TRAVERSAL IS SUPERSEDED FOR NEW WORK. Read the whole source and segment distinguishable represented frames, but DO NOT turn every mapped relation, clause, semantic predicate, or class slot into a primitive candidate. Frame mapping guides selection; it does not generate rows.

RESEARCH-BEARING RECONNECTABILITY GATE: admit a source-present trace only when it performs a distinct class-native research job needed to reconnect represented structure: participant, referential/content handle, source-present characterization, PLACE/TIME episode support, research-bearing relation kernel, or orientation. Lexical occurrence, grammatical predication, semantic interpretability, describability, part of speech, physical/spatial form, or candidate-slot membership never suffices by itself.

MINIMAL SUFFICIENT SET: recover the smallest complete source-native coordinate set that preserves all distinguishable represented research structure. Minimal does not mean globally indispensable: subtle, local, mundane, remembered, reported, prospective, figurative, abstract, concrete, and one-use coordinates remain eligible when they perform a positive research-bearing job. Complete does not mean exhaustive grammar: do not create one row per relation, clause, noun, verb, modifier, temporal token, spatial phrase, sentence, or candidate slot.

VERB DRIVER-VERSUS-CARRIER TEST: retain a predicate only when the relation itself constitutes distinct represented research structure. Reject auxiliary/tense support, copular scaffolding for a characterization already represented elsewhere, existential grammar with no distinct relation, report/speech/cognition frames whose only distinct research content is externalized, discourse/narration carriers, redundant restatements, and proposition-sized wrappers. Copular, reporting, speech, cognition, perception, possession, state, comparison, or simple predicates MAY qualify when that relation itself is a distinct frame driver; verb type alone is never keep/drop evidence.

PLACE/TIME SUPPORT EXCEPTION: first identify source-differentiated episodes/phases, then recover explicit or neutral unnamed support needed to reconnect them. Distinct local, remembered, reported, recurring, intended, prospective, and present-reflection frames may have separate support when the source differentiates them. Merge support doing the same job. Never infer geography or chronology. Never derive support merely from every physical noun, spatial phrase, temporal word, tense, duration, or connective.

FUNCTION BEFORE FORM:
- human/social actor or stable group -> PERSON;
- distinct concrete/abstract referential or content handle -> OBJECT;
- source-present characterization/state/identity/comparison/correction/posture -> LABEL;
- episode/location support -> PLACE;
- period/phase support -> TIME;
- research-bearing frame-driver relation -> VERB;
- relation that distinctly positions/contextualizes another coordinate/frame -> LOCATOR.
Spatial wording is not automatically PLACE. Nominal wording is not automatically OBJECT. Cross-class overlap is allowed only when each projection preserves genuinely different information.

ATOMIC SPAN + LITERAL LOCK: after admission and class resolution, choose the smallest complete exact source-native span for that class-native job. Preserve required particles/prepositions, reflexives, negation, modality, uncertainty, attribution, idiom, comparison, and posture. Never normalize, paraphrase, clean up, lemmatize into a different surface form, or substitute synonyms. Neutral mechanical tags are reserved only for legitimate unnamed PLACE/TIME support where the schema permits null source wording and must be anchored by exact source cues.

FREEZE AUDITS IN ORDER:
1. semantic frame segmentation without clause=frame behavior;
2. reconnectability gate;
3. minimal-sufficient-set / redundancy audit;
4. VERB driver-versus-carrier audit;
5. PLACE/TIME episode-support recovery;
6. functional class assignment;
7. atomic span;
8. anti-tokenization / anti-grammar-census;
9. literal lock;
10. semantic deduplication.
Repeat until stable before compounds.

COMPOUNDS REMAIN DOWNSTREAM. Use frozen canonical refs only and build the smallest selective source-local compound set that adds useful binding for distinct represented frames. No graph closure, pairwise closure, one compound per primitive/clause, singleton-equivalent bundles, subset/superset permutations, redundant restatements, or scene mega-bundles.

Never target hidden counts or infer hidden gold. Never expose approved archetypes, evaluator findings, prior scored outputs, calibration answers, or sealed holdout material. Never perform promotion, APA-ID creation, sovereign/admitted writing, or database mutation.
'''.strip()

V106_BASE_RULES = V104_BASE_RULES + "\n\n" + V106_CORRECTION
V106_CLASS_RULES = dict(V104_CLASS_RULES)
V106_CLASS_RULES.update({
    "PLACE": (
        "Retain explicit settings and distinct local/contained PLACE support only when they support source-differentiated represented episodes, plus neutral unnamed location support when a distinct episode has no explicit place. "
        "Assess support by episode rather than by spatial wording. Merge support doing the same job. Physical objects, surfaces, destinations, movement, scenic nouns, and prepositional phrases are not PLACE unless their research function is episode/location support."
    ),
    "TIME": (
        "Retain explicit periods and distinct semantic episode/phase supports. Recover neutral unnamed support for source-differentiated phases when exact time is unstated, including remembered, reported, recurring, intended, prospective, and present-reflection phases when genuinely distinct. "
        "Merge support doing the same job. Reject tense, every now/then, duration/connective census, temporal-word census, and one-TIME-per-action behavior."
    ),
    "PERSON": (
        "Retain the speaker and each distinct represented human/social actor or stable group after true coreference when the actor performs a participant, possessive, reported, remembered, relational, institutional, or prospective role in represented structure. "
        "Ordinary, one-use, and offscreen actors remain eligible. Suppress aliases and rhetorical/nonreferential addressees."
    ),
    "OBJECT": (
        "Retain concrete or abstract referential/content handles that the source uses as separately reconnectable arguments or anchors in research-bearing relations or independently reifies. "
        "Mundane, local, one-use handles remain eligible when acted on, checked, possessed, selected, contrasted, remembered, reported, considered, exchanged, questioned, decided about, located, or otherwise source-reified. "
        "Reject noun census, incidental scenery, generic pronouns/deixis, discourse organizers, proposition wrappers, and nominal wording whose actual research job is characterization, support, orientation, or grammar."
    ),
    "LABEL": (
        "Retain distinct source-present characterization kernels: qualities, states, identities, comparisons, candidate labels, corrections, polarity, manner, or posture at the smallest complete literal span. "
        "Relational or abstract wording may be LABEL when the source presents it as characterization. Reject modifier/intensifier/colorful-language census, grammar-only descriptions, and proposition wrappers."
    ),
    "VERB": (
        "Retain only research-bearing frame-driver relation kernels at the smallest complete predicate span. Apply the driver-versus-carrier test. "
        "Reject auxiliaries, copular scaffolding, existential grammar, ordinary report/speech/cognition/discourse carriers, redundant restatements, and clause/proposition wrappers when their distinct research content is represented by other coordinates. "
        "Simple/copular/reporting/speech/cognition/perception/possession/state/comparison predicates may still qualify when that relation itself is distinct represented research structure; predicate type alone never decides admission."
    ),
    "LOCATOR": (
        "Retain distinct source-present orienting relations that position/contextualize another coordinate or frame by containment, path, origin/destination, direction, proximity, accompaniment, recurrence, procedure/relation, mental/internal frame, temporal position, or figurative/comparative orientation. "
        "Use the smallest complete literal span. Reject preposition/adverb/recipient/topic/duration/deixis/comparison census, spatial wording whose actual job is OBJECT/PLACE support, and duplicate orientation doing no distinct work."
    ),
})
