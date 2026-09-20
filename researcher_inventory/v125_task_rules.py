"""V125 neutral worker rules: coverage before pruning, then source-job typing and source-local binding.

No archetype answers, expected counts, evaluator findings, prior scored outputs,
canonical gold extracts, case-specific corrections/examples, or holdout material are included.
"""
from researcher_inventory.inventory_apparatus import BASE_RULES as APPARATUS_BASE_RULES, CLASS_RULES as APPARATUS_CLASS_RULES

V125_CORRECTION = r'''
V125 PROSPECTIVE CORRECTION — COVER SOURCE COORDINATES BEFORE ANTI-CENSUS PRUNING.

READ THE WHOLE SOURCE FIRST. Resolve obvious coreference and notice changes in represented setting, period, participants, remembered/reported material, prospect, question, correction, comparison, uncertainty, and present reflection. Do not emit private reasoning.

PASS A — COVERAGE FIRST. Replay the source in order and provisionally mark every exact source-native nucleus that performs a represented researcher-coordinate job: human/social participant; thing/content handle; target-bearing characterization/state/status/evaluation; operative action/state/relation kernel; orientation/path/containment/direction/context relation; explicit spatial support; or explicit temporal period/support.

Do NOT prune in Pass A because a candidate is minor, ordinary, one-use, local, obvious, grammatical, colloquial, uncertain, negated, remembered, reported, prospective, figurative, idiomatic, peripheral, or insufficiently important. Common or grammatically light wording is not automatically scaffolding. The Pass-A question is whether the exact source nucleus performs a represented coordinate job a researcher could stably point back to without inventing language or meaning.

PASS B — PRUNE NARROWLY. After coverage is complete, remove only: pure narration/discourse management with no represented relation/content handle of its own; auxiliary/support morphology with no distinct represented relation beyond a stronger natural predicate nucleus; generic/nonreferential pronoun or deictic wording with no stable endpoint/orientation; proposition/question shells whose content is fully carried elsewhere and which are not themselves treated as content; detached intensity/filler/rhetorical color with no target-bearing state/evaluation or orientation job; true duplicate/restatement of the same class-local identity after coreference; fragments nested inside a stronger natural nucleus; or wording with no represented coordinate role that would exist only to make a token/phrase/clause census.

When uncertain between keeping and pruning, preserve a candidate if the source gives it a distinct represented job or another selected coordinate depends on it. Importance, recurrence, centrality, polish, and formal naming are NOT admission requirements.

EXACT NUCLEUS / EDITORIAL GRAIN. Use the smallest complete exact source-native unit that performs the represented job without changing it. Preserve phrasal relations, particles, reflexives, required complements, negation, modality, comparison, idiom, and orientation constructions when needed for identity. Do not inflate to whole clauses/propositions/question shells; do not shrink until relation, target, polarity, orientation, or idiomatic meaning changes. Every non-null source_wording/source_cue/order_cue must be character-for-character source text. Never normalize, polish, translate, diagnose, euphemize, synonymize, regularize grammar, or lemmatize into another surface form.

PASS C — UNNAMED PLACE/TIME SUPPORT. After explicit coverage and pruning, reconstruct unnamed support when: (1) the source differentiates a represented where-frame or when-frame from another; (2) at least one surviving coordinate/binding would otherwise be mislocated, conflated, or lose a source-established distinction; (3) no explicit PLACE/TIME already supplies the support; (4) an exact source cue anchors it; and (5) a mechanical short tag can describe it without inventing where/when. The support may be local, one-use, ordinary, remembered, reported, prospective, or the present telling/reflection frame. Use null source_wording, exact source cue, and neutral mechanical short tag.

An action, question, decision, intention, proposition, remembered content, or rhetorical span is NOT itself TIME just because it happens or marks discourse. It may establish an unnamed period when the source differentiates that period. A concrete thing, destination phrase, spatial image, or orientation phrase is NOT itself PLACE merely because spatial; it may be another class while helping establish a support. Two supports remain distinct when merging them would put surviving coordinates in the wrong source-established where/when frame.

TYPE BY REPRESENTED JOB, NOT SURFACE SHAPE:
- spatial support -> PLACE
- temporal period/support -> TIME
- represented human/social actor or stable group -> PERSON
- independently represented thing/content handle -> OBJECT
- target-bearing characterization/state/status/evaluation -> LABEL
- operative action/state/relation kernel -> VERB
- orientation/path/containment/direction/context relation -> LOCATOR
Grammar is evidence, not authority. Cross-class duplication is lawful only when the source establishes two distinct represented coordinate jobs.

PLACE: return explicit or lawfully reconstructed spatial supports that answer where a represented configuration is situated. Broad and contained supports may both qualify when distinguished. Local and unnamed supports may qualify. Do not turn every physical noun, destination, comparison, orientation phrase, or spatial image into PLACE.

TIME: return explicit or lawfully reconstructed temporal periods/supports that answer which differentiated represented period a configuration occupies. Local episode periods, remembered/reported periods, prospective periods, and a source-established present reflective frame may qualify. Do not turn every event clause, action, question, or discourse segment into TIME.

PERSON: return speaker plus each distinct represented human/social actor or stable group after true coreference when participant, endpoint, possessor/beneficiary, remembered/reported, institutional, prospective, peripheral, or one-use. Reject rhetorical/generic/nonreferential person wording.

OBJECT: return concrete/abstract thing or content handles that function as independently represented endpoints/nodes, including source-distinguished parts, amounts/values, services/results, choices/decisions as things, internal/mental handles, named sets/categories, remembered/reported content, and figurative/quoted content when referred to as content. A physical detail qualifies when separately acted on, checked, located, compared, possessed, moved, referred to, reasoned about, or used as an endpoint. Reject scenic furniture with no own represented role, generic noun phrases, bare pronouns/deictics, and nominalized actions with no independent thing/content job.

LABEL: return exact target-bearing characterization/state/status/evaluation coordinates. One-use, uncertain, questioned, negated, corrected, rejected, comparative, colloquial, idiomatic, and figurative labels may qualify. Preserve the complete natural characterization phrase. Require a represented target/state. Reject decorative description, generic manner, detached intensity, and wording with no represented predication/evaluation job.

VERB: return exact operative action/state/relation kernels that connect or position represented coordinates or establish a represented state. Preserve particles, required complements, reflexives, negation, modality, comparison, or idiomatic structure when needed for identity. Do not emit every lexical verb, but do not reject a valid relation merely because it is common, grammatically light, perceptual, cognitive, positional, copular, possessive, or ordinary. Reject only auxiliaries/support morphology with no distinct relation, discourse shells whose content is carried elsewhere, true duplicate restatements, whole-clause wrappers, and fragments inside a stronger natural kernel.

LOCATOR: return exact source-native orientation/context relations that independently position or orient represented coordinates: position, path, direction, containment, proximity, entry/exit, origin/destination, accompaniment, recurrence/context, internal/relational orientation, or spatialized figurative orientation. Local, colloquial, idiomatic, and one-use orientations may qualify. Prefer complete natural orientation phrase over bare deictic. Reject recipient/topic/purpose/possession/degree complements, generic adverbials with no orientation job, and every-preposition behavior.

COVERAGE AUDIT BEFORE FREEZE. Replay the source in order for omitted actors/endpoints; separately handled things/content/parts/values/choices/internal handles; target-bearing characterizations/states; operative relations; orientation relations; differentiated spatial supports; differentiated temporal supports. Restore a candidate whenever it has a distinct represented job, even if minor or one-use. Remove it only when the anti-census exclusions actually apply. Then freeze primitives.

COMPOUNDS AFTER FREEZE ONLY. A compound is one selective source-local binding among two or more frozen primitive refs. Build it when the source represents one local relation, characterization, question, choice, report, remembered/reported event, comparison, or reflection whose participating frozen coordinates form one coherent binding. Include all and only actual participating actors/endpoints, relation, target/content/object, target-bearing label/state, orientation relation, and PLACE/TIME support when that support actually situates the binding. Do not omit participating support/orientation merely because it feels redundant; do not add unrelated nearby scene context. Split when actor set, target/content, source posture, support frame, or independently represented relation changes. Do not create one-per-sentence/clause/verb/primitive/support, arbitrary co-occurrence, all-pairs links, scene mega-bundles, support chains, singleton equivalents, duplicate restatements, alternate subset/superset decompositions, or graph closure.

qualities_available is only a yes/no flag that source qualities/descriptions exist. It does not replace LABEL and does not authorize deeper APA analysis.

Never expose approved archetypes, canonical gold extracts, expected counts, evaluator findings, scored prior outputs, calibration answers, case-specific hidden corrections/examples, sealed holdout source, or holdout output. Never perform promotion, Oval Office admission, APA-ID creation, sovereign/admitted writing, APA scoring, psychological interpretation, or APA database mutation.
'''.strip()

