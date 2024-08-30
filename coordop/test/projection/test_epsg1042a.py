"""test module for EPSG 1042 projections"""

import pytest

import numpy as np

from coordop.projection.epsg import Epsg1042a
from coordop.surface import Ellipsoid

A = 6377397.155
E = 0.081696831

C1 = 2.946529277e-2
C2 = 2.515965696e-2
C3 = 1.193845912e-7
C4 = -4.668270147e-7
C5 = 9.233980362e-12
C6 = 1.523735715e-12
C7 = 1.696780024e-18
C8 = 4.408314235e-18
C9 = -8.331083518e-24
C10 = -3.689471323e-24

PHIC = 0.863937979
LAMBDA0 = 0.741764932
ALPHAC = 0.528627763
PHIP = 1.370083463
KP = 0.9999
EF = 5000000.00
NF =5000000.00

PHI = 0.876312568
LAMBDA = 0.602425500
SOUTHING = 6050538.71
WESTING = 5568990.91


@pytest.fixture(name="epsg_1042")
def epsg_1042_fixture() -> Epsg1042a:
    """test fixture for EPSG::1042 tests"""
    return Epsg1042a(Ellipsoid.of_eccentricity(a=A, eccentricity=E),
                     phic=PHIC, lambda0=LAMBDA0, alphac=ALPHAC, phip=PHIP, kp=KP,
                     ef=EF, nf=NF, x0=1089000.00, y0=654000.00,
                     c1=C1, c2=C2, c3=C3, c4=C4, c5=C5, c6=C6, c7=C7, c8=C8, c9=C9, c10=C10)


def test_forward(epsg_1042):
    """forward test"""

    u = epsg_1042._compute_u(PHI)
    v = epsg_1042._compute_v(LAMBDA)
    t = epsg_1042._compute_t(u, v)

    assert u == pytest.approx(expected=0.875596949, rel=1e-8)
    assert v == pytest.approx(expected=0.139422687, rel=1e-9)
    assert t == pytest.approx(expected=1.386275049, rel=1e-8)
    assert epsg_1042._compute_d(u, v, t) == pytest.approx(expected=0.506554623, rel=1e-8)
    assert epsg_1042._theta(u, v, t) == pytest.approx(expected=0.496385389, rel=1e-8)
    assert epsg_1042._r(u, v, t) == pytest.approx(expected=1194731.014, rel=1e-1)

    assert epsg_1042([PHI, LAMBDA]) == pytest.approx(expected=[SOUTHING, WESTING], rel=1e-1)
    assert epsg_1042(np.array([PHI, LAMBDA])) == pytest.approx(expected=[SOUTHING, WESTING], rel=1e-1)


def test_inverse(epsg_1042):
    """inverse test"""

    i_xp = epsg_1042._inv_xp([SOUTHING, WESTING])
    i_yp = epsg_1042._inv_yp([SOUTHING, WESTING])

    i_d = epsg_1042._compute_inv_d(i_xp, i_yp)
    i_t = epsg_1042._compute_inv_t(i_xp, i_yp)
    i_u = epsg_1042._compute_inv_u(i_t, i_d)

    assert i_xp == pytest.approx(expected=1050538.631, rel=1e-3)
    assert i_yp == pytest.approx(expected=568990.995, rel=1e-3)
    assert epsg_1042._compute_inv_r(i_xp, i_yp) == pytest.approx(expected=1194731.002, rel=1e-3)
    assert epsg_1042._compute_inv_theta(i_xp, i_yp) == pytest.approx(expected=0.496385393, rel=1e-8)
    assert i_d == pytest.approx(expected=0.506554627, rel=1e-8)
    assert i_t == pytest.approx(expected=1.386275051, rel=1e-9)
    assert i_u == pytest.approx(expected=0.875596951, rel=1e-9)
    assert epsg_1042._compute_inv_v(i_t, i_d, i_u) == pytest.approx(expected=0.139422687, abs=1e-9)

    assert epsg_1042.inverse(np.array([SOUTHING, WESTING])) == pytest.approx(expected=[PHI, LAMBDA], rel=1e-8)
    assert epsg_1042.inverse([SOUTHING, WESTING]) == pytest.approx(expected=[PHI, LAMBDA], rel=1e-8)
    assert ((~epsg_1042)(np.array([SOUTHING, WESTING])) == pytest.approx(expected=[PHI, LAMBDA], rel=1e-8))
    assert (~epsg_1042)([SOUTHING, WESTING]) == pytest.approx(expected=[PHI, LAMBDA], rel=1e-8)
