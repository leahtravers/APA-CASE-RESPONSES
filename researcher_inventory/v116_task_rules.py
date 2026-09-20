"""V116 neutral apparatus rules: relation-slot closure at natural class grain.

No archetype answers, evaluator findings, expected counts, prior scored outputs,
calibration answers, or holdout material are included here.
"""
from researcher_inventory.inventory_apparatus import BASE_RULES as APPARATUS_BASE_RULES, CLASS_RULES as APPARATUS_CLASS_RULES

V116_CORRECTION = r'''
V116 PROSPECTIVE CORRECTION — RELATION-SLOT CLOSURE AT NATURAL CLASS GRAIN.

READ THE WHOLE SOURCE FIRST. Reconstruct the source as ordered MATERIAL REPRESENTED RELATION/BINDING INSTANCES, not as sentences, token lists, a summary, or an exhaustive graph. A relation instance is a source-presented action, state, communication, cognition, question, intention, possession, movement, comparison, evaluation, characterization, remembered/reported occurrence, prospective occurrence, or other represented relation connecting class-native roles.

LIGHTWEIGHT DOES NOT MEAN HIGH-SALIENCE ONLY. A slot may be one-use, local, nested, mundane, low-salience, remembered, reported, prospective, uncertain, negated, figurative, or colloquial. Recurrence, broad importance, later reuse, and narrative centrality are never required.

BUT MEANINGFUL WORDING IS NOT AUTOMATICALLY A SLOT. Source presence, semantic content, grammatical separability, local typability, a noun/verb/adjective/preposition form, or membership in a clause is insufficient by itself.

RELATION-SLOT ADMISSION TEST:
A) SOURCE GROUNDING: source establishes the coordinate in the requested class, or establishes a legitimate unnamed PLACE/TIME support slot.
B) CLASS-NATIVE FUNCTION: candidate performs the represented job of that class.
C) RELATION-SLOT ENTITLEMENT: candidate occupies a distinct slot in at least one represented relation instance. Ask: WHAT EXACT CLASS-NATIVE SLOT DOES THIS CANDIDATE FILL IN THE REPRESENTED RELATION? If no answer exists without analyst paraphrase, reject it.
D) NATURAL GRAIN: retain the slot itself, not wording nested inside it and not a larger clause wrapper around it. Use the smallest complete source-native span preserving slot identity.
E) CLASS-LOCAL DISTINCTNESS: resolve true coreference, aliases, and same-class restatements. Do not merge genuinely different slots merely because they share a scene, episode, target, or relation family.

FOR EACH RELATION INSTANCE, inspect only the slots the source actually establishes:
- human/social participant -> PERSON
- tracked referent/content -> OBJECT
- applied characterization/state/evaluation -> LABEL
- operative relation kernel -> VERB
- independent orientation -> LOCATOR
- spatial occurrence support -> PLACE
- temporal episode/phase support -> TIME

SYMMETRIC CLOSURE AUDIT BEFORE FREEZE:
MISSING-SLOT SIDE: replay every relation instance and verify every class-native slot actually established by the source is represented, including local/one-use/nested/remembered/reported/prospective/uncertain/negated and unnamed-support roles.
EXCESS-SLOT SIDE: every proposed primitive must name the relation instance and class-native slot that licenses it. Remove it when it is merely wording inside another slot, a grammatical argument with no independent class role, a non-reified clause wrapper, modifier fragment, generic PP/recipient/topic/purpose phrase, lexical verb token that is not the relation kernel, physical noun mistaken for support, temporal wording mistaken for an episode, discourse/filler/auxiliary/tense machinery, or analyst interpretation.

PLACE: retain each spatial support coordinate differentiated enough by the source to reconnect a represented relation instance. A distinct occurrence-position may exist inside one broader physical setting when the source distinguishes participant position, destination, waiting position, later interaction position, remembered/prospective position, or another local support role. Several relation instances may share one PLACE when support is not differentiated. Unnamed PLACE is allowed only when the source establishes a distinct support slot without naming physical details. Do not turn every physical noun/surface/object part/path phrase into PLACE.

TIME: retain each temporal support coordinate differentiated enough to reconnect a represented relation instance: episode, phase, period, recurrence frame, remembered/reported episode, intended/prospective period, present-reflection episode. Several relations may share one TIME; a broad episode does not erase a source-differentiated local temporal support. Unnamed TIME is allowed only when the source establishes a distinct episode/phase without naming it. Do not create TIME from every clause, predicate, tense, transition, question, or duration phrase.

PERSON: retain speaker plus every distinct represented human/social actor or stable group after true coreference when it occupies a participant slot. Direct, offscreen, relational, possessive/beneficiary, remembered, reported, institutional, prospective, peripheral, and one-use actors may qualify. Reject only generic/rhetorical/nonreferential person wording that never becomes a represented participant.

OBJECT: retain each concrete or abstract referent/content handle occupying a tracked slot in a represented relation: something acted on, possessed, exchanged, located, checked, compared, selected, rejected, remembered, reported, contemplated, valued, or otherwise related as a thing/content node. One-use/low-salience slots qualify. Decisions, plans, relations, values, sets, internal content, and proposition-like content qualify only when the source itself reifies/tracks them as referential handles. Do not nominalize every clause, question, intention, grammatical argument, or discourse point.

LABEL: retain each smallest complete source-applied characterization/state/status/identity/evaluation/comparison/candidate label/rejection/correction or materially distinct manner/posture that occupies a characterization slot. One-use, colloquial, idiomatic, uncertain, questioned, negated, corrected, rejected, and figurative labels may qualify. Choose the natural complete judgment unit. Do not inventory every adjective, adverb, intensifier, modifier, discourse stance, or rhetorical flourish.

VERB: retain one minimal complete literal predicate kernel for each distinct represented relation instance carrying an operative lexical relation. Actions, states, stances, cognitions, perceptions, reports/communications, intentions, questions, decisions, possessions, comparisons, evaluations, movements, transitions, gestures, existence/location, obligation, and low-salience relations may qualify. Preserve particles/reflexives/negation/modality/bound complements only when required for relation identity. Split nested/coordinated predicates only when the source presents genuinely distinct relation instances. Reject auxiliaries/tense-aspect support, copular carriage with no separate relation, discourse/filler predicates, duplicate restatements, and lexical verb tokens nested inside a stronger natural relation kernel.

LOCATOR: retain each smallest complete exact span occupying an independent orientation slot: position, path, origin/destination, direction, containment, proximity, accompaniment/carrying, entry/exit, internal/mental/relational position, recurrence/context, or materially spatialized figurative/comparative orientation. It must orient a retained participant/referent/relation/frame. Do not inventory every prepositional, recipient/topic/purpose, possession, degree, temporal, or generic adverbial phrase.

LITERAL LOCK: use the smallest complete exact contiguous source-native span preserving each explicit coordinate's identity. Preserve negation, modality, uncertainty, question form, attribution, comparison, idiom/dialect, reported/recalled posture, hypothetical/prospective posture, correction/rejection, particles, reflexives, and bound complements when needed. Every non-null source_wording/source_cue/order_cue must be exact source text. Never normalize, paraphrase, clean up, translate, diagnose, euphemize, lemmatize into a different form, or substitute synonyms.

PRIMITIVE FREEZE: replay relation instances; close missing slots; remove wording-only excess; verify PLACE/TIME support grain; verify functional typing; verify natural complete spans; resolve coreference/same-class duplicates; order by first source establishment subject to apparatus rules; then freeze all seven ledgers. Never target hidden counts or infer hidden gold.

COMPOUNDS: after primitive freeze, serialize materially distinct represented relation instances. Emit one smallest complete compound needed to reconnect each such relation. Use a retained VERB backbone when one carries the relation and include only frozen PERSON/OBJECT/LABEL/PLACE/TIME/LOCATOR slots actually participating in that same relation instance. A non-VERB characterization/state/question binding may form a compound only when distinct represented structure is not already carried by another relation. No graph closure, arbitrary co-occurrence, all-pairs links, scene mega-bundles, singleton equivalents, subset/superset variants, support chains, duplicate restatements, or compounds invented merely to justify primitives.

Never expose approved archetypes, evaluator findings, prior scored outputs, calibration answers, or sealed holdout material. Never perform promotion, Oval Office admission, APA-ID creation, sovereign/admitted writing, or APA database mutation.
'''.strip()

