"""V103 neutral apparatus rules: comprehensive source-reified recovery plus canonical projection.

These rules contain no archetype answers, evaluator findings, expected counts,
prior scored outputs, or holdout material.
"""
from researcher_inventory.inventory_apparatus import BASE_RULES as APPARATUS_BASE_RULES, CLASS_RULES as APPARATUS_CLASS_RULES

V103_CORRECTION = r'''
V103 PROSPECTIVE CORRECTION — COMPREHENSIVE SOURCE-REIFIED RECOVERY + CANONICAL CLASS-NATIVE PROJECTION.

READ THE WHOLE SOURCE. For the requested class, first recover every distinct source-present candidate facet before pruning, including subtle, local, one-use, low-salience, remembered, reported, hypothetical, prospective, figurative, nested, concrete, or abstract facets. A coordinate does NOT have to be globally indispensable, narratively central, repeated, or compound-bound to qualify.

THEN CANONICALIZE. Lightweight resolution comes from canonical span, correct class assignment, semantic identity, deduplication, and class-specific exclusions — not from deleting low-salience source-reified coordinates.

CANONICAL SPAN:
- choose the smallest exact source-native span that is semantically complete for the requested class;
- expand a head fragment when necessary wording carries lexical identity, particle, complement, negation, modality, comparison, uncertainty, posture, or orientation;
- shrink proposition/discourse wrappers when the class-native unit is smaller;
- preserve idioms and inseparable constructions intact;
- never normalize or substitute synonyms.

CLASS ASSIGNMENT:
Classify by research function, not part of speech or physical form. Physical/spatial wording is not automatically PLACE. A source referent can be OBJECT even when spatial. A characterization can be LABEL even when idiomatic/adverbial. A relation can be VERB even when copular, cognitive, reported, modal, or posture-bearing. A LOCATOR can orient by route, context, recurrence, mental frame, relation, or comparison as well as static space.

CROSS-CLASS FACETS:
Overlapping source wording may support more than one class only when each row preserves genuinely different class-native information. Do not suppress a valid facet merely because another class overlaps it. Do not duplicate identical semantic work across classes.

SEMANTIC IDENTITY:
Merge true aliases/coreference/restatements of one stable coordinate. Remove duplicate head-only/full-span variants and analyst paraphrases. Preserve distinct source-present occurrences/facets when they do different research work.

PLACE/TIME SUPPORT:
Preserve explicit broad and local support when they do different work. Restore neutral unnamed PLACE/TIME support when a distinct represented frame needs a support slot but exact location/time is unstated. Do not create one support row per clause or inventory every spatial/temporal token.

LOW-SALIENCE RECOVERY SWEEP:
Before freezing primitives, revisit the whole source and restore any distinct class-native coordinate rejected merely because it was one-use, subtle, local, nested, descriptive, concrete, or not globally indispensable.

WRONG-CLASS / FRAGMENT SWEEP:
Before freezing primitives, remove grammar-only fragments, proposition wrappers, unsupported inference, generic deixis with no distinct referent, duplicate semantic rows, and wrong-class projections. Reassign rather than duplicate when one class is the true function.

LITERAL LOCK:
Preserve exact source wording, dialect, contractions, numbers, uncertainty, negation, modality, comparison, attribution, punctuation, and figurative posture. Neutral mechanical tags are reserved for legitimate unnamed PLACE/TIME support.

COMPOUNDS:
Freeze all seven canonical primitive classes first. Then build only a selective canonical set of source-local multi-coordinate bindings. Use frozen refs only. Do not make graph closure, pairwise closure, one compound per primitive/clause, subset/superset permutations, redundant restatements, or scene mega-bundles.

Never target hidden counts or infer hidden gold. Never expose approved archetypes, evaluator findings, prior scored outputs, calibration answers, or sealed holdout material. Never perform promotion, APA-ID creation, sovereign/admitted writing, or database mutation.
'''.strip()

V103_BASE_RULES = APPARATUS_BASE_RULES + "\n\n" + V103_CORRECTION
V103_CLASS_RULES = dict(APPARATUS_CLASS_RULES)
V103_CLASS_RULES.update({
    "PLACE": (
        "Recover every distinct explicit setting or local/contained location support plus legitimate neutral unnamed support needed to reconnect a distinct represented frame. "
        "Broad support does not erase local support when they do different work. Low-salience or one-use place supports remain eligible. "
        "Reject physical-object/spatial-token census, movement alone, and duplicate supports doing identical work."
    ),
    "TIME": (
        "Recover every distinct explicit period and semantic episode/span support for represented attempts, responses, waits, conversations, reports, memories, transitions, recurrence, reflection, intentions, alternatives, and prospects. "
        "Use neutral unnamed support when the phase is distinct but exact time is unstated. Merge expressions serving one phase; reject tense/connective/duration census and one-frame-per-clause proliferation."
    ),
    "PERSON": (
        "Recover the speaker and every distinct represented human/social actor or stable group after true coreference. One-use, local, offscreen, remembered, reported, possessive, institutional, relational, and prospective actors may qualify. "
        "Suppress true aliases/coreferent repeats and rhetorical/nonreferential addressees only."
    ),
    "OBJECT": (
        "Recover source-reified concrete and abstract referents/content handles at canonical source-native grain, including low-salience and one-use handles when distinctly represented. "
        "Things acted on, checked, possessed, chosen, contrasted, remembered, reported, considered, or used as stable reference anchors may qualify; so may source-reified choices, decisions, relations, conditions, amounts, alternatives, and internal content. "
        "Reject noun-phrase census, generic pronouns/deixis without a distinct referent, discourse organizers, proposition wrappers, and duplicate/coreferent variants."
    ),
    "LABEL": (
        "Recover source-present characterization, quality, state, identity, manner/posture, comparison, candidate label, correction, acceptance/rejection, or polarity units at the smallest complete exact span. "
        "Idiomatic, local, adverbial, comparative, figurative, and one-use descriptive units may qualify when they preserve a distinct characterization. "
        "Reject modifier/intensifier census, grammar-only fragments, duplicate variants, and proposition wrappers."
    ),
    "VERB": (
        "Recover source-present semantic relations/predicates at the smallest complete predicate span. Action, state, copular, speech/report, cognition, intention, question, comparison, modality, possession, movement, waiting, trying, remembering, deciding, and similar relations may qualify when semantically present. "
        "Normally omit subjects and externalize retained arguments, but keep required particles/prepositions/complements, reflexives, negation, modality, and posture. "
        "Reject pure auxiliary/grammar support only when it carries no separate relation; reject head fragments and clause-sized wrappers."
    ),
    "LOCATOR": (
        "Recover source-present orienting constructions at the smallest complete span: spatial position/containment, origin/destination/path, approach/exit/direction, proximity, accompaniment, recurrence, procedural/relational context, mental/internal orientation, temporal-position orientation, and figurative/comparative orientation may qualify. "
        "Overlap with VERB/PLACE/TIME is allowed only for a distinct orientation facet. Reject preposition/particle/adverb census, mere recipients/topics/durations, duplicate projections, and fragmentary heads."
    ),
})
