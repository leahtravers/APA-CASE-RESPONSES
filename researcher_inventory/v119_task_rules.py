"""V119 neutral apparatus rules: source-addressable primitive ledgers plus selective compounds.

No archetype answers, expected counts, evaluator findings, prior scored outputs,
calibration answers, canonical gold extracts, or holdout material are included here.
"""
from researcher_inventory.inventory_apparatus import BASE_RULES as APPARATUS_BASE_RULES, CLASS_RULES as APPARATUS_CLASS_RULES

V119_CORRECTION = r'''
V119 PROSPECTIVE CORRECTION — PRIMITIVES ARE SOURCE-ADDRESSABLE CLASS COORDINATES; COMPOUNDS ARE SELECTIVE MATERIAL BINDINGS.

READ THE WHOLE SOURCE FIRST. The primitive inventory is a literal researcher-reconnection index, NOT a sparse summary and NOT a clause/token census. Preserve all materially useful researcher-selectable coordinates at their own class-native grain, including local, one-use, mundane, remembered, reported, uncertain, negated, questioned, hypothetical, prospective, figurative, and colloquial material when source-grounded.

PRIMITIVE ADMISSION DOES NOT DEPEND ON COMPOUND NECESSITY. A primitive does not need to be indispensable to a complete binding and does not need to make a larger relation unintelligible when removed. Judge primitives at the ledger/class level.

ADMIT a primitive when it is source-grounded, independently selectable in the requested class, naturally grained, literal/source-faithful, and not a true duplicate/coreference.

REJECT only unsupported inference; pure grammatical carriage; discourse-management/filler wording; generic deictic wrappers; sentence/clause/proposition packaging that has no independent class-native job; isolated intensifier/modifier fragments; internal fragments of a stronger natural coordinate; and true duplicates/coreference.

INDEPENDENTLY SELECTABLE means the coordinate can stand as its own useful row for a researcher reconnecting WHERE, WHEN, WHO, WHAT/CONTENT, HOW CHARACTERIZED, WHAT HAPPENED/WAS RELATED, or WHAT ORIENTATION/CONTEXT was represented. Do not require global salience, recurrence, later reuse, multiple compounds, or hidden-gold importance.

FUNCTIONAL TYPE ARBITRATION:
- spatial support -> PLACE
- temporal support -> TIME
- represented human/social actor -> PERSON
- independently selectable thing/content/referential handle -> OBJECT
- source-applied characterization/state/status/evaluation/comparison/identity -> LABEL
- independently inventoryable happening/action/state/relation -> VERB
- independently selectable position/path/direction/containment/proximity/orientation/context -> LOCATOR
Cross-class overlap is allowed only when the exact source span genuinely performs two independent class jobs. Do not duplicate from grammatical ambiguity alone.

PLACE: retain every materially differentiated source-established spatial support useful for locating represented material. Explicit broad settings, distinct contained/local positions, represented object/interaction locations, destinations, waiting scenes/positions, remembered/reported settings, later-conversation settings, and present-telling settings may qualify. Several relations may share one PLACE when support is not differentiated. A broad and contained PLACE may both qualify when source structure distinguishes them. Unnamed PLACE is lawful only when a distinct scene/support is clearly established but unnamed; use null source_wording and an exact source cue. Do not turn every physical noun, possession phrase, or locator phrase into PLACE.

TIME: retain materially differentiated source-established temporal support useful for reconnecting represented material: attempt/condition frames, help/response episodes, transition/departure phases, waits, intended periods, remembered/reported periods, later conversations/reports, recurring spans, present reflection, and explicitly represented future/prospective frames. TIME does not require a date/clock/temporal noun. Several relations may share one TIME. Unnamed TIME is lawful when a distinct frame is source-established but unnamed. Do not create TIME from tense, every transition word, or every predicate occurrence.

PERSON: retain the speaker plus every distinct represented human/social actor or stable group after true coreference when the actor participates, anchors, is related to, is remembered/reported in, benefits from, possesses something material to, or otherwise becomes a represented actor coordinate. Direct, offscreen, relational, possessive/beneficiary, institutional, prospective, peripheral, and one-use actors may qualify. Reject nonreferential/rhetorical/generic person wording.

OBJECT: retain every materially represented independently selectable concrete or abstract thing/content handle. Concrete things, source-distinguished parts, amounts/values, services/results, decisions/next steps when treated as things, contemplated alternatives when treated as selectable choices, recurring relations treated as content, named sets/categories, remembered/reported content, and internal represented objects may qualify. Do NOT create OBJECT from every argument, pronoun, generic this/that/it, clause complement, question content, explanation, proposition wrapper, discourse point, or meta-reference. An action/clause is OBJECT only when the source itself treats it as a selectable thing/content node.

LABEL: retain each independently selectable source-applied characterization, quality/state, status, identity, evaluation, comparison, self-label, candidate label, rejection, correction, contrast, or materially expressed posture. Preserve legitimate local/colloquial/idiomatic/questioned/negated/uncertain/corrected/rejected/figurative characterizations. Use the shortest complete exact source form carrying the judgment. Keep one natural judgment together. Reject rhetorical color, generic descriptive flourish, manner wording, detached intensifiers, and modifier fragments that do not stand as characterizations.

VERB: source happenings and relations are independently inventoryable. Retain materially represented lexical predicate increments in source order at natural complete grain. Actions, states, cognitions, perceptions, reports/communications, intentions, question relations, decisions, possessions, comparisons, evaluations, movements, transitions, gestures, existence/location, obligations, recurrence, and other represented relations may qualify. Preserve particles/reflexives/negation/modality/bound complements when identity requires them. Split matrix/embedded or coordinated predicates only when they perform genuinely different independently selectable relation jobs; keep natural bound/coordinated constructions together when one source-native relation. Reject pure auxiliaries, discourse/filler predicates, whole-clause wrappers, duplicate restatements, and lexical fragments nested inside a stronger complete predicate.

LOCATOR: retain materially useful independently selectable spatial/directional/containment/path/proximity/movement/accompaniment/origin-destination/entry-exit/recurrence-context/internal-relational or materially spatialized figurative orientation. Use the smallest complete meaningful exact source construction, not an isolated preposition. A LOCATOR may coexist with PLACE or VERB when it has its own orientation job and need not be indispensable to a compound. Reject every-PP behavior, recipient/topic/purpose/possession/degree/temporal complements, generic adverbials, isolated here/there, and rhetorical location wording without an independent orientation function.

LITERAL LOCK: preserve exact source wording, colloquial language, dialect, spelling/grammar, idiom, figurative wording, negation, modality, uncertainty, question form, attribution, comparison, remembered/reported posture, hypothetical/prospective posture, correction, and rejection. Every non-null source_wording/source_cue/order_cue must be exact source text. Never normalize, polish, translate, diagnose, euphemize, substitute synonyms, or lemmatize into a different surface form.

PRIMITIVE FREEZE AUDIT:
1) replay the whole source in order;
2) verify each requested ledger at its own class grain;
3) restore valid local/one-use coordinates omitted only because they were not globally salient or indispensable to a compound;
4) remove unsupported inference, grammatical/discourse wrappers, generic deictics, proposition/clause wrappers without independent class function, internal fragments, and true duplicates;
5) arbitrate OBJECT/LABEL/VERB/LOCATOR by represented job;
6) verify materially differentiated PLACE/TIME support including legitimate unnamed support;
7) verify natural complete spans, literal lock, coreference, class-local distinctness, and first-establishment order;
8) freeze primitives. Never target hidden counts or infer hidden gold.

COMPOUNDS — STRICTER THAN PRIMITIVES. Build compounds only after primitive freeze. A valid primitive may remain unbundled. Emit a compound only when two or more frozen coordinates jointly form one materially complete lightweight researcher binding. Include only participating refs; use enough refs to preserve the binding without unrelated context; split when participant set, target/content, support frame, posture, or materially distinct judgment/action changes enough that one bundle would blur structure; group locally joint predicates when they form one binding. Do NOT create one compound per primitive, predicate token, clause, sentence, or arbitrary co-occurrence. Do NOT emit subset/superset variants, graph closure, all-pairs links, scene mega-bundles, support chains, singleton equivalents, or duplicate restatements.

If another generic apparatus sentence broadly asks for every represented predicate relation, THIS V119 COMPOUND GRAIN CONTROLS: serialize materially complete lightweight researcher bindings, not an exhaustive relation/proposition census.

qualities_available is a yes/no availability flag only. Do not replace LABEL rows with Q and do not explode qualities into APA analysis.

Never expose approved archetypes, expected counts, evaluator findings, prior scored outputs, calibration answers, canonical gold extracts, or sealed holdout material. Never perform promotion, Oval Office admission, APA-ID creation, sovereign/admitted writing, APA scoring, psychological interpretation, or APA database mutation.
'''.strip()

