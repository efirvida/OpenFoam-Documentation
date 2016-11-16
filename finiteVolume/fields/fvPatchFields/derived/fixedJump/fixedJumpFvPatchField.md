# fixedJumpFvPatchField 
## Class
Foam::fixedJumpFvPatchField

## Group
grpCoupledBoundaryConditions

## Description
This boundary condition provides a jump condition, using the \c cyclic
condition as a base.

The jump is specified as a fixed value field, applied as an offset to the
'owner' patch.

## Usage

        Property     | Description             | Required    | Default value
        patchType    | underlying patch type should be \c cyclic| yes |
        jump         | current jump value      | yes         |


Example of the boundary condition specification:
```
<patchName>
{
        type            fixedJump;
        patchType       cyclic;
        jump            uniform 10;
}
```

The above example shows the use of a fixed jump of '10'.

## Note
     The underlying \c patchType should be set to \c cyclic

## See also
Foam::jumpCyclicFvPatchField

## SourceFiles
fixedJumpFvPatchField.C

