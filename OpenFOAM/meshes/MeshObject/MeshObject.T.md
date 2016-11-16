# MeshObject.T 
## Class
Foam::MeshObject

## Description
Templated abstract base-class for optional mesh objects used to automate
their allocation to the mesh database and the mesh-modifier event-loop.

MeshObject is templated on the type of mesh it is allocated to, the type of
the mesh object (TopologicalMeshObject, GeometricMeshObject,
MoveableMeshObject, UpdateableMeshObject) and the type of the actual object
it is created for example:

```
class leastSquaresVectors
:
        public MeshObject<fvMesh, MoveableMeshObject, leastSquaresVectors>
{
.
.
.
        //- Delete the least square vectors when the mesh moves
        virtual bool movePoints();
};
```

MeshObject types:

- TopologicalMeshObject: mesh object to be deleted on topology change
- GeometricMeshObject: mesh object to be deleted on geometry change
- MoveableMeshObject: mesh object to be updated in movePoints
- UpdateableMeshObject: mesh object to be updated in updateMesh or
        movePoints

## Note
movePoints must be provided for MeshObjects of type MoveableMeshObject
and both movePoints and updateMesh functions must exist, provided for
MeshObjects of type UpdateableMeshObject.

## SourceFiles
MeshObject.C

