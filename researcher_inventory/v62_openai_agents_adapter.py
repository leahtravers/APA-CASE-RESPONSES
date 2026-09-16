#!/usr/bin/env python3
"""V62 contract-version adapter preserving the proven V60 transport/session recovery implementation.

Only contract identity and recovery storage are changed prospectively. Gold/evaluator/holdout
material remains outside the worker boundary.
"""
from __future__ import annotations

import os
from pathlib import Path

import v60_openai_agents_adapter as prior

prior.base.CONTRACT_VERSION = os.environ.get("CONTRACT_VERSION", "RI-CONTRACT-V62").strip() or "RI-CONTRACT-V62"
RECOVERY_DIR = Path("researcher_inventory/runtime/v62_session_recovery")
prior.recovery.RECOVERY_DIR = RECOVERY_DIR
prior.base.recovery.RECOVERY_DIR = RECOVERY_DIR

if __name__ == "__main__":
    raise SystemExit(prior.base.main())
