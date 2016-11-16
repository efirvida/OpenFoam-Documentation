# nutUTabulatedWallFunctionFvPatchScalarField 
## Class
Foam::nutUTabulatedWallFunctionFvPatchScalarField

## Group
grpWallFunctions

## Description
This boundary condition provides a turbulent kinematic viscosity condition
when using wall functions.  As input, the user specifies a look-up table
of U+ as a function of near-wall Reynolds number.  The table should be
located in the $FOAM_CASE/constant directory.

## Usage

        Property     | Description             | Required    | Default value
        uPlusTable   | U+ as a function of Re table name | yes |


Example of the boundary condition specification:
```
<patchName>
{
        type            nutTabulatedWallFunction;
        uPlusTable      myUPlusTable;
}
```

## Note
The tables are not registered since the same table object may be used for
more than one patch.

## See also
Foam::nutWallFunctionFvPatchScalarField

## SourceFiles
nutUTabulatedWallFunctionFvPatchScalarField.C

