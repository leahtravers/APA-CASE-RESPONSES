"""V91 neutral apparatus rules: whole-source coverage with durable-coordinate admission.

These rules mirror AGENT_CONTRACT_V91 without archetype answers, evaluator findings,
expected counts, prior scored outputs, or holdout material.
"""

V91_BASE_RULES = r'''
V91 LIGHTWEIGHT RULE: COVER THE SOURCE, BUT ADMIT ONLY DURABLE COORDINATES.

Read the complete source first. Map materially distinct settings/scenes, time frames, actors, persistent referents, staged characterizations, relation edges, and orientations. This coverage map is not itself the primitive inventory.

A primitive is admitted only when all are true: (1) it is materially source-present, (2) it performs a genuine job of the requested class at source-native grain, and (3) it has independent coordinate value beyond merely restating one local proposition or duplicating another coordinate. Structural PLACE/TIME support coordinates are also allowed when necessary to keep materially distinct represented scenes or frames from collapsing.

Independent coordinate value is strongest when the source names/revisits/contrasts/corrects/questions the trace as its own thing, when it participates in multiple materially distinct bindings, when it anchors a scene/frame/actor/persistent referent/durable characterization/reusable orientation, or when omission would collapse materially distinct source organization.

SOURCE PRESENCE ALONE IS NOT ENTITLEMENT. Being a noun, adjective, verb, prepositional phrase, amount, object/body part, clause fragment, grammatically extractable relation, or one-time selectable phrase is not enough by itself.

SUPPRESS CENSUS ARTIFACTS: true aliases/coreferent repeats; pure grammar/auxiliary support; one-off noun/content fragments that belong only inside a local proposition; ordinary modifiers/intensifiers not independently staged; mechanically split predicate fragments; weak prepositional/context fragments; generic discourse wrappers when specific content is the real coordinate; analyst abstractions; and unjustified cross-class duplicates.

When uncertain, prefer the smallest selective coordinate set that still preserves materially distinct source structure. The inventory is neither a minimal ontology nor a token/noun/modifier/verb/preposition census.

CROSS-CLASS OVERLAP IS EXCEPTIONAL. Reuse the same literal trace in two classes only when each projection remains independently useful as a durable coordinate after the other projection is removed. Grammatical plausibility alone is not enough.

PLACE: retain explicit settings and source-organizing occurrence positions. Use unnamed support positions only when needed to keep distinct represented scenes/waits/reports/present-telling contexts from collapsing. Do not inventory every object position, implied destination, surface, path, body part, or one-off action location.

TIME: retain source-organizing episode/period/recurrence/remembered/report/present/prospective frames. Several relations share one frame unless the source materially shifts the when-context. Do not create TIME from every action, tense, duration question, hypothetical act, or clause.

PERSON: retain B plus every distinct represented human/social actor or stable group after true coreference when the actor materially participates. Minor/offscreen/relational/reported actors qualify when they have source identity. Suppress aliases and nonreferential addressees.

OBJECT: retain persistent concrete or source-reified referents/content with independent identity: tracked things, values, choices, decisions, plans, relations/practices, reified situations/content, or figurative objects when the source gives them stable referential identity. Do not nominalize every clause, emotion, adjective, amount, noun, body/object part, quoted fragment, or candidate concept. Suppress generic wrappers when specific content is the actual tracked referent.

LABEL: retain independently staged characterizations, states, statuses, manners, comparisons, identity/candidate labels, rejections, or corrections. Do not inventory every adjective, adverb, intensity marker, rhetorical reaction, positional phrase, or momentary state. Keep non-durable characterization material inside its local compound.

VERB: retain the source-native relation edge needed to connect admitted coordinates or a relation independently revisited/contrasted/central enough to remain a reusable coordinate. Prefer one complete predicate for one represented edge. Do not mechanically split matrix/support/copular/control/subordinate/coordinated fragments when one source-native relation is the better unit. Preserve modality, negation, particles, complements, and stance when part of relation identity. Do not inventory every verb in the text.

LOCATOR: retain orientation that independently locates/relates admitted coordinates through setting, position, path, origin/destination, containment, internal orientation, comparison, or recurring context. Prefer reused, contrasted, or structurally necessary orientations. Do not inventory every prepositional or movement phrase, and do not duplicate a VERB as LOCATOR unless the orientation remains independently useful.

LITERAL LOCK: preserve source language exactly wherever source text is required. Do not normalize dialect, grammar, contractions, numbers, uncertainty, negation, modality, comparison, or punctuation. Unnamed structural PLACE/TIME support may use null source_wording with an exact source cue. researcher_note is null or minimal mechanical/coreference bookkeeping.

FREEZE PRIMITIVES BEFORE COMPOUNDS. Recheck that every retained primitive has source identity, class identity, and durable coordinate value; remove census artifacts and unjustified cross-class duplicates before freezing.

COMPOUNDS: reconstruct the smallest complete source-local proposition/event/state/report/intention/question/comparison from frozen coordinates. Bind all and only admitted coordinates materially belonging to the local binding. Do not create arbitrary pairwise closure, subset/superset permutations, broad scene mega-bundles, or new primitives merely to make a proposition verbally complete; researcher_bundle may preserve local source wording while references remain limited to admitted coordinates.

Never target hidden counts or infer hidden gold. Never expose approved archetypes, evaluator findings, prior scored answers, or sealed holdout content/output to the worker. Never perform APA scoring, psychological interpretation, promotion, APA-ID creation, sovereign/admitted writing, or database mutation.
'''.strip()

V91_CLASS_RULES = {
    "PLACE": "Retain source-organizing settings/occurrence positions with durable navigation value. Add unnamed support positions only when distinct represented scenes would otherwise collapse. Avoid micro-position, object-position, destination, surface, path, or action-location census.",
    "TIME": "Retain source-organizing episode/period/recurrence/report/present/prospective frames. Several relations may share one frame. Avoid action-phase, tense, duration-question, hypothetical-act, or clause census.",
    "PERSON": "Retain B plus every distinct materially represented actor or stable social group after true coreference. Minor/offscreen/relational/reported actors qualify when source-identified; suppress aliases and nonreferential addressees.",
    "OBJECT": "Retain persistent or source-reified referents/content with independent identity. Do not nominalize every noun, clause, emotion, amount, part, quoted fragment, or one-off content span. Prefer specific tracked content over generic wrappers.",
    "LABEL": "Retain independently staged durable characterization/state/status/manner/comparison/identity/candidate-label/rejection/correction. Do not inventory ordinary modifiers, intensifiers, reactions, or momentary descriptors that matter only inside one local proposition.",
    "VERB": "Retain complete source-native relation edges that connect admitted coordinates or remain independently reusable. Avoid verb census and mechanical splitting of matrix/support/copular/control/subordinate fragments. Preserve modality/negation/particles/complements when part of relation identity.",
    "LOCATOR": "Retain durable or structurally necessary orientation among admitted coordinates. Avoid preposition/movement census and duplicate VERB projection unless the orientation remains independently useful.",
}
