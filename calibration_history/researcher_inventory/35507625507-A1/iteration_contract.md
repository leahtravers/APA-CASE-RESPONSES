# APA Researcher Inventory Agent Contract V115

Status: `ACTIVE SUCCESSOR FOR CALIBRATION — NOT CERTIFIED`
Contract version: `RI-CONTRACT-V115`
Predecessor: `RI-CONTRACT-V114`
Effective date: 2026-09-20
Authority: Leah's standing Researcher Inventory calibration instruction.
Registrar record: `APA-EXEC-2026-09-20-CASES-RI-V115-CAL-0001`

## Prospective correction basis

V114 workflow run `35502967928` verified both Leah-approved immutable archetype workbooks against their required SHA-256 values without repair, passed all 21 deterministic apparatus/harness tests, then failed the first paired semantic diagnostic on both approved archetypes. The complete failed attempt remains preserved append-only under `calibration_history/researcher_inventory/35502967928-A1/`. The sealed holdout was not reached.

The failure is worker-semantic. V114 correctly removed V113's recurrence/salience bias, but its rule that each distinct represented denotatum, relation, support, or orientation belongs unless it is grammar was interpreted as an exhaustive semantic census. The worker over-produced standalone primitives and compounds from locally meaningful clause material, modifiers, argument phrases, micro-relations, and per-clause support while still missing some natural-grain coordinates and making some functional type errors.

This is a generalizable boundary defect. Historical calibration already demonstrated both poles: a global indispensability/stability threshold can over-prune, while source presence or local semantic typability can over-produce. V115 therefore restores the middle rule:

> **SOURCE-PRESENTED BINDING-ROLE ENTITLEMENT AT NATURAL CLASS GRAIN.** A primitive may be one-use, local, nested, low-salience, remembered, reported, prospective, uncertain, negated, figurative, or colloquial. It is retained only when the source gives it a distinct class-native role in a source-presented binding or frame at the natural resolution of that class. Source presence, grammatical separability, semantic content, or local typability alone are not sufficient.

No archetype rows, expected counts, evaluator findings, prior scored outputs, calibration answers, or sealed holdout material are supplied to the worker.

## Mission

Produce a literal, lightweight Researcher Inventory of the complete supplied source in exactly seven classes:

1. `PLACE`
2. `TIME`
3. `PERSON`
4. `OBJECT`
5. `LABEL`
6. `VERB`
7. `LOCATOR`

The inventory is a **source-reconnection index**, not a token/POS census, clause decomposition, modifier census, semantic-role census, event census, or exhaustive semantic graph. Preserve the source-native coordinates and bindings needed to reconnect the represented research structure at the inventory's natural resolution.

Do not perform APA scoring, psychological interpretation, conclusions, promotion, APA-ID creation, executive analysis, sovereign/admitted writing, or APA Data Fabric/database mutation.

## 1. Whole-source binding/frame skeleton before extraction

Read the entire source before extracting any class. Silently reconstruct a **binding/frame skeleton** containing only source-presented research structure at natural grain:

- distinct scenes and occurrence positions;
- distinct temporal episodes, phases, periods, recurrence frames, remembered/reported frames, prospective frames, and present reflection when source-differentiated;
- represented human/social actors and stable groups;
- tracked concrete or abstract referents/content handles;
- source-applied characterizations, states, identities, comparisons, candidate labels, rejections, and corrections;
- operative actions, states, communications, cognitions, intentions, questions, movements, and relations at their natural source grain;
- independent orientations such as position, path, direction, containment, origin/destination, accompaniment, internal/relational position, recurrence/context, and figurative orientation when source-presented.

The skeleton is neither a sentence parse nor a summary. It preserves distinct source-presented bindings while refusing to create a separate binding for every clause fragment, modifier, argument, preposition, auxiliary, discourse wrapper, or semantic implication.

## 2. Primitive admission: four gates

A proposed primitive is retained only when all four gates pass.

### Gate A — source grounding

The source itself establishes the candidate in the requested class. Do not invent analyst abstractions, diagnoses, normalizations, or inferred facts.

For explicit coordinates, use the smallest complete exact contiguous source span that preserves the class-native identity. Supported unnamed PLACE/TIME coordinates may use null `source_wording` only when the source clearly differentiates a scene/frame but does not name its support.

### Gate B — class-native role

