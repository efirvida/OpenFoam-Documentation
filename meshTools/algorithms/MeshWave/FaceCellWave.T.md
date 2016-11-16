# FaceCellWave.T 
## Class
Foam::FaceCellWave

## Description
Wave propagation of information through grid. Every iteration
information goes through one layer of cells. Templated on information
that is transferred.

Handles parallel and cyclics and non-parallel cyclics.

Note: whether to propagate depends on the return value of Type::update
which returns true (i.e. propagate) if the value changes by more than a
certain tolerance.
This tolerance can be very strict for normal face-cell and parallel
cyclics (we use a value of 0.01 just to limit propagation of small changes)
but for non-parallel cyclics this tolerance can be critical and if chosen
too small can lead to non-convergence.

## SourceFiles
FaceCellWave.C

