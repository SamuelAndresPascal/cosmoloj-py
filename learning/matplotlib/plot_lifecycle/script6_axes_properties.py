import matplotlib.pyplot as plt

from learning.matplotlib.plot_lifecycle.data import group_data, group_names

plt.rcParams.update({'figure.autolayout': True})

plt.style.use('fivethirtyeight')

fig, ax = plt.subplots(figsize=(8, 4))
ax.barh(group_names, group_data)
labels = ax.get_xticklabels()
plt.setp(labels, rotation=45, horizontalalignment='right')
ax.set(xlim=[-10000, 140000], xlabel='Total Revenue', ylabel='Company',
       title='Company Revenue')
plt.show()
