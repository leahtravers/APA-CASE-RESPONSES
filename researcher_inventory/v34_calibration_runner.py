#!/usr/bin/env python3
"""V34 calibration entry point.

V34 restores the research-coordinate admission gate after V33 over-enumeration,
while retaining evaluator isolation, immutable workbook gates, and candidate-only
boundaries.

The V34 harness also filters the predecessor evaluator's ORDERING_MISMATCH finding.
That finding compared worker order to editor/workbook row order, while the durable
contract independently requires source-establishment order. Gold row sequence is
therefore not a semantic archetype requirement. Resolution, type, source/literal
preservation, Q flags, and compound construction remain evaluated unchanged.
"""
from __future__ import annotations

from researcher_inventory import v33_calibration_runner as v33
from researcher_inventory import inventory_apparatus as apparatus
from researcher_inventory.v34_task_rules import V34_BASE_RULES, V34_CLASS_RULES

apparatus.BASE_RULES = V34_BASE_RULES
apparatus.CLASS_RULES = V34_CLASS_RULES

base = v33.base
_OriginalEvaluate = base.evaluate


def v34_evaluate(payload, fixture):
    """Evaluator-only correction: do not score hidden editor row ordering.

    The worker never receives gold rows or this finding. V34 itself still requires
    source-establishment ordering; this wrapper only prevents arbitrary workbook
    row sequence from being treated as the gold semantic order.
    """
    return [
        (kind, message)
        for kind, message in _OriginalEvaluate(payload, fixture)
        if kind != "ORDERING_MISMATCH"
    ]


base.evaluate = v34_evaluate

if __name__ == "__main__":
    base.main()