The candidate performs a real job of the requested class in the represented source. Type by represented function, not part of speech or phrase shape.

### Gate C — source-presented binding/frame role

The candidate fills a distinct inventory-bearing role in at least one source-presented binding or frame in the whole-source skeleton.

Use this question:

**Would a researcher need this candidate as a selectable coordinate to reconnect a distinct source-presented participant, referent/content handle, scene/frame support, characterization, operative relation, or orientation at this class's natural resolution, rather than merely to recover wording already carried inside a stronger retained coordinate or binding?**

If yes, retain it. If no, reject it even when the phrase is meaningful, concrete, descriptive, or locally typable.

This is not a salience or recurrence test. A one-use, local, nested, background, or low-salience coordinate can qualify when the source separately projects that role. Do not require global narrative importance, repeated mention, reuse across compounds, or independence from the proposition that gives the coordinate meaning.

### Gate D — class-local distinctness and natural grain

Resolve true aliases/coreference and genuine same-class restatements. Retain one natural complete coordinate for each class-native identity. Do not split one natural relation/orientation/characterization into support fragments merely because each fragment is semantically interpretable.

## 3. Anti-census boundary

Reject material whose proposed standalone row exists only because it is locally meaningful inside a stronger retained coordinate/binding, including:

- grammar-only auxiliaries, tense/aspect machinery, articles, conjunctions, fillers, and discourse scaffolding;
- proposition or clause wrappers that merely restate a relation already represented by its retained participants/content/predicate;
- every grammatical argument or complement treated automatically as OBJECT;
- every adjective/adverb/modifier treated automatically as LABEL;
- every prepositional or purpose/recipient/topic phrase treated automatically as LOCATOR;
- every clause/action treated automatically as a new TIME;
- every physical noun/surface treated automatically as PLACE;
- support predicates or micro-relations split away from one natural predicate kernel;
- token fragments that have no complete class-native identity;
- duplicate/coreferent mentions;
- analyst-created abstractions or paraphrases.

Do not reject a coordinate merely because it occurs once, is mundane, local, nested, relational, possessive, remembered, reported, uncertain, negated, prospective, or figurative.

## 4. Functional typing

Type by the role the source gives the span in the represented binding/frame:

- represented human/social actor -> `PERSON`
- independently tracked thing/content/referent -> `OBJECT`
- source-applied characterization/state/identity/evaluation/comparison/candidate label/correction -> `LABEL`
- scene/location support -> `PLACE`
- episode/period/phase support -> `TIME`
- operative lexical action/state/relation edge -> `VERB`
- independent position/path/direction/context/orientation edge -> `LOCATOR`

Cross-class overlap is allowed only when the same literal span genuinely performs distinct source-presented roles in more than one class. Do not manufacture overlap from grammar alone.

## 5. PLACE — scene/location support

Retain each distinct physical scene or occurrence-position that hosts or materially locates a source-presented binding/frame.

A broad scene and a materially distinct contained/local scene may both qualify. A destination, waiting position, later interaction location, remembered scene, prospective scene, or present-telling location may qualify when the source differentiates it as a scene support.

A supported unnamed PLACE is permitted only when a source-differentiated scene/interaction needs its own location slot and cannot truthfully share another retained scene. Use null `source_wording`, exact source cue, and a neutral mechanical tag. Never invent the physical details.

Do not create PLACE merely from every physical noun, surface, object part, path phrase, or object-location mention. Physical thinghood belongs in OBJECT; orientation belongs in LOCATOR unless a distinct scene/location support is actually present.

## 6. TIME — episode/frame support

Retain each distinct temporal episode, phase, period, recurrence frame, remembered/reported frame, prospective frame, or present-reflection frame that organizes source-presented bindings.

A supported unnamed TIME is permitted only when the source separates a real episode/phase from neighboring material even though it does not name the time. Several actions/relations may share one TIME.

Do not create a TIME for every clause, predicate, question, wait-duration phrase, transition word, or local action. Split only when the source materially changes the represented episode/frame or explicitly establishes a distinct period/phase.

## 7. PERSON — represented actors

Retain the speaker and each distinct represented human/social actor or stable group after true coreference when that actor fills a participant role in at least one source-presented binding.

Direct, offscreen, relational, possessive/beneficiary, remembered, reported, institutional, prospective, peripheral, and one-use actors may qualify.

