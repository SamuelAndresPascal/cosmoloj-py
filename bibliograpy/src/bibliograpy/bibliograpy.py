"""
bibliograpy command entrypoint
"""
import logging

from argparse import ArgumentParser, Namespace

LOG = logging.getLogger(__name__)


def _info(ns: Namespace):
    """info
    """
    LOG.info("info %s", ns)




def _create_parser() -> ArgumentParser:

    # parse argument line
    parser = ArgumentParser(description='Multi environment management.')

    subparsers = parser.add_subparsers(dest='CMD', help='available commands')

    subparsers.add_parser('info', help='get general info')

    return parser


def entrypoint():
    """The pyenvs command entrypoint."""

    commands = {
        'info': _info
    }

    ns: Namespace = _create_parser().parse_args()

    commands[ns.CMD](ns)
