"""V93 neutral apparatus rules: independent research-coordinate identity.

These rules mirror AGENT_CONTRACT_V93 without archetype answers, evaluator findings,
expected counts, prior scored outputs, or holdout material.
"""

V93_BASE_RULES = r'''
V93 LIGHTWEIGHT RULE: INDEPENDENT RESEARCH-COORDINATE IDENTITY BEFORE CLASS ENTITLEMENT.

Read the complete source first and silently map scenes/positions, time frames/phases, actors, referents/content handles, characterizations, relation structure, and orientations. This whole-source map prevents omissions; it does NOT automatically create primitives.

A primitive is admitted only when all are true: (1) it is materially source-present rather than analyst-invented, (2) it performs a real job of the requested class rather than merely being grammatically compatible with it, (3) it is independently addressable as a research coordinate of that class, and (4) omitting it would remove a distinct source-reconnection handle rather than merely remove a clause fragment already carried by stronger coordinates and their compound.

INDEPENDENT ADDRESSABILITY DOES NOT REQUIRE RECURRENCE OR REUSE. A correct primitive may occur once, be local, low-salience, or participate in only one proposition. Repeated mention, multiple compounds, persistence, and broad scene anchoring are not prerequisites.

MATERIAL SEMANTICS ALONE IS NOT ENOUGH. Do not inventory every clause fragment, modifier, support predicate, copula/control verb, physical surface, temporal adverb, preposition, comparison particle, transition word, or syntactic attachment merely because it contributes some meaning. The source trace must have a source-native identity that a researcher could point back to as a distinct place, time, actor, referent, characterization, relation edge, or orientation.

A useful test: if a researcher later saw this primitive by itself, would it function as a meaningful source-reconnection handle of THIS CLASS, or would it look like a fragment extracted only because the sentence could be decomposed further? Keep the former; suppress the latter.

Suppress true aliases/coreferent repeats; pure grammar/support; analyst-created abstractions; generic wrappers with no distinct referential job; clause complements that the source does not reify; modifier fragments with no independently selectable characterization; predicate fragments with no distinct relation edge; routine preposition/adverb attachments with no independent orientation; duplicate tokenizations; and cross-class shadows whose second class job has no independent addressability.

CLASS-NATIVE GRAIN: use the smallest complete source-native wording that preserves the admitted coordinate identity. Keep identity-bearing particles/complements/negation/modality/uncertainty/comparison. Do not absorb separable arguments merely to make a sentence. Do not split a coordinate into lexical debris merely because its words can be classified separately.

CROSS-CLASS OVERLAP: allow the same literal trace in multiple classes only when each projection is independently addressable in that class. Grammatical plausibility alone is insufficient.

PLACE: retain source-organizing settings and occurrence-positions that independently locate materially represented content: meaningful broad/contained settings, distinct waits/encounters/conversations/reports/memories/reflections, materially staged positions, and real origins/destinations. One-use places qualify. Necessary unnamed support positions may use null source_wording with an exact cue. Do not inventory every room part, surface, body part, path noun, container noun, or physical object as PLACE.

TIME: retain source-organizing frames and event phases that independently locate when material occurs: distinct phases, waits/transitions, later reports/conversations, remembered frames, recurring spans, present reflection, prospective periods, and necessary unnamed support frames. One-use frames qualify. Do not inventory tense, every action, every temporal adverb, transition word, duration phrase, recurrence marker, or redundant container episode as TIME.

PERSON: retain B plus every distinct materially represented human/social actor or stable group after true coreference. Minor, one-use, offscreen, relational, remembered, reported, prospective, and institutional actors qualify. Suppress aliases and nonreferential/rhetorical addressees.

OBJECT: retain source-treated concrete or abstract things with independent referential identity: physical things/parts, products/documents/services/results/orders, amounts/values/sets/categories, choices/decisions/next steps/plans/options, stable relations/practices/relationships/situations/content when the source treats them as things, and source-reified figurative objects. One-use objects qualify. Do not nominalize every clause, complement, question, action, or noun phrase.

LABEL: retain source-applied characterizations, states, statuses, manners, comparisons, identity/candidate labels, rejections, and corrections when independently selectable as characterizations. One-use labels qualify. Preserve exact uncertainty, question form, negation, rejection, correction, intensity, comparison, and dialect when identity-bearing. Do not inventory every adjective, adverb, intensifier, rhetorical aside, evaluative clause, or modifier.

VERB: retain independently meaningful source-native relation edges: actions, states, stances, cognition, reports, intentions, obligations, decisions, perceptions, placement/existence relations, or happenings whose relation identity matters for reconnection. One-use relations qualify. A matrix/support/copular/control predicate qualifies only when it contributes a distinct relation beyond grammatical staging of another admitted coordinate/relation. Suppress pure auxiliaries, duplicated nested predicates, and full-clause/question fragments masquerading as lexical relations. Use the smallest complete predicate construction with identity-bearing particles/complements/negation/modality.

LOCATOR: retain independently useful orientation relations that locate or position source material: meaningful position/proximity, path/movement, entry/exit, origin/destination, containment, situational/recurring context, internal orientation, and temporal/comparative orientation when the phrase itself functions as an orienting handle. One-use locators qualify and may contain verbal material when that full construction is the orientation. Suppress routine recipient/topic marking, phrase-internal prepositions, generic transitions, adverbial attachments, comparison particles, and local clause modifiers with no independent locating job.

LITERAL LOCK: preserve source language exactly wherever source text is required. Do not normalize grammar, dialect, contractions, numbers, uncertainty, negation, modality, comparison, or punctuation. Only genuinely unnamed structural PLACE/TIME support may use null source_wording with an exact cue. researcher_note is null or minimal mechanical/coreference/unnamed-coordinate bookkeeping.

FREEZE PRIMITIVES BEFORE COMPOUNDS. Recheck that every row has source identity, a real class job, independent coordinate identity, and distinct reconnection value. Recheck that no legitimate row was suppressed merely for being one-use/local and no row was admitted merely because a clause can be decomposed further.

COMPOUNDS: create only source-local bindings needed to reconnect materially distinct propositions/events/states/reports/intentions/questions/comparisons/characterizations/orientations among frozen coordinates. A clause does not automatically deserve a compound. Include only frozen coordinates materially belonging to the binding. Do not create arbitrary graph closure, every nested grammatical proposition, subset/superset permutations, mega-bundles, or new primitives merely to complete wording.

Never target hidden counts or infer hidden gold. Never expose approved archetypes, evaluator findings, prior scored answers, or sealed holdout content/output to the worker. Never perform APA scoring, psychological interpretation, promotion, APA-ID creation, sovereign/admitted writing, or database mutation.
'''.strip()

