#!/usr/bin/env python3
"""V53 calibration entry point using V52 hidden evaluator with relation-integrity worker rules."""
from researcher_inventory import v52_calibration_runner as v52
from researcher_inventory import inventory_apparatus as apparatus
from researcher_inventory.v53_task_rules import V53_BASE_RULES, V53_CLASS_RULES

apparatus.BASE_RULES = V53_BASE_RULES
apparatus.CLASS_RULES = V53_CLASS_RULES

if __name__ == "__main__":
    v52.v34.base.main()
