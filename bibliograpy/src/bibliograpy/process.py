"""
bibliograpy process module
"""
import json
import logging
from argparse import Namespace
from pathlib import Path
from typing import Any

import bibtexparser
import yaml
from bibtexparser.bibdatabase import BibDatabase

from bibliograpy.api import TYPES

LOG = logging.getLogger(__name__)


def _process(ns: Namespace):
    """config
    """
    LOG.info("dependencies")

    in_extension = ns.file.split('.')[-1]
    output_dir = Path(Path.cwd(), ns.output)
    output_file = ns.output_file
    out_extension = output_file.split('.')[-1]

    LOG.info('open configuration file %s', ns.file)
    with open(ns.file, encoding=ns.encoding) as s:

        if in_extension == 'yml':
            content = yaml.safe_load(s)
        elif in_extension == 'json':
            content = json.load(s)
        elif in_extension == 'bib':
            content = bibtexparser.load(s)
        else:
            raise ValueError(f'unsupported configuration format {in_extension}')

        with open(Path(output_dir, output_file), 'w', encoding=ns.encoding) as o:
            if out_extension == 'py':

                scope: dict[str, Any] = {}

                o.write('from bibliograpy.api import *\n')
                o.write('\n')
                for ref in content:
                    if ref['entry_type'] in TYPES:
                        o.write(f"{TYPES[ref['entry_type']].from_dict(ref, scope).to_py()}\n")
            elif out_extension in ['yml', 'yaml']:
                yaml.dump(content, o, sort_keys=False)
            elif out_extension in ['bib']:
                scope: dict[str, Any] = {}
                entries = []
                for ref in content:
                    if ref['entry_type'] in TYPES:
                        entries.append(TYPES[ref['entry_type']].from_dict(ref, scope).to_bib())
                db = BibDatabase()
                db.entries = entries
                bibtexparser.dump(db, o)
