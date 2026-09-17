#!/usr/bin/env python3
"""V66 calibration entry point.

V66 restores bounded primitive admission while preserving independent class-specific
projection only when each projection independently satisfies its class job. The
V64 evaluator-only compound-order correction and all hidden-evaluator isolation
remain unchanged.
"""
from researcher_inventory import v64_compound_order_calibration_runner as v64o
from researcher_inventory import inventory_apparatus as apparatus
from researcher_inventory.v66_task_rules import V66_BASE_RULES, V66_CLASS_RULES

apparatus.BASE_RULES = V66_BASE_RULES
apparatus.CLASS_RULES = V66_CLASS_RULES

base = v64o.base

if __name__ == "__main__":
    base.main()
