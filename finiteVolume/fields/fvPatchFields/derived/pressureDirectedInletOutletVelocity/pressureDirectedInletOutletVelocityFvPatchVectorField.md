# pressureDirectedInletOutletVelocityFvPatchVectorField 
## Class
Foam::pressureDirectedInletOutletVelocityFvPatchVectorField

## Group
grpInletBoundaryConditions grpOutletBoundaryConditions

## Description
This velocity inlet/outlet boundary condition is applied to pressure
boundaries where the pressure is specified.  A zero-gradient condtion is
applied for outflow (as defined by the flux); for inflow, the velocity
is obtained from the flux with the specified inlet direction.

## Usage

        Property     | Description             | Required    | Default value
        phi          | flux field name         | no          | phi
        rho          | density field name      | no          | rho
        inletDirection | inlet direction per patch face | yes |


Example of the boundary condition specification:
```
<patchName>
{
        type            pressureDirectedInletOutletVelocity;
        phi             phi;
        rho             rho;
        inletDirection  uniform (1 0 0);
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

## SourceFiles
pressureDirectedInletOutletVelocityFvPatchVectorField.C

