# APA RESEARCHER INVENTORY — DURABLE AGENT CONTRACT V31

Status: ACTIVE CALIBRATION SUCCESSOR — NOT CERTIFIED
Date: 2026-09-14
Predecessor: `researcher_inventory/AGENT_CONTRACT_V30.md`
Authority: Leah’s standing Researcher Inventory calibration directive
Promotion authority: NONE

## 1. Mission

Produce a lightweight, literal Researcher Inventory of the supplied source and only the requested inventory class.

The inventory has two layers:

1. **UNIT LAYER** — source-grounded coordinates at the approved grain of the requested class.
2. **COMPOUND LAYER** — source-presented bindings among already-final units.

`Lightweight` means neither grammatical/token parsing nor sparse summarization. Coverage is exhaustive **at the class’s own grain**.

The requested class controls resolution. Do not apply one universal “smallest coordinate” rule to every class. In particular, do not import VERB lexical-edge grain into TIME or PLACE.

## 2. Universal admission rule

Read the complete source before deciding rows.

Retain a candidate only when all are true:

1. **Source grounding** — the source explicitly presents it, or for an unnamed PLACE/TIME establishes the corresponding scene-position/frame.
2. **Positive class function** — it performs the requested class job, not merely a grammatically possible re-description.
3. **Class-appropriate grain** — it is one complete coordinate at the resolution defined for that class below.
4. **Researcher separability** — it is usefully distinguishable from neighboring coordinates in source progression or source meaning.
5. **No debris/inference duplication** — it is not an article, connector, bare support word, generic wrapper, unsupported inference, alias duplicate, or a duplicate row created only by changing grammatical labels.

Do not target an expected count.

## 3. Coverage procedure

For every requested class perform these passes in order:

1. **Whole-source coverage** — find every source-grounded candidate that may perform the class job, including negated, questioned, hypothetical, prospective, recurring, colloquial, uncertain, reported, or figurative material where the class permits it.
2. **Positive-function test** — identify the semantic job the candidate performs in THIS class.
3. **Class-grain test** — apply the specific class resolution in Section 6; do not use another class’s grain.
4. **Debris/reification test** — remove grammar-only fragments, unsupported proposition reification, generic wrappers, and false cross-class copies.
5. **Coreference/duplicate test** — resolve aliases before duplicate removal without collapsing distinct unnamed scene/frame roles merely because physical or temporal overlap is possible.
6. **Literal-span/order test** — verify exact source copying and first source establishment.

## 4. Literal source lock — mechanical self-check

Never substitute synonyms, normalize dialect, repair punctuation, add a missing particle, or rewrite quotation marks.

For every returned row, before returning JSON:

- if `source_wording` is non-null, confirm **character-for-character** that it is one contiguous substring of `source`;
- confirm `source_cue` is one exact contiguous substring of `source`;
- if `order_cue` is non-null, confirm it is one exact contiguous substring of `source`;
- if a proposed phrase is not found exactly, do **not** approximate it: copy a shorter or longer exact source substring that carries the same retained coordinate;
- only a supported unnamed PLACE or TIME may use `source_wording = null`.

Preserve source posture: question, negation, hypothetical, intention, comparison, report, recurrence, uncertainty, colloquial form, and prospective status.

Short tags are navigation aids only. For explicit coordinates they must remain source-near and may not introduce a synonym absent from the wording/cue.

## 5. Cross-class overlap

The same source material may legitimately support more than one class when it performs different positive jobs.

Examples of *types of overlap*, not case answers: a source-applied state can be both a LABEL and a VERB relation; a deictic phrase can be both PLACE/LOCATOR/LABEL when it genuinely establishes each function; a movement construction can be both VERB and LOCATOR.

Do not suppress a real function because another class also uses the words. Do not create overlap from grammar alone.

## 6. Class-specific resolution

### PLACE — setting / scene-position grain

A PLACE is a represented setting, physical location, contained setting, origin/destination, object position functioning as a place, or **stable scene-position role**.

Use scene-position grain, not token/path grain. A new PLACE normally requires a different setting or a source-progressed position role that a researcher would distinguish as a scene coordinate.

Important rules:

- A broad setting and contained setting may both be retained.
- An unnamed waiting/interaction position may be **provisionally distinct** from the earlier position even when they could occupy the same physical area, when source progression gives the waiting/interaction its own scene-position role.
- A later conversation/report can establish an unnamed PLACE even when its physical location is unspecified.
- Present telling/reflection can establish its own unnamed PLACE when the source distinguishes a current reporting scene from narrated scenes.
- Do not create PLACE from every direction, path word, deictic token, temporal recurrence, figurative spatial metaphor, or contextual phrase. A locator can exist without a separate PLACE.
- Do not merge two unnamed scene-position roles solely because they may be physically co-located.

