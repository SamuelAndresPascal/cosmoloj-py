"""
pyenvs command entrypoint
"""
import logging
from argparse import ArgumentParser, Namespace
from collections.abc import Callable
from dataclasses import dataclass
from enum import Enum

import yaml
from packaging.markers import default_environment

LOG = logging.getLogger(__name__)

@dataclass(frozen=True)
class Dependency:
    id: str
    version: str | None
    environments: list[str] | None
    source: str | None
    sha: str | None

    @staticmethod
    def from_dict(source: dict):
        return Dependency(
            id=source['id'],
            version=str(source['version']) if 'version' in source else None,
            environments=source['environments'] if 'environments' in source else None,
            source=source['source'] if 'source' in source else None,
            sha=source['sha'] if 'sha' in source else None
        )

@dataclass(frozen=True)
class Configuration:
    handlers: list[str, dict]
    environments: list[str] | None
    dependencies: list[Dependency]

    @staticmethod
    def from_dict(source: dict):
        return Configuration(
            handlers=source['configuration']['handlers'],
            environments=source['environments'] if 'environments' in source else None,
            dependencies=[Dependency.from_dict(d) for d in source['dependencies']]
        )


def _info(ns: Namespace):
    """info
    """
    LOG.info("info")
    print("print info")
    print(ns)


def conda_formatter(d: Dependency) -> str:
    result : str = d.id
    if d.version is not None:
        result += '=' + d.version
        if d.sha is not None:
            result += d.sha
    return result

def conda_handler(configuration: Configuration):

    handler_configuration = Handlers.CONDA.handler_configuration(configuration)
    print(handler_configuration)
    default_environment = 'default_environment' not in handler_configuration or handler_configuration['default_environment']
    prefix = handler_configuration['prefix'] if 'prefix' in handler_configuration else 'environment'

    # default environment includes all dependencies
    if default_environment:
        ed = []
        for d in configuration.dependencies:
            ed.append(conda_formatter(d))

        output = {}
        output['dependencies'] = ed
        with open(f'{prefix}_.yml', "w") as o:
            yaml.dump(output, o)

    if configuration.environments:
        for e in configuration.environments:
            ed = []
            for d in configuration.dependencies:
                if d.environments is None or e in d.environments:
                    ed.append(conda_formatter(d))

            output = {}
            output['dependencies'] = ed
            with open(f'{prefix}_{e}.yml', "w") as o:
                yaml.dump(output, o)

@dataclass
class _HandlerValue:
    name: str
    handler: Callable[[Configuration], None]


class Handlers(Enum):
    CONDA = _HandlerValue(name='conda', handler=conda_handler)

    def test(self, handler: dict | str) -> bool:
        for h in Handlers:
            if (isinstance(handler, str) and self.value.name == handler
                    or isinstance(handler, dict) and self.value.name in handler):
                return True
        return False


    def handler_configuration(self, configuration: Configuration) -> dict | None:
        for h in configuration.handlers:
            if isinstance(h, dict) and self.value.name in h:
                return h[self.value.name]


def _config(ns: Namespace):
    """config
    """
    LOG.info("config")

    extension = ns.file.split('.')[-1]

    if extension in ['yml']:
        with open(ns.file) as s:
            content = yaml.safe_load(s)
            print(content)
            configuration = Configuration.from_dict(content)

            for req_handler in configuration.handlers:
                for supported_handler in Handlers:
                    if supported_handler.test(req_handler):
                        supported_handler.value.handler(configuration)


    else:
        raise ValueError(f'unsupported configuration format {extension}')

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
                               default="multienv.yml")

    return parser


def entrypoint():
    """The pyenvs command entrypoint."""

    commands = {
        'info': _info,
        'config': _config
    }

    ns: Namespace = _config_parser().parse_args()

    commands[ns.CMD](ns)
