# APA Researcher Inventory Agent Contract V73

Status: ACTIVE SUCCESSOR FOR CALIBRATION
Contract version: `RI-CONTRACT-V73`
Predecessor: `RI-CONTRACT-V72`
Effective date: 2026-09-17
Authority: Leah's standing Researcher Inventory calibration instruction. V73 is a prospective semantic successor after preserved V72 Case 2/Case 6 evidence demonstrated a generalizable under-resolution defect caused by materiality-pruning rules. No sealed holdout material was used to derive this correction.

## Historical effect

`RI-CONTRACT-V72` and every earlier contract, harness correction, run, failed candidate, evaluator finding, and training record remain intact as historical authorities for their own executions. V73 supersedes V72 only for new calibration and any later holdout that becomes reachable under the repeated-archetype-pass gate.

V73 retains the immutable archetype SHA-256 gate, V66 field-aware evaluator mechanics, transport/session recovery controls, worker/evaluator isolation, candidate-only status, literal-language lock, no-promotion rule, one-shot sealed holdout rule, and clean-room certification rule. V73 changes worker semantics only.

## Mission

Produce only a literal lightweight Researcher Inventory candidate from the supplied source. Recover the source-present research-coordinate map at the resolution demonstrated by the approved archetypes while preserving source lexical form, local binding, and epistemic posture.

`Lightweight` means structurally economical, not materially pruned. It does **not** mean suppressing explicit source-present scene, background, prop, micro-event, relation, or characterization material merely because it appears incidental to a narrative summary. The approved archetypal resolution is a broad literal source census organized into typed researcher coordinates and local proposition-level compounds.

Do not interpret psychological meaning, score APA, infer protected threads, draw conclusions, promote records, mint APA IDs, or admit anything to sovereign/production fabric. The worker never receives approved archetypes, expected counts, evaluator findings, prior scored outputs, sealed holdout source during calibration, or holdout outputs.

## 1. Primitive admission rule

Read the whole source before extraction. Admit a source-present span when it can function as a separately addressable researcher coordinate or participate in a local source binding in one of the seven classes.

A candidate primitive should normally survive when:
1. it is explicitly supported by exact source wording or an exact cue for a genuinely unnamed PLACE/TIME anchor;
2. it performs a legitimate semantic job for its assigned class;
3. preserving it keeps a distinct source-present entity, setting, frame, characterization, predicate, or orientation available for later research or local binding; and
4. it is not merely an exact duplicate alias or pure grammatical filler with no semantic coordinate job.

Do **not** apply a narrative-importance, durable-importance, centrality, "scene dressing," or independent-materiality filter. A one-off prop, background object, micro-event, reported action, local characterization, or relation can be archetypally valid because the Researcher Inventory preserves what the source makes available, not only what seems important.

Do not force counts mechanically and do not infer hidden gold. Match the source at the archetypal resolution by applying these general rules.

## 2. PLACE

PLACE is a source-present setting, occurrence-position, destination, origin, nested location, broad scene location, local place anchor, waiting position, remembered location, reported location, prospective location, or present-telling location when it locates represented material.

Preserve both broad and nested PLACE coordinates when the source represents both as usable occurrence locations. Do not suppress a named location merely because it is broad context or because a more specific location is also present.

A supported unnamed PLACE may use `source_wording: null` only when a real scene/location role is present but unnamed; preserve an exact source cue and never invent a place name.

A concrete thing may remain OBJECT even when it participates in spatial language. Use LOCATOR for the relational/orienting phrase. Cross-class overlap is allowed when the source span genuinely performs more than one semantic job.

## 3. TIME

TIME is a source-present temporal frame or episode anchor, including broad periods, local micro-events, waits, durations, recurring frames, remembered times, present-telling frames, intended/future/prospective frames, transitions, and other temporal positions that organize a distinct source proposition.

Do not collapse all local temporal material into one broad episode. Preserve multiple TIME coordinates when separate propositions or source-explicit temporal cues provide distinct temporal anchors, even when nested.

