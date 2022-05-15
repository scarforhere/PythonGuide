# coding: utf-8
"""
-------------------------------------------------
   Project :       PythonGuide
   File Name :     Scipy
   Author :        Scar
   E-mail :        scarforhere@gmail.com
   Date：          2021-05-09 11:14 PM
-------------------------------------------------
Description : 

    回归
    求近似值

    Ordinary Differential Equations Operation (DGL-Integrator)
        Die Funktion odeint(rhs, xx0, tt) erwartet drei Parameter:
            1. Eine Funktion der rechten Seite der DGL also  f(x,t) ,
            2. den Anfangszustand  x0 ,
            3. einen array mit Zeitpunkten bei denen die Lösung ausgewertet werden soll.

        rhs: ("right hand side" der DGL)

    – Daten-Ein- u. Ausgabe (z.B. mat-Format (Matlab))
    – Physikalische Konstanten
    – Noch mehr lineare Algebra
    – Signalverarbeitung (Fouriertransformation, Filter, ...)
    – Statistik
    – Optimierung
    – Interpolation
    – Numerische Integration („Simulation“)


    • http://www.scipy.org/Tentative_NumPy_Tutorial
    • http://www.scipy.org/NumPy_for_Matlab_Users
    • https://docs.scipy.org/doc/numpy/user/basics.broadcasting.html
    • http://scipy.org/Numpy_Example_List_With_Doc (umfangreich)
    • http://docs.scipy.org/doc/scipy/reference/ (Tutorial + Referenz)
    • http://www.scipy.org/Cookbook

"""
"""
Besonders nützlich: fsolve und fmin
    • fsolve: findet Nullstelle einer skalaren Funktkion f : R --> R 
                oder eines (nichtlinearen) Gleichungssystems f : R --> R 
    • fmin: findet Minimum einer Funktion f : R --> R 
    • Bei beiden: Startschätzung wichtig
"""
# Beispiel: Näherungslösung der Gl. x + 2.3 * cos(x) = 1

import numpy as np
from scipy import optimize


# 求解近似值
def fnc1(x):
    return x + 2.3 * np.cos(x) - 1


sol = optimize.fsolve(fnc1, 0)  # -> array([-0.723632])
# Probe:
sol + 2.3 * np.cos(sol)  # -> array([ 1.])

"""
Bsp. harmonischer Oszillator mit DGL
"""
import numpy as np
from scipy.integrate import odeint

delta = .1
omega_2 = 2 ** 2


def rhs(z, t):
    """ rhs heißt 'right hand side [function]' """
    z1, z2 = z  # Entpacken
    z1_dot = z2
    z2_dot = -(2 * delta * z2 + omega_2 * z1)
    return [z1_dot, z2_dot]


tt = np.arange(0, 100, .01)  # unabhängige Variable (Zeit)
z0 = [10, 0]  # Anfangszustand fuer y, und y_dot
zz = odeint(rhs, z0, tt)  # Aufruf des Integrators

# zz=
# [
#     [z1_dot_01, z2_dot_01],
#     [z1_dot_02, z2_dot_02],
#     [z1_dot_03, z2_dot_03]
# ]

from matplotlib import pyplot as plt

plt.plot(tt, zz[:, 0])

"""
Beispielskript zu den Themen
 * Interpolation
 * Splines
"""
import numpy as np
import pylab as pl

# ipython Hilfsmodul:
from ipydex import IPS

# Quelle: http://www.scipy.org/Cookbook/LinearRegression
# angepasst
"""
    Interpolation:

        siehe auch: http://docs.scipy.org/doc/scipy/reference/tutorial/interpolate.html
        
        normalerweise sollten alle imports an den Anfang,
        aber damit man sieht, dass man das erst hier braucht:
"""
# Example 1
from scipy.interpolate import interp1d

# Sample data creation
# number of points
n = 10
t = np.linspace(-5, 5, n)

# parameters
a = 0.02;
b = 0.8;
c = -1
x = np.polyval([a, b, c], t)  # alternativ: x = a*t+b

# add some noise
x_noise = x + 0.4 * np.random.randn(n)

func1 = interp1d(t, x_noise)  # kind = 'linear' ist standard
func0 = interp1d(t, x_noise, kind='nearest')  # Ordnung 0 ist 'nearest' (neighbor)
func3 = interp1d(t, x_noise, kind=3)  # kubischer spline

t_highres = np.linspace(t[0], t[-1], 100)

xi0 = func0(t_highres)
xi1 = func1(t_highres)
xi3 = func3(t_highres)

# plotten
# neues Bild
mm = 1. / 25.4  # mm to inch
fs = [90 * mm, 60 * mm]
pl.figure(figsize=fs)  # benutzerdef. Bildgröße erzwingen

pl.plot(t, x_noise, 'ro', )  # Daten
pl.plot(t_highres, xi0, 'bo', ms=2)
pl.plot(t_highres, xi1, 'g', lw=1.3)
# pl.savefig('bsp3_4.pdf')
pl.plot(t_highres, xi3, 'k-', lw=2)
# pl.savefig('bsp3_5.pdf')


# Example 2
import numpy as np
import scipy.interpolate as ip
import matplotlib.pyplot as plt
pl.figure(figsize=fs)  # benutzerdef. Bildgröße erzwingen
# Ausgangs-Daten
x = [1, 2, 3, 4]
y = [2, 0, 1, 3]
plt.plot(x, y, "bx") # Blaue Kreuze
# plt.savefig("interpolation0.pdf")
# Interpolator-Funktion erstellen (linear)
fnc1 = ip.interp1d(x, y)
# Höherer x-Auflösung erreichen durch Auswertung von fnc1
xx = np.linspace(1, 4, 20)
plt.plot(xx, fnc1(xx), "r.-") # rote Punkte, solide Linie


"""
    "Smoothing Spline":

        siehe auch: http://www.scipy.org/Cookbook/Interpolation
"""
from scipy.interpolate import splrep, splev

# spline parameters
s = 0.4  # smoothness parameter
k = 2  # spline order
nest = -1  # estimate of number of knots needed (-1 = maximal)

tck = splrep(t, x_noise, s=s, k=k)
tck2 = splrep(t, x_noise, s=0.0, k=k)

# evaluate spline, including interpolated points
t_highres = np.linspace(t[0], t[-1], 100)
xspline = splev(t_highres, tck)
xspline2 = splev(t_highres, tck2)

# neues Bild
pl.figure(figsize=fs)  # benutzerdef. Bildgröße erzwingen

pl.plot(t, x_noise, 'ro')  # Daten
pl.plot(t_highres, xspline, lw=1.5)
# pl.savefig('bsp3_6.pdf')
pl.plot(t_highres, xspline2, 'g--', lw=2)
# pl.savefig('bsp3_7.pdf')

pl.show()
