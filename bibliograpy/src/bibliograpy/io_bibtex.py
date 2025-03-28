"""Bibtex I/O module."""

import json

from typing import Any, TextIO

import bibtexparser
import yaml
from bibtexparser.bibdatabase import BibDatabase
from bibtexparser.bwriter import BibTexWriter

from bibliograpy.api_bibtex import TYPES, BibtexReference


def read(s, extension: str) -> list[dict]:
    """Reads the input bibliography file content."""

    if extension == 'yml':
        return yaml.safe_load(s)

    if extension == 'json':
        return json.load(s)

    if extension == 'bib':
        meta = {}
        content = []
        for e in bibtexparser.load(s).entries:
            meta['entry_type'] = e['ENTRYTYPE']
            meta[BibtexReference.CITE_KEY_FIELD] = e['ID']
            del e['ENTRYTYPE']
            del e['ID']
            content.append({**meta, **e})
        return content

    raise ValueError(f'unsupported configuration format {extension}')

def write(o: TextIO, extension: str, content: list[dict], scope_symbol: str | None, init_scope: str | None):
    """Writes the bibliography in the format specified by the provided extension."""

    if extension == 'py':

        scope: dict[str, Any] = {}

        o.write('from bibliograpy.api_bibtex import *\n')
        o.write('\n')

        if init_scope is not None:
            o.write(f'{init_scope}\n')
            o.write('\n')

        for ref in content:
            if ref['entry_type'] in TYPES:
                o.write(f"{TYPES[ref['entry_type']].from_dict(ref, scope).to_py(scope_symbol=scope_symbol)}\n")
    elif extension in ['yml', 'yaml']:
        yaml.dump(content, o, sort_keys=False)
    elif extension in ['bib']:
        scope: dict[str, Any] = {}
        entries = []
        for ref in content:
            if ref['entry_type'] in TYPES:
                entries.append(TYPES[ref['entry_type']].from_dict(ref, scope).to_bib())
        db = BibDatabase()
        db.entries = entries
        writer = BibTexWriter()
        writer.order_entries_by = None
        bibtexparser.dump(bib_database=db, bibtex_file=o, writer=writer)
    elif extension in ['json']:
        json.dump(content, fp=o, sort_keys=False)
