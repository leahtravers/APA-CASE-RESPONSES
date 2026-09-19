"""V96 neutral apparatus rules: class-native coordinate sufficiency.

These rules contain no archetype answers, evaluator findings, expected counts,
prior scored outputs, or holdout material.
"""
from researcher_inventory.v94_task_rules import V94_BASE_RULES, V94_CLASS_RULES

V96_CORRECTION = r'''

V96 PROSPECTIVE CORRECTION — CLASS-NATIVE COORDINATE SUFFICIENCY.

Do not use a universal removal test such as "would the whole proposition still be reconstructable without this row?" That test is too coarse across the seven classes. Restore class-native entitlement: a primitive is entitled when the source materially establishes that class's native job at the source's own local resolution. Local, one-use, low-salience, endpoint-dependent, unnamed-support, or wording-overlapping coordinates may be correct. This still does NOT authorize a raw token/POS/noun-phrase census.

PLACE/TIME: recover support geography and chronology at occurrence/episode resolution. A broad scene or episode does not automatically suppress materially distinct local occurrence positions or phases. Necessary unnamed support coordinates are permitted with exact cues. Do not create a row for every locative/temporal mention.

OBJECT/LABEL: preserve source-indexed one-use as well as recurring referents/content handles and characterizations when they perform their class-native job. Do not require recurrence, centrality, or independent whole-proposition necessity. Still suppress arbitrary clause nominalizations, decorative modifiers, and cross-class shadows without a distinct job.

VERB: the target grain is the smallest complete ATOMIC SOURCE RELATION EDGE, not a proposition-sized "complete semantic predicate relation." Split matrix/embedded relations and coordinated relations when each contributes represented structure. Leave separable PERSON/OBJECT/LABEL/PLACE/TIME arguments outside VERB and separable orientation to LOCATOR. Suppress pure auxiliaries/tense support and whole-clause bundles.

LOCATOR: preserve atomic orientation edges even when endpoint-dependent. A movement/state construction may legitimately supply both a VERB edge and a LOCATOR edge, including overlapping source wording, when the relation and orientation jobs differ. Suppress purely grammatical recipient/topic markers and transitions.

CROSS-CLASS OVERLAP: do not force textual disjointness. Overlap is legitimate when each row preserves different class-native information; grammatical ambiguity alone is insufficient.

COMPOUNDS: freeze primitives first, then construct canonical source-local bindings. Integrate applicable local PLACE/TIME/LOCATOR/LABEL support into the represented binding. Do not create graph closure, redundant shadow compounds, pairwise permutations, or proposition-sized primitives as a substitute for compounds.

LITERAL LOCK remains absolute after selection: preserve source language, dialect, contractions, numbers, uncertainty, negation, modality, comparison, and punctuation exactly where source text is expected.

Never target hidden counts or infer hidden gold. Never expose approved archetypes, evaluator findings, prior scored answers, calibration answers, or sealed holdout material to the worker. Never perform promotion, APA-ID creation, sovereign/admitted writing, or database mutation.
'''.strip()

V96_BASE_RULES = V94_BASE_RULES + "\n\n" + V96_CORRECTION
V96_CLASS_RULES = dict(V94_CLASS_RULES)
V96_CLASS_RULES.update({
    "PLACE": "Recover support geography at source occurrence resolution: named settings plus materially distinct local occurrence positions and necessary unnamed places. Broad settings do not suppress legitimate local support; avoid raw locative-mention census.",
    "TIME": "Recover support chronology at source episode/phase resolution, including materially distinct local phases, remembered/recurring/present/prospective spans, and necessary unnamed frames. Avoid tense/adverb/action census.",
    "PERSON": V94_CLASS_RULES["PERSON"],
    "OBJECT": "Retain source-indexed concrete/abstract referents and content handles, including one-use details and source-reified figurative/internal content. Do not require recurrence or coarse proposition-level necessity; avoid arbitrary clause nominalization and jobless shadows.",
    "LABEL": "Retain source-indexed characterizations/candidate characterizations, including local states/manners and material correction/polarity. Brief or one-use characterizations may qualify; avoid decorative modifier or whole-clause census.",
    "VERB": "Recover materially distinct atomic source relation edges. Split matrix/embedded/coordinated relations when structurally distinct; leave separable arguments/orientation outside the verb. Suppress auxiliaries and proposition-sized semantic bundles.",
    "LOCATOR": "Recover materially distinct atomic orientation edges, including local endpoint-dependent position/path/containment/context relations. Legitimate wording overlap with VERB is allowed when relation and orientation jobs differ; suppress purely grammatical markers.",
})
