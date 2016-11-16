# sampledTriSurfaceMesh 
## Class
Foam::sampledTriSurfaceMesh

## Description
A sampledSurface from a triSurfaceMesh. It samples on the points/triangles
of the triSurface.

- it either samples cells or (non-coupled) boundary faces

- 6 different modes:
        - source=cells, interpolate=false:
            finds per triangle centre the nearest cell centre and uses its value
        - source=cells, interpolate=true
            finds per triangle centre the nearest cell centre.
            Per surface point checks if this nearest cell is the one containing
            point; otherwise projects the point onto the nearest point on
            the boundary of the cell (to make sure interpolateCellPoint
            gets a valid location)

        - source=insideCells, interpolate=false:
            finds per triangle centre the cell containing it and uses its value.
            Trims triangles outside mesh.
        - source=insideCells, interpolate=true
            Per surface point interpolate cell containing it.

        - source=boundaryFaces, interpolate=false:
            finds per triangle centre the nearest point on the boundary
            (uncoupled faces only) and uses the value (or 0 if the nearest
            is on an empty boundary)
        - source=boundaryFaces, interpolate=true:
            finds per triangle centre the nearest point on the boundary
            (uncoupled faces only).
            Per surface point projects the point onto this boundary face
            (to make sure interpolateCellPoint gets a valid location)

- since it finds a nearest per triangle each triangle is guaranteed
to be on one processor only. So after stitching (by sampledSurfaces)
the original surface should be complete.

## SourceFiles
sampledTriSurfaceMesh.C

