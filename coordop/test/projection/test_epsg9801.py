"""test module for EPSG 9801 projections"""

import pytest

import numpy as np


from coordop.projection.epsg import Epsg9801
from coordop.surface import Ellipsoid

PHI = 0.31297535
LAMBDA = -1.34292061
EASTING = 255966.58
NORTHING = 142493.51

PHI0=0.31415927


@pytest.fixture(name="epsg_9801")
def epsg_9801_fixture() -> Epsg9801:
    """test fixture for EPSG::9801 tests"""
    return Epsg9801(Ellipsoid.of_eccentricity(a=6378206.4, eccentricity=0.08227185), phi0=PHI0,
                    lambda0=-1.34390352, k0=1., fe=250000., fn=150000.)


def test_forward(epsg_9801):
    """forward test"""

    assert epsg_9801._compute_m(PHI0) == pytest.approx(expected=0.95136402, rel=1e-8)
    assert epsg_9801._compute_t(PHI0) == pytest.approx(expected=0.72806411, abs=1e-8)
    assert epsg_9801._compute_f() == pytest.approx(expected=3.39591092, abs=1e-7)
    assert epsg_9801._compute_n() == pytest.approx(expected=0.30901699, abs=1e-8)
    assert epsg_9801._compute_r(PHI) == pytest.approx(expected=19643955.26, rel=1.)
    assert epsg_9801._compute_r(PHI0) == pytest.approx(expected=19636447.86, rel=1.)
    assert epsg_9801._compute_theta(LAMBDA) == pytest.approx(expected=0.00030374, abs=1e-8)
    assert epsg_9801._compute_t(PHI) == pytest.approx(expected=0.728965259, rel=1e-9)
    assert epsg_9801._compute_easting(PHI, LAMBDA) == pytest.approx(expected=EASTING, rel=1e-2)
    assert epsg_9801._compute_northing(PHI, LAMBDA) == pytest.approx(expected=NORTHING, rel=1e-1)

    assert epsg_9801(np.array([PHI, LAMBDA])) == pytest.approx(expected=[EASTING, NORTHING], rel=1e-2)
    assert epsg_9801([PHI, LAMBDA]) == pytest.approx(expected=[EASTING, NORTHING], rel=1e-2)


def test_inverse(epsg_9801):
    """inverse test"""

    assert epsg_9801._compute_inv_theta(EASTING, NORTHING) == pytest.approx(expected=0.000303736, abs=1e-9)
    assert epsg_9801._compute_inv_t(EASTING, NORTHING) == pytest.approx(expected=0.728965259, rel=1e-8)
    assert epsg_9801._compute_inv_r(EASTING, NORTHING) == pytest.approx(expected=19643955.26, rel=1e-2)
    assert epsg_9801._compute_phi(EASTING, NORTHING) == pytest.approx(expected=PHI, abs=1e-8)
    assert epsg_9801._compute_lambda(EASTING, NORTHING) == pytest.approx(expected=LAMBDA, rel=1e-9)

    assert epsg_9801.inverse(np.array([EASTING, NORTHING])) == pytest.approx(expected=[PHI, LAMBDA], abs=1e-8)
    assert epsg_9801.inverse([EASTING, NORTHING]) == pytest.approx(expected=[PHI, LAMBDA], abs=1e-8)
    assert ((~epsg_9801)(np.array([EASTING, NORTHING])) == pytest.approx(expected=[PHI, LAMBDA], abs=1e-8))
    assert (~epsg_9801)([EASTING, NORTHING]) == pytest.approx(expected=[PHI, LAMBDA], abs=1e-8)
