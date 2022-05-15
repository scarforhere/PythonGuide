# -*- coding: utf-8 -*-
from __future__ import  division

import numpy as np
from numpy import sin, cos
import vtk





def calcPositions(y):
    """
    Position und Orientierung der Körper im Raum berechnen (im raumfesten
    Koordinatensystem). y ist das Ergebnis der Integration [x, phi, xd, phid].

    r - Position (3-Vektor)
    R - Orientierung (3x3-Matrix)

    Rueckgabewert der Funktion ist ein Tupel mit r und T von Laufkatze und Last
    """

    # Geometrieparameter - Pendellaenge
    l = 0.5

    # Zustaende x und phi aus Argument - Geschwindigkeiten nicht benoetigt
    x = y[0]
    phi = y[1]

    # Lage und Orientierung der Laufkatze berechnen
    r_laufkatze = np.array([x,0,0])
    R_laufkatze = np.eye(3)

    # Lage und Orientierung der Last
    r_last = np.array([x+l*sin(phi), 0, -l*cos(phi)])

    R_last = np.array([[cos(phi), 0, -sin(phi)],
                       [    0,    1,      0   ],
                       [sin(phi), 0,  cos(phi)]])

    # Lage und Orientierung Seil
    # Zylinder muss zusätzlich um 90 Grad um x-Achse in die x-z-Ebene gedreht werden
    r_seil = np.array([x+l/2*sin(phi),0,-l/2*cos(phi)])

    Rx = np.array([[1,            0,           0],
                   [0,  cos(np.pi/2), sin(np.pi/2)],
                   [0, -sin(np.pi/2), cos(np.pi/2)]])

    # Matrix-Multiplikation (*-Operator multipliziert np-arrays elementweise)
    R_seil = np.dot(R_last, Rx)

    return (r_laufkatze, R_laufkatze, r_last, R_last, r_seil, R_seil)





def setPokeMatrix(actor, r, R):
    """
    Die Lage von 3D-Objekten in vtk wird mit einer sog. Poke-Matrix definiert.
    Sie ist eine 4x4-Matrix mit folgender Gestalt:

    [          ]
    [   R     r]
    [          ]
    [0  0  0  1]

    Soll die Lage eines Koerpers aktualisiert werden, muessen die Werte der
    Poke-Matrix geaendert werden. Das geschieht mit Hilfe dieser Funktion.
    """

    # leere Matrix anlegen (ist eine 4x4 Einheitsmatrix)
    poke = vtk.vtkMatrix4x4()

    # arrays zusammenfügen
    P = np.column_stack((R, r))
    P = np.row_stack( (P, np.array([0, 0, 0, 1])) )

    vtk.vtkMatrix4x4.DeepCopy(poke, P.ravel()*1)

    # Matrix an Actor übergeben
    actor.PokeMatrix(poke)
