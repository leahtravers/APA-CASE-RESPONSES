"""Neutral V54 task rules. No gold rows/counts/evaluator findings/holdout content."""
from researcher_inventory.v53_task_rules import V53_BASE_RULES, V53_CLASS_RULES

V54_DELTA = """
V54 EXHAUSTIVE RELATION-PRESERVING DECOMPOSITION: keep V53's protection against syntactic over-fragmentation, but do not let relation integrity suppress a second source-distinguished coordinate. Before collapsing anything, scan the entire source for every plausible class-native coordinate, including nested, embedded, unnamed, grammatically dependent, and relation-participating material. Retain a candidate when it has its own reusable class-native research function after context is restored; grammatical dependence is not an exclusion rule. VERB: split genuinely distinct relation jobs even when one is infinitival, coordinated, reported, or embedded; merge only words that together express one relation identity. TIME: one broad episode may contain distinct source-established temporal frames; do not create one per predicate, but do not collapse distinct before/after/recurring/waiting/current/prospective/transition roles merely because they share an episode. PLACE: supported unnamed scenes and source-established physical endpoints/contained positions may qualify when independently reusable; relational wording alone does not disqualify them. OBJECT/LABEL/LOCATOR: a complement, argument, predicate-linked value, or orientation phrase may qualify when the source independently treats it as a reusable thing/value/orientation. Deduplicate true aliases/restatements, not parent/child coordinates merely because they participate in one larger relation. Freeze primitive units before compounds; compounds recombine proven bindings and must not replace or erase independently retained primitives.
"""

V54_BASE_RULES = V53_BASE_RULES + "\n" + V54_DELTA
V54_CLASS_RULES = dict(V53_CLASS_RULES)
V54_CLASS_RULES.update({
    "PLACE": V53_CLASS_RULES["PLACE"] + " Preserve a supported unnamed or relationally expressed physical scene/occurrence position when it is independently reusable; do not reject it solely because it is also an endpoint, contained position, or locator participant.",
    "TIME": V53_CLASS_RULES["TIME"] + " A broad episode may contain multiple source-distinguished temporal roles or frames. Preserve those independent frames while still rejecting one-TIME-per-predicate fragmentation.",
    "OBJECT": V53_CLASS_RULES["OBJECT"] + " A complement or relation argument may still be OBJECT when the source independently treats its content as a stable reusable referent; grammatical embedding alone is not exclusion.",
    "LABEL": V53_CLASS_RULES["LABEL"] + " Preserve a nested or predicate-linked state/value when that value itself is independently reusable as characterization; embedding alone is not exclusion.",
    "VERB": V53_CLASS_RULES["VERB"] + " Do not merge genuinely distinct relation jobs merely because one is infinitival, coordinated, reported, embedded, or grammatically dependent on another. Relation identity, not syntax alone, decides split versus merge.",
    "LOCATOR": V53_CLASS_RULES["LOCATOR"] + " Preserve a relation-participating phrase when it independently supplies a reusable orientation relation; participation in another retained relation does not by itself make it excess."
})
