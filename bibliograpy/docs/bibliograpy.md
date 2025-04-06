# Bibliograpy

`bibliograpy` is a tool of bibliography management.

The bibliograpy purpose consists in two distinct parts.

* [API](#bibliograpy-api)
* [Preprocessing Tool](#bibliograpy-preprocessing)

## Bibliograpy API

First, the **Bibliograpy API** allows to manipulate bibliographic references as symbols of the code itself instead of
simple character strings deprived of any semantics in the docstrings.

Consider the ordinary way to mention bibliographic references in source code.

```python
def foo():
    """
    Foo does nothing.
    
    Bibliography: the Bibliograpy documentation
    """
    
def bar():
    """
    Foo does nothing more.
    
    Bibliography: the Bibliograpy documentation
    """
```

Both functions use the same reference.

But nothing is factorized for maintenance purpose. Maybe a typo could affect all
the citations of the same references, maybe a single one.

The information is poor: nothing about the author, nothing
about the journal. This observation is related to the previous one: the information is poor, because it is verbosely
repeated and hard to maintain and to format.

The information is deprived of any semantics. No way to detect the same bibliographic reference is used twice, but a raw
character string search in the source code.

Compare:

```python
from bibliograpy.api_bibtex import Misc, NonStandard, cite

BIBLIOGRAPY_DOC = Misc.generic(cite_key='bibliograpy_doc',
                               title='the Bibliograpy documentation',
                               non_standard=NonStandard(url='https://cosmoloj.com/mkdocs/bibliograpy/latest/'))

@cite(BIBLIOGRAPY_DOC)
def foo():
    """
    Foo does nothing.
    """


@cite(BIBLIOGRAPY_DOC)
def bar():
    """
    Foo does nothing more.
    """
```

Now, the bibliographic documentation is factorized, symbolic and semantic. This facilitates maintenance, refactoring 
search in code and enrichment operations.

Furthermore, providing heritage mechanisms based on the BibTex specification using crossreferencing, the Bibliograpy API
allows to define navigable links in code between bibliographic variables, for instance all the articles refering to the 
same journal which factorizes its title:

```python
from bibliograpy.api_bibtex import Misc, Article, cite

JOURNAL = Misc.generic(cite_key='my_journal', journal='My International Journal')

ARTICLE_A = Article.generic(cite_key='article_a', title='Mi first discovery', crossref=JOURNAL)

ARTICLE_B = Article.generic(cite_key='article_b', title='Mi second discovery', crossref=JOURNAL)

@cite(ARTICLE_A)
def foo():
    """
    My first discovery demonstration.
    """


@cite(ARTICLE_A, ARTICLE_B)
def bar():
    """
    Comparison between my first discovery and my second one.
    """

```


## Bibliograpy Preprocessing




```text
usage: bibliograpy [-h] {bibtex,ris2001,ris2011,refer,endnote} ...

Bibliography management.

positional arguments:
  {bibtex,ris2001,ris2011,refer,endnote}
                        available commands
    bibtex              generates bibliograpy Python source bibliography from Bibtex format
    ris2001             generates bibliograpy Python source bibliography from RIS (2001) format
    ris2011             generates bibliograpy Python source bibliography from RIS (2011) format
    refer               generates bibliograpy Python source bibliography from refer format
    endnote             generates bibliograpy Python source bibliography from Endnote format

options:
  -h, --help            show this help message and exit
```
