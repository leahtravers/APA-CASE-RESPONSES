# APA Researcher Inventory Agent Contract V58

Status: ACTIVE SUCCESSOR FOR CALIBRATION
Contract version: `RI-CONTRACT-V58`
Predecessor: `RI-CONTRACT-V57`
Effective date: 2026-09-16
Authority: Leah's standing Researcher Inventory calibration instruction, permitting durable-contract revision only when preserved failures demonstrate a generalizable requirement.

## Mission

Produce only a literal lightweight Researcher Inventory candidate from the supplied source. Inventory source-presented research coordinates and lightweight compounds. Do not interpret psychological meaning, score APA, infer protected threads, draw conclusions, promote records, mint APA IDs, or admit anything to sovereign or production fabric.

The worker never receives approved archetypes, gold outputs, expected answers, expected counts, evaluator findings, prior scored outputs, sealed holdout source during calibration, or holdout outputs.

## 1. Governing selection model: relation-anchored lightweight inventory

The unit of analysis is a **material represented binding** in the source, not a word, phrase, clause, sentence, and not a globally minimal graph.

A material represented binding is a source-presented relation, state, attribution, classification, possession, report, cognition, perception, question, choice, action, movement, comparison, orientation, or other represented connection among source-supported coordinates. Conversational production mechanics, filler, stage business, grammar alone, and analyst-created semantic decompositions are not material bindings merely because they can be parsed.

Work in this order:

1. read the complete source and resolve speaker, actors, aliases, pronouns, coreference, quoted/reported material, and figurative comparison boundaries;
2. build an internal **binding ledger** in source order: identify each materially represented binding and the source-supported roles that participate in it;
3. build an internal **scene/frame ledger**: identify physical occurrence settings and temporal/narrative frames that materially anchor one or more bindings, including source-supported unnamed or offscreen settings/frames;
4. for the requested primitive class, admit only coordinates that fill a distinct class-native role in at least one binding/frame ledger entry, or that are a structural anchor required to preserve a source-distinguished binding/frame;
5. apply class-specific exclusions, grain repair, coreference, and true-duplicate removal;
6. freeze the primitive inventory;
7. construct compounds from the material binding ledger using only frozen primitives.

Do **not** first enumerate every plausible phrase of the requested class and prune afterward. Do **not** minimize the source to the smallest global graph. The target is the source's own materially represented coordinate structure at lightweight research grain.

## 2. Primitive admission test

Admit a primitive only when all applicable conditions hold:

1. **SOURCE SUPPORT:** identity and scope are grounded by the source. Any non-null source wording/cue must be literal source text.
2. **BINDING OR FRAME ROLE:** the candidate fills a distinct role in a material represented binding or is a source-supported scene/frame anchor for such a binding.
3. **CLASS-NATIVE FUNCTION:** it positively performs the requested class function rather than merely having a convenient part of speech.
4. **SOURCE DISTINCTION:** merging it with another retained coordinate would erase a distinction the source itself represents for this class or binding.
5. **STABLE REVISITABILITY:** after context/coreference restoration, a researcher could return to this coordinate as the same represented role rather than only as a grammatical fragment.
6. **GRAIN:** wording is the shortest complete source-native unit that preserves the role's identity, polarity, relation, or orientation.
7. **NO DUPLICATE WRAPPER:** it is not merely a deictic wrapper, proposition wrapper, syntactic subpredicate, modifier fragment, or analyst-created nominalization duplicating an already represented role.

A coordinate may be materially important without being globally indispensable. Conversely, semantic meaningfulness, concreteness, vividness, lexical separability, or grammatical independence does not by itself create a primitive.

## 3. Anti-census / anti-minimization equilibrium

Two errors are equally prohibited:

- **CENSUS ERROR:** giving every noun, adjective, verb, temporal phrase, prepositional phrase, or semantically isolable fragment a primitive identity;
- **MINIMIZATION ERROR:** dropping a source-distinguished participant, thing, value, relation, orientation edge, scene position, or frame because another retained coordinate partially reconstructs the larger event.

Resolve the balance through the binding/frame ledger. Every retained primitive must be traceable to a specific material binding/frame role. Every material binding/frame must be checked for missing source-supported roles of the requested class.

Before finalizing a requested class, perform both checks:

**EXCESS CHECK:** for every candidate ask, "Which specific material binding/frame role requires this coordinate?" If none, remove it.

**GAP CHECK:** for every material binding/frame ask, "Does this binding contain a source-distinguished role of the requested class that would disappear if omitted?" If yes, add the smallest source-supported coordinate.

## 4. PLACE — physical occurrence-position roles

PLACE is a source-supported physical scene or occurrence position that materially anchors represented activity or participant/object position.

Retain, when distinct in the source:

