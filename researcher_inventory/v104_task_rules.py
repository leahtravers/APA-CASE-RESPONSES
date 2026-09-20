"""V104 neutral apparatus rules: frame-anchored class-native admission.

These rules contain no archetype answers, evaluator findings, expected counts,
prior scored outputs, or holdout material.
"""
from researcher_inventory.inventory_apparatus import BASE_RULES as APPARATUS_BASE_RULES, CLASS_RULES as APPARATUS_CLASS_RULES

V104_CORRECTION = r'''
V104 PROSPECTIVE CORRECTION — FRAME-ANCHORED CLASS-NATIVE ADMISSION.

READ THE WHOLE SOURCE FIRST. Silently map its represented relations and frames: actions, interactions, states, attempts, responses, waits, questions, decisions, intentions, reports, memories, comparisons, corrections, recurrence, reflection, and prospective relations, together with the actors, referential handles, characterizations, support frames, and orientations that the source itself uses in them.

ADMIT BY POSITIVE RESEARCH ROLE, NOT BY MENTION. A primitive is eligible only when its exact source-present trace performs a distinct class-native research function inside a represented relation/frame, or is legitimate PLACE/TIME support for one. Low-salience, local, nested, subtle, concrete, abstract, figurative, remembered, reported, hypothetical, prospective, and one-use coordinates may qualify. They do NOT need recurrence, narrative centrality, compound membership, or global indispensability.

POSITIVE ROUTES:
- FRAME_ARGUMENT: distinct actor/referent/content/characterization/endpoint/support/orientation in a represented relation/frame;
- INDEPENDENT_REIFICATION: source separately names, identifies, possesses materially, contrasts, selects, questions, corrects, accepts/rejects, remembers/reports, or otherwise treats the coordinate as a reconnectable handle;
- RELATION_KERNEL: for VERB, a distinct represented relation/state/attempt/report/cognition/intention/decision/comparison/movement/question/possession rather than a grammatical verb token;
- CHARACTERIZATION_KERNEL: for LABEL, a distinct source-present characterization/state/identity/comparison/candidate/correction/polarity/posture rather than any modifier;
- ORIENTATION_KERNEL: for LOCATOR, a distinct source-present orienting relation rather than any preposition/adverb/topic/recipient/comparison phrase;
- SUPPORT_FRAME: PLACE/TIME only, explicit or neutral implicit support that distinguishes a represented episode/phase without inventing geography or chronology.

NON-ADMISSION EVIDENCE: lexical occurrence, part of speech, grammatical separability, vividness, concreteness, one-use mention, repetition, describability, chronological sequence, spatial wording, or possible analyst usefulness never suffices by itself. Do not build noun, verb, modifier, temporal, spatial, or preposition censuses. Ordinary discourse organization, narration, quotation/report framing, and grammar are not primitives unless they themselves perform one of the positive source-present research roles above.

CANONICALIZE AFTER ADMISSION. Choose the smallest exact source-native span that remains semantically complete for the class-native function. Keep required particles/prepositions, reflexives, light-verb support, essential complements, negation, modality, uncertainty, comparison, attribution, idiom, and posture. Shrink proposition/discourse wrappers. Expand head fragments that lose necessary identity. Never normalize or substitute synonyms.

CLASSIFY BY RESEARCH FUNCTION, NOT FORM. Physical/spatial wording is not automatically PLACE. A concrete or abstract handle may be OBJECT. Descriptive wording may be LABEL. A relation may be VERB even if copular, cognitive, reported, modal, or posture-bearing. A LOCATOR may orient by path, context, recurrence, relation, mental frame, temporal position, or comparison. Overlap across classes is allowed only when each projection preserves genuinely different information.

SEMANTIC IDENTITY: merge true aliases, coreference, restatements, inflection-only repeats, and duplicate head/full-span variants. Preserve distinct local roles/occurrences when the source itself differentiates them. Never add analyst paraphrases beside literal source wording.

AUDIT BEFORE FREEZE:
1. Frame coverage — every represented relation/frame gets the class-native coordinates it actually uses.
2. Positive-route audit — every proposed primitive must name a qualifying route; if justification is only lexical/grammatical presence, remove it.
3. Low-salience recovery — restore subtle/one-use/local coordinates that do qualify.
4. Anti-tokenization — remove noun/verb/modifier/spatial/temporal/preposition census rows.
5. Canonical span — fix too-short fragments and too-long proposition wrappers.
6. Wrong class — reassign rather than duplicate identical work.
7. PLACE/TIME support — restore distinct support frames and merge redundant ones.
8. Literal/dedup — exact wording, no synonyms/inference/duplicates.
Repeat until stable, then freeze primitives.

COMPOUNDS: only after all seven primitive classes are frozen, build a selective canonical set of source-local multi-coordinate bindings. Use frozen refs only. No graph closure, pairwise closure, one compound per primitive/clause, singleton equivalents, subset/superset permutations, redundant restatements, or scene mega-bundles. A primitive may remain unbundled. Compounds never justify missing or extra primitives.

Never target hidden counts or infer hidden gold. Never expose approved archetypes, evaluator findings, prior scored outputs, calibration answers, or sealed holdout material. Never perform promotion, APA-ID creation, sovereign/admitted writing, or database mutation.
'''.strip()

