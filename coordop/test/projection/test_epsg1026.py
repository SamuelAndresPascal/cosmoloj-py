"""test module for EPSG 1026 projections"""

import pytest

import numpy as np


from coordop.projection.epsg import Epsg1026
from coordop.surface import Spheroid

PHI = 0.425542460
LAMBDA = -1.751147016
EASTING = -11156569.90
NORTHING = 2796869.94


@pytest.fixture(name="epsg_1026")
def epsg_1026_fixture() -> Epsg1026:
    """test fixture for EPSG::1026 tests"""
    return Epsg1026(Spheroid.of_radius(r=6371007.0), phi0=0.0, lambda0=0.0, fe=0.00, fn=0.00)


def test_forward(epsg_1026):
    """forward test"""
    assert epsg_1026(np.array([PHI, LAMBDA])) == pytest.approx(expected=[EASTING, NORTHING], rel=1e-2)
    assert epsg_1026([PHI, LAMBDA]) == pytest.approx(expected=[EASTING, NORTHING], rel=1e-2)


def test_inverse(epsg_1026):
    """inverse test"""
    assert epsg_1026.inverse(np.array([EASTING, NORTHING])) == pytest.approx(expected=[PHI, LAMBDA], rel=1e-2)
    assert epsg_1026.inverse([EASTING, NORTHING]) == pytest.approx(expected=[PHI, LAMBDA], rel=1e-2)
    assert ((~epsg_1026)(np.array([EASTING, NORTHING])) == pytest.approx(expected=[PHI, LAMBDA], rel=1e-2))
    assert (~epsg_1026)([EASTING, NORTHING]) == pytest.approx(expected=[PHI, LAMBDA], rel=1e-2)
