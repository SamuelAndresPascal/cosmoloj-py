import matplotlib.pyplot as plt

from learning.matplotlib.plot_lifecycle.data import group_data, group_names, currency, group_mean

plt.rcParams.update({'figure.autolayout': True})

fig, ax = plt.subplots(figsize=(8, 8))
ax.barh(group_names, group_data)
labels = ax.get_xticklabels()
plt.setp(labels, rotation=45, horizontalalignment='right')

# Add a vertical line, here we set the style in the function call
ax.axvline(group_mean, ls='--', color='r')

# Annotate new companies
for group in [3, 5, 8]:
    ax.text(145000, group, "New Company", fontsize=10, verticalalignment="center")

# Now we move our title up since it's getting a little cramped
ax.title.set(y=1.05)

ax.set(xlim=[-10000, 140000], xlabel='Total Revenue', ylabel='Company',
       title='Company Revenue')
ax.xaxis.set_major_formatter(currency)
ax.set_xticks([0, 25e3, 50e3, 75e3, 100e3, 125e3])
fig.subplots_adjust(left=0, right=.1)

plt.show()

print(fig.canvas.get_supported_filetypes())

# uncomment to save the figure
#fig.savefig('sales.png', transparent=False, dpi=80, bbox_inches='tight')
