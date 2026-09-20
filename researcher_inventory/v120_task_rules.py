"""V120 neutral worker rules: stable class-native coordinates plus selective compounds.

No archetype answers, expected counts, evaluator findings, prior scored outputs,
canonical gold extracts, calibration answers, or holdout material are included here.
"""
from researcher_inventory.inventory_apparatus import BASE_RULES as APPARATUS_BASE_RULES, CLASS_RULES as APPARATUS_CLASS_RULES

V120_CORRECTION = r'''
V120 PROSPECTIVE CORRECTION — STABLE SOURCE-INDIVIDUATED CLASS-NATIVE COORDINATES AT BOUNDED GRAIN.

READ THE WHOLE SOURCE FIRST. Before extracting PLACE or TIME, map the materially differentiated spatial supports and temporal episodes/frames established across the complete source, including legitimate unnamed supports. Then answer only the requested class.

THE INVENTORY IS NEITHER A SPARSE SUMMARY NOR A SURFACE-SPAN CENSUS. Mere source addressability is not enough. A primitive must have a stable identity in its requested class beyond simply being a meaningful phrase that can be pointed to.

ADMIT a primitive when it is source-grounded; source-individuated as one stable class-native coordinate; materially participates in represented structure or materially supports it for PLACE/TIME; is naturally grained; is literal/source-faithful; and is not a true duplicate/coreference.

A primitive does NOT need to be indispensable to a compound, globally salient, recurrent, or necessary to make the story understandable. Local, one-use, mundane, remembered, reported, uncertain, negated, questioned, hypothetical, prospective, figurative, and colloquial coordinates may qualify when the source itself individuates them in the requested class.

REJECT candidates admitted only because they are grammatical constituents, lexical verb occurrences, noun phrases, temporal expressions, prepositional phrases, question shells, clause/proposition wrappers, rhetorical or descriptive color, discourse management, generic deictics, detached modifiers/intensifiers, repeated restatements, or internal fragments of a stronger natural coordinate.

FUNCTIONAL TYPE — PRIMARY REPRESENTED JOB:
- spatial support -> PLACE
- temporal episode/support -> TIME
- represented human/social actor -> PERSON
- independently represented thing/content/referential handle -> OBJECT
- source-applied characterization/state/status/evaluation/comparison/identity -> LABEL
- operative happening/action/state/relation kernel -> VERB
- independently represented orientation/path/direction/containment/proximity/context -> LOCATOR
Use the primary represented job when grammar permits several descriptions. Cross-class duplication is allowed only when the source genuinely establishes two independently selectable class jobs, not merely because the phrase can be parsed more than one way.

PLACE: retain each materially differentiated source-established spatial SUPPORT frame. This may be an explicit broad setting, a distinct contained/local support, an unnamed location of a represented object/interaction/participant configuration/wait/event, a destination, remembered/reported setting, later setting, or source-established present-telling setting. Several relations may share one PLACE when support is not differentiated. Multiple unnamed PLACE rows are lawful when materially distinct supports are established. For unnamed PLACE use source_wording null, an exact source cue, and a neutral mechanical tag. Never invent where. Do not turn every physical noun or locator phrase into PLACE.

TIME: retain each materially differentiated source-established temporal EPISODE/SUPPORT frame rather than every temporal expression. Attempts/conditions, help/response phases, departures/transitions, waits, intended periods, remembered/reported periods, later conversations/reports, recurring spans, present reflection, and explicit future/prospective frames may qualify. TIME does not require a date/clock/temporal noun. Several relations may share one TIME when their support is the same. An explicit temporal phrase is not automatically TIME when it merely orients a larger episode. For unnamed TIME use source_wording null, an exact source cue, and a neutral mechanical tag.

PERSON: retain the speaker plus every distinct represented human/social actor or stable group after true coreference when the source establishes that actor as a participant, anchor, relation endpoint, remembered/reported actor, possessor/beneficiary, institutional actor, prospective actor, peripheral actor, or one-use actor. Reject rhetorical, generic, or nonreferential person wording that never becomes a represented actor coordinate.

OBJECT: retain source-individuated concrete or abstract THING/CONTENT handles: things/parts, values, services/results, decisions or next steps treated as things, choices treated as choices, named sets/categories, remembered/reported content, and internal represented content handles. Reject pronouns/generic deictics, every noun phrase or grammatical argument/complement, explanations, question content, clause/proposition wrappers, discourse points, and actions merely because they can be nominalized. The source must treat the candidate as a stable thing/content node.

LABEL: retain source-individuated CHARACTERIZATIONS: qualities/states, statuses, identities, evaluations, comparisons, self-labels, candidate labels, rejections, corrections, contrasts, and materially expressed postures. Preserve colloquial, idiomatic, questioned, negated, uncertain, corrected, rejected, and figurative labels when the characterization itself is represented. Use the shortest complete exact source form carrying the characterization. Reject decorative/rhetorical color, incidental description, generic manner wording, detached modifiers/intensifiers, and repeated restatements that do not establish a distinct characterization.

VERB: retain source-individuated operative RELATION KERNELS at natural predicate grain. Actions, states, cognitions, perceptions, reports/communications, intentions, decisions, possessions, comparisons, evaluations, movements, transitions, gestures, existence/location, obligations, recurrence, and other relations qualify only when the relation itself is a stable selectable coordinate. Do NOT create one VERB for every lexical verb or clause. Reject auxiliary/support verbs, discourse/filler predicates, question shells whose stable coordinate belongs elsewhere, copular/reporting scaffolding when stable content belongs to another class, repeated restatements, whole-clause wrappers, and fragments nested inside stronger natural relation kernels. Preserve particles/reflexives/negation/modality/bound complements when required for relation identity. Preserve questioned/negated/hypothetical/intended/reported/remembered/recurring/prospective posture without asserting occurrence.

LOCATOR: retain source-individuated ORIENTATION/CONTEXT coordinates: position, path, direction, containment, proximity, movement orientation, accompaniment, origin/destination, entry/exit, recurrence/context, internal/relational orientation, or materially spatialized figurative orientation. A LOCATOR is not every prepositional/adverbial phrase. An explicit spatial or temporal phrase may be LOCATOR rather than PLACE/TIME when it orients a larger support frame instead of constituting that support. Reject recipient/topic/purpose/possession/degree complements, generic adverbials, isolated here/there, and rhetorical location wording without independent orientation identity.

LITERAL LOCK: every non-null source_wording, source_cue, and order_cue must be exact source text. Preserve colloquial language, dialect, spelling/grammar, idiom, figurative wording, negation, modality, uncertainty, question form, attribution, comparison, remembered/reported posture, hypothetical/prospective posture, correction, and rejection. Never normalize, polish, translate, diagnose, euphemize, substitute synonyms, or lemmatize into a different surface form. Researcher short tags are navigational only and must stay source-near.

PRIMITIVE FREEZE AUDIT — COMPRESSION AND OMISSION ARE EQUALLY MANDATORY:
1) replay the whole source in order;
2) verify the scene/place map and temporal episode map, including legitimate unnamed supports;
3) verify each class for stable class-native identities;
4) restore valid low-salience/local/one-use coordinates omitted only because they were not globally important;
5) remove candidates admitted only because they are addressable surface spans;
6) remove grammar/discourse scaffolding, rhetorical color, proposition wrappers, internal fragments, repeated restatements, and true duplicates;
7) arbitrate OBJECT/LABEL/VERB/LOCATOR by primary represented job;
8) verify natural literal grain, exact wording, coreference, class-local distinctness, and first-establishment order;
9) freeze primitives.
Do not solve omission by turning the source into a lexical/clause census, and do not solve over-admission by returning to sparse summary.

COMPOUNDS — SELECTIVE MATERIAL BINDINGS AFTER PRIMITIVE FREEZE. A valid primitive may remain unbundled. Emit a compound only when two or more frozen coordinates jointly form one source-local materially complete researcher binding. Use only participating refs; include enough for completeness without unrelated context; split only when actor set, target/content, posture, support frame, or independently represented relation changes materially. Do not create one compound per clause, predicate token, primitive, sentence, or addressable phrase. Do not emit arbitrary co-occurrence, subset/superset variants, graph closure, all-pairs links, support chains, scene mega-bundles, singleton equivalents, or duplicate restatements.

qualities_available is a yes/no availability flag only. Do not replace LABEL rows with Q and do not expand qualities into APA analysis.

Never expose approved archetypes, canonical gold extracts, expected counts, evaluator findings, prior scored outputs, calibration answers, sealed holdout source, or holdout output. Never perform promotion, Oval Office admission, APA-ID creation, sovereign/admitted writing, APA scoring, psychological interpretation, or APA database mutation.
'''.strip()

