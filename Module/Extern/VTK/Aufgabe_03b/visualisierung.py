# -*- coding: utf-8 -*-
from __future__ import  division


import vtk
from vtk.util.colors import *


# importe einfügen
from functions import calcPositions, setPokeMatrix
from model import calcStep


#-------------------------------------------------------------------------------

# Quader für Laufkatze mit Abmessungen x,y,z anlegen
#laufkatze = vtk.vtkCubeSource()
#laufkatze.SetXLength(0.3)
#laufkatze.SetYLength(0.1)
#laufkatze.SetZLength(0.1)


# Geometrie aus stl-Datei
laufkatze = vtk.vtkSTLReader()
laufkatze.SetFileName(r'E:\Python_Code\PythonGuide\Module\Extern\VTK\laufkatze.stl')

lk_mapper = vtk.vtkPolyDataMapper()
lk_mapper.SetInputConnection(laufkatze.GetOutputPort())

lk_actor = vtk.vtkLODActor()
lk_actor.SetMapper(lk_mapper)


haken = vtk.vtkSTLReader()
haken.SetFileName(r'E:\Python_Code\PythonGuide\Module\Extern\VTK\haken.stl')

hk_mapper = vtk.vtkPolyDataMapper()
hk_mapper.SetInputConnection(haken.GetOutputPort())

hk_actor = vtk.vtkLODActor()
hk_actor.SetMapper(hk_mapper)

#-------------------------------------------------------------------------------

# Würfel für Last
last = vtk.vtkCubeSource()
last.SetXLength(0.1)
last.SetYLength(0.1)
last.SetZLength(0.1)

last_mapper = vtk.vtkPolyDataMapper()
last_mapper.SetInputConnection(last.GetOutputPort())

last_actor = vtk.vtkLODActor()
last_actor.SetMapper(last_mapper)


#-------------------------------------------------------------------------------

# Zylinder für Seil
seil = vtk.vtkCylinderSource()
seil.SetRadius(0.01)
seil.SetHeight(0.5)


seil_mapper = vtk.vtkPolyDataMapper()
seil_mapper.SetInputConnection(seil.GetOutputPort())

seil_actor = vtk.vtkLODActor()
seil_actor.SetMapper(seil_mapper)


#-------------------------------------------------------------------------------

# Renderer, RenderWindow und RenderWindowInteractor
ren = vtk.vtkRenderer()
renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren)
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)

# Actors zum Renderer hinzufügen
ren.AddActor(lk_actor)
ren.AddActor(hk_actor)
ren.AddActor(last_actor)
ren.AddActor(seil_actor)

# Hintergrundfarbe und Fenstergrösse
ren.SetBackground(0.1, 0.2, 0.4)
renWin.SetSize(500, 500)

# Mausmanipulator anpassen und Interactor initialisieren
iren.SetInteractorStyle(vtk.vtkInteractorStyleTrackballCamera())
iren.Initialize()


#-------------------------------------------------------------------------------


def updateScene(*args):
    """
    Diese Funktion berechnet das System neu und aktualisiert die Szene.
    """

    # einen Simulationsschritt berechnen
    t,y = calcStep()

    # Positionen und Orientierungen der Körper berechnen
    r_laufkatze, R_laufkatze, r_last, R_last, r_seil, R_seil = calcPositions(y)

    # Körper updaten
    setPokeMatrix(lk_actor, r_laufkatze, R_laufkatze)
    setPokeMatrix(hk_actor, r_laufkatze, R_laufkatze)
    setPokeMatrix(last_actor, r_last, R_last)
    setPokeMatrix(seil_actor, r_seil, R_seil)

    # Bild neu rendern
    renWin.Render()


#-------------------------------------------------------------------------------


# Anlegen des Timers. Die Funktion updateScene wird jetzt alle 20ms aufgerufen
iren.AddObserver('TimerEvent', updateScene)
iren.CreateRepeatingTimer(20)

# Fenster öffnen
iren.Start()

# Schliesst das Vtk Fenster wieder (q drücken oder Fenster mit Maus schliessen)
iren.GetRenderWindow().Finalize()
