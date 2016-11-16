# tetIndices 
## Class
Foam::tetIndices

## Description
Storage and named access for the indices of a tet which is part of
the decomposition of a cell.

Tets are designated by
- cell (of course)
- face on cell
- three points on face (faceBasePt, facePtA, facePtB)
      When constructing from a mesh and index in the face (tetPtI):
        - faceBasePt is the mesh.tetBasePtIs() base point
        - facePtA is tetPtI away from faceBasePt
        - facePtB is next one after/before facePtA
        e.g.:

            +---+
            |2 /|
            | / |
            |/ 1|  <- tetPt (so 1 for first triangle, 2 for second)
            +---+
            ^
           faceBasePt

## SourceFiles
tetIndicesI.H
tetIndices.C

