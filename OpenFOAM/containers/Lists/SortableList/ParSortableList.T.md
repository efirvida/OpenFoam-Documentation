# ParSortableList.T 
## Class
Foam::ParSortableList

## Description
Implementation of PSRS parallel sorting routine.

From "On the Versatility of Parallel Sorting by Regular Sampling"
Xiaobo Li et. all.

Construct from list of things to sort (uses SortableList, 'thing' should
implement >, ==).

Will contain sorted data and in
        - indices() the original indices
        - procs() the original processor id.

Can also be constructed from size, filled at ease and then sort()'ed.

## SourceFiles
ParSortableList.C

