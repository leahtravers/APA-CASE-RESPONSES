# Researcher Inventory Durable Worker Contract V46

Status: `ACTIVE CALIBRATION SUCCESSOR — NOT CERTIFIED`
Contract ref: `RI-CONTRACT-V46`
Predecessor: `RI-CONTRACT-V45`
Effective for new calibration only: 2026-09-15

## 1. Scope

Produce the lightweight Researcher Inventory candidate only. Inventory the source; do not interpret it, score APA, infer psychological meaning, draw conclusions, promote records, mint APA IDs, or admit anything to sovereign/production fabric.

V46 preserves the immutable-archetype gate, literal/source-near lock, hidden-evaluator isolation, candidate-only boundary, failed-attempt preservation, one-shot holdout gate, and clean-room certification requirements. It changes only prospective semantic admission, primary class assignment, supported scene/time role construction, and compound reconstruction.

## 2. Why V46 exists

V45 treated each source-established class-native coordinate as independently admissible unless it was grammar, an alias, an arbitrary fragment, or analyst invention. Repeated cross-case calibration showed that this rule is too permissive for the approved lightweight inventory: it converts local lexical, nested, descriptive, temporal, orienting, and proposition-like material into too many independent rows and then reproduces that inflation in compounds. At the same time, purely lexical admission can still miss supported unnamed scene/time coordinates needed to reconnect who or what participated in a materially distinct represented frame.

The general V46 correction is **canonical binding-role coordinate admission**.

The inventory is neither a lexical census nor a minimal summary. Preserve the independent coordinates needed to reconstruct the source-presented participant/referent/predicate/place/time/orientation/characterization bindings at lightweight research grain. A source span does not earn a row merely because it is explicit, separable, local, nested, descriptive, or independently variable. Conversely, an unnamed PLACE or TIME may be required when a materially distinct source-presented binding needs a scene or episode anchor.

## 3. Whole-source binding reconstruction before class extraction

Read the complete source before answering any requested class. Build silently:

1. a **frame map** of materially distinct represented scenes, episodes, interactions, recollections, reports, recurring periods, intended/hypothetical/prospective frames, and present telling/reflection;
2. a **participant/referent map** of persons and source-treated things that serve as stable arguments in those frames;
3. a **predicate map** of the operative source relations that bind participants/referents and preserve source posture;
4. a **scene/time map** assigning each materially distinct frame the PLACE/TIME navigation coordinates needed to distinguish it, including supported unnamed coordinates when the source gives no explicit name/date;
5. an **orientation/characterization map** of only those LOCATOR/LABEL roles that independently modify or orient a retained binding rather than merely repeating grammar or lexical detail.

These maps define the research-coordinate roles. They are not output themselves and they must not be reduced to a narrative summary.

## 4. Canonical binding-role admission test

Admit a candidate unit only when all are true:

1. **Source support** — the source explicitly supports the coordinate, or it is a permitted supported unnamed PLACE/TIME role anchored to exact source text.
2. **Binding role** — the candidate occupies an independent role in at least one retained source-presented frame/relation: participant, referent/content, operative predicate, scene, time, orientation, or characterization.
3. **Research independence** — removing it would erase a materially distinct role needed to reconnect the represented binding at lightweight research grain, not merely remove lexical detail from a role already represented.
4. **Primary semantic identity** — assign the coordinate to the class that best expresses its role in the binding map. A second class requires a genuinely different independent role, not surface ambiguity or part-of-speech flexibility.
5. **Natural grain** — use the smallest complete source-near form that preserves that role without splitting a governing relation or turning modifiers/arguments into stand-alone units.
6. **Distinctness** — after coreference, alias, occurrence, and frame reconciliation, it is not the same research coordinate already retained.
7. **No analyst invention** — the role can be grounded in the source without importing interpretation, hidden evaluation, expected answers, or external categories.

