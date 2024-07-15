"""test module for EPSG 1044 projections"""

import pytest

import numpy as np


from coord_operation.projection.epsg import Epsg1044
from coord_operation.surface import Ellipsoid

PHI = 0.9250245
LAMBDA = 0.9250245
EASTING = 165704.29
NORTHING = 1351950.22


@pytest.fixture(name="epsg_1044")
def epsg_1044_fixture() -> Epsg1044:
    """test fixture for EPSG::1044 tests"""
    return Epsg1044(Ellipsoid.of_eccentricity(a=6378245.0, eccentricity=0.08181333), phi1=0.73303829,
                    lambda0=0.89011792, phif=0.73303829, ef=0.00, nf=0.00)


def test_forward(epsg_1044):
    """forward test"""

    assert epsg_1044._compute_k0() == pytest.approx(expected=0.744260894, rel=1e-8)
    assert epsg_1044(np.array([PHI, LAMBDA])) == pytest.approx(expected=[EASTING, NORTHING], rel=1e-2)
    assert epsg_1044([PHI, LAMBDA]) == pytest.approx(expected=[EASTING, NORTHING], rel=1e-2)


def test_inverse(epsg_1044):
    """inverse test"""
    assert epsg_1044.inverse(np.array([EASTING, NORTHING])) == pytest.approx(expected=[PHI, LAMBDA], rel=1e-8)
    assert epsg_1044.inverse([EASTING, NORTHING]) == pytest.approx(expected=[PHI, LAMBDA], rel=1e-8)
    assert ((~epsg_1044)(np.array([EASTING, NORTHING])) == pytest.approx(expected=[PHI, LAMBDA], rel=1e-8))
    assert (~epsg_1044)([EASTING, NORTHING]) == pytest.approx(expected=[PHI, LAMBDA], rel=1e-8)
