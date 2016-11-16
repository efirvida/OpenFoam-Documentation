# meshReader 
## Class
Foam::meshReader

## Description
This class supports creating polyMeshes with baffles.

The derived classes are responsible for providing the protected data.
This implementation is somewhat messy, but could/should be restructured
to provide a more generalized reader (at the moment it has been written
for converting pro-STAR data).

The meshReader supports cellTable information (see new user's guide entry).

## Note
The boundary definitions are given as cell/face.

## SourceFiles
calcPointCells.C
createPolyBoundary.C
createPolyCells.C
meshReader.C
meshReaderAux.C

