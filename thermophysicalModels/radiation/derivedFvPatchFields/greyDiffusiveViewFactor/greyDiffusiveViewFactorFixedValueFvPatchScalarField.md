# greyDiffusiveViewFactorFixedValueFvPatchScalarField 
## Class
Foam::radiation::greyDiffusiveViewFactorFixedValueFvPatchScalarField

## Group
grpThermoBoundaryConditions

## Description
This boundary condition provides a grey-diffuse condition for radiative
heat flux, \c Qr, for use with the view factor model

## Usage

        Property     | Description             | Required    | Default value
        Qro          | external radiative heat flux | yes    |
        emissivityMode | emissivity mode: solidRadiation or lookup | yes |


Example of the boundary condition specification:
```
<patchName>
{
        type            greyDiffusiveRadiationViewFactor;
        Qro             uniform 0;
        emissivityMode  solidRadiation;
        value           uniform 0;
}
```

## See also
Foam::radiationCoupledBase
Foam::radiation::radiationModel
Foam::radiation::viewFactor
Foam::fixedValueFvPatchField

## SourceFiles
greyDiffusiveViewFactorFixedValueFvPatchScalarField.C

