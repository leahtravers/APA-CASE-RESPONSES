"""V97 neutral apparatus rules: class-native entitlement with source-native semantic grouping.

These rules contain no archetype answers, evaluator findings, expected counts,
prior scored outputs, or holdout material.
"""
from researcher_inventory.v96_task_rules import V96_BASE_RULES, V96_CLASS_RULES

V97_CORRECTION = r'''

V97 PROSPECTIVE CORRECTION — SOURCE-NATIVE SEMANTIC GROUPING.

Keep V96 class-native entitlement. Correct V96's generalizable over-tokenization defect by separating ENTITLEMENT from GRAIN.

ENTITLEMENT remains class-native: a local, one-use, low-salience, unnamed-support, endpoint-dependent, or wording-overlapping coordinate may be correct when the source materially establishes that class's native semantic job.

GRAIN is NOT the smallest lexical or syntactic fragment. Choose the smallest COMPLETE SEMANTIC UNIT that performs the admitted class job in the represented source. A split is allowed only when each resulting row has its own independently reconnectable semantic job. Grammatical divisibility alone is insufficient.

PLACE/TIME: preserve materially distinct occurrence/episode support, including necessary unnamed coordinates. Broad scenes do not suppress real local support, but literal spatial/temporal mention alone does not create a row. Do not inventory surfaces, path nouns, time adverbs, tense markers, or every action phase unless the source uses them to organize a distinct occurrence/episode.

OBJECT: preserve source-treated referents/content handles, including one-use referents. Do not inventory every noun phrase, pronoun, clause complement, placeholder, or action nominalization. Generic deixis such as this/it/anything/something qualifies only when that occurrence is itself used as a distinct source referential handle.

LABEL: preserve represented characterization units, including candidate labels, corrections/rejections, states/manners, and characterization comparisons. Do not inventory every adjective, adverb, intensifier, decorative phrase, comparison scaffold, or rhetorical flourish.

VERB: recover complete semantic relation units, not grammatical verb tokens. Split matrix/embedded/coordinated material only when each side is an independently reconnectable represented relation. Keep together wording needed for one relation's identity/posture, including necessary auxiliaries, negation, modality, particles, light-verb support, infinitival/complement material, or comparison material. Suppress pure grammatical support. Do not make proposition-sized verb bundles either.

LOCATOR: recover complete semantic orientation units, not every preposition/particle/adverb/transition. Local and endpoint-dependent orientation may qualify. Tokens such as to/at/in/when/while/since/still/like/as/back/up/out qualify only when that occurrence itself carries a materially distinct orientation job.

CROSS-CLASS OVERLAP: allow only when the same trace preserves genuinely different semantic jobs. Grammatical ambiguity alone is not enough.

COMPOUNDS: freeze primitives first. Create the smallest canonical set of materially distinct source-local bindings. One represented binding normally gets one canonical compound. Do not create a compound merely because a primitive exists; do not create graph closure, pairwise permutations, lexical-fragment compounds, subset/superset duplicates, or support-coordinate propagation.

LITERAL LOCK remains absolute after selection. Preserve source wording, dialect, contractions, numbers, uncertainty, negation, modality, comparison, and punctuation exactly where source text is expected.

Never target hidden counts or infer hidden gold. Never expose approved archetypes, evaluator findings, prior scored outputs, calibration answers, or sealed holdout material. Never perform promotion, APA-ID creation, sovereign/admitted writing, or database mutation.
'''.strip()

V97_BASE_RULES = V96_BASE_RULES + "\n\n" + V97_CORRECTION
V97_CLASS_RULES = dict(V96_CLASS_RULES)
V97_CLASS_RULES.update({
    "PLACE": "Recover materially distinct occurrence-support geography, including necessary unnamed coordinates. Broad settings do not erase real local occurrence positions, but spatial mention alone is insufficient; avoid surfaces/path-noun/preposition census.",
    "TIME": "Recover materially distinct source-organizing episodes/phases, including necessary unnamed frames. Broad episodes do not erase real local phases, but temporal mention alone is insufficient; avoid tense/adverb/duration/action-phase census.",
    "PERSON": V96_CLASS_RULES["PERSON"],
    "OBJECT": "Retain source-treated concrete/abstract referents and content handles, including one-use referents. Do not inventory every noun phrase, pronoun, placeholder, clause complement, or action nominalization; generic deixis qualifies only when used as a distinct referential handle.",
    "LABEL": "Retain complete represented characterization units, including candidate labels and material correction/rejection. Do not inventory every modifier, intensifier, decorative phrase, rhetorical flourish, or comparison scaffold.",
    "VERB": "Recover complete semantic relation units. Split only when each resulting relation is independently reconnectable in the represented source; do not split grammatical verb tokens/support fragments and do not create proposition-sized bundles.",
    "LOCATOR": "Recover complete semantic orientation units. Local endpoint-dependent orientation may qualify, but prepositions/particles/adverbs/transitions are not rows unless that occurrence carries a distinct orientation job.",
})
