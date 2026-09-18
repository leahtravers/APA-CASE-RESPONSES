"""V77 semantic task rules: binding-first entitlement, one-job arbitration, removal test, and proposition-led compounds."""

V77_BASE_RULES = r'''
V77 ARCHETYPAL LIGHTWEIGHT RULE: build the inventory by BINDING-FIRST ENTITLEMENT, never by mention-first census and pruning.

READ THE WHOLE SOURCE FIRST. Silently build: (1) materially distinct EPISODES, (2) materially distinct SOURCE-REPRESENTED PROPOSITIONS/RELATIONS, (3) the independent semantic ROLES required by each selected proposition, and (4) PLACE/TIME ANCHORS needed to locate those propositions. Do not make primitive candidates before the proposition ledger exists.

SELECT a proposition only when losing it would erase a distinct represented relation/state a researcher could later reconnect. A clause/predicate token is not automatically a proposition. Suppress auxiliary/support grammar, generic narration/discourse shells whose act is not materially staged, modifier-only support, and duplicate paraphrases. Minor one-off relations may still qualify; narrative importance is not the test.

A PRIMITIVE IS ENTITLED only by one of three routes:
A) BINDING ROLE — it fills an independent actor/referent/content/value/relation/orientation role in a selected proposition;
B) EPISODE ANCHOR — it is PLACE/TIME needed to locate selected proposition(s) or preserve a materially distinct frame;
C) STANDALONE IDENTITY — recurrence/coreference, later reference, explicit reification, possession/evaluation, comparison, choice/decision treatment, stable relational content, or another source relation establishes independent identity even without its own compound.
MERE MENTION IS NOT ENTITLEMENT. Explicitness, concreteness, vividness, grammatical completeness, or scene membership alone never suffices.

REMOVAL TEST: mentally delete each primitive. If every selected proposition, episode distinction, independent referent, staged value, and genuine orientation remains reconstructable without loss, SUPPRESS IT.

ONE-JOB ARBITRATION precedes overlap. Give a span/referent the class demanded by its represented role. Duplicate cross-class projections require genuinely independent jobs, not grammatical alternatives. Setting/occurrence position => PLACE. Episode frame => TIME. Reified content/choice/relation => OBJECT when independently treated as content. Directly asserted/questioned/rejected/comparison value => LABEL. Selected lexical relation edge => VERB. Independent orientation relation => LOCATOR. A noun/complement inside a relation is not OBJECT without independent entitlement.

PLACE: backchain selected propositions to physical occurrence positions. Keep separate PLACE only when replacing it with the broader available setting would lose a distinct represented position for an interaction, wait, destination, object configuration, remembered/reported/prospective scene, or present telling. Supported unnamed PLACE is allowed with null source_wording + exact cue. No PLACE from every surface/deictic/container/body-part/preposition/imagined destination.

TIME: retain only represented frames that scope or distinguish selected propositions: episode, period, wait, transition stage, recurrence, remembered/reported/prospective frame, present telling. Supported unnamed TIME is allowed when a distinct episode lacks explicit wording. No TIME from physical setting phrases, every clause, every sequence/adverb/tense marker, duration question, intended action, or predicate.

PERSON: B plus each represented human/social actor or stable group after coreference when the actor participates in a selected proposition or has source-established independent identity. Minor/offscreen/possessive/remembered/reported/prospective/comparison actors may qualify. Exclude nonreferential rhetorical/generic addressees.

OBJECT: concrete/abstract referent with independent identity. Strong entitlement: argument/content of a selected proposition; reidentified/coreferred later; explicitly possessed/evaluated/compared/selected; or treated as stable choice, decision, relationship, recurring situation, mental content, plan, amount, set, product/document/part, or comparison referent. A one-off scene noun is NOT automatically an OBJECT. Suppress relation-internal complements, spatial supports already doing PLACE/LOCATOR work, discourse shells, arbitrary subparts, aliases, and alternate decompositions unless independent entitlement survives the removal test.

LABEL: source-STAGED value/state/classification/evaluation/comparison/correction/rejection/status. It must be meaningfully asserted, questioned, rejected, compared, or foregrounded as a value. Ordinary noun-modifying/adverbial texture is not enough. Preserve question/negation/uncertainty/correction/comparison posture and shortest complete source-native value.

VERB: lexical relation edge that carries a selected proposition. Use the smallest complete source-native lexical relation; keep required particle/reflexive/idiomatic material only when removing it changes relation identity, but do not absorb whole clausal complements. Suppress auxiliaries/support/aspect fragments, duplicate local restatements, generic narration/report shells whose reporting act is not selected, and predicates with no independent proposition.

LOCATOR: orientation relation that independently positions/path-links retained material: relative position, containment, direction, origin/destination, path, proximity, accompaniment, embodied/internal orientation. Mere prepositional grammar is not enough. Beneficiary/topic/recipient/purpose/possession/evidentiary-source/ordinary idiom arguments are not LOCATOR unless a genuine orientation job survives the removal test.

LITERAL LOCK: preserve source-derived strings character-for-character where schema requires source text. No synonym, repair, normalization, number change, expanded contraction, punctuation cleanup, or inferred wording. Only genuinely unnamed PLACE/TIME may use null source_wording with exact source cue.

PRIMITIVE FREEZE ORDER: (1) binding-role coverage; (2) anchor backchain; (3) standalone-identity check; (4) one-job arbitration; (5) removal test; (6) literal lock. Compounds cannot add/repair primitives.

COMPOUNDS COME FROM THE PROPOSITION LEDGER, NOT THE PRIMITIVE LIST. For each selected proposition emit one complete local compound containing its defining VERB/LABEL/LOCATOR relation primitive(s), every frozen PERSON/OBJECT/value with an independent role in that proposition, and the most specific applicable PLACE/TIME anchor(s). Do not make a compound merely because a primitive exists. No pairwise subsets, partial duplicates, alternate decompositions, token-by-token compounds, support bundles, or scene-wide mega-bundles.

FINAL ENTITLEMENT AUDIT: for every primitive identify exactly which selected proposition, necessary episode anchor, or standalone-identity rule entitles it. If none, delete it. For every compound identify exactly one selected proposition it serializes. If none, delete it. Then verify source order, coreference, type arbitration, qualities flags, literal strings, candidate-only status, and sealed-holdout isolation.

Never target hidden counts or infer gold. Never interpret APA, promote records, mint APA IDs, or access the sealed holdout during calibration.
'''.strip()

