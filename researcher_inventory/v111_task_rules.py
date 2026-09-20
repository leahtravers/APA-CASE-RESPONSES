"""V111 neutral apparatus rules: independent research-coordinate admission.

These rules contain no archetype answers, evaluator findings, expected counts,
prior scored outputs, calibration answers, or holdout material.
"""
from researcher_inventory.inventory_apparatus import BASE_RULES as APPARATUS_BASE_RULES, CLASS_RULES as APPARATUS_CLASS_RULES

V111_CORRECTION = r'''
V111 PROSPECTIVE CORRECTION — INDEPENDENT RESEARCH-COORDINATE ADMISSION.

READ THE WHOLE SOURCE FIRST. Silently map source-differentiated episodes/scenes, participants, referred-to or acted-on handles, characterizations/states, relation edges, orientations, memories, reports, questions, intentions, alternatives, recurring relations, prospective situations, and present reflection. This map is an omission aid, not a primitive generator.

TWO-GATE ADMISSION:
A) EXACT CLASS-NATIVE IDENTITY: the source establishes the candidate at the smallest complete natural literal span, except legitimate unnamed PLACE/TIME support may use null source_wording with an exact source cue and neutral tag.
B) INDEPENDENT RESEARCH COORDINATE: the candidate supplies a distinct dimension of represented experience that a researcher could code or track separately from neighboring wording and already-retained coordinates.

Do NOT require importance, centrality, recurrence, or indispensability. A legitimate coordinate may be local, one-use, mundane, neutral, nested, subtle, remembered, reported, prospective, or low-salience. Do NOT prune merely because the broader frame remains intelligible without it.

Do NOT admit wording merely because it is independently interpretable, semantically real, grammatically identifiable, descriptive, vivid, spatial, temporal, verbal, nominal, or prepositional. Ask whether retaining it gives the researcher a separate codeable dimension rather than another lexical realization, incidental detail, or fragment of a dimension already represented.

REJECT NON-COORDINATE DETAIL: reject auxiliaries/tense/aspect/copular grammar with no separate relation axis; narration/discourse carriage or sequencing with no separately codeable relation; incidental scene dressing or props; intensification, rhetoric, stylistic color, or descriptive detail without a separate state/handle axis; arbitrary lexical/POS decomposition; free-standing temporal/spatial/deictic wording without differentiated support/orientation identity; proposition wrappers whose research work is already carried by retained coordinates; true duplicates; and restatements that create no new research coordinate.

PROJECTION SPLITTING WITHOUT ATOM EXPLOSION: split a larger span only when it contains genuinely different independent research coordinates. Preserve required particles, complements, reflexives, negation, modality, uncertainty, attribution, comparison, idiom/dialect, and other material necessary to keep an admitted coordinate semantically complete. Do not split grammar, incidental modifiers, scene dressing, or style into primitives.

FUNCTION BEFORE FORM:
- represented human/social participant coordinate -> PERSON;
- stable concrete/abstract/internal/relational/content/decision/value/category/figurative handle coordinate -> OBJECT;
- separately trackable characterization/state/identity/evaluation/comparison/posture coordinate -> LABEL;
- differentiated scene/location support coordinate -> PLACE;
- differentiated episode/period/phase support coordinate -> TIME;
- separately trackable event/state/relation edge -> VERB;
- separately trackable orientation situating retained structure -> LOCATOR.
Cross-class overlap is allowed only when the exact same source span genuinely supplies two different independent research coordinates.

PLACE/TIME: preserve each source-differentiated scene/location or episode/period/phase that functions as a separate support coordinate. Broad and local support may coexist only when they are genuinely different support dimensions. Legitimate unnamed support may use null source_wording with an exact source cue and neutral tag. Reject physical nouns, destinations, temporal tokens, durations, recurrence words, transitions, tense, and actions that do not themselves establish a separate support coordinate.

PERSON: retain the speaker and each distinct source-established human/social actor or stable group that forms a participant coordinate after true coreference. Direct, offscreen, remembered, reported, institutional, relational, possessive-within-a-material-relation, and prospective participation may qualify. Reject rhetorical/generic/nonreferential addressees and incidental mentions without a participant axis.

OBJECT: retain each stable represented concrete, abstract, internal, relational, decision/choice-like, value-like, set/category, content, or figurative handle that forms its own research coordinate. Reject noun census, generic pronouns/deixis, incidental props, arbitrary nominalizations, discourse topics, and proposition wrappers without a separate handle axis.

LABEL: retain the smallest complete source-present characterization/state/identity/evaluation/comparison/correction/polarity/manner/posture that forms a separate research coordinate. Local, one-use, idiomatic, figurative, comparative, uncertain, negated, and colloquial roles may qualify. Reject descriptive color, intensification, exclamation, rhetorical flourish, and modifiers that merely decorate another coordinate.

VERB: retain the smallest complete source-supported event/state/relation predicate that forms a separately trackable relation axis. Actions, states, attempts, responses, movement, possession, perception, communication/report, cognition, intention, questions, decisions, comparisons, evaluations, transitions, and location/state relations may qualify. Reject auxiliaries, tense/aspect support, bare copular/grammar shells, discourse organizers, stylistic narration, redundant restatements, and incidental predicates that add no separate relation dimension. Preserve required particles/complements for the relation itself without swallowing independently typed coordinates.

LOCATOR: retain the smallest complete exact orientation that separately situates a retained node, relation, or scene by position, containment, path, direction, origin/destination, proximity, accompaniment, recurrence, procedure/relation, internal/mental context, temporal position, or figurative/comparative orientation. Reject bare prepositions, argument/topic markers, discourse connectors, unanchored deictics, duplicated TIME support, and decorative/redundant orientation wording.

ATOMIC SPAN + LITERAL LOCK: use the smallest complete exact contiguous source-native span for each admitted coordinate. Preserve required particles/prepositions, reflexives, complements, negation, modality, uncertainty, questions, attribution, comparison, idiom/dialect, and hypothetical/prospective/reported/corrective posture. Never normalize, paraphrase, clean up, lemmatize into a different form, or substitute synonyms. Neutral mechanical tags are reserved only for legitimate unnamed PLACE/TIME support anchored by exact source cues.

FREEZE AUDITS: (1) whole-source experience map; (2) research-coordinate audit; (3) omission audit for local/one-use/low-salience/remembered/reported/prospective/nested axes; (4) PLACE/TIME support audit; (5) anti-census audit removing grammar/discourse/incidental props/style/lexical decomposition/non-coordinate temporal-spatial fragments; (6) projection splitting only for genuinely different coordinates; (7) functional-class audit; (8) atomic-span audit; (9) literal-lock audit; (10) semantic-deduplication audit. Repeat until stable before compounds.

RELATION-INSTANCE COMPOUNDS: after primitives freeze, reread relation by relation. For each retained VERB relation instance, emit the smallest complete compound linking only frozen coordinates that actually participate in that exact relation. Add participant/content/support/orientation/characterization refs only when they play a role in that relation. Additional non-VERB compounds are allowed only for represented relation/state structure not already captured by a retained VERB relation. Do not emit graph closure, arbitrary co-occurrence bundles, singleton equivalents, generic question closure, duplicate restatements, subset/superset permutations, scene mega-bundles, or compounds containing rejected non-coordinate details.

Never target hidden counts or infer hidden gold. Never expose approved archetypes, evaluator findings, prior scored outputs, calibration answers, or sealed holdout material. Never perform promotion, Oval Office admission, APA-ID creation, sovereign/admitted writing, or database mutation.
'''.strip()

