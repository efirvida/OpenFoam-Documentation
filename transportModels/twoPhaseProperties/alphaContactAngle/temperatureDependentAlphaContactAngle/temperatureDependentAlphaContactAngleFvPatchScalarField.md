# temperatureDependentAlphaContactAngleFvPatchScalarField 
## Class
Foam::temperatureDependentAlphaContactAngleFvPatchScalarField

## Description
Temperature-dependent constant alphaContactAngle scalar boundary condition.

## Usage

        Property     | Description             | Required    | Default value
        T            | Temperature field name  | no          | T
        theta0       | Contact angle data      | yes         |


Example of the boundary condition specification:
```
<patchName>
{
        type            temperatureDependentAlphaContactAngle;
        theta0          constant 60;
}
```

## See also
Foam::alphaContactAngleFvPatchScalarField
Foam::constantAlphaContactAngleFvPatchScalarField

## SourceFiles
temperatureDependentAlphaContactAngleFvPatchScalarField.C

