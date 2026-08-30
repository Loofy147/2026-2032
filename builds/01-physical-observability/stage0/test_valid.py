from __future__ import annotations

import numpy as np

from cps_valid import CaseConfig, run_once, run_matrix, summarize


def test_online_measurements_follow_the_same_trajectory() -> None:
    cfg = CaseConfig(horizon=100, seed=7)
    a = run_once(cfg, "nominal", "fixed_feedback")
    b = run_once(cfg, "nominal", "fixed_feedback")
    assert np.array_equal(a["true"], b["true"])
    assert np.array_equal(a["estimate"], b["estimate"])


def test_open_loop_is_distinct_from_feedback() -> None:
    cfg = CaseConfig(horizon=200, seed=11)
    open_loop = summarize(run_once(cfg, "pulse", "open_loop"))
    fixed = summarize(run_once(cfg, "pulse", "fixed_feedback"))
    assert fixed["mean_abs_control"] > open_loop["mean_abs_control"]
    assert fixed["violation_rate"] < open_loop["violation_rate"]


def test_held_out_case_is_explicit() -> None:
    cfg = CaseConfig(horizon=300, seed=13)
    result = run_matrix(cfg, repetitions=2)
    assert "held_out_ramp" in result["fixed_feedback"]


def test_uncertainty_coverage_is_a_probability() -> None:
    cfg = CaseConfig(horizon=200, seed=19)
    metrics = summarize(run_once(cfg, "pulse", "adaptive_uncertainty"))
    assert 0.0 <= metrics["coverage95"] <= 1.0
