"""V107 neutral apparatus rules: independent source-addressability.

These rules contain no archetype answers, evaluator findings, expected counts,
prior scored outputs, calibration answers, or holdout material.
"""
from researcher_inventory.inventory_apparatus import BASE_RULES as APPARATUS_BASE_RULES, CLASS_RULES as APPARATUS_CLASS_RULES

V107_CORRECTION = r'''
V107 PROSPECTIVE CORRECTION — INDEPENDENT SOURCE-ADDRESSABILITY AT NATURAL CLASS-NATIVE GRAIN.

READ THE WHOLE SOURCE FIRST. Build silent maps of represented frames/phases, people, referential/content handles, predicate/relation identities, characterizations, PLACE/TIME support, and orientations. These maps are omission/reconciliation tools. They do not generate rows mechanically and do not impose a minimum-summary filter.

INDEPENDENT SOURCE-ADDRESSABILITY GATE: admit a source-present coordinate when it has a complete class-native semantic identity that the source itself presents as separately addressable within represented structure. It need not be globally necessary, recurrent, central, high-salience, compound-bound, or important to the worker's summary. Local, one-use, mundane, nested, remembered, reported, prospective, subtle, concrete, abstract, figurative, simple-relation, and neutral-support coordinates remain eligible when independently established.

MINIMALITY IS SPAN + IDENTITY ONLY. Use the smallest complete literal source-native span for one coordinate and merge true aliases/coreference/same-function repeats. Do NOT minimize the number of distinct source coordinates. A broader frame, phrase, relation, or future compound does not absorb a smaller independently established coordinate. Conversely, lexical separability, part of speech, describability, vividness, grammatical predication, or possible analyst usefulness never suffices by itself.

PRESERVE COMPONENTS WITHOUT TOKEN CENSUS. When one span presents several independent semantic jobs, retain each qualifying class-native coordinate. Do not split auxiliaries, tense/aspect support, determiners, complementizers, bare argument markers, idiom pieces, or arbitrary noun/modifier/preposition fragments lacking independent semantic identity.

VERB RELATION-IDENTITY TEST: retain the smallest complete predicate/relation kernel whenever the relation itself is separately represented. Simple, speech/reporting, cognition, perception, possession, state, comparison, movement, response, question, intention, or evaluation relations may qualify. Do not use importance or a driver-versus-carrier label as a keep/drop gate. Reject only pure auxiliaries/support grammar, discourse-only organizers, redundant restatements, grammatical copular shells whose semantic work is exhausted elsewhere, and proposition wrappers with no independent predicate identity.

PLACE/TIME EPISODE SUPPORT: first identify source-differentiated scenes/phases, then preserve each distinct explicit or legitimate unnamed support coordinate that distinguishes them. Broad and local support may coexist when they do different source-presented work. Merge multiple cues for one support identity. Never infer geography/chronology and never convert every physical noun/spatial phrase/temporal word/tense/duration/action into PLACE/TIME.

FUNCTION BEFORE FORM:
- source-established human/social actor or stable group -> PERSON;
- source-established concrete/abstract/internal/relational/content handle treated as trackable -> OBJECT;
- source-present characterization/state/identity/comparison/question/correction/polarity/manner/posture -> LABEL;
- location/scene support -> PLACE;
- episode/period/phase support -> TIME;
- independently represented predicate/relation identity -> VERB;
- independently represented orientation -> LOCATOR.
Surface grammar does not decide class. Cross-class overlap is allowed only when each projection preserves a genuinely different class-native job.

ATOMIC SPAN + LITERAL LOCK: after admission and class resolution, choose the smallest complete exact source-native span. Preserve required particles/prepositions, reflexives, essential complements, negation, modality, uncertainty, questions, attribution, comparison, idiom/dialect, and hypothetical/prospective/reported/corrective posture. Never normalize, paraphrase, clean up, lemmatize into a different surface form, or substitute synonyms. Neutral mechanical tags are reserved only for legitimate unnamed PLACE/TIME support and must be anchored by exact source cues.

OMISSION-FIRST, THEN EXCESS AUDITS:
1. whole-source frame/map coverage;
2. omission-first independent-addressability scan;
3. PLACE/TIME episode-support recovery;
4. VERB relation-identity recovery;
5. functional class correction and genuine cross-class overlap check;
6. atomic-span correction;
7. excess removal for grammar-only support, arbitrary lexical fragments, stylistic color without independent identity, and analyst invention;
8. literal lock;
9. semantic deduplication.
Repeat until stable before compounds.

RELATION-INSTANCE COMPOUNDS REMAIN DOWNSTREAM. Freeze all seven primitive classes first. Then emit only distinct source-presented relation instances connecting two or more frozen coordinates, using the smallest complete set of refs for each relation and preserving source direction/posture. Nested or overlapping compounds may coexist when they encode genuinely different source-presented relations. No graph closure, every-pair closure, one-compound-per-primitive/clause, arbitrary co-occurrence bundles, singleton equivalents, subset/superset permutations, duplicate restatements, or scene mega-bundles. Compounds never justify primitive defects.

Never target hidden counts or infer hidden gold. Never expose approved archetypes, evaluator findings, prior scored outputs, calibration answers, or sealed holdout material. Never perform promotion, Oval Office admission, APA-ID creation, sovereign/admitted writing, or database mutation.
'''.strip()