V125_BASE_RULES = APPARATUS_BASE_RULES + "\n\n" + V125_CORRECTION
V125_CLASS_RULES = dict(APPARATUS_CLASS_RULES)
V125_CLASS_RULES.update({
    "PLACE": "Return explicit or lawfully reconstructed SPATIAL SUPPORT coordinates that situate surviving represented material. Local/one-use unnamed supports may qualify when source-differentiated and exactly cued. Do not convert every physical noun, destination, comparison, orientation phrase, or spatial image into PLACE.",
    "TIME": "Return explicit or lawfully reconstructed TEMPORAL PERIOD/SUPPORT coordinates that distinguish represented when-frames. Local episode, remembered/reported, prospective, and source-established present-reflection periods may qualify. Do not convert event/action/question/discourse spans themselves into TIME merely because they occur.",
    "PERSON": "Return speaker plus every distinct represented human/social actor or stable group after true coreference when participant, endpoint, possessor/beneficiary, remembered/reported, institutional, prospective, peripheral, or one-use. Reject generic/rhetorical/nonreferential person wording.",
    "OBJECT": "Return independently represented THING/CONTENT endpoints at exact source grain, including source-distinguished parts, values, choices as things, internal handles, sets/categories, and remembered/reported/figurative content when treated as content. Preserve mundane/one-use endpoints; reject scenic furniture with no own represented role and shells with no content-handle job.",
    "LABEL": "Return exact TARGET-BEARING characterization/state/status/evaluation coordinates. Preserve complete source-native characterization phrases, including uncertain, negated, corrected, colloquial, idiomatic, figurative, peripheral, or one-use forms. Reject only wording with no represented predication/evaluation job.",
    "VERB": "Return exact OPERATIVE action/state/relation kernels at the smallest complete source-native grain. Common or grammatically light relations may qualify when they actually connect/position represented coordinates. Preserve needed particles/complements/polarity/modality. Reject auxiliaries with no distinct relation, discourse shells, true duplicates, and fragments nested in stronger kernels.",
    "LOCATOR": "Return exact ORIENTATION/CONTEXT relations that independently position or orient represented coordinates. Local, colloquial, idiomatic, figurative-spatialized, and one-use orientations may qualify. Prefer complete natural orientation phrases; reject generic adverbials with no orientation job, non-orienting complements, and every-preposition behavior.",
})
