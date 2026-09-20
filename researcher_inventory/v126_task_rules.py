"""V126 neutral worker rules: source-local frames first, then editor-coordinate admission.

No archetype answers, expected counts, evaluator findings, prior scored outputs,
canonical gold extracts, case-specific corrections/examples, or holdout material are included.
"""
from researcher_inventory.inventory_apparatus import BASE_RULES as APPARATUS_BASE_RULES, CLASS_RULES as APPARATUS_CLASS_RULES

V126_CORRECTION = r'''
V126 PROSPECTIVE CORRECTION — FRAME FIRST, EDITOR COORDINATES SECOND.

READ THE WHOLE SOURCE FIRST. Resolve obvious coreference and internally distinguish source-local represented frames/configurations. A frame can change when participant set, operative relation, target/content, represented posture, where-support, or when-support changes. A frame is not automatically one sentence, clause, paragraph, or discourse turn. Do not emit this internal map or private reasoning.

SUPPORT BEFORE FINAL ADMISSION. For each frame determine the PLACE/TIME support needed to keep its bindings correctly situated. Create unnamed PLACE/TIME only when the source differentiates the where/when frame, a binding would otherwise be mislocated or conflated, no explicit support already suffices, an exact source cue anchors it, and a mechanical tag can describe it without invention. Local, one-use, remembered, reported, prospective, and present-reflection support may qualify. Explicit spatial/temporal wording is evidence, not automatic PLACE/TIME entitlement.

PRIMITIVE ADMISSION = DISTINCT BINDING ROLE. After the frame/support map is stable, admit an explicit source-native nucleus only when it occupies a distinct role in at least one source-local binding: human/social participant or endpoint; independently handled thing/content endpoint; target-bearing characterization/state/status/evaluation; operative action/state/relation kernel; orientation/path/containment/direction/context relation; spatial support; or temporal support.

Represented meaning alone is NOT enough. Mention alone is NOT enough. Grammatical independence alone is NOT enough. Use this removal test: if the candidate disappeared as an independent coordinate, would a distinct source-established participant, endpoint/content handle, state/evaluation, relation, orientation, or support distinction in at least one binding be lost? If no, omit it. If uncertain, do not preserve by default; rerun the removal test against the local binding.

Minor, ordinary, one-use, colloquial, idiomatic, uncertain, negated, remembered, reported, prospective, figurative, or peripheral wording can qualify when it passes the binding-role test.

EDITORIAL GRAIN. Use the smallest complete exact source-native unit that performs the admitted role without changing it. Preserve particles, reflexives, required complements, negation, modality, comparison, idiom, and orientation constructions when needed for identity. Do not inflate to proposition/question shells; do not shrink until relation, target, polarity, orientation, or idiomatic meaning changes. Every non-null source_wording/source_cue/order_cue must be character-for-character source text. Never normalize, polish, translate, diagnose, euphemize, synonymize, regularize grammar, or lemmatize into another surface form.

TYPE BY BINDING ROLE, NOT SURFACE SHAPE:
- spatial support -> PLACE
- temporal period/support -> TIME
- represented human/social actor or stable group -> PERSON
- independently represented thing/content handle -> OBJECT
- target-bearing characterization/state/status/evaluation -> LABEL
- operative action/state/relation kernel -> VERB
- orientation/path/containment/direction/context relation -> LOCATOR
Grammar, concreteness, and spatial/temporal imagery are evidence, not authority. A noun-shaped phrase may be LABEL or OBJECT rather than PLACE. Spatial wording may be OBJECT/content or LOCATOR rather than PLACE. A verbal phrase may be OBJECT/content or LABEL. Cross-class duplication is lawful only when the source establishes two distinct coordinate jobs.

PLACE: return only explicit or lawfully reconstructed spatial supports that answer where a represented binding is situated. Broad/contained, local, and unnamed supports may qualify when source-differentiated. Do not turn scenic physical nouns, destinations, comparisons, orientation phrases, or spatial images into PLACE unless they perform the support role.

TIME: return only explicit or lawfully reconstructed temporal supports that answer which differentiated represented period a binding occupies. Local event periods, remembered/reported periods, prospective periods, and source-established present reflection may qualify. Do not turn event clauses, actions, questions, discourse segments, durations, or time adverbs into TIME unless they perform the support role.

PERSON: return speaker plus each distinct represented human/social actor or stable group after true coreference when the actor is a participant, endpoint, possessor/beneficiary with independent role, remembered/reported actor, institutional actor, prospective actor, peripheral actor, or one-use actor in at least one binding. Reject generic/rhetorical/nonreferential person wording.

OBJECT: return concrete/abstract thing or content handles that function as independently represented endpoints/nodes in at least one binding. This can include source-distinguished parts, values, services/results, choices/decisions as things, internal content, named sets/categories, remembered/reported content, and figurative/quoted content when handled as content. A physical detail is not admitted merely because it is visible; it qualifies when separately acted on, checked, located, compared, possessed, moved, referred to, reasoned about, or otherwise used as an independent endpoint. Reject scenic furniture, generic noun phrases, bare pronouns/deictics, and nominalized actions with no independent endpoint/content job.

LABEL: return exact target-bearing characterization/state/status/evaluation coordinates. One-use, uncertain, questioned, negated, corrected, rejected, comparative, colloquial, idiomatic, and figurative labels may qualify. Use the smallest complete source phrase that preserves the actual state, target, polarity, comparison, or evaluation. Do not wrap a label in an entire proposition when a shorter exact nucleus carries the predication. Distinct source-local evaluation/polarity turns may remain distinct when each is independently predicated. Reject decorative description, generic manner, detached intensity, and wording with no target-bearing state/evaluation role.

VERB: return exact operative action/state/relation kernels that organize at least one admitted binding. Preserve required particles, complements, reflexives, negation, modality, comparison, or idiomatic structure. Common, grammatically light, copular, positional, speech, asking, perceptual, cognitive, possessive, or relational wording may qualify when it actually links selected coordinates in a distinct binding. Reject auxiliaries with no distinct relation, discourse-management shells, true duplicate restatements, whole-clause wrappers, and lexical verbs whose removal would not erase a selected binding relation.

LOCATOR: return exact source-native orientation/context relations that independently position or orient coordinates in at least one binding: position, path, direction, containment, proximity, entry/exit, origin/destination, accompaniment, recurrence/context, internal/relational orientation, or spatialized figurative orientation. Local, one-use, colloquial, idiomatic, and figurative orientation may qualify. Prefer the complete natural orientation phrase. Reject every-preposition behavior, non-orienting recipient/topic/purpose/possession/degree complements, and generic adverbials with no binding-orientation role.

FRAME-ROLE AUDIT BEFORE FREEZE. Replay the source frame by frame. For every binding, check actor/endpoints, independent thing/content, target-bearing state/evaluation, operative relation, orientation, spatial support, and temporal support. For every explicit primitive ask which exact binding uses it, what distinct role it performs, whether removing it erases that role rather than descriptive wording, whether its grain is the smallest complete natural unit, and whether its class comes from binding role rather than grammar. For every unnamed support identify the binding that would be mislocated or conflated without it. Remove anything that cannot answer these questions; restore any missing role/support. Then freeze primitives.

COMPOUNDS BIND THE FRAMES ALREADY IDENTIFIED. Build one selective source-local compound for each distinct represented binding that needs a compound. Include all and only frozen participating actors/endpoints, operative relation, target/content/object, target-bearing label/state, orientation relation, and PLACE/TIME support when it situates that binding. Split when actor set, target/content, operative relation, source posture, or support frame changes materially. Questions, choices, reports, memories, comparisons, and reflections can organize a binding without forcing their whole proposition to be primitive.

Do not create compounds to justify primitives. Do not create one-per-sentence/clause/verb/primitive/support, arbitrary co-occurrence, all-pairs links, scene mega-bundles, support chains, singleton equivalents, duplicate restatements, alternate subset/superset decompositions, or graph closure.

FINAL ANTI-OVERGENERATION AUDIT. Every explicit primitive must point to at least one distinct binding role. Every unnamed support must prevent a real source-established where/when collapse. Every compound must represent one coherent local binding. No coordinate survives merely because its wording is represented, vivid, grammatical, spatial, temporal, nominal, adjectival, verbal, prepositional, or potentially useful. The correct inventory is the smallest complete editorial coordinate system that preserves all distinct source-local bindings and necessary supports.

qualities_available is only a yes/no flag that source qualities/descriptions exist. It does not replace LABEL and does not authorize deeper APA analysis.

Never expose approved archetypes, canonical gold extracts, expected counts, evaluator findings, scored prior outputs, calibration answers, case-specific hidden corrections/examples, sealed holdout source, or holdout output. Never perform promotion, Oval Office admission, APA-ID creation, sovereign/admitted writing, APA scoring, psychological interpretation, or APA database mutation.
'''.strip()

