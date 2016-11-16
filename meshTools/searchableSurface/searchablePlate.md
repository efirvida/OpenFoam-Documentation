# searchablePlate 
## Class
Foam::searchablePlate

## Description
Searching on finite plate. Plate has to be aligned with coordinate
axes.
Plate defined as origin and span. One of the components of span has
to be 0 which defines the normal direction. E.g.

    span    = (Sx Sy 0)     // plate in x-y plane
origin  = (Ox Oy Oz)

now plane is from (Ox Oy Oz) to (Ox+Sx Oy+Sy Oz)

## SourceFiles
searchablePlate.C

