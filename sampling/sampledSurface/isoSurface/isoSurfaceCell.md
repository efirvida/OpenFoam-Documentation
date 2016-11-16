# isoSurfaceCell 
## Class
Foam::isoSurfaceCell

## Description
A surface formed by the iso value.
After "Polygonising A Scalar Field Using Tetrahedrons", Paul Bourke
(http://paulbourke.net/geometry/polygonise) and
"Regularised Marching Tetrahedra: improved iso-surface extraction",
G.M. Treece, R.W. Prager and A.H. Gee.

See isoSurface. This is a variant which does tetrahedrisation from
triangulation of face to cell centre instead of edge of face to two
neighbouring cell centres. This gives much lower quality triangles
but they are local to a cell.

## SourceFiles
isoSurfaceCell.C

