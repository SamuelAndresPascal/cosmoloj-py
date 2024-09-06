"""Pyenvs config:
Formatter definitions.

Supported formatters:
- conda
"""

from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Callable

from multienv._pyenvs_config_input_std import Configuration
from multienv._pyenvs_config_output_conda import CondaEnvironment

@dataclass(frozen=True)
class CondaConfiguration:
    """The specific conda configuration model."""

    default_environment: str | None
    strict_environment: str | None
    file_pattern: str
    encoding: str
    channels: list[str] | None
    pip: list[str] | None

    @staticmethod
    def from_configuration(formatter: dict | str):
        """Builds a conda configuration object form a dict or a default one form a string"""

        if isinstance(formatter, str):
            return _DEFAULT_CONDA_CONFIGURATION

        body = formatter[Formatters.CONDA.value.name]

        return CondaConfiguration(
            default_environment=body['default_environment'] if 'default_environment' in body
            else _DEFAULT_CONDA_CONFIGURATION.default_environment,
            strict_environment=body['strict_environment'] if 'strict_environment' in body
            else _DEFAULT_CONDA_CONFIGURATION.strict_environment,
            file_pattern=body['file_pattern'] if 'file_pattern' in body else _DEFAULT_CONDA_CONFIGURATION.file_pattern,
            encoding=body['encoding'] if 'encoding' in body else _DEFAULT_CONDA_CONFIGURATION.encoding,
            channels=body['channels'] if 'channels' in body else _DEFAULT_CONDA_CONFIGURATION.channels,
            pip=body['pip'] if 'pip' in body else _DEFAULT_CONDA_CONFIGURATION.pip
        )

_DEFAULT_CONDA_CONFIGURATION = CondaConfiguration(
    default_environment=None,
    strict_environment=None,
    file_pattern='environment',
    encoding='utf-8',
    channels=None,
    pip=None
)

def conda_writer(conf: Configuration, output_dir: Path):
    """Writes a configuration as conda configuration environment files."""

    environments = conf.effective_environments()

    formatter_conf: CondaConfiguration = Formatters.CONDA.get_formatter_configuration(conf)

    envs: list[CondaEnvironment] = []

    # default environment includes all dependencies
    if formatter_conf.default_environment:
        envs.append(CondaEnvironment.from_configuration(name=formatter_conf.default_environment,
                                                        channels=formatter_conf.channels,
                                                        pip=formatter_conf.pip,
                                                        configuration=conf))

    # strict environment excludes all dependencies specific to an environment
    if formatter_conf.strict_environment:
        envs.append(CondaEnvironment.from_dependencies(name=formatter_conf.strict_environment,
                                                       channels=formatter_conf.channels,
                                                       pip=formatter_conf.pip,
                                                       dependencies=conf.strict_dependencies()))

    for e in environments:

        envs.append(CondaEnvironment.from_dependencies(name=e,
                                                       channels=formatter_conf.channels,
                                                       pip=formatter_conf.pip,
                                                       dependencies=conf.env_dependencies(e)))

    for env in envs:
        env.dump(path=Path(output_dir, f'{formatter_conf.file_pattern}_{env.name}.yml'),
                 encoding=formatter_conf.encoding)


@dataclass(frozen=True)
class _FormatterValue[C]:
    name: str
    write: Callable[[Configuration, Path], None]
    configuration: Callable[[dict | str], C]


class Formatters(Enum):
    """The enumeration of the supported formatters."""
    CONDA = _FormatterValue[CondaConfiguration](name='conda',
                                                write=conda_writer,
                                                configuration=CondaConfiguration.from_configuration)

    def test(self, formatter: dict | str) -> bool:
        """Checks if a formatter configuration dict refers to the current Formatter value."""
        return (isinstance(formatter, str) and self.value.name == formatter
                or isinstance(formatter, dict) and self.value.name in formatter)

    def get_formatter_configuration(self, configuration: Configuration):
        """Builds a specific formatter configuration from the main configuration related to the current Formatter value.
        """
        for formatter in configuration.formatters:
            if self.test(formatter):
                return self.value.configuration(formatter)
        raise ValueError
