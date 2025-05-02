"""Module documentation.

Documentation supplémentaire.
"""

from bibliograpy.api_common import cite, cite_hint, cite_module
from learning.bibliograpy.bibliography import ART00, ART01

# module bibliography
cite_module(ART00)

from enum import Enum
from dataclasses import dataclass


@cite(ART00, ART01)
@dataclass(frozen=True)
class MyType:
    """MyType dataclass documentation."""
    field1: cite_hint(str, ART01)


@cite(ART00, ART01)
class MyEnum(Enum):
    """MyEnum enum documentation."""
    INSTANCE1 = cite_hint('My instance', ART00)


A: cite_hint(int, ART00, ART01) = 0
"""An universal constant."""


@cite(ART00)
class Bar:
    """The Bar class."""


@cite(ART00, ART01)
def foo(a: int, b: int) -> int:
    """The foo function."""
    return a // b