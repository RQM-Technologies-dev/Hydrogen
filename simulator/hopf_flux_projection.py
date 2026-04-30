"""Hopf projection and inverse-square diagnostics for Hydrogen Bridge v1.

These routines test a projection/scaling support layer only; they do not
constitute a full derivation of electromagnetism.
"""

from __future__ import annotations

from math import pi

import numpy as np


_AXIS_MAP = {
    "i": np.array([0.0, 1.0, 0.0, 0.0]),
    "j": np.array([0.0, 0.0, 1.0, 0.0]),
    "k": np.array([0.0, 0.0, 0.0, 1.0]),
}


def normalize_quaternion(q: np.ndarray) -> np.ndarray:
    """Normalize quaternion array of shape (..., 4) to unit length."""
    arr = np.asarray(q, dtype=float)
    if arr.shape[-1] != 4:
        raise ValueError("Quaternion input must have last dimension 4.")
    norms = np.linalg.norm(arr, axis=-1, keepdims=True)
    if np.any(norms == 0.0):
        raise ValueError("Cannot normalize zero-norm quaternion.")
    return arr / norms


def quaternion_conjugate(q: np.ndarray) -> np.ndarray:
    """Return quaternion conjugate [a, -b, -c, -d] for input [..., 4]."""
    arr = np.asarray(q, dtype=float)
    if arr.shape[-1] != 4:
        raise ValueError("Quaternion input must have last dimension 4.")
    out = arr.copy()
    out[..., 1:] *= -1.0
    return out


def quaternion_multiply(q1: np.ndarray, q2: np.ndarray) -> np.ndarray:
    """Hamilton product for quaternion arrays with trailing dimension 4."""
    a1, b1, c1, d1 = np.moveaxis(np.asarray(q1, dtype=float), -1, 0)
    a2, b2, c2, d2 = np.moveaxis(np.asarray(q2, dtype=float), -1, 0)
    return np.stack(
        [
            a1 * a2 - b1 * b2 - c1 * c2 - d1 * d2,
            a1 * b2 + b1 * a2 + c1 * d2 - d1 * c2,
            a1 * c2 - b1 * d2 + c1 * a2 + d1 * b2,
            a1 * d2 + b1 * c2 - c1 * b2 + d1 * a2,
        ],
        axis=-1,
    )


def hopf_project(q: np.ndarray, axis: str = "k") -> np.ndarray:
    """Project unit-quaternion orientation q to S^2 direction via q*a*q^{-1}."""
    if axis not in _AXIS_MAP:
        raise ValueError("axis must be one of 'i', 'j', 'k'.")
    qn = normalize_quaternion(q)
    axis_q = _AXIS_MAP[axis]
    axis_q = np.broadcast_to(axis_q, qn.shape)
    projected = quaternion_multiply(quaternion_multiply(qn, axis_q), quaternion_conjugate(qn))
    return projected[..., 1:]


def sample_unit_quaternions(count: int, seed: int = 0) -> np.ndarray:
    """Sample unit quaternions by normalizing Gaussian draws in R^4."""
    if count <= 0:
        raise ValueError("count must be positive.")
    rng = np.random.default_rng(seed)
    draws = rng.normal(size=(count, 4))
    return normalize_quaternion(draws)


def projection_statistics(count: int = 10000, seed: int = 0, axis: str = "k") -> dict:
    """Compute isotropy and norm diagnostics for Hopf-projected S^2 directions."""
    samples = sample_unit_quaternions(count=count, seed=seed)
    vecs = hopf_project(samples, axis=axis)
    norms = np.linalg.norm(vecs, axis=1)
    return {
        "count": int(count),
        "mean_norm": float(np.mean(norms)),
        "max_norm_error": float(np.max(np.abs(norms - 1.0))),
        "mean_x": float(np.mean(vecs[:, 0])),
        "mean_y": float(np.mean(vecs[:, 1])),
        "mean_z": float(np.mean(vecs[:, 2])),
        "second_moment_x": float(np.mean(vecs[:, 0] ** 2)),
        "second_moment_y": float(np.mean(vecs[:, 1] ** 2)),
        "second_moment_z": float(np.mean(vecs[:, 2] ** 2)),
    }


def inverse_square_flux_table(radii: list[float] | np.ndarray, flux: float = 1.0) -> list[dict]:
    """Build inverse-square flux table on spherical shells for scaling diagnostics."""
    rs = np.asarray(radii, dtype=float)
    if np.any(rs <= 0):
        raise ValueError("All radii must be positive.")

    rows: list[dict] = []
    for r in rs:
        area = 4.0 * pi * r**2
        field = flux / area
        potential = -flux / (4.0 * pi * r)
        reconstructed_flux = field * area
        rows.append(
            {
                "r": float(r),
                "area": float(area),
                "field": float(field),
                "potential": float(potential),
                "reconstructed_flux": float(reconstructed_flux),
            }
        )
    return rows


def fit_loglog_slope(x, y) -> float:
    """Fit slope of log(abs(y)) vs log(x) for positive x and nonzero y."""
    x_arr = np.asarray(x, dtype=float)
    y_arr = np.asarray(y, dtype=float)
    if np.any(x_arr <= 0):
        raise ValueError("x values must be positive.")
    if np.any(y_arr == 0):
        raise ValueError("y values must be nonzero.")
    slope, _ = np.polyfit(np.log(x_arr), np.log(np.abs(y_arr)), 1)
    return float(slope)


def flux_scaling_diagnostics(radii=None, flux: float = 1.0) -> dict:
    """Compute inverse-square and inverse-radius slope diagnostics for field support layer."""
    if radii is None:
        radii = np.array([1, 2, 3, 4, 5, 8, 13], dtype=float)
    rows = inverse_square_flux_table(radii=radii, flux=flux)
    radii_arr = np.asarray([row["r"] for row in rows], dtype=float)
    field_vals = np.asarray([row["field"] for row in rows], dtype=float)
    potential_vals = np.asarray([abs(row["potential"]) for row in rows], dtype=float)
    reconstructed_flux = np.asarray([row["reconstructed_flux"] for row in rows], dtype=float)
    return {
        "field_slope": fit_loglog_slope(radii_arr, field_vals),
        "potential_slope": fit_loglog_slope(radii_arr, potential_vals),
        "max_flux_error": float(np.max(np.abs(reconstructed_flux - flux))),
        "rows": rows,
    }
