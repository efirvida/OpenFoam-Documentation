# pressureInletVelocityFvPatchVectorField 
## Class
Foam::pressureInletVelocityFvPatchVectorField

## Group
grpInletBoundaryConditions

## Description
This velocity inlet boundary condition is applied to patches where the
pressure is specified.  The inflow velocity is obtained from the flux with
a direction normal to the patch faces.

## Usage
Example of the boundary condition specification:
```
<patchName>
{
        type            pressureInletVelocity;
        phi             phi;
        rho             rho;
        value           uniform 0;
}
```

## Note
If reverse flow is possible or expected use
the pressureInletOutletVelocityFvPatchVectorField condition instead.

## See also
Foam::fixedValueFvPatchField
Foam::pressureInletOutletVelocityFvPatchVectorField

## SourceFiles
pressureInletVelocityFvPatchVectorField.C

