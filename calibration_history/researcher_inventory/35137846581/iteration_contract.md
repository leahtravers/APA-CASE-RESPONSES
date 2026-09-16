# APA Researcher Inventory Agent Contract V57

Status: ACTIVE SUCCESSOR FOR CALIBRATION
Contract version: `RI-CONTRACT-V57`
Predecessor: `RI-CONTRACT-V56`
Effective date: 2026-09-16
Authority: Leah's standing Researcher Inventory calibration instruction, permitting durable-contract revision only when preserved failures demonstrate a generalizable requirement.

## Mission

Produce only a literal lightweight Researcher Inventory candidate from the supplied source. Inventory source-presented research coordinates and lightweight compounds. Do not interpret psychological meaning, score APA, infer protected threads, draw conclusions, promote records, mint APA IDs, or admit anything to sovereign or production fabric.

The worker never receives approved archetypes, gold outputs, expected answers, expected counts, evaluator findings, prior scored outputs, sealed holdout source during calibration, or holdout outputs.

## 1. Governing model: complete lightweight class-native inventory

Read the complete source before answering any requested class.

The Researcher Inventory is not a vocabulary list, syntactic parse, exhaustive phrase census, or globally minimal graph. It is a **complete lightweight inventory of source-supported coordinates** at a stable semantic grain.

For the requested class, retain every source-supported coordinate that independently performs that class's research function after context and coreference are restored. A coordinate does not have to be globally indispensable to the smallest possible representation of the source. It must, however, have a real class-native identity beyond mere lexical or grammatical separability.

Use this internal order:

1. read the whole source and resolve speaker, actors, aliases, and coreference;
2. map distinct represented physical scenes/occurrence positions and temporal/episode frames;
3. traverse the entire source for plausible coordinates of the requested class, including nested and supported unnamed coordinates;
4. backfill structural roles that lexical scanning can miss;
5. apply the requested class's positive admission rule and exclusions;
6. resolve cross-class function;
7. deduplicate only true aliases, duplicate decompositions, unsupported wrappers, and same-coordinate restatements;
8. freeze the primitive inventory before compound construction.

Coverage comes before pruning. Pruning may remove a false coordinate; it may not erase a source-distinguished coordinate merely because another retained unit already helps reconstruct the same larger event.

## 2. Universal admission test

Admit a primitive when all applicable conditions hold:

1. **SOURCE SUPPORT:** its identity and scope are grounded in the supplied source; supported unnamed PLACE/TIME coordinates use exact source cues rather than invented content.
2. **CLASS FUNCTION:** it performs the requested class's positive function, not merely a grammatical role or neighboring class function.
3. **INDEPENDENT COORDINATE IDENTITY:** after restoring context, a researcher could return to it as this class coordinate without requiring the analyst to invent a new proposition or concept.
4. **SOURCE DISTINCTION:** collapsing it into another retained coordinate would erase a distinction the source itself presents for this class.
5. **GRAIN:** it is the shortest complete source-native semantic unit for that class function; neither a token fragment nor an unnecessary whole-clause wrapper.

Do **not** require global graph necessity. Do **not** admit merely because a word or phrase is semantically meaningful, syntactically separable, vivid, concrete, evaluative, verbal, or prepositional.

## 3. Structural backfill

After the first requested-class pass, inspect each materially represented relation cluster before final pruning.

Ask, as applicable:

- Does the source establish a distinct physical scene or occurrence position for this cluster?
- Does it establish a distinct episode, period, phase, remembered/current/prospective frame?
- Are source-distinguished people or social groups represented even if introduced indirectly or offscreen?
- Are stable concrete/content referents underrepresented because they were treated as merely descriptive or relational?
- Is a foregrounded value/state/classification present?
- Is there a materially distinct lexical relation that has been swallowed by a larger clause?
- Is there a genuine orientation edge that is not already represented by PLACE/TIME alone?

Backfill only source-supported roles. Do not invent symmetric coordinates where the source supplies none.

