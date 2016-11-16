# nonBlockingGaussSeidelSmoother 
## Class
Foam::nonBlockingGaussSeidelSmoother

## Description
Variant of gaussSeidelSmoother that expects processor boundary
cells to be sorted last and so can block later. Only when the
cells are actually visited does it need the results to be present.
It is expected that there is little benefit to be gained from doing
this on a patch by patch basis since the number of processor interfaces
is quite small and the overhead of checking whether a processor interface
is finished might be quite high (call into mpi). Also this would
require a dynamic memory allocation to store the state of the outstanding
requests.

## SourceFiles
nonBlockingGaussSeidelSmoother.C

