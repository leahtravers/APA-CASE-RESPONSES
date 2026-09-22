"""V149A harness-only operation rule.

RI-CONTRACT-V149 is the sole durable semantic authority. This rule changes only the
whole-source request topology needed to execute that contract coherently. It contains
no gold answers, counts, evaluator findings, scored outputs, case-specific corrections,
or holdout material.
"""

V149A_INTEGRATED_RULE = """V149A RUNTIME TOPOLOGY — DURABLE CONTRACT CONTROLS.
Perform one whole-source semantic pass under the durable contract before returning anything.

Follow the durable contract's exact order: map represented frames/transitions; positively capture candidates separately for PLACE, TIME, PERSON, OBJECT, LABEL, VERB, and LOCATOR by represented source function; apply the class-local inventory-coordinate admission test; reconcile the smallest COMPLETE source-native atom; perform structural PLACE/TIME recall; perform PERSON/OBJECT recall and same-class identity/coreference; freeze primitives; then replay minimal source-presented compounds from those frozen primitives.

CLASS FUNCTION IS NECESSARY BUT NOT SUFFICIENT. A retained primitive must also be source-staged as a distinct coordinate at that class's own inventory grain. This is class-local. Do not require global importance, repeated use, independent cross-context reuse, or a scaffold-level research distinction. Low-salience, one-use, unnamed, local, deictic, reported, remembered, intended, prospective, questioned, recurrent, figurative, or present-telling material remains eligible when source-staged distinctly.

COMPLETE-ATOM GRAIN: for LABEL, VERB, and LOCATOR, return the smallest exact contiguous source-native span that is COMPLETE for one retained characterization/relation/orientation identity. Smallest complete does not mean shortest fragment. Keep predicate/complement, particle, polarity, modality, degree, aspect, path, or orientation wording when needed for that source unit's identity. Do not return dependent intensifiers, bare support/copular/auxiliary/control fragments, bare particles/prepositions, isolated deictics, or shortened sub-fragments as standalone primitives when their identity belongs to a larger complete source-native atom. Split only genuinely independent coordinated or serial moves.

STRUCTURAL RECALL: PLACE and TIME are semantic coordinates, not vocabulary buckets. A distinct source-staged scene, participant position, phase, episode, recurrence, remembered frame, intended period, later-explanation frame, or present-telling frame may establish an unnamed coordinate when it has reconstructive identity even without an explicit location/time noun. Do not create PLACE/TIME for every predicate merely because every event occurs somewhere/sometime.

OBJECT requires source-treated referential identity. Exclude analyst proposition shells, discourse packaging, generic content handles, or anaphoric wrappers whose entire identity resolves to an already represented relation/binding unless the source separately treats them as stable things.

EXACT SOURCE LOCK: every non-null source-derived string must be exact contiguous source text. Never add, repair, normalize, synonymize, lemmatize, or concatenate source wording. If a prior attempt is rejected because a proposed string is not exact source text, correct it by choosing an exact contiguous source span or an allowed unnamed PLACE/TIME representation; never invent a near-source replacement.

TYPE BY REPRESENTED FUNCTION, not part of speech or vocabulary shape. Same-span cross-class multiplicity is permitted only when the same complete source span genuinely performs distinct retained functions.

Return all seven primitive classes and compounds together in the single JSON object required by response_schema. For compound members, refer only to canonical_key values returned in the named primitive class. Do not use apparatus IDs because code assigns them after validation. Compounds reuse frozen primitives only and never create, repair, merge, split, or retype them.

Do not output internal candidate lists, frame maps, reasoning, archetype guesses, expected counts, evaluator material, scored prior outputs, case-specific hidden corrections, canonical gold extracts, or sealed-holdout material. Return only the JSON object required by response_schema."""
