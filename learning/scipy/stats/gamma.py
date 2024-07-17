from scipy import stats
import numpy as np

import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 1)

a = 0.9

mean, var, skew, kurt = stats.gamma.stats(moments='mvsk', a=a)

x = np.linspace(stats.gamma.ppf(0.01, a=a), stats.gamma.ppf(0.99, a=a), 100)
ax.plot(x, stats.gamma.pdf(x, a=a), '-', lw=2, label='expon pdf', color='green')
ax.plot(x, stats.gamma.cdf(x, a=a), '--', lw=2, label='expon cdf', color='green')
print(stats.gamma.stats(moments='mvsk', a=a))

x = np.linspace(stats.gamma.ppf(0.01, a=a, loc=0.3, scale=2), stats.gamma.ppf(0.99, a=a, loc=0.3, scale=2), 100)
ax.plot(x, stats.gamma.pdf(x, a=a, loc=0.3, scale=2), '-', lw=2, label='expon pdf', color='blue')
ax.plot(x, stats.gamma.cdf(x, a=a, loc=0.3, scale=2), '--', lw=2, label='expon cdf', color='blue')
print(stats.gamma.stats(moments='mvsk', a=a, loc=0.3, scale=2))
#ax.plot(x, norm.ppf(x), 'r-', lw=5, alpha=0.6, label='norm cdf')

plt.show()
