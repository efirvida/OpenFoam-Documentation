# externalDisplacementMeshMover 
## Class
Foam::externalDisplacementMeshMover

## Description
Virtual base class for mesh movers with externally provided displacement
field giving the boundary conditions. Move the mesh from the current
location to a new location (so modify the mesh; v.s. motionSolver that
only returns the new location).

All mesh movers are expected to read the dictionary settings at invocation
of move(), i.e. not cache any settings.

## SourceFiles
externalDisplacementMeshMover.C

