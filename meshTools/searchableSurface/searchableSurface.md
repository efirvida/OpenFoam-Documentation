# searchableSurface 
## Class
Foam::searchableSurface

## Description
Base class of (analytical or triangulated) surface.
Encapsulates all the search routines. WIP.

Information returned is usually a pointIndexHit:
- bool  : was intersection/nearest found?
- point : intersection point or nearest point
- index : unique index on surface (e.g. triangle for triSurfaceMesh)

## SourceFiles
searchableSurface.C

