# fvsPatchField 
## Class
Foam::fvsPatchField

## Description
An abstract base class with a fat-interface to all derived classes
covering all possible ways in which they might be used.

The first level of derivation is to basic patchFields which cover
zero-gradient, fixed-gradient, fixed-value and mixed conditions.

The next level of derivation covers all the specialised typed with
specific evaluation proceedures, particularly with respect to specific
fields.

## SourceFiles
fvsPatchField.C
fvsPatchFieldNew.C

