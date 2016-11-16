# procFacesGAMGProcAgglomeration 
## Class
Foam::procFacesGAMGProcAgglomeration

## Description
Processor agglomeration of GAMGAgglomerations. Needs nAgglomeratingCells
which is when to start agglomerating processors. Processors get agglomerated
by constructing a single cell mesh for each processor with each
processor interface a face. This then gets agglomerated using
the pairGAMGAgglomeration algorithm with the number of faces
on the original processor interface as face weight.

## SourceFiles
procFacesGAMGProcAgglomeration.C

