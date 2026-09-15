#!/usr/bin/env python3
"""V38 calibration entry point.

V38 applies admission-before-atomization and a structural-sufficiency deletion
test after repeated V37 over-admission, while retaining immutable archetype gates,
evaluator isolation, candidate-only boundaries, and one-shot holdout protections.
"""
from researcher_inventory import v34_calibration_runner as v34
from researcher_inventory import inventory_apparatus as apparatus
from researcher_inventory.v38_task_rules import V38_BASE_RULES, V38_CLASS_RULES

apparatus.BASE_RULES = V38_BASE_RULES
apparatus.CLASS_RULES = V38_CLASS_RULES

if __name__ == "__main__":
    v34.base.main()
