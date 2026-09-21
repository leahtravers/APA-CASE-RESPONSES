"""V147A harness-only operation rule.

RI-CONTRACT-V147 is the sole durable semantic authority. This rule changes only the
whole-source request topology needed to execute that contract coherently. It contains
no gold answers, counts, evaluator findings, scored outputs, case-specific corrections,
or holdout material.
"""

V147A_INTEGRATED_RULE = """V147A RUNTIME TOPOLOGY — DURABLE CONTRACT CONTROLS.
Perform one whole-source semantic pass under the durable contract before returning anything. Follow the contract's exact order: resolve represented frames; build the structural PERSON/OBJECT/PLACE/TIME scaffold; build only the scaffold-bounded inventory-bearing relation ledger; derive bounded VERB/LABEL/LOCATOR slots; run structural recall and the relation ceiling; reconcile identity; freeze primitives; then replay only contract-admitted compounds from that same bounded ledger.

Return all seven primitive classes and compounds together in the single JSON object required by response_schema. This request topology preserves one coherent semantic backbone across classes. It does not add, broaden, weaken, reinterpret, or replace any durable admission, typing, lexical-grain, support, compound, isolation, or candidate-boundary rule.

PLACE and TIME are semantic coordinates, not lexical phrase buckets. Relations do not automatically manufacture structural coordinates. Conversely, source-staged unnamed PLACE/TIME coordinates may be returned with null source_wording when the durable contract requires them.

For compound members, refer only to canonical_key values that you returned in the named primitive class. Do not use apparatus IDs because code assigns them after validation. Do not create a primitive solely to support a compound, and do not create a compound to repair a missing primitive.

Do not output the internal frame map, scaffold, relation ledger, reasoning, archetype guesses, expected counts, evaluator material, scored prior outputs, case-specific hidden corrections, or sealed-holdout material. Return only the JSON object required by response_schema."""
