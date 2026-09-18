"""V86 semantic task rules: proposition-anchored represented coordinates and canonical local bindings."""

V86_BASE_RULES = r'''
V86 ARCHETYPAL LIGHTWEIGHT RULE: recover REPRESENTED RESEARCH COORDINATES AND LOCAL SOURCE-PROPOSITION TOPOLOGY. The target is broader than semantic summary and narrower than token/grammar/preposition census.

READ THE WHOLE SOURCE FIRST.

PASS A — SOURCE PROPOSITION MAP: silently map local source propositions/events/states/orientations in source order. For each, identify represented participants/referents, content-bearing lexical relations, explicitly staged values/states, setting/occurrence position, episode/period frame, and material orientation. This map is a construction aid only; do not turn every proposition into an OBJECT.

PASS B — PRIMITIVE PROJECTION: retain a coordinate when (1) the source explicitly names or directly stages it as a participant, referent, lexical relation, value/state, setting, episode/frame, or orientation; OR (2) it is a necessary unnamed PLACE/TIME support frame that prevents a materially distinct source event/scene from collapsing into another. Low salience, one-use status, ordinary wording, reporting, memory, prospectivity, uncertainty, negation, or figurative form do not disqualify a source-established coordinate.

REJECT only aliases/coreferential duplicates; function grammar or auxiliary support with no distinct relation; analyst-created nominalizations of clauses/propositions; modifier fragments already carried as qualities and not separately staged values; telling-management metadiscourse; automatic class shadows; duplicate/alternate tokenizations.

DO NOT use salience, frequency, dramatic importance, or standalone conceptual interest as an admission test.

PLACE: represented physical/institutional settings and source-supported occurrence positions. Retain broad and contained explicit settings when both are represented. Reconstruct unnamed PLACE (source_wording null, exact source_cue) for materially distinct interactions, waits, reports, remembered scenes, comparisons, or present-telling/reflection scenes when occurrence position would otherwise disappear or merge. Do not turn every spatial noun/object position/path/distance/figurative expression into PLACE.

TIME: represented event/episode/period frames at the grain needed to distinguish local source propositions. Retain/reconstruct attempts, help episodes, departures, waits, reports, recurring periods, relationship periods, future recurrence, comparisons, present reflection/telling, and other materially distinct phases. Nested TIME is allowed when source clearly stages a distinct local event phase. Do not inventory tense or every duration/frequency/sequencing word as TIME.

PERSON: retain B plus every distinct represented human/social actor or stable group after true coreference, including minor, relational, offscreen, remembered, reported, prospective, and institutional actors. Suppress only true aliases and nonreferential/rhetorical addressees.

OBJECT: retain source-established concrete/abstract referents with identity as things/content: physical things, products/documents/parts, amounts/values, decisions, plans, relationships, recurring situations, comparison vehicles, and explicitly reified mental/content objects. DO NOT manufacture OBJECTs by nominalizing an event, clause, proposition, intention, question, or relation merely because it can be discussed. If clause work is carried by participant/relation/value/context coordinates, do not add a proposition-shell OBJECT. Low-salience one-use real referents remain eligible.

LABEL: retain explicitly staged source values, states, classifications, evaluations, comparisons, manners, corrections/rejections, identities, or statuses. Preserve question, negation, uncertainty, contrast, and intensity when part of the staged state. Do not suppress low-salience states. Do not create LABEL for every modifier; ordinary description may be qualities_available.

VERB: retain source-established content-bearing lexical relations/happenings that create represented relation/event edges, even when ordinary, one-use, reporting, cognition, asking/telling/saying, meaning, locating, helping, seeing, trying, deciding, waiting, or moving language. After admission, split separately predicated lexical relations to smallest complete relation grain. Suppress only genuine function/support material: pure auxiliaries, do-support, aspect/support verbs, empty copulas, and current-telling scaffolding with no represented relation. A copular form may qualify when it carries a real locative, identity, modal/obligation, or state relation not already fully represented elsewhere. Preserve particles, negation, reflexives, and required complements when relation identity requires them.

LOCATOR: retain explicit source-native orientation attached to represented coordinates/relations: position, containment, origin/destination, direction, path, proximity/distance, accompaniment, carrying, temporal/contextual orientation, or represented figurative/comparative orientation. A locator need not remain independently interesting after broad PLACE/TIME is known; retain it when removing it discards represented where/whither/relative-position information. Do not inventory every preposition or discourse connective.

CROSS-CLASS: overlap only when wording performs distinct research jobs in source topology. Never create automatic class shadows from part of speech or surface spatial/temporal wording.

LITERAL LOCK: preserve source language character-for-character for source-derived non-null fields where schema requires source text. No synonym substitution, grammar repair, dialect normalization, number changes, contraction expansion, or punctuation cleanup. Only genuinely unnamed PLACE/TIME support frames may use null source_wording, with exact source_cue.

ORDER/COREFERENCE/QUALITIES: order by first source establishment after true coreference, with speaker-first PERSON and broad-before-contained setting navigation where source supports it. qualities_available is boolean only and does not force LABEL. Do not split true coreferents because wording changes.

FREEZE primitives before compounds.

COMPOUNDS — PROPOSITION ANCHORED: return canonical local bindings from the source proposition map. For each materially represented local proposition/state/orientation, include its frozen relation/value/orientation anchor, participating PERSON/OBJECT coordinates, and material PLACE/TIME/LOCATOR coordinates. Include multiple lexical relations in one compound only when source presents one inseparable local event/course; otherwise split separately predicated relations. No pairwise closure, subset variants, alternate tokenizations, whole-scene mega-bundles, duplicate compounds, or cross-proposition bundles.

FINAL AUDIT: did every materially distinct local proposition preserve participant/relation/context topology? Did ordinary content-bearing relations disappear as 'unimportant'? Did I invent proposition-shell OBJECTs or class shadows? Did distinct event phases lose necessary PLACE/TIME? Did explicit low-salience values/states/orientations disappear? Are literal wording and coreference exact? Are compounds canonical local proposition bindings from frozen primitives?

Never target hidden counts or infer hidden gold. Never perform APA scoring, psychological interpretation, promotion, APA-ID creation, sovereign/admitted writing, or database mutation. Never access the sealed holdout during calibration.
'''.strip()

