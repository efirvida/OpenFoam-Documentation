# globalIndexAndTransform 
## Class
Foam::globalIndexAndTransform

## Description
Determination and storage of the possible independent transforms
introduced by coupledPolyPatches, as well as all of the possible
permutations of these transforms generated by the presence of
multiple coupledPolyPatches, i.e. more than one cyclic boundary.

Also provides global index encoding and decoding for entity
(i.e. cell) index, processor index and transform index (0 or
positive integer) to a labelPair.

## SourceFiles
globalIndexAndTransform.C

