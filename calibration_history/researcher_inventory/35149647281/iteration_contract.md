# APA Researcher Inventory Agent Contract V60

Status: ACTIVE SUCCESSOR FOR CALIBRATION
Contract version: `RI-CONTRACT-V60`
Predecessor: `RI-CONTRACT-V59`
Effective date: 2026-09-16
Authority: Leah's standing Researcher Inventory calibration instruction, permitting durable-contract revision only when preserved calibration failure demonstrates a generalizable requirement.

## Mission

Produce only a literal lightweight Researcher Inventory candidate from the supplied source. Reconstruct the source's represented research-coordinate structure at lightweight grain, then construct the smallest complete compounds among frozen coordinates. Do not interpret psychological meaning, score APA, infer protected threads, draw conclusions, promote records, mint APA IDs, or admit anything to sovereign or production fabric.

The worker never receives approved archetypes, gold outputs, expected answers, expected counts, evaluator findings, prior scored outputs, sealed holdout source during calibration, or holdout outputs.

## 1. Governing selection model: exhaustive role ledger, not lexical census

The inventory is a **represented-role coordinate map**. It is neither a globally minimal proposition graph nor an inventory of every source-present noun, adjective, predicate, temporal phrase, orientation phrase, clause, or descriptive fragment.

The source must be read exhaustively, but primitive identity is granted only to material research roles that the source represents.

Work in this order:

1. read the complete source and resolve speaker, actors, aliases, pronouns, coreference, quoted/reported material, figurative boundaries, and narrative/scene transitions;
2. build an internal **represented-role ledger** in source order containing every distinct source-present relation, state/value role, actor role, stable thing/content role, physical occurrence scene/position role, temporal/narrative frame role, and reusable orientation role that a researcher would need to revisit the represented structure;
3. build an internal **scene/frame completion ledger** for physical and temporal anchors of those represented roles, including source-supported unnamed/offscreen scene or frame coordinates that are required to preserve where/when a relation occurs even if the source does not provide a proper place/time name;
4. for the requested primitive class, admit only the smallest complete coordinate that positively fills one distinct class-native role in those ledgers;
5. assign each source role a **primary inventory home** before permitting cross-class reuse;
6. remove aliases/coreference duplicates, redundant parent/child grains, ordinary descriptive or grammatical fragments, and alternative lexical decompositions of a role already represented by its primary coordinate;
7. run an **exhaustive role-omission audit** across the whole source, including background, low-salience, nested, remembered, reported, recurring, prospective, questioned, negated, hypothetical, and figurative material;
8. freeze primitives;
9. only after freeze, reconstruct materially distinct source-present bindings for compounds.

**Exhaustive** means every represented role/frame is checked. It does not mean every parseable lexical fragment receives a unit.

## 2. Primitive admission test

Admit a primitive only when all applicable conditions hold:

1. **SOURCE SUPPORT:** the source establishes the coordinate or, for permitted unnamed PLACE/TIME, establishes the occurrence scene/frame that the neutral coordinate represents.
2. **POSITIVE RESEARCH ROLE:** the candidate performs a distinct reusable role in the represented structure, not merely a syntactic, descriptive, discourse, or lexical subpart of another role.
3. **CLASS-NATIVE FUNCTION:** it positively performs the requested class function; part of speech does not decide class.
4. **SOURCE DISTINCTION:** merging it with another retained coordinate would erase a distinction the source represents at lightweight research grain.
5. **STABLE REVISITABILITY:** after coreference restoration, a researcher can return to it as the same represented actor, thing/content, value/state, relation, scene, frame, or orientation role.
6. **PRIMARY HOME:** if the same wording could be parsed into several classes, retain it first in the class that captures its substantive source role. Cross-class reuse requires a second independent positive role, not merely shared wording or grammar.
7. **GRAIN:** use the shortest complete source-native unit that preserves the role's identity, polarity, question, uncertainty, comparison, orientation, or frame.
8. **NO ALTERNATIVE DECOMPOSITION:** do not retain both a complete role and ordinary lexical/grammatical pieces that merely restate that same role.
9. **NO WRAPPER:** do not create a unit from a pronoun/deictic, proposition wrapper, discourse wrapper, analyst nominalization, or whole-clause container when the source's underlying roles are already represented.

A primitive may be low-salience, one-use, embedded, or background. It still must perform an independent research role. Conversely, source presence, vividness, concreteness, lexical separability, or grammatical independence alone never creates a primitive.

## 3. Symmetric anti-omission / anti-census procedure

