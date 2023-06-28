from learning.mutable.model import MutableNotHashable, MutableHashable, ImmutableHashable

"""Problème : ranger un objet dans un ensemble et le retrouver.
1. Pour le ranger dans l'ensemble il doit être hashable.
2. Pour être certain de le retrouver, le hash ne doit pas changer. La recette classique est l'immuabilité (frozen)

Grâce à "frozen", on peut utiliser l'objet comme un hashable tout en évitant des bogues et en aidant l'IDE à
signaler les tentatives de modification d'un objet qui ne doit pas pouvoir l'être.

https://docs.python.org/2/glossary.html => hashable
"""


def mutable_not_hashable():

    # On crée un mutable non hashable
    object1 = MutableNotHashable(id=1)

    # on place l'objet dans un hashmap
    collection = {object1 : 'Trouvé'}  # ==> ERREUR : l'objet n'est pas hashable

    print(collection[object1])

    object1.id = 2

    print(collection[object1])


def mutable_hashable():

    # On crée un mutable hashable
    object1 = MutableHashable(id=1)

    # on place l'objet dans un hashmap
    collection = {object1 : 'Trouvé'}

    # on cherche l'objet dans le hashmap
    print(collection[object1])

    # on change l'état de l'objet : on peut car il est mutable
    object1.id = 2

    # on cherche l'objet dans le hashmap
    print(collection[object1])  # ==> PROBLÈME : on ne le trouve plus ==> ERREUR python (difficile à comprendre) !!!


def immutable_hashable():

    # On crée un mutable hashable
    object1 = ImmutableHashable(id=1)

    # on place l'objet dans un hashmap
    collection = {object1 : 'Trouvé'}

    # on cherche l'objet dans le hashmap
    print(collection[object1])

    # on change l'état de l'objet : on peut car il est mutable
    object1.id = 2  # ==> ERREUR : l'objet est marqué "FROZEN" et on évite ainsi l'utiliser comme hashable modifié

    # on cherche l'objet dans le hashmap
    print(collection[object1])


if __name__ == '__main__':
   mutable_not_hashable()  ## mutable non hashable ==> erreur python
   # mutable_hashable()  ## mutable hashable ==> pas d'erreur python mais 99% de chances de bug
   # immutable_hashable()  ## immutable hashable ==> erreur python qui prévient la modification de l'objet

