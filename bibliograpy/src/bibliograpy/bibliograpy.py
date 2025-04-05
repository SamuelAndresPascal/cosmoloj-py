"""
bibliograpy command entrypoint
"""
import logging

from argparse import ArgumentParser, Namespace

from bibliograpy.process import _process

LOG = logging.getLogger(__name__)


DEFAULT_FILE = "bibliograpy.yaml"
DEFAULT_ENCODING = 'utf-8'
DEFAULT_OUTPUT_DIR = '.'
DEFAULT_OUTPUT_FILE = 'bibliography.py'
DEFAULT_FORMAT = 'bib'
DEFAULT_INIT_SCOPE = '{}'


def _create_parser() -> ArgumentParser:

    # parse argument line
    parser = ArgumentParser(description='Bibliography management.')

    subparsers = parser.add_subparsers(dest='CMD', help='available commands')

    bibtex = subparsers.add_parser(name='bibtex',
                                   help='generates bibliograpy Python source bibliography from Bibtex format')
    bibtex.add_argument('file',
                         nargs='?',
                         help="path to the input bibliography file",
                         default=DEFAULT_FILE)
    bibtex.add_argument('--encoding', '-e',
                         nargs='?',
                         help='the bibliograpy configuration file encoding (default to utf-8)',
                         default=DEFAULT_ENCODING)
    bibtex.add_argument('--output-dir', '-O',
                         nargs='?',
                         help='the source bibliograpy file output directory',
                         default=DEFAULT_OUTPUT_DIR)
    bibtex.add_argument('--output-file', '-o',
                         nargs='?',
                         help='the source bibliograpy output file name',
                         default=DEFAULT_OUTPUT_FILE)
    group = bibtex.add_mutually_exclusive_group()
    group.add_argument('--scope', '-s',
                       nargs='?',
                       help="""the scope name, must be consistent with --init-scope \
    (for bibtex format cross-reference resolution)""")
    group.add_argument('--shared-scope', '-S',
                       action='store_true',
                       help='use the default shared scope named SHARED_SCOPE')
    bibtex.add_argument('--init-scope', '-i',
                         nargs='?',
                         help='the scope initialization value line (for bibtex format cross-reference resolution)')


    for format in ['RIS 2001', 'RIS 2011', 'refer']:

        f = subparsers.add_parser(name=format.replace(' ', '').lower(),
                                  help=f'generates bibliograpy Python source bibliography from {format} format')
        f.add_argument('file',
                       nargs='?',
                       help="path to the input bibliography file",
                       default=DEFAULT_FILE)
        f.add_argument('--encoding', '-e',
                       nargs='?',
                       help='the bibliograpy configuration file encoding (default to utf-8)',
                       default=DEFAULT_ENCODING)
        f.add_argument('--output-dir', '-O',
                       nargs='?',
                       help='the source bibliograpy file output directory',
                       default=DEFAULT_OUTPUT_DIR)
        f.add_argument('--output-file', '-o',
                       nargs='?',
                       help='the source bibliograpy output file name',
                       default=DEFAULT_OUTPUT_FILE)

    return parser


def entrypoint():
    """The pyenvs command entrypoint."""

    commands = {
        'bibtex': _process,
        'ris2001': _process,
        'ris2011': _process,
        'refer': _process
    }

    ns: Namespace = _create_parser().parse_args()

    commands.get(ns.CMD)(ns)
