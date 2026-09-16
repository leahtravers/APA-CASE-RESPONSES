# APA Researcher Inventory Agent Contract V51

Status: ACTIVE SUCCESSOR FOR CALIBRATION
Contract version: `RI-CONTRACT-V51`
Predecessor: `RI-CONTRACT-V50`

## Mission

Produce only a literal lightweight Researcher Inventory candidate from the supplied source. Inventory source-presented research roles and their lightweight compounds. Do not interpret psychological meaning, score APA, infer protected threads, draw conclusions, promote records, mint APA IDs, or admit anything to sovereign/production fabric.

The worker never receives approved archetypes, gold outputs, expected answers, expected counts, evaluator findings, prior scored outputs, sealed holdout source during calibration, or holdout outputs.

## 1. Role-bearing proposition map

Read the entire source first. Silently map the materially distinct source-presented propositions, events, states, comparisons, questions, corrections, reports, intentions, orientations, and scene/episode frames at lightweight research grain.

The map is a navigation device only. It is not an entitlement list and does not tell you how many rows or compounds to return.

A proposition is retained when the source presents a materially distinct relation/state/orientation that a researcher could reconnect from lightweight coordinates. Do not create a proposition merely because a clause, noun phrase, verb, adjective, prepositional phrase, or discourse fragment is grammatically separable.

## 2. Unit admission: necessary role in a retained proposition

Admit a unit only when all of the following are true:

1. the source establishes it explicitly, or it is a permitted source-supported unnamed PLACE/TIME frame;
2. it fills a necessary class-native role in at least one retained proposition;
3. it is expressed at the smallest complete source-native grain that preserves that role; and
4. it is not support grammar, an incidental modifier/background mention, a discourse wrapper, a same-role restatement, a true alias/coreference duplicate, or an alternate grain of the same role.

The available role families are:

- PERSON — participant/social actor;
- OBJECT — referent/content/thing under relation;
- LABEL — characterization/state/polarity/comparison value;
- VERB — operative lexical relation carrier;
- LOCATOR — represented orientation relation;
- PLACE — scene/occurrence-position frame;
- TIME — episode/period frame.

Local, nested, one-use, remembered, reported, questioned, negated, hypothetical, prospective, relational, figurative, and embedded roles may qualify. Global narrative importance is not required. Lexical separability alone never qualifies a unit.

## 3. Role collision and class choice

Choose class from the role the source span performs inside the retained proposition, not from surface part of speech.

A verbal, adverbial, locative, interrogative, comparative, or polarity-shaped span may be LABEL when it functions as the proposition's bound state/value. A noun phrase may be OBJECT only when it functions as a referent/content role, not merely because it is a noun. A verb-looking span belongs in VERB only when it is the operative relation carrier rather than support, report scaffolding, or a state value already captured as LABEL.

Cross-class reuse is allowed only when the same source span independently fills two genuinely different necessary roles in retained propositions. Never duplicate a span across classes merely for coverage.

## 4. PLACE — proposition scene/position frame

Retain a PLACE when a retained proposition requires a materially distinct physical scene or occurrence position to situate represented material.

A PLACE may be explicit or supported unnamed. Supported unnamed PLACE is permitted when the source clearly establishes a distinct situated scene without naming the location. This can include a current/telling scene, waiting position, remembered interaction scene, another participant's scene, departure/arrival scene, object-location scene, or other physically situated frame when that frame is required to distinguish the proposition.

Do not create PLACE from every locality noun, destination, surface, container, body part, direction, movement endpoint, imagined endpoint, recurring activity phrase, or concrete setting word. A named location is not automatically a PLACE row if it does not carry a distinct proposition-frame role.

Broad and contained places may coexist only when different retained propositions or different necessary frame roles require both.

For supported unnamed PLACE, `source_wording` may be null and `source_cue` must be exact source text.

## 5. TIME — proposition episode/period frame

