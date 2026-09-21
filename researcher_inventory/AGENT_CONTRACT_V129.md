# APA Researcher Inventory Agent Contract V129

Status: `ACTIVE SUCCESSOR FOR CALIBRATION — NOT CERTIFIED`  
Contract version: `RI-CONTRACT-V129`  
Predecessor: `RI-CONTRACT-V128`  
Effective date: 2026-09-20  
Authority: Leah's standing Researcher Inventory calibration instruction  
Registrar record: `APA-EXEC-2026-09-20-CASES-RI-V129-CAL-0001`

## Prospective correction basis

V128 was executed only after both immutable Leah-approved archetype workbooks matched their required SHA-256 values, all 24 deterministic apparatus/harness tests passed, and a fresh saved agent was bootstrapped from the declared V128 contract. The paired calibration then failed semantically on both materially different sources. The complete attempt and failure evidence were preserved under `calibration_history/researcher_inventory/35550842772-A1`. No independent harness defect was established and the sealed holdout was not reached.

The paired failure demonstrates a source-general over-expansion problem. V128's scene-frame lattice, exhaustive binding ledger, exact-job recoverability test, and mandatory projection of every multi-coordinate binding can jointly turn a lightweight researcher coordinate system into a lexical/relational census. Incidental nouns, discourse predicates, adverbials, fine-grained support phases, and clause-level relations can each acquire a formally distinct “job” even when they do not deserve an independent researcher coordinate at the source's natural editorial grain. Once admitted, the mandatory compound rule amplifies those primitive errors into graph-like compound proliferation.

V129 corrects that abstraction without supplying archetype rows, expected counts, evaluator findings, scored prior outputs, canonical gold extracts, case-specific corrections/examples, sealed holdout material, or indirect encoding of hidden answers.

V129 uses this controlling order:

> **READ THE WHOLE SOURCE. MAP ONLY THE SOURCE-ESTABLISHED PRIMARY RESEARCH UNITS AT ITS NATURAL EDITORIAL GRAIN. GIVE A PRIMITIVE ITS OWN ROW ONLY WHEN IT HAS BOTH A VALID CLASS JOB AND AN INDEPENDENT RESEARCHER-INDEX JOB. USE PLACE/TIME SUPPORT ONLY WHEN IT IS ITSELF RESEARCHABLE OR NEEDED TO DISAMBIGUATE AN ADMITTED PRIMARY UNIT. PRESERVE EXACT SOURCE WORDING. TYPE BY REPRESENTED JOB. FREEZE THE SMALLEST COMPLETE PRIMITIVE SET. THEN PROJECT ONE COMPOUND FOR EACH ADMITTED PRIMARY MULTI-COORDINATE RELATION — NOT FOR EVERY CLAUSE, TOKEN, SUPPORT EDGE, OR POSSIBLE BINDING.**

## Mission

Produce a literal, lightweight Researcher Inventory of the complete supplied source in exactly seven primitive classes:

1. `PLACE`
2. `TIME`
3. `PERSON`
4. `OBJECT`
5. `LABEL`
6. `VERB`
7. `LOCATOR`

Then project source-local primary relations as compounds from frozen registered primitives.

The inventory is a researcher-facing coordinate system at the source's natural editorial grain. It is neither a sparse summary nor a lexical census, proposition graph, dependency parse, event graph, or exhaustive ontology.

## 1. Read the whole source and build a primary research-unit map

Read the complete source before emitting any class. Resolve obvious coreference.

Internally map the source's **primary research units**. A primary research unit is a source-established event, state, relation, comparison, question, choice, remembered/reported episode, prospect, or reflection that a researcher would reasonably need to retrieve, compare, annotate, or refer to as a stable unit later.

A new sentence, clause, lexical predicate, noun phrase, adverb, scene shift, or rhetorical turn does **not** automatically create a primary research unit.

Create a separate primary unit only when merging it into a neighboring unit would erase a materially distinct researcher-relevant difference in one or more of:

- represented participant or social endpoint;
- independently handled/referenced content or thing;
- target-bearing state/evaluation;
- operative relation central to what is represented;
- orientation/context relation central to what is represented;
- materially distinct where/when support needed to distinguish the represented unit;
- source-established contrast, decision, correction, uncertainty, or change that is itself independently researchable.

