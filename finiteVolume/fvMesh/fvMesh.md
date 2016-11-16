# fvMesh 
## Class
Foam::fvMesh

## Description
Mesh data needed to do the Finite Volume discretisation.

NOTE ON USAGE:
fvMesh contains all the topological and geometric information
related to the mesh.  It is also responsible for keeping the data
up-to-date.  This is done by deleting the cell volume, face area,
cell/face centre, addressing and other derived information as
required and recalculating it as necessary.  The fvMesh therefore
reserves the right to delete the derived information upon every
topological (mesh refinement/morphing) or geometric change (mesh
motion).  It is therefore unsafe to keep local references to the
derived data outside of the time loop.

## SourceFiles
fvMesh.C
fvMeshGeometry.C

