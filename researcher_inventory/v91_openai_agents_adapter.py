#!/usr/bin/env python3
"""V91 contract adapter retaining V90 bounded same-session recovery behavior."""
from __future__ import annotations

import os
from pathlib import Path

import v90_openai_agents_adapter as v90

CONTRACT_VERSION = os.environ.get("CONTRACT_VERSION", "RI-CONTRACT-V91").strip() or "RI-CONTRACT-V91"
v90.prior.base.CONTRACT_VERSION = CONTRACT_VERSION

RECOVERY_DIR = Path("researcher_inventory/runtime/v91_session_recovery")
v90.RECOVERY_DIR = RECOVERY_DIR
v90.recovery.RECOVERY_DIR = RECOVERY_DIR
v90.prior.base.recovery.RECOVERY_DIR = RECOVERY_DIR

if __name__ == "__main__":
    raise SystemExit(v90.prior.base.main())