Reject nonreferential/rhetorical/generic persons that never become represented participants. Do not duplicate pronouns, roles, kinship terms, or aliases after true coreference.

## 8. OBJECT — tracked referents/content handles

Retain each concrete or abstract source-presented referent/content handle that the source treats as an independently trackable participant in one or more bindings: something acted on, possessed, exchanged, located, checked, compared, selected, rejected, remembered, reported, contemplated, valued, or otherwise related as a thing/content node.

One-use and low-salience referents can qualify. Decisions, choices, plans, relations, values, sets/categories, internal content, and proposition-like content qualify only when the source actually reifies or tracks them as content/objects.

Do not nominalize every clause, question, intention, relation, or grammatical argument into OBJECT. A clause/proposition becomes OBJECT only when the source itself treats that content as a referential handle beyond the relation that states it.

Do not duplicate a PLACE whose only role is scene support or a LABEL whose only role is characterization.

## 9. LABEL — source-applied characterizations

Retain each smallest complete source-presented characterization, state, status, identity, evaluation, comparison, candidate label, rejection, correction, or materially distinct manner/posture that the source applies to a represented target.

A label can be one-use, colloquial, idiomatic, uncertain, questioned, negated, corrected, rejected, or figurative.

Choose the natural complete judgment unit. Do not split ordinary characterization wording into adjective/intensifier/polarity fragments merely because each fragment is typable. Do not create LABEL from every descriptive modifier/adverb or discourse stance when it does not function as an independently source-applied characterization.

## 10. VERB — operative relation edges

Retain one minimal complete literal predicate kernel for each distinct source-presented **operative relation edge** in the binding skeleton.

A qualifying edge may express action, state, stance, cognition, perception, report/communication, intention, question, decision, possession, comparison, evaluation, movement, transition, gesture, existence/location, or another represented relation. One-use, ordinary, and low-salience relations may qualify.

Do not require broad story change. Instead require that the predicate be the operative relation of a source-presented binding rather than merely a grammatical/support fragment or an incidental lexical verb embedded inside a stronger natural relation.

Use the smallest complete source-native predicate kernel. Preserve particles, reflexives, negation, modality, or bound complements when needed for relation identity. Split matrix/embedded/coordinated predicates only when the source presents genuinely distinct operative edges. Keep them together when splitting would create support grammar or micro-relations.

Reporting, asking, seeing, saying, thinking, obligation, location, and simple relational predicates are not excluded merely for being ordinary; they qualify when they form a distinct source-presented relation edge.

Exclude pure tense/aspect auxiliaries, copular support whose entire represented content is already one LABEL and adds no relation, discourse organizers/fillers with no represented edge, and true same-relation restatements.

## 11. LOCATOR — independent orientation edges

Retain each smallest complete exact source span that fills an independent orientation role in a source-presented binding: scene position, path, origin/destination, direction, containment, proximity, accompaniment/carrying, entry/exit, internal/mental/relational position, recurrence/context, or materially spatialized figurative/comparative orientation.

A LOCATOR must actually orient a retained participant, referent, relation, or frame. Do not create LOCATOR from every prepositional phrase, recipient/topic/purpose argument, possession phrase, degree phrase, temporal phrase, or generic adverbial merely because it can be read relationally.

Use the natural complete orienting span rather than isolated prepositions/deictics or clause-sized paraphrases.

## 12. Literal lock and source posture

For every explicit primitive, preserve the smallest complete exact contiguous source-native span that carries the coordinate's identity. Every non-null `source_wording`, `source_cue`, and `order_cue` must be character-for-character source text.

Preserve source posture where semantically required: negation, modality, uncertainty, question form, attribution, comparison, idiom/dialect, reported/recalled posture, hypothetical/prospective posture, and correction/rejection.

Never normalize, improve, translate, diagnose, euphemize, paraphrase, lemmatize into a different surface form, or substitute synonyms.

## 13. Freeze audit

Before compounds:

1. replay every source-presented binding/frame in source order;
2. verify each class-native role that needs a selectable coordinate is represented;
3. check low-salience, one-use, local, remembered, reported, and prospective roles for accidental pruning;
4. check every retained row for anti-census excess: if it only reproduces internal wording of a stronger retained coordinate/binding, remove it;
5. check PLACE/TIME support is scene/frame based rather than clause/action based;
6. check OBJECT/LABEL/LOCATOR typing by source function;
7. check VERB kernels are natural operative edges, neither support fragments nor clause-sized bundles;
8. verify literal lock, coreference, class-local distinctness, and source order;
9. freeze all seven primitive ledgers.

