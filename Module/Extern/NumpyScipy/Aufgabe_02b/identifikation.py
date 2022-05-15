# -*- coding: utf-8 -*-
from __future__ import division

import numpy as np
import sys

# odeint importieren
from scipy.integrate import odeint

from lagrange_lsg import xdd_fnc2, phidd_fnc2

t = np.linspace(1, 10, 101)

# Daten im Binärformat laden
res_target = np.load('messdaten.npy')

## alternativ: Text-Format:
# res_target = np.loadtxt('messdaten.txt')

x0 = res_target[0, :]  # erste Zeile der Messdaten -> Anfangswert


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

    ## Differenz der x-Positionen bilden (jeweils erste Spalte) und quadrieren

    err = np.sum((res[:, 0] - res_target[:, 0]) ** 2)
    print("simulation ready. p=", p, " Error:", err)
    # x, phi, xd, phid = res.T

    return err


p0 = np.array([.3, .5])  # Startschätzung

from scipy.optimize import fmin

p_res = fmin(min_target, p0)
print("Berechnete Parameter:", p_res)
