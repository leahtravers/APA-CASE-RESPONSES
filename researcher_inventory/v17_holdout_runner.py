#!/usr/bin/env python3
"""V17 sealed-holdout entry point.

Delegates to the sealed holdout harness and only enlarges the subprocess timeout
for the V17 two-session adapter. This file never reads or emits holdout content.
"""
from researcher_inventory import holdout_runner as base


_OriginalCommandAdapter = base.CommandAdapter


class V17CommandAdapter(_OriginalCommandAdapter):
    def __init__(self, command: str, timeout: int = 480):
        super().__init__(command, timeout=timeout)


base.CommandAdapter = V17CommandAdapter


if __name__ == "__main__":
    base.main()
