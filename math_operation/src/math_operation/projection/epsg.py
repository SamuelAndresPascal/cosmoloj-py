"""The EPSG projection definitions."""

from math import log, tan, pi, atan, exp

from math_operation.operation import InversibleProjection
from math_operation.surface import Surface


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

    def compute(self, i):
        return self._fe + self._a * (i[Epsg1024._LAMBDA] - self._lambda0), \
            self._fn + self._a * log(tan(pi / 4. + i[Epsg1024._PHI] / 2.))

    def inverse(self, i):
        return pi / 2. - 2. * atan(exp((self._fn - i[Epsg1024._NORTHING]) / self._a)), \
            (i[Epsg1024._EASTING] - self._fe) / self._a + self._lambda0
