"""V105 neutral apparatus rules: relation decomposition + class-slot coverage.

These rules contain no archetype answers, evaluator findings, expected counts,
prior scored outputs, or holdout material.
"""
from researcher_inventory.v104_task_rules import V104_BASE_RULES, V104_CLASS_RULES

V105_CORRECTION = r'''
V105 PROSPECTIVE CORRECTION — RELATION DECOMPOSITION + CLASS-SLOT COVERAGE.

V104'S POSITIVE FRAME-ANCHORED ADMISSION REMAINS REQUIRED, BUT DO NOT JUMP DIRECTLY FROM A GLOBAL FRAME MAP TO ROW SELECTION. BEFORE ADMISSION, WALK EVERY REPRESENTED RELATION/FRAME IN SOURCE ORDER AND SILENTLY DECOMPOSE IT INTO THE DISTINCT CLASS-NATIVE ROLES THE SOURCE ACTUALLY PRESENTS:
- relation kernel;
- human/social actors;
- concrete or abstract referential/content handles;
- source-present characterizations;
- PLACE support;
- TIME support;
- orienting/LOCATOR relations.

THIS IS DECOMPOSITION, NOT A QUOTA. A SLOT STAYS EMPTY WHEN THE SOURCE SUPPLIES NO DISTINCT CLASS-NATIVE COORDINATE. NEVER FABRICATE A ROW TO COMPLETE A TEMPLATE.

ANTI-PROPOSITION RULE: when a clause or proposition separates into a relation kernel plus independently qualifying actors/referents/characterizations/support/orientations, inventory those class-native coordinates separately. Do not preserve the whole clause as a VERB, OBJECT, LABEL, or LOCATOR merely because it expresses coherent content. Keep only essential complements that are part of the coordinate's own identity.

CLASS-SLOT COVERAGE AUDIT: after the first decomposition pass, revisit every represented relation/frame and ask whether any qualifying class-native role was omitted merely because it was ordinary, subtle, local, mundane, one-use, reported, remembered, prospective, figurative, concrete, abstract, or grammatically simple. Restore it when it satisfies a positive route. This is local coverage, not global indispensability.

RELATION KERNELS: simple/copular/reporting/speech/possession/cognition/perception/movement/question/state/decision/comparison predicates can be genuine VERB coordinates when they are the represented relation, not merely narration or grammar. Grammatical simplicity is not a pruning reason. Externalize independently qualifying participants, content, support, labels, and locators.

REFERENTIAL HANDLES: mundane, local, one-use concrete or abstract things remain OBJECT-eligible when a represented relation actually uses them as distinct arguments/anchors. Mere nounhood remains insufficient. Do not dismiss a qualifying referent merely as scenery when it is acted on, possessed, checked, selected, contrasted, remembered, reported, considered, exchanged, located, or otherwise relationally engaged.

PLACE/TIME SUPPORT: assess support relation by relation, not only at scene level. Distinct local, remembered, reported, intended, prospective, recurring, and present-telling episodes/phases may retain separate support when the source differentiates them. Merge supports doing the same job. Never invent geography or chronology.

FUNCTIONAL TIE-BREAKS:
- human/social actor -> PERSON;
- distinct concrete/abstract referential or content handle -> OBJECT;
- source-present characterization/state/identity/comparison/correction/posture -> LABEL;
- episode/location support -> PLACE;
- period/phase support -> TIME;
- represented predicate/relation kernel -> VERB;
- relation that positions/contextualizes another coordinate/frame -> LOCATOR.
Cross-class overlap is allowed only when each projection preserves genuinely different information.

ATOMIC SPAN + LITERAL LOCK: choose the smallest complete exact source-native span for the class-native function. Preserve required particles/prepositions, reflexives, negation, modality, uncertainty, attribution, idiom, comparison, and posture. Never normalize, paraphrase, clean up, lemmatize into a different surface form, or substitute synonyms. Expand a head fragment only when necessary for identity; shrink a proposition wrapper when separable coordinates carry its content.

FREEZE AUDITS IN ORDER:
1. relation decomposition;
2. class-slot coverage;
3. positive admission route;
4. anti-proposition;
5. anti-tokenization;
6. atomic span;
7. wrong-class/function tie-break;
8. PLACE/TIME support;
9. literal lock;
10. semantic deduplication.
Repeat until stable before constructing compounds.

COMPOUNDS REMAIN DOWNSTREAM. Use only frozen canonical refs and build a selective source-local set. Primitive semantic errors must be fixed at the primitive layer; do not compensate with compound proliferation or evaluator changes.

Never target hidden counts or infer hidden gold. Never expose approved archetypes, evaluator findings, prior scored outputs, calibration answers, or sealed holdout material. Never perform promotion, APA-ID creation, sovereign/admitted writing, or database mutation.
'''.strip()

