# faceCoupleInfo 
## Class
Foam::faceCoupleInfo

## Description
Container for information needed to couple to meshes. When constructed
from two meshes and a geometric tolerance finds the corresponding
boundary faces.

The information it keeps is the set of faces&points (cutFaces,
cutPoints) that should replace a set of faces on the master
(masterPatch) and a set of faces on the slave (slavePatch)


Uses same tolerance to match faces and points on matched faces since
they both originate from the same points and the tolerance usually
comes from writing these points with limited precision (6 by default)

-# Perfect match:
       - one-to-one match for faces and points.
       - the cut is always the 'most connected' of the master and slave so
         multiple master or slave points might point to the same cut point.

```
e.g. master:

        +--+
        |  |
        |  |
        +--+
            +--+
            |  |
            |  |
            +--+
slave:
            +--+
            |  |
            |  |
            +--+
        +--+
        |  |
        |  |
        +--+
```
adding both together creates a singly connected 2x2 cavity so suddenly
the duplicate master points and the duplicate slave points all become
a single cut point.


-# Subdivision match:
       - Can be constructed from slave being subdivision of master with the
         polyPatch constructor.
       - Does not include above shared-point detection!

Notes on multiple slave faces per master:

As long as
- all master edges are present in slave
- slave can have extra edges/points/faces BUT all subfaces have to have
      at least one point on a maste face.

```
So master:
+-------+
    |       |
    |       |
    |       |
    |       |
    |       |
    |       |
    |       |
+-------+

slave:
+---+---+
|\  |  /|
| \ | / |
|  \|/  |
+---+---+
|  /|\  |
| / | \ |
|/  |  \|
+---+---+
is ok.
```

For this kind of matching the order is:
- match cutpoint to masterpoint
- find those cutEdges that align with a master edge. This gives two sets
      of cut edges: those that have a master equivalent ('border edges') and
      those that don't ('internal edges'). The border edges now divide the
      cutFaces into regions with the same masterFace correspondence.
- find cutFaces that are fully determined by the border edges they use.
- all cutFaces that are connected through an internal edge have the same
      master face.


Note: matching refined faces onto master is a bit dodgy and will probably
only work for unwarped faces. Also it will fail if e.g. face is split
into 3x3 since then middle face has no point/edge in common with master.
(problem is in face matching (findSlavesCoveringMaster), probably
     point/edge matching might just work)


## SourceFiles
faceCoupleInfo.C


