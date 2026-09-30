"""
Putting x, M and K on one physical scale: molecules per cell.

The equilibrium layer is not scale free. f competes with K in x*f/(K+f), so
the ratio of affinity to abundance decides everything, and both have to be in
the same units before rho means anything.

Three literature constants are needed, and every one of them is read from
data/constants.json, which is written by scripts/write_constants.py from
sources recorded in data/lit/constants/CONSTANTS_SOURCES.md and in
data/PROVENANCE.json. If that file is missing this module raises. It never
falls back to a default: a silently assumed constant would propagate into
every downstream result with nothing in the record to show where it came
from.

  n_mrna_per_cell      converts relative array intensity to molecules/cell
  ago2_copies_per_cell sets the RISC pool before the loaded fraction alpha
  kd_seed_match        anchors the arbitrary reference state of exp(ddG/RT)
  cell_volume_L        converts a molar Kd into molecules per cell

alpha, the fraction of Argonaute loaded with the transfected guide, is not
measured anywhere and is therefore swept, never chosen.
"""

import json
import os

import numpy as np

from .features import RT
from .provenance import DATA

CONST = os.path.join(DATA, "constants.json")
AVOGADRO = 6.02214076e23


def load_constants(path=CONST):
    if not os.path.exists(path):
        raise FileNotFoundError(
            f"{path} is missing. Literature constants must be written by "
            f"scripts/write_constants.py from verified sources before any "
            f"experiment that needs a physical scale can run.")
    with open(path) as fh:
        return json.load(fh)


def kd_molar_to_molecules_per_cell(kd_molar, cell_volume_L):
    return float(kd_molar) * AVOGADRO * float(cell_volume_L)


def anchor_constant(features_df, kd_anchor_molecules, anchor_class="7mer-m8"):
    """
    C such that the median site of the anchor class has the published
    dissociation constant. K_site = C * exp(ddG/RT); because that is a single
    multiplicative factor it carries straight through the parallel-site
    combination, so K_transcript_calibrated = C * K_transcript_uncalibrated.
    """
    d = features_df[features_df.site_class == anchor_class]
    b = np.exp(d.ddG_kcal.to_numpy() / RT)
    b = b[np.isfinite(b) & (b > 0)]
    if b.size == 0:
        raise ValueError(f"no finite sites of class {anchor_class}")
    med = float(np.median(b))
    return float(kd_anchor_molecules) / med, med


def build_scale(features_df, constants=None, kd_choice="central",
                mrna_choice="central"):
    """Returns everything downstream needs to work in molecules per cell."""
    c = constants or load_constants()
    kd = c["kd_seed_match_molar"][kd_choice]
    vol = c["hela_cell_volume_litres"]["central"]
    kd_mol = kd_molar_to_molecules_per_cell(kd, vol)
    C, med = anchor_constant(features_df, kd_mol,
                             c["kd_seed_match_site_class"])
    n_mrna = c["mrna_molecules_per_cell"][mrna_choice]
    return {
        "kd_seed_match_molar": kd,
        "kd_seed_match_molecules_per_cell": kd_mol,
        "hela_cell_volume_litres": vol,
        "anchor_site_class": c["kd_seed_match_site_class"],
        "median_boltzmann_factor_anchor_class": med,
        "K_scale_constant_C": C,
        "mrna_molecules_per_cell": n_mrna,
        "ago2_copies_per_cell_low": c["ago2_copies_per_cell"]["low"],
        "ago2_copies_per_cell_high": c["ago2_copies_per_cell"]["high"],
    }


def rho_from_alpha(alpha, scale):
    """rho = M / sum_j x_j = alpha * Ago2 copies / total mRNA copies.

    The abundance vector sums to the total mRNA count by construction, so rho
    reduces to a ratio of two measured copy numbers and one swept fraction.
    Returned as (low, high) because the Argonaute measurement is a range.
    """
    n = scale["mrna_molecules_per_cell"]
    return (alpha * scale["ago2_copies_per_cell_low"] / n,
            alpha * scale["ago2_copies_per_cell_high"] / n)