## 4. PLACE — occurrence-position inventory

Retain each distinct source-supported **physical scene or occurrence position** that independently hosts represented material.

PLACE may include:

- broad and contained physical scenes when the source materially distinguishes both;
- an object's physical position when that position functions as a revisitable occurrence location rather than only an orientation phrase;
- a waiting or interaction position inside a broader site when the source distinguishes that occurrence role;
- a source-supported offscreen or unnamed physical location for represented participants/interactions;
- remembered, reported, current-telling, or other represented physical settings when distinct;
- physical support/context that functions as where represented activity occurs.

Distinct PLACE coordinates may share the same broader geography. Do not merge them solely because they are co-located or unnamed.

Do not create PLACE merely from a physical noun, path, endpoint, surface, distance, or orientation phrase when the source does not establish an independently revisitable occurrence position. Use LOCATOR when the material's function is orientation only.

For supported unnamed PLACE, `source_wording` may be null and `source_cue` must be an exact contiguous source substring that grounds the position.

## 5. TIME — episode/frame inventory

Retain each distinct source-supported **episode, period, phase, or temporal/narrative frame** that independently organizes represented material.

TIME may include, when source-distinguished:

- discrete interaction or action episodes;
- before/after or earlier/later periods;
- waiting versus active phases;
- remembered or reported periods;
- recurring spans;
- continuing relationship/state periods;
- present telling or present reflection;
- prospective/future frames;
- a broader contextual period and a contained episode when both have independent temporal roles.

Do not mint a new TIME merely because a new predicate occurs. Do not turn ordinary adverbs, discourse transitions, tense/aspect markers, durations, or isolated time phrases into TIME when they only position an already-retained frame.

Do not collapse distinct frames solely because they occur within one broader story or because the source does not name them explicitly.

For supported unnamed TIME, `source_wording` may be null and `source_cue` must be an exact contiguous source substring that grounds the frame.

## 6. PERSON — represented social actors

Retain the speaker and every distinct represented human/social actor or stable group after coreference resolution.

An actor/group may qualify when introduced through:

- direct participation;
- kinship or relational identity;
- possession or beneficiary relation;
- report, memory, or another participant's scene;
- offscreen action;
- a stable represented addressee role;
- a socially meaningful group role.

Resolve aliases, titles, kinship terms, pronouns, and coreference before deduplication. Speaker canonical key is `B`.

Do not admit generic, impersonal, rhetorical, idiomatic, or self-directed grammatical second person unless the source establishes a stable represented actor/addressee.

## 7. OBJECT — stable source-treated things/content

Retain source-distinguished concrete or abstract referents that function as stable, revisitable things/content.

After coreference, apply a **default-retain bias to concrete source-distinguished referents** when the source treats them as separate things rather than mere grammatical decoration. Do not prune a concrete referent merely because it is background, descriptive, nested, a component of a larger scene, or not central to the main proposition.

OBJECT may include:

- physical things and source-distinguished wholes/parts;
- containers, contents, supports, artifacts, materials, or environmental objects when the source separately treats them as things;
- choices, decisions, amounts, services/results, relations or sets treated as things;
- stable topics or mental/abstract content treated as a referent;
- figurative/comparison referents when the source itself presents them as things;
- source-reified event/result content when the source treats that content as a stable object of thought or discussion.

Do not create OBJECT for every clause content, action, state, proposition, pronoun/deictic, complement, relation argument, or analyst-created nominalization. If the underlying retained participants/relations/values already represent the content and the source does not independently reify a wrapper, do not add a duplicate proposition object.

Distinguish related concrete referents when the source distinguishes them; do not collapse a whole, part, container, content, support, or other thing merely because they participate in one relation.

When wording functions primarily as a characterization/state/value, use LABEL instead. When its primary class function is a physical occurrence position, use PLACE; genuine cross-class overlap requires two independent functions, not noun shape.

## 8. LABEL — foregrounded source-presented values

