#! /usr/bin/env python
# -*- coding: utf-8 -*-


# adapted from source: http://numba.pydata.org/numba-doc/dev/user/examples.html

from matplotlib.pyplot import imshow, show, cm, savefig
import matplotlib.pyplot as plt
import numpy as np

import time


def mandel(x, y, max_iters):
    """
    Given a complex number x + y*j, determine
    if it is part of the Mandelbrot set given
    a fixed number of iterations.
    """
    i = 0
    c = complex(x, y)
    z = 0.0j
    for i in range(max_iters):
        z = z*z + c
        if (z.real*z.real + z.imag*z.imag) >= 1e3:
            return i

    return 255


def create_fractal(min_x, max_x, min_y, max_y, image, iters):
    height = image.shape[0]
    width = image.shape[1]

    pixel_size_x = (max_x - min_x) / width
    pixel_size_y = (max_y - min_y) / height
    for x in range(width):
        real = min_x + x * pixel_size_x
        for y in range(height):
            imag = min_y + y * pixel_size_y
            color = mandel(real, imag, iters)
            image[y, x] = color

    return image

dt_results = []
for r in range(1, 6):
    res = r*100
    image = np.zeros((res, res), dtype=np.uint8)

    xmin, xmax, ymin, ymax = -2.0, 1.0, -1.0, 1.0

    t0 = time.time()
    create_fractal(xmin, xmax, ymin, ymax, image, 255)
    dt = time.time()-t0
    print("res = {}; Benötigte Zeit: {}".format(res, dt))
    dt_results.append((res, dt))

    # Zeit zur Erstellung des Bildes wird nicht mit berechnet
    plt.figure()
    # set special colormap
    imshow(image, extent=(xmin, xmax, ymin, ymax), cmap=cm.plasma)

# Umwandlung von [(1, a), (2, b), (3, c), ...] in [[1, 2, 3, ...], [a, b, c, ...]]
# siehe https://docs.python.org/3.4/library/functions.html#zip
res_list, dt_list = zip(*dt_results)
plt.figure()
plt.plot(res_list, dt_list, 'b.-')
plt.xlabel("Auflösung")
plt.ylabel("Rechenzeit")

show()