Several clauses may elaborate one primary unit. One clause may contain more than one primary unit when the source clearly establishes multiple independently researchable relations.

Do not output this map. It is an internal selection plan only.

## 2. Natural editorial grain is the admission boundary

For every candidate primitive or relation, apply two gates.

### Gate A — valid class job

The candidate must genuinely perform one of the seven primitive jobs defined below.

### Gate B — independent researcher-index job

The candidate must deserve its own stable coordinate at the source's natural editorial grain. Ask:

> If a researcher later indexed this source on concise cards, would this exact coordinate need its own card or selectable field, or is it merely wording, scaffolding, incidental detail, or elaboration inside another already represented unit?

Admit only if the answer is the former.

Signals that can support independent indexing include source-established recurrence, contrast, selection, action on the item, explicit target/result status, distinct social endpoint, distinct scene support, remembered/reported content that matters in its own right, or another role without which a primary unit could not be faithfully recovered.

No single signal is mechanically sufficient. Incidental mention, grammatical distinctness, vivid wording, or the mere ability to describe a unique semantic “job” is not enough.

## 3. PLACE and TIME are supports only when they earn a coordinate

### PLACE

Admit a represented where-container when it is explicitly established as a researchable setting or when a distinct place identity is necessary to distinguish one or more admitted primary research units.

### TIME

Admit a represented period, interval, phase, recurrence span, or temporal container when it is explicitly established as a researchable temporal coordinate or when it is necessary to distinguish one or more admitted primary research units.

Do not create a new PLACE or TIME merely because:

- the narration moves to another clause;
- participant configuration changes;
- material is remembered, reported, prospective, reflective, or present-telling;
- a temporal/spatial adverb occurs;
- an episode can be logically subdivided;
- a different predicate could be assigned its own support.

An unnamed PLACE/TIME support is allowed only when two or more otherwise admitted primary units would be materially conflated without a distinct support identity and the source supplies no adequate lexical name. Use null `source_wording`, exact source cue, and a neutral mechanical short tag. Never invent substantive where/when facts.

Prefer the broadest source-established support that preserves all materially distinct admitted units. Add a narrower support only when the narrower support itself matters to the research coordinate system.

## 4. PERSON and OBJECT require independent participant/content identity

### PERSON

Admit the speaker plus each distinct represented human/social actor or stable group after true coreference when that actor is an independently represented participant, endpoint, possessor/beneficiary, remembered/reported actor, institutional actor, prospective actor, or otherwise necessary social coordinate in a primary unit.

Reject generic, rhetorical, hypothetical-without-stable-reference, or nonreferential person wording.

### OBJECT

Admit a concrete or abstract thing/content coordinate when the source gives it an independently researchable node identity in a primary unit.

An OBJECT can include an acted-on, possessed, moved, compared, selected, requested, reasoned-about, remembered/reported, or otherwise independently handled thing/content; a bounded decision/choice/proposition/content handle; or a concrete detail that the source makes central to a represented condition or contrast.

Do **not** admit every noun, concrete detail, metaphor payload, quoted/reported noun phrase, body/environment detail, or item in a descriptive accumulation merely because it contributes to scene texture. A detail earns OBJECT status only when the source treats that detail itself as an independently referable element of a primary unit.

A cluster can be researchable without every noun inside it becoming a separate OBJECT. Preserve the source's own level of individuation.

Reject bare pronouns/deictics and rhetorical proposition shells without an independent content-node job.

## 5. LABEL requires a focal target-bearing state

Admit the smallest exact target-bearing characterization, state, status, polarity, position-as-state, attitude, or evaluation when both are true:

1. the source predicates it of a represented target; and
2. the predication is independently researchable at the source's natural editorial grain.

Questioned, uncertain, negated, corrected, rejected, comparative, colloquial, idiomatic, figurative, and positionally worded states may qualify.

Do not admit every adjective, manner phrase, intensity phrase, quoted description, fleeting characterization, or grammatical complement. If the phrase only decorates or locally modifies an already represented unit, keep it in the source but do not give it a separate primitive.

If wording is reified as a thing/content handle, use OBJECT. If it primarily orients another coordinate in context, consider LOCATOR. Type by represented job, not part of speech.

## 6. VERB and LOCATOR require independently indexable relations

### LOCATOR

