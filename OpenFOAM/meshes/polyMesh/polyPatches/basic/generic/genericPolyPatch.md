# genericPolyPatch 
## Class
Foam::genericPolyPatch

## Description
Substitute for unknown patches. Used for postprocessing when only
basic polyPatch info is needed.

## Note
Storage is not optimal. It stores all face centres and cells on all
processors to keep the addressing calculation simple.

## SourceFiles
genericPolyPatch.C

