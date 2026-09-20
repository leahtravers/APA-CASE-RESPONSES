"""V123 neutral worker rules: episode-ledger constrained admission and source-use typing.

No archetype answers, expected counts, evaluator findings, prior scored outputs,
canonical gold extracts, calibration answers, or holdout material are included here.
"""
from researcher_inventory.inventory_apparatus import BASE_RULES as APPARATUS_BASE_RULES, CLASS_RULES as APPARATUS_CLASS_RULES

V123_CORRECTION = r'''
V123 PROSPECTIVE CORRECTION — MATERIAL EPISODE LEDGER FIRST; SOURCE-USE ROLE CONTROLS ADMISSION AND TYPE.

READ THE WHOLE SOURCE FIRST. Before answering any requested class, privately build a MATERIAL EPISODE LEDGER. Segment represented episodes by source-established changes in spatial support, temporal phase, participant configuration, material relation cluster, memory/report posture, intention/choice/prospect, uncertainty/question/correction/rejection, reflection, present-telling, or another materially different represented frame. Do not segment by sentence or clause merely because punctuation changes. Do not emit this private ledger.

For each private episode row, fill only roles the source actually establishes: spatial support; temporal support; participants/endpoints; thing/content handles; applied characterizations/states; operative relation kernels; orientation/context relations; and posture needed to preserve whether material is remembered, reported, questioned, negated, uncertain, intended, hypothetical, prospective, corrected, or rejected.

LEDGER-CONSTRAINED ADMISSION: a primitive is admitted only when it is one source-native value filling one distinct role in that private episode ledger. A valid value may be local, one-use, mundane, colloquial, uncertain, negated, remembered, reported, hypothetical, prospective, figurative, idiomatic, or peripheral. Do not require recurrence, persistence, global salience, or compound indispensability. But literal addressability is never enough. Reject grammar/support scaffolding, narration/discourse management, rhetorical color, isolated intensification, generic scene detail, incidental description, and subordinate lexical furniture that does not occupy its own researcher-selectable ledger role.

MATERIAL PARTICIPATION: the admitted role must participate in, support, characterize, orient, or provide a participant/endpoint/content handle for something materially represented in an episode. Do not admit a span merely because it is a noun, lexical verb, adjective, prepositional phrase, temporal expression, vivid phrase, or concrete detail.

SOURCE-USE ROLE CONTROLS TYPE. Never classify from what the words appear to denote in isolation. First ask what job the source is making that exact unit perform here:
- spatial support -> PLACE
- temporal episode/support -> TIME
- human/social participant or stable group -> PERSON
- thing/content handle treated as an endpoint/node of represented relations -> OBJECT
- target-bearing characterization/state/status/evaluation/comparison/identity/correction/rejection -> LABEL
- operative action/state/relation kernel -> VERB
- orientation/path/direction/containment/proximity/context relation -> LOCATOR
A spatial-sounding phrase is not PLACE if the source uses it as content/thing. A noun-like phrase is not OBJECT if it is applied as a characterization. An adjective-like phrase is not LABEL if the source treats it as content. A verbal surface form is not VERB if it is only a shell or content handle. A temporal expression is not TIME if it merely orients a larger episode. Cross-class duplication is lawful only when the source establishes two independently selectable represented jobs.

EDITORIAL GRAIN: use the smallest complete source-native unit that performs the ledger role without losing represented meaning. Keep idioms, phrasal relations, negation, modality, reflexives, bound complements, comparisons, and orientation constructions whole when splitting would destroy their job. Do not inflate a coordinate into a whole clause, proposition, question shell, or rhetorical bundle when a smaller natural nucleus performs the role.

SUPPORT FRAMES ARE DERIVED FROM EPISODES, NOT FROM PLACE/TIME WORDS:
- PLACE: retain every materially differentiated source-established spatial support needed by the private episode ledger. Supports may be explicit or unnamed, broad or contained, direct or remembered/reported, destination/later, interaction/wait specific, or present-telling. Multiple bindings may share one PLACE; multiple unnamed PLACE rows are required when materially distinct spatial supports exist. For unnamed PLACE use null source_wording, exact source cue, neutral mechanical tag. Never invent where. Do not turn every physical noun, spatial phrase, or scenic reference into PLACE.
- TIME: retain every materially differentiated source-established temporal episode/support. Supports may be explicit or unnamed, including attempt/condition, response, transition, wait, intended period, remembered/reported period, later conversation/report, recurring span, present reflection, and prospect. Multiple relations may share one TIME when the episode is the same; open distinct unnamed TIME rows when source structure differentiates the episode. For unnamed TIME use null source_wording, exact source cue, neutral mechanical tag. Do not inventory temporal expressions simply because they mention time.

PERSON: retain the speaker plus every distinct source-established human/social actor or stable group after true coreference when the actor fills a participant, anchor, possessor/beneficiary, relation-endpoint, remembered/reported, institutional, prospective, peripheral, or one-use role. Reject generic/rhetorical/nonreferential person wording.

OBJECT: retain concrete or abstract thing/content handles that fill an independently usable endpoint/node role in the ledger. Concrete things or distinguished parts, values, services/results, decisions/next steps treated as things, choices treated as choices, named sets/categories, remembered/reported content, quoted or figurative content treated as content, and internal represented handles may qualify. The question is whether the source treats the unit as something that can stand as content/endpoint of a represented relation, not whether it is noun-shaped. Reject generic noun phrases, pronouns/deictics, proposition/question shells, discourse points, scenic props with no separate ledger role, descriptive fragments, and nominalized actions without an independent thing/content job.

LABEL: retain distinct source-applied target-bearing characterization events. States, statuses, identities, evaluations, comparisons, self/candidate labels, corrections, rejections, contrasts, and materially represented postures may qualify, including local/one-use, colloquial, idiomatic, uncertain, questioned, negated, corrected, rejected, or figurative forms. Require a target or represented state being characterized. Reject decorative/rhetorical color, incidental description, generic manner, detached modifiers/intensifiers, and scene-setting wording that never fills its own predication role.

VERB: retain each distinct source-native operative relation kernel filling one material relation role in the ledger. Actions, states, cognitions, perceptions, communications, intentions, decisions, possessions, comparisons, evaluations, movements, transitions, gestures, existence/location, obligations, recurrence, and other relations may qualify. One-use relations qualify. Reject auxiliaries/support verbs, filler/discourse predicates, reporting or question shells when represented content is carried elsewhere, empty copular scaffolding, duplicate restatements, whole-clause wrappers, rhetorical bundles, and fragments nested inside a stronger natural relation kernel. Preserve particles/reflexives/negation/modality/bound complements when required and preserve nonasserted posture.

LOCATOR: retain each distinct source-native orientation/context relation filling one material orientation role: position, path, direction, containment, proximity, movement orientation, accompaniment, origin/destination, entry/exit, recurrence/context, internal/relational orientation, or materially spatialized figurative orientation. One-use orientations qualify. Reject every-PP/adverbial behavior, recipient/topic/purpose/possession/degree complements, generic adverbials, isolated deictics with no orientation role, and rhetorical location wording. A spatial/temporal phrase may be LOCATOR when it orients rather than constitutes the support frame.

LITERAL LOCK: every non-null source_wording, source_cue, and order_cue must be character-for-character source text. Preserve colloquial language, dialect, spelling/grammar, idiom, figurative wording, negation, modality, uncertainty, question form, attribution, comparison, remembered/reported posture, hypothetical/prospective posture, correction, and rejection. Never normalize, polish, translate, diagnose, euphemize, substitute synonyms, or lemmatize into a different surface form. Researcher short tags are navigational only and must stay source-near.

PRIMITIVE FREEZE AUDIT:
1) replay the source by material episodes, not sentence tokens;
2) verify every materially differentiated episode has its actual spatial and temporal support;
3) verify each participant, thing/content handle, characterization, operative relation, and orientation occupies a distinct ledger role;
4) restore legitimate local/one-use/colloquial/uncertain/figurative values omitted only because they looked small or nonpersistent;
5) remove candidates admitted only because they are literal spans, nouns, verbs, adjectives, prepositional phrases, scenic details, rhetorical material, or grammatical constituents;
6) redo source-use type arbitration without relying on lexical shape;
7) reduce relation-like units to the smallest complete natural source-native grain;
8) verify exact wording, coreference, class-local distinctness, and first-establishment order;
9) freeze primitives.
Coverage and compression are equally mandatory. Do not solve over-admission by sparse summary and do not solve omission by lexical census.

COMPOUNDS: return to the same private episode ledger after primitive freeze. A valid primitive may remain unbundled. Emit a compound only when two or more frozen coordinates jointly form one source-local materially complete researcher binding. Choose one materially distinct represented relation/characterization/question/choice/report/reflection binding; include only actual participating refs; include support/orientation only when needed to distinguish or materially situate the binding; split when actor set, target/content, source posture, support frame, or independently represented relation changes. Do not create one compound per sentence, clause, lexical verb, primitive, phrase, or episode row. Do not create a compound merely to justify a primitive. Do not create arbitrary co-occurrence, all-pairs links, support chains, scene mega-bundles, singleton equivalents, duplicate restatements, alternate subset/superset decompositions, or graph closure.

qualities_available is a yes/no availability flag only. Do not replace LABEL rows with Q and do not expand qualities into APA analysis.

Never expose approved archetypes, canonical gold extracts, expected counts, evaluator findings, prior scored outputs, calibration answers, sealed holdout source, or holdout output. Never perform promotion, Oval Office admission, APA-ID creation, sovereign/admitted writing, APA scoring, psychological interpretation, or APA database mutation.
'''.strip()

