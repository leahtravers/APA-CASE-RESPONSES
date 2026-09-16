#!/usr/bin/env python3
"""V56 calibration entry point using the preserved hidden evaluator with representation-graph rules."""
from researcher_inventory import v52_calibration_runner as v52
from researcher_inventory import inventory_apparatus as apparatus
from researcher_inventory.v56_task_rules import V56_BASE_RULES, V56_CLASS_RULES

apparatus.BASE_RULES = V56_BASE_RULES
apparatus.CLASS_RULES = V56_CLASS_RULES

if __name__ == "__main__":
    v52.v34.base.main()
