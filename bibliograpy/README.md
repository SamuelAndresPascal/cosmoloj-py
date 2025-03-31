# Bibliograpy

Bibliography management to decorate source code.

[![example workflow](https://github.com/SamuelAndresPascal/cosmoloj-py/actions/workflows/bibliograpy.yml/badge.svg)](https://github.com/SamuelAndresPascal/cosmoloj-py/actions)

[![Anaconda-Server Badge](https://anaconda.org/cosmoloj/bibliograpy/badges/version.svg)](https://anaconda.org/cosmoloj/bibliograpy)
[![Anaconda-Server Badge](https://anaconda.org/cosmoloj/bibliograpy/badges/latest_release_date.svg)](https://anaconda.org/cosmoloj/bibliograpy)
[![Anaconda-Server Badge](https://anaconda.org/cosmoloj/bibliograpy/badges/latest_release_relative_date.svg)](https://anaconda.org/cosmoloj/bibliograpy)
[![Anaconda-Server Badge](https://anaconda.org/cosmoloj/bibliograpy/badges/platforms.svg)](https://anaconda.org/cosmoloj/bibliograpy)
[![Anaconda-Server Badge](https://anaconda.org/cosmoloj/bibliograpy/badges/license.svg)](https://anaconda.org/cosmoloj/bibliograpy)

[![PyPI repository Badge](https://badge.fury.io/py/bibliograpy.svg)](https://badge.fury.io/py/bibliograpy)


* [API](#api)
* [Preprocessing tool](#preprocessing-tool)
* [Documentation](#documentation)




The Bibliograpy API allows to manage bibliographic centralized references.

1. As an executable tool, it generates python constant bibliography modules mapping bibliographic files in `Bibtex` and
`RIS (2001)` formats.

2. As an API, it allows to decorate functions, classes and methods referencing the python constant bibliographies.

3. As an underlying library, it supplements the docstring of decorated elements with bibliographical information.


## Preprocessing tool

Bibliograpy allows generating a source code bibliograpy from a resource bibliography file.

Bibliograpy process supports bibliography files in yaml format. Each bibliographic entry contains three fields. 
The `type` field only supports the `misc` value. The `key` fields represents the bibliographic entry unique key (id).
The `title` field represents the readable form or the entry. For instance:

```yml
- entry_type: misc
  cite_key: nasa
  title: NASA
- entry_type: misc
  cite_key: iau
  title: International Astronomical Union
```

This bibliography file can be preprocessend by the `bibliograpy process` tool.

By default, the `bibliograpy process` tool searches for a `bibliograpy.yaml` file reproducing the `Bibtex` format.

```shell
bibliograpy process
```

The bibliograpy file can be renamed, but the `.yaml`/`.yml` extension is needed to supplie a YAML formatted file.

```shell
bibliograpy process my_biblio.yml
```

The json syntax is also supported mapping the `Bibtex` format (`.json` extension mandatory):

```json
[
  {
    "entry_type": "misc",
    "cite_key": "nasa",
    "title": "NASA"
  },
  {
    "entry_type": "misc",
    "cite_key": "iau",
    "title": "International Astronomical Union"
  }
]
```

```shell
bibliograpy process mybiblio.json
```

Or the `Bibtex` syntax itself (`.bib` or `.bibtex` extension mandatory):

```bibtex
@misc{nasa
  title = {NASA}
}

@misc{iau,
  title = {International Astronomical Union}
 }
```

```shell
bibliograpy process my_biblio.bib
```

By default, it produces a `bibliography.py` python module of bibliographic references.

```py
from bibliograpy.api_bibtex import Misc

NASA = Misc.generic(cite_key='nasa',
                    title='NASA')

IAU = Misc.generic(cite_key='iau',
                   title='International Astronomical Union')
```

Otherwise, *for a given format*, the process tool allow to convert a bibiligraphy file from one of the `JSON`, `YAML` 
and standard syntaxes to another one.

### Cross-referencing support (Bibtex format)

The `bibliograpy process` tool support the cross-referencing/inheritance `Bibtex` mechanism.

Example, from a bibtex bibliography (`bibliograpy.bib`):

```
@misc{ogc,
 institution = {OGC},
 title = {Open Geospatial Consortium}
}

@misc{zeitschrift_fur_vermessungswesen,
 journal = {Zeitschrift für Vermessungswesen},
 title = {Zeitschrift für Vermessungswesen}
}

@techreport{cts_revision_v1_0,
 author = {},
 crossref = {ogc},
 month = {January},
 number = {OGC 01-009},
 title = {Coordinate Transformation Services},
 type = {standard},
 year = {2001}
}

@article{joachim_boljen_2004,
 author = {},
 crossref = {zeitschrift_fur_vermessungswesen},
 pages = {258-260},
 title = {Zur geometrischen Interpretation und direkten Bestimmung von Formfunktionen},
 volume = {129},
 year = {2004}
}
```

```shell
bibliograpy process bibliograpy.bib
```

When preprocessed, the bibliography produces some python constants to import in the code which uses these 
bibliographical references.

```python
from bibliograpy.api_bibtex import *


OGC = Misc.generic(cite_key='ogc',
                   institution='OGC',
                   title='Open Geospatial Consortium')

ZEITSCHRIFT_FUR_VERMESSUNGSWESEN = Misc.generic(cite_key='zeitschrift_fur_vermessungswesen',
                                                journal='Zeitschrift für Vermessungswesen',
                                                title='Zeitschrift für Vermessungswesen',
                                                non_standard=NonStandard(issn='0044-3689'))

CTS_REVISION_V1_0 = TechReport.generic(cite_key='cts_revision_v1_0',
                                       author='',
                                       crossref=OGC,
                                       month='January',
                                       number='OGC 01-009',
                                       title='Coordinate Transformation Services',
                                       type='standard',
                                       year=2001,
                                       non_standard=NonStandard(url='https://portal.ogc.org/files/?artifact_id=999'))

JOACHIM_BOLJEN_2004 = Article.generic(cite_key='joachim_boljen_2004',
                                      author='',
                                      crossref=ZEITSCHRIFT_FUR_VERMESSUNGSWESEN,
                                      pages='258-260',
                                      title='Zur geometrischen Interpretation und direkten Bestimmung von Formfunktionen',
                                      volume='129',
                                      year=2004,
                                      non_standard=NonStandard(url='https://geodaesie.info/system/files/privat/zfv_2004_4_Boljen.pdf'))
```

Nevertheless, to be actually cross-resolved all the references *must* use a scope.

```shell
bibliograpy process --scope=_SCOPE --init-scope="_SCOPE = {}" bibliograpy.bib
```

```python
from bibliograpy.api_bibtex import *

_SCOPE = {}


OGC = Misc.generic(cite_key='ogc',
                   institution='OGC',
                   title='Open Geospatial Consortium',
                   scope=_SCOPE)

ZEITSCHRIFT_FUR_VERMESSUNGSWESEN = Misc.generic(cite_key='zeitschrift_fur_vermessungswesen',
                                                journal='Zeitschrift für Vermessungswesen',
                                                title='Zeitschrift für Vermessungswesen',
                                                non_standard=NonStandard(issn='0044-3689'),
                                                scope=_SCOPE)

CTS_REVISION_V1_0 = TechReport.generic(cite_key='cts_revision_v1_0',
                                       author='',
                                       crossref=OGC,
                                       month='January',
                                       number='OGC 01-009',
                                       title='Coordinate Transformation Services',
                                       type='standard',
                                       year=2001,
                                       non_standard=NonStandard(url='https://portal.ogc.org/files/?artifact_id=999'),
                                       scope=_SCOPE)

JOACHIM_BOLJEN_2004 = Article.generic(cite_key='joachim_boljen_2004',
                                      author='',
                                      crossref=ZEITSCHRIFT_FUR_VERMESSUNGSWESEN,
                                      pages='258-260',
                                      title='Zur geometrischen Interpretation und direkten Bestimmung von Formfunktionen',
                                      volume='129',
                                      year=2004,
                                      non_standard=NonStandard(url='https://geodaesie.info/system/files/privat/zfv_2004_4_Boljen.pdf'),
                                      scope=_SCOPE)
```

Note the scope name *must* be provided by the `--scope` option and be properly initialized using the `--init-scope`
option.

A default `SHARED_SCOPE` shared scope is provided by the `bibliograpy.api_bibtex` module. If this name is supplied to
the `--scope` option, no initialization is necessary unless the user wants to shadow the common `SHARED_SCOPE`.

## API

Hence, is it possible to factorize all bibliographic sources as variables in a single module, using them as arguments of
decorators.

```py
"""The bibliography module."""

from bibliograpy.api_bibtex import TechReport

IAU_2006_B1 = TechReport.generic(
    cite_key='iau_2006_b1',
    author='',
    institution='iau',
    title='Adoption of the P03 Precession Theory and Definition of the Ecliptic',
    year=2006)
```

```py
"""The bibliography_client module using the bibliography module."""

from bibliograpy.api_common import cite

from bibliography import IAU_2006_B1

@cite(IAU_2006_B1)
def my_function():
    """My my_function documentation."""
    # some implementation here using the reference given as a parameter to the decorator

```

The usage of the decorator has two purposes.

First, to use a bibliographic reference defined once and for all, centralized and reusable.

Second, to implicitly add to the documentation of the decorated entity a bibliographical section.

```
import bibliography_client

>>> help(my_function)
Help on function my_function in module bibliography_client

my_function()
    My my_function documentation.

    Bibliography: Adoption of the P03 Precession Theory and Definition of the Ecliptic [iau_2006_b1]
```

## Documentation

[Latest release](https://cosmoloj.com/mkdocs/bibliograpy/latest/)

[Trunk](https://cosmoloj.com/mkdocs/bibliograpy/master/)