V123_BASE_RULES = APPARATUS_BASE_RULES + "\n\n" + V123_CORRECTION
V123_CLASS_RULES = dict(APPARATUS_CLASS_RULES)
V123_CLASS_RULES.update({
    "PLACE": "Return each materially differentiated source-established spatial SUPPORT frame in the private material episode ledger, including legitimate unnamed and present-telling supports. Derive support from episode structure, not from spatial-looking words. Multiple bindings may share support; multiple unnamed supports may qualify when materially distinct. Use null source_wording plus exact source cue for unnamed PLACE. Do not turn physical nouns, scenic references, destination wording, or locator phrases into PLACE unless they actually constitute support.",
    "TIME": "Return each materially differentiated source-established temporal EPISODE/SUPPORT frame in the private material episode ledger, including legitimate unnamed attempt/condition, response, transition, wait, remembered/reported, recurring, present-reflection, and prospective frames. Derive TIME from episode structure, not from temporal-looking words. Explicit temporal wording may instead orient a larger episode.",
    "PERSON": "Return the speaker plus every distinct source-established human/social actor or stable group after true coreference when it fills a participant, anchor, possessor/beneficiary, relation-endpoint, remembered/reported, institutional, prospective, peripheral, or one-use ledger role. Reject generic/rhetorical/nonreferential person wording.",
    "OBJECT": "Return source-established concrete or abstract THING/CONTENT handles that fill independently usable endpoint/node roles in the material episode ledger. Type by source use, not noun shape or literal denotation. Quoted, figurative, remembered, or reported wording can be OBJECT when the source treats it as content. Reject generic noun phrases, proposition/question shells, discourse points, scenic props with no separate ledger role, descriptive fragments, and nominalized actions without an independent thing/content job.",
    "LABEL": "Return distinct source-applied TARGET-BEARING CHARACTERIZATION events occupying a ledger role. Valid labels may be one-use, colloquial, uncertain, negated, corrected, rejected, or figurative. Type by source use rather than adjective-like wording. Require a represented target/state being characterized. Reject decorative color, incidental description, detached modifiers/intensifiers, and scene-setting language with no independent predication role.",
    "VERB": "Return each distinct source-native operative RELATION KERNEL occupying one material ledger role at the smallest complete natural predicate grain. One-use relations qualify. Type by source use rather than lexical verb presence. Reject auxiliaries/support verbs, filler, report/question shells whose content is carried elsewhere, empty scaffolding, duplicates, whole-clause wrappers, rhetorical bundles, and fragments inside stronger relation kernels. Preserve source posture and bound material needed for identity.",
    "LOCATOR": "Return each distinct source-native ORIENTATION/CONTEXT RELATION occupying one material ledger role at the smallest complete literal grain. One-use orientations qualify. Type by source use rather than prepositional/adverbial shape. Reject recipient/topic/purpose/possession/degree complements, generic adverbials, isolated deictics without orientation role, and rhetorical location wording. Spatial/temporal phrases may be LOCATOR when they orient rather than constitute support.",
})
