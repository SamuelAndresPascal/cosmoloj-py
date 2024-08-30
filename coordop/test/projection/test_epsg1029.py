"""test module for EPSG 1029 projections"""

import pytest

import numpy as np

from coordop.projection.epsg import Epsg1029
from coordop.surface import Ellipsoid

PHI = 0.959931086
LAMBDA = 0.174532925
EASTING = 1109462.5749057303
NORTHING = 6102044.152446388


@pytest.fixture(name="epsg_1029")
def epsg_1029_fixture() -> Epsg1029:
    """test fixture for EPSG::1029 tests"""
    return Epsg1029(Ellipsoid.of_inverse_flattening(a=6378137.0, invf=298.257223563), phi1=0., lambda0=0., fe=0., fn=0.)


def test_forward(epsg_1029):
    """forward test"""
    assert epsg_1029(np.array([PHI, LAMBDA])) == pytest.approx(expected=[EASTING, NORTHING], rel=1e-2)
    assert epsg_1029([PHI, LAMBDA]) == pytest.approx(expected=[EASTING, NORTHING], rel=1e-2)


def test_inverse(epsg_1029):
    """inverse test"""
    assert epsg_1029.inverse(np.array([EASTING, NORTHING])) == pytest.approx(expected=[PHI, LAMBDA], rel=1e-8)
    assert epsg_1029.inverse([EASTING, NORTHING]) == pytest.approx(expected=[PHI, LAMBDA], rel=1e-8)
    assert ((~epsg_1029)(np.array([EASTING, NORTHING])) == pytest.approx(expected=[PHI, LAMBDA], rel=1e-8))
    assert (~epsg_1029)([EASTING, NORTHING]) == pytest.approx(expected=[PHI, LAMBDA], rel=1e-8)
