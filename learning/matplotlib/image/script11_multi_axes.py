import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

fig, ax = plt.subplots(1, 3)

img = np.asarray(Image.open('stinkbug.png'))
lum_img = img[:, :, 2]

ax[0].hist(lum_img.ravel(), bins=range(256), fc='k', ec='k')

raw = ax[1].imshow(lum_img)
fig.colorbar(raw, ax=ax[1])

lim = ax[2].imshow(lum_img, clim=(0, 175))
fig.colorbar(lim, ax=ax[2])
#ax[2].colorbar()

plt.show()
