# Researcher Inventory Training History Contract

Every training attempt is retained, including failures.

## Purpose

The researcher-inventory agent is expected to improve through iterative contract revisions. Early failures are research material and must not be discarded.

## Database destination

Training history lives only in `apa_cases_candidate`:

- `research_inventory_training_run`
- `research_inventory_training_finding`
- `research_inventory_contract_revision`

These records are candidate/training records only. They do not receive APA IDs and do not imply promotion.

## Run recording

For every test attempt, record:

- training run reference
- contract version
- source case reference/text
- researcher interest, if any
- model
- session
- attempt number
- status: STARTED / COMPLETED / FAILED / HELD
- raw model output when available
- candidate reference when a candidate inventory was successfully written
- start/finish timestamps
- bounded notes

## Failure recording

Failures should be classified when possible using the database vocabulary:

- SCHEMA_VIOLATION
- SOURCE_FLATTENING
- OVER_NORMALIZATION
- OVER_GRANULARITY
- UNDER_GRANULARITY
- MISSING_UNIT
- EXTRA_UNIT
- BAD_COMPOUND
- BAD_TIME_BINDING
- BAD_PLACE_BINDING
- BAD_PERSON_BINDING
- BAD_OBJECT_BINDING
- BAD_LABEL_BINDING
- BAD_VERB_BINDING
- BAD_LOCATOR_BINDING
- BAD_Q_FLAG
- DATABASE_WRITE_FAILURE
- OTHER

Keep the observed behavior and the expected behavior separate.

## Contract revision linkage

Every meaningful prompt/contract revision should create or update a `research_inventory_contract_revision` row and point back to the training runs/findings it is intended to address.

This provides a durable learning history from early failures through stable behavior.
