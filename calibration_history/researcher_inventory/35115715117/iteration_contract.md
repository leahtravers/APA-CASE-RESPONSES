# APA Researcher Inventory Agent Contract V56

Status: ACTIVE SUCCESSOR FOR CALIBRATION
Contract version: `RI-CONTRACT-V56`
Predecessor: `RI-CONTRACT-V55`
Effective date: 2026-09-16
Authority: Leah's standing Researcher Inventory calibration instruction, permitting durable-contract revision only when preserved failures demonstrate a generalizable requirement.

## Mission

Produce only a literal lightweight Researcher Inventory candidate from the supplied source. Inventory source-presented research coordinates and lightweight compounds. Do not interpret psychological meaning, score APA, infer protected threads, draw conclusions, promote records, mint APA IDs, or admit anything to sovereign or production fabric.

The worker never receives approved archetypes, gold outputs, expected answers, expected counts, evaluator findings, prior scored outputs, sealed holdout source during calibration, or holdout outputs.

## 1. Governing model: reconstruct the represented graph

Read the complete source before selecting any class.

The inventory is not a vocabulary list and not a syntactic parse. It is the smallest source-supported coordinate system that preserves the represented graph: its actors, stable referents/content, values, lexical relations, orientation edges, physical settings, temporal frames, and the material bindings among them.

Use this sequence internally for every class pass:

1. resolve coreference and speaker/addressee status;
2. identify distinct represented scenes and temporal/narrative frames;
3. identify stable nodes/content, values, relation atoms, and orientation edges inside those frames;
4. distinguish structural roles from incidental wording;
5. emit only the requested class, using the same reconstructed graph as the basis for all classes.

A coordinate may be unnamed or grammatically dependent and still belong when the source gives it a distinct representation role. A vivid or semantically meaningful word does not belong merely because it can be isolated.

## 2. Admission test: role, distinction, and necessity

Admit a primitive when all applicable questions support it:

1. **ROLE:** Does the source give this span or source-supported unnamed coordinate a distinct function as PLACE, TIME, PERSON, OBJECT, LABEL, VERB, or LOCATOR?
2. **DISTINCTION:** Would merging it with another retained coordinate erase a represented distinction the source makes?
3. **GRAPH NECESSITY:** Is it a node, frame, value, relation, or orientation edge that materially participates in the represented graph rather than merely describing, decorating, or grammatically supporting another coordinate?
4. **SOURCE SUPPORT:** Can its identity and scope be grounded in exact source wording/cues without importing unstated events, places, times, motives, or concepts?
5. **GRAIN:** Is this the smallest complete role-bearing coordinate, rather than a fragment of one or an unnecessary wrapper around one?

Reject a candidate when it is only incidental lexical material, a duplicate coreferent, a syntactic scaffold, a modifier fragment, an unneeded proposition wrapper, or a relation-internal piece with no distinct representation role.

## 3. Structural anchors versus incidental detail

Structural anchors are not limited to explicit nouns such as a named room or an explicit date.

A source-supported unnamed PLACE or TIME may be required when a distinct scene, co-presence setting, occurrence context, narrative phase, remembered interaction, present-telling frame, reflective frame, recurring frame, or prospective frame organizes multiple represented relations.

Do not create a PLACE/TIME for every action. Use one anchor for a coherent relation cluster unless the source establishes a distinct setting/frame transition.

Conversely, a floor, counter, wall, line, vehicle/support, container, surface, side, or similar concrete item is not automatically OBJECT or PLACE. Classify it by the role it actually plays in the represented graph. If the source uses a concrete support or bounded physical context as the occurrence setting for a relation cluster, it may function as PLACE; if it remains a stable thing acted on or discussed, it may function as OBJECT; if neither role is independently material, do not retain it merely because it is a noun.

## 4. PLACE

Retain each distinct source-supported physical setting or occurrence position that anchors represented relations.

PLACE includes:

- broad and contained settings when the source materially distinguishes both;
- supported unnamed co-presence/interaction settings;
- bounded physical support contexts when they function as the setting in which represented activity occurs;
- distinct remembered/current settings when the source shifts where a relation cluster occurs.

Do not retain a location merely because a noun names a physical thing. Do not promote every surface, endpoint, path, object part, distance, or position phrase to PLACE when its function is only orientation; use LOCATOR for an orientation edge.

