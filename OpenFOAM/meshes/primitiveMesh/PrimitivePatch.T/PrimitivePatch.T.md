# PrimitivePatch.T 
## Class
Foam::PrimitivePatch

## Description
A list of faces which address into the list of points.

The class is templated on the face type (e.g. triangle, polygon etc.)
and on the list type of faces and points so that it can refer to
existing lists using UList and const pointField& or hold the storage
using List and pointField.

## SourceFiles
PrimitivePatchAddressing.C
PrimitivePatchBdryPoints.C
PrimitivePatch.C
PrimitivePatchCheck.C
PrimitivePatchClear.C
PrimitivePatchEdgeLoops.C
PrimitivePatchLocalPointOrder.C
PrimitivePatchMeshData.C
PrimitivePatchMeshEdges.C
PrimitivePatchName.C
PrimitivePatchPointAddressing.C
PrimitivePatchProjectPoints.C

