# globalIndex 
## Class
Foam::globalIndex

## Description
Calculates a unique integer (label so might not have enough room - 2G max)
for processor + local index. E.g.

globalIndex globalFaces(mesh.nFaces());
label globalFacei = globalFaces.toGlobal(facei);


## SourceFiles
globalIndexI.H
globalIndex.C
globalIndexTemplates.C