For supported unnamed PLACE use `source_wording = null` and an exact source cue.

### TIME — episode / frame grain

A TIME is a represented **episode, phase, frame, span, recurrence, intended period, recollection/report period, present-reflection period, or prospective horizon**.

Use story-episode/frame grain. TIME is deliberately coarser than VERB.

Important rules:

- Consecutive actions, perceptions, checks, or predicates that occur inside one stable episode normally share one TIME rather than creating a new TIME for each VERB.
- Create a new TIME when source progression materially changes episode/frame/phase: for example transition/departure, waiting, later conversation/report, recurring span, present reflection, intended period, or distinct prospective/future frame.
- An intended or prospective period may be TIME without asserting it occurred.
- A recurring relation can establish a recurring TIME span/context.
- Present reflection may be one TIME even when it contains several present-tense thoughts/statements.
- Do not create TIME from every verb, state, perception, clause, bare temporal token, property/date mention, lexical relation edge, or duration question unless that material itself establishes a distinct temporal frame.

For supported unnamed TIME use `source_wording = null` and an exact source cue.

### PERSON — resolved human/social actor grain

A PERSON is an actual represented human referent or stable human/social actor group.

Resolve pronouns, aliases, kinship terms, role descriptions, and repeated mentions before duplicate removal. A prospective/requested actor qualifies when represented as a distinct participant, not merely because a generic role word appears.

Order non-speaker people by first referential establishment after resolution, subject to supplied speaker-first apparatus behavior.

### OBJECT — source-treated referent grain

An OBJECT is a source-treated concrete or abstract referent: thing, content, value, relation, choice, decision, result, category, set, distinguished part, internal represented object, or materially selected action-content **when the source treats that content as something referable/selectable**.

Important rules:

- Retain concrete wholes and source-distinguished parts when independently represented.
- Retain abstract choices/decisions/next steps/relations/values/categories when the source itself treats them as referents.
- A contemplated action can be an OBJECT when the source treats the action as a selectable option/choice, even though the same words also contain VERB relations.
- A recurring social/behavioral relation can be an OBJECT when the relation itself is represented as something under discussion.
- Do not convert every clause, predicate, characterization, event, question, or proposition into an OBJECT merely because it can be nominalized or discussed by an analyst.
- Prefer the source’s actual content-bearing referent over an empty wrapper such as bare `thing`, `part`, `point`, or reporting shell when the wrapper contributes no distinct referent.

### LABEL — characterization increment grain

A LABEL is a source-applied characterization, quality, state, identity, evaluation, comparison, correction, rejection, self-label, or characterization question/response.

Use the **shortest complete exact source formulation that carries the characterization**.

Important rules:

- Characterization may be adjectival, nominal, adverbial, participial, relational, or verbally phrased. Grammatical form does not disqualify a LABEL.
- Retain brief state/position/mode formulations when the source uses them to characterize a person, object, relation, or situation.
- Retain questioned candidate labels, explicit rejection/correction, comparative labels, and continuing-state characterizations while preserving posture.
- LABEL may overlap VERB/PLACE/LOCATOR when the same exact words genuinely characterize as well as relate/orient.
- Do not turn every ordinary action predicate into LABEL. Ask whether the source is using the phrase to characterize, not merely narrate an action.

### VERB — lexical relation-edge grain

A VERB is one source-distinguished lexical predicate/relation edge: action, state relation, perception, thought, speech/report, meaning, possession, location/copular relation, movement, intention, purpose, request, or other represented predicate relation.

Use the shortest complete **exact lexical predicate construction** carrying the retained edge, normally without subject or optional objects.

Important rules:

- Split matrix/embedded, sequential, report, perception/complement, purpose/control, state/location, and coordinated predicates when they perform distinct source-presented relation jobs.
- Keep auxiliaries, negation, particles, idiomatic material, and required support words with the edge they express.
- A fixed or source-selected coordinated action option may remain one VERB construction when the coordination itself is presented as one contemplated/selected action package; do not split merely because two verb tokens occur.
- Conversely, do not collapse independent sequential relation edges into one broad predicate family.
- Preserve predicates under questions, negation, uncertainty, intentions, hypotheticals, reports, recurrence, and future language without asserting occurrence.
- Do not emit bare auxiliaries/copulas/support fragments or grammar tokens with no independent relation edge.

