"""V115 neutral apparatus rules: source-presented binding roles at natural class grain.

These rules contain no archetype answers, evaluator findings, expected counts,
prior scored outputs, calibration answers, or holdout material.
"""
from researcher_inventory.inventory_apparatus import BASE_RULES as APPARATUS_BASE_RULES, CLASS_RULES as APPARATUS_CLASS_RULES

V115_CORRECTION = r'''
V115 PROSPECTIVE CORRECTION — SOURCE-PRESENTED BINDING-ROLE ENTITLEMENT AT NATURAL CLASS GRAIN.

READ THE WHOLE SOURCE FIRST. Reconstruct a source binding/frame skeleton at natural research grain: distinct scenes/frames, actors, tracked referents/content handles, source-applied characterizations, operative relation edges, and independent orientations. The skeleton is not a sentence parse, token ledger, clause decomposition, or exhaustive semantic graph.

LIGHTWEIGHT MEANS SOURCE-RECONNECTABLE STRUCTURE, NOT HIGH-SALIENCE PRUNING AND NOT SEMANTIC CENSUS. A coordinate may be one-use, local, nested, mundane, low-salience, remembered, reported, uncertain, negated, prospective, hypothetical, figurative, or colloquial. Recurrence, broad importance, repeated mention, and multi-compound reuse are never required. But source presence, semantic content, grammatical separability, and local typability are not sufficient by themselves.

FOUR-GATE ADMISSION:
A) SOURCE GROUNDING: the source establishes the candidate in the requested class, or legitimately establishes an unnamed PLACE/TIME support slot.
B) CLASS-NATIVE FUNCTION: the candidate performs a real job of the requested class, not merely a grammatically compatible form.
C) BINDING/FRAME ROLE: the candidate fills a distinct selectable role in at least one source-presented binding/frame in the whole-source skeleton. Ask whether a researcher needs it as its own coordinate to reconnect a distinct participant, referent/content handle, scene/frame support, characterization, operative relation, or orientation at this class's natural resolution rather than merely to recover wording inside a stronger retained coordinate/binding.
D) CLASS-LOCAL DISTINCTNESS + NATURAL GRAIN: merge true aliases/coreference and same-class restatements; do not split one natural relation, orientation, characterization, or referent into support fragments merely because each fragment has meaning.

ANTI-CENSUS: reject standalone rows created only from grammar or from locally meaningful wording internal to a stronger retained coordinate/binding. This includes proposition/clause wrappers that merely restate a relation, every grammatical argument as OBJECT, every modifier as LABEL, every PP/purpose/topic/recipient phrase as LOCATOR, every clause/action as TIME, every physical noun/surface as PLACE, every lexical verb as VERB, and support fragments split from one natural predicate/orientation. Reject grammar-only auxiliaries, articles, connectives, tense/aspect machinery, fillers, generic pronouns after coreference, and analyst abstractions.

FUNCTION BEATS SURFACE FORM:
- represented human/social actor -> PERSON
- independently tracked thing/content/referent -> OBJECT
- source-applied characterization/state/identity/evaluation/comparison/candidate label/correction -> LABEL
- source-differentiated scene/location support -> PLACE
- source-differentiated episode/period/phase support -> TIME
- operative lexical action/state/relation edge -> VERB
- independent position/path/direction/context/orientation edge -> LOCATOR
Cross-class overlap is allowed only when the same exact source wording genuinely performs distinct source-presented roles in more than one class.

PLACE: retain each distinct physical scene or occurrence-position that hosts or materially locates a source-presented binding/frame. Broad and materially distinct contained scenes may both qualify. Destination, waiting, later-interaction, remembered, prospective, or present-telling locations may qualify when source-differentiated. Unnamed PLACE is allowed only for a distinct source-established scene that cannot truthfully share another retained scene; use null source_wording + exact cue + neutral tag. Do not turn every physical noun, surface, object part, path, or object-location mention into PLACE.

TIME: retain each distinct episode/frame/phase/period/recurrence/remembered/reported/prospective/present-reflection support that organizes source-presented bindings. Unnamed TIME is allowed only for a source-differentiated frame. Several actions or relations may share one TIME. Do not create TIME for every clause, predicate, local action, question, transition word, duration phrase, or grammatical tense/aspect signal.

PERSON: retain speaker plus every distinct represented human/social actor or stable group after coreference when it fills a participant role in a source-presented binding. Direct, offscreen, relational, possessive/beneficiary, remembered, reported, institutional, prospective, peripheral, and one-use actors may qualify. Reject only generic/rhetorical/nonreferential persons that never become represented participants.

OBJECT: retain each concrete or abstract referent/content handle independently tracked as a participant in one or more bindings: something acted on, possessed, exchanged, located, checked, compared, selected, rejected, remembered, reported, contemplated, valued, or otherwise related as a thing/content node. One-use and low-salience referents may qualify. Decisions/choices/plans/relations/values/sets/internal content/proposition-like content qualify only when the source actually reifies or tracks them as content. Do not nominalize every clause, question, intention, relation, or grammatical argument into OBJECT.

LABEL: retain each smallest complete source-presented characterization/state/status/identity/evaluation/comparison/candidate label/rejection/correction or materially distinct manner/posture applied to a represented target. One-use, colloquial, idiomatic, uncertain, questioned, negated, corrected, rejected, and figurative labels may qualify. Choose the natural judgment unit. Do not turn every adjective, adverb, intensifier, local modifier, or discourse stance into LABEL.

VERB: retain one minimal complete literal predicate kernel for each distinct source-presented OPERATIVE RELATION EDGE in the binding skeleton. Qualifying edges may express action, state, stance, cognition, perception, report/communication, intention, question, decision, possession, comparison, evaluation, movement, transition, gesture, existence/location, or another represented relation. One-use, ordinary, reporting, perception, obligation, location, gestural, and low-salience edges may qualify. DO NOT REQUIRE BROAD STORY CHANGE. But lexical meaning alone is insufficient: do not retain every grammatical/contentful verb token or split one natural relation into micro-relations/support fragments. Preserve particles/reflexives/negation/modality/bound complements only when needed for relation identity. Split nested/coordinated predicates only when the source presents genuinely distinct operative edges. Exclude pure tense/aspect auxiliaries, support copulas with no separate relation, discourse/filler predicates with no edge, and true same-relation restatements.

LOCATOR: retain each smallest complete exact span that fills an independent orientation role in a source-presented binding: scene position, path, origin/destination, direction, containment, proximity, accompaniment/carrying, entry/exit, internal/mental/relational position, recurrence/context, or materially spatialized figurative/comparative orientation. The locator must actually orient a retained participant/referent/relation/frame. Do not turn every prepositional phrase, recipient/topic/purpose argument, possession phrase, degree phrase, temporal phrase, or generic adverbial into LOCATOR.

ATOMIC SPAN + LITERAL LOCK: use the smallest complete exact contiguous source-native span that preserves each explicit coordinate's identity. Preserve required particles/prepositions, reflexives, bound complements, negation, modality, uncertainty, questions, attribution, comparison, idiom/dialect, and hypothetical/prospective/reported/corrective posture. Every non-null source_wording/source_cue/order_cue must be exact source text. Never normalize, paraphrase, clean up, translate, diagnose, euphemize, lemmatize into a different surface form, or substitute synonyms.

FREEZE AUDIT:
1) replay every source-presented binding/frame in source order;
2) verify each class-native role that needs a selectable coordinate is represented;
3) check one-use/local/low-salience/remembered/reported/prospective roles for accidental pruning;
4) remove anti-census excess whose only function is internal wording of a stronger retained coordinate/binding;
5) verify PLACE/TIME support is scene/frame based rather than clause/action based;
6) verify OBJECT/LABEL/LOCATOR typing by source function;
7) verify VERB kernels are natural operative edges, neither support fragments nor clause-sized bundles;
8) verify literal lock, coreference, class-local distinctness, and source order;
9) freeze all seven ledgers before compounds.

COMPOUNDS: after primitive freeze, serialize only the materially distinct source-presented bindings from the same skeleton. Emit the smallest complete compound needed to reconnect each such binding. Use a retained VERB as backbone when one carries the binding; include participants, referents/content, labels/states, PLACE/TIME support, and LOCATOR refs only when they actually participate in that exact binding. A non-VERB label/state/question binding may form a compound only when it is distinct source structure not already carried by another relation. Do not emit compounds merely because wording forms a clause or sentence. No graph closure, arbitrary co-occurrence, all-pairs links, scene mega-bundles, singleton equivalents, subset/superset permutations, support chains, or duplicate restatements.

Never target hidden counts or infer hidden gold. Never expose approved archetypes, evaluator findings, prior scored outputs, calibration answers, or sealed holdout material. Never perform promotion, Oval Office admission, APA-ID creation, sovereign/admitted writing, or database mutation.
'''.strip()