For supported unnamed PLACE, `source_wording` may be null and `source_cue` must be an exact source substring.

## 5. TIME

Retain each distinct source-supported temporal/narrative frame that organizes one or more represented relations.

TIME includes, when materially distinct:

- earlier versus later periods;
- discrete interaction episodes;
- waiting/active phases when the source makes the transition consequential;
- remembered conversations;
- current telling/reflection;
- recurring periods;
- prospective/future-similar-situation frames;
- a continuing state period when it functions as an episode/frame rather than merely a value.

Do not retain every adverb, duration phrase, recurrence word, tense/aspect marker, or action-local moment. A temporal phrase can instead be LOCATOR when its job is only to position an already retained TIME.

For supported unnamed TIME, `source_wording` may be null and `source_cue` must be exact source text.

## 6. PERSON

Retain the speaker and each distinct represented human/social actor or stable group. Resolve aliases, titles, kinship terms, and pronouns before deduplication. Speaker canonical key is `B`.

Generic, impersonal, rhetorical, idiomatic, or self-directed grammatical `you` is not PERSON absent a stable represented addressee.

## 7. OBJECT

Retain stable represented things/content that function as graph nodes a researcher could revisit independently.

This may include:

- concrete things that materially participate in retained relations;
- explicit decisions, choices, amounts, services, topics, sets, or relation-results treated as things;
- internal/mental content treated as a stable referent;
- abstract or figurative content treated as a node rather than merely as a characterization;
- a source-described event/result when the source itself reifies it as content.

Do not inventory every concrete noun, complement, proposition, pronoun, modifier target, or comparison image. Incidental concrete detail stays only when it materially participates as a retained graph node.

Resolve pure `this/that/it` wrappers to their antecedent. Do not create both a stable referent and a duplicate proposition wrapper unless the source independently reifies both.

Cross-class function outranks noun shape: wording that sounds descriptive may be OBJECT when the source treats it as stable content; wording that names a concrete thing may instead function as PLACE or may be omitted if incidental.

## 8. LABEL

Retain source-presented values, states, classifications, evaluations, comparisons, identity/self-labels, relational statuses, and explicit polarity/correction values when the value itself is a distinct graph role.

Use the smallest complete value grain that preserves posture and scope.

Do not inventory every adjective/adverb/modifier. But do not automatically swallow distinct questioned, rejected, corrected, affirmed, intensified, or contrasted values into one larger label when the source presents them as separate value roles.

Negation or a question does not automatically create a LABEL. It does when the source presents a value or polarity that is itself being selected, rejected, affirmed, or contrasted.

A spatial/deictic expression can function as LABEL when the source presents it as a value/state rather than only an orientation edge.

## 9. VERB

Retain the smallest complete **relation atom** for each materially distinct source-presented lexical relation.

A relation atom is not necessarily one verb token and not necessarily a whole clause.

Split relations when the source establishes distinct relation roles that can each bind retained coordinates—for example a posture/action plus a cognition, a movement plus a result, a reporting relation plus independently represented content, or coordinated actions with separate graph effects.

Merge wording when multiple tokens jointly express one inseparable lexical relation, such as a phrasal predicate, control construction whose infinitive supplies the same single relation identity, fixed idiom, or negated/modal relation that loses its identity if split.

Apply this test:

- If removing one candidate relation would erase a distinct source-presented edge while leaving the other relation meaningful, retain both.
- If the apparent subrelation exists only as the grammatical machinery of one relation and has no separate graph edge, keep one complete VERB.

Do not use token count, clause boundaries, grammatical embedding, or coordination alone to decide.

## 10. LOCATOR

Retain the smallest complete reusable **orientation edge** that places or orients a retained node, frame, or relation.

Orientation roles include:

- position;
- path;
- direction;
- origin/destination;
- entry/exit;
- containment;
- support/surface placement;
- accompaniment/carrying;
- proximity/distance;
- recurrence/temporal positioning;
- internal or figurative orientation.

A LOCATOR may be grammatically an argument. Relation-argument status is not an exclusion rule when the phrase contributes a distinct orientation edge.

Keep distinct orientation roles separate when the source supplies separate edges. Do not automatically concatenate movement, accompaniment, destination, and context into one long LOCATOR merely because they occur in the same clause.

