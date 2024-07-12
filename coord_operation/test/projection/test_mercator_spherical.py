"""test module for Mercator Spherical defined in Map Projections"""

from math import radians

import pytest

from coord_operation.projection.mercator_spherical import MercatorSpherical
from coord_operation.surface import Spheroid


_RADIUS: float = 1.0
_DELTA: float = 5e-5
_EXPECTED_YTAB = [0.0000, 0.08738, 0.17543, 0.26484, 0.35638, 0.45088, 0.54931,
                  0.65284, 0.76291, 0.88137, 1.01068, 1.15423, 1.31696, 1.50645, 1.73542, 2.02759, 2.43625, 3.13130]


@pytest.fixture(name="projection")
def epsg_1024_fixture() -> MercatorSpherical:
    """test fixture for Mercator Spherical tests"""
    return MercatorSpherical(spheroid=Spheroid.of_radius(r=_RADIUS), phi0=0.0, lambda0=0.0)


def test_equatorial(projection):
    """table 7, page 45"""
    for i in range(18):
        lat = 5 * i
        lon = 5 * i * 2
        proj = projection.compute([radians(lat), radians(lon)])
        assert proj[1] == pytest.approx(_EXPECTED_YTAB[i], _DELTA)
        assert proj[0] == pytest.approx(lon * 0.017453, _DELTA)
