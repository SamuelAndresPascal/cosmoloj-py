"""
bibliograpy process module
"""
import logging
from argparse import Namespace
from enum import Enum
from pathlib import Path

from bibliograpy.io_bibtex import read as r_bib, write as w_bib
from bibliograpy.io_ris import read as r_ris2001, write as w_ris

LOG = logging.getLogger(__name__)

class Formats(Enum):
    """Supported bibliography formats."""
    BIBTEX = ['bib', 'bibtex']
    RIS2001 = ['ris2001']
    RIS2011 = ['ris2011', 'ris']

    @staticmethod
    def parse(format_id: str):
        """Gets a supported format enum instance from a supported process argument string."""
        for f in Formats:
            if format_id in f.value:
                return f
        raise ValueError(f'unexpected format {format_id}')


def _process(ns: Namespace):
    """config
    """
    LOG.info("dependencies")

    in_extension = ns.file.split('.')[-1]
    output_dir = Path(Path.cwd(), ns.output_dir)
    output_file = ns.output_file
    out_extension = output_file.split('.')[-1]
    scope_symbol = ns.scope if 'scope' in ns else None
    init_scope = ns.init_scope if 'init_scope' in ns else None
    fmt = Formats.parse(ns.format)

    LOG.info('open configuration file %s', ns.file)

    if fmt is Formats.BIBTEX:
        with open(ns.file, encoding=ns.encoding) as s:
            content = r_bib(s, extension=in_extension)

            with open(Path(output_dir, output_file), 'w', encoding=ns.encoding) as o:
                w_bib(o, extension=out_extension, content=content, scope_symbol=scope_symbol, init_scope=init_scope)
    elif fmt is Formats.RIS2001:
        with open(ns.file, encoding=ns.encoding) as s:
            content = r_ris2001(s, extension=in_extension)

            with open(Path(output_dir, output_file), 'w', encoding=ns.encoding) as o:
                w_ris(o, extension=out_extension, content=content)
    else:
        raise ValueError(f'unsupported format {format}')