V115_BASE_RULES = APPARATUS_BASE_RULES + "\n\n" + V115_CORRECTION
V115_CLASS_RULES = dict(APPARATUS_CLASS_RULES)
V115_CLASS_RULES.update({
    "PLACE": "Retain a PLACE only when it is a distinct source-presented scene/location support role for a binding/frame. One-use, contained, destination, waiting, remembered, prospective, and unnamed support may qualify. Do not promote every physical noun/surface/object position. Several relations may share one scene support.",
    "TIME": "Retain a TIME only when it is a distinct source-presented episode/frame/phase/period support role. One-use, remembered, reported, intended, recurring, prospective, and unnamed frames may qualify. Do not create a TIME for every clause, action, transition, question, or duration phrase; several relations may share one frame.",
    "PERSON": "Retain speaker plus each distinct represented human/social actor or stable group after coreference when it fills a participant role in a source-presented binding. Direct, offscreen, relational, possessive/beneficiary, remembered, reported, institutional, prospective, peripheral, and one-use actors may qualify. Reject only generic/nonreferential persons.",
    "OBJECT": "Retain an OBJECT when the source independently tracks/reifies it as a referent/content node participating in a binding. Concrete, abstract, internal, relational, decision/value/set/figurative content may qualify, including one-use material. Do not nominalize every clause, question, intention, grammatical argument, place, or characterization into OBJECT.",
    "LABEL": "Retain the smallest complete source-applied characterization/state/status/identity/evaluation/comparison/candidate label/rejection/correction that fills a distinct role in a binding. One-use and colloquial labels may qualify. Do not inventory every adjective/adverb/intensifier/modifier or split one natural characterization into fragments.",
    "VERB": "Retain one minimal complete literal predicate kernel for each distinct source-presented operative relation edge. One-use, ordinary, reporting, perception, question, obligation, location, cognition, gesture, and low-salience relations may qualify. Do not require broad story change, but do not retain every lexical verb token or split one natural predicate into support/micro-relations.",
    "LOCATOR": "Retain the smallest complete span that fills an independent orientation role in a source-presented binding. Position/path/direction/origin-destination/containment/proximity/accompaniment/internal-context/figurative orientation may qualify. Do not inventory every prepositional, recipient/topic/purpose, possession, degree, or temporal phrase merely because it is relational.",
})
