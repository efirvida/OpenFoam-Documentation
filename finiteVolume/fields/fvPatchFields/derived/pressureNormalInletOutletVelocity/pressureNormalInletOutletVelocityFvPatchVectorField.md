# pressureNormalInletOutletVelocityFvPatchVectorField 
## Class
Foam::pressureNormalInletOutletVelocityFvPatchVectorField

## Group
grpInletBoundaryConditions grpOutletBoundaryConditions

## Description
This velocity inlet/outlet boundary condition is applied to patches where
the pressure is specified.  A zero-gradient condition is applied for
outflow (as defined by the flux); for inflow, the velocity is obtained from
the flux with a direction normal to the patch faces.

## Usage

        Property     | Description             | Required    | Default value
        phi          | flux field name         | no          | phi
        rho          | density field name      | no          | rho


Example of the boundary condition specification:
```
<patchName>
{
        type            pressureNormalInletOutletVelocity;
        phi             phi;
        rho             rho;
        value           uniform 0;
}
```

## Note
Sign conventions:
- positive flux (out of domain): apply zero-gradient condition
- negative flux (into of domain): derive from the flux and patch-normal
      direction

## See also
Foam::mixedFvPatchVectorField

## SourceFiles
pressureNormalInletOutletVelocityFvPatchVectorField.C

