# -*- coding: utf-8 -*-
from __future__ import division

"""
Dieses Skript besteht im wesentlichen aus der Lösung der Aufgabe 2 von Kurs02b
Es ist um Plotfunktionen erweitert.
"""

from scipy.integrate import odeint
from scipy.optimize import fmin
import matplotlib.pyplot as plt
import numpy as np

# import unserer Differentialgleichungen
from lagrange_lsg import xdd_fnc2, phidd_fnc2

# Zeitachse und Startwerte fuer den Solver
t = np.linspace(1, 10, 101)

# Referenz-Datensatz, auf den das Modell optimiert werden soll
# Daten im Binärformat laden
target = np.load('messdaten.npy')

x0 = target[0, :]  # erste Zeile der Messdaten -> Anfangswert

# Leere Liste zum Sammeln der Zwischenergebnisse der Optimierung anlegen:
resList = []


def min_target(p):
    m2, l = p

    def rhs(z, t):
        x, phi, xd, phid = z  # Entpacken
        F = 0

        # m2 und l kommen aus dem Namensraum eine Ebene höher
        xdd = xdd_fnc2(x, phi, xd, phid, F, m2, l)
        phidd = phidd_fnc2(x, phi, xd, phid, F, m2, l)

        return np.array([xd, phid, xdd, phidd])

    res = odeint(rhs, x0, t)

    # Zwischenergebnisse merken (an Liste anhängen)
    resList.append(res)

    # Differenz der x-Positionen bilden (jeweils erste Spalte) und quadrieren

    err = np.sum((res[:, 0] - target[:, 0]) ** 2)
    print("Simulation finished. p = {},  Error = {}".format(p, err))
    # x, phi, xd, phid = res.T

    return err


## Um bei wiederholter Ausführung (z.B. zur Anpassung der Plots)
## Zeit zu sparen, sollte man das Ergebnis der Simulation speichern.
## Hier wird das Serialisierungsmodul pickle benutzt.
## Damit können (fast) beliebige Pythonobjekte persistent gespeichert
## werden. Siehe https://docs.python.org/3/library/pickle.html

## Alternativ bieten sich für numerische Daten natürlich auch die
## Funktionen numpy.save und numpy.load an.

## Generell ist eine Trennung von (aufwendiger) Datenerzeugung und
## Visualisierung oftmals sehr sinnvoll.

import pickle  # Serialisierungsmodul

pfname = "res_list.pcl"  # Dateiname beliebig

## Nach dem erfolgreichen speichern hier eine 0 einsetzten:
if 0:
    # Optimierung - Ergebnis sind die zwei Parameter m2 und l

    # Startwerte fuer Optimierung
    p0 = [.5, .7]

    # Durchführen der Optimierung
    p_res = fmin(min_target, p0)

    myfile = open(pfname, 'wb')  # Datei zum Schreiben öffnen (Binär-Modus)
    pickle.dump(resList, myfile)  # resList wird serialisiert u. gespeichert
    myfile.close()
    print("Simulationsdaten erfolgreich gespeichert:", pfname)
    print("Programm-Ende")
    import sys

    sys.exit()
else:
    # Berechnungsergebnisse laden
    myfile = open(pfname, 'rb')  # Datei zum Lesen öffnen (Binär-Modus)
    resList = pickle.load(myfile)
    myfile.close()

# -------------------------------------------------------------------------------
# Aufgabe 1: Messwerte, Optimierungsergebnis und Fehler plotten (3x1 Anordnung)
# -------------------------------------------------------------------------------

mm = 1. / 25.4  # mm -> Zoll
fig = plt.figure(figsize=(300 * mm, 170 * mm))

# Subplot fuer Anfangswerte
ax1 = fig.add_subplot(3, 1, 1)
ax1.plot(t, target[:, 0], label='Messung')
ax1.plot(t, resList[0][:, 0], label='Modell (Startschätzung)')
ax1.legend()
ax1.grid()
ax1.set_ylabel('Weg x [m]')

# Subplot fuer Optimierungsergebnise
ax2 = fig.add_subplot(3, 1, 2)
ax2.plot(t, target[:, 0], lw=3, label='Messung')
ax2.plot(t, resList[-1][:, 0], label='Modell optimiert')
ax2.legend()
ax2.grid()
ax2.set_ylabel('Weg x [m]')

# Subplot fuer Restfehler der Position x
ax3 = fig.add_subplot(3, 1, 3)
ax3.plot(t, target[:, 0] - resList[-1][:, 0])
ax3.grid()
ax3.set_xlabel('Zeit [s]')
ax3.set_ylabel('Fehler $\epsilon$ [m]')
# plt.show()

# -------------------------------------------------------------------------------
# Aufgabe 2: Verlauf der Optimierung (2D)
# -------------------------------------------------------------------------------

fig = plt.figure(figsize=(300 * mm, 170 * mm))

# Plotten aller Zwischenergebnisse in verschiedenen Grautönen (0.1 < col < 0.8)
for i in range(len(resList) - 1):
    colStep = 0.9 / len(resList)
    gray_value = str(0.01 + (0.9 - i * colStep))

    plt.plot(t, resList[i][:, 0], color=gray_value)

# Plotten der Messung und der Simulation
plt.plot(t, target[:, 0], color='#3366FF', lw=4, label='Messung')
plt.plot(t, resList[-1][:, 0], color='#FF9900', ls='--', lw=2, label='Modell optimiert')
plt.grid()
plt.legend()
plt.xlabel('Zeit [s]')
plt.ylabel('Weg x [m]')

# plt.show()

# -------------------------------------------------------------------------------
# Aufgabe 3 Zusatz: Verlauf der Optimierung (3D)
# -------------------------------------------------------------------------------

from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm
from pylab import meshgrid

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection='3d')

x_res = [i[:, 0] for i in resList]

Z = np.vstack(x_res).T
X, Y = meshgrid(range(len(resList)), t)

ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.viridis)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.show()
