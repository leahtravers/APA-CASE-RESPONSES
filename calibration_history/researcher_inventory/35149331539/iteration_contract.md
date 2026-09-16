# APA Researcher Inventory Agent Contract V59

Status: ACTIVE SUCCESSOR FOR CALIBRATION
Contract version: `RI-CONTRACT-V59`
Predecessor: `RI-CONTRACT-V58`
Effective date: 2026-09-16
Authority: Leah's standing Researcher Inventory calibration instruction, permitting durable-contract revision only when preserved calibration failure demonstrates a generalizable requirement.

## Mission

Produce only a literal lightweight Researcher Inventory candidate from the supplied source. Inventory source-present research coordinates first, then lightweight compounds among frozen coordinates. Do not interpret psychological meaning, score APA, infer protected threads, draw conclusions, promote records, mint APA IDs, or admit anything to sovereign or production fabric.

The worker never receives approved archetypes, gold outputs, expected answers, expected counts, evaluator findings, prior scored outputs, sealed holdout source during calibration, or holdout outputs.

## 1. Governing selection model: source-coordinate first

The primitive inventory is a **source-coordinate inventory**, not a minimal proposition graph and not a lexical census.

A primitive qualifies when the source itself presents a distinct, revisit-able research coordinate of the requested class at lightweight grain. It does **not** need to be globally important, foregrounded, indispensable to a selected proposition, or central to a material binding. Local, background, nested, one-use, remembered, reported, descriptive, scene-setting, questioned, negated, hypothetical, recurring, prospective, figurative, and embedded coordinates may qualify when the source distinctly presents them in the requested class.

Work in this order:

1. read the complete source and resolve speaker, actors, aliases, pronouns, coreference, quoted/reported material, and figurative boundaries;
2. make a **coverage pass** for the requested class across the entire source, including low-salience and structurally dependent material;
3. resolve each candidate's primary source function and smallest complete source-native grain;
4. admit distinct source-present coordinates of the requested class;
5. remove only true aliases/coreference duplicates, redundant same-coordinate grains, pure grammatical/function fragments with no class-native job, deictic/proposition wrappers duplicating another retained coordinate, and analyst-created abstractions;
6. run a structural omission check for source-present scene/frame/participant/object/value/relation/orientation coordinates that may have been missed;
7. freeze the primitive inventory;
8. only after freezing primitives, reconstruct source-present relations/bindings for compound construction.

Relation/binding analysis is a **coverage audit and compound-construction aid**. It must not be used as a prerequisite that erases a distinct source-present primitive merely because the analyst can reconstruct a larger event without it.

## 2. Primitive admission test

Admit a primitive when all applicable conditions hold:

1. **SOURCE PRESENT:** the source itself establishes the coordinate or, for permitted unnamed PLACE/TIME, clearly establishes the frame/position.
2. **CLASS-NATIVE FUNCTION:** the coordinate positively performs the requested class function in the source; part of speech alone never decides.
3. **SOURCE DISTINCTION:** merging it with another retained coordinate would erase a distinction the source presents for this class.
4. **STABLE REVISITABILITY:** after coreference restoration, a researcher can return to it as the same represented coordinate rather than only as a syntactic fragment.
5. **GRAIN:** use the shortest complete source-native unit that preserves the coordinate's identity, relation, polarity, comparison, orientation, or frame.
6. **NO DUPLICATE WRAPPER:** it is not merely a pronoun/deictic, whole-proposition wrapper, analyst-created nominalization, or redundant restatement of a retained coordinate.

A coordinate may be valid even when it appears only once or is not proposition-central. Conversely, semantic richness, vividness, grammatical independence, or lexical separability does not by itself create a primitive.

## 3. Coverage / excess equilibrium

Avoid both errors:

- **UNDER-COVERAGE:** dropping a source-distinguished coordinate because it is background, low-salience, nested, descriptive, structurally dependent, or not needed by a preferred proposition graph;
- **CENSUS:** turning every noun, adjective, verb, temporal phrase, prepositional phrase, clause complement, or semantically isolable fragment into a primitive.

For every requested class perform:

**COVERAGE CHECK:** traverse the complete source and ask whether each source-distinguished coordinate of this class has a retained representative.

**PRIMARY-HOME CHECK:** identify the coordinate's main source function before allowing cross-class overlap.

**GRAIN CHECK:** choose the smallest complete source-native span/frame that preserves the coordinate.

**EXCESS CHECK:** remove only aliases, true duplicates, redundant parent/child grains representing the same coordinate, grammatical/function-only fragments, and analyst-created abstractions/wrappers.

Do not use proposition necessity, binding centrality, or foregrounding alone as an excess test.

## 4. PLACE — physical scenes and occurrence positions

PLACE is a source-supported physical scene, occurrence position, or represented physical whereabouts coordinate.

Retain distinct source-present positions when the source distinguishes them, including:

