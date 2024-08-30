"""test module for EPSG 1041 projections"""

import pytest

import numpy as np

from coordop.projection.epsg import Epsg1041a
from coordop.surface import Ellipsoid


A = 6377397.155
E = 0.081696831

PHIC = 0.863937979
LAMBDA0 = 0.741764932
ALPHAC = 0.528627763
PHIP = 1.370083463
KP = 0.9999
EF = 0.00
NF = 0.00

PHI = 0.876312568
LAMBDA = 0.602425500
NORTHING = -1050538.64
EASTING = -568990.00


@pytest.fixture(name="epsg_1041")
def epsg_1041_fixture() -> Epsg1041a:
    """test fixture for EPSG::1041 tests"""
    return Epsg1041a(Ellipsoid.of_eccentricity(a=A, eccentricity=E),
                     phic=PHIC, lambda0=LAMBDA0, alphac=ALPHAC, phip=PHIP, kp=KP, fe=EF, fn=NF)


def test_forward(epsg_1041):
    """forward test"""

    u = epsg_1041._compute_u(PHI)
    v = epsg_1041._compute_v(LAMBDA)
    t = epsg_1041._compute_t(u, v)

    assert u == pytest.approx(expected=0.875596949, rel=1e-8)
    assert v == pytest.approx(expected=0.139422687, rel=1e-9)
    assert t == pytest.approx(expected=1.386275049, rel=1e-8)
    assert epsg_1041._compute_d(u, v, t) == pytest.approx(expected=0.506554623, rel=1e-8)
    assert epsg_1041._theta(u, v, t) == pytest.approx(expected=0.496385389, rel=1e-8)
    assert epsg_1041._r(u, v, t) == pytest.approx(expected=1194731.014, rel=1e-1)

    assert epsg_1041([PHI, LAMBDA]) == pytest.approx(expected=[EASTING, NORTHING], rel=1e-1)
    assert epsg_1041(np.array([PHI, LAMBDA])) == pytest.approx(expected=[EASTING, NORTHING], rel=1e-1)


def test_inverse(epsg_1041):
    """inverse test"""

    i_xp = epsg_1041._compute_inv_xp(-NORTHING)
    i_yp = epsg_1041._compute_inv_yp(-EASTING)

    i_d = epsg_1041._compute_inv_d(i_xp, i_yp)
    i_t = epsg_1041._compute_inv_t(i_xp, i_yp)
    i_u = epsg_1041._compute_inv_u(i_t, i_d)

    assert i_xp == pytest.approx(expected=1050538.643, rel=1e-3)
    assert i_yp == pytest.approx(expected=568990.997, rel=1e-3)
    assert epsg_1041._compute_inv_r(i_xp, i_yp) == pytest.approx(expected=1194731.014, rel=1e-3)
    assert epsg_1041._compute_inv_theta(i_xp, i_yp) == pytest.approx(expected=0.496385389, rel=1e-5)
    assert i_d == pytest.approx(expected=0.506554623, rel=1e-5)
    assert i_t == pytest.approx(expected=1.386275049, rel=1e-7)
    assert i_u == pytest.approx(expected=0.875596949, rel=1e-7)
    assert epsg_1041._compute_inv_v(i_t, i_d, i_u) == pytest.approx(expected=0.139422687, abs=1e-6)

    assert epsg_1041.inverse(np.array([EASTING, NORTHING])) == pytest.approx(expected=[PHI, LAMBDA], rel=1e-6)
    assert epsg_1041.inverse([EASTING, NORTHING]) == pytest.approx(expected=[PHI, LAMBDA], rel=1e-6)
    assert ((~epsg_1041)(np.array([EASTING, NORTHING])) == pytest.approx(expected=[PHI, LAMBDA], rel=1e-6))
    assert (~epsg_1041)([EASTING, NORTHING]) == pytest.approx(expected=[PHI, LAMBDA], rel=1e-6)