A broader sentence or scene does not suppress a legitimate role coordinate. But source explicitness alone does not create a coordinate. Local, one-use, reported, remembered, possessive, descriptive, prospective, or nested material survives only when it fills an independent binding role under this test.

## 5. Role-first omission and excess passes

For each requested class:

1. reconstruct the complete binding/frame map;
2. identify every role of that class required by those bindings;
3. map explicit source spans or supported unnamed PLACE/TIME anchors to those roles;
4. merge aliases/coreference and repeated mentions of the same role;
5. suppress lexical/grammatical material that does not occupy a distinct role;
6. run an omission pass for missing roles;
7. run an excess pass for rows that merely restate a role already represented.

Suppress, in particular:

- auxiliaries, determiners, complementizers, bare prepositions, tense/aspect support, discourse wrappers, and ordinary argument marking;
- proposition/clause wrappers when the operative relation and its arguments already carry the binding;
- descriptive or evaluative fragments that do not function as independent characterization roles;
- temporal words or action substeps that do not define a distinct episode role;
- physical nouns or place names that do not function as scene coordinates;
- nested lexical predicates that do not instantiate a separate bound event/relation;
- cross-class duplicates created only by surface multifunction;
- true aliases/coreference duplicates and repeated mentions of the same research coordinate;
- analyst-created abstractions or normalized paraphrases.

Do not suppress a supported unnamed scene/time role merely because it lacks a named lexical phrase.

## 6. Primary-class rule

Choose the class from the coordinate's **primary semantic job in the binding map**, not from surface part of speech.

- If source wording denotes a thing/content/relation treated as a selectable argument, prefer `OBJECT` even when its wording is descriptive.
- If wording characterizes another retained coordinate, prefer `LABEL`.
- If wording supplies the operative relation, prefer `VERB`.
- If wording supplies path, destination, position, recurrence, or other binding-relevant orientation, prefer `LOCATOR` rather than creating an episode merely because the phrase describes an action or temporal context.
- If the role is the scene in which represented material occurs, use `PLACE`.
- If the role is the episode/period that distinguishes represented material, use `TIME`.

Cross-class reuse is exceptional. Retain the same source material in two classes only when the binding map contains two genuinely independent roles that would otherwise be lost.

## 7. Class rules

### PLACE

PLACE is a **scene/occurrence-position coordinate** used to situate a retained frame, participant, or materially distinct represented action.

Retain:

- a broad or contained physical scene when it is needed to locate a retained binding;
- a materially distinct participant/action position even when the physical venue is unnamed or overlaps another scene;
- origin/destination sites when they function as scene coordinates rather than only as path language;
- the scene of a materially distinct remembered/reported interaction, waiting episode, recurring activity, or present telling when the source supports such a scene role.

A supported unnamed PLACE uses `source_wording = null`, an exact source cue, and a neutral navigation tag.

Do not retain every physical noun, geographic expression, body/surface/container, generic locality, or place-like referent. A named place is not automatically a PLACE row unless it performs a scene role in a retained binding. Prefer the role coordinate over a lexical place census.

### TIME

TIME is an **episode/period/frame coordinate** used to distinguish materially different represented bindings.

Retain:

- a materially distinct earlier/later/current episode;
- a remembered/reported period that anchors a separate binding;
- a recurring span when recurrence itself organizes a retained frame;
- an intended/hypothetical/prospective period when the source separately represents that frame;
- present telling/reflection when it is a distinct frame that must reconnect to present-tense relations;
- a supported unnamed episode when a materially distinct binding would otherwise have no temporal frame coordinate.

A supported unnamed TIME uses `source_wording = null`, an exact source cue, and a neutral episode tag.

Do not create TIME for every action, question, transition, duration phrase, date-like mention, temporal adverb, subordinate clause, or lexical cue inside an already represented episode. Several actions may share one TIME. A phrase may instead be a LOCATOR if its primary job is orientation/recurrence/context rather than episode identity.

### PERSON

Retain the speaker and every distinct human/social actor or stable actor group that fills an independent participant or relational-person role in a retained binding.

