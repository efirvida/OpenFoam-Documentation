# mapDistributePolyMesh 
## Class
Foam::mapDistributePolyMesh

## Description
Class containing mesh-to-mesh mapping information after a mesh distribution
where we send parts of meshes (using subsetting) to other processors
and receive and reconstruct mesh.

We store mapping from the bits-to-send to the complete starting mesh
(subXXXMap) and from the received bits to their location in the new
mesh (constructXXXMap).

## SourceFiles
mapDistributePolyMesh.C

