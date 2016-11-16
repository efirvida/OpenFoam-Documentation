# fixedEnergyFvPatchScalarField 
## Class
Foam::fixedEnergyFvPatchScalarField

## Group
grpThermoBoundaryConditions

## Description
This boundary condition provides a fixed condition for internal energy

## Usage
Example of the boundary condition specification:
```
<patchName>
{
        type            fixedEnergy;
        value           uniform 100;
}
```

## See also
Foam::fixedValueFvPatchField

## SourceFiles
fixedEnergyFvPatchScalarField.C

