import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

img = np.asarray(Image.open('stinkbug.png'))
lum_img = img[:, :, 2]
imgplot = plt.imshow(lum_img)
imgplot.set_cmap('nipy_spectral')
plt.colorbar()

plt.show()