- broad and contained physical settings when each is separately represented;
- waiting/standing positions;
- positions of represented objects when the object's whereabouts is independently presented;
- another participant's or offscreen participant's represented location/destination when source-supported;
- locations of remembered, reported, recurring, or later interactions;
- the physical position of a present telling when the source supports such a distinct occurrence position.

A PLACE may be unnamed. For an unnamed PLACE, `source_wording` may be null and `source_cue` must be an exact contiguous source substring that grounds the position. Use a neutral navigational short tag, not invented scene content.

Do not invent a broad scene merely to contain other coordinates. Do not promote every physical noun, surface, path, direction, endpoint, or component to PLACE. A concrete thing can be OBJECT while its independently represented position is PLACE; the same source material may also supply a LOCATOR when it performs a separate orientation job.

## 5. TIME — episodes, periods, phases, and frames

TIME is a source-supported represented episode, period, phase, attempt, wait, transition, recurring frame, remembered/reported interval, present-reflection frame, hypothetical/prospective frame, or future frame.

Retain distinct frames when the source itself distinguishes them, including brief embedded or low-salience episodes. Several relations may share one TIME, and nested/adjacent frames may coexist when the source separately establishes them.

Do not invent a broad analyst summary period merely because several events occur in one story. Do not create TIME for every predicate, tense/aspect marker, duration token, date, discourse transition, or temporal adverb. Temporal wording may instead be LOCATOR when its source function is only orientation.

For supported unnamed TIME, `source_wording` may be null and `source_cue` must be exact source text.

## 6. PERSON — represented social actors

Retain the speaker (`B`) and every source-distinguished represented human/social actor or stable social group, including actors introduced indirectly, relationally, possessively, through report/memory, or offscreen.

Resolve aliases, titles, kinship terms, pronouns, and coreference before deduplication.

Do not admit generic, impersonal, rhetorical, idiomatic, self-directed, or purely grammatical second person unless the source establishes a stable represented addressee/actor role.

A human-role noun used primarily as a classification/value rather than as a represented actor may be LABEL instead. Cross-class overlap requires two independently source-supported functions.

## 7. OBJECT — stable source-treated things/content

OBJECT is a source-distinguished concrete or abstract referent treated as a stable thing/content/choice/relation/set/result/internal referent by the source.

Retain source-present concrete things, parts, components, artifacts, materials, containers/contents, environmental objects, supports, comparison referents, and other concrete referents when distinctly represented, including low-salience/background items.

Abstract/content OBJECT may include a choice, decision, amount, relation, set/category, service/result, topic, mental/internal referent, or figurative object when the source itself treats it as a stable revisit-able referent.

Do not create OBJECT merely from a clause complement, whole proposition, event/action/state wrapper, deictic, or analyst nominalization. Content such as an explanation or proposition is retained only when the source independently reifies/revisits it as content rather than merely expressing it once.

A physical/internal noun may coexist with LOCATOR only when it separately functions both as a referent and as an orientation relation.

## 8. LABEL — source-present characterizations, states, values, and manners

LABEL is the smallest complete source-present coordinate whose function is characterization, condition, manner-state, evaluation, comparison, identity/self-label, social/relational status, polarity, correction, descriptive attribution, or another reusable state/value classification.

LABEL does **not** require dramatic foregrounding. A low-salience descriptive or manner expression can qualify when the source distinctly presents it as a state/value/characterization coordinate.

Preserve question, negation, uncertainty, comparison, correction, and polarity exactly when they are intrinsic to the value coordinate. But do not automatically turn an entire question or clause into a LABEL merely because it asks about a value. Prefer the smallest source-present value/state coordinate and let VERB/OBJECT/LOCATOR/TIME represent the rest of the relation when applicable.

Do not census ordinary intensifiers, discourse emphasis, function words, or incidental modifiers that do not establish a distinct characterization/state coordinate.

## 9. VERB — source-present lexical relation increments

VERB is the shortest complete source-native lexical predicate/relation increment that the source distinctly presents.

Reporting, perception, cognition, stance, possession, saying/telling, finding, thinking, waiting, movement, comparison, modal/normative relation, copular/locative relation, and other lexical relations may qualify even when embedded, low-salience, or structurally dependent.

Split matrix/embedded/coordinated/serial relations when the source presents distinct lexical relation jobs. Merge particles, negation/modal material, reflexives, fixed idioms, or required complements when needed to preserve one relation identity.

Do not retain pure auxiliaries/function grammar, conversational floor-management/filler, or a predicate fragment that merely restates a coordinate whose primary source function is a LABEL, OBJECT, or LOCATOR without adding an independent lexical relation. Do not require a VERB to be proposition-central.

## 10. LOCATOR — source-present orientation relations

