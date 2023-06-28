from learning.mutable.model import MutableNotHashable, MutableHashable, ImmutableHashable

"""Problème : ranger un objet dans un ensemble et le retrouver.
1. Pour le ranger dans l'ensemble il doit être hashable.
2. Pour être certain de le retrouver, le hash ne doit pas changer. La recette classique est l'immuabilité (frozen)

Il ne suffit pas cependant qu'un objet soit hashable et immuable (tuple) mais s'il référence des objets, ceux-ci
doivent l'être aussi !!!

https://docs.python.org/2/glossary.html => hashable
"""


def mutable_not_hashable():

    # On crée un mutable non hashable
    object1 = tuple([MutableNotHashable(id=1)])

    # on place l'objet dans un hashmap
    collection = {object1}  # ==> ERREUR : l'objet n'est pas hashable

    print(object1 in collection)

    object1.id = 2

    print(object1 in collection)


def mutable_hashable():

    # On crée un mutable hashable
    object1 = tuple([MutableHashable(id=1)])

    # on place l'objet dans un hashmap
    collection = {object1}

    # on cherche l'objet dans le hashmap
    print(object1 in collection)

    # on change l'état de l'objet : on peut car il est mutable
    object1[0].id = 2

    # on cherche l'objet dans le hashmap
    print(object1 in collection)  # ==> PROBLÈME : on ne le trouve plus !!!


def immutable_hashable():

    # On crée un mutable hashable
    object1 = tuple([ImmutableHashable(id=1)])

    # on place l'objet dans un hashmap
    collection = {object1: 'Trouvé'}

    # on cherche l'objet dans le hashmap
    print(object1 in collection)

    # on change l'état de l'objet : on peut car il est mutable
    object1[0].id = 2  # ==> ERREUR : l'objet est marqué "FROZEN" et on évite ainsi l'utiliser comme hashable modifié

    # on cherche l'objet dans le hashmap
    print(object1 in collection)


if __name__ == '__main__':
   # mutable_not_hashable()  ## tuple avec mutable non hashable ==> erreur python
   # mutable_hashable()  ## tuple avec mutable hashable ==> pas d'erreur python mais 99% de chances de bug
   # immutable_hashable()  ## tuple avec immutable hashable ==> erreur python qui prévient la modification de l'objet