Background, remembered, reported, possessive, prospective, or one-use persons may qualify when they fill such a role. Resolve pronouns, titles, kinship terms, and aliases before deduplication.

Do not create PERSON from generic audiences, grammatical person marking, hypothetical placeholders, or mentions that do not establish a distinct human coordinate.

### OBJECT

OBJECT is a **stable selectable referent/content role** used as an argument in a retained binding.

Retain source-treated concrete things, abstract contents, choices, decisions, values, relations, sets/categories, results, services, internal/figurative objects, or represented content when the source treats them as independently trackable things.

A descriptive-looking phrase may be OBJECT when the source uses the whole phrase as the thing being referred to. Conversely, do not create OBJECT for every noun phrase, pronoun, grammatical complement, proposition wrapper, discourse phrase, or place noun whose only role is location.

Prefer the smallest complete referential whole. Nested parts survive only when they fill a separate retained binding role.

### LABEL

LABEL is an **independent characterization role** applied to a retained coordinate or proposition.

Retain a characterization, classification, comparison, state, evaluation, correction, rejection, polarity, identity term, or characterization-question when the characterization itself is necessary to preserve a source-presented distinction in a retained binding.

Use the shortest complete source wording that preserves the characterization and its uncertainty/negation/question/correction posture.

Do not convert every adjective, adverb, manner phrase, evaluative aside, discourse token, or descriptive subphrase into LABEL. If the whole phrase is functioning as a selectable thing/content, prefer OBJECT. If it is only part of a predicate or orientation, keep it with that role.

### VERB

VERB is an **operative source relation/predicate role** in a retained binding.

Prefer the complete governing lexical relation that connects the relevant participants/referents while preserving source posture. Keep particles, negation, reflexive material, or bound complements needed to preserve that relation.

Retain an embedded/reporting/cognition/perception/intention/question predicate separately only when it creates a distinct bound event/relation with its own materially different role structure. Do not split every matrix/embedded verb or every lexical predicate token merely because both are explicit.

Do not create VERB for auxiliaries/support grammar, predicate shells whose only content is a retained LABEL/LOCATOR, repeated lexical mentions of the same relation, or subordinate micro-actions that do not form a separate retained binding.

Inventorying a predicate never asserts that its event happened.

### LOCATOR

LOCATOR is a **binding-relevant orientation relation**: where/which-position/which-path/which-destination/which-recurring-or-contextual orientation connects a retained coordinate to its frame.

Retain the smallest complete meaningful construction when it supplies a distinct position, path, direction, origin/destination, containment, proximity, movement, recurrence, situational context, or figurative orientation needed by a retained binding.

A goal/destination or next-step construction can be LOCATOR when its primary job is navigation/orientation rather than episode identity. Multiple LOCATORs may coexist only when they fill different orientation roles.

Do not retain ordinary possession, beneficiary/recipient marking, topic marking, comparison support, complement marking, every prepositional phrase, or every temporal subordinate phrase. A bare preposition is never sufficient. If removing the phrase leaves the binding's orientation unchanged, omit it.

## 8. Literal lock and posture

- Every non-null `source_wording`, every `source_cue`, and every non-null `order_cue` must be a character-for-character contiguous source substring.
- Preserve punctuation, spelling, dialect, negation, uncertainty, question, correction, comparison, intention, hypothetical, recurrence, report, and prospective posture.
- For explicitly worded coordinates, `researcher_short_tag` may use only words already present in that coordinate's `source_wording` and/or `source_cue`.
- Supported unnamed PLACE/TIME may use a neutral navigation tag grounded by exact source cue.
- Copy literal spans from source; do not reconstruct them from memory.
- `qualities_available` is boolean metadata only and never creates a unit.

## 9. Ordering and identity

Code owns canonical IDs. The worker supplies neutral canonical keys only for alias/coreference merge.

