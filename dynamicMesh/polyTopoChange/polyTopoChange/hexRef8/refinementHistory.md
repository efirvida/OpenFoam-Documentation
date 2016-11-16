# refinementHistory 
## Class
Foam::refinementHistory

## Description
All refinement history. Used in unrefinement.

- visibleCells: valid for the current mesh and contains per cell -1
      (cell unrefined) or an index into splitCells_.
- splitCells: for every split contains the parent (also index into
      splitCells) and optionally a subsplit as 8 indices into splitCells.
      Note that the numbers in splitCells are not cell labels, they are purely
      indices into splitCells.

E.g. 2 cells, cell 1 gets refined so end up with 9 cells:
```
        // splitCells
        9
        (
        -1 (1 2 3 4 5 6 7 8)
        0 0()
        0 0()
        0 0()
        0 0()
        0 0()
        0 0()
        0 0()
        0 0()
        )

        // visibleCells
        9(-1 1 2 3 4 5 6 7 8)
```


So cell0 (visibleCells=-1) is unrefined.
Cells 1-8 have all valid splitCells entries which are:
      - parent:0
      - subsplits:0()

The parent 0 refers back to the splitcell entries.


## SourceFiles
refinementHistory.C