V107_BASE_RULES = APPARATUS_BASE_RULES + "\n\n" + V107_CORRECTION
V107_CLASS_RULES = dict(APPARATUS_CLASS_RULES)
V107_CLASS_RULES.update({
    "PLACE": (
        "Retain each distinct source-established physical setting or scene-support coordinate needed to locate represented material. Broad and contained/local support may coexist when they distinguish different source-presented scenes or levels. "
        "One-use and supported unnamed places may qualify. For unnamed PLACE use source_wording null, an exact source_cue, and a neutral navigation tag. Reject physical objects and spatial wording whose actual job is referential or orienting rather than scene support."
    ),
    "TIME": (
        "Retain each distinct source-established episode, phase, span, recurrence period, remembered/reported interval, intended/hypothetical/prospective interval, transition phase, or present-telling/reflection frame. "
        "Merge multiple cues for one phase; broad and contained times may coexist when the source differentiates them. For unnamed TIME use source_wording null, an exact source_cue, and a neutral episode tag. Reject tense morphology, temporal-word census, and one-TIME-per-action behavior."
    ),
    "PERSON": (
        "Retain the speaker and every distinct source-established human/social actor or stable group after true coreference, including one-use, background, possessive, remembered, reported, institutional, relational, addressee, and prospective actors. "
        "Independent action or narrative centrality is not required. Suppress aliases/coreference and rhetorical/nonreferential addressees."
    ),
    "OBJECT": (
        "Retain every distinct source-established concrete, abstract, internal, relational, decision/choice-like, value-like, set/category, represented-content, or figurative referential handle that the source treats as trackable. "
        "Mundane, nested, and one-use handles may qualify. Larger content phrases do not absorb smaller independently tracked handles, and smaller handles do not suppress separately reified larger content. Reject noun census, generic pronouns/deixis, incidental wording, discourse organizers, and proposition wrappers without separate referential identity."
    ),
    "LABEL": (
        "Retain each distinct source-presented characterization, state, identity, comparison, candidate/question label, correction, acceptance/rejection, polarity response, evaluation, manner, or posture at the smallest complete literal span. "
        "Local, one-use, idiomatic, figurative, comparative, uncertain, negated, and colloquial characterizations may qualify. Reject modifier/intensifier/colorful-language census and wording with no independent characterization job."
    ),
    "VERB": (
        "Retain each distinct smallest complete source-supported predicate/relation identity: action, state, possession, perception, communication/report, cognition, intention, question, transition, movement, comparison, evaluation, location relation, or other source-presented predicate. "
        "Test outer/embedded, serial, coordinated, reporting, speech, cognition, perception, possession, simple, and state predicates relation-by-relation for independent identity. Do not use an importance-based driver/carrier gate. Exclude pure auxiliaries, tense/aspect support, grammar-only copular shells, discourse-only organizers, redundant restatements, and proposition wrappers with no independent predicate identity."
    ),
    "LOCATOR": (
        "Retain each distinct smallest complete source-presented orienting relation establishing position, containment, path, direction, origin/destination, entry/exit, proximity, accompaniment/carrying, recurrence, procedure/relation, mental/internal context, temporal position, or figurative/comparative orientation. "
        "Multiple orientations may coexist when they do different work. Reject bare prepositions, ordinary argument markers, and orientation wording with no independent orienting identity."
    ),
})
