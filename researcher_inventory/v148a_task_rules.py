"""V148A harness-only operation rule.

RI-CONTRACT-V148 is the sole durable semantic authority. This rule changes only the
whole-source request topology needed to execute that contract coherently. It contains
no gold answers, counts, evaluator findings, scored outputs, case-specific corrections,
or holdout material.
"""

V148A_INTEGRATED_RULE = """V148A RUNTIME TOPOLOGY — DURABLE CONTRACT CONTROLS.
Perform one whole-source semantic pass under the durable contract before returning anything.

Follow the durable contract's exact order: read the complete source; positively capture candidates separately for PLACE, TIME, PERSON, OBJECT, LABEL, VERB, and LOCATOR by represented source function; apply only the contract's class-local exclusions; reconcile lexical grain; perform structural-coordinate recall; merge only true same-class identity/coreference; freeze primitives; then replay minimal source-presented compounds from those frozen primitives.

PRIMITIVE COMPLETENESS IS CLASS-LOCAL. Do not require a valid primitive to prove independent global importance, cross-context reuse, or a separate scaffold-level research distinction. Low-salience, one-use, relation-bound, deictic, unnamed, generic, reported, remembered, prospective, questioned, recurrent, figurative, or present-telling material remains eligible when it genuinely performs the named primitive class function.

ANTI-CENSUS CONTROL IS ALSO CLASS-LOCAL. Exclude unsupported inference/paraphrase, true same-class aliases/coreference, grammar-only material with no represented class function, analyst-created proposition shells, alternate parses without a distinct source function, same-grain duplicates, and fused spans whose valid class functions are carried by smaller separable source-native atoms.

LEXICAL GRAIN: for LABEL, VERB, and LOCATOR use the smallest exact contiguous source-native span that performs one class function. Do not fuse neighboring actions, states, characterizations, arguments, sites, times, or orientations merely because they share one sentence or event. Preserve modal/negative/aspect/particle material only when removing it changes represented identity or posture. Reporting/cognitive/support/copular wording is not automatically excluded when it itself performs a represented class function.

PLACE and TIME are semantic coordinates, not vocabulary buckets. PLACE requires a represented where-coordinate. TIME requires a represented when/period/frame coordinate and is not created merely because an action or interaction forms an event episode. Genuinely unnamed PLACE/TIME may use null source_wording only as allowed by the durable contract.

OBJECT requires source-treated referential standing, but one-use, abstract, deictic, choice-like, relational, or internal referents remain eligible when the source itself treats them as things. Do not invent proposition/content objects from analyst paraphrase.

LOCATOR is orientation/context by represented function and may be verb-like on the surface. Same-span cross-class multiplicity is permitted only when the span genuinely performs distinct retained functions.

Return all seven primitive classes and compounds together in the single JSON object required by response_schema. For compound members, refer only to canonical_key values returned in the named primitive class. Do not use apparatus IDs because code assigns them after validation. Compounds reuse frozen primitives only and never create, repair, merge, or retype them.

Do not output internal candidate lists, frame maps, reasoning, archetype guesses, expected counts, evaluator material, scored prior outputs, case-specific hidden corrections, or sealed-holdout material. Return only the JSON object required by response_schema."""
