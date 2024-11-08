"""test module for EPSG 9802 projections"""

import pytest

import numpy as np


from coordop.projection.epsg import Epsg9802
from coordop.surface import Ellipsoid

PHI = 0.49741884
LAMBDA = -1.67551608
EASTING = 2963503.91
NORTHING = 254759.80

PHIF = 0.48578331
PHI1 = 0.49538262
PHI2 = 0.52854388

@pytest.fixture(name="epsg_9802")
def epsg_9802_fixture() -> Epsg9802:
    """test fixture for EPSG::9801 tests"""
    return Epsg9802(Ellipsoid.of_eccentricity(a=20925832.16, eccentricity=0.08227185), phif=PHIF,
                    lambdaf=-1.72787596, phi1=PHI1, phi2=PHI2, ef=2000000., nf=0.)

def test_forward(epsg_9802):
    """forward test"""

    assert epsg_9802._compute_m(PHI1) == pytest.approx(expected=0.88046050, rel=1e-9)
    assert epsg_9802._compute_m(PHI2) == pytest.approx(expected=0.86428642, rel=1e-8)
    assert epsg_9802._compute_t(PHI) == pytest.approx(expected=0.59686306, abs=1e-9)
    assert epsg_9802._compute_t(PHIF) == pytest.approx(expected=0.60475101, abs=1e-8)
    assert epsg_9802._compute_t(PHI1) == pytest.approx(expected=0.59823957, abs=1e-9)
    assert epsg_9802._compute_t(PHI2) == pytest.approx(expected=0.57602212, abs=1e-8)
    assert epsg_9802._compute_f() == pytest.approx(expected=2.31154807, abs=1e-8)
    assert epsg_9802._compute_n() == pytest.approx(expected=0.48991263, abs=1e-8)
    assert epsg_9802._compute_r(PHI) == pytest.approx(expected=37565039.86, rel=1.)
    assert epsg_9802._compute_r(PHIF) == pytest.approx(expected=37807441.20, rel=1.)
    assert epsg_9802._compute_theta(LAMBDA) == pytest.approx(expected=0.02565177, abs=1e-8)
    assert epsg_9802._compute_easting(PHI, LAMBDA) == pytest.approx(expected=EASTING, rel=1e-1)
    assert epsg_9802._compute_northing(PHI, LAMBDA) == pytest.approx(expected=NORTHING, rel=1e-1)

    assert epsg_9802(np.array([PHI, LAMBDA])) == pytest.approx(expected=[EASTING, NORTHING], rel=1e-1)
    assert epsg_9802([PHI, LAMBDA]) == pytest.approx(expected=[EASTING, NORTHING], rel=1e-1)

def test_inverse(epsg_9802):
    """inverse test"""

    assert epsg_9802._compute_inv_theta(EASTING, NORTHING) == pytest.approx(expected=0.025651765, abs=1e-9)
    assert epsg_9802._compute_inv_t(EASTING, NORTHING) == pytest.approx(expected=0.59686306, rel=1e-8)
    assert epsg_9802._compute_inv_r(EASTING, NORTHING) == pytest.approx(expected=37565039.86, rel=1)
    assert epsg_9802._compute_phi(EASTING, NORTHING) == pytest.approx(expected=PHI, abs=1e-8)
    assert epsg_9802._compute_lambda(EASTING, NORTHING) == pytest.approx(expected=LAMBDA, rel=1e-8)

    assert epsg_9802.inverse(np.array([EASTING, NORTHING])) == pytest.approx(expected=[PHI, LAMBDA], abs=1e-8)
    assert epsg_9802.inverse([EASTING, NORTHING]) == pytest.approx(expected=[PHI, LAMBDA], abs=1e-8)
    assert ((~epsg_9802)(np.array([EASTING, NORTHING])) == pytest.approx(expected=[PHI, LAMBDA], abs=1e-8))
    assert (~epsg_9802)([EASTING, NORTHING]) == pytest.approx(expected=[PHI, LAMBDA], abs=1e-8)