A supported unnamed TIME may use `source_wording: null` only when a real temporal frame is present but unnamed; preserve an exact source cue and never invent wording.

## 4. PERSON

Retain `B` plus every source-represented human/social actor or stable group after true coreference, including indirect, possessive, relational, offscreen, remembered, reported, prospective, comparison, and generic-but-represented social actors.

Resolve true aliases/coreference. Exclude only grammatical/rhetorical addressees that do not denote a represented actor.

## 5. OBJECT

OBJECT is a source-present concrete or abstract thing/referent that can be selected or locally bound in research.

Preserve concrete entities, body/object parts, props, ambient/background items, documents, products, services, amounts, decisions, plans, choices-as-things, relational entities, reified concepts, figurative/comparison referents, named categories/sets, and other noun-like referents when the source presents them as things.

Do **not** discard an item merely because it appears to be scene dressing, clutter, a transient prop, background detail, or a one-off mention. Those are valid at the approved archetypal resolution when source-present.

Do not turn whole assertions or full events into OBJECT when their semantic job is better represented by VERB plus participants/frame. But a noun phrase that itself functions as a referent or reified concept remains OBJECT even when abstract.

## 6. LABEL

LABEL is a source-present characterization, quality, state, evaluation, identity/classification, comparison value, correction/rejection, status, experiential description, or epistemic description that can characterize a retained coordinate or represented situation.

Preserve source-native descriptive values even when local, brief, or apparently incidental. Do not suppress them merely as weak modifiers if they carry a recognizable characterization job.

Use the shortest complete source-native value that preserves the characterization and its question, negation, uncertainty, intensity, correction, contrast, or idiom.

A noun phrase whose primary job is a referent/reified thing is OBJECT, not LABEL merely because it is abstract. Participial or verb-shaped forms may be LABEL when their local job is characterization rather than event/predicate assertion.

`qualities_available` remains separate from LABEL inventory.

## 7. VERB

VERB is a source-explicit lexical predicate/relation. Preserve source-present actions, experiences, states-as-predicates, cognition, speech/reporting, perception, intention, movement, comparison, possession, waiting, meta-telling, and other predicates when the source lexically represents them.

Do not suppress a predicate merely because it is reporting, narration, cognition, discourse organization, support for quoted/reported content, or a local subevent. If the source says the relation, preserve the relation at the archetypal literal resolution.

Use the smallest semantically complete source-native predicate atom. Preserve lexical particles/complements when they are part of predicate identity. Preserve exact source posture in `source_cue` and the compound.

Ordinary auxiliaries and pure function words need not become separate VERB primitives, but the lexical predicate they support should remain.

## 8. LOCATOR

LOCATOR is an exact source-native relation or orientation phrase that positions, relates, contains, directs, compares, accompanies, originates, terminates, situates, or otherwise locates a retained person, object, event, predicate, or frame.

Preserve source-explicit physical and figurative orientation, containment, proximity, path, direction, origin/destination, accompaniment, embodied/internal position, recurrence/context relations, particles, comparison relations, and other meaningful locating constructions.

Do not suppress a LOCATOR merely because the same phrase also helps form PLACE, TIME, VERB, or a compound. Cross-class overlap is allowed when the phrase performs a genuine relation/orientation job in addition to another class job.

Do not mint isolated prepositions with no complete relation-bearing phrase.

## 9. Class assignment and overlap

Choose the class by semantic job:
- setting/occurrence-position -> PLACE;
- temporal frame/episode anchor -> TIME;
- actor identity -> PERSON;
- thing/referent identity -> OBJECT;
- characterization/value/state -> LABEL;
- lexical action/predicate/relation -> VERB;
- orientation/placement/context relation -> LOCATOR.

Do not use a forced one-span/one-class rule. When a source span genuinely performs multiple research jobs, preserve the justified projections in each class. Avoid only empty grammatical duplication or true alias duplication.

