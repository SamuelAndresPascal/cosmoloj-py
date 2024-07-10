import pytest

from math_operation.projection.epsg_1024 import Epsg1024
from math_operation.surface import  Spheroid

import numpy as np

phi = 0.425542460
l = -1.751147016
easting = -11169055.58
northing = 2800000.00


@pytest.fixture()
def transform() -> Epsg1024:
    return Epsg1024(ellipsoid=Spheroid.of_radius(r=6378137.0), lambda0=0.0, fe=0.00, fn=0.00)


def test_forward(transform):
    assert transform.compute(np.array([phi, l])) == pytest.approx(expected=[easting, northing], rel=1e-2)
    assert transform.compute([phi, l]) == pytest.approx(expected=[easting, northing], rel=1e-2)


def test_inverse(transform):
    assert transform.inverse(np.array([easting, northing])) == pytest.approx(expected=[phi, l], rel=1e-2)
    assert transform.inverse([easting, northing]) == pytest.approx(expected=[phi, l], rel=1e-2)
    assert (transform.inverseOperation().compute(np.array([easting, northing]))
            == pytest.approx(expected=[phi, l], rel=1e-2))
    assert transform.inverseOperation().compute([easting, northing]) == pytest.approx(expected=[phi, l], rel=1e-2)
