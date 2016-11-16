# MarshakRadiationFixedTemperatureFvPatchScalarField 
## Class
Foam::MarshakRadiationFixedTemperatureFvPatchScalarField

## Group
grpThermoBoundaryConditions

## Description
A 'mixed' boundary condition that implements a Marshak condition for the
incident radiation field (usually written as G)

The radiation temperature field across the patch is supplied by the user
using the \c Trad entry.

## Usage

        Property     | Description             | Required    | Default value
        T            | temperature field name  | no          | T


Example of the boundary condition specification:
```
<patchName>
{
        type            MarshakRadiationFixedTemperature;
        Trad            uniform 1000;       // radiation temperature field
        value           uniform 0;          // place holder
}
```

## See also
Foam::radiationCoupledBase
Foam::mixedFvPatchField

## SourceFiles
MarshakRadiationFixedTemperatureFvPatchScalarField.C

