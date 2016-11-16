# alphatJayatillekeWallFunctionFvPatchScalarField 
## Class
Foam::compressible::alphatJayatillekeWallFunctionFvPatchScalarField

## Group
grpCmpWallFunctions

## Description
This boundary condition provides a thermal wall function for turbulent
thermal diffusivity (usually\c alphat) based on the Jayatilleke model.

## Usage

        Property     | Description             | Required    | Default value
        Prt          | turbulent Prandtl number | no         | 0.85
        Cmu          | model coefficient       | no          | 0.09
        kappa        | Von Karman constant     | no          | 0.41
        E            | model coefficient       | no          | 9.8


Example of the boundary condition specification:
```
<patchName>
{
        type            alphatJayatillekeWallFunction;
        Prt             0.85;
        kappa           0.41;
        E               9.8;
        value           uniform 0; // optional value entry
}
```

## See also
Foam::fixedValueFvPatchField

## SourceFiles
alphatJayatillekeWallFunctionFvPatchScalarField.C

