#!/usr/bin/env python3
"""V60 calibration entry point using the preserved hidden evaluator and role-ledger task rules."""
from researcher_inventory import v52_calibration_runner as v52
from researcher_inventory import inventory_apparatus as apparatus
from researcher_inventory.v60_task_rules import V60_BASE_RULES, V60_CLASS_RULES

apparatus.BASE_RULES = V60_BASE_RULES
apparatus.CLASS_RULES = V60_CLASS_RULES

if __name__ == "__main__":
    v52.v34.base.main()