V111_BASE_RULES = APPARATUS_BASE_RULES + "\n\n" + V111_CORRECTION
V111_CLASS_RULES = dict(APPARATUS_CLASS_RULES)
V111_CLASS_RULES.update({
    "PLACE": "Retain each distinct source-established scene/location that functions as a separate research support coordinate. Broad and contained support may coexist only when their research roles differ. Supported unnamed PLACE may use null source_wording with exact source_cue and a neutral tag. Reject physical nouns, destinations, spatial phrases, incidental settings, and scene dressing that do not establish a separate support axis.",
    "TIME": "Retain each distinct source-established episode/period/phase that functions as a separate research support coordinate, including legitimate remembered, reported, recurring, prospective, and present-reflection phases. Supported unnamed TIME may use null source_wording with exact source_cue and a neutral tag. Reject temporal-token, duration, tense, transition, recurrence-word, or one-time-per-action census behavior when no separate phase axis exists.",
    "PERSON": "Retain the speaker and each distinct represented human/social actor or stable group that forms a participant coordinate after true coreference. Direct, offscreen, remembered, reported, institutional, relational, possessive-within-a-material-relation, and prospective participation may qualify. Reject rhetorical/generic/nonreferential addressees and incidental mentions without a participant axis.",
    "OBJECT": "Retain each stable represented concrete, abstract, internal, relational, decision/choice-like, value-like, set/category, content, or figurative handle that forms its own research coordinate. Reject noun census, generic pronouns/deixis, incidental props, arbitrary nominalizations, discourse topics, and proposition wrappers without a separate handle axis.",
    "LABEL": "Retain each smallest complete source-present characterization/state/identity/evaluation/comparison/correction/polarity/manner/posture that forms a separately trackable research coordinate. Local, one-use, idiomatic, figurative, comparative, uncertain, negated, and colloquial coordinates may qualify. Reject descriptive color, intensification, exclamation, rhetorical flourish, and modifiers that merely decorate another coordinate.",
    "VERB": "Retain each smallest complete source-supported event/state/relation predicate that forms a separately trackable relation coordinate. Simple actions/states, possession, perception, communication/report, cognition, intention, questions, decisions, comparisons, evaluations, movement, location/state relations, and transitions may qualify. Reject auxiliaries, tense/aspect support, bare copular/grammar shells, discourse organizers, stylistic narration, redundant restatements, and incidental predicates that add no separate relation dimension. Preserve required particles/complements without swallowing independently typed coordinates.",
    "LOCATOR": "Retain each smallest complete exact orientation that forms a separate research coordinate situating a retained node, relation, or scene by position, containment, path, direction, origin/destination, proximity, accompaniment, recurrence, procedure/relation, internal/mental context, temporal position, or figurative/comparative orientation. Reject bare prepositions, argument/topic markers, discourse connectors, unanchored deictics, duplicated TIME support, and decorative or redundant orientation wording.",
})
