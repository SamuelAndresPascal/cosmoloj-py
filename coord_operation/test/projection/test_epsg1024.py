"""test module for EPSG projections"""

import pytest

import numpy as np


from coord_operation.projection.epsg import Epsg1024
from coord_operation.surface import Spheroid

PHI = 0.425542460
LAMBDA = -1.751147016
EASTING = -11169055.58
NORTHING = 2800000.00


@pytest.fixture(name="epsg_1024")
def epsg_1024_fixture() -> Epsg1024:
    """test fixture for EPSG::1024 tests"""
    return Epsg1024(ellipsoid=Spheroid.of_radius(r=6378137.0), lambda0=0.0, fe=0.00, fn=0.00)


def test_1024_forward(epsg_1024):
    """forward test"""
    assert epsg_1024(np.array([PHI, LAMBDA])) == pytest.approx(expected=[EASTING, NORTHING], rel=1e-2)
    assert epsg_1024([PHI, LAMBDA]) == pytest.approx(expected=[EASTING, NORTHING], rel=1e-2)


def test_1024_inverse(epsg_1024):
    """inverse test"""
    assert epsg_1024.inverse(np.array([EASTING, NORTHING])) == pytest.approx(expected=[PHI, LAMBDA], rel=1e-2)
    assert epsg_1024.inverse([EASTING, NORTHING]) == pytest.approx(expected=[PHI, LAMBDA], rel=1e-2)
    assert ((~epsg_1024)(np.array([EASTING, NORTHING])) == pytest.approx(expected=[PHI, LAMBDA], rel=1e-2))
    assert (~epsg_1024)([EASTING, NORTHING]) == pytest.approx(expected=[PHI, LAMBDA], rel=1e-2)