V120_BASE_RULES = APPARATUS_BASE_RULES + "\n\n" + V120_CORRECTION
V120_CLASS_RULES = dict(APPARATUS_CLASS_RULES)
V120_CLASS_RULES.update({
    "PLACE": "Return each materially differentiated source-established spatial SUPPORT frame with stable identity, including legitimate unnamed supports. Map scenes across the whole source before extraction. Broad and contained supports may both qualify when source structure distinguishes them; multiple unnamed supports may qualify when materially distinct. Use null source_wording plus exact cue for unnamed PLACE. Mere physical nouns, locator phrases, or addressable wording are not PLACE by themselves.",
    "TIME": "Return each materially differentiated source-established temporal EPISODE/SUPPORT frame with stable identity, not every temporal expression or predicate occurrence. Attempts/conditions, response phases, transitions, waits, intended/remembered/reported periods, later conversations/reports, recurring spans, present reflection, and future/prospective frames may qualify. Use null source_wording plus exact cue for unnamed TIME. Explicit temporal wording may instead be LOCATOR/context when it only orients a larger episode.",
    "PERSON": "Return the speaker plus every distinct source-established human/social actor or stable group after true coreference when represented as participant, anchor, relation endpoint, remembered/reported actor, possessor/beneficiary, institutional actor, prospective actor, peripheral actor, or one-use actor. Reject rhetorical/generic/nonreferential person wording that never becomes a stable actor coordinate.",
    "OBJECT": "Return source-individuated concrete or abstract THING/CONTENT handles with stable identity. Things/parts, values, services/results, decisions/next steps treated as things, choices treated as choices, named sets/categories, remembered/reported content, and internal represented content may qualify. Reject generic noun phrases, pronouns/deictics, every argument/complement, explanations, question content, clause/proposition wrappers, discourse points, and actions merely because they can be nominalized.",
    "LABEL": "Return source-individuated CHARACTERIZATIONS with stable target/state identity: qualities/states, statuses, identities, evaluations, comparisons, self/candidate labels, rejections, corrections, contrasts, and materially expressed postures. Preserve legitimate colloquial/idiomatic/questioned/negated/uncertain/corrected/rejected/figurative characterization. Reject rhetorical color, incidental description, generic manner wording, detached modifiers/intensifiers, and repeated restatements without distinct characterization identity.",
    "VERB": "Return source-individuated operative RELATION KERNELS at natural complete predicate grain, not every lexical verb or clause. Retain a relation only when it is itself a stable selectable coordinate. Preserve particles/reflexives/negation/modality/bound complements when identity requires them and preserve nonasserted posture. Reject auxiliaries, filler, question shells, copular/reporting scaffolding when stable content belongs elsewhere, duplicate restatements, whole-clause wrappers, and fragments nested inside stronger relation kernels.",
    "LOCATOR": "Return source-individuated ORIENTATION/CONTEXT coordinates with stable identity: position, path, direction, containment, proximity, movement orientation, accompaniment, origin/destination, entry/exit, recurrence/context, internal/relational orientation, or materially spatialized figurative orientation. Reject every-PP/adverbial behavior, recipient/topic/purpose/possession/degree complements, isolated here/there, and rhetorical location wording without independent orientation identity. A spatial/temporal phrase may be LOCATOR when it orients rather than constitutes a PLACE/TIME support frame.",
})
