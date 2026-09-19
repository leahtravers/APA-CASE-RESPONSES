"""V92 neutral apparatus rules: material source-trace entitlement at class-native grain.

These rules mirror AGENT_CONTRACT_V92 without archetype answers, evaluator findings,
expected counts, prior scored outputs, or holdout material.
"""

V92_BASE_RULES = r'''
V92 LIGHTWEIGHT RULE: MATERIAL SOURCE-TRACE ENTITLEMENT, THEN CLASS-NATIVE GRAIN.

Read the complete source first. Account for materially represented settings/positions, time frames/event phases, actors, referents/content handles, characterizations, relation increments, and orientations. This whole-source ledger prevents omissions but does not automatically create rows.

A primitive is admitted when all are true: (1) it is materially source-present rather than analyst-invented, (2) it performs a distinguishable job of the requested class at source-native grain, and (3) after true coreference/repetition is resolved, it is not merely grammar or a duplicate of the same class job.

DO NOT REQUIRE DURABILITY OR REUSE. A valid primitive may occur once, belong primarily to one local proposition, be low-salience, or never recur. Recurrence, multiple bindings, persistence, broad scene anchoring, and reuse outside the local proposition are not entitlement requirements.

SOURCE PRESENCE ALONE IS STILL NOT ENOUGH. Suppress true aliases/coreferent repeats; pure articles/auxiliaries/do-support/punctuation; token fragments with no complete class identity; analyst-created abstractions; generic discourse wrappers with no distinct job; duplicate tokenizations; and cross-class shadows whose supposed second class job disappears once the real coordinate is known.

When uncertain, ask whether removing the row would erase a materially represented job of THIS CLASS, not whether related meaning survives somewhere else. Do not force one semantic home merely to reduce row count. Do not create a token/POS census merely because words are extractable.

CLASS-NATIVE GRAIN: use the smallest complete source-native wording that preserves the admitted class job. Keep required particles/complements/negation/modality/comparison when they are identity-bearing. Do not absorb separable subjects, objects, places, times, labels, locators, or neighboring predicates just to make a complete sentence.

CROSS-CLASS OVERLAP: allow the same literal trace in multiple classes only when each projection performs a real distinguishable class job. Grammatical plausibility alone is insufficient; related meaning elsewhere is not a reason to suppress a real class job.

PLACE: retain materially represented settings and occurrence-positions, including object positions, origins/destinations, waits, encounters, conversations/reports, remembered scenes, present-telling positions, and unnamed support positions when those are distinct location jobs. Do not inventory every physical noun, surface, body part, path word, or figurative expression.

TIME: retain materially distinct episode/period frames and event phases such as attempts/conditions, response/help episodes, transitions/departures, waits, intended periods, later reports/conversations, recurring spans, remembered/comparison frames, present reflection, and separately represented prospective/future recurring frames. Several relations may share one TIME. Do not create TIME from every action, clause, tense, duration question, or redundant broad container frame.

PERSON: retain B plus every distinct materially represented human/social actor or stable group after true coreference. Direct, minor, offscreen, relational/possessive, remembered, reported, prospective, and institutional actors qualify when source-represented. Suppress aliases and nonreferential/rhetorical addressees.

OBJECT: retain source-treated concrete or abstract things with a distinct referential job: physical things/parts, products/documents/services/results/orders, amounts/values/sets/categories, choices/decisions/next steps/plans/options, relations/practices treated as things, explicitly reified situations/content/internal objects, and source-reified figurative objects. One-use referents may qualify. Do not nominalize every noun or clause, duplicate a pure PLACE/LABEL job, or keep empty discourse wrappers.

LABEL: retain source-applied characterizations, states, statuses, manners, comparisons, identity/candidate labels, rejections, and corrections when they perform a distinguishable characterization job. One-use local characterizations may qualify. Preserve exact posture including negation, uncertainty, question form, rejection, correction, intensity, comparison, and dialect when identity-bearing. Do not split a characterization into modifier fragments or inventory every adjective/adverb.

VERB: retain materially represented source-native predicate/relation increments: actions, states, stances, cognition, reports, intentions, questions, modality, placement/existence relations, and happenings. One-use relations qualify. Semantically active matrix/support/copular/control predicates may qualify when they contribute a distinct relation; embedded/coordinated predicates may also qualify when they do a different relation job. Suppress pure auxiliary support. Use the smallest complete predicate construction, preserving required particles/complements/negation/modality.

LOCATOR: retain materially represented orientation/context relations: settings, position/proximity, movement/path, entry/exit, origin/destination, toward/away, containment, accompaniment when orientational, recurring/situational context, internal/mental orientation, and genuine figurative/comparative orientation. One-use locators may qualify and may contain verbal material when that full construction supplies the orientation. Suppress routine recipient/topic/argument marking and phrase-internal prepositions with no independent locating job.

LITERAL LOCK: preserve source language exactly wherever source text is required. Do not normalize grammar, dialect, contractions, numbers, uncertainty, negation, modality, comparison, or punctuation. Unnamed structural PLACE/TIME support may use null source_wording with an exact source cue. researcher_note is null or minimal mechanical/coreference/unnamed-coordinate bookkeeping.

FREEZE PRIMITIVES BEFORE COMPOUNDS. Recheck that every retained primitive has source identity, a distinguishable class job, and is not a true duplicate/grammar artifact. Recheck that no material row was suppressed merely for being one-use or local.

COMPOUNDS: reconstruct proposition-level source-local bindings from frozen coordinates. Create a binding for each materially distinct proposition/event/state/report/intention/question/comparison/characterization/orientation useful to reconnect the inventory. Include only frozen coordinates materially belonging to that binding. Prefer proposition-level coverage over broad scene summaries. Do not create arbitrary graph closure, subset/superset permutations, mega-bundles, or new primitives merely to complete wording.

Never target hidden counts or infer hidden gold. Never expose approved archetypes, evaluator findings, prior scored answers, or sealed holdout content/output to the worker. Never perform APA scoring, psychological interpretation, promotion, APA-ID creation, sovereign/admitted writing, or database mutation.
'''.strip()