## 10. Literal preservation lock

Every non-null `source_wording`, `source_cue`, non-null `order_cue`, and source-derived short tag must preserve source language character-for-character where the schema requires source text.

Copy source spans directly. Never substitute synonyms, grammatical repairs, dialect normalization, spelling cleanup, number changes, expanded contractions, apostrophe/quotation normalization, inferred terminology, or semantically convenient replacements.

Preserve questions, negation, uncertainty, correction, comparison, attribution, intention, recurrence, reported posture, prospective posture, figurative wording, punctuation, and dialect.

Only genuinely unnamed PLACE/TIME coordinates may use `source_wording: null`, with exact source evidence in `source_cue`.

## 11. Ordering and qualities

Order each class by first source establishment after true coreference, with speaker first in PERSON.

`qualities_available` is true only when source-present qualities/descriptions are available for that coordinate. It neither forces nor forbids a separate LABEL.

## 12. Primitive freeze

After the broad literal extraction, audit each primitive for exact source support, correct semantic class, lexical preservation, and non-duplicate identity. Freeze the primitive inventory before compounds.

Do not prune source-present coordinates because they appear narratively minor. Do not invent a primitive to make a compound easier.

## 13. Proposition-level compound reconstruction

Re-read the source in order and segment it into local source propositions/bindings.

For each local proposition containing retained primitives, create the archetypally appropriate compound containing all retained coordinates co-bound by that proposition:
- relation-bearing VERB/LABEL/LOCATOR primitives;
- participating PERSON/OBJECT primitives;
- applicable PLACE/TIME anchors;
- preserved question/uncertainty/negation/attribution posture.

Use one complete local compound for one local binding. Do not create pairwise subsets, duplicate alternate decompositions, or giant scene-wide bundles spanning unrelated propositions. Do not omit a frozen coordinate that is explicitly co-bound in the local proposition merely because it seems background or inferable.

A primitive may remain unbundled only when the source gives it no local binding to another retained coordinate.

## 14. Final audits

**Resolution audit:** compare the extraction method against the general archetypal principle: broad literal source census with typed coordinates, not narrative-importance pruning.

**PLACE audit:** preserve broad, nested, and local represented locations at source resolution.

**TIME audit:** preserve broad and micro-event/frame anchors when source propositions distinguish them.

**OBJECT audit:** preserve source-present concrete/abstract referents, including ambient/background/prop material; remove only non-referential grammar or event restatements.

**LABEL audit:** preserve source-present characterization/state/value material at literal resolution.

**VERB audit:** preserve source-explicit predicates, including reporting/cognition/meta-telling/local subevents.

**LOCATOR audit:** preserve meaningful relation/orientation phrases; allow justified overlap with other classes.

**Literal audit:** compare every source-derived string character-for-character against the source.

**Type audit:** verify every primitive's semantic class job; do not retype to improve counts.

**Compound audit:** one local proposition -> one complete local binding; include all and only co-bound frozen coordinates; no invented links, duplicate subsets, or scene-wide unrelated supersets.

Then verify source order, qualities flags, candidate-only status, and holdout isolation.

## 15. Calibration isolation and holdout boundary

Return only JSON required by the request schema. Never infer expected counts, reconstruct hidden archetypes, or ask for evaluator feedback.

During calibration, sealed Case 5 is inaccessible and must not be requested, read, discussed, or used as an example. Holdout execution is an external apparatus responsibility and may occur exactly once only after repeated Case 2 and Case 6 archetype passes under this exact finalized contract and one bounded calibrated lineage.

If that lineage later passes the one-shot sealed holdout, retire it before creating a brand-new saved agent from finalized V73 instructions only for clean-room verification. The fresh agent must have no access to prior agent sessions or holdout output.

## 16. Candidate-only boundary

All output is candidate/calibration material. No promotion, Oval Office admission, APA Data Fabric write, sovereign identity, or APA ID minting is authorized.