Retain a TIME when a retained proposition requires a materially distinct episode, phase, period, recurrence frame, remembered period, report/telling period, life-event period, wait, attempt period, present reflection, hypothetical/prospective frame, or future frame.

Several actions, clauses, or temporal cues may belong to one TIME when they participate in the same episode. Conversely, a later or earlier proposition may require its own TIME even without an explicit clock/date phrase.

Do not create TIME merely from every action, subordinate clause, duration, frequency word, deictic, transition cue, aspect marker, recurrence word, question, or descriptive phrase. A source phrase is TIME only when it establishes a necessary episode/period frame for a retained proposition.

For supported unnamed TIME, `source_wording` may be null and `source_cue` must be exact source text.

## 6. PERSON

Retain the speaker and each distinct represented human/social actor or stable group that fills a participant role in a retained proposition. Include local, one-use, remembered, reported, possessive/relational, prospective, and represented addressee roles when applicable.

Resolve aliases, titles, kinship terms, pronouns, and coreference before deduplication. The speaker canonical key is `B`.

Do not create PERSON from generic second-person grammar, generic people/classes not represented as participants, or pronoun duplicates after coreference.

## 7. OBJECT — proposition referent/content role

Retain an OBJECT when a concrete or abstract source-treated item fills a necessary referent/content/thing role in a retained proposition. Eligible roles include physical things, represented content, choices, decisions, values, relations, sets/categories, amounts, services/results, internal/figurative objects, comparison referents, and source-distinguished wholes or parts.

Concrete nouns are not automatically entitled. A background setting prop, incidental possessed object, discourse filler, generic noun, proposition wrapper, deictic duplicate, ordinary grammatical complement, or nominalized whole clause is excluded unless the source treats it as an independent referent participating in a retained proposition.

A local or nested referent may qualify when it fills its own relation role.

## 8. LABEL — bound characterization/state/value

Retain the smallest complete source-presented value that a retained proposition binds to a participant, referent, relation, or situation. Eligible values include classification, state, manner-state, comparison, identity/self-label, evaluation, questioned label, correction, acceptance/rejection, polarity response, contrast, relational status, or descriptive attribution.

LABEL is functional rather than part-of-speech based. A phrase that looks verbal, adverbial, locative, interrogative, or polarity-shaped may be LABEL when the source uses it as the proposition's state/value.

Do not retain every adjective, adverb, intensifier, manner fragment, descriptive modifier, discourse marker, or predicate complement. Incidental description is excluded when it does not fill an independently necessary state/value role in a retained proposition.

Preserve question, uncertainty, negation, comparison, correction, colloquial wording, and intensity exactly.

## 9. VERB — operative relation carrier

Retain the source-native lexical carrier of each materially distinct operative relation needed by a retained proposition.

Use the smallest complete relation span that preserves the relation as represented. Keep particles, reflexives, idiomatic material, copular/locative material, modality, aspect, or required complements when removing them would change or destroy relation identity. Split coordinated, matrix/embedded, or serial relations only when they carry different retained propositions or different necessary relation roles.

Do not inventory every lexical verb. Exclude pure auxiliaries, support predicates, reporting/meta scaffolding, speech fillers, cognition wrappers, discourse-management verbs, and repeated same-relation mentions when their only function is to host or comment on another retained relation. A predicate-shaped state/value belongs in LABEL rather than VERB when state/value is its proposition role.

Retain relations under negation, uncertainty, questions, intentions, hypotheticals, reports, recurrence, and future language without asserting occurrence.

## 10. LOCATOR — necessary orientation role

Retain the smallest complete source-presented orientation relation required by a retained proposition. Orientation can include position, path, direction, origin/destination, entry/exit, proximity, containment, accompaniment/carrying, movement, recurrence orientation, situational context, internal orientation, or figurative/relational orientation.

A LOCATOR may be multiword when the complete orientation relation requires the phrase. Do not reduce it to a bare preposition or inflate it to an entire proposition.

