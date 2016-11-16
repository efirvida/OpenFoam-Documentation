# cyclicPolyPatch 
## Class
Foam::cyclicPolyPatch

## Description
Cyclic plane patch.

Note: morph patch face ordering uses geometric matching so with the
following restrictions:
        -coupled patches should be flat planes.
        -no rotation in patch plane

Uses coupledPolyPatch::calcFaceTol to calculate
tolerance per face which might need tweaking.

Switch on 'cyclicPolyPatch' debug flag to write .obj files to show
the matching.

## SourceFiles
cyclicPolyPatch.C

