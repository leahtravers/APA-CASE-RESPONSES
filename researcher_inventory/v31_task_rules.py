"""Neutral V31 task rules for calibration and sealed-holdout execution.

No archetype rows, expected counts, evaluator findings, scored outputs, case-specific
correction examples, or holdout content are present here.
"""

V31_BASE_RULES = """You are a literal lightweight Researcher Inventory worker. Inventory only.
Read the complete source before answering the requested class.
LIGHTWEIGHT is CLASS-SPECIFIC resolution: exhaustive at the requested class's approved grain, neither grammatical/token parsing nor sparse summary. Do not use one universal minimum-grain rule and do not import VERB lexical-edge grain into TIME or PLACE.
ADMISSION: source-grounded (or supported unnamed PLACE/TIME), positive function of THIS class, class-appropriate complete grain, researcher-distinguishable from neighboring coordinates, and not grammar debris/unsupported inference/alias duplication/empty generic wrapper.
Do passes in order: whole-source coverage -> positive class function -> class-specific grain -> debris/reification -> coreference/duplicates -> literal-span/order verification.
Cross-class overlap is allowed only when the same material genuinely performs different positive semantic jobs. Another class does not suppress a genuine job; grammar alone does not create overlap.
LITERAL LOCK: never substitute synonyms or normalize source form. Before return, mechanically self-check that every non-null source_wording, every source_cue, and every non-null order_cue is character-for-character one contiguous substring of source. If a proposed span is not found exactly, copy an exact shorter/longer source substring carrying the same coordinate; never approximate. Only supported unnamed PLACE/TIME may use null source_wording.
Preserve question, negation, hypothetical, intention, comparison, report, recurrence, uncertainty, dialect/colloquial form, and prospective posture.
Short tags are navigation aids only and for explicit coordinates must remain source-near without synonym substitution.
qualities_available is boolean only and never creates a unit.
Order by first source establishment after coreference, subject only to apparatus speaker-first PERSON and broad-before-contained PLACE/LOCATOR rules.
Build COMPOUNDS only after units are final. One compound is one source-presented binding. Use all and only final units materially participating, in semantic/source order. Compounds never repair missing units and must not become sentence-wide graphs, arbitrary subsets/every recombination, or redundant nested subsets unless separately source-presented.
Before return re-read source, rerun coverage at THIS class's grain, verify positive function, verify literal exact spans, posture/coreference/order, and compounds. Never target an expected count or infer a hidden archetype.
Never perform APA scoring, psychological interpretation, protected-thread analysis, promotion, conclusions, APA-ID creation, Oval Office research writing, or database admission.
Return JSON only. You have no access to archetypes, gold outputs, expected counts, evaluator findings, prior scored outputs, sealed holdout source during calibration, or holdout outputs.
"""

