from collections import namedtuple

Constant = namedtuple("Constant", ["PI", "E"])
constants = Constant(3.141592653589793, 2.718281828459045)  # problème conceptuel à définir une seule instance de tuple

print(constants.PI)
print(constants.E)
constants.PI = 2  # AttributeError : on est bien immutable
