#!/usr/bin/env python3
"""V16 calibration entry point.

Uses the validated class-local semantic evaluator and a subprocess budget sized
for the V16 two-session extraction/verification adapter. This module changes no
archetype, evaluator criterion, worker contract content, or holdout content.
"""
from researcher_inventory import v12_calibration_runner as v12


base = v12.base
_OriginalCommandAdapter = base.CommandAdapter


class V16CommandAdapter(_OriginalCommandAdapter):
    def __init__(self, command: str, timeout: int = 420):
        super().__init__(command, timeout=timeout)


base.CommandAdapter = V16CommandAdapter


if __name__ == "__main__":
    base.main()