Do not target an expected count or infer a hidden archetype.

## 14. Compounds — serialize source-presented bindings after primitive freeze

Compounds are built only after all primitives are frozen. They serialize the same binding/frame skeleton used for primitive admission.

Emit one smallest complete compound for each materially distinct source-presented proposition/relation/state/question/comparison binding that is needed to reconnect the frozen coordinates.

Use a retained VERB as backbone when one carries the binding. Include retained participants, referents/content, labels/states, PLACE/TIME support, and LOCATORs only when they actually participate in that exact binding.

A non-VERB label/state/question binding may form a compound only when the source presents it as distinct structure not already carried by another retained relation.

Do not emit compounds merely because wording forms a clause or sentence. Do not emit graph closure, arbitrary co-occurrence links, all-pairs links, scene mega-bundles, singleton equivalents, subset/superset permutations, support chains, or duplicate restatements. Do not use compounds to justify unsupported primitives or to repair missing primitives.

## 15. Ordering and identity

Primitive identity is class-local source identity, not mention count. Resolve true aliases/coreference before duplicate removal. Do not merge genuinely different coordinates merely because they are related or colocated.

Code owns canonical IDs. The worker supplies only neutral identity keys where the apparatus requires them. Order by first source establishment after coreference, subject to apparatus speaker-first PERSON and genuine broad-before-contained scene rules.

## 16. Isolation boundary

The calibration worker must never receive:

- Case 2 or Case 6 gold workbook rows or canonical extracts;
- expected counts;
- evaluator findings;
- scored prior outputs;
- case-specific gold corrections/examples;
- `researcher_inventory/tests/holdout/CASE_5.sealed.txt` during calibration;
- any Case 5 holdout output.

A hidden evaluator may compare worker output after execution. That comparison must not be included in later worker instructions/examples.

## 17. Archetype integrity and failure separation

Before calibration uses Case 2 or Case 6, repository workbook copies must pass Leah's immutable SHA-256 gates. If a copy is wrong, reconstruct it only from an already authorized canonical source/extract and use it only if the reconstructed digest exactly equals the approved hash.

Preserve every calibration attempt, partial result, failure, transport/recovery record, and successor as durable history. Do not delete failed runs.

Classify harness/apparatus defects separately from worker-semantic defects. A harness correction alone does not justify semantic contract revision, and a semantic failure does not authorize changing evaluator mechanics.

## 18. Certification gate

V115 is not certified merely because it is active for calibration.

Certification requires, in order:

1. immutable Case 2 and Case 6 SHA-256 verification;
2. one paired diagnostic Case 2 + Case 6 pass under the finalized V115 contract;
3. two paired repeatability batches under the same finalized V115 contract and same calibrated saved-agent lineage;
4. only after all repeated archetype gates pass, exactly one sealed Case 5 holdout attempt on that calibrated lineage;
5. if that holdout is archetypal, retire the calibrated lineage;
6. create a brand-new saved agent bootstrapped only from finalized V115 durable instructions, with no prior sessions or holdout output;
7. run Case 5 once in a new session as clean-room verification;
8. certify only if that fresh agent succeeds.

If the sealed holdout has already been consumed for a lineage, automatic reuse is prohibited.

## 19. Historical effect

`AGENT_CONTRACT_V114.md` remains preserved as the controlling contract for work executed under V114, including run `35502967928`.

V115 supersedes V114 prospectively for new Researcher Inventory calibration and any later holdout/clean-room stage lawfully reached from the V115 calibration lineage.

Retained from V114: immutable archetype hashes; literal/source-posture lock; seven classes; function-first typing; legitimate unnamed PLACE/TIME support; one-use/low-salience eligibility; primitive freeze before compounds; evaluator/harness isolation; saved-agent lineage rules; one-shot holdout; clean-room certification; append-only history; candidate-only status; no promotion; no Oval Office research admission; no APA-ID minting; no APA database mutation.

Superseded from V114: source representation or semantic class-native function by itself as sufficient standalone primitive entitlement; exhaustive support closure over every differentiated event/action; broad lexical-predicate admission that can become a verb census; and proposition-instance construction that can serialize every semantically meaningful clause. V115 requires distinct source-presented binding/frame role at natural class grain.
