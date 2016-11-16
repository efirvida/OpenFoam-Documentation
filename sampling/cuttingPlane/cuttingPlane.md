# cuttingPlane 
## Class
Foam::cuttingPlane

## Description
Constructs plane through mesh.

No attempt at resolving degenerate cases. Since the cut faces are
usually quite ugly, they will always be triangulated.

## Note
When the cutting plane coincides with a mesh face, the cell edge on the
positive side of the plane is taken.

## SourceFiles
cuttingPlane.C

