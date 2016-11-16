# intersectedSurface 
## Class
Foam::intersectedSurface

## Description
Given triSurface and intersection creates the intersected
(properly triangulated) surface.
(note: intersection is the list of points and edges 'shared'
by two surfaces)

Algorithm:
- from the intersection get the points created on the edges of the surface
- split the edges of the surface
- construct a new edgeList with (in this order) the edges from the
      intersection ('cuts', i.e. the edges shared with the other surface)
      and the (split) edges from the original triangles (from 0 ..
      nSurfaceEdges)
- construct face-edge addressing for above edges
- for each face do a right-handed walk to reconstruct faces (splitFace)
- retriangulate resulting faces (might be non-convex so use
      faceTriangulation which does proper bisection)

The resulting surface will have the points from the surface first
in the point list (0 .. nSurfacePoints-1)

Note: problematic are the cut-edges which are completely inside a face.
These will not be visited by a edge-point-edge walk. These are handled by
resplitFace which first connects the 'floating' edges to triangle edges
with two extra edges and then tries the splitting again. Seems to work
(mostly). Will probably fail for boundary edge (edge with only face).

Note: points are compact, i.e. points().size() == localPoints().size()
(though points() probably not localPoints())

## SourceFiles
intersectedSurface.C

