# coding: utf-8
"""
-------------------------------------------------
   File Name:      VTK_3
   Author :        Scar
   E-mail :        scarforhere@gmail.com
   Date:           2021-05-18 09:09 PM
-------------------------------------------------
Description : 

    Print info with under format:

"""
import vtk

# part anlegen (Source, Mapper, Actor)
# # Cube Part
# part = vtk.vtkCubeSource()
# part.SetXLength(10)
# part.SetYLength(1)
# part.SetZLength(1)

# # Sphere
# part = vtk.vtkSphereSource()
# part.SetRadius(5)
# part.SetThetaResolution(20)
# part.SetPhiResolution(20)

# # Line Part
# part = vtk.vtkLineSource()
# part.SetPoint1(0,0,0)
# part.SetPoint2(10,0,0)

# # Import STL Part
# part = vtk.vtkSTLReader()
# part.SetFileName("haken.stl")

# # Text Part
# part = vtk.vtkTextSource()
# part.SetText("Hallo Welt")

# # Cylinder Part
# part = vtk.vtkCylinderSource()
# part.SetRadius(1)
# part.SetHeight(10)
# part.SetResolution(20)

# 3 Dimension Axes Part
part = vtk.vtkAxes()
part.SetScaleFactor(1)


# Mapper
partMapper = vtk.vtkPolyDataMapper()
partMapper.SetInputConnection(part.GetOutputPort())


# Actor
partactor = vtk.vtkLODActor()
partactor.SetMapper(partMapper)


# Renderer
ren = vtk.vtkRenderer()


# Actors zum Renderer hinzufügen
ren.AddActor(partactor)


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


# Fenster öffnen
iren.Start()


# Schließt das Vtk Fenster wieder (q drücken oder Fenster mit Maus schließen)
iren.GetRenderWindow().Finalize()