V93_CLASS_RULES = {
    "PLACE": "Retain source-organizing settings and occurrence-positions that are independently addressable location handles, including one-use meaningful staged positions and necessary unnamed support positions. Avoid physical-noun/surface/body-part/path/container census.",
    "TIME": "Retain source-organizing frames and event phases that are independently addressable when-handles. One-use phases qualify. Avoid tense/action/adverb/transition/duration/recurrence-token census and redundant container frames.",
    "PERSON": "Retain B plus every distinct materially represented actor or stable group after true coreference, including minor/offscreen/relational/reported/prospective actors. One-use actors qualify; suppress aliases and nonreferential addressees.",
    "OBJECT": "Retain source-treated things/content with independent referential identity, including one-use concrete parts, orders/amounts/values, choices/decisions/plans, and source-reified relations/situations/content. Avoid arbitrary noun/clause/complement nominalization.",
    "LABEL": "Retain independently selectable source characterizations/states/statuses/manners/comparisons/identity or candidate labels/rejections/corrections. One-use labels qualify. Preserve exact posture; avoid adjective/adverb/modifier/rhetorical-fragment census.",
    "VERB": "Retain independently meaningful source-native relation edges. Matrix/support/copular/control predicates qualify only when they add a distinct action/state/stance/cognition/report/intention/obligation/perception/placement relation beyond grammatical staging. Avoid grammatical-predicate and full-clause census.",
    "LOCATOR": "Retain independently useful orientation relations, including meaningful spatial/path/containment/context/internal and temporal/comparative positioning when the phrase itself orients a represented coordinate/event. Avoid routine preposition/adverb/transition/argument-marking census.",
}
