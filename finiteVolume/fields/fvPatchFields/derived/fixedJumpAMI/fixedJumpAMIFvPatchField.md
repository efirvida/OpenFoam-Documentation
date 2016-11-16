# fixedJumpAMIFvPatchField 
## Class
Foam::fixedJumpAMIFvPatchField

## Group
grpCoupledBoundaryConditions

## Description
This boundary condition provides a jump condition, across non-conformal
cyclic path-pairs, employing an arbitraryMeshInterface (AMI).

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
        type            fixedJumpAMI;
        patchType       cyclic;
        jump            uniform 10;
}
```

The above example shows the use of a fixed jump of '10'.

## Note
     The underlying \c patchType should be set to \c cyclicAMI

## See also
Foam::jumpCyclicAMIFvPatchField

## SourceFiles
fixedJumpAMIFvPatchField.C

