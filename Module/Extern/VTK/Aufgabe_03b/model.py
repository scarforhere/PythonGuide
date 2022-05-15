# -*- coding: utf-8 -*-
from __future__ import  division


from numpy import sin, cos, pi
from scipy.integrate import ode


def rhs(t, y):
    """
    Berechnung der Zustandableitung unseres Systems
    """

    x_s, phi_s, xd_s, phid_s = y

    xdd = (0.09*phid_s**2*sin(phi_s)**3 + 0.09*phid_s**2*sin(phi_s)*cos(phi_s)**2 + 0.24*phid_s**2*sin(phi_s) + 10.791*sin(phi_s)*cos(phi_s))/(2*(0.33*sin(phi_s)**2 + 0.88))
    phidd = -3.33333333333333*(0.09*phid_s**2*sin(phi_s)*cos(phi_s) + 10.791*sin(phi_s))/(0.3*sin(phi_s)**2 + 0.8)

    return [xd_s, phid_s, xdd, phidd]



# Solver und Schrittweite
dt = 0.01

solver = ode(rhs)
solver.set_initial_value([0, 0.75*pi, 0, 0])
solver.set_integrator('vode', method='adams', rtol=1e-6, atol=1e-9)




def calcStep():
    """
    Funktion zur Berechnung eines einzelnen Integrationsschrittes. Gibt die
    aktuelle Simulationszeit und den Vektor [x, phi, xd, phid] zurueck.
    """

    return solver.t, solver.integrate(solver.t+dt)
