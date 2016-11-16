# triSurfaceMesh 
## Class
Foam::triSurfaceMesh

## Description
IOoject and searching on triSurface

Note: when constructing from dictionary has optional parameters:
        - scale     : scaling factor.
        - tolerance : relative tolerance for doing intersections
                      (see triangle::intersection)
        - minQuality: discard triangles with low quality when getting normal

## SourceFiles
triSurfaceMesh.C

