#!/usr/bin/env python3
"""V75 contract-version adapter preserving the proven transport/session recovery implementation."""
from __future__ import annotations

import os
from pathlib import Path

import v60_openai_agents_adapter as prior

prior.base.CONTRACT_VERSION = os.environ.get("CONTRACT_VERSION", "RI-CONTRACT-V75").strip() or "RI-CONTRACT-V75"
RECOVERY_DIR = Path("researcher_inventory/runtime/v75_session_recovery")
prior.recovery.RECOVERY_DIR = RECOVERY_DIR
prior.base.recovery.RECOVERY_DIR = RECOVERY_DIR

if __name__ == "__main__":
    raise SystemExit(prior.base.main())
