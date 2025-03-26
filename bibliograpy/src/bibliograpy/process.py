"""
bibliograpy process module
"""
import logging
from argparse import Namespace
from pathlib import Path

from bibliograpy.io_bibtex import read, write

LOG = logging.getLogger(__name__)


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

    LOG.info('open configuration file %s', ns.file)
    with open(ns.file, encoding=ns.encoding) as s:
        content = read(s, extension=in_extension)

        with open(Path(output_dir, output_file), 'w', encoding=ns.encoding) as o:
            write(o, extension=out_extension, content=content, scope_symbol=scope_symbol, init_scope=init_scope)
