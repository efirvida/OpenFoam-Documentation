# isoSurface 
## Class
Foam::isoSurface

## Description
A surface formed by the iso value.
After "Regularised Marching Tetrahedra: improved iso-surface extraction",
G.M. Treece, R.W. Prager and A.H. Gee.

Note:
- does tets without using cell centres/cell values. Not tested.
- regularisation can create duplicate triangles/non-manifold surfaces.
Current handling of those is bit ad-hoc for now and not perfect.
- regularisation does not do boundary points so as to preserve the
      boundary perfectly.
- uses geometric merge with fraction of bounding box as distance.
- triangles can be between two cell centres so constant sampling
      does not make sense.
- on empty patches behaves like zero gradient.
- does not do 2D correctly, creates non-flat iso surface.
- on processor boundaries might two overlapping (identical) triangles
      (one from either side)

The handling on coupled patches is a bit complex. All fields
(values and coordinates) get rewritten so
- empty patches get zerogradient (value) and facecentre (coordinates)
- separated processor patch faces get interpolate (value) and facecentre
      (coordinates). (this is already the default for cyclics)
- non-separated processor patch faces keep opposite value and cell centre

Now the triangle generation on non-separated processor patch faces
can use the neighbouring value. Any separated processor face or cyclic
face gets handled just like any boundary face.


## SourceFiles
isoSurface.C

