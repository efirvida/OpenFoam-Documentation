# fixedMeanFvPatchField 
## Class
Foam::fixedMeanFvPatchField

## Group
grpInletBoundaryConditions

## Description
This boundary condition extrapolates field to the patch using the near-cell
values and adjusts the distribution to match the specified, optionally
time-varying, mean value.

## Usage

        Property     | Description             | Required    | Default value
        meanValue    | mean value Function1    | yes         |


Example of the boundary condition specification:
```
<patchName>
{
        type            fixedMean;
        meanValue       1.0;
}
```

## See also
Foam::fixedValueFvPatchField
Foam::Function1Types

## SourceFiles
fixedMeanFvPatchField.C

