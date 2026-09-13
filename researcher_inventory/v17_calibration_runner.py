#!/usr/bin/env python3
"""V17 calibration entry point.

Uses the validated class-local semantic evaluator and a subprocess budget sized
for the V17 two-session extraction/verification adapter. This module changes no
archetype, evaluator criterion, holdout content, or worker-visible gold evidence.
"""
from researcher_inventory import v12_calibration_runner as v12


base = v12.base
_OriginalCommandAdapter = base.CommandAdapter


class V17CommandAdapter(_OriginalCommandAdapter):
    def __init__(self, command: str, timeout: int = 480):
        super().__init__(command, timeout=timeout)


base.CommandAdapter = V17CommandAdapter


if __name__ == "__main__":
    base.main()