Do not inventory every prepositional phrase, topic/recipient marker, possession phrase, comparison support, destination word, movement phrase, or internal-discourse phrase. The orientation must fill a necessary role in a retained proposition.

## 11. Literal lock and lexical preservation

Every non-null `source_wording`, every `source_cue`, and every non-null `order_cue` must be a character-for-character contiguous source substring.

Preserve source spelling, punctuation, dialect, question, negation, uncertainty, correction, comparison, attribution, intention, hypothetical, recurrence, report, and prospective posture.

For explicitly worded coordinates, `researcher_short_tag` may use only words present in `source_wording` or `source_cue`. Supported unnamed PLACE/TIME may use a neutral navigation tag grounded by an exact source cue.

Never substitute a synonym or normalize dialect.

## 12. Ordering and qualities_available

Order units by first source establishment of the retained role after coreference, subject to apparatus speaker-first PERSON and broad-before-contained PLACE/LOCATOR ordering only when genuinely established together.

`qualities_available` is a boolean only. It is true only when qualities/descriptions are available for the coordinate or compound. Question, negation, uncertainty, intensity, or presence of a LABEL does not automatically make it true.

## 13. Three unit passes

Before returning a class, perform:

1. **Role omission pass:** inspect every retained proposition for a necessary role of the requested class that has not yet been represented, including local, nested, one-use, implicit-frame, remembered, reported, questioned, relational, or prospective roles.
2. **Role necessity pass:** for every proposed unit, identify the retained proposition and class-native role that requires it. If no proposition needs it, remove it.
3. **Excess/collision pass:** remove lexical-census rows, support/meta predicates, incidental modifiers/background nouns, proposition wrappers, physical-noun PLACE inflation, temporal-cue TIME inflation, every-PP LOCATOR behavior, unjustified cross-class overlap, parent/child alternate grains, and same-role restatements.

Target complete lightweight role resolution: neither compressed summary nor exhaustive lexical decomposition.

## 14. Compounds — one complete lightweight proposition each

Freeze the unit layer first. A compound cannot create, repair, suppress, or retype a unit.

For every retained role-bearing proposition that can be expressed from frozen unit refs, emit exactly one smallest **complete** compound for that proposition.

A complete compound includes every frozen role required to reconstruct the source-presented proposition at lightweight research grain:

- operative relation and/or bound characterization/orientation;
- actual participants;
- necessary referents/content;
- tightly bound co-predicates or state values when they jointly constitute the same proposition;
- PLACE/TIME/LOCATOR anchors when that proposition uses them to situate or orient the relation.

Do not prefer a smaller subset if dropping a retained role makes the proposition incomplete. Do not also emit the subset, alternate decomposition, nested variant, or sentence-wide superset. Distinct carrier/reporting and embedded/content propositions may both survive only when they are genuinely different retained propositions.

Do not emit every pair, combinatorial closure, every sentence, broad co-occurrence bags, or compounds whose apparent completeness depends on redundant/unmatched units.

Compound `qualities_available` follows the same rule as units; it is not a question marker.

## 15. Calibration isolation

Return only the JSON required by the request schema.

Never infer or reconstruct archetypes, expected counts, evaluator preferences, prior scored answers, case-specific gold corrections, sealed holdout source during calibration, or holdout output. Do not optimize toward an imagined hidden answer.

## 16. Prohibited work

Never perform APA scoring, psychological interpretation, protected-thread analysis, conclusions, promotion, APA-ID creation, Oval Office research writing, sovereign admission, or database/fabric admission.

## 17. Successor effect

V51 prospectively supersedes V50 for new calibration and certification runs. V50 and every prior contract/run remain preserved as historical training evidence.

Immutable archetype hashes, exact-source literal lock, deterministic apparatus validation, hidden evaluation, worker/gold isolation, candidate-only status, historical preservation, sealed holdout isolation, repeated-archetype gate, one-shot calibrated-lineage holdout semantics, clean-room fresh-agent certification, and all promotion/APA-ID/database prohibitions remain unchanged.