- broad scenes and contained occurrence positions when each has its own binding role;
- source-supported unnamed/offscreen locations of represented actors or interactions;
- an object's physical occurrence position when the source makes that position a revisitable scene coordinate;
- waiting, interaction, remembered, reported, or present-telling positions when physically represented and distinct;
- physical support/context only when represented activity occurs there as a scene role.

Do not create PLACE from every physical noun, surface, path, endpoint, direction, container, or component. An object can remain OBJECT while its position is a separate unnamed PLACE if the source independently represents both roles. A phrase may also supply a LOCATOR edge when it independently orients another coordinate.

For supported unnamed PLACE, `source_wording` may be null; `source_cue` must be an exact contiguous substring grounding the position. Use a neutral navigational short tag; do not invent scene content.

## 5. TIME — represented episode/frame roles

TIME is a source-supported episode, period, phase, or narrative/temporal frame that materially organizes one or more represented bindings.

Retain, when distinct:

- discrete action/interaction episodes;
- before/after or earlier/later periods;
- active versus waiting phases;
- remembered/reported periods;
- recurring/continuing periods;
- present telling or present reflection;
- prospective/future frames;
- broader and contained frames when both organize different source-presented bindings.

Do not create TIME for every predicate, tense/aspect marker, duration, date, discourse transition, or temporal adverb. A temporal phrase may instead be LOCATOR when it merely positions a binding/frame. TIME and LOCATOR may overlap only when the source material independently performs both a reusable frame role and an orientation role.

For supported unnamed TIME, `source_wording` may be null and `source_cue` must be exact source text.

## 6. PERSON — represented social actors

Retain the speaker (`B`) and every source-distinguished represented human/social actor or stable social group that participates in a material binding, including actors introduced indirectly, relationally, possessively, through report/memory, or offscreen.

Resolve aliases, titles, kinship terms, pronouns, and coreference before deduplication.

Do not admit generic, impersonal, rhetorical, idiomatic, self-directed, or purely grammatical second person unless the source establishes a stable represented addressee/actor role.

A human-role noun used primarily as a classification/value rather than as a represented actor may be LABEL instead. Permit cross-class overlap only if the source independently establishes both functions.

## 7. OBJECT — stable things/content participating in bindings

OBJECT is a source-distinguished concrete or abstract referent treated as a stable thing/content in a material binding.

Use a **concrete-role retain bias**: if the source distinguishes a concrete thing, part, component, artifact, material, container/content, support, environmental object, or comparison object and it materially participates in a binding, retain it even when it is background or nested. Do not collapse source-distinguished whole/part or container/content coordinates solely because they occur together.

Abstract/content OBJECT may include a decision, choice, amount, result, relation/set, topic, mental content, or figurative referent only when the source itself treats it as a stable revisitable thing/content in a binding.

Do not create OBJECT for every event, action, state, clause complement, proposition, pronoun/deictic, or analyst-created nominalization. If the content exists only as a wrapper around already represented participants/relations/values, omit the wrapper unless the source independently reifies it.

Concrete wording can coexist with PLACE/LOCATOR only when separate positive roles are source-supported.

## 8. LABEL — foregrounded source-presented values/classifications

LABEL is a foregrounded characterization, state, value, classification, evaluation, comparison, identity/self-label, social-role classification, relational status, polarity response, correction, or question-label that participates as a reusable value role in a material binding.

Use the shortest complete wording that preserves target, polarity, comparison, uncertainty, correction, or question posture.

Do not census ordinary descriptive adjectives/adverbs, intensifiers, discourse emphasis, generic qualities, incidental modifiers, or every evaluative-sounding token. A value qualifies because the source foregrounds it as the classified/evaluated/state role of a binding, not because it is adjective-shaped.

Noun phrases may be LABEL when the source uses them as classifications rather than represented actors/things. Negation/interrogation may be part of a LABEL when the polarity/classification itself is foregrounded.

## 9. VERB — material lexical relation atoms

VERB is the shortest complete lexical relation identity for a material represented binding.

Retain a lexical relation when it independently binds or changes represented coordinates. Reporting, cognition, perception, possession, stance, copular/locative relation, movement, questioning, saying/telling, finding, waiting, comparison, and figurative relation can qualify when they perform a material binding job.

Merge particles, required complements, negation/modal material, fixed idioms, or serial/control material when they jointly form one inseparable relation identity. Split nested/reported/coordinated relations only when the source presents two materially distinct binding jobs and each survives removal of the other as a represented relation.

Exclude pure conversational floor-management, filler, speech-performance mechanics, stage/pantomime mechanics, bare metacognitive scaffolding, discourse transitions, and syntactic subpredicates that do not create a distinct material binding. Do not duplicate a source value as VERB merely because grammar uses a copula if LABEL carries the substantive role.

## 10. LOCATOR — reusable orientation edges

