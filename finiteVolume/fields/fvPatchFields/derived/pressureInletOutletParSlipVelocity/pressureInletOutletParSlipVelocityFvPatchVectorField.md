# pressureInletOutletParSlipVelocityFvPatchVectorField 
## Class
Foam::pressureInletOutletParSlipVelocityFvPatchVectorField

## Group
grpInletBoundaryConditions grpOutletBoundaryConditions

## Description
This velocity inlet/outlet boundary condition for pressure boundary where
the pressure is specified.  A zero-gradient is applied for outflow (as
defined by the flux); for inflow, the velocity is obtained from the flux
with the specified inlet direction.

A slip condition is applied tangential to the patch.

## Usage

        Property     | Description             | Required    | Default value
        phi          | flux field name         | no          | phi
        rho          | density field name      | no          | rho


Example of the boundary condition specification:
```
<patchName>
{
        type            pressureInletOutletParSlipVelocity;
        value           uniform 0;
}
```

## Note
Sign conventions:
- positive flux (out of domain): apply zero-gradient condition
- negative flux (into of domain): derive from the flux with specified
      direction

## See also
Foam::mixedFvPatchVectorField
Foam::pressureDirectedInletOutletVelocityFvPatchVectorField

## SourceFiles
pressureInletOutletParSlipVelocityFvPatchVectorField.C

