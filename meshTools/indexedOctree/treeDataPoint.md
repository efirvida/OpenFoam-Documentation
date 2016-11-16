# treeDataPoint 
## Class
Foam::treeDataPoint

## Description
Holds (reference to) pointField. Encapsulation of data needed for
octree searches.
Used for searching for nearest point. No bounding boxes around points.
Only overlaps and calcNearest are implemented, rest makes little sense.

Optionally works on subset of points.

## SourceFiles
treeDataPoint.C