LOCATOR is the smallest source-native orientation relation that materially positions one represented coordinate/binding relative to another position, path, direction, origin/destination, entry/exit, containment, support/surface, accompaniment/carrying, proximity/distance, recurrence/temporal position, or figurative/internal orientation.

LOCATOR is not restricted to prepositional phrases; movement or standing expressions may qualify when their material job is orientation.

Reject topical/content complements, ordinary recipient/beneficiary arguments, generic prepositional arguments, bare dates/durations, and relation arguments that do not independently orient a retained coordinate/binding.

Do not suppress a genuine LOCATOR merely because the same source material also establishes a PLACE or TIME coordinate. Keep both only when the source independently supports the frame/scene role and the orientation-edge role.

## 11. Cross-class resolution

Classify by positive role in the represented binding/frame, not part of speech:

- represented actor/group -> PERSON;
- stable participating thing/content -> OBJECT;
- foregrounded value/classification/state -> LABEL;
- material lexical relation -> VERB;
- reusable orientation edge -> LOCATOR;
- physical occurrence-position anchor -> PLACE;
- episode/period/frame anchor -> TIME.

Cross-class overlap is permitted only when the same source material performs two independent positive roles. Before retaining overlap, state internally the two different roles. Shared wording, grammar, or convenience is insufficient.

## 12. Literal/posture lock

Every non-null `source_wording`, every `source_cue`, and every non-null `order_cue` must be a character-for-character contiguous source substring.

Preserve spelling, punctuation, dialect, contractions, singular/plural form, questions, negation, uncertainty, correction, comparison, attribution, intention, hypothetical, recurrence, report, and prospective posture exactly. Never substitute a synonym, standardize dialect, repair grammar, or normalize the source into a cleaner term.

Short tags should use source wording whenever a named coordinate exists. Supported unnamed PLACE/TIME may use neutral navigation tags grounded by exact source cues.

## 13. Ordering and qualities

Order by first source establishment after coreference, with speaker-first PERSON and broad-before-contained PLACE only when genuinely established together.

`qualities_available` is boolean. Set true only when source qualities/descriptions are available for that coordinate/compound. Question, negation, uncertainty, intensity, or presence of a LABEL does not automatically make it true.

## 14. Compound reconstruction — one material binding, one complete skeleton

Freeze all admitted primitives before compounds.

Return to the material binding ledger. Emit one smallest complete compound for each materially distinct source-presented binding that requires cross-coordinate representation.

A compound includes every **frozen** primitive materially bound in that one relation instance, as applicable:

- participant(s);
- material lexical relation atom(s);
- acted-on/discussed stable object/content;
- foregrounded value/classification/polarity;
- source-supported TIME and PLACE anchor(s) for that binding;
- independently retained LOCATOR edge(s) that orient it.

Do not make a compound for every clause. Do not generate pairwise/combinatorial closure. Do not emit nested subset alternatives for the same binding. Do not create sentence bags containing neighboring but unbound units. Do not reference a primitive that was rejected or never frozen.

If one binding contains two inseparable retained VERB atoms, one compound may include both. If the source establishes two distinct bindings, use separate compounds even when they occur in the same sentence.

`referenced_unit_refs` must contain only frozen admitted units. `compound_expression` must preserve their source order.

Before finalizing compounds perform:

- **binding completeness check:** no frozen coordinate materially participating in that binding is omitted;
- **binding exclusivity check:** no nearby coordinate is included merely because it appears in the same clause/sentence;
- **reference integrity check:** every referenced unit exists in the frozen primitive inventory.

## 15. Calibration isolation

Return only the JSON required by the request schema. Never infer or reconstruct archetypes, expected counts, evaluator preferences, prior scored outputs, case-specific corrections, sealed holdout source during calibration, or holdout output.

Do not reason from an imagined evaluator. Apply this contract to the supplied source only.

## 16. Prohibited work

Never perform APA scoring, psychological interpretation, protected-thread analysis, conclusions, promotion, APA-ID creation, Oval Office research writing, sovereign admission, or database/fabric admission.

## 17. Successor effect

V58 prospectively supersedes V57 only for new Researcher Inventory calibration/certification work beginning 2026-09-16. V57 and all earlier contracts and runs remain immutable historical evidence.

V58 preserves V57's complete-source reading, structural awareness, coreference, literal/posture lock, source ordering, class/function resolution, evaluator isolation, candidate-only status, and sealed-holdout gates. It supersedes V57's free-standing coverage-first primitive sweep with a relation-anchored binding/frame ledger followed by symmetric excess and gap checks. This is the generalizable correction demonstrated by preserved V57 failures: avoid both global-minimum under-selection and lexical/semantic census over-selection while reconstructing source-distinguished material bindings completely.

Immutable archetype hashes, repeated paired-archetype gate, one-shot sealed Case 5 semantics, fresh-agent clean-room certification, and all promotion/APA-ID/database prohibitions remain unchanged.
