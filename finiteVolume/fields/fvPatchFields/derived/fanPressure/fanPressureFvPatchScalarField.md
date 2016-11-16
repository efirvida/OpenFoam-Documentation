# fanPressureFvPatchScalarField 
## Class
Foam::fanPressureFvPatchScalarField

## Group
grpInletBoundaryConditions grpOutletBoundaryConditions

## Description
This boundary condition can be applied to assign either a pressure inlet
or outlet total pressure condition for a fan.

## Usage

        Property     | Description             | Required    | Default value
        fileName     | fan curve file name     | yes         |
        outOfBounds  | out of bounds handling  | yes         |
        direction    | direction of flow through fan [in/out] | yes |
        p0           | environmental total pressure | yes    |


Example of the boundary condition specification:
```
inlet
{
        type            fanPressure;
        fileName        "fanCurve";
        outOfBounds     clamp;
        direction       in;
        p0              uniform 0;
        value           uniform 0;
}

outlet
{
        type            fanPressure;
        fileName        "fanCurve";
        outOfBounds     clamp;
        direction       out;
        p0              uniform 0;
        value           uniform 0;
}
```

## See also
Foam::fanFvPatchField
Foam::totalPressureFvPatchScalarField
Foam::interpolationTable

## SourceFiles
   fanPressureFvPatchScalarField.C

