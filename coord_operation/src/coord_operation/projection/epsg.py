"""The EPSG projection definitions."""
from enum import Enum, auto
from typing import override

from math import log, tan, pi, atan, exp, sqrt, sin, cos, asin, atan2

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


class Epsg1027(InversibleProjection):
    """EPSG::1027
    Lambert Azimuthal Equal Area
    """

    class _Aspect(Enum):
        OBLIQUE = auto()
        NORTH_POLE = auto()
        SOUTH_POLE = auto()

    _PHI: int = 0
    _LAMBDA: int = 1
    _EASTING: int = 0
    _NORTHING: int = 1

    def __init__(self, spheroid: Spheroid, phi0: float, lambda0: float, fe: float, fn: float):
        self._spheroid = spheroid
        if abs(phi0 - pi / 2.) < 1e-9:
            self._aspect = Epsg1027._Aspect.NORTH_POLE
        elif abs(phi0 + pi / 2.) < 1e-9:
            self._aspect = Epsg1027._Aspect.SOUTH_POLE
        else:
            self._aspect = Epsg1027._Aspect.OBLIQUE
        self._r = spheroid.r()
        self._phi0 = phi0
        self._lambda0 = lambda0
        self._fe = fe
        self._fn = fn

    @override
    def compute(self, i):
        phi = i[Epsg1027._PHI]
        r_lambda = i[Epsg1027._LAMBDA] - self._lambda0

        if self._aspect == Epsg1027._Aspect.OBLIQUE:

            rkp = self._r * sqrt(2. / (1. + sin(self._phi0)
                                       * sin(phi) + cos(self._phi0) * cos(phi) * cos(r_lambda)))

            return self._fe + rkp * cos(phi) * sin(r_lambda), \
                self._fn + rkp * (cos(self._phi0) * sin(phi) - sin(self._phi0) * cos(phi) * cos(r_lambda))

        north = self._aspect == Epsg1027._Aspect.NORTH_POLE

        return (self._fe + 2. * self._r * sin(r_lambda)
                * (sin(pi / 4. - phi / 2.) if north else cos(pi / 4. - phi / 2.))), \
            (self._fn + 2. * self._r * cos(r_lambda)
             * (-sin(pi / 4. - phi / 2.) if north else cos(pi / 4. - phi / 2.)))

    @override
    def inverse(self, i):
        easting = i[Epsg1027._EASTING]
        northing = i[Epsg1027._NORTHING]

        east = easting - self._fe
        north = northing - self._fn
        rho = sqrt(east * east + north * north)

        if rho < 1e-9:
            return self._phi0, self._lambda0

        c = 2. * asin(rho / (2. * self._r))
        sinc = sin(c)
        cosc = cos(c)
        phi = asin(cosc * sin(self._phi0) + north * sinc * cos(self._phi0) / rho)

        match self._aspect:
            case Epsg1027._Aspect.NORTH_POLE:
                return phi, self._lambda0 + atan2(easting - self._fe, self._fn - northing)
            case Epsg1027._Aspect.SOUTH_POLE:
                return phi, self._lambda0 + atan2(easting - self._fe, northing - self._fn)
            case Epsg1027._Aspect.OBLIQUE:
                return phi, \
                    self._lambda0 + atan2(east * sinc, rho * cos(self._phi0) * cosc - north * sin(self._phi0) * sinc)
