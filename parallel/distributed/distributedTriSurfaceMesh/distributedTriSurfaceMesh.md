# distributedTriSurfaceMesh 
## Class
Foam::distributedTriSurfaceMesh

## Description
IOoject and searching on distributed triSurface. All processor hold
(possibly overlapping) part of the overall surface. All queries are
distributed to the processor that can answer it and the result sent back.

Can work in three modes:
- follow : makes sure each processor has all the triangles inside the
externally provided bounding box (usually the mesh bounding box).
Guarantees minimum amount of communication since mesh-local queries
should be answerable without any comms.
- independent : surface is decomposed according to the triangle centres
so the decomposition might be radically different from the mesh
decomposition. Guarantees best memory balance but at the expense of
more communication.
- frozen : no change

## SourceFiles
distributedTriSurfaceMesh.C

