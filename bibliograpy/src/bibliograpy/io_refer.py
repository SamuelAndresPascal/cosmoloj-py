"""refer I/O module."""

import json

from typing import TextIO

import yaml

from bibliograpy.api_core import InputFormat, OutputFormat, Format, Formats
from bibliograpy.api_refer import Tags

class ReferInputFormat(InputFormat):
    """refer input format implementation."""

    def __init__(self, source: Format):
        super().__init__(source=source, standard=Formats.RIS2001)

    def from_yml(self, i: TextIO):
        """Reads from yml representation."""
        return [{Tags.parse(k): e[k] for k in e} for e in yaml.safe_load(i)]

    def from_json(self, i: TextIO):
        """Reads from json representation."""
        return [{Tags.parse(k): e[k] for k in e} for e in json.load(i)]

    def from_standard(self, i: TextIO) -> list[dict[Tags, str | list[str]]]:
        """Reads from standard format."""

        results: list[dict[Tags, str | list[str]]] = []

        while line := i.readline():
            if line.rstrip() == '':
                continue
            entry: dict[Tags, str | list[str]] = {}
            entry.update(_read_ris_entry(i))
            results.append(entry)
        return results

def _read_ris_entry(tio: TextIO) -> dict[Tags, str | list[str]]:
    """Reads a single RIS entry from the input stream."""

    result = {}

    last_tag: Tags | None = None

    while line := tio.readline():

        if len(line.strip()) == 0:
            if result:
                return result
            else:
                continue

        try:
            tag = Tags.parse(line[:2])
            last_tag = tag

            if tag.repeating:
                if tag in result:
                    result[tag].append(line[6:].rstrip('\n\r'))
                else:
                    result[tag] = [line[6:].rstrip('\n\r')]
            else:
                result[tag] = line[6:].rstrip('\n\r')
        except ValueError as e:
            if line[2:6] == '  - ' or last_tag is None:
                raise e

    return result


class ReferOutputFormat(OutputFormat):
    """Bibtex format implementation."""

    def __init__(self,
                 content: list[dict],
                 target: Format):
        super().__init__(target=target, standard=Formats.RIS2001)
        self._content = content

    def to_yml(self, o: TextIO):
        """Writes to yml representation."""
        yaml.dump([{k.name: e[k] for k in e} for e in self._content],
                  o,
                  sort_keys=False)

    def to_json(self, o: TextIO):
        """Writes to json representation."""
        json.dump([{k.name: e[k] for k in e} for e in self._content],
                  fp=o,
                  sort_keys=False)

    def to_standard(self, o: TextIO):
        """Writes to standard format."""

        for bib_entry in self._content:

            for tag in bib_entry:

                if tag.repeating:
                    for l in bib_entry[tag]:
                        o.write(f'%{tag} {l}\n')
                else:
                    o.write(f'{tag}  - {bib_entry[tag]}\n')

            o.write('\n')

    def to_py(self, o: TextIO):
        """Writes to python representation."""

        o.write('from bibliograpy.api_refer import *\n\n')

        for bib_entry in self._content:
            o.write(f'{bib_entry[Tags.A][0].upper()} = ')
            o.write('{\n')
            for e in bib_entry:
                o.write(f"  Tags.{e.name}: '{bib_entry[e]}',\n")
            o.write('}\n')