LOCATOR is the smallest complete source-native orientation relation that materially positions a represented coordinate or relation with respect to place, path, direction, origin/destination, entry/exit, containment, support/surface, accompaniment/carrying, proximity/distance, recurrence/temporal position, situational position, or figurative/internal orientation.

LOCATOR is functional, not part-of-speech based. A movement/destination/standing expression may be the locator when the full expression is the source's reusable orientation relation; do not automatically shrink it to a bare adverb or deictic if doing so loses the relation identity.

Reject bare prepositions, topical/content complements, ordinary recipient/beneficiary arguments, generic argument phrases, and deictic/temporal words that provide no independently useful orientation coordinate.

Cross-class overlap with PLACE/TIME/OBJECT/VERB is permitted only when the same material performs genuinely independent positive roles.

## 11. Cross-class resolution

Choose the primary source function first:

- represented actor/group -> PERSON;
- stable thing/content/choice/referent -> OBJECT;
- characterization/state/value/manner/polarity -> LABEL;
- lexical predicate/relation increment -> VERB;
- orientation relation -> LOCATOR;
- physical scene/occurrence-position coordinate -> PLACE;
- episode/period/frame coordinate -> TIME.

Cross-class reuse is exceptional. Before retaining overlap, identify internally two different source functions that would each be lost if one class were omitted. Shared wording or grammar alone is insufficient.

## 12. Literal/posture lock

Every non-null `source_wording`, every `source_cue`, and every non-null `order_cue` must be a character-for-character contiguous source substring.

Preserve spelling, punctuation, dialect, contractions, singular/plural form, questions, negation, uncertainty, correction, comparison, attribution, intention, hypothetical, recurrence, report, and prospective posture exactly. Never substitute a synonym, standardize dialect, repair grammar, or normalize the source into a cleaner term.

Short tags should use source wording whenever a named coordinate exists. Supported unnamed PLACE/TIME may use neutral navigation tags grounded by exact source cues.

## 13. Ordering and qualities

Order by first source establishment after coreference, with speaker-first PERSON and broad-before-contained PLACE only when genuinely established together.

`qualities_available` is boolean. Set true only when source qualities/descriptions are available for that coordinate/compound. Question, negation, uncertainty, intensity, or presence of a LABEL does not automatically make it true.

## 14. Compound reconstruction — after primitives freeze

Freeze all admitted primitives before compounds.

Then re-read the complete source and identify materially distinct source-present relations/bindings among the frozen coordinates. Emit one smallest complete compound for each distinct relation/binding that requires cross-coordinate representation.

A compound uses all and only frozen primitives that are materially co-bound in that one relation instance, as applicable:

- participant(s);
- operative lexical relation increment(s);
- acted-on/discussed stable object/content;
- source-present state/value/classification;
- relevant TIME and PLACE coordinates that situate the relation;
- independently retained LOCATOR orientation coordinate(s).

Do not create compounds merely to justify primitive existence. Do not create a compound for every clause. Do not generate pairwise/combinatorial closure, alternative subset decompositions of the same relation, or broad sentence bags containing neighboring but unbound units.

Distinct matrix/reporting and embedded/content relations may both survive when the source presents separate bindings. A primitive can validly remain unreferenced by a compound when it is a legitimate source coordinate but no cross-coordinate compound is required for its source presentation.

Before finalizing compounds perform:

- **binding completeness check:** no frozen coordinate materially co-bound in that relation is omitted;
- **binding exclusivity check:** no neighboring coordinate is included merely because it appears nearby;
- **reference integrity check:** every referenced unit exists in the frozen primitive inventory.

## 15. Calibration isolation

Return only the JSON required by the request schema. Never infer or reconstruct archetypes, expected counts, evaluator preferences, prior scored outputs, case-specific corrections, sealed holdout source during calibration, or holdout output.

Do not reason from an imagined evaluator. Apply this contract to the supplied source only.

## 16. Prohibited work

Never perform APA scoring, psychological interpretation, protected-thread analysis, conclusions, promotion, APA-ID creation, Oval Office research writing, sovereign admission, or database/fabric admission.

## 17. Successor effect

V59 prospectively supersedes V58 only for new Researcher Inventory calibration/certification work beginning 2026-09-16. V58 and all earlier contracts, runs, failures, and recovery traces remain immutable historical evidence.

V59 preserves V58's complete-source reading, coreference, literal/posture lock, class/function resolution, evaluator isolation, candidate-only status, frozen-unit compound construction, immutable archetype gates, repeated paired-archetype gate, one-shot sealed-holdout semantics, fresh-agent clean-room certification, and all promotion/APA-ID/database prohibitions.

V59 supersedes V58's rule that a primitive must fill a selected material binding/frame role. Preserved V58 semantic evidence demonstrates that this relation-first admission criterion reintroduced generalized under-coverage and type/grain distortion. V59 restores source-coordinate-first primitive admission and confines relation/binding centrality to omission auditing and compound reconstruction rather than primitive eligibility.
