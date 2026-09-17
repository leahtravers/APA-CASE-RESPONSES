#!/usr/bin/env python3
"""V65 calibration entry point.

V65 changes worker semantics prospectively from V64 by restoring independent
class-specific projections while retaining the V64 evaluator-only compound-order
correction and all hidden-evaluator isolation.
"""
from researcher_inventory import v64_compound_order_calibration_runner as v64o
from researcher_inventory import inventory_apparatus as apparatus
from researcher_inventory.v65_task_rules import V65_BASE_RULES, V65_CLASS_RULES

apparatus.BASE_RULES = V65_BASE_RULES
apparatus.CLASS_RULES = V65_CLASS_RULES

base = v64o.base

if __name__ == "__main__":
    base.main()
