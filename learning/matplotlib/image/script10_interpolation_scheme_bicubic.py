import matplotlib.pyplot as plt
from PIL import Image

img = Image.open('stinkbug.png')

img.thumbnail((64, 64))
imgplot = plt.imshow(img, interpolation='bicubic')

plt.show()
