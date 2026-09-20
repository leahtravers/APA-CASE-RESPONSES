"""V124 neutral worker rules: source-anchored coordinate entitlement plus separate support reconstruction.

No archetype answers, expected counts, evaluator findings, prior scored outputs,
canonical gold extracts, case-specific corrections/examples, or holdout material are included.
"""
from researcher_inventory.inventory_apparatus import BASE_RULES as APPARATUS_BASE_RULES, CLASS_RULES as APPARATUS_CLASS_RULES

V124_CORRECTION = r'''
V124 PROSPECTIVE CORRECTION — SOURCE-ANCHORED COORDINATE ENTITLEMENT; RECONSTRUCT UNNAMED SUPPORT SEPARATELY.

READ THE WHOLE SOURCE FIRST. Resolve obvious coreference and notice changes in represented setting, period, participants, remembered/reported material, prospect, question, correction, and present reflection. Do not emit private reasoning.

PASS A — EXPLICIT COORDINATES. First identify only exact source-native units that the source itself makes independently researcher-selectable as a human/social participant, thing/content handle, target-bearing characterization/state/status/evaluation, operative action/state/relation kernel, orientation/path/containment/direction/context relation, explicit spatial support, or explicit temporal period/support.

Literal wording alone is not entitlement. Grammar alone is not entitlement. Reject narration/discourse scaffolding, generic pronouns/deictics, proposition/question shells, rhetorical color, detached intensifiers, and subordinate wording that has no independently represented job. Do not suppress a legitimate coordinate because it is local, one-use, mundane, colloquial, uncertain, negated, remembered, reported, prospective, figurative, idiomatic, or peripheral.

EXACT NUCLEUS / EDITORIAL GRAIN. Use the smallest complete exact source-native unit that performs the coordinate job without losing represented meaning. Keep together phrasal relations, particles, reflexives, needed complements, negation, modality, comparison, idiom, and orientation constructions when splitting changes the job. Do not inflate a unit into a whole clause/proposition/question shell when a smaller exact nucleus performs the role. Every non-null source_wording/source_cue/order_cue must be character-for-character source text. Never normalize, polish, translate, diagnose, euphemize, synonymize, or lemmatize into another surface form.

PASS B — UNNAMED SUPPORT. Only after explicit coordinates, reconstruct unnamed PLACE/TIME support. Create an unnamed support only when: (1) the source materially differentiates a represented setting/period from another; (2) that support is needed to locate a distinct represented participant/relation/thing configuration; (3) no explicit PLACE/TIME already supplies it; (4) an exact source cue anchors it; and (5) the support can be described mechanically without inventing where/when. Use null source_wording, exact source cue, and neutral mechanical short tag.

An action, question, choice, intention, proposition, remembered content, or rhetorical span is NOT itself TIME just because it marks an event/discourse segment. It can imply unnamed temporal support only if the source differentiates a period needed to situate a represented configuration. A physical thing, destination phrase, spatial image, or orientation phrase is NOT itself PLACE merely because it sounds spatial. Present telling/reflection support qualifies only when the source establishes a current frame distinct from represented past/prospective material.

TYPE BY REPRESENTED JOB, NOT SURFACE SHAPE:
- spatial support -> PLACE
- temporal period/support -> TIME
- represented human/social actor or stable group -> PERSON
- independently represented thing/content handle -> OBJECT
- target-bearing characterization/state/status/evaluation -> LABEL
- operative action/state/relation kernel -> VERB
- orientation/path/containment/direction/context relation -> LOCATOR
Cross-class duplication is lawful only when the source establishes two independently selectable jobs.

PLACE: return spatial support, explicit or lawfully reconstructed unnamed support. PLACE answers where a represented configuration is situated. Broad and contained supports can both qualify if distinguished. Do not turn every physical noun, destination, comparison, or locator phrase into PLACE.

TIME: return temporal period/support, explicit or lawfully reconstructed unnamed support. TIME answers which differentiated represented period a configuration occupies; it is not a clause/event census. Explicit temporal wording qualifies only when it functions as the period/support itself; otherwise it may orient another frame or have no separate primitive.

PERSON: return speaker plus each distinct represented human/social actor or stable group after true coreference when participant, endpoint, possessor/beneficiary, remembered/reported, institutional, prospective, peripheral, or one-use. Reject rhetorical/generic/nonreferential person wording.

OBJECT: return concrete/abstract thing or content handles that are independently referable endpoints/nodes. This may include source-distinguished parts, amounts/values, services/results, choices/decisions treated as things, internal content/mental handles, named sets/categories, remembered/reported content, and figurative/quoted content when treated as content. A physical detail qualifies when the source separately acts on, checks, locates, compares, possesses, moves, refers to, or reasons about it as its own endpoint. Reject scenic furniture merely mentioned inside a larger description, generic noun phrases, bare pronouns/deictics, proposition/question shells, and nominalized actions without an independent thing/content job.

LABEL: return exact target-bearing characterization/state/status/evaluation events made independently selectable by the source. One-use, uncertain, questioned, negated, corrected, rejected, comparative, colloquial, idiomatic, and figurative forms may qualify. Require a represented target/state. Prefer the complete natural characterization phrase over a detached adjective where the phrase is what is applied. Reject decorative description, generic manner, detached intensity, and wording with no independent predication job.

VERB: return exact operative relation kernels that independently connect/position represented coordinates or establish a material relation/state. Use the smallest complete natural predicate nucleus and preserve particles, required complements, reflexives, negation, modality when needed for identity. Do not emit every lexical verb. Reject auxiliaries/support verbs, discourse/report/question shells whose content is carried elsewhere, duplicate restatements, whole-clause wrappers, and fragments nested inside a stronger relation kernel.

LOCATOR: return exact source-native orientation/context relations that independently position/orient represented coordinates: position, path, direction, containment, proximity, entry/exit, origin/destination, accompaniment, recurrence/context, internal/relational orientation, or materially spatialized figurative orientation. Prefer complete orientation phrase over a bare deictic. Reject recipient/topic/purpose/possession/degree complements, generic adverbials, isolated here/there/now with no independent orientation job, and every-preposition behavior.

PRIMITIVE ENTITLEMENT AUDIT BEFORE COMPOUNDS. For each emitted primitive ask: what exact represented job makes it standalone, what exact source nucleus or lawful support cue entitles it, is the grain the smallest complete natural unit, is it distinct after coreference/restatement, and is type based on source use rather than lexical appearance? Then replay the source for omitted actors/endpoints, separately handled things/content/parts/internal handles, target-bearing characterizations/states, operative relations, orientation relations, and materially differentiated spatial/temporal supports. Restore entitled local/one-use coordinates; remove candidates justified only by surface addressability, sentence structure, vividness, or completion of an abstract scene template. Freeze primitives.

COMPOUNDS AFTER FREEZE ONLY. A compound is one selective source-local material binding among two or more frozen primitive refs. Include only actual participating coordinates and only support/orientation needed to distinguish or materially situate the binding. Split when actor set, target/content, source posture, support frame, or independently represented relation changes. Do not create compounds to justify primitives, one-per-clause/verb/sentence, arbitrary co-occurrence, all-pairs, support chains, scene mega-bundles, singleton equivalents, duplicate restatements, alternate subset/superset decompositions, or graph closure.

qualities_available is only a yes/no flag that source qualities/descriptions exist. It does not replace LABEL and does not authorize deeper APA analysis.

Never expose approved archetypes, canonical gold extracts, expected counts, evaluator findings, scored prior outputs, calibration answers, case-specific hidden corrections/examples, sealed holdout source, or holdout output. Never perform promotion, Oval Office admission, APA-ID creation, sovereign/admitted writing, APA scoring, psychological interpretation, or APA database mutation.
'''.strip()

