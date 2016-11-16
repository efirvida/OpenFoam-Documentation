# abort 
## Class
Foam::functionObjects::abort

## Group
grpUtilitiesFunctionObjects

## Description
Watches for presence of the named file in the $FOAM_CASE directory
and aborts the calculation if it is present.

Currently the following action types are supported:
- noWriteNow
- writeNow
- nextWrite

## SourceFiles
abort.C

