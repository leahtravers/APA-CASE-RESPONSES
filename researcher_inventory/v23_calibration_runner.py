#!/usr/bin/env python3
"""V23 calibration entry point.

V23 changes worker-visible durable/task rules only. Hidden evaluation remains the
V20 evaluator-alignment layer unchanged: immutable gold rows and pass criteria are
not modified. This keeps worker-behavior correction separate from harness repair.
"""
from __future__ import annotations

from researcher_inventory import v20_calibration_runner as v20
from researcher_inventory import inventory_apparatus as apparatus
from researcher_inventory.v23_task_rules import V23_BASE_RULES, V23_CLASS_RULES

# Override only neutral worker-visible task rules. V20 retains the admitted
# evaluator-only alignment normalization; archetype gold and pass criteria remain
# unchanged and are never supplied to the worker.
apparatus.BASE_RULES = V23_BASE_RULES
apparatus.CLASS_RULES = V23_CLASS_RULES

base = v20.base


if __name__ == "__main__":
    base.main()
