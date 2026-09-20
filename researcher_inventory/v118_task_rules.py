"""V118 neutral apparatus rules: minimal sufficient binding basis at source-individuated grain.

No archetype answers, evaluator findings, expected counts, prior scored outputs,
calibration answers, or holdout material are included here.
"""
from researcher_inventory.inventory_apparatus import BASE_RULES as APPARATUS_BASE_RULES, CLASS_RULES as APPARATUS_CLASS_RULES

V118_CORRECTION = r'''
V118 PROSPECTIVE CORRECTION — MINIMAL SUFFICIENT BINDING BASIS AT SOURCE-INDIVIDUATED GRAIN.

READ THE WHOLE SOURCE FIRST. Before extracting any class, identify the materially distinct SOURCE BINDINGS a researcher would need to reconnect the narrative/report. A material binding changes who/what/how/where/when of a represented occurrence, state, judgment, question, comparison, choice, report, memory, reflection, or prospective frame. Do NOT create one binding per sentence, clause, modifier, predicate token, discourse phrase, or rhetorical flourish.

THE INVENTORY IS A COMPACT SOURCE-RECONNECTION BASIS. It is not a token census, clause census, proposition census, discourse annotation, rhetorical-style inventory, exhaustive semantic decomposition, or graph closure.

PRIMITIVE ADMISSION — ALL GATES MUST PASS:
A) SOURCE GROUNDING: the source explicitly establishes the coordinate in the requested class, or clearly establishes a legitimate unnamed PLACE/TIME support coordinate.
B) SOURCE INDIVIDUATION: the source presents the candidate, explicitly or structurally, as a distinct participant, referential handle, characterization, operative relation kernel, orientation, spatial support, or temporal support. Mere semantic meaningfulness or grammatical separability is insufficient.
C) MATERIAL BINDING CONTRIBUTION: if this row were removed while all other retained rows remained, at least one material binding would lose a participant, referential target/content node, characterization, operative relation, orientation, spatial support, or temporal support. If all bindings remain reconstructable, reject the row as redundant/descriptive wording.
D) NATURAL CLASS GRAIN: retain the smallest complete source-native coordinate. Do not split a stronger natural unit into meaningful internal fragments and do not inflate it to a sentence/clause wrapper.
E) NONREDUNDANCY: merge true same-class restatement/coreference; preserve genuinely different coordinates.
F) CLASS-NATIVE FUNCTION: type by represented job, not part of speech, syntax, metaphor, or analytic possibility.

LIGHTWEIGHT DOES NOT MEAN HIGH-SALIENCE ONLY. A coordinate may be local, one-use, mundane, background, remembered, reported, prospective, uncertain, negated, figurative, or colloquial. Recurrence, importance, narrative centrality, later reuse, and multiple compounds are never required. The same source-individuation and binding-contribution tests apply to all units.

REMOVE SURFACE FRAGMENTS. Reject wording that exists only as grammatical carriage, sentence completion, discourse management, rhetorical color, vivid but non-structural aside, quotation/reporting scaffolding without its own relation, modifier fragments, support wording, or an internal fragment of a stronger retained coordinate.

FUNCTIONAL TYPE ARBITRATION:
- represented human/social actor -> PERSON
- tracked thing/content/referential handle -> OBJECT
- source-applied characterization/state/status/evaluation/comparison/identity -> LABEL
- operative lexical action/state/relation -> VERB
- independent position/path/direction/context/orientation -> LOCATOR
- spatial support -> PLACE
- temporal support -> TIME
Cross-class overlap is allowed only when the exact span genuinely performs two independently source-individuated jobs and each changes material binding structure.

PLACE: retain spatial support only when omitting it would blur/collapse a material binding's occurrence position. A broad setting and a contained/local position may both qualify when materially distinguished. Several bindings may share one PLACE. Unnamed PLACE is lawful only when the source establishes distinct spatial support without naming the physical detail; use null source_wording and exact cue. Do not create PLACE from every physical noun, surface, path phrase, possession phrase, or object-location mention.

TIME: retain temporal support only when omitting it would blur/collapse a material binding's episode, phase, period, recurrence frame, remembered/reported frame, intended/prospective frame, or present-reflection frame. Several bindings may share one TIME. A duration phrase or transition word does not automatically become TIME. Unnamed TIME is lawful only when the source establishes distinct temporal support without naming the details.

PERSON: retain speaker plus each distinct represented human/social actor or stable group after true coreference when participating in or anchoring a material binding. Direct, offscreen, relational, possessive/beneficiary, remembered, reported, institutional, prospective, peripheral, and one-use actors may qualify. Reject nonreferential/rhetorical/generic person wording.

OBJECT: retain concrete or abstract source-presented REFERENTIAL HANDLES treated as distinct thing/content nodes in material bindings. Concrete things, parts, values, services/results, decisions/next steps, choices treated as choices, recurring relations treated as content, named sets/categories, remembered/reported content, and internal represented objects may qualify. Do not create OBJECT from every grammatical argument, pronoun, complement, question content, clause wrapper, discourse point, proposition, explanation, or speaker-organizing phrase. Abstract content requires both source individuation and binding contribution.

LABEL: retain the smallest complete source-applied characterization/state/status/identity/evaluation/comparison/candidate label/rejection/correction/posture when source-individuated and structurally material. One-use, colloquial, idiomatic, uncertain, questioned, negated, corrected, rejected, and figurative labels may qualify. Reject rhetorical color, descriptive flourish, narrative aside, intensifier, modifier, or manner wording that does not independently change a material binding. Keep one natural judgment whole.

VERB: retain the smallest complete literal predicate kernel for each source-individuated operative relation that changes a material binding. Actions, states, cognitions, perceptions, reports/communications, intentions, questions, decisions, possessions, comparisons, evaluations, movements, transitions, gestures, existence/location, obligations, and other represented relations may qualify. Preserve particles/reflexives/negation/modality/bound complements when required for identity. Keep coordinated/bound wording together when it forms one source-native relation kernel; split only genuinely separate operative relations that each change binding structure. Reject auxiliaries, copular/support carriage fully represented elsewhere, discourse/filler predicates, quotation/reporting scaffolding without its own relation, duplicate restatements, and lexical fragments nested inside a stronger natural kernel.

LOCATOR: retain the smallest complete exact span that is source-individuated as an independent orientation/context coordinate and changes a material binding. Position, path, origin/destination, direction, containment, proximity, accompaniment/carrying, entry/exit, recurrence/context, internal/mental/relational position, or materially spatialized figurative/comparative orientation may qualify. Do not inventory every PP, recipient/topic/purpose complement, possession phrase, degree phrase, temporal phrase, generic adverbial, rhetorical location metaphor, or evaluative state. If the binding remains structurally identical without it, reject it.

LITERAL LOCK: use the smallest complete exact contiguous source-native span preserving each explicit coordinate's identity. Every non-null source_wording/source_cue/order_cue must be exact source text. Preserve negation, modality, uncertainty, question form, attribution, comparison, idiom/dialect, reported/recalled posture, hypothetical/prospective posture, correction/rejection, particles, reflexives, and bound complements when needed. Never normalize, clean up, correct the speaker, paraphrase, translate, diagnose, euphemize, lemmatize into a different surface form, or substitute synonyms.

MINIMAL-SUFFICIENT FREEZE AUDIT:
1) replay each material binding in source order;
2) restore every source-individuated coordinate whose absence removes binding structure, even if local or low-salience;
3) for every retained row, name the exact binding and class-native job it changes;
4) remove any row whose deletion leaves all material bindings fully reconstructable;
5) remove rhetorical color, discourse scaffolding, clause wrappers, modifier fragments, support wording, and redundant internal fragments;
6) verify PLACE/TIME only where distinct support is structurally necessary;
7) arbitrate OBJECT/LABEL/VERB/LOCATOR by represented function;
8) verify natural complete spans, literal lock, coreference, and class-local distinctness;
9) order by first source establishment subject to apparatus rules;
10) freeze all seven ledgers. Never target hidden counts or infer hidden gold.

COMPOUNDS — SERIALIZE MATERIALLY COMPLETE BINDINGS:
Build only after primitive freeze. Emit a compound only when frozen coordinates jointly represent one materially complete source binding whose structure would otherwise be lost.
- Include only frozen coordinates actually participating in that binding.
- Group locally joint predicates when they jointly form one binding.
- Split when participant set, target/content, support frame, source posture, or materially distinct judgment/action changes enough that one compound would blur separate structure.
- A valid primitive may remain unbundled.
- Never create a compound to justify a primitive.
- Do not emit partial subset/superset variants of the same binding.
- Do not serialize sentence/clause structure merely because it exists.
- No graph closure, arbitrary co-occurrence, all-pairs links, scene mega-bundles, singleton equivalents, support chains, or duplicate restatements.

Never expose approved archetypes, evaluator findings, prior scored outputs, calibration answers, or sealed holdout material. Never perform promotion, Oval Office admission, APA-ID creation, sovereign/admitted writing, or APA database mutation.
'''.strip()

