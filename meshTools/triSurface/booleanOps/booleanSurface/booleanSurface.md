# booleanSurface 
## Class
Foam::booleanSurface

## Description
Surface-surface intersection. Given two surfaces construct combined surface.

Called 'boolean' since the volume of resulting surface will encompass
the volumes of the original surface according to some boolean operation:
- all which is in surface1 AND in surface2 (intersection)
- all which is in surface1 AND NOT in surface2 (surface1 minus surface2)
- all which is in surface1 OR in surface2 (union)

Algorithm:
-# find edge-surface intersection. Class 'surfaceIntersection'.
-# combine intersection with both surfaces. Class 'intersectedSurface'.
-# subset surfaces upto intersection. The 'side' of the surface to
       include is based on the faces that can be reached from a
       user-supplied face index.
-# merge surfaces. Only the points on the intersection are shared.

## SourceFiles
booleanSurface.C

