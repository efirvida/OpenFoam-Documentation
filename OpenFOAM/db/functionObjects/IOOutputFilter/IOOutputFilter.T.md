# IOOutputFilter.T 
## Class
Foam::IOOutputFilter

## Description
IOdictionary wrapper around OutputFilter to allow them to read from
their associated dictionaries.

## Note
The IOobject or the objectRegistry will normally have to be
derived from a fvMesh for a subsequent cast (within OutputFilter)
to work correctly.

## SourceFiles
IOOutputFilter.C

