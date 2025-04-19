"""
bibliograpy process module
"""
import logging
from argparse import Namespace
from pathlib import Path

from bibliograpy.api_core import Formats
from bibliograpy.io_bibtex import BibtexInputFormat, BibtexOutputFormat
from bibliograpy.io_refer import ReferInputFormat, ReferOutputFormat
from bibliograpy.io_ris2001 import Ris2001InputFormat, Ris2001OutputFormat
from bibliograpy.io_ris2011 import Ris2011InputFormat, Ris2011OutputFormat
from bibliograpy.io_endnote import EndnoteInputFormat, EndnoteOutputFormat

LOG = logging.getLogger(__name__)


def _process(ns: Namespace):
    """config
    """
    LOG.info("dependencies")

    source = Formats.as_io_extension(ns.file.split('.')[-1])
    output_dir = Path(Path.cwd(), ns.output_dir)
    output_file = ns.output_file
    target = Formats.as_io_extension(output_file.split('.')[-1])
    if 'shared_scope' in ns and ns.shared_scope:
        scope_symbol = 'SHARED_SCOPE'
        init_scope = None
    else:
        scope_symbol = ns.scope if 'scope' in ns else None
        init_scope = ns.init_scope if 'init_scope' in ns else None
    fmt = Formats.as_command(ns.CMD)

    LOG.info('open configuration file %s', ns.file)

    if fmt is Formats.BIBTEX:
        _process_bibtex(ns=ns,
                        source=source,
                        target=target,
                        output=Path(output_dir, output_file),
                        scope_symbol=scope_symbol,
                        init_scope=init_scope)

    elif fmt is Formats.RIS2001:
        _process_ris2001(ns=ns,
                         source=source,
                         target=target,
                         output=Path(output_dir, output_file))

    elif fmt is Formats.RIS2011:
        _process_ris2011(ns=ns,
                         source=source,
                         target=target,
                         output=Path(output_dir, output_file))

    elif fmt is Formats.REFER:
        _process_refer(ns=ns,
                       source=source,
                       target=target,
                       output=Path(output_dir, output_file))

    elif fmt is Formats.ENDNOTE:
        _process_endnote(ns=ns,
                         source=source,
                         target=target,
                         output=Path(output_dir, output_file))
    else:
        raise ValueError(f'unsupported format {format}')


def _process_bibtex(ns: Namespace,
                    source: Formats,
                    target: Formats,
                    output: Path,
                    scope_symbol: str | None,
                    init_scope: str) -> None:
    """Bibtex processing."""
    iformat = BibtexInputFormat(source=source)
    with open(ns.file, encoding=ns.encoding) as i:
        content = iformat.read(i)
        oformat = BibtexOutputFormat(content=content,
                                     target=target,
                                     scope_symbol=scope_symbol,
                                     init_scope=init_scope)
        with open(output, 'w', encoding=ns.encoding) as o:
            oformat.write(o)

def _process_ris2001(ns: Namespace,
                     source: Formats,
                     target: Formats,
                     output: Path) -> None:
    """RIS 2001 processing."""
    iformat = Ris2001InputFormat(source=source)
    with open(ns.file, encoding=ns.encoding) as i:
        content = iformat.read(i)
        oformat = Ris2001OutputFormat(target=target, content=content)
        with open(output, 'w', encoding=ns.encoding) as o:
            oformat.write(o)

def _process_ris2011(ns: Namespace,
                     source: Formats,
                     target: Formats,
                     output: Path) -> None:
    """RIS 2011 processing."""
    iformat = Ris2011InputFormat(source=source)
    with open(ns.file, encoding=ns.encoding) as i:
        content = iformat.read(i)
        oformat = Ris2011OutputFormat(target=target, content=content)
        with open(output, 'w', encoding=ns.encoding) as o:
            oformat.write(o)

def _process_refer(ns: Namespace,
                     source: Formats,
                     target: Formats,
                     output: Path) -> None:
    """Refer processing."""
    iformat = ReferInputFormat(source=source)
    with open(ns.file, encoding=ns.encoding) as i:
        content = iformat.read(i)
        oformat = ReferOutputFormat(target=target, content=content)
        with open(output, 'w', encoding=ns.encoding) as o:
            oformat.write(o)

def _process_endnote(ns: Namespace,
                     source: Formats,
                     target: Formats,
                     output: Path) -> None:
    """Endnote processing."""
    iformat = EndnoteInputFormat(source=source)
    with open(ns.file, encoding=ns.encoding) as i:
        content = iformat.read(i)
        oformat = EndnoteOutputFormat(target=target, content=content)
        with open(output, 'w', encoding=ns.encoding) as o:
            oformat.write(o)
