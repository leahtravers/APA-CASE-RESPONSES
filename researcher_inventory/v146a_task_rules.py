"""V146A harness-only operation rule.

RI-CONTRACT-V146 remains the sole durable semantic authority. This rule changes only
request topology so the worker can execute V146's mandated whole-source relation-first
construction in one semantic turn. It contains no gold answers, counts, evaluator
findings, scored outputs, case-specific corrections, or holdout material.
"""

V146A_INTEGRATED_RULE = """V146A RUNTIME TOPOLOGY — DURABLE CONTRACT CONTROLS.
Perform one whole-source semantic pass under the durable contract's mandatory construction order before returning anything: resolve represented frames; form one source-native relation ledger; derive all seven primitive classes from that same ledger; reconcile identity/coreference; freeze the complete primitive inventory; then replay only the contract-admitted compounds from that same ledger.

Return all seven primitive classes and the compounds together in the single JSON object required by response_schema. The request topology exists only to preserve one coherent V146 semantic backbone across classes. It does not add, broaden, weaken, reinterpret, or replace any durable admission, typing, lexical-grain, support, compound, isolation, or candidate-boundary rule.

For compound members, refer only to canonical_key values that you returned in the named primitive class. Do not use apparatus IDs because code assigns them after validation. Do not create a primitive solely to support a compound, and do not create a compound to repair a missing primitive.

Do not output the internal relation ledger, reasoning, archetype guesses, expected counts, evaluator material, scored prior outputs, case-specific hidden corrections, or sealed-holdout material. Return only the JSON object required by response_schema."""
