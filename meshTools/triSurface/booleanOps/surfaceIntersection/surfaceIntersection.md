# surfaceIntersection 
## Class
Foam::surfaceIntersection

## Description
Basic surface-surface intersection description. Constructed from two
surfaces it creates a description of the intersection.

The intersection information consists of the intersection line(s)
with new points, new edges between points (note that these edges and
points are on both surfaces) and various addressing from original
surface faces/edges to intersection and vice versa.

Gets either precalculated intersection information or calculates it
itself.
Algorithm works by intersecting all edges of one surface with the other
surface and storing a reference from both faces (one on surface1, one on
surface 2) to the vertex. If the reference re-occurs we have the second
hit of both faces and an edge is created between the retrieved vertex and
the new one.

Note: when doing intersecting itself uses intersection::planarTol() as a
fraction of
current edge length to determine if intersection is a point-touching one
instead of an edge-piercing action.

## SourceFiles
surfaceIntersection.C
surfaceIntersectionFuncs.C
surfaceIntersectionTemplates.C

