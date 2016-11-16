# MarshakRadiationFvPatchScalarField 
## Class
Foam::MarshakRadiationFvPatchScalarField

## Group
grpThermoBoundaryConditions

## Description
A 'mixed' boundary condition that implements a Marshak condition for the
incident radiation field (usually written as G)

The radiation temperature is retrieved from the mesh database, using a
user specified temperature field name.

## Usage

        Property     | Description             | Required    | Default value
        T            | temperature field name  | no          | T


Example of the boundary condition specification:
```
<patchName>
{
        type            MarshakRadiation;
        T               T;
        value           uniform 0;
}
```

## See also
Foam::radiationCoupledBase
Foam::mixedFvPatchField

## SourceFiles
MarshakRadiationFvPatchScalarField.C

