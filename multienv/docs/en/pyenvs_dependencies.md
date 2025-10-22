# Pyenvs dependencies (deps)

* [Purpose](#purpose)
* [Getting started](#getting-started)
* [Basic configuration](#basic-configuration)
* [Strict configuration](#strict-configuration)
* [Default configuration](#default-configuration)
* [Commented example](#commented-example)

```text
usage: pyenvs dependencies [-h] [--encoding [ENCODING]] [--output [OUTPUT]] [file]

positional arguments:
  file                  path to the configuration file

options:
  -h, --help            show this help message and exit
  --encoding [ENCODING], -e [ENCODING]
                        the configuration file encoding (default to utf-8)
  --output [OUTPUT], -o [OUTPUT]
                        the dependency management file output directory
```

## Purpose

The `pyenvs dependencies` command parameterizes environment/requirement files by environments.

For instance, suppose you have to maintain a python program. Its dependencies would be specified in a `pyproject.toml`
file while it is supposed to run in an environment supplying a compatible python interpreter.

Setting a `Conda` environment will resemble to setting a file like this (`environment.yml`):

```yml
dependencies:
- python=3.12
```

But testing purposes would require to add some dependencies specific to the testing environment.
Those dependencies are not functional dependencies of your program supposed to be set in the `pyproject.toml`. They are
specific to the context of the program usage (like testing it) and must be set in coherence between themselves 
and the program. For instance (`environment_pytest.yml`):

```yml
dependencies:
- python=3.12
- pytest=7.4.4
```

Similarly, running a linter would require another specific environment (`environment_pylint.yml`) which 
would not require test dependencies:

```yml
dependencies:
- python=3.12
- pylint=3.2.2
```

But running a linter for the test files, would require another one environment (`environment_pylint_pytest.yml`) 
specifying both the linter and the testing framework dependencies:

```yml
dependencies:
- python=3.12
- pylint=3.2.2
- pytest=7.4.4
```

Defining environment files is one of the way to proceed, but manually adding dependencies to an environment defined by
a minimal dependency file is another one, although less synthetic. Compare:

```bash
conda env create -n default -f environment_strict.yml
conda env create -n pylint_pytest -f environment_strict.yml
conda install pylint=3.2.2 pytest=7.4.4
conda env create -n pylint -f environment_strict.yml
conda install pylint=3.2.2
conda env create -n pytest -f environment_strict.yml
conda install pytest=7.4.4
```

to:

```bash
conda env create -n pylint_pytest -f environment_strict.yml
conda env create -n pylint_pytest -f environment_pylint_pytest.yml
conda env create -n pylint_pytest -f environment_pylint.yml
conda env create -n pylint_pytest -f environment_pytest.yml
```

Both ways to proceed implies maintaining a coherent set of dependency versions in several places, either in command line
arguments or in environment files. The purpose of `pyenvs dependencies` is to manage a coherent dependency version set 
in a single configuration files from which generating all the specific environment files.

## Getting started

Using `pyenvs dependencies`, the configuration mapping the previous environment definitions can be specified in a single 
`pyenvs-deps.yml` file. 

`pyenvs-deps.yml` is the default configuration file name, located by default in the current working directory.

### Basic configuration

```yml
configuration:
  formatters:
    - conda

dependencies:
  - id: python
    version: '3.12'
  - id: pylint
    version: 3.2.2
    environments: [lint]
  - id: pytest
    version: 7.4.4
    environments: [test]
```

Running:

```bash
pyenvs dependencies
```

Generates two environment files because two environments are mentioned in the configuration file: `test` and `lint`.

Dependencies not specifying any environment are supposed not to be specific and so, are added to all generated 
dependency management files.

By default, all generated dependency management files are built as follows: `environment_<env_name>.yml`. The default
`environment` prefix can be parameterized.

The ```environment_lint.yml``` conda environment file:

```yml
name: lint
dependencies:
- python=3.12
- pylint=3.2.2
```

The ```environment_test.yml``` conda environment file:

```yml
name: test
dependencies:
- python=3.12
- pytest=7.4.4
```

### Strict configuration

By default, only the dependency management files specific to each explicit environment are generated. But it could be
useful to also generate a dependency management file containing only the dependencies common to all of them.

Those dependencies could be interpreted as ones to be strictly necessary to all environments as functional dependencies 
of the program.

This can be achieved setting the `strict_environment` option in the formatter parameters. This parameter gives a
name to the *strict* environment to generate. 

```yml
configuration:
  formatters:
    - conda:
        strict_environment: strict

dependencies:
  - id: python
    version: '3.12'
  - id: pylint
    version: 3.2.2
    environments: [lint]
  - id: pytest
    version: 7.4.4
    environments: [test]
```

This configuration produces an additional dependency management file named `environment_strict.yml`:

```yml
name: strict
dependencies:
- python=3.12
```

### Default configuration

The *strict* environment is only generated because it is explicitly parameterized with a name (*strict*) in the 
configuration file. In a same way, a *default* environment file in only generated if the configuration file contains
the `default_environment` parameter providing its name.

```yml
configuration:
  formatters:
    - conda:
        strict_environment: strict
        default_environment: default

dependencies:
  - id: python
    version: '3.12'
  - id: pylint
    version: 3.2.2
    environments: [lint]
  - id: pytest
    version: 7.4.4
    environments: [test]
```

Using this updated configuration file would have produced one more `environment_default.yml`:

```yml
name: default
dependencies:
- python=3.12
- pylint=3.2.2
- pytest=7.4.4
```

From now, all the dependency versions can be managed from a single configuration file for all the environment needed by
the contextual usage of the program.

# Commented example

```yml
configuration:
  formatters:
    # since it contains parameters, the conda formatter is not specified as a single string but as an object containing
    # properties: strict_environment, channels, pip
    - conda:
        # a "strict environment" will be generated containing only the common dependencies (ones which does not
        # specify any environment, and it will be named "strict"
        strict_environment: strict
        # the following channels will be added to the generated conda environment files
        channels:
          - default
          - conda-forge
        # all the following dependencies will be considered as pip dependencies in the generated conda environment 
        # files.
        pip:
          - build

# the environment list is optional
# it is only used to check no environment has been forgotten and none has been misspelled
# when specified, make pyenv dependencies check all the environment specified in the dependency list exactly map this
# environment set
environments:
  - lint
  - test
  - lint_test
  - doc
  - pypi_pkg
  - pypi_publish
  - conda_publish

dependencies:
  # no environment specified for python dependency: it will be added to all the generated dependency management files
  - id: python
    version: '3.12'
  - id: pylint
    version: 3.2.2
    environments: [lint, lint_test]
  - id: pytest
    version: 7.4.4
    environments: [test, lint_test]
  # the version tag is not mandatory
  - id: pytest-cov
    environments: [test]
  - id: mkdocs
    version: '1.6'
    environments: [doc]
  - id: mkdocstrings
    environments: [doc]
  - id: mkdocstrings-python
    environments: [doc]
  - id: build
    version: 1.2.1
    environments: [pypi_pkg]
  - id: twine
    environments: [pypi_publish]
  - id: grayskull
    environments: [conda_publish]
```