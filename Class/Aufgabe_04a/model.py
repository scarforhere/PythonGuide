# -*- coding: utf-8 -*-

from numpy import sin, cos, pi, array, eye
from scipy.integrate import ode




def rhs(t, y):
    '''
    Berechnung der Zustandableitung unseres Systems
    '''

    x_s, phi_s, xd_s, phid_s = y

    xdd = (0.09*phid_s**2*sin(phi_s)**3 + 0.09*phid_s**2*sin(phi_s)*cos(phi_s)**2 + 0.24*phid_s**2*sin(phi_s) + 10.791*sin(phi_s)*cos(phi_s))/(2*(0.33*sin(phi_s)**2 + 0.88))
    phidd = -3.33333333333333*(0.09*phid_s**2*sin(phi_s)*cos(phi_s) + 10.791*sin(phi_s))/(0.3*sin(phi_s)**2 + 0.8)

    return [xd_s, phid_s, xdd, phidd]



# Solver und Schrittweite
dt = 0.01

solver = ode(rhs)
solver.set_initial_value([0,0.75*pi,0,0])
solver.set_integrator('vode', method='adams', rtol=1e-6, atol=1e-9)





def calcStep():
    '''
    Funktion zur Berechnung eines einzelnen Integrationsschrittes. Gibt die
    aktuelle Simulationszeit und den Vektor [x, phi, xd, phid] zurueck.
    '''

    return solver.t, solver.integrate(solver.t+dt)





def calcPositions(y):
    '''
    Position und Orientierung der Koerper im Raum berechnen (im raumfesten
    Koordinatensystem)

    r - Position (3-Vektor)
    T - Orientierung (3x3-Matrix)

    Rueckgabewert der Funktion ist ein Tupel mit r und T von Laufkatze und Last
    '''

    # Geometrieparameter - Pendellaenge
    l = 0.5

    # Zustaende auf Positionsebene - Geschwindigkeiten werden nicht benoetigt
    x = y[0]
    phi = y[1]


    # Lage der Laufkatze
    r_laufkatze = array([x,0,0])
    T_laufkatze = eye(3)


    # Lage der Last
    r_last = array([x+l*sin(phi),0,-l*cos(phi)])
    T_last = array([[cos(phi), 0, -sin(phi)],
                       [          0, 1,            0],
                       [sin(phi), 0,  cos(phi)]])

    return (r_laufkatze, T_laufkatze, r_last, T_last)
