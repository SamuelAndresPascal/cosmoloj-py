import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
from scipy import signal
from scipy.ndimage import shift

delta = 1 / (24 * 60)
period = 5
big_grid = np.arange(-50, 50, delta)

#dist1 = stats.uniform(loc=2, scale=3)
#dist2 = stats.norm(loc=0, scale=0.25)
dist1 = stats.norm(loc=0, scale=0.5)

pmf1 = dist1.pdf(big_grid) * delta

target_nb = 11
convolutions = [pmf1]

for i in range(1, target_nb):
    convolutions.append(signal.fftconvolve(convolutions[i - 1], pmf1, mode='same'))
    print("Sum of convoluted pmf: " + str(sum(convolutions[i])))

for i, _ in enumerate(convolutions):
    convolutions[i] = shift(convolutions[i] / delta, period / delta * i)


#plt.plot(big_grid, pdf1, label='distribution 1')
#plt.plot(big_grid, pdf2, label='distribution 2')
#plt.plot(big_grid, pdf3, label='distribution 23')
#plt.plot(big_grid, dist1.pdf(big_grid - period * 0), label='source 1')
#plt.plot(big_grid, dist1.pdf(big_grid - period * 1), label='source 2')
#plt.plot(big_grid, dist1.pdf(big_grid - period * 2), label='source 3')
#plt.plot(big_grid, pdf_conf_2_1, label='2 sachant 1')
#plt.plot(big_grid, pdf_conf_3_2_1, label='3 sachant 2 sachant 1')
plt.plot(big_grid, sum(convolutions), label='total')
plt.legend(loc='best'), plt.suptitle('PDFs')
plt.show()