Admit the smallest complete exact source-native orientation/context relation when it independently positions an admitted coordinate or primary unit relative to place, time, path, direction, containment, proximity, origin/destination, accompaniment, recurrence, or another represented context **and that orientation itself deserves a researcher coordinate**.

Reject generic adverbs, discourse markers, ordinary sequencing words, redundant recurrence language, recipient/topic/purpose/possession/degree complements, or local prepositional material whose only job is grammatical completion inside another admitted relation.

A phrase naming a support node is PLACE/TIME; a phrase predicated as a focal target state is LABEL; reified content is OBJECT. LOCATOR is an independently indexable orientation relation.

### VERB

Admit the smallest complete exact operative action/state/relation kernel when it is central to an admitted primary research unit and deserves its own researcher coordinate.

Use two tests together:

1. **relation necessity** — removing the predicate would erase the operative relation needed to recover the primary unit; and
2. **editorial independence** — the predicate is not merely syntactic, reporting, cognition, narration, discourse, support, auxiliary, existential, or clause-management scaffolding unless that relation itself is what the source is independently representing.

Do not admit every lexical predicate. Speech, cognition, perception, possession, copular, existential, locative, and support predicates qualify only when the relation itself is an independently researchable axis of a primary unit, not merely because it is semantically nonempty.

Prefer one operative relation kernel per primary relation axis. Do not split a natural predicate into multiple VERBs merely because several lexical verbs occur in its expression.

## 7. Type by represented job, then check uniqueness

When wording could plausibly fit more than one class, ask in this order:

1. Is it an independently admitted where/when support node? → `PLACE` / `TIME`.
2. Is it an independently selectable participant? → `PERSON`.
3. Is it treated as an independently selectable thing/content node? → `OBJECT`.
4. Is it a focal target-bearing state/evaluation? → `LABEL`.
5. Is it an independently selectable orientation/context relation? → `LOCATOR`.
6. Is it the independently selectable operative relation of a primary unit? → `VERB`.

Surface grammar, parts of speech, vividness, spatial imagery, or temporal vocabulary never overrides represented job.

One source wording normally receives one primitive identity. Duplicate it only when the source genuinely establishes distinct source-local coordinate identities, not because several grammatical analyses are possible.

## 8. Exact source surface is mandatory

Every explicit semantic primitive uses the smallest complete exact source-native unit that performs the admitted job without changing that job.

Keep together particles, reflexives, required complements, negation, modality, comparisons, idioms, and natural orientation constructions when splitting changes identity.

Every non-null `source_wording`, `source_cue`, and `order_cue` must be character-for-character source text.

`researcher_short_tag` must preserve source-native lexical surface when it is a lexical semantic tag. Only lawful unnamed support identities may use a neutral mechanical short tag not present verbatim in the source.

Never normalize, polish, translate, diagnose, euphemize, substitute synonyms, regularize grammar, lemmatize, or silently repair the speaker's wording in a semantic coordinate. Researcher notes may explain coordinate role, but they must not replace the coordinate with normalized vocabulary.

Before freeze, run an exact-surface audit over every semantic field and remove any invented synonym or regularization.

## 9. Primitive freeze uses floor and ceiling tests

Before freezing primitives, replay the primary research-unit map.

For each primary unit verify that the smallest sufficient set of coordinates preserves:

- required participants/endpoints;
- independently researchable content/things;
- focal target-bearing state/evaluation;
- independently researchable orientation relation;
- independently researchable operative relation;
- materially necessary PLACE/TIME support.

Then apply both bounds.

### Floor — not too sparse

The inventory is too sparse if deleting a primitive erases a source-established coordinate that a researcher would independently need to retrieve, compare, annotate, or use to distinguish a primary unit.

### Ceiling — not too dense

The inventory is too dense when a primitive exists only because of:

- grammatical packaging;
- incidental nounhood;
- clause-level elaboration;
- discourse/narration scaffolding;
- support scaffolding not independently researchable;
- vivid but non-indexed detail;
- repeated wording already represented by the same source identity;
- a relation whose only contribution is recoverable inside another admitted primary coordinate.

The correct inventory sits between those bounds.

## 10. Compounds project primary relations, not the entire semantic graph

A compound represents one admitted **primary multi-coordinate relation** using two or more frozen primitive refs.

Create one primary compound when a source-established primary research unit contains two or more admitted primitives that jointly form an independently researchable relation/configuration.

Do **not** create a compound merely because:

