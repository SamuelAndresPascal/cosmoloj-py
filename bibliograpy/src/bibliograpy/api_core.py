"""Core management of reference decorators."""

class CitationFormatter:
    """A builder of reference decorators."""

    def format(self, refs: list) -> str:
        """Formats a citation list."""

    def __call__(self, *refs):
        """The reference decorator."""

        def internal(obj):
            if obj.__doc__ is None:
                obj.__doc__ = ''
            if len(refs) == 1:
                ref0 = refs[0]
                if isinstance(ref0, list):
                    obj.__doc__ += self.format(ref0)
                else:
                    obj.__doc__ += self.format([ref0])
            else:
                obj.__doc__ += self.format([*refs])
            return obj

        return internal


class SimpleCitationFormatter[R](CitationFormatter):
    """A simple citation formatter for """

    def __init__(self, prefix, itemize, reference_formatter):
        self._prefix = prefix
        self._itemize = itemize
        self._reference_formatter = reference_formatter

    def format(self, refs: list) -> str:

        if len(refs) == 1:
            return f"\n\n{self._prefix} {self._reference_formatter(refs[0])}\n"

        result = f"\n\n{self._prefix}\n\n"
        for r in refs:
            result += f"{self._itemize} {self._reference_formatter(r)}\n"
        return result
