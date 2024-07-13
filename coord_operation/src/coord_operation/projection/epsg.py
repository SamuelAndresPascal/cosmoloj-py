"""The EPSG projection definitions."""
from enum import Enum, auto
from typing import override

from math import log, tan, pi, atan, exp, sqrt, sin, cos, asin, atan2, degrees, floor

from coord_operation.math_util.integral import sum_function
from coord_operation.operation import InvertibleProjection
from coord_operation.projection.mercator_spherical import MercatorSpherical
from coord_operation.surface import Surface, Spheroid, Ellipsoid


class Epsg1024(InvertibleProjection[Surface]):
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


class Epsg1027(InvertibleProjection[Spheroid]):
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


class Epsg1028(InvertibleProjection[Ellipsoid]):

    _PHI: int = 0
    _LAMBDA: int = 1
    _EASTING: int = 0
    _NORTHING: int = 1

    def __init__(self, ellipsoid: Ellipsoid, phi1: float, lambda0: float, fe: float, fn: float):
        self._ellipsoid = ellipsoid
        self._phi1 = phi1
        self._lambda0 = lambda0
        self._fe = fe
        self._fn = fn

        self._a = ellipsoid.a()
        self._e2 = ellipsoid.e2()
        self._nu1 = ellipsoid.nu(phi1)
        e2 = self._e2
        self._mud = self._a * (1.
                               - e2 * (1. / 4.
                                       + e2 * (3. / 64.
                                               + e2 * (5. / 256.
                                                       + e2 * (175. / 16384.
                                                               + e2 * (441. / 65536.
                                                                       + e2 * (4851. / 1048576.
                                                                               + e2 * 14157. / 4194304.)))))))
        self._n = (1. - sqrt(1. - e2)) / (1. + sqrt(1. - e2))

        n2 = self._n ** 2
        self._f1 = (3. / 2. + n2 * (-27. / 32. + n2 * (269. / 512. - n2 * 6607 / 24576)))
        self._f2 = 21. / 16. + n2 * (-55. / 32. + n2 * 6759. / 4096.)
        self._f3 = 151. / 96. + n2 * (-417. / 128 + n2 * 87963. / 20480.)
        self._f4 = 1097. / 512. - n2 * 15543. / 2560.
        self._f5 = 8011. / 2560. - n2 * 69119. / 6144.
        self._f6 = 293393. / 61440.
        self._f7 = 6845701. / 860160.

    @override
    def compute(self, i):
        return self._fe + self._nu1 * cos(self._phi1) * (i[Epsg1028._LAMBDA] - self._lambda0), \
            self._fn + self.m(i[Epsg1028._PHI])

    @override
    def get_surface(self) -> Ellipsoid:
        return self._ellipsoid

    def m(self, phi: float) -> float:
        """m"""

    @override
    def inverse(self, i):
        easting = i[Epsg1028._EASTING]
        northing = i[Epsg1028._NORTHING]

        x = easting - self._fe
        y = northing - self._fn

        mu = y / self._mud

        return self._f(mu), self._lambda0 + x / (self._nu1 * cos(self._phi1))

    def _f(self, m: float) -> float:
        n = self._n
        return m + n * (self._f1 * sin(2. * m)
                        + n * (self._f2 * sin(4. * m)
                               + n * (self._f3 * sin(6. * m)
                                      + n * (self._f4 * sin(8. * m)
                                             + n * (self._f5 * sin(10. * m)
                                                    + n * (self._f6 * sin(12. * m)
                                                           + n * self._f7 * sin(14. * m)))))))


class Epsg1028Series(Epsg1028):
    """EPSG::1028 implementation using series"""

    def __init__(self, ellipsoid: Ellipsoid, phi1: float, lambda0: float, fe: float, fn: float):
        super().__init__(ellipsoid, phi1, lambda0, fe, fn)

        e2 = self._e2
        self._m1 = (1.
                    - e2 * (1. / 4.
                            + e2 * (3. / 64.
                                    + e2 * (5. / 256.
                                            + e2 * (175. / 16384.
                                                    + e2 * (441. / 65536.
                                                            + e2 * (4851. / 1048576.
                                                                    + e2 * 14157. / 4194304.)))))))
        self._m2 = -(3. / 8.
                     + e2 * (3. / 32.
                             + e2 * (45. / 1024.
                                 + e2 * (105. / 4096.
                                     + e2 * (2205. / 131072.
                                             + e2 * (6237. / 524288.
                                                     + e2 * 297297. / 33554432.))))))
        self._m3 = (15. / 256.
                    + e2 * (45. / 1024.
                            + e2 * (525. / 16384.
                                    + e2 * (1575. / 65536.
                                            + e2 * (155925. / 8388608.
                                                    + e2 * 495495. / 33554432.)))))
        self._m4 = -(35. / 3072
                     + e2 * (175. / 12288.
                             + e2 * (3675. / 262144.
                                     + e2 * (13475. / 1048576.
                                             + e2 * 385385. / 33554432.))))
        self._m5 = 315. / 131072. + e2 * (2205. / 524288. + e2 * (43659. / 8388608. + e2 * 189189. / 33554432.))
        self._m6 = -(693. / 1310720. + e2 * (6237. / 5242880. + e2 * 297297. / 167772160.))
        self._m7 = 1001. / 8388608. + e2 * 11011. / 33554432.
        self._m8 = -6435. / 234881024

    @override
    def m(self, phi: float):
        e2 = self._e2
        return self._a * (self._m1 * phi
                          + e2 * (self._m2 * sin(2. * phi)
                                  + e2 * (self._m3 * sin(4. * phi)
                                          + e2 * (self._m4 * sin(6. * phi)
                                                  + e2 * (self._m5 * sin(8. * phi)
                                                          + e2 * (self._m6 * sin(10. * phi)
                                                                  + e2 * (self._m7 * sin(12. * phi)
                                                                          + e2 * self._m8 * sin(14. * phi))))))))


class Epsg1028Integration2dKind(Epsg1028):
    """EPSG::1028 implementation using elliptic integral of the 2d kind"""

    @override
    def m(self, phi: float) -> float:
        return self._a * (sum_function(lambda phi: sqrt(1. - self._e2 * sin(phi) * sin(phi)),
                                       start=0.,
                                       end=phi,
                                       parts=floor(4. * degrees(phi)) + 1)
                          - self._e2 * sin(phi) * cos(phi) / self.get_surface().e_sin_sqrt(phi))


class Epsg1028Integration3rdKind(Epsg1028):
    """EPSG::1028 implementation using elliptic integral of the 3rd kind"""

    @override
    def m(self, phi: float) -> float:
        return self._a * (1 - self._e2) * (sum_function(lambda phi: pow(1. - self._e2 * sin(phi) * sin(phi), -3. / 2.),
                                                        start=0.,
                                                        end=phi,
                                                        parts=floor(50. * degrees(phi)) + 1))