V124_BASE_RULES = APPARATUS_BASE_RULES + "\n\n" + V124_CORRECTION
V124_CLASS_RULES = dict(APPARATUS_CLASS_RULES)
V124_CLASS_RULES.update({
    "PLACE": "Return spatial SUPPORT coordinates only: explicit setting units plus lawfully reconstructed unnamed supports when the source differentiates a setting needed to locate a distinct represented configuration. Use null source_wording and exact cue for unnamed support. Physical things, destinations, comparisons, and orientation phrases are not PLACE merely because spatial.",
    "TIME": "Return temporal PERIOD/SUPPORT coordinates only: explicit period/support units plus lawfully reconstructed unnamed periods when source structure differentiates a period needed to locate a represented configuration. Do not turn actions, questions, choices, propositions, or discourse segments into TIME merely because they happen or delimit an episode.",
    "PERSON": "Return speaker plus every distinct represented human/social actor or stable group after true coreference when it functions as participant, endpoint, possessor/beneficiary, remembered/reported, institutional, prospective, peripheral, or one-use actor. Reject generic/rhetorical/nonreferential person wording.",
    "OBJECT": "Return independently referable THING/CONTENT endpoints/nodes at exact source grain, including source-distinguished parts, amounts, choices/decisions as things, internal/mental handles, sets/categories, and remembered/reported/figurative content when treated as content. A physical detail qualifies when separately acted on, checked, located, compared, possessed, moved, referred to, or reasoned about. Reject scenic furniture and proposition/question shells.",
    "LABEL": "Return exact TARGET-BEARING characterization/state/status/evaluation coordinates. Require a represented target/state; keep the complete natural characterization phrase. One-use, uncertain, questioned, negated, corrected, rejected, colloquial, idiomatic, and figurative labels may qualify. Reject decorative/generic description and detached intensity with no independent predication job.",
    "VERB": "Return exact OPERATIVE RELATION kernels at the smallest complete natural predicate grain. Preserve particles/complements/reflexives/negation/modality needed for identity. Do not emit every lexical verb; reject auxiliaries, discourse/report/question shells, duplicate restatements, whole-clause wrappers, and fragments inside stronger relations.",
    "LOCATOR": "Return exact ORIENTATION/CONTEXT relations that independently position or orient represented coordinates. Prefer complete orientation phrase over bare deictic. Reject generic adverbials, recipient/topic/purpose/possession/degree complements, isolated here/there/now without independent orientation job, and every-preposition behavior.",
})
