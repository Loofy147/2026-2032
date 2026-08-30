from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

import numpy as np

Mode = Literal["open_loop", "fixed_feedback", "adaptive_uncertainty"]


@dataclass(frozen=True)
class CaseConfig:
    dt: float = 0.01
    horizon: int = 1000
    process_noise: float = 0.01
    measurement_noise: float = 0.03
    dropout_probability: float = 0.0
    measurement_delay_steps: int = 0
    seed: int = 20260830


class PointMass2D:
    def __init__(self, dt: float) -> None:
        self.dt = dt
        self.x = np.zeros(2, dtype=float)

    def reset(self, x0: tuple[float, float] = (1.0, 0.0)) -> None:
        self.x = np.asarray(x0, dtype=float)
        if self.x.shape != (2,):
            raise ValueError("x0 must contain exactly two states")

    def step(self, u: float, disturbance: float) -> np.ndarray:
        a = float(u) + float(disturbance)
        self.x = np.array([
            self.x[0] + self.dt * self.x[1],
            self.x[1] + self.dt * a,
        ])
        return self.x.copy()


class KalmanObserver:
    def __init__(self, cfg: CaseConfig) -> None:
        dt = cfg.dt
        self.A = np.array([[1.0, dt], [0.0, 1.0]])
        self.B = np.array([0.0, dt])
        self.C = np.array([[1.0, 0.0]])
        self.Q = np.eye(2) * max(cfg.process_noise**2, 1e-12)
        self.R = np.array([[max(cfg.measurement_noise**2, 1e-12)]])
        self.reset()

    def reset(self) -> None:
        self.x = np.zeros(2, dtype=float)
        self.P = np.eye(2)

    def predict(self, u: float) -> None:
        self.x = self.A @ self.x + self.B * float(u)
        self.P = self.A @ self.P @ self.A.T + self.Q

    def update(self, measurement: float) -> None:
        innovation = np.array([[measurement]]) - self.C @ self.x[:, None]
        S = self.C @ self.P @ self.C.T + self.R
        K = self.P @ self.C.T @ np.linalg.inv(S)
        self.x = self.x + (K @ innovation).ravel()
        self.P = (np.eye(2) - K @ self.C) @ self.P
        self.P = 0.5 * (self.P + self.P.T)


def disturbance_profile(case: str, k: int) -> float:
    if case == "nominal":
        return 0.0
    if case == "pulse":
        return 0.7 if 250 <= k < 350 else 0.0
    if case == "held_out_ramp":
        return min(0.7, max(0.0, (k - 450) * 0.004)) if 450 <= k < 625 else 0.0
    raise ValueError(f"unknown disturbance case: {case}")


def controller(x_hat: np.ndarray, covariance: np.ndarray, mode: Mode) -> float:
    if mode == "open_loop":
        return 0.0
    scale = 1.0
    if mode == "adaptive_uncertainty":
        scale = 1.0 / (1.0 + 0.5 * float(np.trace(covariance)))
    return float(-scale * (1.8 * x_hat[0] + 1.2 * x_hat[1]))


def run_once(cfg: CaseConfig, case: str, mode: Mode) -> dict[str, np.ndarray | list[float | None]]:
    rng = np.random.default_rng(cfg.seed)
    plant = PointMass2D(cfg.dt)
    observer = KalmanObserver(cfg)
    plant.reset()
    observer.reset()

    true = np.zeros((cfg.horizon, 2))
    estimate = np.zeros((cfg.horizon, 2))
    covariance = np.zeros((cfg.horizon, 2, 2))
    controls = np.zeros(cfg.horizon)
    disturbances = np.zeros(cfg.horizon)
    observations: list[float | None] = []
    previous_control = 0.0

    for k in range(cfg.horizon):
        observer.predict(previous_control)
        measurement: float | None = None
        if k >= cfg.measurement_delay_steps:
            src_index = k - cfg.measurement_delay_steps
            src_position = true[src_index, 0] if cfg.measurement_delay_steps else plant.x[0]
            measurement = float(src_position + rng.normal(0.0, cfg.measurement_noise))
            if rng.random() < cfg.dropout_probability:
                measurement = None
        if mode != "open_loop" and measurement is not None:
            observer.update(measurement)

        control = controller(observer.x, observer.P, mode)
        disturbance = disturbance_profile(case, k)
        state = plant.step(control, disturbance)

        true[k] = state
        estimate[k] = observer.x
        covariance[k] = observer.P
        controls[k] = control
        disturbances[k] = disturbance
        observations.append(measurement)
        previous_control = control

    return {
        "true": true,
        "estimate": estimate,
        "covariance": covariance,
        "control": controls,
        "disturbance": disturbances,
        "observations": observations,
    }


def summarize(run: dict[str, np.ndarray | list[float | None]], threshold: float = 0.2) -> dict[str, float]:
    true = run["true"]
    estimate = run["estimate"]
    covariance = run["covariance"]
    controls = run["control"]
    assert isinstance(true, np.ndarray)
    assert isinstance(estimate, np.ndarray)
    assert isinstance(covariance, np.ndarray)
    assert isinstance(controls, np.ndarray)

    position = true[:, 0]
    estimation_error = estimate[:, 0] - position
    sigma = np.sqrt(np.maximum(covariance[:, 0, 0], 0.0))
    return {
        "rmse_position": float(np.sqrt(np.mean(position**2))),
        "p95_abs_position": float(np.quantile(np.abs(position), 0.95)),
        "violation_rate": float(np.mean(np.abs(position) > threshold)),
        "max_abs_position": float(np.max(np.abs(position))),
        "mean_abs_control": float(np.mean(np.abs(controls))),
        "estimator_rmse": float(np.sqrt(np.mean(estimation_error**2))),
        "coverage95": float(np.mean(np.abs(estimation_error) <= 1.96 * np.maximum(sigma, 1e-12))),
    }


def run_matrix(cfg: CaseConfig, repetitions: int = 5) -> dict[str, dict[str, dict[str, float]]]:
    cases = ("nominal", "pulse", "held_out_ramp")
    modes: tuple[Mode, ...] = ("open_loop", "fixed_feedback", "adaptive_uncertainty")
    out: dict[str, dict[str, dict[str, float]]] = {}
    for mode in modes:
        out[mode] = {}
        for case in cases:
            metrics = []
            for i in range(repetitions):
                run_mode: Mode = "fixed_feedback" if mode == "fixed_feedback" else mode
                run_cfg = CaseConfig(**{**cfg.__dict__, "seed": cfg.seed + i})
                metrics.append(summarize(run_once(run_cfg, case, run_mode)))
            out[mode][case] = {
                key: float(np.mean([m[key] for m in metrics])) for key in metrics[0]
            }
    return out
