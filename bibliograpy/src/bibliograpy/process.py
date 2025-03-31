"""
bibliograpy process module
"""
import logging
from argparse import Namespace
from pathlib import Path

from bibliograpy.api_core import Formats
from bibliograpy.io_bibtex import BibtexInputFormat, BibtexOutputFormat
from bibliograpy.io_ris import Ris2001InputFormat, Ris2001OutputFormat

LOG = logging.getLogger(__name__)


def _process(ns: Namespace):
    """config
    """
    LOG.info("dependencies")

    source = Formats.as_io_extension(ns.file.split('.')[-1])
    output_dir = Path(Path.cwd(), ns.output_dir)
    output_file = ns.output_file
    target = Formats.as_io_extension(output_file.split('.')[-1])
    scope_symbol = ns.scope if 'scope' in ns else None
    init_scope = ns.init_scope if 'init_scope' in ns else None
    fmt = Formats.as_specification(ns.format)

    LOG.info('open configuration file %s', ns.file)

    if fmt is Formats.BIBTEX:
        iformat = BibtexInputFormat(source=source)
        with open(ns.file, encoding=ns.encoding) as i:
            content = iformat.read(i)
            oformat = BibtexOutputFormat(content=content,
                                         target=target,
                                         scope_symbol=scope_symbol,
                                         init_scope=init_scope)
            with open(Path(output_dir, output_file), 'w', encoding=ns.encoding) as o:
                oformat.write(o)
    elif fmt is Formats.RIS2001:
        iformat = Ris2001InputFormat(source=source)
        with open(ns.file, encoding=ns.encoding) as i:
            content = iformat.read(i)
            oformat = Ris2001OutputFormat(target=target, content=content)
            with open(Path(output_dir, output_file), 'w', encoding=ns.encoding) as o:
                oformat.write(o)
    else:
        raise ValueError(f'unsupported format {format}')
