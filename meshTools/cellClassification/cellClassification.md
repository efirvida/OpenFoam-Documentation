# cellClassification 
## Class
Foam::cellClassification

## Description
'Cuts' a mesh with a surface.

Divides cells into three types
- cut, i.e. any of the edges of the cell is split or any edge of the
      surface pierces any of the faces of the cell.
- outside: cell can be reached by Meshwave from any of the supplied
               outside points (without crossing any cut cell)
- inside:  all other.

Used in various meshing programs.

Has various utility functions to deal with 'features' on this level
where the mesh still has all inside and outside cells.

\par Concepts

- point classification:
        - point used by meshType cells only
        - point used by non-meshType cells only
        - point used by both types ('mixed')

- hanging cells: meshType cells using mixed points only.
      These cells would have all their vertices on the surface when
      extracting the meshType cells.

- regionEdges: edges where the cells using it are of mixed type.
      Or more precise when walking around the edge and looking at the
      different types of the cells there are more than two regions with
      same type.

Seen from above:
```
Ok:
         A | A
           |
         --+---
           |
         B | B

Not ok:
         A | B
           |
        ---+---
           |
         B | A
```

because this latter situation would cause the surface after subsetting
type A or B to be multiply connected across this edge. And also when
snapping the edge end points to the surface it might cause some twisted
faces if the surface is normal to the edge (and smoothing the surface
would not help since the points on the edge would be 'pulled' from two
different sides)

- regionPoints: like regionEdges but now for points.
      Points where subsetting the mesh would cause a multiply connected
      outside surface (connected across point, not edge)


## SourceFiles
cellClassification.C

