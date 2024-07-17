from scipy import stats
import numpy as np

import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 1)
mean, var, skew, kurt = stats.expon.stats(moments='mvsk')

x = np.linspace(stats.expon.ppf(0.01), stats.expon.ppf(0.99), 100)
ax.plot(x, stats.expon.pdf(x), '-', lw=2, label='expon pdf', color='green')
ax.plot(x, stats.expon.cdf(x), '--', lw=2, label='expon cdf', color='green')
print(stats.expon.stats(moments='mvsk'))

x = np.linspace(stats.expon.ppf(0.01, loc=0.3, scale=2), stats.expon.ppf(0.99, loc=0.3, scale=2), 100)
ax.plot(x, stats.expon.pdf(x, loc=0.3, scale=2), '-', lw=2, label='expon pdf', color='blue')
ax.plot(x, stats.expon.cdf(x, loc=0.3, scale=2), '--', lw=2, label='expon cdf', color='blue')
print(stats.expon.stats(moments='mvsk', loc=0.3, scale=2))
#ax.plot(x, norm.ppf(x), 'r-', lw=5, alpha=0.6, label='norm cdf')

plt.show()