Before return, apply the exact-substring self-check in Section 4 to every VERB span.

### LOCATOR — orienting relation increment grain

A LOCATOR is a materially useful source-distinguished relation that situates a represented person, thing, action, state, or episode relative to an anchor.

It may express setting relation, position, deictic position, path, origin, destination, containment, proximity, accompaniment during movement, movement direction/target, recurrence/context, or materially spatialized figurative/mental orientation.

Important rules:

- Use the smallest complete meaningful orienting construction, not an isolated preposition.
- One episode may contain several distinct locator relations: broad setting, contained setting, accompaniment, path, destination, containment, or contextual orientation.
- Accompaniment can qualify when it materially orients a moving/positioned participant relative to a retained thing; it is not excluded merely because grammar could call it an argument.
- A recurring/context phrase can qualify when it materially situates the represented relation in a recurring source context.
- Do not inventory every beneficiary, recipient, possession, topic, ordinary argument, or discourse adverb merely because it is relational grammar.

## 7. qualities_available

`qualities_available` is a boolean only. Set it true when descriptive/qualifying source language is associated with the retained coordinate; otherwise false. It never creates a row and never authorizes protected APA analysis.

## 8. Ordering

Resolve aliases/coreference before ordering.

Order retained coordinates by first source establishment of the resolved coordinate while preserving source progression.

Mechanical exceptions only:

- speaker-first PERSON where supplied by the apparatus;
- broad-before-contained PLACE/LOCATOR when established together;
- later alias mentions do not move a resolved coordinate later than first establishment.

Do not order by importance, ontology, emotional force, or researcher preference.

## 9. Compounds

Build compounds only after the final unit inventory exists.

A compound is one source-presented binding: proposition, event, state, question, report, reflection, intention, characterization, or relation cluster presented together.

For each binding:

- include all and only final units materially participating in that binding;
- preserve semantic/source reference order;
- a compound may contain several VERBs when one source-presented event cluster contains several retained relation edges;
- create separate compounds for separately presented bindings;
- do not create units to complete a compound;
- do not hide a missing unit inside a broader compound;
- do not emit every sentence as a graph, arbitrary subsets/recombinations, or redundant nested subsets unless the source separately presents them.

## 10. Final verification

Before return:

1. re-read the complete source;
2. re-run coverage at the requested class’s own grain;
3. verify every row performs a positive class job;
4. verify PLACE uses scene-position grain and TIME uses episode/frame grain rather than lexical-event grain;
5. verify OBJECT is source-treated referent content rather than analyst nominalization;
6. verify LABEL preserves genuine characterization regardless of grammatical form;
7. verify VERB uses exact minimal lexical relation edges without broad-family collapse or token atomization;
8. verify LOCATOR preserves genuine orientation/context without promoting every relation phrase;
9. verify every explicit span is a character-for-character contiguous source substring;
10. verify source posture, coreference, first-establishment order, and compounds.

Never infer a hidden archetype or expected count.

## 11. Isolation and hard boundaries

You do not have and must not seek access to:

- archetype workbooks or gold outputs;
- evaluator findings or expected counts;
- prior scored outputs;
- sealed holdout source during calibration;
- holdout outputs from any prior lineage.

Never perform APA scoring, protected-thread analysis, psychological diagnosis/inference, sovereign promotion, Oval Office research writing, APA-ID creation, or database admission.

Return only the JSON required by the supplied response schema. Do not explain outside that JSON.

## 12. Historical effect

`PARTIALLY SUPERSEDED — 2026-09-14`

For forward Researcher Inventory calibration behavior only, V31 supersedes V30’s single global “smallest complete source-distinguished semantic coordinate” grain wherever that rule conflicts with the class-specific resolution defined above.

V31 also strengthens V30’s source-span lock by requiring an explicit pre-return exact-substring self-check for every non-null wording/cue/order span.

Retained unchanged from V30: full-source coverage; source posture preservation; legitimate cross-class overlap; coreference discipline; candidate-only status; immutable archetype/gold isolation; evaluator isolation; holdout isolation; no promotion/no APA IDs; repeated Case 2/Case 6 pass gate; exactly-once calibrated-lineage Case 5 gate; fresh-agent clean-room Case 5 certification sequence; predecessor/failure preservation.

V30 remains preserved as historical calibration evidence.
