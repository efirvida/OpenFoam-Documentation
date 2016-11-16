# addPatchCellLayer 
## Class
Foam::addPatchCellLayer

## Description
Adds layers of cells to outside of polyPatch. Can optionally create
stand-alone extruded mesh (addToMesh=false).

Call setRefinement with offset vector for every patch point and number
of layers per patch face and number of layers per patch point.
- offset vector should be zero for any non-manifold point and synchronised
      on coupled points before calling this.
- offset vector of zero will not add any points.
- gets supplied the number of extruded layers both per face and per
      point. Usually the point nlayers is the max of surrounding face nlayers.

      point nlayers:
       -  0 : no extrusion. Any surrounding face being extruded becomes 'prism'
       - >0 : should be max of surrounding face nlayers.

- differing face nlayers: 'termination' : (e.g. from 2 to 4 layers) match
      at original patch face side.

        E.g. 2 boundary faces on patches a,b. 2 layers for a, 3 for b.

```
        Was:

           a      b         <- patch of boundary face
        +------+------+
        |      |      |     <- original cells
        +------+------+

        Becomes:

           a      b         <- patch of boundary face
        +------+------+
        +      +------+
        +------+------+
        +------+------+
        |      |      |     <- original cells
        +------+------+
```


- added faces get same patchID as face they are extruded from
- 'side' faces (i.e. on the edge of pp) get the patchID/zoneID of the
other patch/zone they are connected to (hopefully only 1)


E.g. 3 boundary faces on patches a,b. b gets extruded, a doesn't.

```
           a      b      b        <- patch of boundary face
        +------+------+------+
        |      |      |      |    <- cells
        +------+------+------+


               ^      ^           <- wanted extrusion vector (none at far right)
           a   |  b   |  b        <- patch of boundary face
        +------+------+------+
        |      |      |      |    <- cells
        +------+------+------+

                  b
               +------+\ b        1. prism cell added onto second b face since
           a  a|      | ----\          only one side gets extruded.
        +------+------+------+    2. side-face gets patch a, not b.
        |      |      |      |
        +------+------+------+
```


## SourceFiles
addPatchCellLayer.C

