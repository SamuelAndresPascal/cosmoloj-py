"""
pyenvs command entrypoint
"""
import logging

from argparse import ArgumentParser, Namespace

from multienv.pyenvs_deps import _dependencies

LOG = logging.getLogger(__name__)


def _info(ns: Namespace):
    """info
    """
    LOG.info("info")




def _create_parser() -> ArgumentParser:

    # parse argument line
    parser = ArgumentParser(description='Multi environment management.')

    subparsers = parser.add_subparsers(dest='CMD', help='available commands')

    subparsers.add_parser('info', help='get general info')

    parser_config = subparsers.add_parser(name='dependencies',
                                          help='generates environment configurations',
                                          aliases=['deps'])
    parser_config.add_argument('file',
                               nargs='?',
                               help="path to the configuration file",
                               default="pyenvs-deps.yml")
    parser_config.add_argument('--encoding',
                               nargs='?',
                               help='the configuration file encoding (default to utf-8)',
                               default='utf-8')
    parser_config.add_argument('--output',
                               nargs='?',
                               help='the environment file output directory',
                               default='.')

    return parser


def entrypoint():
    """The pyenvs command entrypoint."""

    commands = {
        'info': _info,
        'dependencies': _dependencies,
        'deps': _dependencies
    }

    ns: Namespace = _create_parser().parse_args()

    commands[ns.CMD](ns)
