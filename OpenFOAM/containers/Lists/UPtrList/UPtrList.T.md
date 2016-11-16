# UPtrList.T 
## Class
Foam::UPtrList

## Description
A templated 1D list of pointers to objects of type \<T\>, where the
size of the array is known and used for subscript bounds checking, etc.

The element operator [] returns a reference to the object rather than a
pointer.  Storage is not allocated during construction or use but is
supplied to the constructor as an argument.

## SourceFiles
UPtrList.C
UPtrListIO.C

