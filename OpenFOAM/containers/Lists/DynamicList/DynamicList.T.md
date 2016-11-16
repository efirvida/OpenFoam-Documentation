# DynamicList.T 
## Class
Foam::DynamicList

## Description
A 1D vector of objects of type \<T\> that resizes itself as necessary to
accept the new objects.

Internal storage is a compact array and the list can be shrunk to compact
storage. The increase of list size is controlled by three template
parameters, which allows the list storage to either increase by the given
increment or by the given multiplier and divider (allowing non-integer
multiples).

## SourceFiles
DynamicListI.H
DynamicList.C

