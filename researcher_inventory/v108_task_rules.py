"""V108 neutral apparatus rules: local-frame research-node admission.

These rules contain no archetype answers, evaluator findings, expected counts,
prior scored outputs, calibration answers, or holdout material.
"""
from researcher_inventory.inventory_apparatus import BASE_RULES as APPARATUS_BASE_RULES, CLASS_RULES as APPARATUS_CLASS_RULES

V108_CORRECTION = r'''
V108 PROSPECTIVE CORRECTION — LOCAL-FRAME RESEARCH-NODE ADMISSION.

READ THE WHOLE SOURCE FIRST. Silently map source-differentiated local frames: represented episodes, interactions, waits, attempts, responses, memories, reports, comparisons, questions, decisions, intentions, prospective situations, recurring relations, and present reflection. A frame is a represented situation/relation structure, not a sentence or clause. Frame mapping is an omission aid, not a primitive generator.

TWO-GATE ADMISSION: retain a primitive only when (A) it has a complete class-native source identity and (B) it occupies a distinct represented research role inside at least one local frame: participant, referential/content handle, characterization/state, event/state/relation edge, scene/phase support, or structure-binding orientation.

LOCAL FRAME-LOSS TEST: mentally remove the candidate while leaving the rest of its local frame intact. Retain it when the represented frame loses a distinct who/what/state/relation/where/when/orientation. Reject it when only wording, grammar, discourse carriage, rhetorical presentation, stylistic color, emphasis, or a redundant projection is lost. Apply this test locally, not against the whole narrative: one-use, mundane, background, nested, reported, remembered, prospective, subtle, figurative, and low-salience roles may qualify.

INDEPENDENT POINTABILITY IS NOT SUFFICIENT. Semantic interpretability, lexical separability, part of speech, describability, possible analyst usefulness, or the ability to point to a phrase does not itself create a primitive. Do not turn every noun, predicate, description, temporal phrase, spatial phrase, preposition, speech act, cognition phrase, or clause into a coordinate.

LOCAL COMPLETENESS: within each differentiated frame preserve all distinct research roles that pass both gates. Do not prune a legitimate local role merely because a broad narrative can still be summarized. Do not let a future compound justify admission.

FUNCTION BEFORE FORM:
- represented human/social participant -> PERSON;
- frame-participating or separately reified concrete/abstract/content handle -> OBJECT;
- represented characterization/state/identity/evaluation/comparison/correction/polarity/manner/posture -> LABEL;
- scene/location support -> PLACE;
- episode/phase support -> TIME;
- represented event/state/relation edge -> VERB;
- orientation binding a retained node/relation/frame -> LOCATOR.
Surface grammar does not decide class. Cross-class overlap is allowed only when each projection performs a genuinely different represented job.

PLACE/TIME: preserve differentiated scene/phase support, including legitimate unnamed support. Broad and local support may coexist only when they do different frame-support work. Merge multiple cues for one support identity. Do not infer geography/chronology and do not inventory physical nouns, destination phrases, temporal tokens, durations, transitions, recurrence words, tense, or actions.

PERSON: retain actual represented actors/stable groups, including one-use, offscreen, possessive, remembered, reported, institutional, relational, and prospective actors. Merge coreference. Reject rhetorical/generic/nonreferential addressees.

OBJECT: retain frame-participating or separately reified handles that are acted on, possessed, exchanged, checked, contrasted, questioned, remembered, reported, selected, decided about, located, valued, or otherwise represented as distinct content/things. Reject noun census, generic pronouns/deixis, discourse topics, arbitrary nominalizations, and proposition wrappers without independent represented handle identity.

LABEL: retain characterizations/states/identities/evaluations/comparisons/corrections/polarities/manners/postures whose removal changes represented local state. Reject vivid wording, intensification, rhetorical flourish, and descriptive/modifier vocabulary with no independent represented characterization.

VERB: retain the smallest complete predicate/relation span only when it is a represented event/state/relation edge in a local frame. Simple actions/states, possession, perception, communication/report, cognition, intention, questions, decisions, comparisons, evaluations, movements, and transitions may qualify when the relation itself changes represented structure. Reject auxiliaries, tense/aspect support, copular shells whose work is exhausted by another coordinate, narration/discourse organizers, generic existential/presentation shells, routine report/speech/cognition carriers that add no distinct attribution/perspective/relation edge, proposition wrappers, redundant restatements, and predicate-like grammar fragments.

LOCATOR: retain only orientations that bind a retained node, event/state edge, or frame by spatial position, containment, path, direction, origin/destination, proximity, accompaniment, recurrence, procedure/relation, internal/mental context, temporal position, or figurative/comparative orientation. Reject bare prepositions, ordinary argument/topic markers, discourse connectors, duplicate deictics, duration phrases already represented as TIME, and free-standing spatial/temporal wording with no distinct binding job.

ATOMIC SPAN + LITERAL LOCK: after admission and class resolution use the smallest complete exact contiguous source-native span. Preserve required particles/prepositions, reflexives, essential complements, negation, modality, uncertainty, questions, attribution, comparison, idiom/dialect, and hypothetical/prospective/reported/corrective posture. Never normalize, paraphrase, clean up, lemmatize into a different surface form, or substitute synonyms. Neutral mechanical tags are reserved only for legitimate unnamed PLACE/TIME support and must be anchored by exact source cues.

FREEZE AUDITS: (1) whole-source frame map; (2) local omission scan; (3) two-gate admission; (4) local frame-loss excess removal; (5) PLACE/TIME support; (6) VERB edge/carrier; (7) functional class; (8) atomic span; (9) anti-census; (10) literal lock; (11) semantic deduplication. Repeat until stable before compounds.

COMPOUNDS: only after all primitives are frozen, emit a lightweight set of distinct source-presented local-frame relation instances connecting two or more frozen coordinates. A compound corresponds to a represented proposition/relation edge, not mere co-occurrence. Use the smallest complete set of refs preserving participants/content/support/orientation, direction, and posture. No graph closure, every-pair closure, every grammatical clause, one-compound-per-primitive, arbitrary bundles, singleton equivalents, subset/superset permutations, duplicate restatements, generic question closure, or scene mega-bundles. Compounds never justify primitive defects.

Never target hidden counts or infer hidden gold. Never expose approved archetypes, evaluator findings, prior scored outputs, calibration answers, or sealed holdout material. Never perform promotion, Oval Office admission, APA-ID creation, sovereign/admitted writing, or database mutation.
'''.strip()

