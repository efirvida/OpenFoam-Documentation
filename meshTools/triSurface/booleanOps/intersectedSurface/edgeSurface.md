# edgeSurface 
## Class
Foam::edgeSurface

## Description
Description of surface in form of 'cloud of edges'.

The 'cloud of edges':
- points
- edges
- faceEdges
- parentEdge (edge on surface this edge originates from)
and nothing more.

(pointEdges constructed from above data)

Constructed from triSurface and surfaceIntersection. (uses localPoints
of surface of course)

Used to easily insert cuts and split faces.

## Note
- points with surface (local)points first, intersection points last
- edges with (split) surface edges first, intersection edges last.

## SourceFiles
edgeSurface.C

