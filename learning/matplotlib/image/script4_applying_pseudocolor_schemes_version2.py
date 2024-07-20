import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

img = np.asarray(Image.open('stinkbug.png'))
lum_img = img[:, :, 2]
plt.imshow(lum_img, cmap="hot")

plt.show()
