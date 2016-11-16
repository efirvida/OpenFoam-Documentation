# cellLooper 
## Class
Foam::cellLooper

## Description
Abstract base class. Concrete implementations know how to cut a cell
(i.e. determine a loop around the circumference).

Loop around the cell is given as the vertices to be cut and edges to
be cut (and a weight between 0 and 1 giving where the cut is to be
made). Main routine is 'cut' which gets called for every cell and
gets the current cut situation and expects to return a loop on the
cell circumference.

Calling function needs to determine whether cellLooper is compatible with
existing set of cuts.

Also contains various utility functions which implementations might want to
use.

## SourceFiles
cellLooper.C

