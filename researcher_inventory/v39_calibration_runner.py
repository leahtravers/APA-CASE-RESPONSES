#!/usr/bin/env python3
"""V39 calibration entry point.

V39 restores class-native positive admission after V38 under-resolution while
retaining explicit anti-census exclusions, immutable archetype gates, evaluator
isolation, candidate-only boundaries, and one-shot holdout protections.
"""
from researcher_inventory import v34_calibration_runner as v34
from researcher_inventory import inventory_apparatus as apparatus
from researcher_inventory.v39_task_rules import V39_BASE_RULES, V39_CLASS_RULES

apparatus.BASE_RULES = V39_BASE_RULES
apparatus.CLASS_RULES = V39_CLASS_RULES

if __name__ == "__main__":
    v34.base.main()
