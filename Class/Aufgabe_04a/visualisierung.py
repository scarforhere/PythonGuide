# -*- coding: utf-8 -*-

import vtk
from vtk.util.colors import *


from model import calcStep, calcPositions
from primitives import Sphere, Cube, File


#-------------------------------------------------------------------------------

# Koerper anlegen
# laufkatze = Cube(0.3, 0.1, 0.1)
laufkatze = File("E:\Python_Code\PythonGuide\Class\Aufgabe 04a\laufkatze.stl")

last = Cube(0.05, 0.05, 0.05)
last.setColor(red)


#-------------------------------------------------------------------------------

# Renderer, RenderWindow und RenderWindowInteractor
ren = vtk.vtkRenderer()
renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren)
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)

# Actors zum Renderer hinzufuegen
ren.AddActor(laufkatze.actor)
ren.AddActor(last.actor)

# Hintergrundfarbe und Fenstergroesse
ren.SetBackground(0.1, 0.2, 0.4)
renWin.SetSize(500, 500)

# Mausmanipulator anpassen und Interactor initialisieren
iren.SetInteractorStyle(vtk.vtkInteractorStyleTrackballCamera())
iren.Initialize()


#-------------------------------------------------------------------------------


def updateScene(*args):
    '''
    Diese Funktion berechnet das System neu und aktualisiert die Szene.
    '''

    # einen Simulationsschritt berechnen
    t, y = calcStep()

    # Positionen und Orientierungen der Koerper berechnen
    r_laufkatze, T_laufkatze, r_last, T_last = calcPositions(y)

    # Koerper updaten
    laufkatze.setPositionAndOrientation(r_laufkatze, T_laufkatze)
    last.setPositionAndOrientation(r_last,T_last)

    # Bild neu rendern
    renWin.Render()


#-------------------------------------------------------------------------------


# Anlegen des Timers. Die Funktion updateScene wird jetzt alle 20ms aufgerufen
iren.AddObserver('TimerEvent', updateScene)
iren.CreateRepeatingTimer(20)

# Fenster oeffnen
iren.Start()

# Schliesst das Vtk Fenster wieder (q druecken oder Fenster mit Maus schliessen)
iren.GetRenderWindow().Finalize()
