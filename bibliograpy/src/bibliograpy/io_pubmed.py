"""Pubmed I/O module."""

import json

from typing import TextIO

import yaml

from bibliograpy.api_core import InputFormat, OutputFormat, Format, Formats
from bibliograpy.api_mesh import MeshPublicationType
from bibliograpy.api_pubmed import Tags

class PubmedInputFormat(InputFormat):
    """Ris 2001 input format implementation."""

    def __init__(self, source: Format):
        super().__init__(source=source, standard=Formats.PUBMED)

    def from_yml(self, i: TextIO):
        """Reads from yml representation."""
        return [{Tags.parse(k): MeshPublicationType.parse(e[k]) if Tags.parse(k) is Tags.PT else e[k] for k in e}
                for e in yaml.safe_load(i)]

    def from_json(self, i: TextIO):
        """Reads from json representation."""
        return [{Tags.parse(k): MeshPublicationType.parse(e[k]) if Tags.parse(k) is Tags.PT else e[k] for k in e}
                for e in json.load(i)]

    def from_standard(self, i: TextIO) -> list[dict[Tags, str | list[str] | MeshPublicationType]]:
        """Reads from standard format."""

        results: list[dict[Tags, str | list[str] | MeshPublicationType]] = []

        while True:
            entry: dict[Tags, str | list[str] | MeshPublicationType] | None = _read_pubmed_entry(i)
            if entry is None:
                return results
            if len(entry) == 0:
                continue
            results.append(entry)
        return results

def _read_pubmed_entry(tio: TextIO) -> dict[Tags, str | list[str] | MeshPublicationType] | None:
    """Reads a single Pubmed entry from the input stream.
    Args:
        tio (TextIO): the input text stream

    Return:
        (dict[Tags, str | list[str] | MeshPublicationType] | None): a pubmed entry as a dictionary, an empty dictionary
        is returned if the first potential entry line is empty, None is returned if the end of input stream is reached
    """

    result = None

    last_tag: Tags | None = None

    while line := tio.readline():

        # init the result dictionary inside the loop to return None if the end of the stream has been previously reached
        if result is None:
            result = {}

        # An empty line interrupts the entry reading.
        # Thus, if the first potential entry line is empty, en empty dictionary is returned
        if line.rstrip() == '':
            return result

        try:
            tag = Tags.parse(line[:4].rstrip())
            last_tag = tag

            if tag is Tags.PT:
                if tag in result:
                    result[tag].append(MeshPublicationType.parse(line[6:].rstrip()))
                else:
                    result[tag] = [MeshPublicationType.parse(line[6:].rstrip())]
                continue

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

            # long field support
            if last_tag.repeating:
                result[last_tag][-1] += line.rstrip('\n\r')
            else:
                result[last_tag] += line.rstrip('\n\r')

    return result


class PubmedOutputFormat(OutputFormat):
    """Pubmed format implementation."""

    def __init__(self,
                 content: list[dict[Tags, str | list[str] | MeshPublicationType]],
                 target: Format):
        super().__init__(target=target, standard=Formats.PUBMED)
        self._content = content

    def to_yml(self, o: TextIO):
        """Writes to yml representation."""
        yaml.dump([{k.name: (e[k].name if isinstance(e[k], MeshPublicationType) else e[k]) for k in e}
                   for e in self._content],
                  o,
                  sort_keys=False)

    def to_json(self, o: TextIO):
        """Writes to json representation."""
        json.dump([{k.name: (e[k].name if isinstance(e[k], MeshPublicationType) else e[k]) for k in e}
                   for e in self._content],
                  fp=o,
                  sort_keys=False)

    def to_standard(self, o: TextIO):
        """Writes to standard format."""

        for bib_entry in self._content:
            o.write(f'{Tags.PT.name}  - {bib_entry[Tags.PT].name}')
            o.write('\n')

            for tag in bib_entry:

                if tag is Tags.PT:
                    continue

                if tag.repeating:
                    for l in bib_entry[tag]:
                        o.write(f'{tag.name}  - {l}\n')
                else:
                    o.write(f'{tag.name}  - {bib_entry[tag]}\n')

    def to_py(self, o: TextIO):
        """Writes to python representation."""

        o.write('from bibliograpy.api_mesh import *\n')
        o.write('from bibliograpy.api_pubmed import *\n\n')
        o.write('\n')

        for bib_entry in self._content:
            key = bib_entry[Tags.PMID].upper()
            if not key[0].isalpha():
                key = 'PUBMED_' + key
            o.write(f'{key} = ')
            o.write('{\n')
            for e in bib_entry:
                if e is Tags.PT:
                    o.write(f"  Tags.{e.name}: [")
                    for i in bib_entry[e]:
                        o.write(f"MeshPublicationType.{i.name}, ")
                    o.write("],\n")
                elif e.repeating:
                    o.write(f"  Tags.{e.name}: {bib_entry[e]},\n")
                else:
                    o.write(f"  Tags.{e.name}: '{bib_entry[e]}',\n")
            o.write('}\n')
