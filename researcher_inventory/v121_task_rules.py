"""V121 neutral worker rules: class-relative individuation plus selective compounds.

No archetype answers, expected counts, evaluator findings, prior scored outputs,
canonical gold extracts, calibration answers, or holdout material are included here.
"""
from researcher_inventory.inventory_apparatus import BASE_RULES as APPARATUS_BASE_RULES, CLASS_RULES as APPARATUS_CLASS_RULES

V121_CORRECTION = r'''
V121 PROSPECTIVE CORRECTION — CLASS-RELATIVE SOURCE INDIVIDUATION AT BOUNDED LITERAL GRAIN.

READ THE WHOLE SOURCE FIRST. Before extracting PLACE or TIME, map materially differentiated spatial supports and temporal episodes/frames across the complete source, including legitimate unnamed supports. Then answer only the requested class.

THE INVENTORY IS NEITHER A SPARSE SUMMARY NOR A SURFACE-SPAN CENSUS. Literal source addressability is necessary evidence for explicit units, but it is never sufficient by itself.

COORDINATE IDENTITY IS CLASS-RELATIVE:
- PLACE, TIME, PERSON, OBJECT are referential/support classes. Individuate them when the source establishes a distinct support, participant, thing, content handle, or other referential coordinate appropriate to that class.
- LABEL, VERB, LOCATOR are occurrence-bound relational classes. Individuate them when the source establishes a distinct characterization, relation kernel, orientation, path, containment, contextual relation, or other relational event. A valid relation may be unique/local/one-use and need not persist, recur, or have entity-like identity.

CONTROLLING TEST: does the source itself differentiate this as one selectable coordinate in the requested class, rather than merely containing words that could be segmented that way?

A primitive does NOT need to be compound-indispensable, globally salient, recurrent, or necessary to make the story understandable. Local, one-use, mundane, remembered, reported, uncertain, negated, questioned, hypothetical, prospective, figurative, and colloquial coordinates may qualify when the source itself differentiates them in the requested class.

REJECT candidates that contribute only grammar, narration, discourse management, rhetorical color, incidental description, generic scene wording, detached modifiers/intensifiers, proposition/question shells, or internal fragments of a stronger source-native coordinate.

NATURAL LITERAL GRAIN: use the smallest complete source-native unit that preserves the represented class job. For LABEL/VERB/LOCATOR, prefer the lexical or phrasal nucleus carrying the characterization/relation/orientation. Do not promote an entire clause, proposition, question shell, or rhetorical bundle when a smaller source-native nucleus carries the job. Keep a natural multiword construction whole when splitting would destroy or materially change its source-native job.

FUNCTIONAL TYPE — PRIMARY REPRESENTED JOB:
- spatial support -> PLACE
- temporal episode/support -> TIME
- represented human/social actor -> PERSON
- independently represented thing/content/referential handle -> OBJECT
- source-applied characterization/state/status/evaluation/comparison/identity -> LABEL
- operative happening/action/state/relation kernel -> VERB
- independently represented orientation/path/direction/containment/proximity/context -> LOCATOR
Use the primary represented job when grammar permits several descriptions. Cross-class duplication is allowed only when the source genuinely establishes two independently selectable jobs, not merely because the same wording can be parsed more than one way.

PLACE: retain each materially differentiated source-established spatial SUPPORT frame. This may be an explicit broad setting, a distinct contained/local support, an unnamed location of a represented object/interaction/participant configuration/wait/event, a destination, remembered/reported setting, later setting, or source-established present-telling setting. Several relations may share one PLACE when support is not differentiated. Multiple unnamed PLACE rows are lawful when materially distinct supports are established. For unnamed PLACE use source_wording null, an exact source cue, and a neutral mechanical tag. Never invent where. Do not turn every physical noun, destination wording, or locator phrase into PLACE.

TIME: retain each materially differentiated source-established temporal EPISODE/SUPPORT frame rather than every temporal expression. Attempts/conditions, response phases, transitions, waits, intended/remembered/reported periods, later conversations/reports, recurring spans, present reflection, and future/prospective frames may qualify. TIME does not require a date/clock/temporal noun. Several relations may share one TIME when their support is the same. An explicit temporal phrase is not automatically TIME when it merely orients a larger episode. For unnamed TIME use source_wording null, an exact source cue, and a neutral mechanical tag.

PERSON: retain the speaker plus every distinct source-established human/social actor or stable group after true coreference when represented as participant, anchor, relation endpoint, remembered/reported actor, possessor/beneficiary, institutional actor, prospective actor, peripheral actor, or one-use actor. Reject rhetorical/generic/nonreferential person wording that never becomes a represented actor coordinate.

OBJECT: retain source-individuated concrete or abstract THING/CONTENT handles. Things/parts, values, services/results, decisions/next steps treated as things, choices treated as choices, named sets/categories, remembered/reported content, and internal represented content may qualify. Reject generic noun phrases, pronouns/deictics, every grammatical argument/complement, explanations, question content, clause/proposition wrappers, discourse points, descriptive fragments, and actions merely because they can be nominalized. The source must treat the candidate as a distinct thing/content node.

LABEL: retain distinct source-applied CHARACTERIZATION EVENTS: qualities/states, statuses, identities, evaluations, comparisons, self/candidate labels, rejections, corrections, contrasts, and materially expressed postures. LABEL is occurrence-bound and target-bearing; a legitimate characterization may occur only once and need not persist independently. Preserve legitimate colloquial/idiomatic/questioned/negated/uncertain/corrected/rejected/figurative characterization. Use the shortest complete exact source form carrying the characterization. Reject rhetorical color, incidental description, generic manner wording, detached modifiers/intensifiers, scene-setting adjectives that are not applied as a represented characterization, and repeated restatements.

VERB: retain each distinct source-individuated operative RELATION EVENT at natural predicate grain. Actions, states, cognitions, perceptions, reports/communications, intentions, decisions, possessions, comparisons, evaluations, movements, transitions, gestures, existence/location, obligations, recurrence, and other represented relations may qualify. VERB is occurrence-bound: a legitimate relation may be unique and one-use and need not have persistent identity, recurrence, global salience, or compound indispensability. Do NOT create one VERB for every lexical verb or clause. Reject auxiliaries/support verbs, filler/discourse predicates, question shells when a smaller relation nucleus or another class carries the stable job, copular/reporting scaffolding with no distinct relation contribution, repeated restatements, whole-clause/proposition wrappers, rhetorical bundles, and fragments nested inside stronger relation kernels. Preserve particles/reflexives/negation/modality/bound complements when identity requires them and preserve nonasserted posture.

LOCATOR: retain each distinct source-individuated ORIENTATION/CONTEXT RELATION: position, path, direction, containment, proximity, movement orientation, accompaniment, origin/destination, entry/exit, recurrence/context, internal/relational orientation, or materially spatialized figurative orientation. LOCATOR is occurrence-bound: a legitimate orientation may be unique and one-use and need not persist as an entity-like coordinate. It is not every prepositional/adverbial phrase. Use the smallest complete exact construction carrying the orientation. A spatial/temporal phrase may be LOCATOR when it orients rather than constitutes a PLACE/TIME support. Reject recipient/topic/purpose/possession/degree complements, generic adverbials, isolated deictics without an orientation relation, and rhetorical location wording.

LITERAL LOCK: every non-null source_wording, source_cue, and order_cue must be exact source text. Preserve colloquial language, dialect, spelling/grammar, idiom, figurative wording, negation, modality, uncertainty, question form, attribution, comparison, remembered/reported posture, hypothetical/prospective posture, correction, and rejection. Never normalize, polish, translate, diagnose, euphemize, substitute synonyms, or lemmatize into a different surface form. Researcher short tags are navigational only and must stay source-near.

PRIMITIVE FREEZE AUDIT — CLASS-RELATIVE COVERAGE AND COMPRESSION:
1) replay the whole source in order;
2) verify scene/place and temporal episode maps, including legitimate unnamed supports;
3) verify PLACE/TIME/PERSON/OBJECT for source-established referential/support coordinates;
4) verify LABEL/VERB/LOCATOR for distinct occurrence-bound characterization/relation/orientation coordinates, including valid local and one-use instances;
5) restore valid coordinates omitted only because they lacked persistence, recurrence, or global importance;
6) remove candidates admitted only because they are addressable surface spans, incidental descriptions, grammatical constituents, rhetorical/discourse material, detached modifiers, or proposition wrappers;
7) reduce whole-clause relational candidates to the smallest complete source-native lexical/phrasal nucleus preserving the represented job;
8) arbitrate OBJECT/LABEL/VERB/LOCATOR by primary represented job;
9) verify natural literal grain, exact wording, coreference, class-local distinctness, and first-establishment order;
10) freeze primitives.
Do not solve omission by turning the source into a lexical/clause census, and do not solve over-admission by returning to sparse summary.

BINDING LEDGER IS VALIDATION, NOT PRIMITIVE ENTITLEMENT. Use represented bindings after extraction to check coverage and build compounds. A legitimate primitive may remain unbundled; a unique one-use relation may still be a valid primitive. Do not invent a primitive merely to fill a binding and do not delete a valid primitive merely because no compound requires it.

COMPOUNDS — SELECTIVE MATERIAL BINDINGS AFTER PRIMITIVE FREEZE. Emit a compound only when two or more frozen coordinates jointly form one source-local materially complete researcher binding. Use only participating refs; include enough for completeness without unrelated context; split only when actor set, target/content, posture, support frame, or independently represented relation changes materially. Do not create one compound per clause, predicate token, primitive, sentence, or addressable phrase. Do not emit arbitrary co-occurrence, subset/superset variants, graph closure, all-pairs links, support chains, scene mega-bundles, singleton equivalents, or duplicate restatements.

qualities_available is a yes/no availability flag only. Do not replace LABEL rows with Q and do not expand qualities into APA analysis.

Never expose approved archetypes, canonical gold extracts, expected counts, evaluator findings, prior scored outputs, calibration answers, sealed holdout source, or holdout output. Never perform promotion, Oval Office admission, APA-ID creation, sovereign/admitted writing, APA scoring, psychological interpretation, or APA database mutation.
'''.strip()

