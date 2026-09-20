"""V117 neutral apparatus rules: source-reconnection coordinates at natural frame grain.

No archetype answers, evaluator findings, expected counts, prior scored outputs,
calibration answers, or holdout material are included here.
"""
from researcher_inventory.inventory_apparatus import BASE_RULES as APPARATUS_BASE_RULES, CLASS_RULES as APPARATUS_CLASS_RULES

V117_CORRECTION = r'''
V117 PROSPECTIVE CORRECTION — SOURCE-RECONNECTION COORDINATE CLOSURE AT NATURAL FRAME GRAIN.

READ THE WHOLE SOURCE FIRST. Build a SMALL WHOLE-SOURCE RECONNECTION-FRAME MAP before extracting any class. A reconnection frame is a materially differentiated occurrence position, interaction, episode, remembered/reported frame, intended/prospective frame, recurrence context, comparison frame, later conversation/report, or present-reflection frame. It is NOT every sentence, clause, predicate, or semantic relation. Several relations may share one frame; one broad setting/period may contain several materially differentiated local supports.

THE INVENTORY IS A SOURCE-RECONNECTION INDEX, NOT A RELATION-SLOT CENSUS. Retain the class-native coordinates a researcher would need to select in order to reconnect the materially represented people, things/content, characterizations, operative relations, orientations, places, times, and complete bindings. Do not create a primitive merely because local wording fills a grammatical or semantic slot.

LIGHTWEIGHT DOES NOT MEAN HIGH-SALIENCE ONLY. A coordinate may be local, one-use, nested, mundane, background, remembered, reported, prospective, uncertain, negated, figurative, or colloquial. Recurrence, broad importance, narrative centrality, later reuse, and multiple compounds are never required.

RECONNECTION-COORDINATE ADMISSION TEST:
A) SOURCE GROUNDING: the source establishes the coordinate in the requested class, or clearly establishes a legitimate unnamed PLACE/TIME support coordinate.
B) CLASS-NATIVE FUNCTION: the candidate performs the represented job of that class.
C) RECONNECTION VALUE: if the row were absent, a researcher would lose a materially distinct source coordinate, not merely wording already recoverable inside a stronger retained coordinate or binding.
D) NATURAL GRAIN: retain the smallest complete class-native coordinate. Do not split a natural predicate/characterization/orientation/referential handle into semantically meaningful internal fragments and do not inflate it to a clause wrapper.
E) CLASS-LOCAL DISTINCTNESS: resolve true coreference, aliases, and same-class restatements while preserving genuinely different coordinates.

FRAME-SUPPORT CLOSURE:
Replay the source by reconnection frame before freeze. PLACE/TIME support may be explicit or unnamed. Split support when the source materially differentiates occurrence position, object location, destination, waiting position, later interaction/report position, remembered/prospective position, present-telling position, action episode, response/help episode, transition/departure, waiting episode, intended period, later report/conversation, recurrence span, present reflection, or prospective period. These are categories, not a required checklist. Share one support across several relations when the source does not materially differentiate them. Never create one PLACE/TIME per clause and never invent physical or temporal details.

FUNCTIONAL TYPE ARBITRATION:
- represented human/social actor -> PERSON
- tracked thing/content/referential handle -> OBJECT
- source-applied characterization/state/status/evaluation/comparison/identity -> LABEL
- operative lexical action/state/relation -> VERB
- independent position/path/direction/context/orientation -> LOCATOR
- spatial support -> PLACE
- temporal support -> TIME
Type by the row's reconnective job, not part of speech or metaphor. A state/evaluation is not LOCATOR merely because wording is spatialized. A relational phrase is not OBJECT merely because it can be nominalized. A support/copular phrase is not VERB merely because it contains a verb. Cross-class overlap is allowed only when the exact source span genuinely performs two different selectable jobs.

PLACE: retain each spatial support coordinate needed to reconnect a materially differentiated frame. An explicit broad setting and contained/local occurrence position may both qualify. A materially tracked object position, destination, waiting position, later interaction position, remembered/prospective position, or present-telling position may qualify even when exact physical details are unnamed. For unnamed PLACE use null source_wording and exact source_cue. Do not turn every physical noun, surface, object part, or path phrase into PLACE.

TIME: retain each temporal support coordinate needed to reconnect a materially differentiated frame: attempt/condition, response/help, transition/departure, waiting, intended period, later report/conversation, recurrence span, remembered/reported frame, present reflection, or prospective period when source-differentiated. Several relations may share one TIME. For unnamed TIME use null source_wording and exact source_cue. Do not create TIME from every predicate, tense, clause, question, or duration phrase.

PERSON: retain speaker plus each distinct represented human/social actor or stable group after coreference when the actor materially participates in or anchors a source-presented frame/relation. Direct, offscreen, relational, possessive/beneficiary, remembered, reported, institutional, prospective, peripheral, and one-use actors may qualify. Reject nonreferential/generic/rhetorical person wording.

OBJECT: retain source-presented concrete or abstract REFERENTIAL HANDLES that are materially trackable or selectable as things/content. Concrete things, parts, values, services/results, decisions/next steps, contemplated choices treated as choices, recurring relations treated as content, sets/categories, remembered/reported content, and internal represented objects may qualify. Do NOT promote every pronoun, indefinite complement, grammatical argument, question content, clause wrapper, discourse point, or meaningful proposition. For abstract content require that the source itself treats it as a referential handle beyond the predicate wording that states it.

LABEL: retain the smallest complete source-applied characterization/state/status/identity/evaluation/comparison/candidate label/rejection/correction or materially distinct manner/posture that is independently selectable as a characterization. One-use, colloquial, idiomatic, uncertain, questioned, negated, rejected, corrected, and figurative labels may qualify. Keep one natural judgment together; do not split polarity/intensifier/adjective/adverb fragments. Do not create LABEL when the wording's only reconnective job is the operative relation.

VERB: retain the smallest complete literal predicate kernel for each MATERIALLY RECONNECTIVE operative relation, not every lexical verb and not every locally represented relation. Actions, states, cognitions, perceptions, reports/communications, intentions, decisions, possessions, comparisons, evaluations, movements, transitions, gestures, existence/location, obligations, and questions may qualify when the relation itself is a useful selectable coordinate. Preserve particles/reflexives/negation/modality/bound complements required for identity. Keep a coordinated or bound predicate together when its parts jointly form one source-native candidate action, movement, choice, or relation kernel. Split only when the source presents genuinely separate operative relations that remain independently selectable. Reject auxiliaries, tense/aspect support, grammatical/support predicates, discourse/filler predicates, duplicate restatements, and lexical verb fragments nested inside a stronger natural kernel.

LOCATOR: retain the smallest complete exact source span that independently ORIENTS a retained participant, referent, relation, or frame. Position, path, origin/destination, direction, containment, proximity, accompaniment/carrying, entry/exit, recurrence/context, internal/mental/relational position, and materially spatialized figurative/comparative orientation may qualify. A purpose/destination construction may qualify when it actually supplies direction/orientation; a recurrence clause may qualify when it locates a relation in recurring context. Do not inventory every PP, recipient/topic/purpose complement, possession phrase, degree phrase, temporal phrase, generic adverbial, or evaluative state.

LITERAL LOCK: use the smallest complete exact contiguous source-native span preserving each explicit coordinate's identity. Every non-null source_wording/source_cue/order_cue must be exact source text. Preserve negation, modality, uncertainty, question form, attribution, comparison, idiom/dialect, reported/recalled posture, hypothetical/prospective posture, correction/rejection, particles, reflexives, and bound complements when needed. Never normalize, clean up, correct the speaker, paraphrase, translate, diagnose, euphemize, lemmatize into a different surface form, or substitute synonyms.

PRIMITIVE FREEZE AUDIT:
1) replay the reconnection-frame map;
2) close materially differentiated PLACE/TIME supports without per-clause proliferation;
3) verify every retained PERSON/OBJECT/LABEL/VERB/LOCATOR has independent reconnection value at class-native grain;
4) restore local/one-use/remembered/reported/prospective/uncertain/negated/figurative coordinates pruned only for low salience;
5) remove clause/content wrappers, modifier fragments, support verbs, and orientation fragments whose information is already carried by a stronger retained coordinate/binding;
6) arbitrate OBJECT/LABEL/VERB/LOCATOR by represented function;
7) verify natural complete spans, literal lock, coreference, and class-local distinctness;
8) order by first source establishment subject to apparatus rules;
9) freeze all seven ledgers. Never target hidden counts or infer hidden gold.

COMPOUNDS — MATERIALLY COMPLETE SOURCE BINDINGS:
Build only after primitive freeze. A compound is not proof that every primitive/predicate was inventoried. Emit a compound when combining frozen coordinates materially reconnects a source-presented interaction, proposition, characterization, question, comparison, choice, reflection, or other COMPLETE BINDING that would otherwise be lost as structure.
- Group locally joint predicates, participants, referents, qualities, orientations, and support coordinates when the source presents them as one materially complete interaction/proposition.
- Several retained VERBs may belong in one compound when they jointly describe one local interaction/binding.
- Split when participant set, target/content, support frame, source posture, or materially distinct judgment/action changes enough that one bundle would blur separate structure.
- A non-VERB characterization/state/question may form a compound when independently material.
- A valid primitive may remain unbundled.
- Never invent a compound merely to justify a primitive.
Do NOT emit one compound per sentence, clause, predicate, or relation instance. No graph closure, arbitrary co-occurrence, all-pairs links, scene mega-bundles, singleton equivalents, subset/superset variants, support chains, or duplicate restatements.

Never expose approved archetypes, evaluator findings, prior scored outputs, calibration answers, or sealed holdout material. Never perform promotion, Oval Office admission, APA-ID creation, sovereign/admitted writing, or APA database mutation.
'''.strip()

