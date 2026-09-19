"""V98 neutral apparatus rules: V97 semantic grouping plus bidirectional binding completeness.

These rules contain no archetype answers, evaluator findings, expected counts,
prior scored outputs, or holdout material.
"""
from researcher_inventory.v97_task_rules import V97_BASE_RULES, V97_CLASS_RULES

V98_CORRECTION = r'''

V98 PROSPECTIVE CORRECTION — BIDIRECTIONAL BINDING COMPLETENESS.

Keep all V97 class-native entitlement and source-native semantic grouping. Correct V97's generalizable completeness imbalance by making source-local BINDINGS the coverage audit for primitive selection.

Before freezing primitives, silently map the materially distinct source-local propositions/events/states/reports/intentions/questions/comparisons/characterizations/orientation bindings and the distinct semantic roles each binding actually represents. This is a semantic map, never a token/POS/noun-phrase/clause/verb/preposition/modifier census.

Every primitive must pass BOTH directions:

1. SPARSITY: the row performs its own class-native independently reconnectable semantic job in at least one material binding, or is itself a materially represented standalone coordinate. Mere occurrence, grammatical divisibility, recurrence, vividness, concreteness, or analyst usefulness is insufficient.
2. COMPLETENESS: every materially distinct binding retains the distinct primitive roles/support coordinates needed to reconstruct it. Do not let a broad scene erase a distinct local occurrence place; do not let a broad episode erase a distinct phase; do not let one class swallow a different class-native role; do not drop a local/one-use/unnamed/endpoint-dependent/low-salience coordinate merely because it is minor.

A coordinate is necessary when removing it would make a materially distinct binding unreconstructable, collapse two distinct represented roles, lose source posture/qualification, or require an analyst-created substitute. Restore such a coordinate at the V97 complete-semantic-unit grain.

This completeness gate does NOT license mention census. If a token or phrase performs no independently reconnectable semantic job, suppress it even when it occurs in a material sentence.

PLACE/TIME: preserve all distinct occurrence/episode support required by material bindings, including necessary unnamed/local support, while continuing to reject physical/spatial/temporal mention census.

PERSON: preserve every distinct represented actor role after true coreference, including one-use/offscreen/relational actors when a material binding uses them.

OBJECT: preserve every distinct source-treated referent/content role required by material bindings, including one-use/abstract content handles, while continuing to reject pronoun/noun-phrase/clause-fragment census.

LABEL: preserve every distinct represented characterization/correction/polarity role required by material bindings, at complete characterization-unit grain, while rejecting decorative/modifier census.

VERB: preserve every independently represented semantic relation required by material bindings, at one complete semantic relation per row. Do not suppress a nested/local relation merely because it is low-salience; do not split grammatical support or lexical verb fragments.

LOCATOR: preserve every independently represented orientation role required by material bindings, at one complete semantic orientation per row. Do not suppress local/endpoint-dependent orientation when it carries a distinct job; do not inventory prepositions/particles/adverbs.

CROSS-CLASS OVERLAP: coverage never licenses duplication. Allow overlap only when the same literal trace performs genuinely different semantic jobs.

COMPOUNDS: after primitive freeze, create the smallest canonical set of materially distinct source-local bindings from the private binding map. A compound corresponds to a represented binding; primitives do not automatically generate compounds and broad supports do not automatically propagate.

LITERAL LOCK remains absolute after selection. Preserve source wording, dialect, contractions, numbers, uncertainty, negation, modality, comparison, and punctuation exactly where source text is expected.

Never target hidden counts or infer hidden gold. Never expose approved archetypes, evaluator findings, prior scored outputs, calibration answers, or sealed holdout material. Never perform promotion, APA-ID creation, sovereign/admitted writing, or database mutation.
'''.strip()

V98_BASE_RULES = V97_BASE_RULES + "\n\n" + V98_CORRECTION
V98_CLASS_RULES = dict(V97_CLASS_RULES)
V98_CLASS_RULES.update({
    "PLACE": "Recover every distinct occurrence-support geography role needed by materially represented bindings, including necessary unnamed/local support. Keep V97 semantic-unit grouping: spatial mention, surfaces, object positions, and prepositional phrases are not rows unless they organize a distinct occurrence role.",
    "TIME": "Recover every distinct episode/phase support role needed by materially represented bindings, including necessary unnamed/local phases. Keep V97 semantic-unit grouping: tense, adverbs, durations, transitions, and action mentions are not rows unless they organize a distinct temporal role.",
    "PERSON": "Retain every distinct represented human/social actor or stable group after true coreference when it occupies an actor role in materially represented source content; one-use, offscreen, remembered, relational, possessive, prospective, and institutional actors may qualify.",
    "OBJECT": "Retain every distinct source-treated concrete/abstract referent or content role needed by materially represented bindings, including one-use/abstract handles. Do not inventory pronouns, generic deixis, noun phrases, clause complements, or action nominalizations unless the occurrence itself functions as a distinct source referential handle.",
    "LABEL": "Retain every distinct represented characterization/candidate-characterization/correction/polarity role needed by materially represented bindings at complete characterization-unit grain. Do not inventory modifiers, intensifiers, decorative phrases, rhetorical flourishes, or comparison scaffolding without a distinct characterization job.",
    "VERB": "Retain every independently represented semantic relation needed by materially represented bindings at one complete semantic relation per row. Keep V97 anti-tokenization: split only independently reconnectable relations; suppress auxiliaries/copulas/support fragments that carry no separate relation job.",
    "LOCATOR": "Retain every independently represented orientation/topology role needed by materially represented bindings at one complete semantic orientation per row. Local/endpoint-dependent orientation may qualify; prepositions/particles/adverbs/transitions do not qualify without a distinct orientation job.",
})
