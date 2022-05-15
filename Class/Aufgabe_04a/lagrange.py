# -*- coding: utf-8 -*-

from sympy import sin, cos, Function
import sympy as sp
import sys



# Lösung von Übung 02a, Bewegungsgleichung werden fuer die Berechnung von Lage
# und Orientierung der Koerper im Raum benoetigt



# Symbolische Variablen und Parameter anlegen
t = sp.Symbol('t')

params = sp.symbols('m1, m2, l, g')
m1, m2, l, g= params

xt = Function('x')(t) # x(t)
phit = Function('phi')(t) # phi(t)


# Ableitungen der Zustandsgrossen
xdt = xt.diff(t)
phidt = phit.diff(t)
xddt = xt.diff(t,2)
phiddt = phit.diff(t,2)


# Hilfsrechnung
x2t = xt + l*sin(phit)
y2t = -l*cos(phit)

x2dt =x2t.diff(t)
y2dt =y2t.diff(t)


# kinetische Energie
T = (m1*xdt**2 + m2*(x2dt**2 + y2dt**2))

# Potentielle Energie
U = y2t * g

# Lagrange-Funktion
L = T-U


#Funktionen durch Symbole ersetzen
x_s, phi_s, xd_s, phid_s = sp.symbols('x_s, phi_s, xd_s, phid_s')


# Reihenfolge ist hier wichtig. Hoehere Ableitungen zuerst substituieren.
subs_list1 = [(xdt, xd_s), (phidt, phid_s), (xt, x_s), (phit, phi_s)]
L = L.subs(subs_list1) # subs Funktionen -> Symbole
L = L.expand()
L = sp.trigsimp(L)


# --- Lagrange-Gleichungen ---
# Hilfsterme:
L_d_x = L.diff(x_s)
L_d_phi = L.diff(phi_s)

L_d_xd = L.diff(xd_s)
L_d_phid = L.diff(phid_s)

xdd_s, phidd_s = sp.symbols('xdd_s, phidd_s')


# sub_slist ergaenzen (Reihenfolge beachten: hoehere Ableitungen vorn hin)
subs_list1 = [(xddt, xdd_s), (phiddt, phidd_s)] + subs_list1


# Liste umkehren (subs Symbole -> Funktionen)
subs_list_rev = [ (tup[1], tup[0]) for tup in subs_list1]

L_d_xd = L_d_xd.subs(subs_list_rev)
L_d_phid = L_d_phid.subs(subs_list_rev)

DL_d_xd = L_d_xd.diff(t).subs(subs_list1)
DL_d_phid = L_d_phid.diff(t).subs(subs_list1)


# eingepraegte Last (translatorisch)
F = sp.Symbol('F')


# Gleichungen aufstellen und nach der hoechsten Ableitung aufloesen
Eq1 = sp.Eq( DL_d_xd - L_d_x , F )
Eq2 = sp.Eq( DL_d_phid - L_d_phi, 0 )

res = sp.solve([Eq1, Eq2], xdd_s, phidd_s)


# Gleichungen fuer Simulation (xdd = ...; phidd = ...)
Eq1_  = sp.Eq( xdd_s, res[xdd_s])
Eq2_  = sp.Eq( phidd_s, res[phidd_s])


# Parameter substituieren (hier keine auesseren Kraefte)
params_values = {m1: 0.8, m2: 0.3, l:0.5, g:9.81, F:0}

xdd_expr = Eq1_.rhs.subs(params_values)
phidd_expr = Eq2_.rhs.subs(params_values)


# Funktionen für die numerische Berechnung der Beschleunigungen
xdd_fnc = sp.lambdify([x_s, phi_s, xd_s, phid_s], xdd_expr, 'numpy')
phidd_fnc = sp.lambdify([x_s, phi_s, xd_s, phid_s], phidd_expr, 'numpy')

## xdd_fnc und phi_dd_fnc sind ausführbare bzw. aufrufbare-Objekte
## ("callable objects")
## Es sind Funktionen, die vier Argumente bekommen und einen Wert zurrückgeben.