V104_BASE_RULES = APPARATUS_BASE_RULES + "\n\n" + V104_CORRECTION
V104_CLASS_RULES = dict(APPARATUS_CLASS_RULES)
V104_CLASS_RULES.update({
    "PLACE": (
        "Retain explicit settings/local supports only when they distinguish a represented relation or frame, plus neutral unnamed support when a distinct frame has no explicit location. "
        "Broad and local supports may coexist only when they do different research work. One-use support may qualify. "
        "Reject surfaces, physical objects, spatial nouns, scenic detail, movement, and prepositional wording that do not function as frame support."
    ),
    "TIME": (
        "Retain explicit periods and semantic episode/span supports that distinguish represented phases. Merge expressions serving one phase and separate genuinely different phases. "
        "Use neutral unnamed support for a distinct phase with unstated time. Reject tense, every now/then, duration/connective census, chronology tokens, and one-time-row-per-clause behavior."
    ),
    "PERSON": (
        "Retain the speaker and every distinct represented human/social actor or stable group after true coreference when that actor functions in represented source structure. "
        "One-use, offscreen, possessive, remembered, reported, institutional, relational, and prospective actors may qualify. Suppress aliases/coreference and rhetorical/nonreferential addressees."
    ),
    "OBJECT": (
        "Retain concrete or abstract referential/content handles that function as FRAME_ARGUMENT or INDEPENDENT_REIFICATION. "
        "Eligible handles may be acted on, checked, possessed, selected, contrasted, remembered, reported, considered, exchanged, or otherwise source-reified, including choices/decisions/relations/conditions/amounts/categories/alternatives/internal content. "
        "Reject noun-phrase census, incidental scenery, generic pronouns/deixis, discourse organizers, proposition wrappers, and nominalized grammar without separate referential identity."
    ),
    "LABEL": (
        "Retain CHARACTERIZATION_KERNEL units: source-present qualities, states, identities, comparisons, candidate labels, corrections, acceptances/rejections, polarity, or meaningful manner/posture at the smallest complete exact span. "
        "Idiomatic, local, adverbial, figurative, comparative, subtle, and one-use characterizations may qualify. Reject adjective/adverb/intensifier/colorful-aside census and grammar-only modifiers."
    ),
    "VERB": (
        "Retain RELATION_KERNEL predicates that express distinct represented action/state/attempt/report/cognition/intention/decision/comparison/movement/possession/question relations. "
        "Normally omit subjects and externalize retained arguments while keeping required particles/prepositions/complements, reflexives, negation, modality, and posture. "
        "Reject every-verb-token behavior, auxiliaries with no relation, ordinary speech/report scaffolds, meta-discourse carriers, head fragments, and clause-sized proposition wrappers."
    ),
    "LOCATOR": (
        "Retain ORIENTATION_KERNEL constructions that distinctly position/contextualize a coordinate or frame by space, containment, path, origin/destination, direction, proximity, accompaniment, recurrence, procedure/relation, mental/internal frame, temporal position, or figurative/comparative orientation. "
        "Use the smallest complete span. Reject preposition/adverb/recipient/topic/duration/deixis/comparison census and duplicate projections."
    ),
})
