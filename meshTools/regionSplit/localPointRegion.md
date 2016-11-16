# localPointRegion 
## Class
Foam::localPointRegion

## Description
Takes mesh with 'baffles' (= boundary faces sharing points).
Determines for selected points on boundary faces the 'point region' it is
connected to. Each region can be visited by a cell-face-cell walk.
Used in duplicating points after splitting baffles.

Regions are not consecutive per processor. They will be -1..nRegions_.

Note: coupled boundaries (cyclics, parallel) not fully tested.

## SourceFiles
localPointRegion.C

