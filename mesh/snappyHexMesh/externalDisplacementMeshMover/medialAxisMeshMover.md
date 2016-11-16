# medialAxisMeshMover 
## Class
Foam::medialAxisMeshMover

## Description
Mesh motion solver that uses a medial axis algorithm to work
out a fraction between the (nearest point on a) moving surface
and the (nearest point on a) fixed surface.
This fraction is then used to scale the motion. Use
- fixedValue on all moving patches
- zeroFixedValue on stationary patches
- slip on all slipping patches

## SourceFiles
medialAxisMeshMover.C

