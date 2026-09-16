#!/usr/bin/env python3
"""V62 calibration entry point using the preserved hidden evaluator and bounded-projection task rules."""
from researcher_inventory import v52_calibration_runner as v52
from researcher_inventory import inventory_apparatus as apparatus
from researcher_inventory.v62_task_rules import V62_BASE_RULES, V62_CLASS_RULES

apparatus.BASE_RULES = V62_BASE_RULES
apparatus.CLASS_RULES = V62_CLASS_RULES

if __name__ == "__main__":
    v52.v34.base.main()
