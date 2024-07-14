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

    def __init__(self, surface: Surface, lambda0: float, fe: float, fn: float):
        self._surface = surface
        self._a = surface.semi_major_axis()
        self._lambda0 = lambda0
        self._fe = fe
        self._fn = fn

    @override
    def get_surface(self) -> Surface:
        return self._surface

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
    def get_surface(self) -> Spheroid:
        return self._spheroid

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
    """Abstract EPSG::1028 projection."""

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
        self._f1 = 3. / 2. + n2 * (-27. / 32. + n2 * (269. / 512. - n2 * 6607 / 24576))
        self._f2 = 21. / 16. + n2 * (-55. / 32. + n2 * 6759. / 4096.)
        self._f3 = 151. / 96. + n2 * (-417. / 128 + n2 * 87963. / 20480.)
        self._f4 = 1097. / 512. - n2 * 15543. / 2560.
        self._f5 = 8011. / 2560. - n2 * 69119. / 6144.
        self._f6 = 293393. / 61440.
        self._f7 = 6845701. / 860160.

    @override
    def get_surface(self) -> Ellipsoid:
        return self._ellipsoid

    def m(self, phi: float) -> float:
        """m"""

    @override
    def compute(self, i):
        return self._fe + self._nu1 * cos(self._phi1) * (i[Epsg1028._LAMBDA] - self._lambda0), \
            self._fn + self.m(i[Epsg1028._PHI])

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
    """EPSG::1028 implementation using series."""

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
    """EPSG::1028 implementation using elliptic integral of the 2d kind."""

    @override
    def m(self, phi: float) -> float:
        return self._a * (sum_function(lambda p: sqrt(1. - self._e2 * sin(p) * sin(p)),
                                       start=0.,
                                       end=phi,
                                       parts=floor(4. * degrees(phi)) + 1)
                          - self._e2 * sin(phi) * cos(phi) / self.get_surface().e_sin_sqrt(phi))


class Epsg1028Integration3rdKind(Epsg1028):
    """EPSG::1028 implementation using elliptic integral of the 3rd kind."""

    @override
    def m(self, phi: float) -> float:
        return self._a * (1 - self._e2) * (sum_function(lambda p: pow(1. - self._e2 * sin(p) * sin(p), -3. / 2.),
                                                        start=0.,
                                                        end=phi,
                                                        parts=floor(50. * degrees(phi)) + 1))


class Epsg1029(InvertibleProjection[Surface]):
    """EPSG::1029

    Equidistant Cylindrical (Spherical)

    See method code 1028 for ellipsoidal development. If the latitude of natural origin is at the equator, also known as
    Plate Carrée. See also Pseudo Plate Carree, method code 9825.
    """

    _PHI = 0
    _LAMBDA = 1
    _EASTING = 0
    _NORTHING = 1

    def __init__(self, surface: Surface, phi1: float, lambda0: float, fe: float, fn: float):
        self._surface = surface
        self._phi1 = phi1
        self._lambda0 = lambda0
        self._fe = fe
        self._fn = fn

        if isinstance(surface, Spheroid):
            self._r = surface.r()
        elif isinstance(surface, Ellipsoid):
            self._r = surface.rc(phi1)
        else:
            raise ValueError

    @override
    def compute(self, i):
        return (self._fe + self._r * (i[Epsg1029._LAMBDA] - self._lambda0) * cos(self._phi1),
                self._fn + self._r * i[Epsg1029._PHI])

    @override
    def inverse(self, i):
        return ((i[Epsg1029._NORTHING] - self._fn) / self._r,
                self._lambda0 + (i[Epsg1029._EASTING] - self._fe) / self._r / cos(self._phi1))

    @override
    def get_surface(self):
        return self._surface


