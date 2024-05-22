import math
from dataclasses import dataclass


@dataclass(frozen=True)
class Constant:
    PI = math.pi
    E = math.e


constant = Constant()
print(constant.PI)
# constant.PI = 2  # la modification du champ est protégée à l'échelle de l'instance
print(Constant.PI)  # on peut y accéder sans passer par une instance
Constant.PI = 2  # mais on peut aussi la modifier par ce moyen !!
print(Constant.PI)
print(constant.PI)  # et cela modifie les valeurs des instances prédédemment créées
print(Constant().PI)  # de même que des instances créées ensuite !
