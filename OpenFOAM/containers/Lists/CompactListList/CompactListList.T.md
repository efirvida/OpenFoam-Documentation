# CompactListList.T 
## Class
Foam::CompactListList

## Description
A packed storage unstructured matrix of objects of type \<T\>
using an offset table for access.

The offset table is the size of the number of rows+1
whose elements are the
accumulated sizes of the rows, i.e.
      - offset[i] gives the index of first element of row i
      - offset[i+1] - offset[i] is the number of elements in row i

Storage is allocated on free-store during construction.

As a special case a null-constructed CompactListList has an empty
offsets_ (instead of size 1).

## SourceFiles
CompactListList.C
CompactListListI.H
CompactListListIO.C

