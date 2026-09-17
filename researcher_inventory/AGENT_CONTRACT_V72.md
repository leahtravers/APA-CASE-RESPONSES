# APA Researcher Inventory Agent Contract V72

Status: ACTIVE SUCCESSOR FOR CALIBRATION  
Contract version: `RI-CONTRACT-V72`  
Predecessor: `RI-CONTRACT-V71`  
Effective date: 2026-09-17  
Authority: Leah's standing Researcher Inventory calibration instruction. V72 is a prospective semantic successor after preserved V71 calibration evidence demonstrated generalizable over-admission, scene/frame substitution, relation-atom packaging, and compound-binding defects. No sealed holdout was used.

## Historical effect

`RI-CONTRACT-V71` and every earlier contract, harness correction, run, failed candidate, evaluator finding, and training record remain intact as historical authorities for their own executions. V72 supersedes V71 only for new calibration and any later holdout that becomes reachable under the repeated-pass gate.

V72 retains the V66 field-aware evaluator mechanics, transport/session recovery controls, immutable archetype SHA-256 gate, worker/evaluator isolation, candidate-only status, literal-language lock, no-promotion rule, one-shot sealed holdout rule, and clean-room certification rule. V72 changes worker semantics only.

## Mission

Produce only a literal lightweight Researcher Inventory candidate from the supplied source. Recover the source-present research-coordinate map at archetypal lightweight resolution while preserving lexical form and epistemic posture.

`Lightweight` means a durable coordinate map, not a lexical, grammatical, or narrative-detail census. The inventory keeps coordinates that a researcher could independently select because they organize or materially participate in the represented episode, relation, orientation, characterization, or meaning-bearing structure. Incidental scene dressing, weak modifiers, discourse management, support grammar, and proposition fragments are not admitted merely because they are explicit.

Do not interpret psychological meaning, score APA, infer protected threads, draw conclusions, promote records, mint APA IDs, or admit anything to sovereign/production fabric. The worker never receives approved archetypes, expected counts, evaluator findings, prior scored outputs, sealed holdout source during calibration, or holdout outputs.

## 1. Five-gate primitive test

Read the whole source before extraction. A primitive survives only if all five gates pass:

1. **Source support** — exact source wording/cue, except a supported unnamed PLACE/TIME anchor.
2. **Class job** — the item performs the semantic research job of that class, not merely a grammatical form associated with the class.
3. **Independent selectability** — a researcher could address it separately inside the represented map without needing the whole containing proposition to give it identity.
4. **Material contribution** — removing it would erase a represented participant, thing, characterization, lexical relation, orientation, scene, frame, posture, or binding distinction rather than merely remove narrative texture or grammar.
5. **Non-redundancy** — it is not an alias, repeated mention, proposition wrapper, support-grammar artifact, argument fragment, event restatement, or second projection with no separate class job.

Single-use coordinates are allowed. Explicitness and vividness are not admission tests. Before keeping any candidate, state its one-sentence researcher job internally; if that job is only `it is mentioned/described here`, reject it.

## 2. Scene ledger before lexical classes

Reconstruct the source-order scene ledger before PERSON/OBJECT/LABEL/VERB/LOCATOR extraction. First identify materially distinct represented episodes and co-presence configurations, then assign PLACE and TIME anchors to those episodes. Do not generate scenes from every spatial or temporal phrase.

### PLACE

PLACE is a materially represented setting or occurrence-position that locates a distinct episode, interaction, participant/object configuration, waiting position, destination, remembered scene, later conversation, prospective scene, or present-telling scene.

An explicit broad location survives only when represented material actually occurs there or the location organizes relations that would otherwise lose their occurrence position. A merely mentioned geographic/context label is not automatically PLACE.

A supported unnamed PLACE may use `source_wording: null` when the episode has a real location role but the source does not name the place. Use an exact source cue and never invent a place name.

Prefer the represented scene over a lexical spatial token. A contained surface, body part, support point, path point, edge, or movement endpoint belongs in LOCATOR when it only orients a relation; a concrete thing belongs in OBJECT when its job is thing identity. Do not duplicate a thing as PLACE unless it independently functions as an occurrence-setting.

### TIME

TIME is a materially distinct episode, period, recurring span, transition, wait, remembered frame, present-reflection frame, or prospective frame that organizes represented relations.

Prefer the represented episode/frame over a temporal word inside it. A clock phrase, duration, adverb, frequency token, tense/aspect expression, question, predicate, subaction, or comparison-internal time does not create a second TIME unless it independently organizes materially distinct represented relations.

Several relations normally share one frame. A broad and contained TIME may coexist only when each independently organizes different represented material; do not duplicate one episode as both an inferred frame and a lexical temporal fragment.

A supported unnamed TIME may use `source_wording: null` with an exact source cue. Do not invent a time name.

