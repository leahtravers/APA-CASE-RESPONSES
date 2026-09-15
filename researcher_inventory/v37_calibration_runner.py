#!/usr/bin/env python3
"""V37 calibration entry point.

V37 uses source-binding backchaining and atomic class-native grain after V36
under-admission/over-fusion, while retaining immutable archetype gates, evaluator
isolation, candidate-only boundaries, and one-shot holdout protections.
"""
from researcher_inventory import v34_calibration_runner as v34
from researcher_inventory import inventory_apparatus as apparatus
from researcher_inventory.v37_task_rules import V37_BASE_RULES, V37_CLASS_RULES

apparatus.BASE_RULES = V37_BASE_RULES
apparatus.CLASS_RULES = V37_CLASS_RULES

if __name__ == "__main__":
    v34.base.main()
