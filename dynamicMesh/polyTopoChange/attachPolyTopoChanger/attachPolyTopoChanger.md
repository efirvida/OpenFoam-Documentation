# attachPolyTopoChanger 
## Class
Foam::attachPolyTopoChanger

## Description
This class is derived from polyMesh and serves as a tool for
statically connecting pieces of a mesh by executing the mesh
modifiers and cleaning the mesh.

The idea is that a mesh can be built from pieces and put together
using various mesh modifiers (mainly sliding interfaces) which are
not needed during the run.  Therefore, once the mesh is assembled
and mesh modification triggered, the newly created point, face and
cell zones can be cleared together with the mesh modifiers thus
creating a singly connected static mesh.

Note:
All point, face and cell zoning will be lost!  Do it after
attaching the parts of the mesh, as the point, face and cell
numbering changes.

