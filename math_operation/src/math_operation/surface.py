from enum import Enum, auto
from math import sqrt


class Surface:
    pass


class Parameter(Enum):
    SEMI_MINOR_AXIS = auto()
    INVERSE_FLATTENING = auto()
    FLATTENING = auto()
    ECCENTRICITY = auto()


class Ellipsoid(Surface):

    def __init__(self, a: float, second_parameter: float, p: Parameter):
        self._a = a
        match p:
            case Parameter.SEMI_MINOR_AXIS:
                self._b = second_parameter
                self._inverse_flattening = a / (a - self._b)
                self._f = 1. / self._inverse_flattening
                self._e = sqrt(self._f * (2. - self._f))
            case Parameter.ECCENTRICITY:
                self._e = second_parameter
                self._b = a * sqrt(1. - self._e * self._e)
                self._inverse_flattening = a / (a - self._b)
                self._f = 1. / self._inverse_flattening
            case _:
                raise AttributeError()

    def a(self):
        return self._a

    @staticmethod
    def of_eccentricity(a: float, eccentricity: float):
        return Ellipsoid(a=a, second_parameter=eccentricity, p=Parameter.ECCENTRICITY)


class Spheroid(Surface):


    def __init__(self, r: float):
        self._r = r

    def r(self):
        return self._r

    def to_ellipsoid(self):
        return

    @staticmethod
    def of_radius(r: float):
        return Spheroid(r=r)

    @staticmethod
    def unit():
        return _UNIT

_UNIT = Spheroid.of_radius(1)
