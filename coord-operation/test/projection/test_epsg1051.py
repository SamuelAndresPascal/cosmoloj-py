"""test module for EPSG 1051 projections"""

import pytest

import numpy as np


from coord_operation.projection.epsg import Epsg1051
from coord_operation.surface import Ellipsoid

PHI = 0.763581548
LAMBDA = -1.451532161
EASTING = 2308335.75
NORTHING = 160210.48

PHI1 = 0.771144641
PHI2 = 0.797615468
PHIF=0.756018454


@pytest.fixture(name="epsg_1051")
def epsg_1051_fixture() -> Epsg1051:
    """test fixture for EPSG::1051 tests"""
    return Epsg1051(Ellipsoid.of_eccentricity(a=20925832.164, eccentricity=0.08227185), phif=PHIF,
                    lambdaf=-1.471894336, phi1=PHI1, phi2=PHI2, ef=2000000., nf=0.0, k=1.0000382)


def test_forward(epsg_1051):
    """forward test"""

    assert epsg_1051._compute_m(PHI1) == pytest.approx(expected=0.718295175, rel=1e-9)
    assert epsg_1051._compute_m(PHI2) == pytest.approx(expected=0.699629151, rel=1e-9)
    assert epsg_1051._compute_t(PHI) == pytest.approx(expected=0.429057680, abs=1e-9)
    assert epsg_1051._compute_t(PHIF) == pytest.approx(expected=0.433541026, abs=1e-9)
    assert epsg_1051._compute_t(PHI1) == pytest.approx(expected=0.424588396, rel=1e-9)
    assert epsg_1051._compute_t(PHI2) == pytest.approx(expected=0.409053868, rel=1e-9)
    assert epsg_1051._compute_n() == pytest.approx(expected=0.706407410, rel=1e-9)
    assert epsg_1051._compute_f() == pytest.approx(expected=1.862317735, rel=1e-9)
    assert epsg_1051._compute_r(PHI) == pytest.approx(expected=21436775.51, rel=1e-2)
    assert epsg_1051._compute_r(PHIF) == pytest.approx(expected=21594768.40, rel=1e-2)
    assert epsg_1051._theta(LAMBDA) == pytest.approx(expected=0.014383991, abs=1e-9)
    assert epsg_1051._compute_easting(PHI, LAMBDA) == pytest.approx(expected=EASTING, rel=1e-2)
    assert epsg_1051._compute_northing(PHI, LAMBDA) == pytest.approx(expected=NORTHING, rel=1e-1)

    assert epsg_1051(np.array([PHI, LAMBDA])) == pytest.approx(expected=[EASTING, NORTHING], rel=1e-2)
    assert epsg_1051([PHI, LAMBDA]) == pytest.approx(expected=[EASTING, NORTHING], rel=1e-2)


def test_inverse(epsg_1051):
    """inverse test"""

    assert epsg_1051._inv_theta(EASTING, NORTHING) == pytest.approx(expected=0.014383991, abs=1e-9)
    assert epsg_1051._inv_t(EASTING, NORTHING) == pytest.approx(expected=0.429057680, rel=1e-9)
    assert epsg_1051._inv_r(EASTING, NORTHING) == pytest.approx(expected=21436775.51, rel=1e-2)
    assert epsg_1051._compute_phi(EASTING, NORTHING) == pytest.approx(expected=PHI, rel=1e-9)
    assert epsg_1051._compute_lambda(EASTING, NORTHING) == pytest.approx(expected=LAMBDA, rel=1e-9)

    assert epsg_1051.inverse(np.array([EASTING, NORTHING])) == pytest.approx(expected=[PHI, LAMBDA], rel=1e-8)
    assert epsg_1051.inverse([EASTING, NORTHING]) == pytest.approx(expected=[PHI, LAMBDA], rel=1e-8)
    assert ((~epsg_1051)(np.array([EASTING, NORTHING])) == pytest.approx(expected=[PHI, LAMBDA], rel=1e-8))
    assert (~epsg_1051)([EASTING, NORTHING]) == pytest.approx(expected=[PHI, LAMBDA], rel=1e-8)
