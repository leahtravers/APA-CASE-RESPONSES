#!/usr/bin/env python3
"""V40 calibration entry point.

V40 uses source-binding skeleton reconstruction plus binding-role admission to
avoid both V38 under-resolution and V39 class-native near-census atomization.
Immutable archetype gates, evaluator isolation, candidate-only boundaries, and
one-shot holdout protections remain unchanged.
"""
from researcher_inventory import v34_calibration_runner as v34
from researcher_inventory import inventory_apparatus as apparatus
from researcher_inventory.v40_task_rules import V40_BASE_RULES, V40_CLASS_RULES

apparatus.BASE_RULES = V40_BASE_RULES
apparatus.CLASS_RULES = V40_CLASS_RULES

if __name__ == "__main__":
    v34.base.main()
