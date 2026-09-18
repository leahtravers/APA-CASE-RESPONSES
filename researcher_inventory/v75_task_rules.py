"""V75 semantic task rules: episode-anchor completeness, shell dereferencing, independent-job overlap, relation grain, and locator discipline."""

V75_BASE_RULES = r'''
V75 ARCHETYPAL LIGHTWEIGHT RULE: read the complete source and recover its represented research-coordinate map at natural source-native grain. Lightweight is neither a narrative summary nor a word/phrase census.

FIRST reconstruct source-order EPISODES/SCENES, PEOPLE/REFERENTS, BINDINGS, and PLACE/TIME anchors. THEN extract classes.

ADMIT a primitive only when it has source grounding, performs a real class job, names one distinct represented coordinate (node/frame/value/relation/orientation), uses the smallest semantically complete natural source span, and is not a true alias/support-shell/alternate-decomposition duplicate.

DO NOT use narrative importance as a gate. Minor, one-off, background, reported, hypothetical, prospective, and scene-detail coordinates may qualify. DO NOT use explicit wording as entitlement: every noun phrase, modifier, predicate token, temporal cue, preposition, or clause fragment is not automatically a unit.

EPISODE-ANCHOR COMPLETENESS: a materially distinct interaction scene or action stage may require its own supported unnamed PLACE and/or TIME even when no place/time noun is stated. Distinguish stages by meaningful changes in participant configuration, setting, action regime, wait/transition state, remembered/reported scene, prospective scene, or present-telling frame. Use episode granularity, not one global anchor and not one anchor per clause.

PLACE/TIME are represented occurrence-position and episode/frame coordinates. Named and supported unnamed anchors may coexist at broad/local levels when they locate distinct represented material. Spatial/temporal cue words are evidence, not automatically PLACE/TIME.

COREference collapses true aliases but does not erase minor/indirect/possessive actors or referents. If a later source-native mention gives a clearer stable identity for the same coordinate, it may name the coordinate while order remains tied to first establishment.

OBJECT coverage is broad at natural referent grain. But DEREFERENCE DISCOURSE SHELLS: generic shells such as point/part/thing/fact/idea/issue are not OBJECT merely because they point at nearby proposition/relation/choice content. Omit the shell when it only indexes content represented elsewhere and has no independent stable identity; keep it only when the source treats that reified shell/content as a stable thing with its own downstream bindings.

LABEL preserves source-staged characterization/state/evaluation/classification/correction/rejection values at natural value grain, including uncertainty/negation/question when part of the value. Do not inventory every modifier.

VERB preserves represented lexical actions/relations at the smallest semantically complete source-native grain. Include particles/reflexives/lexical complements when relation identity requires them. Do not absorb independently represented complement content merely to make a longer verb span: if the complement independently qualifies as state/object/label/proposition-content/subordinate event, keep the predicate relation at natural grain and represent the complement separately. Keep coordinated actions together only when source presents one inseparable action/result relation.

LOCATOR requires a genuine orientation/location job: position, containment, path, direction, origin/destination, accompaniment, embodied/internal orientation, or relative location. A phrase is not LOCATOR merely because it contains to/for/about/with/of/at or another preposition. Beneficiary, topic, recipient, purpose, possession/association, self-directed argument, and ordinary verb complements belong in their semantic bindings unless they independently express where/which-way/from/to/relative-position orientation. Movement/directional particles may qualify when they materially encode action geometry.

TYPE by represented semantic job. Cross-class overlap is conservative, but DO NOT suppress overlap when the same source material genuinely performs two independent useful represented jobs. Each projection should remain a distinct useful coordinate if the other disappeared. Grammar-only ambiguity does not justify overlap.

LITERAL LOCK: every non-null source_wording, source_cue, order_cue, and source-derived short tag must preserve source language exactly. Do not normalize spelling, dialect, punctuation, contractions, numbers, question, negation, uncertainty, attribution, correction, or figurative wording. Only genuinely unnamed PLACE/TIME may use null source_wording with exact cue.

PRIMITIVE FREEZE uses TWO passes: (1) COVERAGE — look for omitted minor actors, scene objects, broad/local/unnamed positions, distinct episode frames, source-staged values, minor/reporting actions, and meaningful orientations; explicitly check each distinct interaction/action stage for adequate anchors. (2) ANTI-CENSUS — remove cue tokens, arbitrary noun subparts, modifier inflation, auxiliary/support fragments, discourse-shell objects without identity, proposition wrappers, non-orientational prepositional complements, alias duplicates, and cross-class duplicates with no separate job.

COMPOUNDS are canonical source bindings. After primitives freeze, re-read in source order. For each distinct represented binding make one complete local compound containing its relation-bearing VERB/LABEL/LOCATOR coordinate(s), all actually co-bound PERSON/OBJECT/value coordinates, and applicable PLACE/TIME episode anchors. Do not emit one compound per primitive, pairwise subsets, alternate decompositions, mere co-occurrence bundles, or giant scene-wide bundles.

FINAL AUDIT: broad coordinate coverage without materiality pruning; correct episode anchors without clause inflation; discourse shells dereferenced; valid independent-job overlap preserved; relation spans do not swallow independent complement content; LOCATOR means real orientation; exact source wording; canonical binding compounds; candidate-only status; sealed holdout isolation.

Never target hidden counts or infer gold. Never interpret APA, promote records, mint APA IDs, or access the sealed holdout during calibration.
'''.strip()