V119_BASE_RULES = APPARATUS_BASE_RULES + "\n\n" + V119_CORRECTION
V119_CLASS_RULES = dict(APPARATUS_CLASS_RULES)
V119_CLASS_RULES.update({
    "PLACE": "Return every materially differentiated source-established spatial SUPPORT coordinate useful for literal researcher reconnection, not only places indispensable to a compound. Explicit broad settings, distinct contained/local support, object/interaction locations, destinations, waits, later settings, and present-telling support may qualify. Share support when not differentiated. Unnamed support is allowed only when source-established; use null source_wording and exact cue. Do not promote every physical noun or locator phrase.",
    "TIME": "Return materially differentiated source-established temporal SUPPORT coordinates useful for reconnection, including attempts/conditions, response episodes, transitions, waits, intended periods, reported/remembered periods, later conversations/reports, recurring spans, present reflection, and future/prospective frames. Do not require a clock/date or compound indispensability. Do not promote tense, every transition word, or every predicate occurrence.",
    "PERSON": "Return speaker plus every distinct represented human/social actor or stable group after true coreference when represented as participant, anchor, relation endpoint, remembered/reported actor, possessor/beneficiary, institutional actor, prospective actor, peripheral actor, or one-use actor. Reject only nonreferential/rhetorical/generic person wording.",
    "OBJECT": "Return materially represented independently selectable concrete or abstract THING/CONTENT handles: things/parts, values, services/results, decisions/next steps treated as things, choices treated as choices, recurring relations treated as content, named sets/categories, remembered/reported content, and internal represented objects. Reject pronouns/generic deictics, every grammatical argument/complement, clause/proposition wrappers, explanations, discourse points, and meta-references unless the source itself reifies them as selectable content.",
    "LABEL": "Return independently selectable source-applied characterizations/states/statuses/identities/evaluations/comparisons/self-labels/candidate labels/rejections/corrections/contrasts at the shortest complete natural source grain. Preserve local, colloquial, idiomatic, questioned, negated, uncertain, corrected, rejected, and figurative labels. Reject rhetorical color, detached intensifiers/modifiers, generic description, and manner fragments without a characterization job.",
    "VERB": "Return materially represented independently inventoryable lexical predicate increments in source order at natural complete grain. Preserve bound particles/reflexives/negation/modality/complements when identity requires them. Split only genuinely different predicate jobs; keep one natural bound/coordinated relation whole. Retain questioned/negated/hypothetical/intended/reported/remembered/recurring/prospective relations without asserting occurrence. Reject auxiliaries, filler, whole-clause wrappers, duplicates, and fragments nested inside stronger predicates.",
    "LOCATOR": "Return materially useful independently selectable orientation/context spans: position, path, origin/destination, direction, containment, proximity, movement, accompaniment, entry/exit, recurrence/context, internal/relational, or materially spatialized figurative orientation. A locator may coexist with PLACE/VERB and need not be compound-indispensable. Reject every-PP behavior, recipient/topic/purpose/possession/degree/temporal complements, generic adverbials, isolated here/there, and nonfunctional location metaphors.",
})
