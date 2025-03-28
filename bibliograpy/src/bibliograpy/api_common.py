from bibliograpy.api_bibtex import BibtexReference, default_bibtex_formatter
from bibliograpy.api_core import CitationFormatter
from bibliograpy.api_ris2001 import Tags as Ris2001, TypeFieldName as Ris2001Field, default_ris2001_formatter


class DefaultCitationFormatter(CitationFormatter):

    def __init__(self, prefix: str, itemize: str):
        self._prefix = prefix
        self._itemize = itemize

    def format(self, refs: list) -> str:

        if len(refs) == 1:
            return f"\n\n{self._prefix} {self._by_type(refs[0])}\n"

        result = f"\n\n{self._prefix}\n\n"
        for r in refs:
            result += f"{self._itemize} {self._by_type(r)}\n"
        return result

    def _by_type(self, r):
        if isinstance(r, BibtexReference):
            return self.bibtex(r)
        elif isinstance(r, dict):
            if Ris2001.TY in r:
                return self.ris2001(r)
        raise ValueError('unexpected reference type')

    def bibtex(self, r: BibtexReference):
        return default_bibtex_formatter(r)

    def ris2001(self, r: dict[Ris2001, str | list[str] | Ris2001Field]):
        return default_ris2001_formatter(r)

cite = DefaultCitationFormatter(prefix='Bibliography:', itemize='*')