Retain a LABEL only when the source presents a **foregrounded characterization, state, value, classification, evaluation, comparison, identity/self-label, relational status, polarity response, correction, or question-label** as an independently reusable value coordinate.

Use the shortest complete wording that preserves the value's identity, target, polarity, comparison, question, correction, or uncertainty posture.

Strong exclusion rule: do not inventory ordinary descriptive adjectives/adverbs, incidental modifiers, intensifiers, discourse emphasis, generic qualities, predicate fragments, or every evaluative-sounding word. A modifier is not a LABEL merely because it describes something.

Negation/interrogation is not automatically a LABEL. Retain it when the source foregrounds the value/polarity itself as the thing being classified, questioned, rejected, corrected, affirmed, or contrasted.

Do not turn an entire proposition into LABEL when a smaller complete source value carries the characterization. Conversely, do not split one complete value phrase into modifier fragments that lose its source-presented identity.

## 9. VERB — materially distinct lexical relations

Retain one shortest complete VERB coordinate for each **materially distinct source-presented lexical relation**.

A VERB is a relation identity, not every verb-shaped token and not every clause.

Retain a relation when it independently binds or changes a represented relation among retained/source-supported coordinates. Reporting, cognition, perception, possession, stance, locative/copular relation, movement, questioning, saying/telling, finding, waiting, comparison, and figurative relations may qualify when they perform that independent relation job.

Merge words that jointly express one relation identity, including particles, required complements, negation/modal material, fixed idioms, and control/serial material when splitting would create only grammatical fragments.

Split when the source presents two materially distinct relation jobs, including nested, reported, infinitival, or coordinated relations whose removal would erase a separate represented edge while the other relation remains meaningful.

Strong exclusion rule: do not inventory pure discourse/performance scaffolding, conversational floor-management, filler, bare metacognitive framing, pantomime/stage directions, generic utterance mechanics, or clause fragments when they do not independently bind a material source relation. Do not retain a second VERB merely because the same relation can be parsed at two syntactic levels.

A source-presented value/state belongs in LABEL when value is its primary function; do not duplicate it as VERB solely because grammar uses a copula.

## 10. LOCATOR — orientation only

Retain a LOCATOR only when it supplies an independently reusable **orientation relation**.

Orientation functions include:

- physical position;
- path or direction;
- origin/destination;
- entry/exit;
- containment;
- support/surface placement;
- accompaniment/carrying;
- proximity/distance;
- movement orientation;
- internal or figurative orientation.

A genuine orientation edge may coexist with PLACE, OBJECT, or VERB when the same wording independently performs both functions.

Strong exclusion rule: do not duplicate a TIME or PLACE frame as LOCATOR merely because a temporal/location phrase is prepositional. Do not inventory topical/content complements, ordinary beneficiary/recipient arguments, durations/dates, recurrence wording, comparison complements, or generic prepositional arguments unless they independently orient a retained source coordinate.

Use the shortest complete orientation wording. Keep materially distinct orientation edges separate; do not concatenate unrelated position, movement, accompaniment, and destination roles simply because they share a clause.

## 11. Cross-class type resolution

Classify by positive source function, not surface grammar:

- represented human/social actor -> PERSON;
- stable thing/content/referent -> OBJECT;
- foregrounded characterization/state/value -> LABEL;
- materially distinct lexical relation -> VERB;
- reusable orientation relation -> LOCATOR;
- independently revisitable physical scene/occurrence position -> PLACE;
- independently revisitable episode/period/frame -> TIME.

Before permitting cross-class overlap, state internally the independent positive job performed in each class. Shared wording alone is insufficient. Do not suppress genuine overlap merely to force one-class exclusivity.

## 12. Coverage, exclusion, and deduplication order

For each requested class use this order:

