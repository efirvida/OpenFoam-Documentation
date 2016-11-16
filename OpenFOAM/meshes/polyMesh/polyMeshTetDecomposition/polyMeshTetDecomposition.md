# polyMeshTetDecomposition 
## Class
Foam::polyMeshTetDecomposition

## Description
Tools for performing the minimum decomposition of faces of the
mesh into triangles so that the cells may be tet decomposed.
Includes functions for finding variable face starting (base)
points on each face to avoid the decomposition of cells into tets
that have negative or zero volume.

## SourceFiles
polyMeshTetDecomposition.C

