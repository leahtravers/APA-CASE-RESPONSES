"""V122 neutral worker rules: material-binding editorial resolution.

No archetype answers, expected counts, evaluator findings, prior scored outputs,
canonical gold extracts, calibration answers, or holdout material are included here.
"""
from researcher_inventory.inventory_apparatus import BASE_RULES as APPARATUS_BASE_RULES, CLASS_RULES as APPARATUS_CLASS_RULES

V122_CORRECTION = r'''
V122 PROSPECTIVE CORRECTION — MATERIAL-BINDING-CAPABLE RESEARCHER COORDINATES AT SOURCE-NATIVE EDITORIAL GRAIN.

READ THE WHOLE SOURCE FIRST. Before answering any requested class, privately map the materially distinct represented bindings/situations across the complete source together with their spatial supports, temporal episode/support frames, participants/endpoints, thing/content handles, applied characterizations, operative relation kernels, and orientation/context relations. Do not emit this private map.

THE INVENTORY IS NEITHER A SPARSE SUMMARY NOR A SURFACE-SPAN CENSUS. A primitive is admitted when the source itself establishes it as one independently useful researcher coordinate that can occupy a coherent role in the represented binding/support map. Binding-capable does NOT mean every primitive must appear in a final compound. Legitimate standalone coordinates remain valid.

DO NOT require recurrence, persistence, global salience, narrative centrality, entity-like identity, or compound indispensability. Local, one-use, mundane, remembered, reported, uncertain, negated, questioned, hypothetical, prospective, figurative, idiomatic, and colloquial coordinates may qualify when they perform an independently useful source-established role.

REJECT a candidate whose only entitlement is that its words are literal, grammatical, descriptive, rhetorically vivid, or pointable. Reject grammar/support scaffolding, narration/discourse management, rhetorical color, incidental description, generic scene wording, detached modifiers/intensifiers, proposition/question shells, redundant restatement, and internal fragments of a stronger source-native coordinate unless the source establishes an independent researcher-coordinate role.

EDITORIAL GRAIN: use the smallest complete source-native unit that performs the relevant coordinate job without losing represented meaning. Keep natural idioms, phrasal relations, bound complements, negated constructions, and orientation phrases whole when splitting would destroy their job. Do not inflate a coordinate into a whole clause, proposition, question shell, or rhetorical bundle when a smaller source-native nucleus carries the job.

SUPPORT FRAMES FIRST:
- PLACE: retain each materially differentiated source-established spatial support needed to situate represented bindings. Explicit or unnamed, broad or contained, remembered/reported, destination/later, object/interaction/wait support, and present-telling support may qualify when the source differentiates them. Multiple bindings may share one PLACE; multiple unnamed PLACE rows are lawful when support is materially distinct. For unnamed PLACE use null source_wording, exact source cue, neutral mechanical tag. Never invent where.
- TIME: retain each materially differentiated source-established temporal episode/support needed to situate represented bindings. Explicit or unnamed attempts/conditions, response phases, transitions, waits, intended/remembered/reported periods, later conversations/reports, recurring spans, present-reflection frames, and prospective frames may qualify. A temporal expression is not automatically TIME when it merely orients a larger episode. For unnamed TIME use null source_wording, exact source cue, neutral mechanical tag.

PERSON: retain the speaker plus every distinct source-established human/social actor or stable group after true coreference when the actor functions as participant, anchor, possessor/beneficiary, relation endpoint, remembered/reported actor, institutional actor, prospective actor, peripheral actor, or one-use actor. Reject rhetorical/generic/nonreferential person wording that never becomes a represented actor coordinate.

OBJECT: retain source-established concrete or abstract thing/content handles that function as independently usable endpoints or referential nodes in the represented map. Concrete things/parts, values, services/results, decisions/next steps treated as things, choices treated as choices, named sets/categories, remembered/reported content, and internal represented content may qualify. Reject generic noun phrases, pronouns/deictics, grammatical arguments/complements, proposition/question shells, explanations/discourse points, descriptive fragments, and nominalized actions without an independent thing/content role.

LABEL: retain distinct source-applied characterization events that perform a material role in the represented map: states, statuses, identities, evaluations, comparisons, self/candidate labels, rejections, corrections, contrasts, and materially expressed postures. LABEL is target-bearing and occurrence-bound; a valid characterization may be one-use. Preserve colloquial/idiomatic/questioned/negated/uncertain/corrected/rejected/figurative characterization when it is itself a coordinate. Reject decorative color, incidental description, generic manner wording, detached modifiers/intensifiers, and scene-setting adjectives with no independent applied-characterization role.

VERB: retain each distinct source-native operative relation kernel that performs one material relation role in the represented map. Actions, states, cognitions, perceptions, communications, intentions, decisions, possessions, comparisons, evaluations, movements, transitions, gestures, existence/location, obligations, recurrence, and other represented relations may qualify. A valid relation may be unique/one-use. Reject auxiliaries/support verbs, filler/discourse predicates, lexical verb occurrences without their own material relation role, proposition/question shells when a smaller nucleus carries the job, empty copular/reporting scaffolding, duplicates, whole-clause wrappers, rhetorical bundles, and fragments nested inside stronger relation kernels. Preserve particles/reflexives/negation/modality/bound complements when source identity requires them and preserve nonasserted posture.

LOCATOR: retain each distinct source-native orientation/context relation that performs one material role in the represented map: position, path, direction, containment, proximity, movement orientation, accompaniment, origin/destination, entry/exit, recurrence/context, internal/relational orientation, or materially spatialized figurative orientation. A valid LOCATOR may be unique/one-use. Reject every-PP/adverbial behavior, recipient/topic/purpose/possession/degree complements, generic adverbials, isolated deictics without their own orientation role, and rhetorical location wording. A spatial/temporal phrase may be LOCATOR when it orients rather than constitutes a PLACE/TIME support.

FUNCTIONAL TYPE — PRIMARY REPRESENTED JOB:
- spatial support -> PLACE
- temporal episode/support -> TIME
- represented human/social actor -> PERSON
- independently represented thing/content handle -> OBJECT
- applied characterization/state/status/evaluation/comparison/identity -> LABEL
- operative happening/action/state/relation kernel -> VERB
- orientation/path/direction/containment/proximity/context relation -> LOCATOR
Cross-class duplication is allowed only when the source genuinely establishes two independently selectable jobs, not merely because a phrase can be linguistically described several ways.

LITERAL LOCK: every non-null source_wording, source_cue, and order_cue must be character-for-character source text. Preserve colloquial language, dialect, spelling/grammar, idiom, figurative wording, negation, modality, uncertainty, question form, attribution, comparison, remembered/reported posture, hypothetical/prospective posture, correction, and rejection. Never normalize, polish, translate, diagnose, euphemize, substitute synonyms, or lemmatize into a different surface form. Researcher short tags are navigational only and must stay source-near.

PRIMITIVE FREEZE AUDIT:
1) replay the whole source in order;
2) verify every materially distinct binding has the spatial/temporal support the source actually differentiates;
3) verify PLACE/TIME/PERSON/OBJECT for source-established support/referential roles;
4) verify LABEL/VERB/LOCATOR for source-native characterization/relation/orientation roles;
5) restore legitimate local/one-use coordinates omitted only because they looked small, mundane, colloquial, uncertain, figurative, or nonpersistent;
6) remove candidates admitted only because they are literal spans, grammatical constituents, incidental descriptions, discourse/rhetorical material, redundant restatements, or proposition shells;
7) arbitrate OBJECT/LABEL/VERB/LOCATOR by primary represented job;
8) reduce relation-like units to the smallest complete natural source-native grain;
9) verify exact wording, coreference, class-local distinctness, and first-establishment order;
10) freeze primitives.
Coverage and compression are equally mandatory.

AFTER FREEZE, reconnect primitives to the private material-binding map. A valid primitive may remain unbundled. Emit a compound only when two or more frozen coordinates jointly form one source-local materially complete researcher binding. Use only participating refs, include enough for completeness without unrelated context, and split when actor set, target/content, posture, support frame, or independently represented relation changes materially. Do not create one compound per clause/verb/primitive/sentence/phrase, arbitrary co-occurrence, all-pairs links, graph closure, support chains, scene mega-bundles, duplicate restatements, alternate subset/superset decompositions, or singleton equivalents.

qualities_available is a yes/no availability flag only. Do not replace LABEL rows with Q and do not expand qualities into APA analysis.

Never expose approved archetypes, canonical gold extracts, expected counts, evaluator findings, prior scored outputs, calibration answers, sealed holdout source, or holdout output. Never perform promotion, Oval Office admission, APA-ID creation, sovereign/admitted writing, APA scoring, psychological interpretation, or APA database mutation.
'''.strip()

