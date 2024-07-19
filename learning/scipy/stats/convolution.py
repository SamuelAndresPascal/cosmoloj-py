import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
from scipy import signal
from scipy.ndimage import shift

delta = 1 / (24 * 60)  # assuming the target frequency unit to be the day, require one prob per "minute"
period = 5
big_grid = np.arange(-50, 50, delta)

dist1 = stats.norm(scale=0.5)

pmf1 = dist1.pdf(big_grid) * delta

target_nb = 11
convolutions = [pmf1]

for i in range(1, target_nb):
    convolutions.append(signal.fftconvolve(convolutions[i - 1], pmf1, mode='same'))
    print("Sum of convoluted pmf: " + str(sum(convolutions[i])))

for i, _ in enumerate(convolutions):
    convolutions[i] = shift(convolutions[i] / delta, period / delta * i)

plt.plot(big_grid, sum(convolutions), label='total')
plt.legend(loc='best'), plt.suptitle('PDFs')
plt.show()
