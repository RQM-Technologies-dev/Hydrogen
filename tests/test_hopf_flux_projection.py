import numpy as np
import pytest

from simulator.hopf_flux_projection import (
    flux_scaling_diagnostics,
    hopf_project,
    inverse_square_flux_table,
    normalize_quaternion,
    projection_statistics,
    sample_unit_quaternions,
)


def test_hopf_projection_unit_norm():
    qs = sample_unit_quaternions(1000, seed=42)
    projected = hopf_project(qs)
    norms = np.linalg.norm(projected, axis=1)
    assert np.allclose(norms, 1.0, atol=1e-12)


def test_projection_statistics_are_isotropic_enough():
    stats = projection_statistics(count=5000, seed=1)
    assert abs(stats["mean_norm"] - 1.0) < 1e-3
    assert abs(stats["mean_x"]) < 0.05
    assert abs(stats["mean_y"]) < 0.05
    assert abs(stats["mean_z"]) < 0.05
    assert abs(stats["second_moment_x"] - (1.0 / 3.0)) < 0.05
    assert abs(stats["second_moment_y"] - (1.0 / 3.0)) < 0.05
    assert abs(stats["second_moment_z"] - (1.0 / 3.0)) < 0.05


def test_inverse_square_flux_conservation():
    table = inverse_square_flux_table([1, 2, 3, 5, 8], flux=2.5)
    for row in table:
        assert abs(row["reconstructed_flux"] - 2.5) < 1e-12


def test_flux_scaling_slopes():
    diagnostics = flux_scaling_diagnostics()
    assert abs(diagnostics["field_slope"] + 2.0) < 1e-12
    assert abs(diagnostics["potential_slope"] + 1.0) < 1e-12
    assert diagnostics["max_flux_error"] < 1e-12


def test_invalid_inputs():
    with pytest.raises(ValueError):
        sample_unit_quaternions(0)
    with pytest.raises(ValueError):
        inverse_square_flux_table([1, 0])
    with pytest.raises(ValueError):
        normalize_quaternion(np.array([0.0, 0.0, 0.0, 0.0]))
