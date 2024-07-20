import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

img = np.asarray(Image.open('stinkbug.png'))
lum_img = img[:, :, 2]

plt.figure(1)
plt.hist(lum_img.ravel(), bins=range(256), fc='k', ec='k')

plt.figure(2)
plt.imshow(lum_img)
plt.colorbar()

plt.figure(3)
plt.imshow(lum_img, clim=(0, 175))
plt.colorbar()

plt.show()
