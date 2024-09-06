# Multienv

* [Requirements Installation](#requirements-installation)
* [Pyenvs](#pyenvs)
  - [Pyenvs config](#pyenvs-config)

## Requirements Installation

`multienv` requires `python>=12` and uses `pyyaml`.

It can be installed using pip:

```bash
pip install multienv
```

Or using conda refering to the `cosmoloj` channel:

```bash
conda install multienv -c cosmoloj
```

## Pyenvs

`pyenvs` is a tool of python configuration file management.

```text
usage: pyenvs [-h] {info,config} ...

Multi environment management.

positional arguments:
  {info,config}  available commands
    info         get general info
    config       generates environment configurations

options:
  -h, --help     show this help message and exit
```

### Pyenvs config


```text
usage: pyenvs dependencies [-h] [--encoding [ENCODING]] [--output [OUTPUT]] [file]

positional arguments:
  file                  path to the configuration file

options:
  -h, --help            show this help message and exit
  --encoding [ENCODING]
                        the configuration file encoding (default to utf-8)
  --output [OUTPUT]     the environment file output directory
```


The `pyenvs dependencies` command parameterizes environment/requirement files by environments.

For instance, suppose you have to maintain a python program using `multienv` as a dependency.

Setting a `Conda` environment will resemble to setting a file like this (`environment_strict.yml`):

```yml
dependencies:
- python=3.12
```

But testing purposes would require to add some dependencies specific to the testing environment.
For instance (`environment_pytest.yml`):

```yml
dependencies:
- python=3.12
- pytest=7.4.4
```

Similarly, running a linter would require another specific environment (`environment_pylint.yml`):

```yml
dependencies:
- python=3.12
- pylint=3.2.2
```

And running a linter for the test files, would require another one (`environment_pylint_pytest.yml`):

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

The configuration mapping the previous environment definitions is specified in a single `multienv.yml` file. 
`multienv.yml` is the default configuration file name, located by default in the current working directory.

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

Running:

```bash
pyenvs dependencies
```

Generates three environment files. The `strict` environment only includes the dependencies without specific environment.
Those dependencies are interpreted to be strictly necessary to all environments as functional dependencies of the 
program.

The `environment_strict.yml` conda environment file:

```yml
name: strict
dependencies:
- python=3.12
```


Other dependencies enumerates environment tags which are used to defines each one an environment adding to the stric
dependencies, all the dependencies mentioning the environment tag.

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

The `strict` environment is only generated because it is explicitly parameterized with a name ("strict") in the 
configuration file. In a same way, a `default` environment file in only generated if the configuration file contains
a parameter given its name.

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

Using this updated configuration file would have produced one more `environment_default.yml` conda environment file:

```yml
name: default
dependencies:
- python=3.12
- pylint=3.2.2
- pytest=7.4.4
```

From now, all the dependency versions can be managed from a single configuration files for all the environment needed by
the contextual usage of the program.
