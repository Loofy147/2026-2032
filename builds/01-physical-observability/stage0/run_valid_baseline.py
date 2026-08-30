from __future__ import annotations

import argparse
import json
from pathlib import Path

from cps_valid import CaseConfig, run_matrix


def main() -> int:
    parser = argparse.ArgumentParser(description="Build 01 corrected Stage-0 digital-only experiment")
    parser.add_argument("--out", default="artifacts/stage0-valid-baseline.json")
    args = parser.parse_args()

    cfg = CaseConfig()
    payload = {
        "status": "DIGITAL_ONLY_VALID_HARNESS",
        "claim_id": "PROC-OBS-001",
        "hypothesis_id": "HYP-OBS-001",
        "case": "synthetic_point_mass",
        "modes": ["open_loop", "fixed_feedback", "adaptive_uncertainty"],
        "results": run_matrix(cfg),
        "notes": [
            "Corrected online measurement generation: every observation is generated from the same physical trajectory that receives the action.",
            "No Bosch FMU reproduction is claimed.",
            "Held-out ramp is evaluation-only.",
            "Adaptive mode is intentionally treated as a test hypothesis; it must beat the fixed-feedback baseline to justify added complexity.",
        ],
    }
    p = Path(args.out)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")
    print(p.resolve())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
