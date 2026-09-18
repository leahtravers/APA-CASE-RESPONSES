"""V74 semantic task rules: broad represented-coordinate coverage at natural grain, not materiality pruning or phrase census."""

V74_BASE_RULES = r'''
V74 ARCHETYPAL LIGHTWEIGHT RULE: read the complete source and recover its represented research-coordinate map at natural source-native grain. Lightweight is neither a narrative summary nor a word/phrase census.

FIRST reconstruct source-order EPISODES/SCENES, PEOPLE/REFERENTS, BINDINGS, and PLACE/TIME anchors. THEN extract classes.

ADMIT a primitive only when it has source grounding, performs a real class job, names one distinct represented coordinate (node/frame/value/relation/orientation), uses the smallest semantically complete natural source span, and is not a true alias/support-shell/alternate decomposition duplicate.

DO NOT use narrative importance, durable importance, centrality, or emotional importance as a gate. Minor, one-off, background, ambient, reported, hypothetical, prospective, and scene-detail coordinates may qualify.

DO NOT use explicit wording as an entitlement. Do not make a unit from every noun phrase, adjective, predicate token, temporal cue, preposition, clause fragment, or parseable subphrase. Ask whether the candidate is one represented coordinate at the source's own grain or merely a grammatical/lexical piece of another coordinate.

PLACE/TIME are represented occurrence-position and episode/frame coordinates. Named and supported unnamed anchors may coexist at broad/local levels when they locate distinct represented material. Spatial/temporal cue words are evidence, not automatically PLACE/TIME.

COREference collapses true aliases but does not erase minor/indirect/possessive actors or referents. If a later source-native mention gives a clearer stable identity for the same coordinate, it may name the coordinate while order remains tied to first establishment.

OBJECT coverage is broad: source-present scene props/background things, products, documents, parts, surfaces/things, amounts, abstract/reified referents, plans/choices, internal/mental referents, comparison vehicles, and other represented things may qualify. But use the natural referent; do not atomize every noun phrase or nominalize every event.

LABEL preserves source-staged characterization/state/evaluation/classification/correction/rejection values at natural value grain, including uncertainty/negation/question when part of the value. Do not inventory every modifier.

VERB preserves represented lexical actions/relations at a semantically complete source-native grain. Minor/reporting/cognition/gesture/meta-telling actions may qualify when they establish their own represented relation. Do not split one relation into every predicate token. Include particles/complements/state phrases when needed for relation identity; omit auxiliaries, pure support grammar, aspect/attempt shells, and infinitival scaffolding when they add no separate represented relation.

LOCATOR preserves complete meaningful orientation/context relations (position, containment, path, direction, origin/destination, accompaniment, embodied/internal orientation, etc.) when orientation is a represented job. Do not inventory isolated prepositions, particles, deictics, or every contextual phrase.

TYPE by represented semantic job before overlap. Cross-class overlap is conservative and requires genuinely different research jobs, not grammatical ambiguity.

LITERAL LOCK: every non-null source_wording, source_cue, order_cue, and source-derived short tag must preserve source language exactly. Do not normalize spelling, dialect, punctuation, contractions, numbers, question, negation, uncertainty, attribution, correction, or figurative wording. Only genuinely unnamed PLACE/TIME may use null source_wording with exact cue.

PRIMITIVE FREEZE uses TWO passes: (1) COVERAGE — look for omitted minor actors, scene objects, broad/local/unnamed positions, distinct episode frames, source-staged values, minor/reporting actions, and meaningful orientations; do not prune them as incidental. (2) ANTI-CENSUS — remove cue tokens, arbitrary noun subparts, modifier inflation, auxiliary/support/attempt fragments, incomplete orientation fragments, proposition wrappers, alias duplicates, and cross-class duplicates with no separate job.

COMPOUNDS are canonical source bindings. After primitives freeze, re-read in source order. For each distinct represented binding make one complete local compound containing its relation-bearing VERB/LABEL/LOCATOR coordinate(s), all actually co-bound PERSON/OBJECT/value coordinates, and applicable PLACE/TIME episode anchors. Multiple relation primitives may share one compound if they form one inseparable binding. Do not emit one compound per primitive, pairwise subsets, nested partial duplicates, alternate decompositions, mere co-occurrence bundles, or giant scene-wide bundles. Do not omit applicable episode anchors just because they are implicit after the ledger is built.

FINAL AUDIT: broad coordinate coverage without materiality pruning; anti-census natural grain; correct class job; stable coreference; exact source wording; canonical binding compounds; candidate-only status; sealed holdout isolation.

Never target hidden counts or infer gold. Never interpret APA, promote records, mint APA IDs, or access the sealed holdout during calibration.
'''.strip()

V74_CLASS_RULES = {
    "PLACE": r'''PLACE = represented physical setting/occurrence-position for an episode, participant/object position, destination, wait, remembered/reported/prospective interaction, or present telling. Keep broad/local and supported unnamed positions when each locates real represented material. Do not turn every spatial/deictic token, surface, path fragment, or direction word into PLACE.'''.strip(),
    "TIME": r'''TIME = represented episode/period/stage/wait/recurrence/remembered-reported/prospective/present-telling frame. Keep distinct local frames when the source actually presents distinct stages. A sequence word, duration, clock phrase, tense, adverb, infinitive, question about duration, or predicate is not automatically TIME; it must anchor a represented frame.'''.strip(),
    "PERSON": r'''PERSON = B plus every represented human/social actor or stable group after true coreference, including minor, possessive, indirect, offscreen, reported, remembered, prospective, or comparison actors. Do not discard a real actor because the mention is possessive or one-off. Exclude only non-referential rhetorical/generic addressees.'''.strip(),
    "OBJECT": r'''OBJECT = represented concrete/abstract thing or reified referent at natural grain. Scene props/background things, products, documents, parts, surfaces/things, amounts, plans/choices, relations/situations, mental/internal referents, categories, and comparison vehicles may qualify even when minor. Do not atomize every noun phrase or create event objects that merely restate a VERB/frame. Collapse true aliases to the most stable source-native identity.'''.strip(),
    "LABEL": r'''LABEL = represented characterization/state/evaluation/classification/comparison/correction/rejection/status value at natural source-native grain. Preserve separately staged candidate/rejection/correction values and their uncertainty/negation/question posture. Do not inventory every adjective/adverb/modifier. Reified noun-like referents stay OBJECT when thing identity is primary.'''.strip(),
    "VERB": r'''VERB = represented lexical action/relation at its smallest semantically complete source-native grain. Preserve distinct movement, experience, cognition, speech/reporting, perception, intention, gesture, meta-telling, possession, waiting, and other relations even when minor. Do not split one relation into every parseable predicate. Include required particles/complements/state phrase when bare wording would under-specify the relation; omit auxiliary/support/aspect/attempt scaffolding when it adds no separate binding.'''.strip(),
    "LOCATOR": r'''LOCATOR = complete source-native orientation/context relation that positions, contains, directs, originates, terminates, accompanies, or otherwise orients a retained coordinate/binding. Keep physical/figurative path, position, containment, direction, origin/destination, accompaniment, embodied/internal orientation when independently represented. Use a complete meaningful construction, not isolated prepositions/particles/deictics or every contextual phrase.'''.strip(),
}