V122_BASE_RULES = APPARATUS_BASE_RULES + "\n\n" + V122_CORRECTION
V122_CLASS_RULES = dict(APPARATUS_CLASS_RULES)
V122_CLASS_RULES.update({
    "PLACE": "Return each materially differentiated source-established spatial SUPPORT frame needed to situate represented bindings, including legitimate unnamed and present-telling supports. Map supports across the whole source before extraction. Multiple bindings may share a support; multiple unnamed supports may qualify when materially distinct. Use null source_wording plus exact source cue for unnamed PLACE. Do not turn every physical noun, destination phrase, or locator phrase into PLACE.",
    "TIME": "Return each materially differentiated source-established temporal EPISODE/SUPPORT frame needed to situate represented bindings, including legitimate unnamed attempts/conditions, response phases, transitions, waits, remembered/reported periods, recurring spans, present reflection, and prospective frames. Do not inventory every temporal expression; explicit temporal wording may instead orient a larger episode.",
    "PERSON": "Return the speaker plus every distinct source-established human/social actor or stable group after true coreference when it functions as a participant, anchor, possessor/beneficiary, relation endpoint, remembered/reported actor, institutional actor, prospective actor, peripheral actor, or one-use actor. Reject rhetorical/generic/nonreferential person wording.",
    "OBJECT": "Return source-established concrete or abstract THING/CONTENT handles that function as independently usable endpoints or referential nodes in the represented binding map. Reject generic noun phrases, pronouns/deictics, grammatical arguments/complements, proposition/question shells, explanations/discourse points, descriptive fragments, and nominalized actions without an independent thing/content role.",
    "LABEL": "Return distinct source-applied CHARACTERIZATION EVENTS that perform an independently useful role in the represented binding map. Valid labels may be local/one-use, colloquial, uncertain, negated, corrected, rejected, or figurative. Use the smallest complete exact source form. Reject decorative color, incidental description, detached modifiers/intensifiers, and adjectives with no independent applied-characterization role.",
    "VERB": "Return each distinct source-native operative RELATION KERNEL that performs one material relation role in the represented binding map at the smallest complete natural predicate grain. One-use relations qualify. Reject auxiliaries/support verbs, filler, lexical verbs without their own material relation role, proposition/question shells, empty scaffolding, duplicates, whole-clause wrappers, rhetorical bundles, and fragments inside stronger relation kernels. Preserve source posture and bound material needed for identity.",
    "LOCATOR": "Return each distinct source-native ORIENTATION/CONTEXT RELATION that performs one material role in the represented binding map at the smallest complete literal grain. One-use orientations qualify. Reject every-preposition/adverbial behavior, recipient/topic/purpose/possession/degree complements, generic adverbials, isolated deictics without an orientation role, and rhetorical location wording. Spatial/temporal phrases may be LOCATOR when they orient rather than constitute a support frame.",
})