1. **EXHAUSTIVE CLASS-NATIVE COVERAGE:** traverse the complete source and admit every plausible class-native coordinate before suppression.
2. **STRUCTURAL BACKFILL:** inspect relation clusters for source-supported unnamed/indirect structural coordinates missed by lexical scanning.
3. **TYPE-SPECIFIC EXCLUSION:** apply the strong exclusions of the requested class; remove material whose positive function belongs elsewhere or is only grammatical/discourse scaffolding.
4. **GRAIN:** merge fragments that are not independently class-bearing; split source-distinguished class roles that have been swallowed together.
5. **COREFERENCE/DEDUP:** remove aliases and true duplicate restatements of the same coordinate.
6. **EXCESS PASS:** remove unsupported inference, analyst-created wrappers, lexical census residue, and duplicate decompositions.

Never use proposition centrality, grammatical independence, global graph minimality, or lexical vividness as the admission test.

## 13. Literal and posture lock

Every non-null `source_wording`, every `source_cue`, and every non-null `order_cue` must be a character-for-character contiguous source substring.

Preserve source spelling, punctuation, dialect, questions, negation, uncertainty, correction, comparison, attribution, intention, hypothetical, recurrence, report, and prospective posture.

Explicit short tags use only source words. Supported unnamed PLACE/TIME may use neutral navigation tags grounded by exact source cues. Never substitute synonyms or normalize dialect.

## 14. Ordering and qualities

Order by first source establishment after coreference, subject to apparatus speaker-first PERSON and broad-before-contained PLACE/LOCATOR only when genuinely established together.

`qualities_available` is boolean only. It is true only when qualities/descriptions are available for that coordinate or compound. Question, negation, uncertainty, intensity, or the mere presence of a LABEL does not automatically make it true.

## 15. Compound reconstruction — complete material binding skeleton

Freeze all admitted primitive units before constructing compounds.

Scan source-presented relations in order. Emit **one smallest complete compound per materially distinct binding/relation instance** that requires compound representation.

For each binding, include every frozen coordinate that materially participates in that binding, as applicable:

- participant(s);
- the relation atom(s) that constitute that binding;
- acted-on or discussed object/content;
- foregrounded value/polarity;
- the source-supported TIME and PLACE anchors for that binding;
- any independently retained LOCATOR that materially orients it.

Completeness does not mean adding every nearby unit. Include a coordinate only when the source binds it to that relation instance.

Do not emit:

- a compound for every clause or sentence;
- every pair or combinatorial closure;
- one- or two-unit trivial combinations that add no cross-coordinate binding;
- nested subset alternatives for the same single binding;
- duplicate decompositions of the same relation;
- broad sentence bags containing neighboring but unbound units;
- compounds that reference units not in the frozen inventory.

If two materially distinct source relations occur together, separate compounds may be needed. If one retained VERB already preserves one inseparable relation identity, do not multiply compounds by parsing its internal grammar.

`referenced_unit_refs` must reference only frozen admitted units. `compound_expression` must preserve their source order.

## 16. Calibration isolation

Return only the JSON required by the request schema. Never infer or reconstruct archetypes, expected counts, evaluator preferences, prior scored outputs, case-specific gold corrections, sealed holdout source during calibration, or holdout output.

Do not reason from an imagined evaluator. Apply this contract to the supplied source only.

## 17. Prohibited work

Never perform APA scoring, psychological interpretation, protected-thread analysis, conclusions, promotion, APA-ID creation, Oval Office research writing, sovereign admission, or database/fabric admission.

## 18. Successor effect

V57 prospectively supersedes V56 only for new Researcher Inventory calibration/certification work beginning 2026-09-16. V56 and all earlier contracts and runs remain immutable historical evidence.

V57 preserves V56's valid complete-source reading, structural awareness, coreference, literal/posture lock, source ordering, class/function resolution, evaluator isolation, candidate-only status, and selective-compound controls. It corrects V56's demonstrated generalizable overreliance on global graph necessity by replacing it with complete class-native coverage plus explicit type-specific exclusions and structural backfill.

Immutable archetype hashes, evaluator/worker isolation, repeated paired-archetype gate, sealed Case 5 one-shot semantics, fresh-agent clean-room certification, and all promotion/APA-ID/database prohibitions remain unchanged.
