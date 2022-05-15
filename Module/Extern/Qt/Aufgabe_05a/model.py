# -*- coding: utf-8 -*-

"""
Dieses Modul wird von simgui.py importiert. Keine Anpassung notwendig.
"""


from numpy import sin, cos, pi



def rhs(y, t, m1, m2, l):
    """
    Berechnung der Zustandsableitung unseres Systems
    """

    x_s, phi_s, xd_s, phid_s = y

    xdd = (2*l*m1*m2*phid_s**2*sin(phi_s) + 2*l*m2**2*phid_s**2*sin(phi_s)**3 + 2*l*m2**2*phid_s**2*sin(phi_s)*cos(phi_s)**2 + 9.81*m1*sin(phi_s)*cos(phi_s) + 9.81*m2*sin(phi_s)*cos(phi_s))/(2*(m1**2 + m1*m2*sin(phi_s)**2 + m1*m2 + m2**2*sin(phi_s)**2))
    phidd = -(2*l*m2**2*phid_s**2*sin(phi_s)*cos(phi_s) + 9.81*m1*sin(phi_s) + 9.81*m2*sin(phi_s))/(2*l*m2*(m1 + m2*sin(phi_s)**2))

    return [xd_s, phid_s, xdd, phidd]