class Epsg9819a(InvertibleProjection[Ellipsoid]):
    """EPSG:9819

    Krovak
    """

    _PHI = 0
    _LAMBDA = 1
    _EASTING = 0
    _NORTHING = 1
    _PRECISION = 1e-12

    def __init__(self,
                 ellipsoid: Ellipsoid,
                 phic: float,
                 lambda0: float,
                 alphac: float,
                 phip: float,
                 kp: float,
                 fe: float,
                 fn: float):
        self._ellipsoid = ellipsoid
        self._a = ellipsoid.a()
        self._e = ellipsoid.e()
        self._phic = phic
        self._lambda0 = lambda0
        self._alphac = alphac
        self._phip = phip
        self._kp = kp
        self._fe = fe
        self._fn = fn

        self._e2 = self._e ** 2
        self._coef_a = self._compute_a()
        self._coef_b = self._compute_b()
        self._g0 = self._compute_g0()
        self._t0 = self._compute_t0()
        self._n = self._compute_n()
        self._r0 = self._compute_r0()

    @override
    def get_surface(self) -> Ellipsoid:
        return self._ellipsoid

    @override
    def compute(self, i):
        u = self._compute_u(i[Epsg9819a._PHI])
        v = self._compute_v(i[Epsg9819a._LAMBDA])
        t = self._compute_t(u, v)
        r = self._r(u, v, t)
        theta = self._theta(u, v, t)
        return r * cos(theta) + self._fn, r * sin(theta) + self._fe

    @override
    def inverse(self, i):
        i_xp = self._compute_inv_xp(i[Epsg9819a._EASTING])
        i_yp = self._compute_inv_yp(i[Epsg9819a._NORTHING])
        i_t = self._compute_inv_t(i_xp, i_yp)
        i_d = self._compute_inv_d(i_xp, i_yp)
        i_u = self._compute_inv_u(i_t, i_d)
        return self.__phi(i_u), self.__lambda(i_t, i_d, i_u)

    def _compute_a(self) -> float:
        return self._a * sqrt(1. - self._e2) / (1. - self._e2 * sin(self._phic) ** 2)

    def _compute_b(self) -> float:
        return sqrt(1. + self._e2 * cos(self._phic) ** 4 / (1 - self._e2))

    def _compute_u(self, f: float) -> float:
        esinf = self._e * sin(f)
        return 2. * (atan2(self._t0 * pow(tan(f / 2. + pi / 4.), self._coef_b),
                           pow((1. + esinf) / (1. - esinf), self._e * self._coef_b / 2.)) - pi / 4.)

    def _compute_v(self, l: float) -> float:
        return self._coef_b * (self._lambda0 - l)

    def _compute_t(self, u: float, v: float) -> float:
        return asin(cos(self._alphac) * sin(u) + sin(self._alphac) * cos(u) * cos(v))

    def _compute_d(self, u: float, v: float, t: float) -> float:
        return asin(cos(u) * sin(v) / cos(t))

    def _theta(self, u: float, v: float, t: float) -> float:
        return self._n * self._compute_d(u, v, t)

    def _r(self, u: float, v: float, t: float) -> float:
        return self._r0 * pow(tan(pi / 4. + self._phip / 2.) / tan(t / 2. + pi / 4.), self._n)

    def _compute_g0(self) -> float:
        return asin(sin(self._phic) / self._coef_b)

    def _compute_t0(self) -> float:
        sinphic = sin(self._phic)
        return tan(pi / 4. + self._g0 / 2.) \
            * pow((1. + self._e * sinphic) / (1. - self._e * sinphic), self._e * self._coef_b / 2.) \
            / pow(tan(pi / 4. + self._phic / 2.), self._coef_b)

    def _compute_n(self) -> float:
        return sin(self._phip)

    def _compute_r0(self) -> float:
        return self._kp * self._coef_a / tan(self._phip)

    def __lambda(self, i_t: float, i_d: float, i_u: float) -> float:
        return self._lambda0 - self._compute_inv_v(i_t, i_d, i_u) / self._coef_b

    def __phi(self, i_u: float) -> float:
        phi = i_u

        while True:
            tmp = self.___phi(i_u, phi)
            if abs(tmp - phi) > Epsg9819a._PRECISION:
                phi = tmp
            else:
                return tmp

    def ___phi(self, i_u: float, phi: float) -> float:
        esinphi = self._e * sin(phi)
        return 2 * (atan(pow(tan(i_u / 2. + pi / 4.) / self._t0, 1. / self._coef_b)
                * pow((1. + esinphi) / (1. - esinphi), self._e / 2.)) - pi / 4.)

    def _compute_inv_xp(self, southing: float) -> float:
        return southing - self._fn

    def _compute_inv_yp(self, westing: float) -> float:
        return westing - self._fe

    def _compute_inv_r(self, i_xp: float, i_yp: float) -> float:
        return sqrt(i_xp ** 2 + i_yp ** 2)

    def _compute_inv_theta(self, i_xp: float, i_yp: float) -> float:
        return atan2(i_yp, i_xp)

    def _compute_inv_d(self, i_xp: float, i_yp: float) -> float:
        return self._compute_inv_theta(i_xp, i_yp) / sin(self._phip)

    def _compute_inv_t(self, i_xp: float, i_yp: float) -> float:
        return 2. * (atan(pow(self._r0 / self._compute_inv_r(i_xp, i_yp),
                              1. / self._n) * tan(pi / 4. + self._phip / 2.)) - pi / 4.)

    def _compute_inv_u(self, i_t: float, i_d: float) -> float:
        return asin(cos(self._alphac) * sin(i_t) - sin(self._alphac) * cos(i_t) *  cos(i_d))

    def _compute_inv_v(self, i_t: float, i_d: float, i_u: float) -> float:
        return asin(cos(i_t) * sin(i_d) / cos(i_u))
