# wideBandDiffusiveRadiationMixedFvPatchScalarField 
## Class
Foam::radiation::wideBandDiffusiveRadiationMixedFvPatchScalarField

## Group
grpThermoBoundaryConditions

## Description
This boundary condition provides a wide-band, diffusive radiation
condition, where the patch temperature is specified.

## Usage

        Property     | Description             | Required    | Default value
        T            | temperature field name  | no          | T


Example of the boundary condition specification:
```
<patchName>
{
        type            wideBandDiffusiveRadiation;
        value           uniform 0;
}
```

## See also
Foam::mixedFvPatchScalarField
Foam::radiationCoupledBase

## SourceFiles
wideBandDiffusiveRadiationMixedFvPatchScalarField.C

