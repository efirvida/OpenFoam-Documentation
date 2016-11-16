# UList.T 
## Class
Foam::UList

## Description
A 1D vector of objects of type \<T\>, where the size of the vector is
known and can be used for subscript bounds checking, etc.

Storage is not allocated during construction or use but is supplied to
the constructor as an argument.  This type of list is particularly useful
for lists that refer to parts of existing lists such as SubList.

## SourceFiles
UList.C
UListI.H
UListIO.C

