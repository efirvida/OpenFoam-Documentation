# PointEdgeWave.T 
## Class
Foam::PointEdgeWave

## Description
Wave propagation of information through grid. Every iteration
information goes through one layer of edges.

Templated on information that is transferred.

Handles parallel and cyclics. Only parallel reasonably tested. Cyclics
hardly tested.

Note: whether to propagate depends on the return value of Type::update
which returns true (i.e. propagate) if the value changes by more than a
certain tolerance.

Note: parallel is done in two steps:
      -# transfer patch points in offset notation, i.e. every patch
         point is denoted by a patchface label and an index in this face.
         Receiving end uses that fact that f[0] is shared and order is
         reversed.
      -# do all non-local shared points by means of reduce of data on them.

Note: cyclics is with offset in patchface as well. Patch is divided into
two sub patches and the point-point addressing is never explicitly
calculated but instead use is made of the face-face correspondence.
(it probably is more efficient to calculate a point-point
correspondence at the start and then reuse this; task to be done)

## SourceFiles
PointEdgeWave.C

