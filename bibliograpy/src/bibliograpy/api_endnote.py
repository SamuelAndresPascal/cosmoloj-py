"""
endnote specification model.
"""
from dataclasses import dataclass
from enum import Enum, auto

from bibliograpy.bibliography import REFER_MAN
from bibliograpy.api_bibtex import _cite


@dataclass(frozen=True)
class Tag:
    """A field tag."""
    auto: auto
    _name: str | None = None
    repeating: bool = False

class Tags(Tag, Enum):
    """
    REFER fields.
    """

    ZERO = (auto(), '0')
    """the entry type"""

    T = (auto())

    A = (auto(), None, True)
    """author"""

    J = (auto())
    """journal title"""

    V = (auto())
    """volume number"""

    N = (auto())
    """issue number"""

    P = (auto())
    """page"""

    AT = (auto(), '@')
    """identification number (ISSN)"""

    D = (auto())
    """date"""

    I = (auto())
    """editor"""

    def name(self):
        return self._name if self._name is not None else self.name

    @staticmethod
    def parse(tag_str: str):
        """Parses a tag name into an enum value."""
        for n in Tags:
            if tag_str in (n.name, "%" + n.name):
                return n
        raise ValueError(f'unknown {tag_str} tag')

def default_endnote_formatter(r: dict[Tags, str | list[str]]):
    """The default formatter for endnote references."""
    title = r[Tags.T] if Tags.T in r else ""
    return f"{title} [{r[Tags.L]}]" if Tags.L in r else title
