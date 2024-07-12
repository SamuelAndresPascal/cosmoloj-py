"""The EPSG projection definitions."""
from typing import override

from math import log, tan, pi, atan, exp

from coord_operation.operation import InversibleProjection
from coord_operation.projection.mercator_spherical import MercatorSpherical
from coord_operation.surface import Surface, Spheroid


class Epsg1024(InversibleProjection):
    """EPSG::1024
    Popular Visualisation Pseudo-Mercator ("Web Mercator")
    """

    _PHI: int = 0
    _LAMBDA: int = 1
    _EASTING: int = 0
    _NORTHING: int = 1

    def __init__(self, ellipsoid: Surface, lambda0: float, fe: float, fn: float):
        self._ellipsoid = ellipsoid
        self._a = ellipsoid.semi_major_axis()
        self._lambda0 = lambda0
        self._fe = fe
        self._fn = fn

    @override
    def compute(self, i):
        return self._fe + self._a * (i[Epsg1024._LAMBDA] - self._lambda0), \
            self._fn + self._a * log(tan(pi / 4. + i[Epsg1024._PHI] / 2.))

    @override
    def inverse(self, i):
        return pi / 2. - 2. * atan(exp((self._fn - i[Epsg1024._NORTHING]) / self._a)), \
            (i[Epsg1024._EASTING] - self._fe) / self._a + self._lambda0


class Epsg1026(MercatorSpherical):
    """EPSG::1026
    Mercator (Spherical)
    """

    _EASTING: int = 0
    _NORTHING: int = 1

    def __init__(self, spheroid: Spheroid, phi0: float, lambda0: float, fe: float, fn: float):
        super().__init__(spheroid=spheroid, phi0=phi0, lambda0=lambda0)
        self._fe = fe
        self._fn = fn

    @override
    def compute(self, i):
        output = super().compute(i)
        return self._fe + output[Epsg1026._EASTING], self._fn + output[Epsg1026._NORTHING]

    @override
    def inverse(self, i):
        return super().inverse([i[Epsg1026._EASTING] - self._fe, i[Epsg1026._NORTHING] - self._fn])
