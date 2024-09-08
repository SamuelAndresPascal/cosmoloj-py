"""Pyenv config:
General standard input definition.
"""

from dataclasses import dataclass

@dataclass(frozen=True)
class Rule:
    key: str
    value: str
    environments: list[str]

    @staticmethod
    def from_dict(source: dict):
        """Builds a Rule from a configuration dict."""

        assert 'key' in source, 'key is a mandatory section field'
        assert 'value' in source, 'value is a mandatory section field'

        return Rule(
            key=source['key'],
            value=source['value'],
            environments=source['environments'] if 'environments' in source else None,
        )

@dataclass(frozen=True)
class Section:
    name: str
    rules: list[Rule]

    @staticmethod
    def from_dict(source: dict):
        """Builds a Section from a configuration dict."""

        assert 'name' in source, 'name is a mandatory section field'
        assert 'rules' in source, 'rules is a mandatory section field'

        return Section(
            name=source['name'],
            rules=[Rule.from_dict(s) for s in source['rules']],
        )

@dataclass(frozen=True)
class Configuration:
    """Representation of pyenvs configuration content."""

    formatters: list[dict | str]
    """Each formatter either can be a single character string of one of supported formatters or a key/value pair with 
    the key referencing to the formatter name and the value referencing to its specific configuration."""

    environments: list[str] | None
    """A reference list of the environments referenced by dependencies. If the list is provided, dependencies 
    referencing an unknown environment raise an error. If the list is not provided, it is inferred from the dependency
    environments. If an empty list is provided, no dependency is supposed to reference any specific environment."""

    sections: list[Section]
    """The list of the sections."""

    @staticmethod
    def from_dict(source: dict):
        """Builds a Configuration from a configuration dict."""
        return Configuration(
            formatters=source['formatters'],
            environments=source['environments'] if 'environments' in source else None,
            sections=[Section.from_dict(s) for s in source['sections']]
        )
