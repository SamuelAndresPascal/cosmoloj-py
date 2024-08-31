"""
pyenvs command entrypoint
"""
import logging
from argparse import ArgumentParser, Namespace

LOG = logging.getLogger(__name__)


def _info(ns: Namespace):
    """info
    """
    LOG.info("info")
    print("print info")
    print(ns)


def _config(ns: Namespace):
    """config
    """
    LOG.info("config")
    print("print config")
    print(ns)


def _config_parser() -> ArgumentParser:

    # parse argument line
    parser = ArgumentParser(description='Multi environment management.')

    subparsers = parser.add_subparsers(dest='CMD', help='available commands')

    subparsers.add_parser('info', help='get general info')

    parser_config = subparsers.add_parser('config', help='generates environment configurations')
    parser_config.add_argument('file',
                               nargs='?',
                               help="path to the configuration file",
                               default="multienv.json")

    return parser


def entrypoint():
    """The pyenvs command entrypoint."""

    commands = {
        'info': _info,
        'config': _config
    }

    ns: Namespace = _config_parser().parse_args()

    commands[ns.CMD](ns)
