# fixedNormalSlipFvPatchField 
## Class
Foam::fixedNormalSlipFvPatchField

## Group
grpGenericBoundaryConditions grpWallBoundaryConditions

## Description
This boundary condition sets the patch-normal component to a fixed value.

## Usage

        Property     | Description             | Required    | Default value
        fixedValue   | fixed value             | yes         |


Example of the boundary condition specification:
```
<patchName>
{
        type            fixedNormalSlip;
        fixedValue      uniform 0;     // example entry for a scalar field
}
```

## See also
Foam::transformFvPatchField

## SourceFiles
fixedNormalSlipFvPatchField.C