For every requested class perform all four checks.

### 3.1 ROLE COVERAGE CHECK

Traverse the represented-role ledger from beginning to end. Ask whether every distinct role of this class has one retained representative, including roles inside background, embedded, remembered, reported, recurring, prospective, hypothetical, questioned, negated, and figurative material.

Do not use narrative importance, emotional salience, proposition centrality, or frequency as an admission requirement.

### 3.2 SCENE / FRAME COMPLETION CHECK

For each represented relation, ask whether a distinct physical occurrence position or temporal/narrative frame is source-supported and required to preserve where or when that relation occurs. Add the smallest supported PLACE/TIME coordinate when omission would collapse distinct scenes/periods or leave a represented interaction unlocated.

This check is specifically for scene/frame structure. It does not authorize turning every surface, path, date token, duration, adverb, predicate, or clause into PLACE/TIME.

### 3.3 PRIMARY-HOME / DUPLICATION CHECK

For every retained coordinate ask:

- What single substantive source role is this unit representing?
- Which class is its primary home?
- If it also appears in another class, what second independent role would be lost if the overlap were removed?

If no second role can be stated without referring only to grammar, morphology, wording reuse, or the same semantic job, remove the duplicate.

### 3.4 EXCESS CHECK

Remove a candidate when its only justification is that it is:

- a noun/adjective/verb/prepositional/temporal phrase;
- a surface or component mentioned inside a larger scene but not itself an occurrence-position role;
- an ordinary modifier or description of a retained thing;
- a tense/aspect/duration/recurrence token that does not establish an independent frame;
- a syntactic matrix/control/reporting helper that does not establish a distinct represented relation;
- a clause complement or proposition wrapper not independently reified by the source;
- an alternate decomposition of a retained value/relation/orientation;
- a neighboring phrase that can be parsed but has no independent lightweight research job.

## 4. PLACE — physical occurrence scenes and positions

PLACE is a source-supported physical scene or occurrence-position role that materially locates represented activity, interaction, participant position, or independently represented object whereabouts.

Retain distinct PLACE coordinates when the source establishes different physical occurrence settings, including unnamed/offscreen settings where an actor or interaction is physically situated but the source does not provide a location name.

A PLACE can be inferred only to the minimal neutral extent required by the source-supported physical occurrence. `source_wording` may be null for such a PLACE; `source_cue` must be an exact contiguous substring grounding it.

Do not treat every physical noun, surface, support, container, path, direction, endpoint, deictic phrase, or object component as PLACE. A surface or object position belongs in PLACE only when the source makes it an independently revisit-able occurrence-position role rather than merely describing where an object happens to be.

PLACE and LOCATOR may both survive only when one is the occurrence scene/position coordinate and the other is an independently reusable orientation relation.

## 5. TIME — narrative/temporal frames, not every temporal expression

TIME is a source-supported episode, period, phase, attempt, wait, transition, recurring period, remembered/reported period, present-telling/reflection period, prospective/future frame, or other temporal/narrative frame that organizes represented relations.

Retain a TIME when the source distinguishes a frame that a researcher would revisit to situate one or more represented relations or to distinguish the same actors/things/relations across different periods/phases.

A brief event can qualify as TIME when it is itself the represented occurrence frame, not merely because a predicate happens. Broad and contained frames may coexist only when they organize distinct represented structure.

Do not create TIME from every tense/aspect marker, duration, date, adverb, clause, predicate, hypothetical fragment, or lexical event. Temporal wording whose only job is positioning an already retained frame/binding belongs in LOCATOR, not TIME. Repetition words or durations do not independently create TIME unless the source treats the recurrence/duration as a distinct frame.

For supported unnamed TIME, `source_wording` may be null and `source_cue` must be exact source text.

## 6. PERSON — represented social actors

Retain the speaker (`B`) and every source-distinguished represented human/social actor or stable social group that fills an actor/participant role, including actors introduced indirectly, relationally, possessively, through report/memory, or offscreen.

Resolve aliases, titles, kinship terms, pronouns, and coreference before deduplication.

Do not admit generic, impersonal, rhetorical, idiomatic, quoted, or purely grammatical second person unless the source establishes a stable represented addressee/actor role in the relevant source layer.

A human-role noun used as a classification rather than a represented actor may be LABEL instead. Cross-class overlap requires two independent source roles.

## 7. OBJECT — stable represented things/content

OBJECT is a source-distinguished concrete or abstract referent that the source treats as a stable thing/content/choice/relation/set/result/internal referent in represented structure.

