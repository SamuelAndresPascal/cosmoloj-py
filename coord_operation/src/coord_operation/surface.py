"""
The module define the surface types in usage in geomatics and geodesy.
"""


from enum import Enum, auto
from typing import override

from math import sqrt


class Surface:
    """An abstract type of surfaces."""

    def semi_major_axis(self) -> float:
        """An abstract method to return the semi-major axis value for all surface kinds."""


class Parameter(Enum):
    """An enum to specify the way an ellipsoid is defined. It refers to the semantics of the second parameter given
    along with the semi-major axis.
    """
    SEMI_MINOR_AXIS = auto()
    INVERSE_FLATTENING = auto()
    FLATTENING = auto()
    ECCENTRICITY = auto()


class Ellipsoid(Surface):
    """An ellipsoidal surface defined by two axis lengths. The first one is given by the semi-major axis parameter. The
    second one can be either directly defined using a semi-minor axis parameter or indirectly defined by the mean of
    eccentricity, inverse flattening or flattening which allow to compute the semi-minor axis value from the semi-major
    one."""

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

    def a(self) -> float:
        """The semi-major axis value."""
        return self._a

    @override
    def semi_major_axis(self) -> float:
        return self.a()

    @staticmethod
    def of_eccentricity(a: float, eccentricity: float):
        """Builds an ellipsoid from the semi-major axis and eccentricity values.
        Args:
            a (float): semi-major axis
            eccentricity (float): eccentricity

        Return (Ellipsoid)
        """
        return Ellipsoid(a=a, second_parameter=eccentricity, p=Parameter.ECCENTRICITY)


class Spheroid(Surface):
    """A spheroid can be seen as a particular ellipsoid for which the semi-major axis and the semi-minor axis are equal.
    """

    def __init__(self, r: float):
        self._r = r

    def r(self) -> float:
        """
        Return (float): the sphere radius
        """
        return self._r

    @override
    def semi_major_axis(self) -> float:
        return self.r()

    @staticmethod
    def of_radius(r: float):
        """Build a spheroid for a given radius.
        Args:
            r (float): the sphere radius

        Return (Spheroid)
        """
        return Spheroid(r=r)

    @staticmethod
    def unit():
        """
        Return (Spheroid): the unit sphere instance
        """
        return _UNIT


_UNIT = Spheroid.of_radius(1)
