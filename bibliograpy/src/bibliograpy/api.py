"""Bibliograpy API module."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Callable


@dataclass(frozen=True, repr=False)
class Reference:
    """A bibliography reference."""
    key: str
    title: str

    def __repr__(self):
        return f"{self.title} [{self.key}]"

@dataclass(frozen=True, repr=False)
class Institution(Reference):
    """A reference to an institution."""

@dataclass(frozen=True, repr=False)
class TechReport(Reference):
    """A reference to a tech report."""
    institution: Institution | None

@dataclass(frozen=True)
class ReferenceBuilder:
    reference_wrapper: Callable[[list[Reference]], str]

    @staticmethod
    def _default_lambda(refs: list[Reference]) -> str:
        if len(refs)==1:
            return f"\n\nBibliography: {refs[0]}\n"
        else:
            result = "\n\nBibliography:\n\n"
            for r in refs:
                result += f"* {r}\n"
            return result

    @staticmethod
    def default():
        return ReferenceBuilder(reference_wrapper=ReferenceBuilder._default_lambda)

    def __call__(self, *refs):
        """The reference decorator."""

        def internal(obj):
            if len(refs) == 1:
                ref0 = refs[0]
                if isinstance(ref0, Reference):
                    obj.__doc__ += self.reference_wrapper([ref0])
                elif isinstance(ref0, list):
                    obj.__doc__ += self.reference_wrapper(ref0)
            else:
                obj.__doc__ += self.reference_wrapper([*refs])
            return obj

        return internal

reference = ReferenceBuilder.default()