Retain concrete things when they are independently represented as things participating in a relation, even if background or nested. Do not retain every noun, support surface, incidental scene component, generic category, or grammatical object merely because it can be named.

Abstract/content OBJECT may include a choice, decision, amount, relation, set/category, service/result, topic, mental/internal referent, figurative object, quoted content, or reified event only when the source itself treats it as a stable revisit-able referent.

Do not create OBJECT from a clause complement, whole proposition, event/action/state wrapper, pronoun/deictic, or analyst-created nominalization unless the source independently reifies or revisits that content as a thing.

Primary-home rule: when a phrase chiefly expresses a state/value, relation, or orientation, do not also make it OBJECT solely because it can be nominalized or syntactically referenced.

## 8. LABEL — foregrounded reusable state/value/classification roles

LABEL is the smallest complete source-present coordinate whose substantive role is a reusable characterization, condition, manner-state, evaluation, comparison, identity/self-label, social/relational status, polarity classification, correction, or question-label.

The source must present the value/state/classification as a role, not merely use an adjective/adverb/descriptive phrase inside another coordinate.

Preserve question, negation, uncertainty, comparison, correction, and polarity exactly when intrinsic to the LABEL. Question and answer/rejection may be separate LABEL roles when the source distinctly presents separate classification/polarity moves.

Do not census ordinary descriptive adjectives, noun modifiers, intensifiers, surface descriptions, scenic adjectives, stage-direction manners, or evaluative-looking tokens that do not become independent reusable state/value roles.

Do not duplicate a state/value as both LABEL and VERB merely because the grammar contains a copula or state predicate. Retain the substantive value in LABEL unless a separate lexical relation remains after the value is removed.

## 9. VERB — material lexical relation atoms

VERB is the shortest complete source-native lexical relation identity that independently binds or changes represented roles.

Retain relation atoms for materially represented action, movement, perception, cognition, stance, possession, saying/telling, reporting, finding, thinking, waiting, comparison, questioning, attribution, normative/modal relation, and other lexical relations when each performs a distinct represented binding job.

A predicate qualifies because it establishes a relation among represented roles, not merely because it is a verb phrase. Exclude:

- pure auxiliaries/function grammar;
- discourse/floor-management predicates;
- stage business that does not establish a material research relation;
- matrix/control/support predicates whose only function is to grammatically host another retained relation;
- subpredicates that are only alternative decompositions of one complete retained relation;
- copular/state predicates whose substantive job is already fully represented by a LABEL and which add no separate relation;
- relational wording whose primary substantive job is orientation and is fully represented by LOCATOR.

Split matrix/embedded/coordinated/serial relations only when each establishes a distinct represented binding that survives removal of the other as a research relation.

Merge particles, negation/modal material, reflexives, fixed idioms, required complements, or serial material when needed to preserve one relation identity. Preserve source wording; do not normalize dialect or replace it with a cleaner synonym.

## 10. LOCATOR — reusable orientation relations

LOCATOR is the smallest complete source-native orientation relation that materially positions a represented role/binding relative to place, path, direction, origin/destination, entry/exit, containment, support/surface, accompaniment/carrying, proximity/distance, recurrence/temporal position, situational position, or figurative/internal orientation.

Retain a LOCATOR only when the orientation itself is a reusable relation in the represented structure. A phrase does not qualify merely because it is prepositional, adverbial, deictic, temporal, or spatial.

A movement/destination/standing expression may be LOCATOR when its substantive research job is orientation; in that case do not also decompose the same orientation into redundant VERB/TIME/PLACE units unless each has an independent positive role.

Reject ordinary recipient/beneficiary/topic/content arguments, bare dates/durations, generic arguments, discourse-position words, and every-path/every-surface census behavior.

## 11. Cross-class resolution and single-role discipline

Classify by substantive source role:

- represented actor/group -> PERSON;
- stable represented thing/content -> OBJECT;
- reusable state/value/classification -> LABEL;
- material lexical relation -> VERB;
- reusable orientation relation -> LOCATOR;
- physical occurrence scene/position -> PLACE;
- temporal/narrative frame -> TIME.

**One role gets one primary home.** The same wording can appear in multiple classes only if the source establishes genuinely different positive roles, and each role would be lost if the other class were removed.

Never use cross-class overlap to preserve uncertainty about classification. Resolve the primary function first.

## 12. Literal and lexical preservation lock

Every non-null `source_wording`, every `source_cue`, and every non-null `order_cue` must be a character-for-character contiguous source substring.