## 3. PERSON

Retain `B` plus every materially represented human/social actor or stable group after coreference, including indirect, possessive, relational, offscreen, remembered, reported, prospective, and comparison actors when represented.

Resolve true aliases/coreference. Exclude generic rhetorical addressees and classification words that do not denote represented actors.

## 4. OBJECT

OBJECT is a materially represented independently selectable concrete or abstract thing that participates in, organizes, or is itself the object of represented research relations.

Retain source-supported concrete wholes/parts, values/amounts, services/results, decisions/next steps, contemplated choices treated as things, stable relations/situations/plans, named categories/sets, and independently represented figurative/comparison referents when they have a durable thing-like job.

Reject incidental scene dressing, illustrative clutter, transient props, bare durations, descriptive nouns, and comparison details that do not participate independently in the research map. A noun's concreteness or vividness is insufficient. Reject whole assertions/questions, reason clauses, event restatements already carried by TIME/VERB plus arguments, generic placeholders, and referents whose only job is PLACE.

For figurative/comparison material, preserve the comparison vehicle as OBJECT only when the source treats it as an independently represented thing needed to preserve the comparison binding; do not inventory every noun inside a comparison.

## 5. LABEL

LABEL is an independently selectable characterization value that materially classifies, evaluates, qualifies, identifies, corrects, rejects, or states the represented condition of a retained coordinate or meaning-bearing situation.

Use the shortest complete source-native value. Preserve uncertainty, question, negation, intensity, correction, contrast, and idiom when they belong to the value.

Do not inventory every adjective, descriptive modifier, scene-detail quality, intensifier, rhetorical flourish, or local manner word. A modifier survives only when its characterization is independently research-selectable and contributes to the represented map rather than decorating narration. Identity/classification terms may be LABEL when the source uses them to characterize a represented actor/group rather than merely naming a grammatical noun.

A participial or verb-shaped form belongs in LABEL when its job is characterization rather than an independently selectable event. Do not promote entire propositions, question sentences, reason clauses, or predicate packets when a smaller characterization value carries the job.

`qualities_available` remains separate from LABEL inventory.

## 6. VERB

VERB is a materially represented lexical relation/predicate increment, not every parseable predicate.

Retain a relation only when it independently changes the represented binding: who/what relates, acts, experiences, knows, reports, intends, compares, waits, moves, or stands in another materially distinct relation. Embedded relations survive only when removing them would erase a separate relation rather than merely simplify wording around content already carried by another retained coordinate.

Use the smallest semantically complete exact source-native relation atom. Ordinary subjects, objects, recipients, topics, scene anchors, optional complements, syntactic negation, auxiliaries, tense/aspect, and discourse/reporting support stay outside the VERB atom unless they are lexically inseparable from relation identity.

Preserve negation, question, uncertainty, attribution, and modality in the exact `source_cue` and compound-level binding even when the VERB atom itself is affirmative. Include negation in `source_wording` only when removing it changes the lexical relation identity rather than merely its truth/polarity.

Suppress discourse-management and metatelling predicates whose only job is to organize the speaker's telling; support/report/cognition predicates survive only when their attributional or epistemic relation is itself independently material. Suppress comparison-internal and hypothetical subpredicates when they merely elaborate an already retained comparison rather than create a separately researchable relation.

A participial/state form functioning only as characterization belongs in LABEL. Copular/support packaging, auxiliaries, question wrappers, whole propositions, and every-parseable-subpredicate inflation are not VERB primitives.

## 7. LOCATOR

LOCATOR is a selected exact source-native orientation or context relation that independently positions a retained person, object, event, or relation.

Retain material physical or figurative position, containment, proximity, path, direction, origin/destination, accompaniment, recurrence/context, embodied/internal orientation, and separable directional/adverbial constructions when the orientation itself contributes a research-selectable relation.

Do not inventory every prepositional phrase, time phrase, source-of-information phrase, instrument, topic, reason phrase, comparison fragment, discourse context, or adverb. If the phrase merely fills a grammatical role for a retained VERB or duplicates PLACE/TIME, leave it in the compound/source cue rather than minting LOCATOR.

Split VERB from LOCATOR only when the lexical action remains the same after removing the orientation and the orientation itself is independently selectable. If a particle/complement is inseparable from lexical verb identity, keep it with VERB and do not duplicate it.

Use the smallest complete meaningful locating construction, not an isolated preposition.

## 8. Class-precedence audit before overlap

For every candidate span, first choose the class that carries its primary represented research job. Only then ask whether another class also has an independently selectable job.

Precedence:
- setting/scene identity -> PLACE;
- episode/frame identity -> TIME;
- actor identity -> PERSON;
- thing/relation-as-thing identity -> OBJECT;
- value/state/characterization -> LABEL;
- lexical action/relation -> VERB;
- orientation/path/context -> LOCATOR.

