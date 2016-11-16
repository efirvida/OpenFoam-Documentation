# cyclicAMIFvPatchField 
## Class
Foam::cyclicAMIFvPatchField

## Group
grpCoupledBoundaryConditions

## Description
This boundary condition enforces a cyclic condition between a pair of
boundaries, whereby communication between the patches is performed using
an arbitrary mesh interface (AMI) interpolation.

## Usage
Example of the boundary condition specification:
```
<patchName>
{
        type            cyclicAMI;
}
```

## Note
The outer boundary of the patch pairs must be similar, i.e. if the owner
patch is transformed to the neighbour patch, the outer perimiter of each
patch should be identical (or very similar).

## See also
Foam::AMIInterpolation

## SourceFiles
cyclicAMIFvPatchField.C

