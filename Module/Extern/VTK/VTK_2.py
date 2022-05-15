# coding: utf-8
"""
-------------------------------------------------
   File Name:      VTK_2
   Author :        Scar
   E-mail :        scarforhere@gmail.com
   Date:           2021-05-18 04:58 PM
-------------------------------------------------
Description : 

    Print info with under format:

"""
import vtk

# Quader anlegen (Source, Mapper, Actor)
quaderSource = vtk.vtkCubeSource()
quaderSource.SetXLength(0.3)
quaderSource.SetYLength(0.1)
quaderSource.SetZLength(0.1)

# Mapper
quaderMapper = vtk.vtkPolyDataMapper()
quaderMapper.SetInputConnection(quaderSource.GetOutputPort())

# Actor
quader = vtk.vtkLODActor()
quader.SetMapper(quaderMapper)

# Kugel anlegen (Source, Mapper, Actor)
kugelSource = vtk.vtkSphereSource()
kugelSource.SetRadius(0.08)
kugelSource.SetThetaResolution(10) # Diskretisierung
kugelSource.SetPhiResolution(10)

# Mapper
kugelMapper = vtk.vtkPolyDataMapper()
kugelMapper.SetInputConnection(kugelSource.GetOutputPort())

# Actor
kugel = vtk.vtkLODActor()
kugel.SetMapper(kugelMapper)


# Renderer
ren = vtk.vtkRenderer()

# Actors zum Renderer hinzufügen
ren.AddActor(quader)
ren.AddActor(kugel)

# RenderWindow und RenderWindowInteractor
renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren)
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)


# Hintergrundfarbe und Fenstergröße
ren.SetBackground(0.1, 0.2, 0.4)
renWin.SetSize(500, 500)

# Mausmanipulator anpassen, Fenster mit Visualisierung initialisieren
iren.SetInteractorStyle(vtk.vtkInteractorStyleTrackballCamera())
iren.Initialize()


# Verschieben
import numpy as np

P = np.eye(4)  # Einheitsmatrix (keine Rotation)
# Verschiebung: 1 in x-Richtung, 2 in y-Richtung usw
P[:-1, -1] = np.array([1, 2, 3])

# leere Matrix anlegen und Inhalt von T kopieren
poke_matrix = vtk.vtkMatrix4x4()
vtk.vtkMatrix4x4.DeepCopy(poke_matrix, P.flatten())
quader.PokeMatrix(poke_matrix)



# Fenster öffnen
iren.Start()


# Schließt das Vtk Fenster wieder (q drücken oder Fenster mit Maus schließen)
iren.GetRenderWindow().Finalize()
