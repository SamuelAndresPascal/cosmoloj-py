"""test module for EPSG 9819 projections"""

import pytest

import numpy as np

from coord_operation.projection.epsg import Epsg9819b
from coord_operation.surface import Ellipsoid


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
SOUTHING = 1050538.643
WESTING = 568990.997


@pytest.fixture(name="epsg_9819")
def epsg_9819_fixture() -> Epsg9819b:
    """test fixture for EPSG::9819 tests"""
    return Epsg9819b(Ellipsoid.of_eccentricity(a=A, eccentricity=E),
                     phic=PHIC, lambda0=LAMBDA0, alphac=ALPHAC, phip=PHIP, kp=KP, fe=EF, fn=NF)


def test_forward(epsg_9819):
    """forward test"""

    u = epsg_9819._compute_u(PHI)
    v = epsg_9819._compute_v(LAMBDA)
    t = epsg_9819._compute_t(u, v)

    assert u == pytest.approx(expected=0.875596949, rel=1e-8)
    assert v == pytest.approx(expected=0.139422687, rel=1e-9)
    assert t == pytest.approx(expected=1.386275049, rel=1e-8)
    assert epsg_9819._compute_d(u, v, t) == pytest.approx(expected=0.506554623, rel=1e-8)
    assert epsg_9819._theta(u, v, t) == pytest.approx(expected=0.496385389, rel=1e-8)
    assert epsg_9819._r(u, v, t) == pytest.approx(expected=1194731.014, rel=1e-1)

    assert epsg_9819([PHI, LAMBDA]) == pytest.approx(expected=[SOUTHING, WESTING], rel=1e-1)
    assert epsg_9819(np.array([PHI, LAMBDA])) == pytest.approx(expected=[SOUTHING, WESTING], rel=1e-1)


def test_inverse(epsg_9819):
    """inverse test"""

    i_xp = epsg_9819._compute_inv_xp(SOUTHING)
    i_yp = epsg_9819._compute_inv_yp(WESTING)

    i_d = epsg_9819._compute_inv_d(i_xp, i_yp)
    i_t = epsg_9819._compute_inv_t(i_xp, i_yp)
    i_u = epsg_9819._compute_inv_u(i_t, i_d)

    assert i_xp == pytest.approx(expected=1050538.643, rel=1e-3)
    assert i_yp == pytest.approx(expected=568990.997, rel=1e-3)
    assert epsg_9819._compute_inv_r(i_xp, i_yp) == pytest.approx(expected=1194731.014, rel=1e-3)
    assert epsg_9819._compute_inv_theta(i_xp, i_yp) == pytest.approx(expected=0.496385389, rel=1e-9)
    assert i_d == pytest.approx(expected=0.506554623, rel=1e-9)
    assert i_t == pytest.approx(expected=1.386275049, rel=1e-9)
    assert i_u == pytest.approx(expected=0.875596949, rel=1e-9)
    assert epsg_9819._compute_inv_v(i_t, i_d, i_u) == pytest.approx(expected=0.139422687, abs=1e-9)

    assert epsg_9819.inverse(np.array([SOUTHING, WESTING])) == pytest.approx(expected=[PHI, LAMBDA], rel=1e-8)
    assert epsg_9819.inverse([SOUTHING, WESTING]) == pytest.approx(expected=[PHI, LAMBDA], rel=1e-8)
    assert ((~epsg_9819)(np.array([SOUTHING, WESTING])) == pytest.approx(expected=[PHI, LAMBDA], rel=1e-8))
    assert (~epsg_9819)([SOUTHING, WESTING]) == pytest.approx(expected=[PHI, LAMBDA], rel=1e-8)
