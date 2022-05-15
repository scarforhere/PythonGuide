from __future__ import division

from sympy import sin, cos, Function
import sympy as sp
import sys

# Aufgabe 1
params = sp.symbols('m1, m2, l, g')
m1, m2, l, g = params

# Aufgabe 2
t = sp.Symbol('t')          # Symbol für die Zeit
xt = Function('x')(t)       # x(t)
phit = Function('phi')(t)   # phi(t)

# Aufgabe 3
xdt = xt.diff(t)
phidt = phit.diff(t)
xddt = xt.diff(t, 2)
phiddt = phit.diff(t, 2)

# Aufgabe 4
x2t = xt + l * sin(phit)  # Hilfsgrößen
y2t = -l * cos(phit)
x2dt = x2t.diff(t)
y2dt = y2t.diff(t)

# Aufgabe 5
T = (m1 * xdt ** 2 + m2 * (x2dt ** 2 + y2dt ** 2)) / 2  # kinetische Energie
U = y2t * g * m2                                        # Potentielle Energie
L = T - U                                               # Lagrange-Funktion
L = L.expand()                                          # Symbolische Vereinfachungen
L = sp.trigsimp(L)

# Aufgabe 6
L_d_x = L.diff(xt)      # Hilfsterme:
L_d_phi = L.diff(phit)
L_d_xd = L.diff(xdt)
L_d_phid = L.diff(phidt)

# Aufgabe 7
DL_d_xd = L_d_xd.diff(t)
DL_d_phid = L_d_phid.diff(t)

# Aufgabe 8
F = sp.Symbol('F')              # eingeprägte Last (translatorisch)
Eq1 = DL_d_xd - L_d_x - F       # Gleichungen
Eq2 = DL_d_phid - L_d_phi
sp.pprint(Eq1)
sp.pprint(Eq2)

# Aufgabe 9
acc = [xddt, phiddt]                # Liste der Beschleunigungen
res = sp.solve([Eq1, Eq2], acc)     # Gleichungen nach den Beschleunigungen auflösen

# Aufgabe 10
msg = "\nDie Variable `res` ist vom Typ: {} und hat folgenden Wert:\n"
print(msg.format(type(res)))
sp.pprint(res)
xdd_expr = res[xddt]
phidd_expr = res[phiddt]

# Aufgabe 11
"""
Erzeugen von Python-Funktionen für die num. Berechnung der Beschleunigungen
Dazu vorher Zeit-Funktionen durch normale Symbole ersetzen und numerische
Parameter-Werte einsetzen.
"""
# Symbole anlegen (bisher hatten wir Funktionen in Abhängigkeit von t):
x, phi, xd, phid, xdd, phidd = sp.symbols('x, phi, xd, phid, xdd, phidd')

# Liste für Ersetzungen (replacements); jeweils Zeitfunktion -> Symbol
# Beachte: Höchste Zeitableitung zuerst substituieren
rplmts = [(xddt, xdd), (phiddt, phidd), (xdt, xd), (phidt, phid),
          (xt, x), (phit, phi)]

params_values = [(m1, 0.8), (m2, 0.3), (l, 0.5), (g, 9.81)]

# Subsititution durchführen und Ergebnis speichern
xdd_expr_num = xdd_expr.subs(rplmts + params_values)
phidd_expr_num = phidd_expr.subs(rplmts + params_values)

# Erzeugung der Python-Fukntionen mittels sp.lambdify
xdd_fnc = sp.lambdify([x, phi, xd, phid, F], xdd_expr_num, modules='numpy')
phidd_fnc = sp.lambdify([x, phi, xd, phid, F], phidd_expr_num, modules='numpy')


# xdd_fnc und phi_dd_fnc sind ausführbare bzw. aufrufbare-Objekte
# ("callable objects")
# Es sind Funktionen, die je fünf Argumente bekommen und einen Wert zurrückgeben.


def preview(expr, **kwargs):
    """
     Hilfsfunktion zur "schönen" Anzeige umfangreicher Ausdrücke
     """

    import matplotlib.pyplot as plt
    latex_str = "$ %s $" % sp.latex(expr, **kwargs)
    latex_str = latex_str.replace("operatorname", "mathrm")
    plt.figure(figsize=(20, 5))  # 20x5 Zoll
    plt.text(0.5, 0.5, latex_str, fontsize=30, horizontalalignment='center')
    plt.axis('off')
    plt.show()


if __name__ == "__main__":
    # Dieser Block wird nur ausgeführt, wenn diese Datei das Haupt-Skript ist,
    # nicht wenn sie als Modul woanders importiert wird.

    # Anzeigen:

    ## sp.Eq -> sympy Equation object
    Eq1a = sp.Eq(xdd, xdd_expr.subs(rplmts))
    Eq2a = sp.Eq(phidd, phidd_expr.subs(rplmts))

    # Symbolbenennung in LaTeX-Notation
    sn_dict = {phi: r'\varphi', phid: r'\dot{\varphi}',
               xdd: r'\ddot{x}', phidd: r'\ddot{\varphi}'}

    preview(Eq1a, symbol_names=sn_dict)
    preview(Eq2a, symbol_names=sn_dict)
