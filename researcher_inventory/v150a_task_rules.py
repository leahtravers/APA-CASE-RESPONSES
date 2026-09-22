"""V150A harness-only operation rule.

RI-CONTRACT-V150 is the sole durable semantic authority. This rule changes only the
whole-source request topology needed to execute that contract coherently. It contains
no gold answers, counts, evaluator findings, scored outputs, case-specific corrections,
or holdout material.
"""

V150A_INTEGRATED_RULE = """V150A RUNTIME TOPOLOGY — DURABLE CONTRACT CONTROLS.
Perform one whole-source semantic pass under the durable contract before returning anything.

Follow the durable contract's exact order: map represented scenes/frames/actors/referents/transitions; positively capture candidates separately for PLACE, TIME, PERSON, OBJECT, LABEL, VERB, and LOCATOR; determine each occurrence's primary represented role; apply the promoted-coordinate test and class-local nonredundancy test; reconcile the smallest COMPLETE exact source-native atom; perform structural PLACE/TIME recall; perform PERSON/OBJECT recall and class arbitration; audit descriptive qualities separately from LABEL promotion; freeze primitives; then replay minimal source-presented compounds from those frozen primitives.

CLASS FUNCTION IS NECESSARY BUT NOT SUFFICIENT. Do not retain material merely because it can be semantically interpreted or tracked. A retained primitive must be source-promoted as a distinct coordinate at that class's own grain and must make a nonredundant LOCAL reconstructive contribution. Ask whether removing it while retaining all other primitives, qualities, exact source cues, and minimal bindings would erase a distinct source-presented where/when/actor/referent/characterization/relation/orientation coordinate. If not, treat it as evidence, quality, cue, argument, support, wording, or context rather than a primitive. This test is class-local and never requires global importance, recurrence, independent reuse, or scaffold-level salience.

PRIMARY ROLE FIRST. Type by what the source is doing with the occurrence, not by part of speech or every class-compatible interpretation. Cross-class duplication is exceptional and requires the source to separately stage both functions as distinct coordinates. Semantic ambiguity alone does not justify twins.

QUALITY CHANNEL. Descriptive wording can support qualities_available=true without becoming a LABEL. Promote a LABEL only when the characterization itself is source-staged as a distinct represented state/evaluation/classification/comparison. Do not create a characterization census from incidental adjectives, naming modifiers, texture, degree words, or ordinary descriptive predicates.

PLACE/TIME ARE STRUCTURAL COORDINATES. Preserve unnamed source-staged settings, positions, phases, recurrence frames, intended periods, remembered/reported periods, and present-telling frames when they organize reconstruction. Do not turn every spatial noun/surface/container into PLACE or every temporal word/event occurrence into TIME. Incidental spatial/temporal wording may be only evidence for another coordinate.

OBJECT requires source-promoted referential standing, not nounhood. Exclude proposition shells, discourse packaging, incidental nominal texture, and expressions whose primary role is another class.

VERB requires a promoted relation/action/state, not every predicate. LOCATOR requires a promoted orientation/context relation, not every preposition, spatial phrase, temporal cue, manner phrase, or figurative expression. Exclude support/discourse wording and fragments whose entire contribution is already preserved elsewhere.

COMPLETE-ATOM GRAIN: for LABEL, VERB, and LOCATOR, return the smallest exact contiguous source-native span that is COMPLETE for one promoted characterization/relation/orientation identity. Keep predicate/complement, particle, polarity, modality, degree, aspect, comparison, path, or orientation wording when required for identity. Do not return dependent intensifiers, bare support/copular/auxiliary/control fragments, bare particles/prepositions, isolated deictics, naming modifiers, or shortened sub-fragments as standalone primitives when their identity belongs elsewhere. Split coordinated/serial moves only when each independently passes promotion and local nonredundancy.

EXACT SOURCE LOCK: every non-null source-derived string must be exact contiguous source text. Never add, repair, normalize, synonymize, lemmatize, or concatenate source wording. If a proposed string is rejected as non-source text, correct it only by choosing an exact contiguous source span or an allowed unnamed PLACE/TIME representation.

Return all seven primitive classes and compounds together in the single JSON object required by response_schema. For compound members, refer only to canonical_key values returned in the named primitive class. Compounds reuse frozen primitives only and never create, repair, merge, split, or retype them. A clause does not automatically require a compound.

Do not output internal candidate lists, frame maps, reasoning, archetype guesses, expected counts, evaluator material, scored prior outputs, case-specific hidden corrections, canonical gold extracts, or sealed-holdout material. Return only the JSON object required by response_schema."""
