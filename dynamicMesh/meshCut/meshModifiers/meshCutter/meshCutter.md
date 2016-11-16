# meshCutter 
## Class
Foam::meshCutter

## Description
Cuts (splits) cells.

Description of cut is given as a loop of 'cuts' per cell (see cellCuts).
setRefinement() takes this cut description and inserts the necessary
topoActions (add points/faces/cells) into the polyTopoChange.

Stores added cells/faces/points.

Cut description gives orientation to cut by calculating 'anchorPoints'.
The side of the cell that contains the anchorPoints is the master cell.
Likewise the cells' edges will have the split added as a duplicate of the
master (anchor) point.
Think of it as the cell with the anchor points at the bottom. Add a face
at the bottom to split the cell and then sweep this face up to be through
the middle of the cell (inflation).


-# Start:
       cell with anchor points at bottom
```
+-------+
    |       +
    |       +
    |       +
    |       +
    |       +
    |       +
    |       +
+-------+
anchor  anchor
```


-# Topo change:
       splitface introduced at bottom of cell, introducing a new
       cell and splitting the side faces into two.
```
+-------+
    |       +
    |       +
    |       + <- addedCell
    |       +
    |       +
    |       +
+-------+ <- splitFace
+-------+ <- original cell
anchor  anchor
```


-# Inflation:
       splitface shifted up to middle of cell (or wherever cut was)
```
+-------+
    |       +
    |       + <- addedCell
    |       +
+-------+ <- splitFace
    |       +
    |       + <- original cell
    |       +
+-------+
anchor  anchor
```

Anyway this was the original idea. Inflation was meant to handle
conservative properties distribution without interpolation.
(just face sweeping through space). But problem was that
only if the introduced splitface was exactly the same shape as bottom face
(so same 2D topo or perfectly flat) the volume between them was 0.

This meshCutting still uses anchorPoints though:
- the master cell is the one without the anchor points. The added cell
      (on top of the splitFace) is the with.
- the splitFace is owned by the master cell (since it has the lower number)
- the side faces get split and get either the original cell as neighbour
      or the added cell (if the faces contain the cell anchor points)

## SourceFiles
meshCutter.C

