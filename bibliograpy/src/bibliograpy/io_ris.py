"""RIS I/O module."""

import json

from typing import TextIO

import yaml

from bibliograpy.api_ris2001 import read_ris_entries, Tags, TypeFieldName


def read(s, extension: str) -> list[dict]:
    """Reads the input bibliography file content."""

    if extension == 'yml':
        return [{Tags.parse(k): TypeFieldName.parse(e[k]) if k is Tags.TY else e[k] for k in e}
                for e in yaml.safe_load(s)]

    if extension == 'json':
        return [{Tags.parse(k): TypeFieldName.parse(e[k]) if k is Tags.TY else e[k] for k in e} for e in json.load(s)]

    if extension == 'ris':
        return read_ris_entries(tio=s)

    raise ValueError(f'unsupported configuration format {extension}')

def _write_py(o: TextIO, content: list[dict]):
    """Writes the bibliography content in a RIS 2001 python script."""
    o.write('from bibliograpy.api_ris2001 import *\n')
    o.write('\n')

    for bib_entry in content:
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

def _write_ris2001(o: TextIO, content: list[dict]):
    """Writes the bibliography content in the RIS 2001 format."""
    for bib_entry in content:
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


def write(o: TextIO, extension: str, content: list[dict]):
    """Writes the bibliography in the format specified by the provided extension."""

    if extension == 'py':
        _write_py(o, content)
    elif extension in ['yml', 'yaml']:
        yaml.dump([{k.name: (e[k].name if isinstance(e[k], TypeFieldName) else e[k]) for k in e} for e in content],
                  o,
                  sort_keys=False)
    elif extension in ['ris', 'ris2001', 'ris2011']:
        _write_ris2001(o, content)
    elif extension in ['json']:
        json.dump([{k.name: (e[k].name if isinstance(e[k], TypeFieldName) else e[k]) for k in e} for e in content],
                  fp=o,
                  sort_keys=False)
