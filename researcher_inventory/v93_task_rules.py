"""V93 neutral apparatus rules: standalone research-coordinate identity.

These rules mirror AGENT_CONTRACT_V93 without archetype answers, evaluator findings,
expected counts, prior scored outputs, or holdout material.
"""

V93_BASE_RULES = r'''
V93 LIGHTWEIGHT RULE: STANDALONE RESEARCH-COORDINATE IDENTITY, NOT SOURCE-DETAIL CENSUS.

Read the whole source and account for materially represented settings, frames, actors, referents, characterizations, relations, and orientations. This ledger prevents omissions but does NOT automatically create rows.

A primitive is admitted only when all are true: (1) SOURCE IDENTITY: materially represented rather than analyst-invented; (2) CLASS-NATIVE IDENTITY: it performs this requested class's job; (3) STANDALONE INDEXABILITY: it is a bounded source handle that remains independently useful for source reconnection rather than only completing one surrounding proposition; and (4) EDITORIAL MATERIALITY: removing it would lose a meaningful coordinate, not merely local sentence detail, grammar, scenery, or a redundant shadow.

ONE-USE IS ALLOWED BUT NOT AUTOMATIC. Recurrence, reuse, repeated mention, multiple compounds, broad salience, or persistence across scenes are never required. A one-use actor, explicitly treated referent, source-organizing site/frame, independently applied characterization, discrete relation edge, or genuine orientation may qualify when the source itself gives it bounded identity. Material that only matters inside one local proposition stays represented by that proposition/compound rather than receiving a redundant primitive.

Resolve aliases/coreference and repeated mentions first. Cross-class overlap is allowed only when the same source material performs two independently indexable class jobs; grammatical plausibility alone is insufficient.

CLASS-NATIVE GRAIN: use the smallest complete source-native form that preserves the admitted coordinate. Do not absorb separable subjects/objects/places/times/labels/locators/neighboring predicates. Keep particles, required complements, negation, modality, comparison, and dialect when identity-bearing.

PLACE: retain source-organizing settings or occurrence-positions. A distinct wait, encounter, remembered scene, report/conversation, materially staged position, or unnamed occurrence-position can qualify when it independently organizes where represented material occurs. Do not inventory every surface, body part, location noun, inferred destination, contemplated exit, object position, or present-reflection clause.

TIME: retain source-organizing episode/frame/period coordinates. Initial episodes, materially separate responses/transitions/waits, later reports/conversations, recurring spans, remembered frames, present reflection, and separately represented prospective frames can qualify. Several actions can share one TIME. Do not create TIME for every action, clause, question, hypothetical, tense, or local phase.

PERSON: retain B plus every distinct source-represented human/social actor or stable group after coreference. One-use/offscreen actors may qualify because actor identity is independently indexable. Suppress aliases and nonreferential/rhetorical addressees.

OBJECT: retain source-treated concrete/abstract referents with bounded independent referential identity: things, amounts/values, documents/orders/results/services, choices/decisions/next steps, sets/categories, explicitly reified situations/content, internal objects. One-use may qualify. Nounhood, possession, vivid scenery, or appearance in one proposition is insufficient. Do not nominalize clauses or retain incidental scenic props/wrappers merely because named.

LABEL: retain independently selectable source-applied characterizations of represented targets: compact qualities, states, comparisons, identity/candidate labels, evaluations, rejections, corrections. One-use may qualify. Do not inventory every adjective/adverb/intensifier/vivid phrase/rhetorical aside/whole clause or predicate complement merely because descriptive.

VERB: retain source-native relation edges, not verb tokens or every clause. Prefer one smallest complete predicate relation over mechanical matrix/support/embedded/copular decomposition. A matrix/control/support predicate is separate only when it contributes an independently selectable relation beyond scoping the embedded predicate. An embedded predicate is separate only when it remains a distinct relation rather than lexical completion. A copula fully represented by LABEL/LOCATOR normally does not create another VERB. Do not use whole questions/sentences when a bounded lexical predicate carries the relation. One-use relations may qualify.

LOCATOR: retain independently indexable orientation/context relations: setting, position, path, origin/destination, containment, internal orientation, or materially organizing context. Do not inventory every preposition, recipient/topic relation, possession, comparison support, path-flavored verb, or clause merely because spatial/context language appears. Movement may be a VERB without also being LOCATOR unless a separate orientation relation is established.

LITERAL LOCK: preserve exact source language wherever source text is required. Do not normalize dialect, grammar, contractions, numbers, punctuation, uncertainty, negation, modality, or comparison. Only genuinely unnamed structural PLACE/TIME support may use null source_wording with exact source cue. researcher_note is null or minimal mechanical/coreference bookkeeping.

FREEZE PRIMITIVES BEFORE COMPOUNDS. Recheck all four gates. Do not keep a row solely because it appears in a proposition. Do not reject a legitimate row solely for being one-use.

COMPOUNDS: reconstruct the smallest complete source-local semantic binding for each materially distinct proposition/event/state/report/intention/question/comparison/characterization/orientation using only frozen units. Proposition meaning may include local detail that did not earn a primitive; do not mint a unit for every word. No graph closure, arbitrary pairwise combinations, subset/superset permutations, duplicate mega-bundles, or primitives invented to complete wording.

Never target hidden counts or infer hidden gold. Never expose approved archetypes, evaluator findings, prior scored answers, or sealed holdout content/output to the worker. Never perform APA scoring, psychological interpretation, promotion, APA-ID creation, sovereign/admitted writing, or database mutation.
'''.strip()

V93_CLASS_RULES = {
    "PLACE": "Retain independently indexable source-organizing sites/occurrence-positions. One-use may qualify, but local spatial detail or inferred movement position alone does not.",
    "TIME": "Retain independently indexable source-organizing episode/frame/period coordinates. Several actions may share one frame; do not split every clause/action/local phase.",
    "PERSON": "Retain B plus every distinct represented actor/group after true coreference. One-use/offscreen actors can qualify; suppress aliases/nonreferential addressees.",
    "OBJECT": "Retain source-treated referents with bounded independent identity. One-use can qualify, but nounhood, scenery, possession, or one-proposition support alone does not.",
    "LABEL": "Retain independently selectable source-applied characterizations. One-use can qualify; avoid adjective/adverb/intensifier/rhetorical/whole-clause census.",
    "VERB": "Retain source-native relation edges. Prefer one complete relation over matrix/support/embedded/copular decomposition unless each piece independently survives as a relation.",
    "LOCATOR": "Retain independently bounded orientation/context relations. Avoid preposition/path/context vocabulary census and duplicate VERB shadows.",
}
