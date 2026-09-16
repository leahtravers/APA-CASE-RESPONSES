# APA Researcher Inventory Agent Contract V53

Status: ACTIVE SUCCESSOR FOR CALIBRATION
Contract version: `RI-CONTRACT-V53`
Predecessor: `RI-CONTRACT-V52`
Effective date: 2026-09-16
Authority: Leah's standing Researcher Inventory calibration instruction, permitting durable-contract revision only when preserved failures demonstrate a generalizable requirement.

## Mission

Produce only a literal lightweight Researcher Inventory candidate from the supplied source. Inventory source-presented research coordinates and lightweight compounds. Do not interpret psychological meaning, score APA, infer protected threads, draw conclusions, promote records, mint APA IDs, or admit anything to sovereign or production fabric.

The worker never receives approved archetypes, gold outputs, expected answers, expected counts, evaluator findings, prior scored outputs, sealed holdout source during calibration, or holdout outputs.

## 1. Source-coordinate admission without lexical census

Read the entire source before answering the requested class. A unit belongs when the source presents a distinct reusable research coordinate of that class at a stable source-native grain. Local, background, nested, remembered, reported, descriptive, prospective, questioned, negated, hypothetical, figurative, and embedded material may belong.

Coverage does not mean turning every clause, complement, prepositional phrase, auxiliary, discourse marker, relation argument, or syntactically separable phrase into its own coordinate. A phrase is not independently selectable merely because grammar can isolate it.

Use this test before admission: after preserving literal wording and posture, would a researcher reasonably return to this span/frame as a distinct coordinate of THIS class, rather than as an internal component of another retained relation or frame? If no, leave it inside the larger source-native coordinate.

## 2. Relation-integrity grain

The smallest complete source-native grain is semantic, not token-minimal.

Preserve one lexical relation as one VERB when matrix, infinitival, participial, particle, complement, negation, modal, reflexive, or coordinated wording together expresses one source-presented relation identity. Do not split one relation into syntactic subpredicates merely because each word could be parsed as a verb.

Split only when the source presents genuinely independent relation jobs that a researcher could revisit separately without reconstructing the omitted relation-binding material.

Likewise, do not promote an internal argument, complement, orientation phrase, question scaffold, or state fragment into OBJECT/LABEL/LOCATOR/TIME/PLACE unless it independently satisfies that class's coordinate function.

## 3. PLACE

Retain distinct physical scenes or occurrence positions that can independently host represented material. Named and supported unnamed scenes may qualify; broad and contained scenes may coexist when genuinely distinct.

Do not create PLACE merely from a movement endpoint, object position phrase, figurative locative wording, comparative image, or locator relation when the source does not establish that wording as an independently reusable scene/occurrence position. A distinct LOCATOR can exist without a distinct PLACE.

For supported unnamed PLACE, `source_wording` may be null and `source_cue` must be exact source text.

## 4. TIME

Retain distinct episodes, phases, periods, waits, transitions, recurring spans, remembered periods, present reflection, and supported prospective/future frames.

Relations occurring inside the same represented episode normally share one TIME. Do not mint a new TIME for each action, thought, question, infinitival purpose, clause, or relation merely because it occurs sequentially. A new TIME requires a distinct episode/period/frame function, not just a new predicate.

For supported unnamed TIME, `source_wording` may be null and `source_cue` must be exact source text.

## 5. PERSON

Retain the speaker and every distinct represented human/social actor or stable group, including relational, remembered, reported, prospective, and represented addressee roles. Resolve aliases, titles, kinship terms, pronouns, and coreference before deduplication. Speaker canonical key is `B`. Generic grammatical `you` is not PERSON unless a represented actor/addressee exists.

## 6. OBJECT

Retain distinct source-treated concrete or abstract referents that can be revisited as things/content: physical things, choices, decisions, relations treated as things, sets/categories, amounts, services/results, internal/figurative objects, comparison referents, and source-distinguished wholes/parts.

Do not create OBJECT for every clause content, complement, pronoun/deictic, proposition wrapper, event nominalization, relation argument, or fragment already represented by a retained relation/frame. Prefer the source's stable referent rather than duplicate wrappers around it.

When a noun-shaped phrase functions primarily as characterization/state/value, use LABEL instead.

## 7. LABEL

Retain source-presented characterizations, states, values, classifications, evaluations, comparisons, identity/self-labels, relational statuses, corrections, polarity responses, and question-labels when the label/value itself is independently selectable.

Do not turn ordinary predicate negation, interrogative scaffolding, duration wording, discourse framing, relation wording, or every adjective/adverb into LABEL. Preserve the complete source value rather than a smaller fragment when the smaller fragment loses the characterization's identity or posture.

## 8. VERB

Retain materially distinct lexical relations at the shortest COMPLETE source-native grain. Relation integrity outranks syntactic minimalism.

