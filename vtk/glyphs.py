import vtk
 
# Python example translated directly from Tcl test
# [vtk_source]/Graphics/Testing/Tcl/progGlyphs.tcl
 
res = 6
plane = vtk.vtkPlaneSource()
plane.SetResolution(res,res)
colors = vtk.vtkElevationFilter()
colors.SetInputConnection(plane.GetOutputPort())
colors.SetLowPoint(-0.25,-0.25,-0.25)
colors.SetHighPoint(0.25,0.25,0.25)
planeMapper = vtk.vtkPolyDataMapper()
planeMapper.SetInput(colors.GetPolyDataOutput())
planeActor = vtk.vtkActor()
planeActor.SetMapper(planeMapper)
planeActor.GetProperty().SetRepresentationToWireframe()
 
# procedure for generating glyphs
def Glyph():    
    ptId = glypher.GetPointId()
    pd = glypher.GetPointData()
    xyz = glypher.GetPoint()
    x = xyz[0]
    y = xyz[1]
    length = glypher.GetInput(0).GetLength()
    scale = length / (2.0*res)
 
    squad.SetScale(scale,scale,scale)
    squad.SetCenter(xyz)
    squad.SetPhiRoundness(abs(x)*5.0)
    squad.SetThetaRoundness(abs(y)*5.0)
 
# create simple poly data so we can apply glyph
squad = vtk.vtkSuperquadricSource()
 
glypher = vtk.vtkProgrammableGlyphFilter()
glypher.SetInputConnection(colors.GetOutputPort())
glypher.SetSource(squad.GetOutput())
glypher.SetGlyphMethod(Glyph)
glyphMapper = vtk.vtkPolyDataMapper()
glyphMapper.SetInputConnection(glypher.GetOutputPort())
glyphActor = vtk.vtkActor()
glyphActor.SetMapper(glyphMapper)
 
# Create the rendering stuff
ren1 = vtk.vtkRenderer()
renWin = vtk.vtkRenderWindow()
renWin.SetMultiSamples(0)
renWin.AddRenderer(ren1)
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)
ren1.AddActor(planeActor)
ren1.AddActor(glyphActor)
ren1.SetBackground(1,1,1)
renWin.SetSize(450,450)
renWin.Render()
 
iren.Start()
