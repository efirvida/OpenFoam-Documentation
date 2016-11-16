# greyDiffusiveRadiationMixedFvPatchScalarField 
## Class
Foam::radiation::greyDiffusiveRadiationMixedFvPatchScalarField

## Group
grpThermoBoundaryConditions

## Description
This boundary condition provides a grey-diffuse condition for radiation
intensity, \c I, for use with the finite-volume discrete-ordinates model
(fvDOM), in which the radiation temperature is retrieved from the
temperature field boundary condition.

## Usage

        Property     | Description             | Required    | Default value
        T            | temperature field name  | no          | T
        emissivityMode | emissivity mode: solidRadiation or lookup | yes |


Example of the boundary condition specification:
```
<patchName>
{
        type            greyDiffusiveRadiation;
        T               T;
        emissivityMode  solidRadiation;
        value           uniform 0;
}
```

## See also
Foam::radiationCoupledBase
Foam::radiation::radiationModel
Foam::radiation::fvDOM
Foam::mixedFvPatchField

## SourceFiles
greyDiffusiveRadiationMixedFvPatchScalarField.C

