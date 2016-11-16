# fixedFluxExtrapolatedPressureFvPatchScalarField 
## Class
Foam::fixedFluxExtrapolatedPressureFvPatchScalarField

## Group
grpInletBoundaryConditions grpWallBoundaryConditions

## Description
This boundary condition sets the pressure gradient to the provided value
such that the flux on the boundary is that specified by the velocity
boundary condition.

Example of the boundary condition specification:
```
<patchName>
{
        type            fixedFluxExtrapolatedPressure;
}
```

## See also
Foam::fixedGradientFvPatchField

## SourceFiles
fixedFluxExtrapolatedPressureFvPatchScalarField.C

