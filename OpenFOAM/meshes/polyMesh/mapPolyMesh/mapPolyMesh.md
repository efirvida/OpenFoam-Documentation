# mapPolyMesh 
## Class
Foam::mapPolyMesh

## Description
Class containing mesh-to-mesh mapping information after a change
in polyMesh topology.

General:
        - pointMap/faceMap/cellMap: \n
          from current mesh back to previous mesh.
          (so to 'pull' the information onto the current mesh)
        - reversePointMap/faceMap/cellMap: \n
          from previous mesh to current. (so to 'push' information)

In the topology change points/faces/cells
- can be unchanged. (faces might be renumbered though)
- can be removed (into nothing)
- can be removed into/merged with existing same entity
      (so point merged with other point, face with other face, cell with
       other cell. Note that probably only cell with cell is relevant)
- can be added from existing same 'master' entity
      (so point from point, face from face and cell from cell)
- can be inflated: face out of edge or point,
        cell out of face, edge or point.
- can be appended: added 'out of nothing'.

All this information is necessary to correctly map fields.

\par points

- unchanged:
        - pointMap[pointi] contains old point label
        - reversePointMap[oldPointi] contains new point label
- removed:
        - reversePointMap[oldPointi] contains -1
- merged into point:
        - reversePointMap[oldPointi] contains <-1 : -newPointi-2
        - pointMap[pointi] contains the old master point label
        - pointsFromPoints gives for pointi all the old point labels
          (including the old master point!)
- added-from-same:
        - pointMap[pointi] contains the old master point label
- appended:
        - pointMap[pointi] contains -1

\par faces

- unchanged:
        - faceMap[facei] contains old face label
        - reverseFaceMap[oldFacei] contains new face label
- removed:
        - reverseFaceMap[oldFacei] contains -1
- merged into face:
        - reverseFaceMap[oldFacei] contains <-1 : -newFacei-2
        - faceMap[facei] contains the old master face label
        - facesFromFaces gives for facei all the old face labels
          (including the old master face!)
- added-from-same:
        - faceMap[facei] contains the old master face label
- inflated-from-edge:
        - faceMap[facei] contains -1
        - facesFromEdges contains an entry with
            - facei
            - list of faces(*) on old mesh that connected to the old edge
- inflated-from-point:
        - faceMap[facei] contains -1
        - facesFromPoints contains an entry with
            - facei
            - list of faces(*) on old mesh that connected to the old point
- appended:
        - faceMap[facei] contains -1

Note (*) \n
       if the newly inflated face is a boundary face the list of faces will
       only be boundary faces; if the new face is an internal face they
       will only be internal faces.

\par cells

- unchanged:
        - cellMap[celli] contains old cell label
        - reverseCellMap[oldCelli] contains new cell label
- removed:
        - reverseCellMap[oldCelli] contains -1
- merged into cell:
        - reverseCellMap[oldCelli] contains <-1 : -newCelli-2
        - cellMap[celli] contains the old master cell label
        - cellsFromCells gives for celli all the old cell labels
          (including the old master cell!)
- added-from-same:
        - cellMap[celli] contains the old master cell label
- inflated-from-face:
        - cellMap[celli] contains -1
        - cellsFromFaces contains an entry with
            - celli
            - list of cells on old mesh that connected to the old face
- inflated-from-edge:
        - cellMap[celli] contains -1
        - cellsFromEdges contains an entry with
            - celli
            - list of cells on old mesh that connected to the old edge
- inflated-from-point:
        - cellMap[celli] contains -1
        - cellsFromPoints contains an entry with
            - celli
            - list of cells on old mesh that connected to the old point
- appended:
        - cellMap[celli] contains -1


## SourceFiles
mapPolyMesh.C