V92_CLASS_RULES = {
    "PLACE": "Retain materially represented settings and occurrence-positions that perform a distinct location job, including one-use object positions, origins/destinations, waits, reports/conversations, remembered scenes, present-telling positions, and necessary unnamed support positions. Avoid physical-noun/surface/path vocabulary census.",
    "TIME": "Retain materially distinct episode/period frames and event phases. Attempts, help/response, transitions, waits, intended periods, reports, recurring spans, reflection, and separately represented future frames can qualify. Do not require recurrence; avoid every-action/clause/tense/duration-question or redundant broad-frame census.",
    "PERSON": "Retain B plus every distinct materially represented actor or stable group after true coreference, including minor/offscreen/relational/reported/prospective actors. One-use actors qualify; suppress aliases and nonreferential addressees.",
    "OBJECT": "Retain source-treated things/content with a distinct referential job, including one-use concrete parts, documents/orders/amounts/values, choices/decisions/plans, reified situations/relations/internal objects. Avoid noun/clause census, empty wrappers, and pure PLACE/LABEL duplicates.",
    "LABEL": "Retain source-applied characterization/state/status/manner/comparison/identity/candidate-label/rejection/correction when it has a distinct characterization job, even if one-use. Preserve exact posture; avoid modifier/intensifier fragments and adjective census.",
    "VERB": "Retain source-native relation increments with distinct semantic jobs, including one-use semantically active matrix/support/copular/control and embedded/coordinated predicates when each contributes a different relation. Suppress pure auxiliaries; use minimal complete predicate grain.",
    "LOCATOR": "Retain materially represented orientation/context relations, including one-use path/movement/position/origin/destination/containment/internal/context constructions when they perform a distinct locating job. Avoid routine argument/preposition census.",
}
