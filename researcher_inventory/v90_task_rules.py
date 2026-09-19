"""V90 neutral apparatus rules: coverage-first editorial entitlement, then class-native grain.

These rules describe the same durable semantics as AGENT_CONTRACT_V90. The contract-isolated
adapter removes apparatus prose before worker dispatch, so this module remains apparatus-side
mechanical configuration and must not contain archetype answers or evaluator findings.
"""

V90_BASE_RULES = r'''
V90 LIGHTWEIGHT RULE: COVERAGE-FIRST EDITORIAL ENTITLEMENT; THEN CLASS-NATIVE GRAIN.

The Researcher Inventory is a lightweight source-reconnection index, not a minimal ontology and not a token/grammar/modifier/preposition census. Read the complete source first. Retain every materially source-present trace that performs a recognizable job in the requested class and could be independently selected to reconnect to a distinct source relation, referent, characterization, scene/frame, or orientation. Do not suppress a valid class handle merely because related meaning also appears in another class or in a compound.

CROSS-CLASS OVERLAP: allowed whenever the same literal source material performs distinct useful class jobs. Do not force one primary semantic home. Reject overlap only when the second projection is grammar-only, incidental, duplicative, or has no independently selectable class job.

SUPPRESS: true aliases/coreferent repeats; pure auxiliaries/syntactic glue with no semantic relation; token fragments without class identity; incidental modifiers/prepositions without an independently useful class job; analyst-created abstractions; generic discourse wrappers when the more specific source content is the actual tracked referent and the wrapper is not independently revisited.

PLACE: named settings plus materially represented occurrence-positions, including useful object positions, destinations/offscreen positions, distinct wait/interaction positions, remembered/reported scene positions, and present-telling position when exact location is unstated. Unnamed required positions use null source_wording and exact source cues. Do not census every physical noun/surface/path.

TIME: source-organizing episode/period/recurrence/intended/report/present/future frames. Several relations can share one frame. A one-off hypothetical action is not automatically a TIME unless the source stages a period/frame around it.

PERSON: B plus every distinct represented actor or stable social group after true coreference, including minor, offscreen, relational, remembered, reported, prospective, and institutional actors.

OBJECT: source-treated independently selectable referents/content: concrete things, values, choices, decisions, next steps, plans, stable relations/practices, source-reified mental/content objects, situations/events when made thing-like, figurative objects, and explicit internal containers/loci. Suppress empty discourse wrappers such as generic point/part shells when their underlying content is what is tracked.

LABEL: independently selectable source-staged characterization/value/state/status/manner/comparison/identity/candidate label/rejection/correction/continuing state. A label may overlap VERB or LOCATOR. Do not census every adjective or intensifier. Preserve exact posture, negation, uncertainty, comparison, dialect, and intensity when identity-relevant.

VERB: materially represented action/relation/state/stance/cognition/report/intention/question/modality/happening. Coverage precedes minimality. Semantically active copular, modal, support, matrix, control, perception, cognition, reporting, possession, movement, and negated relations qualify when they add an independent source edge. Suppress only truly empty grammatical support. Use the smallest complete source-native predicate wording that preserves relation identity; keep particles/complements/modal-negative posture when required.

LOCATOR: independently useful orientation, including setting relation, position/proximity, origin/destination, path/movement, entry/exit, containment, orientational accompaniment, recurring situational context, internal/mental orientation, figurative/comparative orientation, and relative-distance constructions. A full directional/purpose construction may be the locator when that is what supplies orientation. Allow overlap with VERB/PLACE/TIME/LABEL when jobs differ.

LITERAL LOCK: preserve source language exactly where source text is required. Unnamed PLACE/TIME support frames may use null source_wording with exact source_cue. researcher_note is null or minimal mechanical/coreference bookkeeping.

FREEZE PRIMITIVES BEFORE COMPOUNDS. Audit the coverage ledger for suppressed valid handles, then remove only duplicates/artifacts and resize to class-native grain.

COMPOUNDS: for each materially presented source-local proposition/event/state/report/intention/question/comparison, bind all and only frozen coordinates materially belonging to that binding. Include relevant participants/referents, PLACE/TIME/LOCATOR/LABEL, and multiple VERBs when one local relation cluster requires them. Avoid arbitrary pairwise closure, duplicate subset/superset permutations, and broad scene mega-bundles.

Never target hidden counts or infer hidden gold. Never perform APA scoring, psychological interpretation, promotion, APA-ID creation, sovereign/admitted writing, or database mutation. Never access sealed holdout content/output during calibration.
'''.strip()

V90_CLASS_RULES = {
    "PLACE": "Retain explicit settings and source-organizing occurrence-positions, including useful object/destination/wait/report/telling positions. Unnamed distinct positions may use null source_wording with an exact source cue. Avoid physical-noun census.",
    "TIME": "Retain source-organizing episode/period/recurrence/intended/report/present/prospective frames. Do not create a separate frame from every action, tense marker, duration, or one-off hypothetical action.",
    "PERSON": "Retain B plus every distinct represented actor or stable social group after true coreference, including minor/offscreen/relational/reported actors. Suppress only true aliases and nonreferential addressees.",
    "OBJECT": "Retain source-represented concrete/abstract referents, values, choices, decisions, plans, stable relations/practices, reified content/situations, figurative objects, and explicit mental/internal loci. Suppress empty discourse wrappers when underlying content is the real referent.",
    "LABEL": "Retain source-staged selectable characterizations, states, statuses, manners, comparisons, identity labels, candidate labels, rejections/corrections, and continuing states. Preserve exact posture. Do not census ordinary modifiers.",
    "VERB": "Retain materially represented relation edges, including semantically active copular/modal/support/control/cognition/reporting/possession/movement/negated relations. Suppress only empty grammar. Use the smallest complete predicate wording that preserves relation identity.",
    "LOCATOR": "Retain useful setting/position/path/origin/destination/containment/recurring-context/internal/comparative orientation. Allow overlap with other classes when orientation is independently selectable; avoid preposition census.",
}