Order units by first source establishment of the retained binding role after coreference, subject to apparatus rules that place the speaker first and broad-before-contained PLACE/LOCATOR coordinates when genuinely established together. Remembered/reported/hypothetical/future frames stay at source position rather than being reordered into real-world chronology.

Do not reorder by importance.

## 10. Unit freeze, then canonical binding compounds

Complete and freeze the unit ledger before compounds. Compounds may not create, suppress, merge, repair, rename, or retype units.

Then rebuild the source binding map using frozen units only.

Emit **one canonical compound per materially distinct retained source binding/frame**. A compound should contain the smallest complete set of frozen refs that expresses that binding's necessary participants/referents, operative predicate, and any PLACE/TIME/LOCATOR/LABEL role needed to distinguish or qualify it.

Rules:

- Prefer one complete canonical binding over multiple nested phrase/subset compounds for the same relation.
- A reporting/cognition/intention wrapper receives its own compound only when it is itself a distinct retained binding rather than merely the carrier of another relation.
- Do not make a compound for every unit, every sentence, every pair, every nested clause, or every co-occurring phrase.
- Do not emit combinatorial subset closure.
- Do not duplicate one binding under alternate lexical decompositions.
- Preserve source direction and posture.
- Use registered frozen unit references only.

## 11. Final adjudication

Before return:

1. reread the complete source;
2. rebuild the frame and binding-role maps;
3. ask whether every materially distinct retained binding has the necessary PERSON/OBJECT/VERB and scene/time/orientation/characterization roles;
4. specifically check whether a distinct frame needs a supported unnamed PLACE or TIME even when no explicit place/time phrase appears;
5. apply primary semantic class assignment and remove cross-class duplicates without an independent second role;
6. collapse lexical/nested/detail rows that do not fill independent binding roles;
7. verify natural grain and exact-source locks;
8. freeze units;
9. emit one canonical compound per retained binding/frame;
10. remove duplicate/nested/subset compounds representing the same binding;
11. verify source order and posture.

The target is a **complete lightweight binding-role inventory**: enough independent coordinates to reconstruct the source-presented research bindings without lexical census behavior, lost scene/time navigation, or analyst invention.

Never target an expected count or infer a hidden archetype.

## 12. Isolation and protected evaluation

The worker must never receive Leah-approved archetype workbook contents, archetype rows or expected counts, evaluator findings or scored outputs, case-specific gold corrections, prior failed-output corrections derived from hidden gold, the sealed Case 5 source during calibration, or any Case 5 holdout output.

Mechanical validator feedback may be returned only for deterministic schema, exact-source, tag-token, identifier, or equivalent mechanical defects. It is not gold/evaluator guidance.

## 13. Calibration and certification gate

V46 is not certified by existing.

Before sealed holdout use, the same finalized V46 contract and saved-agent lineage must repeatedly pass immutable Case 2 and Case 6 archetype verification for resolution, lexical preservation, class assignment, and compound construction.

Only then may the protected harness run sealed Case 5 exactly once on that calibrated lineage. If it passes archetypally, retire that lineage, create a brand-new saved agent from this finalized durable contract only, and run sealed Case 5 in a new clean-room session. Certification requires the fresh agent to pass without access to prior sessions or holdout output.

Any failed holdout remains final evidence for that lineage and may not be reused as calibration material.

## 14. Historical effect

`RI-CONTRACT-V45` remains authoritative historical evidence for executions that actually ran under V45. V46 supersedes V45 prospectively only for new Researcher Inventory calibration and any later protected stage lawfully reached from a successful V46 calibration lineage.

Retained from V45: immutable archetype verification, exact-source lock, hidden evaluator isolation, candidate-only storage, failure preservation, saved-agent lineage discipline, protected one-shot holdout, and clean-room certification law.

Superseded from V45: exhaustive source-established-coordinate admission, permissive cross-class reuse, outer-and-embedded-predicate default retention, broad source-presented orientation retention, and nested/overlapping relation-instance compound construction where those rules conflict with V46 canonical binding-role admission.