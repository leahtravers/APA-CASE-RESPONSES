"""V126A harness-only request rules.

The saved agent's AGENT_CONTRACT_V126 is the sole semantic authority. These strings
only select the requested operation and never add admission, typing, or coverage rules.
No archetype answers, expected counts, evaluator findings, scored outputs, canonical
gold extracts, case-specific corrections/examples, or holdout material appear here.
"""

V126A_BASE_RULES = """RUNTIME OPERATION ENVELOPE — DURABLE CONTRACT CONTROLS.
The saved Researcher Inventory agent's durable contract is the complete and controlling semantic authority for this request.
The task, class, response schema, source, and supplied frozen units only select which contract-defined operation to perform. They do not add, broaden, weaken, reinterpret, or replace any admission, typing, lexical-grain, support, compound, isolation, or candidate-boundary rule in the durable contract.
Read the complete supplied source as required by the durable contract. Preserve exact source wording and return only the JSON value required by response_schema. Do not add unrequested fields.
Never infer permission from this request to expose or reconstruct archetypes, expected counts, evaluator findings, scored prior outputs, case-specific hidden corrections, sealed holdout source, or holdout output. Never perform APA scoring, psychological interpretation, promotion, sovereign/admitted writing, APA-ID creation, or APA database mutation.
"""

V126A_CLASS_RULES = {
    "PLACE": "Operation selector only: apply the durable contract's PLACE rule exactly to this class request; add no independent admission criteria.",
    "TIME": "Operation selector only: apply the durable contract's TIME rule exactly to this class request; add no independent admission criteria.",
    "PERSON": "Operation selector only: apply the durable contract's PERSON rule exactly to this class request; add no independent admission criteria.",
    "OBJECT": "Operation selector only: apply the durable contract's OBJECT rule exactly to this class request; add no independent admission criteria.",
    "LABEL": "Operation selector only: apply the durable contract's LABEL rule exactly to this class request; add no independent admission criteria.",
    "VERB": "Operation selector only: apply the durable contract's VERB rule exactly to this class request; add no independent admission criteria.",
    "LOCATOR": "Operation selector only: apply the durable contract's LOCATOR rule exactly to this class request; add no independent admission criteria.",
}

V126A_COMPOUND_RULE = """Operation selector only: apply the durable contract's compound-construction rule exactly to the frozen supplied primitive units. Use only supplied unit_ref values; Q is not a unit ref and a compound cannot repair a missing primitive. Do not add any independent event/proposition census, closure, bundling, or expansion criterion beyond the durable contract."""
