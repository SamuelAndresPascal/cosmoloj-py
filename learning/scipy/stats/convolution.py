import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
from scipy import signal
from scipy.ndimage import shift

MINUTES_IN_DAY = 24 * 60
WEIGHT = 1 / MINUTES_IN_DAY  # assuming the target freq. unit to be the day, require one prob to have a "minute" weight
PERIOD = 7 * MINUTES_IN_DAY  # period in days converted to minutes for shifting curves purpose
TARGET_NB = 10

# P(t) avec t l'écart temporel entre le déclenchement de l'événement
# ét l'instant de déclenchement de l'événement précédent augmenté de la période
#
# Donc t=0 correspond à l'instant de déclenchement de l'événement précédent augmenté de la période. C'est l'instant
# de déclenchement théorique de l'événement.
#
# Si on pose t_n l'écart temporel entre le déclenchement de l'événement du cycle n
# et l'instant de déclenchement de l'événement au cycle n-1 augmenté de la période, la famille des événements t_n
# respecte donc la relation : P(t_n) = P(t_n | t_n-1)
#
# On a donc :
# P(t_n and t_n-1) = P(t_n | t_n-1) * P(t_n-1) = P(t_n) * P(t_n-1) et donc indépendance entre les variables aléatoires
#
# P(t_n) suppose que t_n-1 est réalisé et suit do
# P(t_n) et P(t_n-1) sont indépendants car par définition P(t_n) = P(t_n | t_n-1)

COMB = np.arange(start=-100, stop=100, step=WEIGHT)
ASYMPTOTE = COMB.copy()
ASYMPTOTE.fill(1 / PERIOD)

DISTRIBUTION_0 = stats.norm(scale=0.75)

# get pdf + discretisation to pmf
PMF_0 = DISTRIBUTION_0.pdf(COMB) * WEIGHT

distributions = [PMF_0]

for i in range(1, TARGET_NB):
    distributions.append(signal.convolve(distributions[i - 1], PMF_0, mode='same'))
    print("Sum of convoluted pmf: " + str(sum(distributions[i])))


# to pdf values ("undiscretisation")
for distribution in distributions:
    distribution = distribution / WEIGHT

fig1, ax1 = plt.subplots(1, 3)

for i, c in enumerate(distributions):
    ax1[0].plot(COMB, c, label=f'{i}')
ax1[0].legend(loc='best')

for i, _ in enumerate(distributions):
    distributions[i] = shift(distributions[i], PERIOD * i)

for i, c in enumerate(distributions):
    ax1[1].plot(COMB, c, label=f'cycle {i}')
ax1[1].legend(loc='best')

ax1[2].plot(COMB, ASYMPTOTE, label="constant prob")
ax1[2].plot(COMB, sum(distributions), label='total prob')
ax1[2].legend(loc='best')

fig1.suptitle('shifted convolution series')

plt.show()