V117_BASE_RULES = APPARATUS_BASE_RULES + "\n\n" + V117_CORRECTION
V117_CLASS_RULES = dict(APPARATUS_CLASS_RULES)
V117_CLASS_RULES.update({
    "PLACE": "Return each source-grounded spatial SUPPORT COORDINATE needed to reconnect a materially differentiated frame, including broad/contained scene, tracked object position, destination, waiting position, later interaction/report position, remembered/prospective position, or present-telling position when source-differentiated. Unnamed support is allowed only when source-established; use null source_wording and exact cue. Do not create one place per relation or promote every physical noun/path phrase.",
    "TIME": "Return each source-grounded temporal SUPPORT COORDINATE needed to reconnect a materially differentiated frame, including attempt/response/transition/wait/intended/later-report/recurrence/present-reflection/prospective frames when differentiated. Several relations may share one time. Unnamed support is allowed only when source-established. Do not create one time per predicate/clause/tense/question.",
    "PERSON": "Return speaker plus each distinct represented human/social actor or stable group after true coreference when materially participating in or anchoring a source frame/relation. One-use, offscreen, relational, possessive/beneficiary, remembered, reported, institutional, prospective, and peripheral actors may qualify; reject nonreferential/generic person wording.",
    "OBJECT": "Return source-presented concrete or abstract REFERENTIAL HANDLES with independent reconnection value: materially tracked things/content, including source-reified choices, decisions, recurring relations, internal objects, values, sets, or reported content when treated as things. Do not turn every pronoun, complement, grammatical argument, question content, clause wrapper, discourse point, or proposition into OBJECT.",
    "LABEL": "Return the smallest complete independently selectable source-applied characterization/state/status/identity/evaluation/comparison/candidate label/rejection/correction. Preserve one-use/colloquial/questioned/negated/figurative labels. Keep natural judgments whole; do not inventory every modifier fragment or wording whose only role is the operative relation.",
    "VERB": "Return the smallest complete literal kernel for each MATERIALLY RECONNECTIVE operative relation. Keep coordinated/bound predicates together when they jointly form one source-native action/choice/movement/relation; split only genuinely separate selectable relations. Reject auxiliaries, support/interrogative grammar, duplicates, discourse predicates, and lexical fragments nested inside a stronger natural kernel.",
    "LOCATOR": "Return the smallest complete exact span with independent ORIENTATION/CONTEXT value: position, path, origin/destination, direction, containment, proximity, accompaniment, entry/exit, recurrence/context, internal/relational position, or genuinely spatialized figurative orientation. Do not treat evaluative states or every PP/recipient/topic/purpose/temporal/adverbial phrase as LOCATOR.",
})
