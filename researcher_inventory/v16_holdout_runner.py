#!/usr/bin/env python3
"""V16 sealed-holdout entry point.

Delegates to the sealed holdout harness and only enlarges the subprocess timeout
for the V16 two-session adapter. This file never reads or emits holdout content.
"""
from researcher_inventory import holdout_runner as base


_OriginalCommandAdapter = base.CommandAdapter


class V16CommandAdapter(_OriginalCommandAdapter):
    def __init__(self, command: str, timeout: int = 420):
        super().__init__(command, timeout=timeout)


base.CommandAdapter = V16CommandAdapter


if __name__ == "__main__":
    base.main()
