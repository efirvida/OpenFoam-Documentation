# MeshedSurface.T 
## Class
Foam::MeshedSurface

## Description
A surface geometry mesh with zone information, not to be confused with
the similarly named surfaceMesh, which actually refers to the cell faces
of a volume mesh.

A MeshedSurface can have zero or more surface zones (roughly equivalent
to faceZones for a polyMesh). If surface zones are defined, they must
be contiguous and cover all of the faces.

The MeshedSurface is intended for surfaces from a variety of sources.
- A set of points and faces without any surface zone information.
- A set of points and faces with randomly ordered zone information.
      This could arise, for example, from reading external file formats
      such as STL, etc.

## SourceFiles
MeshedSurface.C

