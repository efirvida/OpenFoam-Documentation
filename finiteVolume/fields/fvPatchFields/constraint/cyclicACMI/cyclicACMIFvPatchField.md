# cyclicACMIFvPatchField 
## Class
Foam::cyclicACMIFvPatchField

## Group
grpCoupledBoundaryConditions

## Description
This boundary condition enforces a cyclic condition between a pair of
boundaries, whereby communication between the patches is performed using
an arbitrarily coupled mesh interface (ACMI) interpolation.

## Usage
Example of the boundary condition specification:
```
<patchName>
{
        type            cyclicACMI;
}
```

## See also
Foam::AMIInterpolation

## SourceFiles
cyclicACMIFvPatchField.C

