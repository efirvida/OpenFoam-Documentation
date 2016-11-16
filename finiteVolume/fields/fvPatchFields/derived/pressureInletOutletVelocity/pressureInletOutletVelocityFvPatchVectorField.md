# pressureInletOutletVelocityFvPatchVectorField 
## Class
Foam::pressureInletOutletVelocityFvPatchVectorField

## Group
grpInletletBoundaryConditions grpOutletBoundaryConditions

## Description
This velocity inlet/outlet boundary condition is applied to pressure
boundaries where the pressure is specified.  A zero-gradient condition is
applied for outflow (as defined by the flux); for inflow, the velocity is
obtained from the patch-face normal component of the internal-cell value.

The tangential patch velocity can be optionally specified.

## Usage

        Property     | Description             | Required    | Default value
        phi          | flux field name         | no          | phi
        tangentialVelocity | tangential velocity field | no  |


Example of the boundary condition specification:
```
<patchName>
{
        type            pressureInletOutletVelocity;
        phi             phi;
        tangentialVelocity uniform (0 0 0);
        value           uniform 0;
}
```

## Note
Sign conventions:
- positive flux (out of domain): apply zero-gradient condition
- negative flux (into of domain): derive from the flux in the patch-normal
      direction

## SourceFiles
pressureInletOutletVelocityFvPatchVectorField.C