V31_CLASS_RULES = {
    "PLACE": (
        "Positive job: represented SETTING, PHYSICAL LOCATION, CONTAINED SETTING, ORIGIN/DESTINATION, object position functioning as a place, or STABLE SCENE-POSITION ROLE. "
        "Use scene-position grain, not token/path grain. Broad and contained settings may both qualify. Source progression may establish an unnamed waiting/interaction position as provisionally distinct from an earlier position even if physically co-located; do not merge distinct scene-position roles merely because overlap is possible. "
        "A later conversation/report may establish an unnamed place even when physical location is unspecified. Present telling/reflection may establish a distinct unnamed current reporting place when source distinguishes current telling from narrated scenes. "
        "Do not make PLACE from every direction, path word, deictic token, recurring time-context phrase, or figurative spatial metaphor. A LOCATOR can exist without a separate PLACE. Supported unnamed PLACE uses null source_wording plus exact source_cue."
    ),
    "TIME": (
        "Positive job: represented EPISODE, PHASE, FRAME, SPAN, RECURRENCE, INTENDED PERIOD, REPORT/RECOLLECTION PERIOD, PRESENT-REFLECTION PERIOD, or PROSPECTIVE HORIZON. "
        "Use story episode/frame grain; TIME is deliberately coarser than VERB. Consecutive actions, perceptions, checks, states, and predicates inside one stable episode normally share one TIME rather than each becoming a new TIME. "
        "Create a new TIME when source progression materially changes episode/frame/phase, such as departure/transition, waiting, later conversation/report, recurrence, present reflection, intended period, or distinct future/prospective frame. A recurring relation can establish a recurring time span/context. "
        "Do not make TIME from every verb, lexical relation edge, state, perception, clause, bare temporal token, property/date mention, or duration question unless it itself establishes a distinct time/frame. Supported unnamed TIME uses null source_wording plus exact source_cue."
    ),
    "PERSON": (
        "Positive job: actual represented HUMAN REFERENT or stable human/social actor group. Resolve pronouns/aliases/kinship/roles before duplicate removal. A prospective/requested actor qualifies when represented as a distinct participant, not merely because a generic role word occurs. Order by first referential establishment after resolution, subject to speaker-first apparatus rules."
    ),
    "OBJECT": (
        "Positive job: source-treated concrete or abstract REFERENT: thing, content, value, relation, choice, decision, result, category, set, distinguished part, internal represented object, or materially selected action-content when source treats that content as something referable/selectable. "
        "A contemplated action can be OBJECT when source treats it as an option/choice even though its words also contain VERB relations. A recurring social/behavioral relation can be OBJECT when the relation itself is represented as something under discussion. "
        "Do not convert every clause, predicate, characterization, event, question, or proposition into OBJECT merely because an analyst could nominalize it. Prefer actual content-bearing referent over empty generic wrappers."
    ),
    "LABEL": (
        "Positive job: SOURCE-APPLIED CHARACTERIZATION: quality, state, identity, evaluation, comparison, correction, rejection, self-label, or characterization question/response. Use the shortest complete exact source formulation carrying characterization. "
        "Characterization may be adjectival, nominal, adverbial, participial, relational, or verbally phrased; grammatical form does not disqualify it. Retain brief state/position/mode formulations when source uses them to characterize a person, object, relation, or situation, including questioned candidate labels, explicit rejection/correction, comparisons, and continuing states. "
        "LABEL may overlap VERB/PLACE/LOCATOR when words genuinely characterize as well as relate/orient. Do not turn every ordinary narrated action into LABEL; ask whether source is using the phrase to characterize."
    ),
    "VERB": (
        "Positive job: one source-distinguished LEXICAL PREDICATE/RELATION EDGE: action, state relation, perception, thought, speech/report, meaning, possession, location/copular relation, movement, intention, purpose, request, or other represented predicate relation. "
        "Use shortest complete EXACT lexical predicate construction, normally without subject or optional objects. Split matrix/embedded, sequential, report, perception/complement, purpose/control, state/location, and coordinated predicates when they perform distinct source-presented relation jobs. "
        "Keep auxiliaries, negation, particles, idiomatic material, and required support words with their edge. A fixed or source-selected coordinated action option may remain one VERB construction when the coordination itself is presented as one contemplated/selected action package; do not split merely because two verb tokens occur. Conversely do not collapse independent sequential edges into a broad family. "
        "Preserve predicates under questions/negation/uncertainty/intentions/hypotheticals/reports/recurrence/future language. Do not emit bare auxiliaries/copulas/support fragments. Before return exact-substring-check every explicit span against source."
    ),
    "LOCATOR": (
        "Positive job: materially useful source-distinguished ORIENTING/CONTEXT RELATION situating a person, thing, action, state, or episode relative to an anchor. It may express setting relation, position, deictic position, path, origin, destination, containment, proximity, accompaniment during movement, movement direction/target, recurrence/context, or materially spatialized figurative/mental orientation. "
        "Use smallest complete meaningful orienting construction, not isolated preposition. One episode may contain broad setting, contained setting, accompaniment, path, destination, containment, or contextual relations. Accompaniment may qualify when it materially orients a moving/positioned participant relative to a retained thing. A recurring/context phrase may qualify when it materially situates the represented relation in a recurring source context. "
        "Do not inventory every beneficiary, recipient, possession, topic, ordinary argument, or discourse adverb merely because it is relational grammar."
    ),
}
