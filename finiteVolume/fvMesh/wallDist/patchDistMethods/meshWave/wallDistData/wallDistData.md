# wallDistData 
## Class
Foam::wallDistData

## Description
Wall distance calculation. Like wallDist but also transports extra
data (template argument).

Used for e.g reflection vector calculation or vanDriest damping.

Templated on two parameters:
        - TransferType: type of overall data transported
          (e.g. wallPointData\<vector\>)

## SourceFiles
wallDistData.C

