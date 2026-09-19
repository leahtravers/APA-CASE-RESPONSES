"""V101 neutral apparatus rules: coordinate-first kernel/frame inventory.

These rules contain no archetype answers, evaluator findings, expected counts,
prior scored outputs, or holdout material.
"""
from researcher_inventory.v100_task_rules import V100_BASE_RULES, V100_CLASS_RULES

V101_CORRECTION = r'''
V101 PROSPECTIVE CORRECTION — COORDINATE-FIRST KERNEL/FRAME INVENTORY.

This correction supersedes any V100 wording that makes primitive admission depend on membership in a whole-source binding ledger or likely compound use.

FIRST recover class-native source coordinates. THEN freeze primitives. ONLY AFTERWARD build selective compounds. A valid primitive may remain completely unbundled.

PRIMITIVE ADMISSION:
- Admit a distinct source-reified actor, referent, characterization, semantic relation kernel, orientation/frame relation, place, or time frame that is independently selectable in its class.
- Ordinary concrete scene entities and low-salience one-use referents are eligible; thematic importance and compound membership are not requirements.
- Admit abstract choices/decisions/relations/conditions/internal objects only when the source reifies them as distinct handles.
- PLACE/TIME may use neutral implicit support for a distinct represented setting/episode/span whose exact place/time is unnamed.
- Do not admit grammatical or proposition wrappers merely because they can be segmented.

PROPOSITION DE-BUNDLING:
A sentence/clause contains coordinates but is not automatically a VERB, LABEL, OBJECT, TIME, or LOCATOR. Choose the smallest complete class-native kernel. A broad clause-sized row is wrong when its remaining words are independently selectable participants/content/characterizations/support or mere discourse scaffolding.

REFERENTIAL SWEEP:
For PERSON and OBJECT, rescan the whole source for distinct represented handles, including ordinary physical/environmental items and low-salience referents. Do not omit them merely because they never enter a compound. Generic anaphors/metadiscourse nouns require their own stable source-reified identity.

RELATION KERNEL:
VERB is the shortest complete source-native predicate construction. Normally omit the subject and externalize independently selectable actor/object/content/label/place/time/locator arguments. Keep a particle, reflexive, required preposition, negation, modality, light-verb support, or complement only when needed for the predicate's lexical/semantic identity. Split independently selectable matrix/embedded/coordinated relations. Never return a whole proposition when a smaller relation kernel preserves the predicate.

FRAME DISCIPLINE:
PLACE/TIME inventory semantic support frames, not every spatial/temporal word or every ledger event. LOCATOR inventories orientation/frame relations, not recipients, topics, durations, discourse deixis, or every preposition/adverb. LABEL inventories characterization units, not whole evaluative propositions; keep independently selectable candidate/denial/correction units separate.

LITERAL LOCK remains absolute: preserve source wording, dialect, contractions, uncertainty, negation, modality, comparison, attribution, punctuation, and figurative posture. Do not normalize to synonyms or analyst-preferred terms.

COMPOUNDS remain selective. A primitive need not be bundled. Build only smallest materially useful multi-coordinate source-local bindings from frozen units. Do not emit exhaustive predicate/proposition closure, one compound per primitive, pairwise closure, subset/superset variants, or scene mega-bundles.

Never target hidden counts or infer hidden gold. Never expose approved archetypes, evaluator findings, prior scored outputs, calibration answers, or sealed holdout material. Never perform promotion, APA-ID creation, sovereign/admitted writing, or database mutation.
'''.strip()

V101_BASE_RULES = V100_BASE_RULES + "\n\n" + V101_CORRECTION

V101_CLASS_RULES = dict(V100_CLASS_RULES)
V101_CLASS_RULES.update({
    "PLACE": (
        "Coordinate-first PLACE: retain settings/location supports in which represented actors, objects, relations, conversations, waits, reports, reflections, or distinct material are situated. "
        "Keep materially distinct broad/contained/local settings and legitimate unnamed support places. "
        "Do not type a source-treated referent as PLACE merely because its wording is spatial, and do not create a PLACE for every clause or movement."
    ),
    "TIME": (
        "Coordinate-first TIME: retain distinct semantic episode/span frames that organize represented material, including recurring, relational, reflective, intended, or prospective frames when distinct. "
        "Merge surface temporal expressions that belong to one semantic frame. Use neutral implicit support when a distinct frame is unnamed. "
        "Do not inventory tense, now/then words, durations, connectives, or one TIME per clause/event."
    ),
    "PERSON": (
        "Retain the speaker and every distinct represented human/social actor or stable group after true coreference. "
        "Minor, one-use, offscreen, remembered, reported, relational, possessive, beneficiary, institutional, or prospective actors may qualify. "
        "Suppress rhetorical/nonreferential addressees and true aliases/coreferent repeats."
    ),
    "OBJECT": (
        "Coordinate-first OBJECT: retain independently selectable concrete and abstract referential handles. "
        "Rescan for ordinary physical/environmental scene entities and low-salience one-use referents even when unbundled. "
        "Admit abstract choices, decisions, relations, conditions, internal objects, sets, or categories only when source-reified. "
        "Reject clause/proposition wrappers, generic anaphors, metadiscourse handles, and nominalizations that lack their own stable referential identity. "
        "Do not type a referent as PLACE merely because its wording is spatial."
    ),
    "LABEL": (
        "Coordinate-first LABEL: retain smallest complete source-presented characterization, quality, state, identity, comparison, candidate label, correction, acceptance/rejection, or polarity unit. "
        "Keep independently selectable candidate/denial/revision units separate instead of merging a whole evaluative sequence. "
        "Reject whole propositions, rhetorical bundles, and wording whose only job is integral to another coordinate's identity."
    ),
    "VERB": (
        "Coordinate-first VERB: return the shortest complete source-native semantic relation kernel, not a proposition and not raw verb tokens. "
        "Normally omit subjects and externalize independently selectable participants/content/labels/place/time/locator arguments. "
        "Keep particles, reflexives, required prepositions, negation, modality, light-verb support, or complements only when required for lexical/semantic identity. "
        "Split independently selectable matrix/embedded/coordinated relations; reject clause-sized restatements when a smaller predicate kernel preserves the relation."
    ),
    "LOCATOR": (
        "Coordinate-first LOCATOR: retain smallest complete source-native orientation/frame relations that position a coordinate relative to another coordinate or frame, including spatial/topological, origin/destination/path, movement, proximity, figurative/comparative, and genuine recurrence/context orientation. "
        "Overlap with VERB/PLACE/TIME is allowed only for an independently selectable orientation facet. "
        "Reject recipients, addressees, mere topics, durations, discourse deixis, and every-preposition/adverb census."
    ),
})