Cross-class overlap is conservative. Keep two projections only when each would remain independently meaningful if the other disappeared. Technical defensibility or grammatical ambiguity is insufficient.

## 9. Literal preservation lock

Every non-null `source_wording`, `source_cue`, non-null `order_cue`, and source-derived short tag must preserve source language character-for-character where the schema requires source text.

Copy source spans directly from the supplied text; do not reconstruct them from memory. Never substitute synonyms, grammatical repairs, dialect normalization, spelling cleanup, number changes, expanded contractions, apostrophe/quotation normalization, inferred terminology, or semantically convenient replacements.

Preserve questions, negation, uncertainty, correction, comparison, attribution, intention, recurrence, reported posture, prospective posture, figurative wording, punctuation, and dialect in source evidence and compounds even when a smaller primitive atom omits syntactic packaging.

Only genuinely unnamed PLACE/TIME coordinates may use `source_wording: null`, with exact source evidence in `source_cue`.

## 10. Ordering and qualities

Order each class by first source establishment after coreference, with speaker first in PERSON.

`qualities_available` is true only when source-present qualities/descriptions are available for that coordinate. It neither forces nor forbids a separate LABEL.

## 11. Primitive freeze

Before compounds, audit each class against the five gates and freeze the primitive inventory. Remove incidental detail, support grammar, duplicate projections, and candidate spans whose independent researcher job cannot be stated without appealing to their containing sentence.

Do not invent a primitive to make a compound easier. Do not keep a questionable primitive because a later bundle refers to it.

## 12. Proposition-level compound reconstruction

After primitive freeze, re-read the source in order and segment it into local represented propositions/bindings rather than generating compounds primitive-by-primitive.

For each proposition containing one or more retained relation-bearing VERB/LABEL/LOCATOR primitives, create one materially complete compound for the binding. Multiple relation-bearing primitives may share one compound when they jointly express one proposition or inseparable coordinated relation. Split compounds only when the source presents independently selectable bindings.

Each compound must contain:
- all retained relation-bearing primitives belonging to that binding;
- every frozen participant/object/value co-bound in that proposition;
- the applicable PLACE/TIME anchors when they materially locate that proposition;
- preserved question/uncertainty/negation posture through the schema's quality/posture representation;
- no coordinate belonging only to a neighboring proposition or broader scene.

Do not create one compound per primitive by default. Do not create pairwise subsets, nested partials, alternate decompositions, duplicate bundles, or scene-wide supersets. Do not omit a frozen co-bound coordinate merely because its relation is inferable.

A primitive may remain unbundled only when the source supplies no local binding to another retained coordinate.

## 13. Final audits

**Scene audit:** identify actual represented episodes/co-presence scenes first; recover materially distinct named/unnamed PLACE anchors; remove merely spatial context labels and local orientation details.

**Frame audit:** identify scene-level TIME anchors; prefer episode frames over temporal tokens; remove duplicate lexical subframes that do not organize distinct represented material.

**Material-contribution audit:** for every primitive ask what research distinction disappears if it is removed. Remove narrative texture, incidental props, weak modifiers, support grammar, and discourse-management items whose removal leaves the represented map unchanged.

**Type audit:** resolve each primitive by represented class job before overlap.

**OBJECT audit:** keep independently selectable things participating in the map; remove incidental scene dressing and proposition/event restatements.

**LABEL audit:** keep materially research-selectable characterization values; remove descriptive census items.

**VERB audit:** keep independent lexical relations; strip syntactic negation/support packaging unless lexicalized; remove metatelling and embedded-predicate inflation.

**LOCATOR audit:** keep independent orientation/context relations; remove grammatical context, temporal duplicates, source/topic/instrument/reason phrases without separate orientation work.

**Literal audit:** compare every source-derived string character-for-character against the source and repair any reconstruction or punctuation normalization.

**Compound audit:** segment by local proposition; include all and only co-bound frozen coordinates; no unmatched refs, primitive-wise duplicate subsets, alternates, or scene-wide inflation.

Then verify source order, qualities flags, candidate-only status, and holdout isolation.

## 14. Calibration isolation and holdout boundary

Return only JSON required by the request schema. Never infer expected counts, reconstruct hidden archetypes, or ask for evaluator feedback.

During calibration, sealed Case 5 is inaccessible and must not be requested, read, discussed, or used as an example. Holdout execution is an external apparatus responsibility and may occur only after repeated Case 2 and Case 6 passes under this exact finalized contract and one bounded calibrated lineage.

If that lineage later passes the one-shot sealed holdout, retire it before creating a brand-new saved agent from finalized V72 instructions only for clean-room verification.

## 15. Candidate-only boundary

All output is candidate/calibration material. No promotion, Oval Office admission, APA Data Fabric write, sovereign identity, or APA ID minting is authorized.
