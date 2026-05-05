from pathlib import Path

from simulator.s3_spectral_operator import (
    hydrogen_energy_from_K,
    hydrogen_energy_from_n,
    s3_laplacian_eigenvalue,
    shell_number_from_K,
    shifted_shell_operator_eigenvalue,
)


def test_s3_shell_eigenvalue_identities_k_0_to_5():
    for k in range(6):
        assert s3_laplacian_eigenvalue(k) == k * (k + 2)
        assert shifted_shell_operator_eigenvalue(k) == (k + 1) ** 2
        assert shell_number_from_K(k) == k + 1
        assert hydrogen_energy_from_K(k) == hydrogen_energy_from_n(k + 1)


def test_hydrogen_energies_negative_and_approach_zero_from_below():
    energies = [hydrogen_energy_from_K(k) for k in range(6)]
    assert all(e < 0 for e in energies)
    for left, right in zip(energies, energies[1:]):
        assert right > left


def test_native_s3_note_and_angular_note_required_sections_exist():
    native_note = Path("notes/native_s3_spectral_hydrogen_equation.md")
    assert native_note.exists()
    native_text = native_note.read_text(encoding="utf-8")
    assert "H_C" in native_text
    assert ("-Ry/(-Delta_{S^3}+1)" in native_text) or ("-\\frac{\\mathrm{Ry}}{-\\Delta_{S^3}+1}" in native_text)
    assert ("E_n = -Ry/n^2" in native_text) or ("E_n = -\\frac{\\mathrm{Ry}}{n^2}" in native_text)
    assert "Honesty boundary" in native_text

    angular_text = Path("notes/pi_k_angular_intertwiner.md").read_text(encoding="utf-8")
    assert "Clean statement" in angular_text
    assert "Technical construction" in angular_text
