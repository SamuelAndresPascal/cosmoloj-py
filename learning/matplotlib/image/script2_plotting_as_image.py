import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

img = np.asarray(Image.open('stinkbug.png'))
imgplot = plt.imshow(img)

plt.show()
