"""Bibliograpy API module"""
from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass


class ReferenceType:
    def __call__(self, *args, **kwargs):
        raise NotImplementedError

@dataclass(frozen=True, repr=False)
class Reference:
    type: Callable
    key: str
    title: str
    ref: Reference | None = None

    def __str__(self):
        return self.key

def institution():
    """d"""
    pass

def tech_report():
    """e"""
    pass



def reference(ref: Reference):
    def internal(obj):
        obj.__doc__ += "\n\nBibliography:\n\n" + str(ref)
        return obj

    return internal
