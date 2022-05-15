# coding: utf-8
"""
-------------------------------------------------
   File Name:      KompilierterCode
   Author :        Scar
   E-mail :        scarforhere@gmail.com
   Date:           2021-05-23 10:26 AM
-------------------------------------------------
Description : 

    Python-Quelltext
        Wird in sog. Bytecode übersetzt und zur Laufzeit vom Interpreter ausgeführt
            -->hohe Flexibilität, aber vergleichsweise geringe Ausführungsgeschwindigkeit

    Kompilierter Code
        Wird in Maschinensprache übersetzt und direkt vom Prozessor verarbeitet
            -->hohe Ausführungsgeschwindigkeit, geringe Flexibilität (z.B. statische Datentypen, Speichermanagement)

    Kombinationsmöglichkeiten (Einbettung von komp. Code in Python):
        ctypes
            – Kann externe Bibliotheken (z.B. *.dll unter Windows) in Python laden
                -->sehr mächtig und flexibel
            – Hier nicht näher betrachtet, siehe ggf.
            https://github.com/cknoll/python-c-code-example

        „Just in Time“-Kompilierung von bestimmten Code-Abschnitten (z.B. Modul numba)

        Übersetzen des Python Codes in cython
            – Sehr ähnlich zu Python aber statisch typisiert und kompiliert
            – Cython ist eigene Programmiersprache, Installation: pip install cython
            – Sehr eng an Python angelehnt aber mit expliziten statischen Typ-Informationen
                --> Kann automatisch nach C übersetzt werden -> kompilierbar -> schneller
            – Details: siehe https://cython.readthedocs.io/en/latest/index.html
            – Vorgehen:
                • Algorithmus in reinem Python entwickeln („Make it run“ + „Make it right“)
                • Python manuell nach Cython übersetzen
                • Cython-Code nach C übersetzen lassen
                • C-Code kompilieren
                • So erstelltes Modul „ganz normal“ importieren / benutzen (-> „Make it fast“)
            – Typischerweise 3 Dateien, z.B.
                – mandel-cython.pyx : Cython-Quelltext
                – mandel-cython-setup.py : Zum Kompilieren
                – mandel-cython-main.py : Zum Importieren u. Aufrufen


"""
# adapted from source: http://numba.pydata.org/numba-doc/dev/user/examples.html

from timeit import default_timer as timer
from matplotlib.pyplot import imshow, show, cm, savefig
import numpy as np

from numba import jit


@jit  # Decorator für just-in-time Kompilierung
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

@jit
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

image = np.zeros((500 * 2, 750 * 2), dtype=np.uint8)
s = timer()
xmin, xmax, ymin, ymax = -2.0, 1.0, -1.0, 1.0

create_fractal(xmin, xmax, ymin, ymax, image, 255)
e = timer()
print(e - s)
# set special colormap
imshow(image, extent=(xmin, xmax, ymin, ymax), cmap=cm.plasma)
#jet()
#ion()
# savefig("mandel.png")
show()
