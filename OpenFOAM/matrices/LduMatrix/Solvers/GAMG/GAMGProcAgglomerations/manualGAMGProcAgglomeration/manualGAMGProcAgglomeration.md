# manualGAMGProcAgglomeration 
## Class
Foam::manualGAMGProcAgglomeration

## Description
Manual processor agglomeration of GAMGAgglomerations.

In the GAMG control dictionary:

        processorAgglomerator manual;
        // List of level+procagglomeration where
        // procagglomeration is a set of labelLists. Each labelList is
        // a cluster of processor which gets combined onto the first element
        // in the list.
        processorAgglomeration
        (
            (
                3           //at level 3
                (
                    (0 1)   //coarse 0 from 0,1 (and moved onto 0)
                    (3 2)   //coarse 1 from 2,3 (and moved onto 3)
                )
            )
            (
                6           //at level6
                (
                    (0 1)   //coarse 0 from 0,1 (and moved onto 0)
                )
            )
        );

## SourceFiles
manualGAMGProcAgglomeration.C

