# coding: utf-8
"""
-------------------------------------------------
   Project :       PythonGuide
   File Name :     aufgabe_03a
   Author :        Scar
   E-mail :        scarforhere@gmail.com
   Date：          2021-05-12 02:59 PM
-------------------------------------------------
Description : 

    Description

"""
from __future__ import division

from sympy import sin, cos, Function
import sympy as sp

"""
Diese Datei beinhaltet die Lösung von Übung 02a, sowie eine Erweiterung,
die für Übung 02b, Teil2 benötigt wird
"""

t = sp.Symbol('t')

params = sp.symbols('m1, m2, l, g')
m1, m2, l, g = params

xt = Function('x')(t)  # x(t)
phit = Function('phi')(t)  # phi(t)

xdt = xt.diff(t)
phidt = phit.diff(t)
xddt = xt.diff(t, 2)
phiddt = phit.diff(t, 2)

# Hilfsrechnung

x2t = xt + l * sin(phit)
y2t = -l * cos(phit)

x2dt = x2t.diff(t)
y2dt = y2t.diff(t)

# kinetische Energie
T = (m1 * xdt ** 2 + m2 * (x2dt ** 2 + y2dt ** 2)) / 2

# Potentielle Energie
U = y2t * g * m2

L = T - U  # Lagrange-Funktion

# Funktionen durch Symbole ersetzen

x_s, phi_s, xd_s, phid_s = sp.symbols('x_s, phi_s, xd_s, phid_s')

# Reihenfolge ist hier wichtig. Höhere Ableitungen zuerst substituieren.
subs_list1 = [(xdt, xd_s), (phidt, phid_s), (xt, x_s), (phit, phi_s)]
L = L.subs(subs_list1)  # subs Funktionen -> Symbole
L = L.expand()
L = sp.trigsimp(L)

# --- Lagrange-Gleichungen ---
# Hilfsterme:


L_d_x = L.diff(x_s)
L_d_phi = L.diff(phi_s)

L_d_xd = L.diff(xd_s)
L_d_phid = L.diff(phid_s)

xdd_s, phidd_s = sp.symbols('xdd_s, phidd_s')

# sub_slist ergänzen (wieder Reihenfolge beachten: höhere Ableitungen vorn hin)
subs_list1 = [(xddt, xdd_s), (phiddt, phidd_s)] + subs_list1

# Liste umkehren (subs Symbole -> Funktionen)
subs_list_rev = [(tup[1], tup[0]) for tup in subs_list1]

# L_d_x = L_d_x.subs(subs_list_rev)
# L_d_phi = L_d_phi.subs(subs_list_rev)

L_d_xd = L_d_xd.subs(subs_list_rev)
L_d_phid = L_d_phid.subs(subs_list_rev)

DL_d_xd = L_d_xd.diff(t).subs(subs_list1)
DL_d_phid = L_d_phid.diff(t).subs(subs_list1)

F = sp.Symbol('F')  # eingeprägte Last (translatorisch)

# Gleichungen

Eq1 = DL_d_xd - L_d_x - F
Eq2 = DL_d_phid - L_d_phi

# sp.preview(Eq1)
# sp.preview(Eq2)


sol = sp.solve([Eq1, Eq2], xdd_s, phidd_s)

# Gleichungen Umformen für Simulation


params_values = {m1: 0.8, m2: 0.3, l: 0.5, g: 9.81}

xdd_expr = sol[xdd_s].subs(params_values)
phidd_expr = sol[phidd_s].subs(params_values)

# Funktionen für die numerische Berechnung der Beschleunigungen

xdd_fnc = sp.lambdify([x_s, phi_s, xd_s, phid_s, F], xdd_expr, 'numpy')
phidd_fnc = sp.lambdify([x_s, phi_s, xd_s, phid_s, F], phidd_expr, 'numpy')

## xdd_fnc und phi_dd_fnc sind ausführbare bzw. aufrufbare-Objekte
## ("callable objects")
## Es sind Funktionen, die fünf Argumente bekommen und einen Wert zurrückgeben.


## Für Aufgabe 2:
## m2 und l nicht mit numerischen Werten ersetzen, sondern diese
## Variablen als Parameter übergeben

params_values2 = {m1: 0.8, g: 9.81}
xdd_expr2 = sol[xdd_s].subs(params_values2)
phidd_expr2 = sol[phidd_s].subs(params_values2)

# Funktionen für die numerische Berechnung der Beschleunigungen

## jetzt mit zusätzlicher Abhängigkeit von m2 und l

xdd_fnc2 = sp.lambdify([x_s, phi_s, xd_s, phid_s, F, m2, l], xdd_expr2, 'numpy')
phidd_fnc2 = sp.lambdify([x_s, phi_s, xd_s, phid_s, F, m2, l], phidd_expr2, 'numpy')


def preview(expr, **kwargs):
    """
     Hilfsfunktion zur "schönen" Anzeige umfangreicher Ausdrücke
     """

    import matplotlib.pyplot as plt
    latex_str = "$ %s $" % sp.latex(expr, **kwargs)
    latex_str = latex_str.replace("operatorname", "mathrm")
    plt.text(0.5, 0.5, latex_str, fontsize=30, horizontalalignment='center')
    plt.axis('off')
    plt.show()


if __name__ == "__main__":
    # Dieser Block wird nur ausgeführt, wenn diese Datei das Haupt-Skript ist,
    # nicht wenn sie als Modul woanders importiert wird.

    # Anzeigen:

    ## sp.Eq -> sympy Equation object

    Eq1a = sp.Eq(xdd_s, sol[xdd_s])
    Eq2a = sp.Eq(phidd_s, sol[phidd_s])

    # Symbolbenennung in LaTeX-Notation
    sn_dict = {phi_s: r'\varphi', phid_s: r'\dot{\varphi}',
               xdd_s: r'\ddot{x}', phidd_s: r'\ddot{\varphi}'}

    preview(Eq1a, symbol_names=sn_dict)
    preview(Eq2a, symbol_names=sn_dict)
