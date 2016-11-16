# surfaceToCell 
## Class
Foam::surfaceToCell

## Description
A topoSetSource to select cells based on relation to surface.

Selects:
- all cells inside/outside/cut by surface
- all cells inside/outside surface ('useSurfaceOrientation', requires closed
      surface)
- cells with centre nearer than XXX to surface
- cells with centre nearer than XXX to surface \b and with normal
      at nearest point to centre and cell-corners differing by
      more than YYY (i.e., point of high curvature)

## SourceFiles
surfaceToCell.C

