# cyclicFvPatchField 
## Class
Foam::cyclicFvPatchField

## Group
grpCoupledBoundaryConditions

## Description
This boundary condition enforces a cyclic condition between a pair of
boundaries.

## Usage
Example of the boundary condition specification:
```
<patchName>
{
        type            cyclic;
}
```

## Note
The patches must be topologically similar, i.e. if the owner patch is
transformed to the neighbour patch, the patches should be identical (or
very similar).

## SourceFiles
cyclicFvPatchField.C