V105_BASE_RULES = V104_BASE_RULES + "\n\n" + V105_CORRECTION
V105_CLASS_RULES = dict(V104_CLASS_RULES)
V105_CLASS_RULES.update({
    "PLACE": (
        "After relation decomposition, retain explicit settings and distinct local/contained PLACE support used by represented episodes, plus neutral unnamed support when a distinct episode has no explicit location. "
        "Assess support relation-by-relation, including remembered, reported, intended, prospective, recurring, and present-telling frames when the source distinguishes them. "
        "Merge supports doing the same job; reject physical-noun/spatial-token census."
    ),
    "TIME": (
        "After relation decomposition, retain explicit periods and distinct semantic episode/phase supports. Assess temporal support relation-by-relation rather than only at whole-scene level. "
        "Merge expressions serving one phase and separate genuinely different phases; use neutral unnamed support when a distinct phase is unstated. "
        "Reject tense, duration, connective, now/then, and one-time-row-per-clause census behavior."
    ),
    "PERSON": (
        "Retain the speaker and each distinct represented human/social actor or stable group after true coreference when that actor occupies an actor/participant/possessive/reported/remembered/prospective role in a represented relation. "
        "Ordinary, one-use, offscreen, institutional, and relational actors remain eligible. Suppress aliases and rhetorical/nonreferential addressees."
    ),
    "OBJECT": (
        "Retain concrete or abstract referential/content handles that occupy a distinct argument/anchor slot in a represented relation or are independently reified. "
        "Mundane, local, one-use, scene-bound handles remain eligible when acted on, possessed, checked, selected, contrasted, remembered, reported, considered, exchanged, located, or otherwise relationally engaged. "
        "Reject noun census, generic pronouns/deixis, discourse organizers, and proposition wrappers without separate referential identity."
    ),
    "LABEL": (
        "Retain source-present characterization slots: distinct qualities, states, identities, comparisons, candidate labels, corrections, polarity, manner, or posture represented by the source. "
        "Choose the smallest complete literal span. Reject modifier census, whole-proposition wrappers, and colorful wording whose only function is style."
    ),
    "VERB": (
        "Retain the atomic relation kernel for each represented relation. Simple/copular/reporting/speech/possession/cognition/perception/movement/question/state/decision/comparison predicates remain eligible when they are the represented relation. "
        "Normally omit subjects and externalize independently qualifying objects/content, labels, place/time support, and locators while keeping particles/prepositions/complements essential to predicate identity, reflexives, negation, modality, and posture. "
        "Reject auxiliary-only rows, narration-only carriers, and clause/proposition wrappers when separable coordinates carry their content."
    ),
    "LOCATOR": (
        "After relation decomposition, retain distinct orienting relations that position/contextualize another coordinate or frame by containment, path, origin/destination, direction, proximity, accompaniment, recurrence, procedural/relational context, mental/internal frame, temporal position, or figurative/comparative orientation. "
        "Use the smallest complete literal span. Reject preposition/adverb/recipient/topic/duration/deixis/comparison census and proposition wrappers."
    ),
})
