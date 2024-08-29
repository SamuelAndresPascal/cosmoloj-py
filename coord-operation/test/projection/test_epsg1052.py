"""test module for EPSG 1052 projections"""

import pytest

import numpy as np


from coord_operation.projection.epsg import Epsg1052
from coord_operation.surface import Ellipsoid

PHI = 0.083775804
LAMBDA = -1.295906970
EASTING = 80859.033
NORTHING = 122543.174

PHI1 = 0.771144641
PHI2 = 0.797615468
PHIF=0.756018454


@pytest.fixture(name="epsg_1052")
def epsg_1051_fixture() -> Epsg1052:
    """test fixture for EPSG::1052 tests"""
    return Epsg1052(ellipsoid=Ellipsoid.of_inverse_flattening(a=6378137.0, invf=298.2572221),
                    phi0=0.081689893, lambda0=-1.294102154, h0=2550.000, fe=92334.879, fn=109320.965)


def test_forward(epsg_1052):
    """forward test"""

    assert epsg_1052(np.array([PHI, LAMBDA])) == pytest.approx(expected=[EASTING, NORTHING], rel=1e-2)
    assert epsg_1052([PHI, LAMBDA]) == pytest.approx(expected=[EASTING, NORTHING], rel=1e-2)


def test_inverse(epsg_1052):
    """inverse test"""

    assert epsg_1052.inverse(np.array([EASTING, NORTHING])) == pytest.approx(expected=[PHI, LAMBDA], abs=1e-9)
    assert epsg_1052.inverse([EASTING, NORTHING]) == pytest.approx(expected=[PHI, LAMBDA], abs=1e-9)
    assert ((~epsg_1052)(np.array([EASTING, NORTHING])) == pytest.approx(expected=[PHI, LAMBDA], abs=1e-9))
    assert (~epsg_1052)([EASTING, NORTHING]) == pytest.approx(expected=[PHI, LAMBDA], abs=1e-9)
