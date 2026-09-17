#!/usr/bin/env python3
"""V63 calibration entry point using the preserved hidden evaluator and scene-binding task rules."""
from researcher_inventory import v52_calibration_runner as v52
from researcher_inventory import inventory_apparatus as apparatus
from researcher_inventory.v63_task_rules import V63_BASE_RULES, V63_CLASS_RULES

apparatus.BASE_RULES = V63_BASE_RULES
apparatus.CLASS_RULES = V63_CLASS_RULES

if __name__ == "__main__":
    v52.v34.base.main()
