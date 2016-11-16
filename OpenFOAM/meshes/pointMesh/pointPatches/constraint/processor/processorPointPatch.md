# processorPointPatch 
## Class
Foam::processorPointPatch

## Description
Processor patch boundary needs to be such that the ordering of
points in the patch is the same on both sides.

Looking at the creation of the faces on both sides of the processor
patch they need to be identical on both sides with the normals pointing
in opposite directions.  This is achieved by calling the reverseFace
function in the decomposition.  It is therefore possible to re-create
the ordering of patch points on the slave side by reversing all the
patch faces of the owner.

## SourceFiles
processorPointPatch.C

