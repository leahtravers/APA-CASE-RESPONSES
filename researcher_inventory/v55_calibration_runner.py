#!/usr/bin/env python3
"""V55 calibration entry point using the preserved hidden evaluator with balanced coordinate-identity rules."""
from researcher_inventory import v52_calibration_runner as v52
from researcher_inventory import inventory_apparatus as apparatus
from researcher_inventory.v55_task_rules import V55_BASE_RULES, V55_CLASS_RULES

apparatus.BASE_RULES = V55_BASE_RULES
apparatus.CLASS_RULES = V55_CLASS_RULES

if __name__ == "__main__":
    v52.v34.base.main()
