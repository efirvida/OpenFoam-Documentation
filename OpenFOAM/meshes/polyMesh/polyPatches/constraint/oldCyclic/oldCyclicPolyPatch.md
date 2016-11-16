# oldCyclicPolyPatch 
## Class
Foam::oldCyclicPolyPatch

## Description
'old' style cyclic polyPatch with all faces in single patch. Does ordering
but cannot be used to run. Writes 'type cyclic' so foamUpgradeCyclics
can be run afterwards.
Used to get cyclics from mesh converters that assume cyclics in single
patch (e.g. fluent3DMeshToFoam)

## SourceFiles
oldCyclicPolyPatch.C

