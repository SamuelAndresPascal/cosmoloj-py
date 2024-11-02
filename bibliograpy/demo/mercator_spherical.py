from math import cos, atan, pi, log, tan, exp

from bibliograpy.api import reference

import cosmoloj_bib as bib


@reference(bib.MAP_PROJECTIONS)
class MercatorSpherical:
    """The mercator spherical projection as defined in Map Projections."""

    _LATITUDE: int = 0
    _LONGITUDE: int = 1
    _X: int = 0
    _Y: int = 1

    def __init__(self, radius: float, phi0: float, lambda0: float):
        self._r = radius
        self._phi0 = phi0
        self._cos_phi1 = cos(phi0)
        self._lambda0 = lambda0

    def compute(self, i):
        return x_7_1(self._r, self._cos_phi1, self._lambda0, i[MercatorSpherical._LONGITUDE]), \
               y_7_2(self._r, self._cos_phi1, i[MercatorSpherical._LATITUDE])

    def inverse(self, i):
        return phi_7_4(self._r, self._cos_phi1, i[MercatorSpherical._Y]), \
               lambda_7_5(self._r, self._cos_phi1, self._lambda0, i[MercatorSpherical._X])

@reference(bib.MAP_PROJECTIONS)
def x_7_1(radius: float, cos_phi1: float, lambda0: float, lon: float) -> float:
    """formula 7-1"""
    return radius * (lon - lambda0) * cos_phi1

@reference(bib.MAP_PROJECTIONS)
def y_7_2(radius: float, cos_phi1: float, lat: float) -> float:
    """formula 7-2"""
    return radius * log(tan(pi / 4. + lat / 2.)) * cos_phi1

@reference(bib.MAP_PROJECTIONS)
def phi_7_4(radius: float, cos_phi1: float, y: float) -> float:
    """formula 7-4"""
    return (pi / 2. - 2 * atan(exp(-y / radius))) / cos_phi1

@reference(bib.MAP_PROJECTIONS, chapter='7')
def lambda_7_5(radius: float, cos_phi1: float, lambda0: float, x: float) -> float:
    """formula 7-5"""
    return (x / radius + lambda0) / cos_phi1
