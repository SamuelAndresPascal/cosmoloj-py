import numpy as np

import matplotlib.pyplot as plt


def mandelbrot(h: int, w: int, maxit: int = 20, r: int = 2):
    """Returns an image of the Mandelbrot fractal of size (h,w)."""

    x = np.linspace(start=-2.5, stop=1.5, num=4 * h + 1)
    y = np.linspace(start=-1.5, stop=1.5, num=3 * w + 1)
    A, B = np.meshgrid(x, y)
    C = A + B * 1j
    z = np.zeros_like(C)
    divtime = maxit + np.zeros(z.shape, dtype=int)

    for i in range(maxit):

        z = z**2 + C
        diverge = abs(z) > r                    # who is diverging
        div_now = diverge & (divtime == maxit)  # who is diverging now
        divtime[div_now] = i                    # note when
        z[diverge] = r                          # avoid diverging too much

    return divtime


plt.clf()
plt.imshow(mandelbrot(h=400, w=400))
plt.show()