V118_BASE_RULES = APPARATUS_BASE_RULES + "\n\n" + V118_CORRECTION
V118_CLASS_RULES = dict(APPARATUS_CLASS_RULES)
V118_CLASS_RULES.update({
    "PLACE": "Return only source-individuated spatial SUPPORT coordinates whose absence would blur/collapse a material binding's occurrence position. Share support across bindings when not materially differentiated. Unnamed support is allowed only when source-established; use null source_wording and exact cue. Do not promote every physical noun/path/object-location phrase.",
    "TIME": "Return only source-individuated temporal SUPPORT coordinates whose absence would blur/collapse a material binding's episode/phase/period/recurrence/remembered/prospective/present-reflection frame. Several bindings may share one time. Do not promote duration questions, transition words, tense, or every predicate occurrence.",
    "PERSON": "Return speaker plus each distinct represented human/social actor or stable group after true coreference when the actor participates in or anchors a material binding. One-use/offscreen/relational/possessive/reported/prospective/peripheral actors may qualify; reject nonreferential/generic person wording.",
    "OBJECT": "Return source-individuated concrete or abstract REFERENTIAL HANDLES that function as distinct thing/content nodes in material bindings. Abstract content requires source reification plus nonredundant binding contribution. Do not turn every argument, pronoun, complement, question content, clause wrapper, discourse point, proposition, explanation, or speaker-organizing phrase into OBJECT.",
    "LABEL": "Return the smallest complete source-individuated characterization/state/status/identity/evaluation/comparison/candidate label/rejection/correction that changes a material binding. Preserve legitimate local/colloquial/questioned/negated/figurative labels. Reject rhetorical color, descriptive flourish, narrative aside, intensifier/modifier/manner fragments that add no independent binding structure.",
    "VERB": "Return the smallest complete literal kernel for each source-individuated operative relation that changes a material binding. Local/ordinary relations may qualify. Preserve bound identity material. Reject auxiliaries, support carriage represented elsewhere, discourse/filler/reporting scaffolding without its own relation, duplicate restatements, and fragments nested inside a stronger natural kernel.",
    "LOCATOR": "Return only source-individuated orientation/context spans that change a material binding: position/path/origin-destination/direction/containment/proximity/accompaniment/entry-exit/recurrence/internal-relational orientation. Reject generic PP/topic/purpose/possession/degree/temporal/adverbial/rhetorical-location wording when the binding is unchanged without it.",
})