V121_BASE_RULES = APPARATUS_BASE_RULES + "\n\n" + V121_CORRECTION
V121_CLASS_RULES = dict(APPARATUS_CLASS_RULES)
V121_CLASS_RULES.update({
    "PLACE": "Return each materially differentiated source-established spatial SUPPORT frame, including legitimate unnamed supports. Map scenes across the whole source before extraction. Broad and contained supports may both qualify when source structure distinguishes them; multiple unnamed supports may qualify when materially distinct. Use null source_wording plus exact cue for unnamed PLACE. Mere physical nouns, destination wording, locator phrases, or addressable text are not PLACE by themselves.",
    "TIME": "Return each materially differentiated source-established temporal EPISODE/SUPPORT frame, not every temporal expression or predicate occurrence. Attempts/conditions, response phases, transitions, waits, intended/remembered/reported periods, later conversations/reports, recurring spans, present reflection, and future/prospective frames may qualify. Use null source_wording plus exact cue for unnamed TIME. Explicit temporal wording may instead be LOCATOR/context when it only orients a larger episode.",
    "PERSON": "Return the speaker plus every distinct source-established human/social actor or stable group after true coreference when represented as participant, anchor, relation endpoint, remembered/reported actor, possessor/beneficiary, institutional actor, prospective actor, peripheral actor, or one-use actor. Reject rhetorical/generic/nonreferential person wording that never becomes a represented actor coordinate.",
    "OBJECT": "Return source-individuated concrete or abstract THING/CONTENT handles. Things/parts, values, services/results, decisions/next steps treated as things, choices treated as choices, named sets/categories, remembered/reported content, and internal represented content may qualify. Reject generic noun phrases, pronouns/deictics, every argument/complement, explanations, question content, clause/proposition wrappers, discourse points, descriptive fragments, and actions merely because they can be nominalized.",
    "LABEL": "Return distinct source-applied CHARACTERIZATION EVENTS with actual targets: qualities/states, statuses, identities, evaluations, comparisons, self/candidate labels, rejections, corrections, contrasts, and materially expressed postures. A valid LABEL may be unique/one-use and need not persist independently. Use the shortest complete exact source form carrying the characterization. Reject incidental description, rhetorical color, generic manner wording, detached modifiers/intensifiers, scene-setting adjectives without a characterization relation, and repeated restatements.",
    "VERB": "Return each distinct source-individuated operative RELATION EVENT at the smallest complete natural predicate grain. A valid relation may be unique/one-use and need not have persistent identity or recur. Do not create one VERB per lexical verb or clause. Reject auxiliaries/support verbs, filler, question shells when a smaller relation nucleus or another class carries the job, empty copular/reporting scaffolding, duplicates, whole-clause/proposition wrappers, rhetorical bundles, and fragments nested inside stronger relation kernels. Preserve particles/reflexives/negation/modality/bound complements when relation identity requires them and preserve nonasserted posture.",
    "LOCATOR": "Return each distinct source-individuated ORIENTATION/CONTEXT RELATION at the smallest complete literal grain: position, path, direction, containment, proximity, movement orientation, accompaniment, origin/destination, entry/exit, recurrence/context, internal/relational orientation, or materially spatialized figurative orientation. A valid LOCATOR may be unique/one-use and need not persist. Reject every-PP/adverbial behavior, recipient/topic/purpose/possession/degree complements, isolated deictics without an orientation relation, and rhetorical location wording. A spatial/temporal phrase may be LOCATOR when it orients rather than constitutes a PLACE/TIME support frame.",
})
