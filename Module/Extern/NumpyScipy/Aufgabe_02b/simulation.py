# -*- coding: utf-8 -*-
from __future__ import division

import sys
import numpy as np
from numpy import r_, pi
import pylab as pl  # für das Plotten am Ende

# odeint aus dem Paket scipy importieren:
from scipy.integrate import odeint

# Funktionen zur Berechnung der Beschleunigungen importieren:
from lagrange_lsg import xdd_fnc, phidd_fnc


def rhs(z, t):
    # Diese Funktion berechnet aus dem Zustand z die Zeitableitung z_dot
    # das 2. Argument (die Zeit t) wird hier nicht benötigt

    x, phi, xd, phid = z  # Entpacken (siehe ggf. Kurs 1a, Syntax-Übersicht, Folie 17 u. 21)
    F = 0

    xdd = xdd_fnc(x, phi, xd, phid, F)
    phidd = phidd_fnc(x, phi, xd, phid, F)

    z_dot = r_[xd, phid, xdd, phidd]
    # equal: z_dot = np.array([xd, phid, xdd, phidd])

    return z_dot


t = np.linspace(1, 10, 101)

x0 = r_[0, pi * 3 / 4, 0, 0]
# equal: z_dot = np.array([0, pi * 3 / 4, 0, 0])

res = odeint(rhs, x0, t)

# res: Spalten -> Zustandskomponenten, Zeilen -> Zeitschritte

# Entpacken der einzelnen Zustandskomponenten.
# Dazu Zeilen u. Spalten vertauschen (Transponieren)

# x, phi, xd, phid = res.T
x, phi, xd, phid = res.T

# Grafische Darstellung:
pl.plot(t, x)
pl.plot(t, phi)
pl.show()

## "Pseudo-Messdaten" für Aufgabe 2 generieren
## der Block wird nicht ausgeführt, lässt sich aber schnell in "aktiven Code"
## umwandeln (0 durch 1 ersetzen)

if 0:
    # Binärformat:
    np.save('messdaten.npy', res)
    # Textfomat (Menschenlesbar, braucht aber mehr Speicherplatz):
    np.savetxt('messdaten.txt', res)

    print("Files written.")
