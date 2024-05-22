import math


class Constant:
    PI = math.pi
    E = math.e

    def __setattr__(self, key, value):
        raise AttributeError('coucou ! tu ne peux pas modifier cette valeur !')


print(Constant.PI)  # on peut passer par la classe
constant = Constant()
print(constant.PI)  # ou par une instance
# constant.PI = 2  # on a bloqué l'affectation de la valeur au niveau de l'instance
Constant.PI = 2  # mais on peut toujours passer par la classe pour modifier la valeur !!
print(constant.PI)  # et cela affecte aussi les instances déjà créées
