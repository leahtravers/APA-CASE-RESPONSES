"""V100 neutral apparatus rules: whole-source binding-ledger projection.

These rules contain no archetype answers, evaluator findings, expected counts,
prior scored outputs, or holdout material.
"""
from researcher_inventory.v99_task_rules import V99_BASE_RULES, V99_CLASS_RULES

V100_CORRECTION = r'''

V100 PROSPECTIVE CORRECTION — BINDING-LEDGER PROJECTION.

Read the complete source first and silently construct one whole-source ledger of materially distinct represented bindings: events, states, reports, intentions, questions, comparisons, characterizations, reflections, corrections, prospective/recurring relations, and orientations. Identify only represented role slots: actor, semantic relation, referent/content, characterization, PLACE support, TIME support, orientation, and source posture.

Each class inventory is a projection of that same semantic ledger. A coordinate in one class never substitutes for a genuinely distinct class-native facet in another merely because wording overlaps. Cross-class overlap is allowed only when the same source trace preserves different class-native information.

ADMISSION ROUTES:
1. BINDING_CORE — needed to reconstruct or distinguish a material ledger binding in the requested class.
2. INDEPENDENT_SUPPORT — independently revisitable source-native support that is reused/coreferred, contrasted, questioned, corrected, accepted/rejected, explicitly characterized, independently participates as an argument/endpoint/orientation/support coordinate, or materially distinguishes one binding/phase from another.
3. IMPLICIT_SUPPORT — PLACE/TIME only; a materially distinct represented occurrence/episode/phase needs a support slot but exact place/time is unspecified. Use exact source cue plus neutral mechanical tag and invent no substantive fact.

Vividness, concreteness, descriptiveness, rhetorical force, lexical recurrence, grammatical separability, or possible analyst usefulness never suffice by themselves. After binding-role completeness is achieved, compress away lexical/grammatical/discourse/scene-color remainder.

NO CROSS-CLASS SUBSTITUTION: do not omit a PLACE because a LOCATOR overlaps it, a LOCATOR because a VERB overlaps it, an OBJECT because a LABEL characterizes it, or a TIME because another relation implies the phase, when the source represents a distinct requested-class role. Conversely, do not duplicate identical meaning across classes when no different class-native information exists.

SEMANTIC IDENTITY: merge true aliases/coreference/restatement of one stable coordinate within a class. Preserve distinct relation occurrences and distinct support phases even when wording repeats.

SOURCE-NATIVE GRAIN: select the smallest complete semantic unit, not the smallest lexical fragment. Keep light verbs, necessary complements, particles, reflexives, negation, modality, comparison, or other posture-bearing material together when they jointly form one semantic relation.

LITERAL LOCK: preserve source wording, dialect, contractions, numbers, uncertainty, negation, modality, comparison, attribution, punctuation, and posture. Never normalize to a synonym or analyst-preferred label. Neutral mechanical tags are reserved for legitimate implicit PLACE/TIME support.

COMPOUNDS: after primitive freeze, reconstruct the same binding ledger using only frozen units. Normally one canonical compound represents one materially distinct binding that needs multiple coordinates. Use only minimal participating references. Never create graph closure, one compound per primitive, lexical-fragment compounds, subset/superset permutations, redundant restatements, or mega-bundles.

Never target hidden counts or infer hidden gold. Never expose approved archetypes, evaluator findings, prior scored outputs, calibration answers, or sealed holdout material. Never perform promotion, APA-ID creation, sovereign/admitted writing, or database mutation.
'''.strip()

V100_BASE_RULES = V99_BASE_RULES + "\n\n" + V100_CORRECTION
V100_CLASS_RULES = dict(V99_CLASS_RULES)
V100_CLASS_RULES.update({
    "PLACE": "Project PLACE from the whole-source binding ledger. Retain explicit settings and distinct occurrence positions/support needed to organize material bindings; add neutral IMPLICIT_SUPPORT only for a materially distinct occurrence whose exact place is unspecified. Broad setting never substitutes for a distinct local support role. Reject spatial/scene-detail census.",
    "TIME": "Project TIME from the whole-source binding ledger. Retain distinct episode/phase/span support, including represented attempts, responses, transitions, waits, reports, recurrence, reflection, intention, and prospectivity when they organize materially distinct bindings; add neutral IMPLICIT_SUPPORT only when exact time is unspecified. Reject tense/connective/duration census.",
    "PERSON": "Project distinct represented human/social actors or stable groups from the binding ledger after true coreference. Material actor, social, possessor, beneficiary, remembered, reported, relational, offscreen, or prospective roles may qualify; rhetorical/nonreferential addressees and aliases do not.",
    "OBJECT": "Project source-treated concrete/abstract referents and content handles that are BINDING_CORE or pass the narrow INDEPENDENT_SUPPORT revisitation gate. Abstract decisions/choices/relations/amounts/sets/internal objects may qualify when source-reified. Reject noun-phrase, generic-anaphor, descriptive-noun, clause-complement, and nominalization census.",
    "LABEL": "Project complete source-presented characterizations, candidate characterizations, states/manners, identity/status terms, comparisons, corrections, acceptances/rejections, and polarity units that are BINDING_CORE or pass the narrow revisitation gate. Reject vivid/descriptive/rhetorical modifier census.",
    "VERB": "Project one complete semantic relation per independently represented ledger relation. Keep necessary light-verb/complement/particle/reflexive/negation/modality/posture material together when jointly constitutive. Split only genuinely distinct relations; reject grammatical/support/discourse verb fragments.",
    "LOCATOR": "Project complete orientation/topology relations from the ledger: position, containment/support, origin/destination, path, movement, accompaniment, direction, internal/mental, temporal-position, or figurative/comparative orientation when independently represented. Cross-class overlap with VERB/PLACE is allowed only for a distinct orientation facet. Reject preposition/particle/adverb census.",
})