V77_CLASS_RULES = {
    "PLACE": r'''PLACE is a physical occurrence-position entitled by selected proposition(s) or a materially distinct episode. Backchain after proposition selection. Keep a separate place only when broader setting substitution would lose a distinct represented position. Supported unnamed place is allowed. Mention/deictic/surface/container/preposition alone is not entitlement.'''.strip(),
    "TIME": r'''TIME is a represented frame that scopes/distinguishes selected proposition(s): episode, period, wait, transition stage, recurrence, remembered/reported/prospective frame, or present telling. Supported unnamed frame may qualify. Clause sequence, physical place wording, adverb/tense, duration question, intended action, or predicate alone is not entitlement.'''.strip(),
    "PERSON": r'''PERSON is B plus each represented human/social actor or stable group after coreference when it participates in a selected proposition or has source-established independent identity. Minor/offscreen/possessive/remembered/reported/prospective/comparison actors may qualify; rhetorical/generic addressees without actor identity do not.'''.strip(),
    "OBJECT": r'''OBJECT is an independently represented concrete/abstract referent: proposition argument/content, reidentified/coreferred item, explicitly possessed/evaluated/compared/selected content, or stable reified choice/decision/relationship/situation/mental content/plan/amount/set/product/document/part/comparison referent. Mere one-off scene mention, relation-internal noun, spatial support, discourse shell, arbitrary subpart, or alias is not entitlement.'''.strip(),
    "LABEL": r'''LABEL is a source-staged value/state/classification/evaluation/comparison/correction/rejection/status that is asserted, questioned, rejected, compared, or foregrounded. Ordinary descriptive texture/modifier wording is not enough. Preserve exact source posture and shortest complete source-native value.'''.strip(),
    "VERB": r'''VERB is the source-native lexical relation edge carrying one selected proposition. Use smallest complete lexical grain; include required particle/reflexive/idiomatic material only when relation identity needs it. Suppress auxiliaries/support/aspect fragments, duplicate restatements, generic narration/report shells, and predicates that carry no selected proposition.'''.strip(),
    "LOCATOR": r'''LOCATOR is an independently useful orientation relation that positions/path-links retained material: relative position, containment, direction, origin/destination, path, proximity, accompaniment, embodied/internal orientation. Prepositional grammar, topic/recipient/purpose/beneficiary/possession/evidentiary-source/ordinary idiom argument alone is insufficient.'''.strip(),
}
