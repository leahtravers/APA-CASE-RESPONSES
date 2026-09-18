"""V78 semantic task rules: relational skeleton plus bounded coordinate completeness."""

V78_BASE_RULES = r'''
V78 ARCHETYPAL LIGHTWEIGHT RULE: recover RESEARCHER-RECONNECTABLE COORDINATE RESOLUTION. Do not summarize, and do not require every primitive to be indispensable to one proposition.

READ THE WHOLE SOURCE FIRST. Build two ordered representations:
(1) a RELATIONAL SKELETON of materially distinct episodes and source-represented propositions/relations for role understanding and compound construction; then
(2) a BOUNDED COORDINATE COMPLETENESS PASS across the full source for distinct PLACE, TIME, PERSON, OBJECT, LABEL, VERB, and LOCATOR coordinates.
The proposition skeleton guides structure but is NOT the exclusive primitive-admission gate.

A PRIMITIVE IS ENTITLED when the source establishes an independent researcher-reconnectable job as:
A) a distinct participant/referent/content coordinate;
B) a distinct physical or temporal/episode frame, including supported unnamed PLACE/TIME;
C) a staged value/state/quality/classification/evaluation/comparison/correction/rejection/status;
D) a distinct source-native lexical action/relation/event edge; or
E) a distinct position/direction/path/orientation relation.
A coordinate need not recur or be proposition-essential. One-off coordinates can qualify when distinctly represented.

BOUNDEDNESS: suppress auxiliaries/support grammar, determiners/glue, discourse filler with no represented job, true aliases/coreference duplicates, arbitrary unrepresented subparts, redundant alternate tokenizations of one lexical relation, and relation-internal grammatical fragments with no independent research job. Do NOT delete a coordinate merely because the proposition remains understandable without it.

TYPE BY SEMANTIC JOB, NOT SURFACE PART OF SPEECH. Physical position=>PLACE. Episode/period/frame=>TIME. Human/social actor/group=>PERSON. Concrete/abstract referent/content=>OBJECT. Staged state/value/quality/classification/evaluation=>LABEL. Lexical action/relation=>VERB. Positional/directional/orientation relation=>LOCATOR. A verbal-looking/participial span that primarily expresses a condition/state is LABEL; if it expresses an action/relation it is VERB. Multiple class projections require genuinely distinct research jobs, not grammatical alternatives.

PLACE: preserve broad and specific physical positions when both are distinctly represented. Include locations of interactions, waits, destinations, object positions/configurations, remembered/reported/prospective/comparison scenes, and present telling when source-established. Supported unnamed PLACE is allowed with null source_wording + exact cue. Do not create PLACE from every surface/container/body-part/preposition unless it is a distinct represented position.

TIME: preserve distinct represented episode/period/stage/wait/transition/recurrence/remembered/reported/prospective/comparison/present-telling frames. Broad episodes and distinct subepisodes may both qualify. Supported unnamed TIME is allowed. Do not create TIME from every clause, tense marker, transition token, or adverb when no distinct frame exists.

PERSON: B plus every distinctly represented human/social actor or stable group after coreference. Minor, possessive, offscreen, remembered, reported, prospective, relational, institutional/group, and comparison actors may qualify. Major action is not required. Exclude nonreferential generic/rhetorical addressees and true aliases.

OBJECT: preserve distinctly represented concrete or abstract referents/content at lightweight research resolution, including one-off scene entities when identifiable as research coordinates; reified actions/situations/relations; choices; decisions; plans; amounts; sets; mental contents; recurring situations; comparison vehicles; products/documents/parts; body/environment entities. Recurrence/proposition necessity is not required. Suppress pure grammatical shells, aliases, arbitrary unrepresented subparts, and noun fragments whose only job is syntactic completion.

LABEL: preserve source-staged states, qualities, classifications, evaluations, comparisons, corrections, rejections, manner/state descriptions, and statuses. Adjectival/adverbial/participial/nominal/verbal-looking wording can be LABEL when its semantic job is condition/value rather than action relation. Preserve question/negation/uncertainty/comparison/attribution/correction/intensity. Use shortest complete source-native span preserving the staged state/value.

VERB: preserve distinct source-native lexical action/relation/event edges at the smallest complete lexical grain. Include movement, possession, experience, cognition, speech/reporting, perception, intention, comparison, waiting, gesture, and other represented relations. Include required particles/reflexives/idiomatic material when identity needs them. Avoid redundant splitting of one relation. Suppress pure auxiliaries/support/aspect fragments.

LOCATOR: preserve distinct source-native orientation relations that position/path-link represented material: relative position, containment, direction, origin/destination, path, proximity, accompaniment, embodied/internal orientation, and comparable locating relations. It need not be proposition-essential but must have an independent orientation job. Do not retain a preposition merely because it is grammatical.

LITERAL LOCK: every source-derived non-null string must preserve source language character-for-character where schema requires source text. No synonym, repair, normalization, number change, contraction expansion, punctuation cleanup, inferred wording, or dialect cleanup. Only genuinely unnamed PLACE/TIME may use null source_wording with exact source cue.

PRIMITIVE FREEZE ORDER: (1) episode/proposition skeleton; (2) whole-source class-by-class coordinate completeness; (3) coreference/alias resolution; (4) semantic type arbitration; (5) exclusion audit for support/glue/duplicates/non-independent fragments; (6) literal lock. Compounds cannot add or repair primitives.

COMPOUNDS COME FROM THE PROPOSITION LEDGER AFTER PRIMITIVE FREEZE. For each materially distinct represented relation, emit a materially complete local compound containing its defining VERB/LABEL/LOCATOR relation primitives when applicable, represented PERSON/OBJECT/value roles, and applicable PLACE/TIME coordinates at lightweight resolution. Not every primitive needs its own compound. Do not emit arbitrary pairwise subsets, token-by-token compounds, incomplete fragments, redundant alternate decompositions, or scene-wide mega-bundles. Keep independently represented relations distinct even when they share a sentence.

FINAL AUDIT: every primitive must have an independent research job: referent identity, frame/setting identity, staged value/state, lexical relation, orientation, or distinct represented role. If its only job is grammar/support, delete it. Every compound must reconnect one materially distinct represented relation. Then verify source order, coreference, type assignment, qualities flags, literal strings, coordinate completeness, candidate-only status, and sealed-holdout isolation.

Never target hidden counts or infer gold. Never interpret APA, promote records, mint APA IDs, or access the sealed holdout during calibration.
'''.strip()

