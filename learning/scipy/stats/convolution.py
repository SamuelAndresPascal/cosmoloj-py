import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
from scipy import signal
from scipy.ndimage import shift

MINUTES_IN_DAY = 24 * 60
WEIGHT = 1 / MINUTES_IN_DAY  # assuming the target freq. unit to be the day, require one prob to have a "minute" weight
PERIOD = 7 * MINUTES_IN_DAY  # period in days converted to minutes for shifting curves purpose
TARGET_NB = 11

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

for i, c in enumerate(distributions):
    plt.plot(COMB, c, label=f'{i}')

for i, _ in enumerate(distributions):
    distributions[i] = shift(distributions[i], PERIOD * i)

for i, c in enumerate(distributions):
    plt.plot(COMB, c, label=f'cycle {i}')

plt.plot(COMB, ASYMPTOTE, label="constant prob")
plt.plot(COMB, sum(distributions), label='total prob')
plt.legend(loc='best')
plt.suptitle('shifted convolution series')
plt.show()
