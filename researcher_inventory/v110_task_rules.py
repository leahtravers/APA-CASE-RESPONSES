"""V110 neutral apparatus rules: represented-role admission.

These rules contain no archetype answers, evaluator findings, expected counts,
prior scored outputs, calibration answers, or holdout material.
"""
from researcher_inventory.inventory_apparatus import BASE_RULES as APPARATUS_BASE_RULES, CLASS_RULES as APPARATUS_CLASS_RULES

V110_CORRECTION = r'''
V110 PROSPECTIVE CORRECTION — REPRESENTED-ROLE ADMISSION.

READ THE WHOLE SOURCE FIRST. Silently map represented situations and relations: episodes, participants, referred-to/content handles, characterizations/states, event/state relations, scene and phase support, orientations, memories, reports, questions, intentions, alternatives, recurring relations, prospective situations, and present telling/reflection. The map is an omission aid, not a primitive generator.

TWO-GATE ADMISSION:
A) EXACT CLASS-NATIVE IDENTITY: the source establishes the candidate at the smallest complete natural literal span, except legitimate unnamed PLACE/TIME support may use null source_wording with an exact source cue.
B) DISTINCT REPRESENTED ROLE: the candidate has its own role in represented structure as a participant, stable thing/content handle, characterization/state, event/state/relation edge, scene/phase support coordinate, or orientation.

Do NOT ask whether the frame becomes unintelligible without the candidate. A legitimate role may be local, one-use, mundane, neutral, nested, subtle, remembered, reported, prospective, or low-salience. Do NOT prune for importance or summary minimality.

Do NOT admit wording merely because it is independently interpretable, linguistically pointable, typable into a class, descriptive, vivid, spatial, temporal, verbal, nominal, or prepositional. The source must assign it a distinct represented role.

SURFACE-ONLY REJECTION: reject auxiliary/tense/aspect/copular/grammar support with no independent relation role; narration/discourse carriage or sequencing with no represented role; filler, intensification, rhetorical organization, or stylistic color without an independent characterization/state; arbitrary lexical decomposition/token census; free-standing temporal/spatial/deictic wording without a support/orientation role; clause/proposition wrappers whose represented work is already carried by retained coordinates; true duplicates; and restatements that establish no new represented role.

PROJECTION SPLITTING WITHOUT ATOM EXPLOSION: split a larger source span only when it contains genuinely different represented roles. Preserve required particles, complements, reflexives, negation, modality, uncertainty, attribution, comparison, idiom/dialect, and other material needed to keep an admitted role semantically complete. Do not split incidental grammar or style into separate primitives.

FUNCTION BEFORE FORM:
- represented human/social participant -> PERSON;
- stable represented concrete/abstract/internal/relational/content/decision/value/category/figurative handle -> OBJECT;
- represented characterization/state/identity/evaluation/comparison/correction/polarity/manner/posture -> LABEL;
- represented scene/location support -> PLACE;
- represented episode/period/phase support -> TIME;
- represented event/state/relation edge -> VERB;
- represented orientation situating retained structure -> LOCATOR.
Cross-class overlap is allowed only when the same exact span genuinely performs two different represented roles.

PLACE/TIME: these are represented support roles, not token inventories. Preserve each source-differentiated scene/location or episode/period/phase supporting represented material when it has its own support role. Broad and local support may coexist when their roles differ. Legitimate unnamed support may use null source_wording with an exact source cue and neutral tag. Reject physical nouns, destinations, temporal tokens, durations, recurrence words, transitions, tense, and actions that do not themselves establish a distinct support coordinate.

PERSON: retain the speaker and each distinct source-established human/social actor or stable group with a participant role. Direct, offscreen, remembered, reported, relational, institutional, possessive-within-a-material-relation, and prospective participation may qualify. Merge aliases/coreference. Reject rhetorical/generic/nonreferential addressees.

OBJECT: retain each stable represented concrete, abstract, internal, relational, decision/choice-like, value-like, set/category, represented-content, or figurative handle. It may qualify because it is acted on, possessed, exchanged, checked, contrasted, questioned, remembered, reported, selected, decided about, located, valued, or otherwise reified. Reject noun census, generic pronouns/deixis, incidental nouns, arbitrary nominalizations, discourse topics, and proposition wrappers without an independent handle role.

LABEL: retain the smallest complete source-native characterization/state when the source actually assigns or presents a distinct quality, state, identity, evaluation, comparison, candidate/question label, correction, acceptance/rejection, polarity, manner, or posture to represented structure. Local, one-use, idiomatic, colloquial, negated, uncertain, figurative, and comparative roles may qualify. Reject descriptive color, intensification, exclamation, rhetorical flourish, or modifier wording that creates no independent characterization/state role.

VERB: retain the smallest complete source-supported predicate when the source presents a distinct represented event/state/relation edge. Actions, states, attempts, responses, movement, possession, perception, communication/report, cognition, intention, questions, decisions, comparison, evaluation, transition, and location/state relations may qualify. A simple relation may qualify even when one-use or low-salience. Reject auxiliaries, tense/aspect support, and bare copular/grammar shells when all represented work is carried by another retained characterization/content/state and the shell adds no distinct relation identity. Reject discourse organizers, redundant restatements, and oversized proposition wrappers. Preserve particles/complements required for the qualifying relation without swallowing independently typed roles.

LOCATOR: retain a LOCATOR when exact source wording has a distinct orienting role for a retained node, relation, or scene: spatial position, containment, path, direction, origin/destination, proximity, accompaniment, recurrence, procedure/relation, internal/mental context, temporal position, or figurative/comparative orientation. Reject bare prepositions, ordinary argument/topic markers, discourse connectors, unanchored deictics, duplicated TIME support, and free-standing spatial/temporal wording that does not orient retained structure.

ATOMIC SPAN + LITERAL LOCK: for each admitted role use the smallest complete exact contiguous source-native span. Preserve required particles/prepositions, reflexives, essential complements, negation, modality, uncertainty, questions, attribution, comparison, idiom/dialect, and hypothetical/prospective/reported/corrective posture. Never normalize, paraphrase, clean up, lemmatize into a different surface form, or substitute synonyms. Neutral mechanical tags are reserved only for legitimate unnamed PLACE/TIME support and must be anchored by exact source cues.

FREEZE AUDITS: (1) whole-source represented-structure map; (2) represented-role admission audit; (3) omission audit for local/one-use/low-salience/remembered/reported/prospective/nested roles; (4) PLACE/TIME support audit; (5) anti-surface audit removing grammar/auxiliary/discourse/rhetoric/style/lexical census/unanchored temporal-spatial fragments; (6) projection splitting only for genuinely different roles; (7) functional-class audit; (8) atomic-span audit; (9) literal-lock audit; (10) semantic-deduplication audit. Repeat until stable before compounds.

RELATION-INSTANCE COMPOUNDS: after primitives freeze, reread relation by relation. For each retained VERB relation instance, emit the smallest complete compound linking only frozen role-bearing coordinates that actually participate in that exact represented relation. Add participant/content/support/orientation/characterization refs only when they play a role in that relation. Additional non-VERB compounds are allowed only for represented relation/state structure not already captured by a retained VERB relation. Do not emit graph closure, arbitrary co-occurrence bundles, singleton equivalents, generic question closure, duplicate restatements, subset/superset permutations, scene mega-bundles, or compounds containing rejected surface fragments.

Never target hidden counts or infer hidden gold. Never expose approved archetypes, evaluator findings, prior scored outputs, calibration answers, or sealed holdout material. Never perform promotion, Oval Office admission, APA-ID creation, sovereign/admitted writing, or database mutation.
'''.strip()