V86_CLASS_RULES = {
    "PLACE": r'''Project source-established physical/institutional settings and necessary occurrence positions. Preserve broad/contained settings and reconstruct unnamed interaction/wait/report/comparison/present-telling positions where a materially distinct scene would otherwise collapse. Do not inventory spatial vocabulary or object positions as PLACE by default.'''.strip(),
    "TIME": r'''Project source-established event/episode/period frames at the grain needed to distinguish local propositions, including nested attempts/help/departure/wait/report/recurring/future/comparison/present frames. Do not inventory tense or every temporal word.'''.strip(),
    "PERSON": r'''Retain B and every distinct represented human/social actor or stable group after true coreference, including minor, relational, offscreen, remembered, reported, prospective, and institutional actors. Suppress only aliases and nonreferential addressees.'''.strip(),
    "OBJECT": r'''Retain real source-established concrete/abstract referents, including low-salience physical things, amounts, decisions/plans/relationships, recurring situations, comparison vehicles, and explicitly reified contents. Reject analyst-created proposition-shell or clause-nominalization objects and automatic noun-phrase census.'''.strip(),
    "LABEL": r'''Retain explicitly staged source values/states/classifications/evaluations/comparisons/manners/corrections/rejections/statuses, including low-salience, questioned, negative, uncertain, or contrasted states. Do not make every modifier a LABEL.'''.strip(),
    "VERB": r'''Retain source-established content-bearing lexical relations even when ordinary, one-use, reporting, cognition, asking/telling/saying, meaning, locating, helping, trying, waiting, or moving. Split separately predicated relations after admission. Suppress only genuine function/support grammar and current-telling scaffolding without a represented relation.'''.strip(),
    "LOCATOR": r'''Retain explicit material orientation of represented coordinates/relations: position, containment, origin/destination, direction/path, proximity, accompaniment/carrying, temporal/contextual, or represented figurative/comparative orientation. It need not remain interesting after broad PLACE/TIME is known; reject only preposition/discourse census.'''.strip(),
}
