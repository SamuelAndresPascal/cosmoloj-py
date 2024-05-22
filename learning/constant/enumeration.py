import math
from enum import Enum


class Constant(Enum):
    PI = math.pi
    E = math.e


print(Constant.PI)
print(Constant.PI.value)  # il faut passer par la valeur !
# Constant.PI = 2  # AttributeError : en revanche on obtient des constantes qui ne sont pas réassignables