V116_BASE_RULES = APPARATUS_BASE_RULES + "\n\n" + V116_CORRECTION
V116_CLASS_RULES = dict(APPARATUS_CLASS_RULES)
V116_CLASS_RULES.update({
    "PLACE": "Retain a PLACE when the source establishes a distinct spatial support slot for a represented relation instance. Local occurrence positions inside one broad setting may be distinct when the source differentiates them; several relations may share support when it does not. Unnamed support is allowed only when source-established. Do not promote physical nouns/surfaces/object positions automatically.",
    "TIME": "Retain a TIME when the source establishes a distinct temporal support slot for a represented relation instance. Local episodes/phases inside one broad narrative period may be distinct when source-differentiated; several relations may share support when not. Unnamed support is allowed only when source-established. Do not promote every clause/action/tense/duration phrase.",
    "PERSON": "Retain speaker plus each distinct represented human/social actor or stable group after coreference when it fills a participant slot in a represented relation instance. One-use, offscreen, relational, possessive/beneficiary, remembered, reported, institutional, prospective, and peripheral actors may qualify; reject nonreferential/generic person wording.",
    "OBJECT": "Retain each source-presented referent/content handle occupying a tracked object/content slot in a represented relation instance. One-use concrete or abstract nodes may qualify. Do not nominalize every clause, question, intention, grammatical argument, discourse point, place support, or characterization.",
    "LABEL": "Retain the smallest complete source-applied characterization/state/status/identity/evaluation/comparison/candidate label/rejection/correction occupying a characterization slot. One-use and colloquial labels may qualify. Do not inventory modifier/adverb/intensifier/discourse fragments or split one natural judgment into pieces.",
    "VERB": "Retain one minimal complete literal predicate kernel for each distinct represented relation instance carrying an operative lexical relation. One-use, ordinary, reporting, perception, question, obligation, location, cognition, gesture, and low-salience relations may qualify. Reject auxiliary/support tokens, duplicates, and lexical verb fragments nested inside a stronger natural relation kernel.",
    "LOCATOR": "Retain the smallest complete exact span occupying an independent orientation slot in a represented relation instance. Position/path/direction/origin-destination/containment/proximity/accompaniment/internal-context/figurative orientation may qualify. Do not inventory every PP, recipient/topic/purpose, possession, degree, temporal, or generic adverbial phrase.",
})