V126_BASE_RULES = APPARATUS_BASE_RULES + "\n\n" + V126_CORRECTION
V126_CLASS_RULES = dict(APPARATUS_CLASS_RULES)
V126_CLASS_RULES.update({
    "PLACE": "Return only source-established SPATIAL SUPPORT coordinates for represented bindings. Explicit wording or unnamed local support may qualify when it actually situates a binding; scenic physical nouns and spatial imagery do not qualify merely by being spatial.",
    "TIME": "Return only source-established TEMPORAL SUPPORT coordinates for represented bindings. Local, remembered/reported, prospective, or present-reflection periods may qualify; event/action/question/discourse wording is not TIME unless it performs the support role.",
    "PERSON": "Return speaker plus every distinct human/social actor or stable group that occupies an independent participant/endpoint role in at least one binding after true coreference. Reject generic/rhetorical/nonreferential person wording.",
    "OBJECT": "Return independently handled THING/CONTENT endpoints used in at least one binding. Mention or physical presence is insufficient; the source must act on, locate, compare, possess, reason about, refer to, or otherwise use the item/content as its own endpoint.",
    "LABEL": "Return the smallest complete exact TARGET-BEARING characterization/state/status/evaluation nucleus used in a binding. Preserve polarity, uncertainty, correction, comparison, idiom, and colloquial grain; reject decorative or proposition-shell wording with no independent predication role.",
    "VERB": "Return the smallest complete exact OPERATIVE relation kernel that actually organizes a selected binding. Common/copular/positional/speech/asking/cognitive relations may qualify; reject discourse shells, auxiliaries without distinct relation, and lexical verbs with no independent binding job.",
    "LOCATOR": "Return exact ORIENTATION/CONTEXT relations that independently position or orient a selected binding. Local, idiomatic, figurative, and one-use orientations may qualify; reject generic complements/adverbials and every-preposition behavior.",
})
