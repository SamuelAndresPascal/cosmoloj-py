import matplotlib.pyplot as plt
from PIL import Image

img = Image.open('stinkbug.png')

img.thumbnail((64, 64))  # resizes image in-place
imgplot = plt.imshow(img)

plt.show()
