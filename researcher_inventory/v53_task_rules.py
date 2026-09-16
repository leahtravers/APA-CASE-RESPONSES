"""Neutral V53 task rules. No gold rows/counts/evaluator findings/holdout content."""
from researcher_inventory.v52_task_rules import V52_BASE_RULES, V52_CLASS_RULES

V53_DELTA = """
V53 RELATION-INTEGRITY CORRECTION: source-coordinate breadth does not mean syntactic census. After broad coverage, collapse relation-internal fragments back into the smallest COMPLETE semantic coordinate. Do not mint a TIME for each action/clause inside one episode; do not promote a movement endpoint, object-position phrase, figurative locative, or orientation-only phrase to PLACE unless it independently establishes a physical scene/occurrence position; do not create OBJECT/LABEL/LOCATOR merely from ordinary complements, arguments, question scaffolding, or relation-internal fragments. For VERB, relation identity outranks token minimalism: keep matrix/infinitival/particle/complement/negation/modal/serial/coordinated wording together when it expresses one source-presented relation, and split only genuinely independently revisitable relations. Cross-class overlap requires genuinely distinct class-native functions, not maximum coverage. Compounds must not duplicate one relation through nested subset alternatives.
"""

V53_BASE_RULES = V52_BASE_RULES + "\n" + V53_DELTA
V53_CLASS_RULES = dict(V52_CLASS_RULES)
V53_CLASS_RULES.update({
    "PLACE": V52_CLASS_RULES["PLACE"] + " Do not promote locator endpoints, object-position phrases, figurative locations, or comparison positions to PLACE unless they independently establish a reusable physical scene/occurrence position.",
    "TIME": V52_CLASS_RULES["TIME"] + " Multiple predicates, thoughts, questions, and purposes inside one represented episode normally share one TIME; require a genuinely distinct episode/period/frame before adding another.",
    "OBJECT": V52_CLASS_RULES["OBJECT"] + " Do not create separate OBJECT wrappers for ordinary complements, proposition content, or relation arguments already represented by a stable retained referent/relation unless the source independently treats that content as a reusable thing.",
    "LABEL": V52_CLASS_RULES["LABEL"] + " Do not inventory ordinary negation, question scaffolding, duration wording, relation wording, or descriptive fragments unless the source presents the span itself as an independently selectable state/value.",
    "VERB": V52_CLASS_RULES["VERB"] + " Preserve one complete lexical relation as one VERB even when it contains matrix/infinitival/particle/complement/negation/modal/serial/coordinated material; split only genuinely independent relation jobs.",
    "LOCATOR": V52_CLASS_RULES["LOCATOR"] + " Reject ordinary argument/beneficiary/content prepositional phrases and locator-looking state/value fragments unless they independently supply a reusable orientation relation."
})
