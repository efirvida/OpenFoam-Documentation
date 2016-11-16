# cellCuts 
## Class
Foam::cellCuts

## Description
Description of cuts across cells.

Description of cut is given as list of vertices and
list of edges to be cut (and position on edge).

Does some checking of correctness/non-overlapping of cuts. 2x2x2
refinement has to be done in three passes since cuts can not overlap
(would make addressing too complicated)

Introduces concept of 'cut' which is either an existing vertex
or a edge.

Input can either be
-# list of cut vertices and list of cut edges. Constructs cell
       circumference walks ('cellLoops').

-# list of cell circumference walks. Will filter them so they
       don't overlap.

-# cellWalker and list of cells to refine (refineCell). Constructs
       cellLoops and does B. cellWalker is class which can cut a single
       cell using a plane through the cell centre and in a certain normal
       direction

CellCuts constructed from cellLoops (B, C) can have multiple cut-edges
and/or cut-point as long as there is per face only one (or none) cut across
a face, i.e. a face can only be split into two faces.

The information available after construction:
      - pointIsCut, edgeIsCut.
      - faceSplitCut : the cross-cut of a face.
      - cellLoops : the loop which cuts across a cell
      - cellAnchorPoints : per cell the vertices on one side which are
        considered the anchor points.

AnchorPoints: connected loops have to be oriented in the same way to
be able to grow new internal faces out of the same bottom faces.
(limitation of the mapping procedure). The loop is cellLoop is oriented
such that the normal of it points towards the anchorPoints.
This is the only routine which uses geometric information.


Limitations:
- cut description is very precise. Hard to get right.
- do anchor points need to be unique per cell? Very inefficient.
- is orientation guaranteed to be correct? Uses geometric info so can go
      wrong on highly distorted meshes.
- is memory inefficient. Probably need to use Maps instead of
      labelLists.

## SourceFiles
cellCuts.C

