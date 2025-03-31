"""RIS I/O module."""

import json

from typing import TextIO

import yaml

from bibliograpy.api_core import InputFormat, OutputFormat, Format, Formats
from bibliograpy.api_ris2001 import read_ris_entries, Tags, TypeFieldName

class Ris2001InputFormat(InputFormat):
    """Ris 2001 input format implementation."""

    def __init__(self, source: Format):
        super().__init__(source=source, standard=Formats.RIS2001)

    def from_yml(self, i: TextIO):
        """Reads from yml representation."""
        return [{Tags.parse(k): TypeFieldName.parse(e[k]) if k is Tags.TY else e[k] for k in e}
                for e in yaml.safe_load(i)]

    def from_json(self, i: TextIO):
        """Reads from json representation."""
        return [{Tags.parse(k): TypeFieldName.parse(e[k]) if k is Tags.TY else e[k] for k in e}
                for e in json.load(i)]

    def from_standard(self, i: TextIO):
        """Reads from standard format."""
        return read_ris_entries(tio=i)

    def _from_standard_ext(self) -> list[str]:
        """Extensions to be deserialized from standard format."""
        return ['ris2001', 'ris']

class Ris2001OutputFormat(OutputFormat):
    """Bibtex format implementation."""

    def __init__(self,
                 content: list[dict],
                 target: Format):
        super().__init__(target=target, standard=Formats.RIS2001)
        self._content = content

    def to_yml(self, o: TextIO):
        """Writes to yml representation."""
        yaml.dump([{k.name: (e[k].name if isinstance(e[k], TypeFieldName) else e[k]) for k in e}
                   for e in self._content],
                  o,
                  sort_keys=False)

    def to_json(self, o: TextIO):
        """Writes to json representation."""
        json.dump([{k.name: (e[k].name if isinstance(e[k], TypeFieldName) else e[k]) for k in e}
                   for e in self._content],
                  fp=o,
                  sort_keys=False)

    def to_standard(self, o: TextIO):
        """Writes to standard format."""

        for bib_entry in self._content:
            o.write(f'{Tags.TY}  - {bib_entry[Tags.TY]}')
            o.write('\n')

            for tag in bib_entry:

                if tag is Tags.TY:
                    continue

                if tag.value.repeating:
                    for l in bib_entry[tag]:
                        o.write(f'{tag}  - {l}')
                        o.write('\n')
                else:
                    o.write(f'{tag}  - {bib_entry[tag]}')
                    o.write('\n')

            o.write(f'{Tags.ER}  - ')
            o.write('\n')

    def to_py(self, o: TextIO):
        """Writes to python representation."""

        o.write('from bibliograpy.api_ris2001 import *\n')
        o.write('\n')

        for bib_entry in self._content:
            o.write(f'{bib_entry[Tags.ID].upper()} = ')
            o.write('{')
            o.write('\n')
            for e in bib_entry:
                if e is Tags.TY:
                    o.write(f"  Tags.{e.name}: TypeFieldName.{bib_entry[e]},")
                else:
                    o.write(f"  Tags.{e.name}: '{bib_entry[e]}',")
                o.write('\n')
            o.write('}')
            o.write('\n')
