# surfaceFeatures 
## Class
Foam::surfaceFeatures

## Description
Holds feature edges/points of surface.

Feature edges are stored in one list and sorted:
        0 .. externalStart_-1               : region edges
        externalStart_ .. internalStart_-1  : external edges
        internalStart_ .. size-1            : internal edges


NOTE: angle is included angle, not feature angle and is in degrees.
The included angle is the smallest angle between two planes. For coplanar
faces it is 180, for straight angles it is 90. To pick up straight edges
only use included angle of 91 degrees


## SourceFiles
surfaceFeatures.C