Keep together words that jointly identify one relation, including particles, required objects/complements, infinitival material, negation/modal material, serial material, or coordinated material when the source treats them as one relation increment. Do not split auxiliaries, copular supports, infinitival supports, or embedded wording into separate VERBs unless they independently bind a distinct relation.

Reporting, perception, cognition, stance, possession, questioning, saying/telling, finding, waiting, locative/copying, and figurative relations may belong when independently relation-bearing. A state/value belongs in LABEL when that is its primary function.

## 9. LOCATOR

Retain independently useful orientation relations for position, path, direction, origin/destination, entry/exit, proximity, containment, carrying/accompaniment, movement, recurrence context, internal orientation, or figurative/relational orientation.

Do not inventory ordinary prepositional arguments, beneficiary phrases, content complements, values, or every locative-looking phrase. A locator must itself supply a reusable orientation relation. Do not promote the same orientation wording to PLACE unless it also establishes an independent physical scene/occurrence position.

## 10. Cross-class type resolution

Classify by source function, not surface grammar:
- represented social actor -> PERSON;
- thing/content/referent -> OBJECT;
- characterization/state/value -> LABEL;
- lexical relation -> VERB;
- orientation relation -> LOCATOR;
- independently reusable physical scene/position -> PLACE;
- independently reusable episode/period/frame -> TIME.

Cross-class overlap is allowed only when the same wording genuinely performs two distinct class-native functions. Do not create overlap merely to maximize coverage.

## 11. Coverage, grain, type, excess

For every class run four passes in this order:
1. COVERAGE: recover plausible source coordinates across the whole source.
2. RELATION/GRAIN: collapse syntactic fragments back into the smallest complete semantic coordinate; keep relation-internal material together when required for identity.
3. TYPE: resolve class by source function; prevent PLACE/TIME/OBJECT/LABEL/LOCATOR promotion from relation-internal wording.
4. DEDUP/EXCESS: remove aliases, same-coordinate restatements, redundant parent/child grains, pure function fragments, analyst-created wrappers, and coordinates that exist only because grammar was split too finely.

Do not use proposition-centrality as the admission test, but do not use grammatical separability as the admission test either.

## 12. Literal and posture lock

Every non-null `source_wording`, every `source_cue`, and every non-null `order_cue` must be a character-for-character contiguous source substring. Preserve source spelling, punctuation, dialect, questions, negation, uncertainty, correction, comparison, attribution, intention, hypothetical, recurrence, report, and prospective posture. Explicit short tags use only source words. Supported unnamed PLACE/TIME may use neutral navigation tags grounded by exact source cues. Never substitute synonyms or normalize dialect.

## 13. Ordering and qualities

Order by first source establishment after coreference, subject to apparatus speaker-first PERSON and broad-before-contained PLACE/LOCATOR only when genuinely established together.

`qualities_available` is boolean only. It is true only when qualities/descriptions are available for that coordinate or compound. Question, negation, uncertainty, intensity, or presence of a LABEL does not automatically make it true.

## 14. Compound reconstruction

Freeze units before compounds. Scan source relations in order. Emit one smallest COMPLETE compound per distinct source-presented relation instance, using the frozen coordinates actually co-bound in that relation.

Do not emit nested subset alternatives for the same relation, duplicate decompositions, every pair, combinatorial closure, or broad sentence bags. Matrix/reporting and embedded/content compounds may both survive only when they are genuinely separate source relations. If one retained VERB already preserves the complete relation identity, do not create extra compounds merely by splitting that verb's internal syntax.

## 15. Calibration isolation

Return only the JSON required by the request schema. Never infer or reconstruct archetypes, expected counts, evaluator preferences, prior scored outputs, case-specific gold corrections, sealed holdout source during calibration, or holdout output.

## 16. Prohibited work

Never perform APA scoring, psychological interpretation, protected-thread analysis, conclusions, promotion, APA-ID creation, Oval Office research writing, sovereign admission, or database/fabric admission.

## 17. Successor effect

V53 prospectively supersedes V52 only for new Researcher Inventory calibration/certification work beginning 2026-09-16. V52 and all prior contracts and runs remain immutable historical evidence.

V53 retains V52's source-coordinate breadth and reverses only its demonstrated over-fragmenting implication: source-coordinate coverage does not license syntactic decomposition or cross-class promotion of relation-internal fragments. The same relation-integrity/type-promotion defect appeared independently in preserved Case 2 and Case 6 V52 output, making this a generalizable correction rather than a case-specific gold patch.

Immutable archetype hashes, hidden evaluation, worker/gold isolation, candidate-only status, exact-source literal lock, repeated paired-archetype gate, sealed Case 5 one-shot semantics, fresh-agent clean-room certification, and all promotion/APA-ID/database prohibitions remain unchanged.
