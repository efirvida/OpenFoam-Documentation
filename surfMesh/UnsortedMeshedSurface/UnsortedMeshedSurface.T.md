# UnsortedMeshedSurface.T 
## Class
Foam::UnsortedMeshedSurface

## Description
A surface geometry mesh, in which the surface zone information is
conveyed by the 'zoneId' associated with each face.

This form of surface description is particularly useful for reading in
surface meshes from third-party formats (eg, obj, stl, gts, etc.). It
can also be particularly useful for situations in which the surface
many be adjusted in an arbitrary manner without worrying about needed
to adjust the zone information (eg, surface refinement).

## See also
The Foam::MeshedSurface - which is organized as a surface mesh, but
with independent zone information.

## SourceFiles
UnsortedMeshedSurface.C

