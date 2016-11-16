# cellZone 
## Class
Foam::cellZone

## Description
A subset of mesh cells.

Currently set up as an indirect list but will be extended to use a
primitive mesh.  For quick check whether a cell belongs to the zone use
the lookup mechanism in cellZoneMesh, where all the zoned cells are
registered with their zone number.

## SourceFiles
cellZone.C
cellZoneNew.C