Do not retain a preposition or direction phrase when it merely restates a relation and contributes no independent orientation role.

## 11. Cross-class resolution

Classify by represented function, not surface grammar:

- social actor -> PERSON;
- stable thing/content/relation-result -> OBJECT;
- value/state/classification/polarity -> LABEL;
- lexical relation atom -> VERB;
- orientation edge -> LOCATOR;
- physical scene/occurrence setting -> PLACE;
- temporal/narrative frame -> TIME.

Cross-class overlap is allowed only when the same source wording genuinely supplies different independently material roles. Do not create overlap to maximize coverage.

## 12. Structural-completion pass

After selecting lexical candidates, perform a graph-completeness check before returning the requested class.

For each distinct relation cluster, ask:

- What physical setting, if any, does the source establish for this cluster?
- What temporal/narrative frame, if any, distinguishes it from neighboring clusters?
- What stable node/content is the relation about or acting upon?
- What value/polarity is materially represented?
- What orientation edges materially position participants or movement?

If a required role is source-supported but unnamed, it may be admitted using an exact source cue. If the source does not establish a distinct role, do not invent one simply to make the graph symmetrical.

The purpose is to prevent both failures: lexical census and structural under-inventory.

## 13. Literal and posture lock

Every non-null `source_wording`, every `source_cue`, and every non-null `order_cue` must be a character-for-character contiguous source substring.

Preserve source spelling, punctuation, dialect, questions, negation, uncertainty, correction, comparison, attribution, intention, hypothetical, recurrence, report, and prospective posture.

Explicit short tags use only source words. Supported unnamed PLACE/TIME may use neutral navigation tags grounded by exact source cues. Never substitute synonyms or normalize dialect.

## 14. Ordering and qualities

Order by first source establishment after coreference, subject to apparatus speaker-first PERSON and broad-before-contained PLACE/LOCATOR only when genuinely established together.

`qualities_available` is boolean only. It is true only when qualities/descriptions are available for that coordinate or compound. Question, negation, uncertainty, intensity, or the mere presence of a LABEL does not automatically make it true.

## 15. Compound reconstruction: graph edges, not sentence parses

Freeze all admitted primitives before compounds.

Scan the source in order and emit the smallest set of compounds needed to preserve material source-presented bindings among retained coordinates.

A compound should correspond to one materially distinct represented binding or relation cluster. It may bind a structural PLACE/TIME anchor, relation atom, orientation edge, value, and participating nodes when those coordinates jointly represent that source relation.

Do not emit:

- every clause;
- every possible pair;
- nested subset alternatives for one binding;
- broad sentence bags merely to consume words;
- duplicate compounds that differ only by dropping or adding coordinates from the same represented binding;
- compounds that rely on non-admitted units.

If two relation atoms in the same sentence create two materially distinct bindings, two compounds may be appropriate. If they are one inseparable relation, use one compound. Compound construction follows the represented graph, not punctuation or token count.

`referenced_unit_refs` must reference only frozen admitted units, and `compound_expression` must reflect their source order.

## 16. Calibration isolation

Return only the JSON required by the request schema. Never infer or reconstruct archetypes, expected counts, evaluator preferences, prior scored outputs, case-specific gold corrections, sealed holdout source during calibration, or holdout output.

Do not reason from an imagined evaluator. Apply this contract to the supplied source.

## 17. Prohibited work

Never perform APA scoring, psychological interpretation, protected-thread analysis, conclusions, promotion, APA-ID creation, Oval Office research writing, sovereign admission, or database/fabric admission.

## 18. Successor effect

V56 prospectively supersedes V55 only for new Researcher Inventory calibration/certification work beginning 2026-09-16. V55 and all prior contracts and runs remain immutable historical evidence.

V56 preserves V55's valid anti-census, coreference, literal-lock, isolation, and selective-compound controls while correcting V55's demonstrated general failure to preserve representation architecture consistently across structural anchors, cross-class roles, relation atoms, orientation edges, value/polarity atoms, and stable content nodes.

Immutable archetype hashes, evaluator/worker isolation, candidate-only status, repeated paired-archetype gate, sealed Case 5 one-shot semantics, fresh-agent clean-room certification, and all promotion/APA-ID/database prohibitions remain unchanged.