V108_BASE_RULES = APPARATUS_BASE_RULES + "\n\n" + V108_CORRECTION
V108_CLASS_RULES = dict(APPARATUS_CLASS_RULES)
V108_CLASS_RULES.update({
    "PLACE": "Retain distinct source-established scene/location support that changes the representation of a differentiated local frame. Broad and local support may coexist only when they do different frame-support work. Supported unnamed PLACE may use null source_wording with exact source_cue and a neutral tag. Reject physical/spatial wording that is merely referential, orienting, or incidental.",
    "TIME": "Retain distinct source-established episode/phase support that changes the representation of a differentiated local frame, including legitimate remembered/reported/recurring/prospective/present-reflection support. Merge cues doing the same support job. Supported unnamed TIME may use null source_wording with exact source_cue and a neutral tag. Reject temporal-token, duration, tense, transition, or one-time-per-action census behavior.",
    "PERSON": "Retain the speaker and each distinct represented human/social actor or stable group after true coreference when the actor occupies a participant role in a local frame. One-use, offscreen, possessive, remembered, reported, institutional, relational, and prospective actors may qualify. Reject rhetorical/generic/nonreferential addressees.",
    "OBJECT": "Retain each frame-participating or separately reified concrete, abstract, internal, relational, decision/choice-like, value-like, set/category, represented-content, or figurative handle. A handle normally qualifies because it is acted on, possessed, checked, contrasted, questioned, remembered, reported, selected, decided about, located, valued, or otherwise represented as distinct. Reject noun census, generic pronouns/deixis, discourse topics, arbitrary nominalizations, incidental wording, and proposition wrappers without independent represented handle identity.",
    "LABEL": "Retain each distinct source-presented characterization/state/identity/evaluation/comparison/correction/polarity/manner/posture whose removal changes represented local state. Local, one-use, idiomatic, figurative, comparative, uncertain, negated, and colloquial characterizations may qualify. Reject intensifier/modifier/colorful-language/rhetorical census and wording with no independent represented characterization.",
    "VERB": "Retain each smallest complete source-supported event/state/relation edge whose removal changes represented local structure. Simple actions/states, possession, perception, communication/report, cognition, intention, questions, decisions, comparisons, evaluations, movement, and transitions may qualify when the relation itself is represented. Reject auxiliaries, tense/aspect support, grammar-only copular shells, narration/discourse organizers, generic presentation/existential shells, routine carriers that add no distinct attribution/perspective/edge, proposition wrappers, redundant restatements, and predicate-like grammar fragments.",
    "LOCATOR": "Retain each distinct smallest complete orientation that binds a retained node, event/state edge, or local frame and whose removal changes represented positioning/context. Spatial, containment, path, direction, origin/destination, proximity, accompaniment, recurrence, procedure/relation, internal/mental, temporal-position, and figurative/comparative orientations may qualify. Reject bare prepositions, ordinary argument/topic markers, discourse connectors, duplicate deictics, TIME-duplicate duration phrases, and free-standing orientation wording with no distinct binding job.",
})