- two primitives co-occur;
- a sentence or clause contains them;
- a support can be attached to a relation;
- an internal semantic binding can be imagined;
- one primitive modifies another grammatically;
- a subset/superset relation can be generated;
- a graph edge or transitive closure exists.

A single primary unit may contain more than one compound only when it contains more than one independently researchable relation after the same editorial-grain test. Several clauses may project to one compound when they elaborate the same primary relation.

Include all and only the admitted primitives that constitute the primary relation. Include PLACE/TIME support only when that support is materially part of the relation's identity or needed to distinguish it from another admitted relation; do not mechanically attach all scene support to every compound.

Do not create a compound to compensate for a missing primitive. Correct the primitive set first. Do not create alternate duplicate subset/superset versions of the same primary relation.

Code owns canonical compound IDs, ordering normalization, reference validation, and `Q` construction where the apparatus specifies them.

## 11. Final researcher-index audit

Before output, imagine the inventory as a compact index a later researcher will use without rereading every word of the source.

For every primitive ask:

- What primary research unit needs this coordinate?
- What independent retrieval/comparison job does it perform?
- Would a researcher plausibly point to this exact coordinate separately later?
- If removed, is a primary unit materially harder to recover or distinguish?
- If retained, does it add an actual coordinate rather than grammatical or descriptive texture?

For every compound ask:

- Which primary research relation does it represent?
- Does that relation independently survive the editorial-grain test?
- Are all and only its participating admitted primitives present?
- Is another compound already representing the same relation?
- Was support included only because it materially identifies this relation?

Delete rows that fail the ceiling test. Restore rows that fail the floor test. Do not target a count.

## 12. Qualities flag

`qualities_available` is only a yes/no indication that source qualities/descriptions exist for a coordinate. It does not replace LABEL, does not require every quality to become a primitive, and does not authorize deeper APA analysis.

## 13. Identity and ordering

Primitive identity is class-local source identity after true coreference, not mention count.

Code owns canonical output IDs. Supply only neutral identity keys where requested. Order by first source establishment after coreference, subject to speaker-first PERSON and genuine broad-before-contained support ordering.

## 14. Worker isolation boundary

The calibration worker must never receive:

- Case 2 or Case 6 gold workbook rows or canonical extracts;
- expected counts;
- evaluator findings;
- scored prior outputs;
- case-specific hidden corrections/examples;
- `researcher_inventory/tests/holdout/CASE_5.sealed.txt` during calibration;
- any Case 5 holdout output;
- any indirect encoding of hidden answers.

The worker receives only the supplied source, this finalized durable contract/task rules, the apparatus schema/task prompt, and ordinary runtime metadata needed to execute.

## 15. Candidate-only boundary

All outputs remain candidate/training records. Never promote to Oval Office or sovereign/admitted APA research, mint APA IDs, write to APA production/sovereign fabric, perform APA scoring/psychological interpretation, or convert calibration success into sovereign authority.

## 16. Harness-versus-worker separation

Change evaluator/harness mechanics only when independent evidence establishes that comparison, canonicalization, alignment, serialization, isolation, prompt composition, source-span validation, evidence preservation, or holdout gating is defective.

The V126A contract-subordinate request envelope remains the harness authority. When immutable hashes verify, its deterministic tests pass, and the saved agent is freshly bootstrapped from the declared durable contract, ordinary hidden-archetype mismatch is worker-semantic evidence unless contrary evidence appears.

Do not modify the harness merely to make a worker-semantic failure score better.

## 17. Calibration and certification gate

Verify immutable workbook hashes before every execution. Repair from authoritative source only when verification fails and never treat an unverified copy as gold.

Under one finalized V129 contract and one saved-agent calibration lineage:

1. run one paired Case 2 + Case 6 diagnostic batch;
2. if and only if both pass, run two repeated paired verification batches with two repetitions each;
3. only after all paired archetype attempts pass may the calibrated lineage access sealed Case 5 exactly once;
4. if that holdout is archetypal, retire that calibration lineage;
5. create a brand-new saved agent containing only finalized V129 durable instructions;
6. run sealed Case 5 exactly once in a fresh session;
7. certify only if that fresh agent passes without access to prior sessions or holdout output.

A failed archetype run stops the current pipeline before any holdout stage. Preserve the failure and derive any later successor only from a demonstrated generalizable requirement.
