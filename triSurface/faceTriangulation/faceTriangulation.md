# faceTriangulation 
## Class
Foam::faceTriangulation

## Description
Triangulation of faces. Handles concave polygons as well
(inefficiently)

Works by trying to subdivide the face at the vertex with 'flattest'
internal angle (i.e. closest to 180 deg).

Based on routine 'Diagonal' in
```
        "Efficient Triangulation of Simple Polygons"
        Godfried Toussaint, McGill University.
```

After construction is the list of triangles the face is decomposed into.
(Or empty list if no valid triangulation could be found).


## SourceFiles
faceTriangulation.C

