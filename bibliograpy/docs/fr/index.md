# Bibliograpy

*Bibliograpy* est à la fois:

* une API de décoration, d'annotation et d'introspection de code par des références bibliographiques 
* un outil de représentation de références bibliographiques sous la forme d'objets python à partir de formats standards
(Bibtex, RIS, Endnote, Refer, PubMed). Accessoirement, cet outil permet de représenter ces formats en utilisant une 
syntaxe `YAML` [@yaml] ou `JSON` [@json]

***Bibliograpy* n'est pas un outil de conversion de bibliographies entre des formats standards.**

* [Cas d'utilisation](#cas-dutilisation)
* [Décorer son code](#decorer-son-code)
* [Synchroniser ses références](#synchroniser-ses-references)
* [Résultat](#resultat)

## Cas d'utilisation

Un code source élégant, rigoureux, raisonnablement documenté, peut être vu comme une documentation exécutable.
À ce titre, on souhaiterait y indiquer les ressources bibliographiques auxquelles il se réfère de manière aussi aisée 
qu'on le pratique dans un article : une simple annotation par une clef bibliographique dans le texte renvoyant à la 
référence détaillée dans une bibliographie centralisée, une même référence pouvant aisément être souvent utilisée dans 
le texte par la simple mention de sa clef bibliographique.

Sans outil dédié, la manière la plus intuitive de référencer des ressources bibliographiques dans du code source Python 
consiste à les énumérer dans la documentation des entités concernées (classes, fonctions, constantes).

```python
"""Module documentation.

Inspired from the best article written ever [art00].
"""

from enum import Enum
from dataclasses import dataclass

@dataclass(frozen=True)
class MyType:
    """MyType dataclass documentation.
    
    Bibliography:
    * the best article written ever [art00]
    * an alternative to the best article written ever [art01]
    """
    field1: str
    """From an alternative to the best article written ever [art01]"""
    
class MyEnum(Enum):
    """MyEnum enum documentation.
    
    Bibliography:
    * the best article written ever [art00]
    * an alternative to the best article written ever [art01]
    """
    INSTANCE1 = 'My instance'
    """From the best article written ever [art00]"""

A: int = 0
"""An universal constant.
    
Bibliography:
* the best article written ever [art00]
* an alternative to the best article written ever [art01]
"""

class Bar:
    """The Bar class.
    
    Bibliography:
    * the best article written ever [art00]
    """
    

def foo(a: int, b: int) -> int:
    """The foo function.
    
    Bibliography:
    * the best article written ever [art00]
    * an alternative to the best article written ever [art01]
    """
    return a // b

```

Cette stratégie présente plusieurs inconvénients :

* La bibliographie prend la forme de suites de caractères difficilement identifiables *en tant que telles* au milieu 
des autres caractères de documentation. Les ressources bibliographiques ne sont pas *réutilisables*.
* Corollaire de l'impossibilité de réutiliser les références bibliographiques, leurs occurrences multiples
réplique leur représentation comme chaînes de caractères, accroît les risques de fautes de frappe et complique les 
opérations de maintenance.
* On assimile la *ressource bibliographique* et sa *mise en forme*, la *donnée* d'une part et son *rendu* d'autre part.
Cette confusion contraint à opérer des choix quant aux informations relatives à la ressource que l'on souhaite 
mentionner et celles que l'on ne souhaite pas conserver pour ne pas encombrer le rendu : il n'y a pas de place pour 
d'éventuelles  informations que l'on souhaiterait conserver en tant que données mais pas afficher dans la documentation.

## Décorer son code

L'API *Bibliograpy* permet de représenter les ressources bibliographiques en tant que telles sous une forme réifiée. Les
ressources sont des objets utilisables dans le code source, ce qui apporte une réponse à ces différents problèmes.

* La bibliographie est séparée de la rédaction de la documentation. Chaque objet représentant une resource 
bibliographique est réutilisable. Les ressources bibliographiques ainsi représentées sont associées : 
  * aux fonctions, aux classes et aux méthodes par des décorateurs, 
  * aux constantes, aux variables, aux paramètres des fonctions et aux champs des *dataclasses* via les *hints* du 
  langage
  * aux instances d'énumérations et aux modules au moyen de fonctions
Décorateurs, *hints* et fonctions sont résolus ou invoqués au chargement du module. Les décorateurs et les fonctions
appliquées aux modules permettent d'intégrer la bibliographie à la documentation de ces entités du languages contenue
dans le champ spécial `__doc__`, de manière à l'afficher au moment son *rendu* (par la fonction `help()` par exemple).
* Toute opération de maintenance relative à une ressource (faute de frappe dans le titre, ajout d'un auteur ou d'un 
sous-titre...) est factorisée à un seul endroit, au moment de l'instanciation de l'objet représentant la référence
bibliographique.
* Un grand nombre d'informations peut être contenu dans l'objet représentant la ressource bibliographique. Cette
information facile d'accès par navigation dans le code source n'est pas forcément affichée dans son intégralité au 
moment du calcul du *rendu* éventuel dans la docstring éventuel. L'API *Bibliograpy* fournit des modalités d'affichage
par défaut qui peuvent être paramétrés, étendus ou imités pour obtenir un résultat adapté à des besoins spécifiques.


```python
"""Module documentation.
"""

from bibliograpy.api_common import cite, cite_hint, cite_module
from bibliograpy.api_bibtex import Misc

# Build the programmatical bibliography
ART00 = Misc.generic(cite_key='art00', title='the best article written ever')
ART01 = Misc.generic(cite_key='art01', title='an alternative to the best article written ever')

# module bibliography
cite_module(ART00)

from enum import Enum
from dataclasses import dataclass

@cite(ART00, ART01)
@dataclass(frozen=True)
class MyType:
    """MyType dataclass documentation."""
    field1: cite_hint(str, ART01)
    
@cite(ART00, ART01)
class MyEnum(Enum):
    """MyEnum enum documentation."""
    INSTANCE1 = cite_hint('My instance', ART00)

A: cite_hint(int, ART00, ART01) = 0
"""An universal constant."""

@cite(ART00)
class Bar:
    """The Bar class."""
    
@cite(ART00, ART01)
def foo(a: int, b: int) -> int:
    """The foo function."""
    return a // b
```

## Synchroniser ses références

Il subsiste toutefois un autre problème. La représentation des ressources bibliographiques sous la forme
d'objets python n'est pas un standard largement partagé. Quoique puissamment factorisée pour son
utilisation dans le code source, cette information n'est pas partageable à l'extérieur du code.

En revanche, il existe pour cela de nombreux formats largement utilisés ouvrant la voie à une
interopérabilité plus ou moins étendue. Par exemple, il peut être intéressant d'utiliser une même base de
références bibliographiques qui serve à la fois dans le code source *et* à d'autres endroits, telles qu'une
documentation en markdown ou au format rst, voire une des articles rédigés à partir du code source, par exemple en 
LaTeX, associés aux sources et destinés eux-mêmes à être publiés. Sans même parler de LaTeX, des plugins *mkdocs* ou 
*sphinx*, permettent de référencer facilement des resources bibliographiques représentées au format Bibtex.
Utiliser un standard pour représenter sa bibliographie ouvre donc la porte à une large factorisation et à une
utilisation rationalisée et optimisée de l'information bibliographique.

La solution *simple* à ce problème consiste forcément à partir du format largement accepté pour
maintenir les ressources bibliographiques et donc à permettre de *synchroniser* leur représentation
accessible dans le code source.

Il s'agit-là du second objectif que *Bibliograpy* propose de réaliser en tant qu'outil exécutable permettant
de générer un module d'objets de références bibliographiques à partir d'un format bibliographiques standard.

Ainsi, seule la maintenance de la bibliographie standard est nécéssaire à partir de la quelle la bibliographie
programmaique peut être générée et synchronisée.

La bibliographie auparavant construite dans le module cible peut être écrite en Bibtex :

```bibtex
@misc{art00, 
 title = {the best article written ever},
 author = {The Author}
}

@misc{art01, 
 title = {an alternative to the best article written ever},
 year = {2025}
}
```

Puis préprocessée par *Bibliograpy* :

```shell
bibliograpy bibtex
```

Afin de produire un module bibliographique programmatique en Python synchronisé avec la bibliographie maintenue au 
format standard :

```python
from bibliograpy.api_bibtex import *

ART00 = Misc.generic(cite_key='art00', 
                     title='the best article written ever',
                     author='The Author')

ART01 = Misc.generic(cite_key='art01', 
                     title='an alternative to the best article written ever',
                     year='2025')
```

Lequel module peut maintenant être importé dans les modules citant les resources qu'il contient :

```python
"""Module documentation.
"""

from bibliograpy.api_common import cite, cite_hint, cite_module
from bibliography import ART00, ART01

# module bibliography
cite_module(ART00)

from enum import Enum
from dataclasses import dataclass

@cite(ART00, ART01)
@dataclass(frozen=True)
class MyType:
    """MyType dataclass documentation."""
    field1: cite_hint(str, ART01)
    
@cite(ART00, ART01)
class MyEnum(Enum):
    """MyEnum enum documentation."""
    INSTANCE1 = cite_hint('My instance', ART00)

A: cite_hint(int, ART00, ART01) = 0
"""An universal constant."""

@cite(ART00)
class Bar:
    """The Bar class."""
    
@cite(ART00, ART01)
def foo(a: int, b: int) -> int:
    """The foo function."""
    return a // b
```

## Résultat

La fonction `cite_module` et les décorateurs `@cite` ont complété dynamiquement les *docstrings* du module, des classes,
des méthodes et des fonctions au chargement du module de sorte que la bibliographie est affichée dans leur documentation
lorsque la méthode `help` est invoquée sur ces entitées. Par exemple:

```
>>> help(foo)
Help on function foo in module learning.bibliograpy.example1:
foo(a: int, b: int) -> int
    The foo function.
    Bibliography:
    * the best article written ever [art00]
    * an alternative to the best article written ever [art01]
```

On peut aussi comparer le code source final avec la version initiale.

Les références sont factorisées, réutilisées, maintenables et partageables à l'extérieur du code source. Les références
ont été enrichies d'informations supplémentaires qui ne sont pas pour autant affichées dans la documentation des entités
qui s'y réfèrent.

Enfin, le code source se trouve assaini d'un grand nombre de caractères redondants qui répétaient les mêmes titres
de références bibliographiques et nuisaient à la lisibilité de l'ensemble. La redondance est réduite au minimum par
la simple utilisation des objets de bibliographie, ce qui ne peut qu'iniciter à enrichir le code par des références
nombreuses.

Enfin, un module utilisant le symbole d'une resource bibliographique inexistante produira une erreur au chargement, 
permettant de tester facilement la cohérence de la bibliographie utilisée.
