from PIL import Image
import numpy as np

img = np.asarray(Image.open('stinkbug.png'))
print(repr(img))