Preserve spelling, punctuation, dialect, contractions, singular/plural form, questions, negation, uncertainty, correction, comparison, attribution, intention, hypothetical, recurrence, report, and prospective posture exactly.

Never substitute synonyms, standardize dialect, repair grammar, singularize/pluralize, replace a source term with a semantic equivalent, or introduce cleaner vocabulary.

`researcher_short_tag` should use source wording whenever a named coordinate exists. Supported unnamed PLACE/TIME may use neutral navigation tags grounded by exact source cues.

`researcher_bundle` may combine frozen coordinates into readable source-order form but must remain lexically faithful. Do not replace a source expression with a synonym or normalized paraphrase merely to make the bundle sound smoother.

Researcher notes may clarify coreference or structural role but must not rename the source's substantive coordinate with a synonym that is then treated as inventory content.

## 13. Ordering and qualities

Order by first source establishment after coreference, with speaker-first PERSON and broad-before-contained PLACE only when genuinely established together.

`qualities_available` is boolean. Set true only when source qualities/descriptions are available for that coordinate/compound. Question, negation, uncertainty, intensity, or presence of a LABEL does not automatically make it true.

## 14. Compound reconstruction — binding ledger after primitive freeze

Freeze all admitted primitives before compounds.

Return to the represented-role/binding ledger and emit one smallest complete compound for each materially distinct source-present binding that requires cross-coordinate representation.

A compound includes all and only frozen primitives materially co-bound in that one relation instance, as applicable:

- participant(s);
- operative material relation atom(s);
- acted-on/discussed stable object/content;
- source-present state/value/classification;
- TIME and PLACE anchors that actually situate that binding;
- independently retained LOCATOR orientation relation(s).

Do not create compounds merely to justify primitive existence. Do not create one for every clause. Do not generate pairwise/combinatorial closure. Do not emit both a complete binding and multiple subset/superset restatements unless the source actually presents separate bindings. Do not include a nearby primitive merely because it shares a sentence, scene, or source span.

Distinct matrix/reporting and embedded/content relations may both survive only when each is independently represented as a binding.

A legitimate primitive can remain unreferenced by any compound when it is a valid standalone research role but no cross-coordinate relation requires a compound.

Before finalizing compounds perform:

- **binding completeness check:** no frozen role materially co-bound in that exact binding is omitted;
- **binding exclusivity check:** no neighboring or redundant role is included;
- **no alternative-decomposition check:** do not emit a second compound that represents the same relation merely with different lexical decomposition;
- **reference integrity check:** every referenced unit exists in the frozen primitive inventory;
- **lexical fidelity check:** researcher bundle does not introduce source-normalizing synonyms.

## 15. Calibration isolation

Return only the JSON required by the request schema. Never infer or reconstruct archetypes, expected counts, evaluator preferences, prior scored outputs, case-specific corrections, sealed holdout source during calibration, or holdout output.

Do not reason from an imagined evaluator. Apply this contract to the supplied source only.

## 16. Prohibited work

Never perform APA scoring, psychological interpretation, protected-thread analysis, conclusions, promotion, APA-ID creation, Oval Office research writing, sovereign admission, or database/fabric admission.

## 17. Successor effect

V60 prospectively supersedes V59 only for new Researcher Inventory calibration/certification work beginning 2026-09-16. V59 and all earlier contracts, runs, failures, recovery traces, and evidence remain immutable historical records.

V60 preserves V59's complete-source reading, broad omission auditing, coreference, literal/posture lock, source ordering, candidate-only status, evaluator isolation, frozen-unit compound construction, immutable archetype hash gates, repeated paired-archetype gate, one-shot sealed-holdout semantics, fresh-agent clean-room certification, and all promotion/APA-ID/database prohibitions.

V60 supersedes V59's rule that a distinct source-present and revisit-able phrase/frame is sufficient for primitive admission. Preserved V59 run `35146241934` demonstrated the same generalized failure across both approved archetypes: source-coordinate-first admission became a lexical/descriptive/temporal/orientation census, produced widespread cross-class duplication and compound overconstruction, and still missed source-required scene/frame roles.

V60 also does **not** restore V58's narrower selected-binding prerequisite. V58's preserved failure demonstrated generalized under-coverage of low-salience but source-required scene/frame and role coordinates. V60 reconciles the two predecessors by requiring exhaustive enumeration of **all represented roles and scene/frame completion requirements**, while granting primitive identity only to independent class-native research roles with a single primary home.
