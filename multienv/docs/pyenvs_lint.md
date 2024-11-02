# Pyenvs lint

* [Purpose](#purpose)
* [Example](#example)

```text
usage: pyenvs lint [-h] [--encoding [ENCODING]] [--output [OUTPUT]] [file]

positional arguments:
  file                  path to the configuration file

options:
  -h, --help            show this help message and exit
  --encoding [ENCODING], -e [ENCODING]
                        the configuration file encoding (default to utf-8)
  --output [OUTPUT], -o [OUTPUT]
                        the linter configuration file output directory
```

## Purpose

The `pyenvs lint` command parameterizes linter configuration files by environments.

It is useful to factorize some linter rules and to make other ones specific to certain contexts (tests, modules etc.)

A common rule could be set in a `pylintrc_strict` file:

```editorconfig
[FORMAT]
max-line-length=120
```

While some specific modules would require to customize more rules in a `pylintrc_mymodule` file:

```editorconfig
[FORMAT]
max-line-length=120

[SIMILARITIES]
min-similarity-lines=100
```

And specific contexts would require to apply other specific adjustments (`pylintrc_test`):

```editorconfig
[FORMAT]
max-line-length=120

[MESSAGES CONTROL]
disable=protected-access,duplicate-code
```

# Example

```yml
configuration:
  formatters:
    - pylint:
        strict_environment: strict

environments:
  - multienv-src
  - taxref-src
  - src
  - test

sections:
  - name: FORMAT
    rules:
      - key: max-line-length
        value: 120
      - key: max-args
        value: 9
        environments: [src, multienv-src]
  - name: SIMILARITIES
    rules:
      - key: min-similarity-lines
        value: 100
        environments: [taxref-src]
  - name: DESIGN
    rules:
      - key: min-public-methods
        value: 1
        environments: [src, multienv-src]
      - key: max-args
        value: 30
        environments: [src, multienv-src]
      - key: max-locals
        value: 30
        environments: [src, multienv-src]
      - key: max-attributes
        value: 100
        environments: [src, multienv-src]
      - key: max-public-methods
        value: 100
        environments: [src, multienv-src]
      - key: max-parents
        value: 10
        environments: [src, multienv-src]
  - name: MESSAGES CONTROL
    rules:
      - key: disable
        value: 'protected-access,duplicate-code'
        environments: [test]
      - key: disable
        value: 'undefined-variable,unused-argument'
        environments: [src]
      - key: disable
        value: 'undefined-variable,unused-argument,duplicate-code'
        environments: [multienv-src]
```
