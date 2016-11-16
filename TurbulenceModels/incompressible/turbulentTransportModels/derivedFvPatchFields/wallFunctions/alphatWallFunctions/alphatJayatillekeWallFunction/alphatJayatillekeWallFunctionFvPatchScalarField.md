# alphatJayatillekeWallFunctionFvPatchScalarField 
## Class
Foam::incompressible::alphatJayatillekeWallFunctionFvPatchScalarField

## Group
grpIcoWallFunctions

## Description
This boundary condition provides a kinematic turbulent thermal conductivity
for using wall functions, using the Jayatilleke 'P' function.

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
}
```

## Note
The units of kinematic turbulent thermal conductivity are [m2/s]

## See also
Foam::fixedValueFvPatchField

## SourceFiles
alphatJayatillekeWallFunctionFvPatchScalarField.C

