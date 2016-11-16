# calculatedFvPatchField 
## Class
Foam::calculatedFvPatchField

## Group
grpGenericBoundaryConditions

## Description
This boundary condition is not designed to be evaluated; it is assmued
that the value is assigned via field assignment, and not via a call to
e.g. \c updateCoeffs or \c evaluate.

## Usage
Example of the boundary condition specification:
```
<patchName>
{
        type            calculated;
        value           uniform (0 0 0);    // Required value entry
}
```

## SourceFiles
calculatedFvPatchField.C

