# geomCellLooper 
## Class
Foam::geomCellLooper

## Description
Implementation of cellLooper. Does pure geometric cut through cell.

Handles all cell shapes in the same way: cut edges with plane through
cell centre and normal in direction of provided direction. Snaps cuts
close to edge endpoints (close = snapTol * minEdgeLen) to vertices.

Currently determines cuts through edges (and edgeendpoints close to plane)
in random order and then sorts them acc. to angle. Could be converted to
use walk but problem is that face can be cut multiple times (since does
not need to be convex). Another problem is that edges parallel to plane
might not be cut. So these are handled by looking at the distance from
edge endpoints to the plane.

## SourceFiles
geomCellLooper.C

