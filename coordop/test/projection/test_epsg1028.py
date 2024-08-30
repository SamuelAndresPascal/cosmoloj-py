"""test module for EPSG 1028 projections"""

import pytest

import numpy as np

from coordop.projection.epsg import Epsg1028Integration2dKind, Epsg1028Integration3rdKind, Epsg1028, \
    Epsg1028Series
from coordop.surface import Ellipsoid


@pytest.fixture(name="epsg_1028_2dkind")
def epsg_1028_2dkind_fixture() -> Epsg1028:
    """test fixture for EPSG::1028 tests"""
    return Epsg1028Integration2dKind(Ellipsoid.of_inverse_flattening(a=6378137.0, invf=298.257223563),
                                     phi1=0.,
                                     lambda0=0.,
                                     fe=0.,
                                     fn=0.)


@pytest.fixture(name="epsg_1028_3rdkind")
def epsg_1028_3rdkind_fixture() -> Epsg1028:
    """test fixture for EPSG::1028 tests"""
    return Epsg1028Integration3rdKind(Ellipsoid.of_inverse_flattening(a=6378137.0, invf=298.257223563),
                                      phi1=0.,
                                      lambda0=0.,
                                      fe=0.,
                                      fn=0.)


@pytest.fixture(name="epsg_1028_series")
def epsg_1028_series_fixture() -> Epsg1028:
    """test fixture for EPSG::1028 tests"""
    return Epsg1028Series(Ellipsoid.of_inverse_flattening(a=6378137.0, invf=298.257223563),
                          phi1=0.,
                          lambda0=0.,
                          fe=0.,
                          fn=0.)


PHI = 0.959931086
LAMBDA = 0.174532925
EASTING = 1113194.91
NORTHING_2DKIND = 6097230.3131
# test avec l'intégrale du troisième type (on ne trouve pas exactement la même valeur pour northing)
NORTHING_3RDKIND = 6097230.30
# test avec la série (la valeur pour northing n'est pas tout à fait identique sans qu'on puisse trouver d'erreur
# dans la série)
NORTHING_SERIES = 6097230.29


def test_forward_2dkind(epsg_1028_2dkind):
    """test 2d kind integration implementation forward"""
    assert epsg_1028_2dkind([PHI, LAMBDA]) == pytest.approx(expected=[EASTING, NORTHING_2DKIND], rel=1e-2)
    assert epsg_1028_2dkind(np.array([PHI, LAMBDA])) == pytest.approx(expected=[EASTING, NORTHING_2DKIND], rel=1e-2)


def test_inverse_2dkind(epsg_1028_2dkind):
    """test 2d kind integration implementation inverse"""
    assert (~epsg_1028_2dkind)([EASTING, NORTHING_2DKIND]) == pytest.approx(expected=[PHI, LAMBDA], rel=1e-8)
    assert (~epsg_1028_2dkind)(np.array([EASTING, NORTHING_2DKIND])) == pytest.approx(expected=[PHI, LAMBDA], rel=1e-8)


def test_forward_3rdkind(epsg_1028_3rdkind):
    """test 3rd kind integration implementation forward"""
    assert epsg_1028_3rdkind([PHI, LAMBDA]) == pytest.approx(expected=[EASTING, NORTHING_3RDKIND], rel=1e-2)
    assert epsg_1028_3rdkind(np.array([PHI, LAMBDA])) == pytest.approx(expected=[EASTING, NORTHING_3RDKIND], rel=1e-2)


def test_inverse_3rdkind(epsg_1028_3rdkind):
    """test 3rd kind integration implementation inverse"""
    assert (~epsg_1028_3rdkind)([EASTING, NORTHING_3RDKIND]) == pytest.approx(expected=[PHI, LAMBDA], rel=1e-8)
    assert ((~epsg_1028_3rdkind)(np.array([EASTING, NORTHING_3RDKIND]))
            == pytest.approx(expected=[PHI, LAMBDA], rel=1e-8))


def test_forward_series(epsg_1028_series):
    """test series implementation forward"""
    assert epsg_1028_series([PHI, LAMBDA]) == pytest.approx(expected=[EASTING, NORTHING_SERIES], rel=1e-2)
    assert epsg_1028_series(np.array([PHI, LAMBDA])) == pytest.approx(expected=[EASTING, NORTHING_SERIES], rel=1e-2)


def test_inverse_series(epsg_1028_series):
    """test series implementation inverse"""
    assert (~epsg_1028_series)([EASTING, NORTHING_SERIES]) == pytest.approx(expected=[PHI, LAMBDA], rel=1e-8)
    assert (~epsg_1028_series)(np.array([EASTING, NORTHING_SERIES])) == pytest.approx(expected=[PHI, LAMBDA], rel=1e-8)
