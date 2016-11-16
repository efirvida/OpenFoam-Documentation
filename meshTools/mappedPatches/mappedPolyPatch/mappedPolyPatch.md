# mappedPolyPatch 
## Class
Foam::mappedPolyPatch

## Description
Determines a mapping between patch face centres and mesh cell or face
centres and processors they're on.

## Note
Storage is not optimal. It stores all face centres and cells on all
processors to keep the addressing calculation simple.

## SourceFiles
mappedPolyPatch.C