V75_CLASS_RULES = {
    "PLACE": r'''PLACE = represented physical setting/occurrence-position for an episode, participant/object configuration, destination, wait, remembered/reported/prospective interaction, or present telling. Keep broad/local and supported unnamed positions when each locates distinct represented material. A distinct source scene can require an unnamed PLACE without an explicit place noun. Do not turn every spatial/deictic token, surface, path fragment, or direction word into PLACE.'''.strip(),
    "TIME": r'''TIME = represented episode/period/stage/wait/recurrence/remembered-reported/prospective/present-telling frame. Keep distinct local frames for genuinely distinct interaction/action stages even without explicit temporal wording. Do not create one TIME per clause or cue; a sequence word, duration, tense, adverb, or predicate is not automatically TIME.'''.strip(),
    "PERSON": r'''PERSON = B plus every represented human/social actor or stable group after true coreference, including minor, possessive, indirect, offscreen, reported, remembered, prospective, or comparison actors. Exclude only non-referential rhetorical/generic addressees.'''.strip(),
    "OBJECT": r'''OBJECT = represented concrete/abstract thing or reified referent at natural grain. Keep real scene/background things, products, documents, parts, amounts, plans/choices, relations/situations, mental referents, categories, and comparison vehicles. Do not atomize every noun phrase. Generic discourse shells that merely point to already represented content are not OBJECT unless the shell/reified content has independent stable identity and downstream binding.'''.strip(),
    "LABEL": r'''LABEL = represented characterization/state/evaluation/classification/comparison/correction/rejection/status value at natural source-native grain. Preserve separately staged values and their uncertainty/negation/question posture. Do not inventory every adjective/adverb/modifier.'''.strip(),
    "VERB": r'''VERB = represented lexical action/relation at its smallest semantically complete source-native grain. Include required particles/reflexives/lexical complements when they define relation identity. Do not swallow independently represented complement state/object/label/proposition/event content into the relation span; represent that content separately when it independently qualifies. Keep coordinated actions together only when one inseparable relation is represented.'''.strip(),
    "LOCATOR": r'''LOCATOR = complete source-native orientation/location relation: position, containment, path, direction, origin/destination, accompaniment, embodied/internal orientation, or relative position. Prepositional grammar alone is insufficient. Beneficiary/topic/recipient/purpose/possession/self-directed or ordinary verb complements are not LOCATOR unless they independently encode where/which-way/from/to/relative-position orientation.'''.strip(),
}
