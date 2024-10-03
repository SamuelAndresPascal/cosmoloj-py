"""Bibliograpy API module"""
from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass

@dataclass(frozen=True, repr=False)
class Reference:
    """A bibliography reference"""
    type: Callable
    key: str
    title: str
    ref: Reference | None = None

    def __str__(self):
        return self.key

def institution():
    """d"""

def tech_report():
    """e"""


def reference(ref: Reference):
    """The reference decorator."""
    def internal(obj):
        obj.__doc__ += "\n\nBibliography:\n\n" + str(ref)
        return obj

    return internal