V110_BASE_RULES = APPARATUS_BASE_RULES + "\n\n" + V110_CORRECTION
V110_CLASS_RULES = dict(APPARATUS_CLASS_RULES)
V110_CLASS_RULES.update({
    "PLACE": "Retain each distinct source-established scene/location support role used by represented material. Broad and contained support may coexist only when they serve different represented support roles. Supported unnamed PLACE may use null source_wording with exact source_cue and a neutral tag. Reject physical nouns, destinations, spatial phrases, and incidental settings that do not establish a distinct scene/location support role.",
    "TIME": "Retain each distinct source-established episode/period/phase support role used by represented material, including legitimate remembered, reported, recurring, prospective, and present-reflection phases. Supported unnamed TIME may use null source_wording with exact source_cue and a neutral tag. Reject temporal-token, duration, tense, transition, recurrence-word, or one-time-per-action census behavior when no distinct phase support role exists.",
    "PERSON": "Retain the speaker and each distinct represented human/social actor or stable group with a participant role after true coreference. Direct, offscreen, remembered, reported, institutional, relational, possessive-within-a-material-relation, and prospective participation may qualify. Reject rhetorical/generic/nonreferential addressees.",
    "OBJECT": "Retain each stable represented concrete, abstract, internal, relational, decision/choice-like, value-like, set/category, represented-content, or figurative handle that has its own thing/content role. Reject noun census, generic pronouns/deixis, incidental nouns, arbitrary nominalizations, discourse topics, and proposition wrappers without an independent handle role.",
    "LABEL": "Retain each smallest complete source-present characterization/state/identity/evaluation/comparison/correction/polarity/manner/posture that has its own represented characterization role. Local, one-use, idiomatic, figurative, comparative, uncertain, negated, and colloquial roles may qualify. Reject descriptive color, intensification, exclamation, rhetorical flourish, and modifiers with no independent characterization/state role.",
    "VERB": "Retain each smallest complete source-supported event/state/relation predicate that has its own represented relation-edge role. Simple actions/states, possession, perception, communication/report, cognition, intention, questions, decisions, comparisons, evaluations, movement, location/state relations, and transitions may qualify. Reject auxiliaries, tense/aspect support, bare copular/grammar shells with no independent relation identity, discourse organizers, redundant restatements, and oversized proposition wrappers. Preserve required particles/complements for the relation itself without swallowing independently typed roles.",
    "LOCATOR": "Retain each smallest complete exact orientation with its own role situating a retained node, relation, or scene, including position, containment, path, direction, origin/destination, proximity, accompaniment, recurrence, procedure/relation, internal/mental context, temporal position, and figurative/comparative orientation. Reject bare prepositions, argument/topic markers, discourse connectors, unanchored deictics, duplicated TIME support, and free-standing spatial/temporal wording with no distinct orienting role.",
})
