"""V99 neutral apparatus rules: source-native grouping plus editorial admission proof.

These rules contain no archetype answers, evaluator findings, expected counts,
prior scored outputs, or holdout material.
"""
from researcher_inventory.v97_task_rules import V97_BASE_RULES, V97_CLASS_RULES

V99_CORRECTION = r'''

V99 PROSPECTIVE CORRECTION — EDITORIAL ADMISSION PROOF.

Retain V97 class-native entitlement and complete-semantic-unit grouping. Correct the V98 oscillation between over-pruning and lexical/grammatical census by admitting primitives only through one of three semantic lanes:

1. BINDING_CORE: required to reconstruct a materially represented binding in its class-native role.
2. QUALITATIVE_SUPPORT: an independently represented, source-native referent/characterization/detail/orientation materially qualifies a binding or scene even when it need not appear in the binding's explicit compound references.
3. IMPLICIT_SUPPORT: PLACE or TIME only; a distinct represented occurrence/episode/conversation/wait/memory/reflection/report/performance requires a support slot but the exact place/time is unspecified. Use an exact source cue and a neutral mechanical tag; do not invent substantive content.

A proposed primitive that fits none of these lanes is excluded. Completeness is audited at this editorial semantic layer, never by token/POS/noun-phrase/clause/verb/preposition/adverb/spatial-mention/temporal-mention census.

UNIVERSAL EXCLUSIONS: suppress grammar-only support; discourse scaffolding; generic pronouns/deixis that merely point to an already represented referent; clause or phrase fragments admitted only because they are segmentable; physical/spatial/temporal mentions that do not organize a distinct source role; decorative modifiers without independent characterization identity; and duplicate/coreferent/paraphrastic restatements.

SEMANTIC IDENTITY: one stable actor/referent/characterization/support/orientation coordinate survives repeated/coreferent mentions. Repeated relation wording may yield separate VERB rows only for genuinely distinct represented relation occurrences/bindings.

PLACE/TIME: check for implicit support after mapping material occurrences/episodes. Broad support does not erase a distinct local support role, but every spatial/temporal phrase is not a coordinate.

PERSON: retain each distinct represented actor/group after true coreference when materially represented.

OBJECT: retain source-treated referents/content handles that are binding-core or independently represented qualitative support. Do not inventory generic anaphora, noun phrases, clause complements, or nominalizations by grammar alone.

LABEL: retain complete represented characterization/candidate-characterization/correction/polarity units that are binding-core or independently represented qualitative support. Do not inventory every modifier or rhetorical flourish.

VERB: retain one complete semantic relation per independently represented relation occurrence. Necessary negation/modality/support stays with the relation; pure auxiliary/copular/tense/discourse fragments do not become rows.

LOCATOR: retain one complete semantic orientation relation when independently represented as binding-core or qualitative support. Do not inventory prepositions/particles/adverbs.

QUALITIES_AVAILABLE: this boolean marks source-present qualitative/descriptive availability under the schema. It is not confidence and does not create/suppress primitives. Qualitative/support coordinates may be available around a compound without being forced into its explicit reference list.

COMPOUNDS: reconstruct only the smallest canonical materially represented bindings. Explicit references normally use binding-core coordinates plus only support/qualification/orientation necessary to distinguish the binding. Qualitative-support primitives do not automatically propagate into compounds. Never create graph closure, pairwise combinations, fragment compounds, subset/superset permutations, or one compound per primitive.

LITERAL LOCK: preserve source language, dialect, contractions, numbers, uncertainty, negation, modality, comparison, and punctuation exactly after selection. Use source-near tags when wording exists; reserve neutral mechanical tags for legitimate implicit PLACE/TIME support.

Never target hidden counts or infer hidden gold. Never expose approved archetypes, evaluator findings, prior scored outputs, calibration answers, or sealed holdout material. Never perform promotion, APA-ID creation, sovereign/admitted writing, or database mutation.
'''.strip()

V99_BASE_RULES = V97_BASE_RULES + "\n\n" + V99_CORRECTION
V99_CLASS_RULES = dict(V97_CLASS_RULES)
V99_CLASS_RULES.update({
    "PLACE": "Admit occurrence-support geography only through BINDING_CORE, QUALITATIVE_SUPPORT, or legitimate IMPLICIT_SUPPORT. Preserve explicit settings and distinct local occurrence support; create neutral unnamed support only for a distinct represented occurrence whose exact place is unspecified. Reject spatial mention census.",
    "TIME": "Admit episode/phase chronology only through BINDING_CORE, QUALITATIVE_SUPPORT, or legitimate IMPLICIT_SUPPORT. Preserve explicit periods and distinct phases; create neutral unnamed support only for a distinct represented episode whose exact time is unspecified. Reject tense/adverb/duration mention census.",
    "PERSON": "Retain every distinct represented human/social actor or stable group after true coreference when materially represented. One-use/offscreen/remembered/relational actors may qualify; rhetorical addressees and coreferent repeats do not.",
    "OBJECT": "Retain source-treated concrete/abstract referents or content handles that are binding-core or independently represented qualitative support. Reject generic anaphora/deixis, noun-phrase/clause-fragment census, and duplicate semantic referents.",
    "LABEL": "Retain complete represented characterization/candidate-characterization/correction/polarity units that are binding-core or independently represented qualitative support. Reject modifier/intensifier/decorative/rhetorical census.",
    "VERB": "Retain one complete semantic relation per independently represented relation occurrence. Repeated wording can remain separate only for distinct events/bindings. Keep necessary posture support with the relation; reject grammatical/support verb fragments.",
    "LOCATOR": "Retain one complete semantic orientation/topology relation when independently represented as binding-core or qualitative support. Endpoint/local orientation may qualify; reject preposition/particle/adverb census and duplicated VERB meaning.",
})