V78_CLASS_RULES = {
    "PLACE": r'''PLACE is a distinct source-established physical setting or occurrence position useful for reconnecting represented material. Preserve broad and specific positions when both are represented; supported unnamed places are allowed. Do not require proposition indispensability, but do require a real represented position rather than mere grammatical/spatial wording.'''.strip(),
    "TIME": r'''TIME is a distinct represented episode/period/stage/wait/transition/recurrence/remembered/reported/prospective/comparison/present-telling frame. Broad and nested frames may both qualify when materially distinguishable. Supported unnamed frames are allowed; mere tense/adverb/clause sequence is not enough.'''.strip(),
    "PERSON": r'''PERSON is B plus each distinctly represented human/social actor or stable group after coreference. Minor, possessive, offscreen, remembered, reported, prospective, relational, institutional/group, and comparison actors may qualify even without a major action. Merge true aliases; exclude nonreferential generic addressees.'''.strip(),
    "OBJECT": r'''OBJECT is a distinctly represented concrete or abstract referent/content at lightweight research resolution. One-off scene entities may qualify when they have identifiable research identity. Include reified actions/situations/relations, choices, decisions, plans, amounts, sets, mental content, comparison vehicles, products/documents/parts, body/environment entities. Suppress grammatical shells, aliases, arbitrary unrepresented subparts, and syntactic-completion fragments.'''.strip(),
    "LABEL": r'''LABEL is a source-staged state, quality, classification, evaluation, comparison, correction, rejection, manner/state description, or status. Adjectival/adverbial/participial/verbal-looking wording is LABEL when its semantic job is condition/value rather than action. Preserve exact posture and shortest complete source-native value.'''.strip(),
    "VERB": r'''VERB is a distinct source-native lexical action/relation/event edge. Preserve the smallest complete lexical grain and required particles/idiom material. Retain represented movement, possession, experience, cognition, speech, perception, intention, comparison, waiting, gesture, and other relations. Suppress auxiliaries/support/aspect fragments and redundant decomposition.'''.strip(),
    "LOCATOR": r'''LOCATOR is a distinct source-native orientation relation that positions or path-links represented material: relative position, containment, direction, origin/destination, path, proximity, accompaniment, embodied/internal orientation, or comparable locating relation. Proposition indispensability is not required; independent orientation work is.'''.strip(),
}
