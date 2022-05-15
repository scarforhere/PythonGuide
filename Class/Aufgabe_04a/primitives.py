# -*- coding: utf-8 -*-

import numpy as np
import vtk
import os




class Geometry(object):
    '''
    Klasse, die einen Koerper repraesentiert.
    '''

    def __init__(self):

        # Standardwerte fuer Lage (Koerper liegt im Ursprung, unverdreht)
        self._r = np.array([0,0,0])
        self._T = np.eye(3)

        # wir haben noch keine Geometriedaten!
        self.source = None

        # actor
        self.actor = vtk.vtkLODActor()


    def _createMapper(self):
        '''
        Hier wird der Mapper fuer self.source angelegt und mit dem Actor
        verbunden. Muss im Konstruktor der erbenden Klassen aufgerufen werden.
        '''

        # pruefen, ob Quelle vorhanden ist
        if self.source is None:
            raise ValueError('Keine Geometriequelle vorhanden')

        # Mapper anlegen und verbinden
        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputConnection(self.source.GetOutputPort())

        self.actor.SetMapper(mapper)


    def setColor(self, color):
        '''
        Funktion zum setzen der Farbe, nur zur Vereinfachung
        '''
        self.actor.GetProperty().SetColor(color)


    def setOpacity(self, opac):
        '''
        Funktion zum setzen der Transparenz, nur zur Vereinfachung
        '''
        self.actor.GetProperty().SetOpacity(opac)


    def setPosition(self, r):
        '''
        Nur Position uebergeben und aktualisieren.
        '''
        self._r = r
        self.update()


    def setOrientation(self, T):
        '''
        Nur Orientierung uebergeben und aktualisieren
        '''
        self._T = T
        self.update()


    def setPositionAndOrientation(self, r, T):
        '''
        Position und Orientierung uebergeben und aktualisieren
        '''
        self._r = r
        self._T = T
        self.update()


    def update(self):
        '''
        Die Lage von 3D-Objekten in vtk wird mit einer sog. Poke-Matrix
        definiert. Sie ist eine 4x4-Matrix mit folgender Gestalt:

        [          ]
        [   T     r]
        [          ]
        [0  0  0  0]

        Soll die Lage eines Koerpers aktualisiert werden, muessen die Werte der
        Poke-Matrix geaendert werden. Das geschieht mit Hilfe dieser Funktion.
        '''

        # leere Matrix anlegen (ist eine 4x4 Einheitsmatrix)
        poke = vtk.vtkMatrix4x4()

        # Matrix elementweise befuellen
        for row in range(3):

            # Positionsvektor
            poke.SetElement(row,3, self._r[row])

            # Orientierung
            for col in range(3):
                poke.SetElement(row, col, self._T[row,col])

        # Matrix an Actor übergeben
        self.actor.PokeMatrix(poke)


    @property
    def position(self):
        return self._r


    @property
    def orientation(self):
        return self._T


class Cube(Geometry):
    '''
    Klasse fuer einen Quader
    '''

    def __init__(self, xLen,yLen,zLen):

        # Konstruktor der Basisklasse aufrufen
        Geometry.__init__(self)

        # Geometriequelle
        self.source = vtk.vtkCubeSource()
        self.source.SetXLength(xLen)
        self.source.SetYLength(yLen)
        self.source.SetZLength(zLen)

        self._createMapper()


class Sphere(Geometry):
    '''
    Klasse fuer eine Kugel
    '''

    def __init__(self, radius, thetaRes=20, phiRes=20):

        # Konstruktor der Basisklasse aufrufen
        Geometry.__init__(self)

        # Geometriequelle
        self.source = vtk.vtkSphereSource()
        self.source.SetRadius(radius)
        self.source.SetThetaResolution(thetaRes)
        self.source.SetPhiResolution(phiRes)

        self._createMapper()


class File(Geometry):
    '''
    Klasse fuer ein stl-File
    '''

    def __init__(self, path):

        # kleiner Test
        if not os.path.exists(path):
            raise IOError('Datei existiert nicht')

        # Konstruktor der Basisklasse aufrufen
        Geometry.__init__(self)

        # Geometriequelle
        self.source = vtk.vtkSTLReader()
        self.source.SetFileName(path)

        self._createMapper()
