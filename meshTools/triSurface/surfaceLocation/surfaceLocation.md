# surfaceLocation 
## Class
Foam::surfaceLocation

## Description
Contains information about location on a triSurface

Access to data:
      - pointIndexHit provides
        - location
        - bool: hit/miss
        - index (of triangle/point/edge)
      - elementType() provides
        - what index above relates to. In triangle::proxType
      - triangle() provides
        - last known triangle

## SourceFiles
surfaceLocation.C

