import math
from typing import Final

PI: Final[float] = math.pi
E: Final[float] = math.e

print(PI)
PI = 2  # l'alerte n'est que de surface dans l'IDE : l'interpréteur accepte la modification
print(PI)  # aucune sécurité
