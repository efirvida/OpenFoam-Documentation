# partialSlipFvPatchField 
## Class
Foam::partialSlipFvPatchField

## Group
grpWallBoundaryConditions grpGenericBoundaryConditions

## Description
This boundary condition provides a partial slip condition.  The amount of
slip is controlled by a user-supplied field.

## Usage

        Property      | Description             | Required    | Default value
        valueFraction | fraction od value used for boundary [0-1] | yes |


Example of the boundary condition specification:
```
<patchName>
{
        type            partialSlip;
        valueFraction   uniform 0.1;
        value           uniform 0;
}
```

## See also
Foam::transformFvPatchField

## SourceFiles
partialSlipFvPatchField.C

