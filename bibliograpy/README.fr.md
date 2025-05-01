# Bibliograpy

Bibliograpy est à la fois:

* une API de décoration de code par des références bibliographiques 
* un outil de représentation de références bibliographiques sous la forme d'objets python à partir de formats standards
(Bibtex, RIS, Endnote, Refer, PubMed).

**Bibliograpy n'est pas un outil de conversion de bibliographies entre des formats standards.**

[![example workflow](https://github.com/SamuelAndresPascal/cosmoloj-py/actions/workflows/bibliograpy.yml/badge.svg)](https://github.com/SamuelAndresPascal/cosmoloj-py/actions)

[![Anaconda-Server Badge](https://anaconda.org/cosmoloj/bibliograpy/badges/version.svg)](https://anaconda.org/cosmoloj/bibliograpy)
[![Anaconda-Server Badge](https://anaconda.org/cosmoloj/bibliograpy/badges/latest_release_date.svg)](https://anaconda.org/cosmoloj/bibliograpy)
[![Anaconda-Server Badge](https://anaconda.org/cosmoloj/bibliograpy/badges/latest_release_relative_date.svg)](https://anaconda.org/cosmoloj/bibliograpy)
[![Anaconda-Server Badge](https://anaconda.org/cosmoloj/bibliograpy/badges/platforms.svg)](https://anaconda.org/cosmoloj/bibliograpy)
[![Anaconda-Server Badge](https://anaconda.org/cosmoloj/bibliograpy/badges/license.svg)](https://anaconda.org/cosmoloj/bibliograpy)

[![PyPI repository Badge](https://badge.fury.io/py/bibliograpy.svg)](https://badge.fury.io/py/bibliograpy)

* PURPOSE
  * INTRO
  * PRESENTATION - IDÉAL
  * 

## Utiliser des références bibliographiques dans du code source

Un code source élégant, rigoureux, raisonnablement documenté peut être vu comme une documentation exécutable. À ce titre
on souhaiterait y indiquer les ressouces bibliographiques auxquelles il se réfère de manière aussi simple qu'on le fait
dans un article même: une simple annotation par une clef bibliographique dans le texte renvoyant à la référence 
détaillée dans une bibliographie centralisée, une même référence pouvant aisément être souvent utilisée dans le texte
par le truchement de sa clef.

Sans outil dédié, la manière la plus intuitive de référencer des ressources bibliographiques dans du code source 
consiste à les énumérer dans la documentation des entités concernées (classes, fonctions, constantes).

```python

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
* Corollaire de l'impossibilité de réutiliser les références bibliographiques, leur utilisation à plusieurs occurrences
duplique leur représentation comme chaînes de caractères, accroît les risques de fautes de frappe et complique les 
opérations de maintenance.
* On assimile la ressource bibliographique et sa mise en forme, ce qui contraint à opérer des choix quant
aux informations relatives à la ressource que l'on souhaite indiquer et celles que l'on ne souhaite pas
conserver : il n'y a pas de place pour d'éventuelles informations que l'on souhaiterait conserver mais pas
indiquer dans la documentation.

L'API Bibliograpy permet de représenter les ressources bibliographiques en tant que telles sous une forme réifiée. Les
ressources deviennent des objets utilisables dans le code source, ce qui apporte une réponse à ces différents problèmes.

* La bibliographie est séparée de la rédaction de la documentation. Chaque objet représentant une resource 
bibliographique est réutilisable. Les ressouces bibliographiques ainsi représentées sont associées aux fonctions, aux
classes eet aux méthodes par des décorateurs, aux constantes/variables, aux paramètres via les *hints* du langage.
Décorateurs et *hints* sont résolus au chargement du module. Les décorateurs permettent d'intégrer la bibliographie à 
la documentation, de manière à la rendre disponible au moment son *rendu* (par la fonction `help()` par exemple).
* Toute opération de maintenance relative à une ressource (faute de frappe dans le titre, ajout d'un auteur ou d'un 
sous-titre...) est factorisée à un seul endroit, au moment de l'instanciation de l'objet.
* Un grand nombre d'informations peut-être contenu dans l'objet représentant la ressource bibliographique. Cette
information facile d'accès par navigation dans le code source n'est pas forcément affichée dans son intégralité au 
moment du calcul du *rendu* éventuel dans la docstring éventuel.


Il subsiste toutefois un autre problème. La représentation des ressources bibliographiques sous la forme
d'objets python n'est pas un standard largement partagé. Quoique puissamment factorisée pour son
utilisation dans le code source, cette information n'est pas partageable à l'extérieur du code. En revanche,
il existe pour cela de nombreux formats largement utilisés ouvrant la voie à  plus ou moins une
interopérabilité plus ou moins étendue. Il peut être par exemple intéressant d'utiliser une même base de
références bibliographiques qui serve à la fois dans le code source *et* à d'autres endroits, telles qu'une
documentation en markdown ou au format rst. Des plugins *mkdocs* ou *sphinx*, permettent par exemple
de référencer facilement des resources bibliographiques représentées au format Bibtex.

La solution *simple* à ce problème consiste forcément à partir du format largement accepté pour
maintenir les ressources bibliographiques et donc à permettre de *synchroniser* leur représentation
accessible dans le code source.

