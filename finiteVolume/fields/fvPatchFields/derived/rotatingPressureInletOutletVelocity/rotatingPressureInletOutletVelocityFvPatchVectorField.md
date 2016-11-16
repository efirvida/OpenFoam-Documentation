# rotatingPressureInletOutletVelocityFvPatchVectorField 
## Class
Foam::rotatingPressureInletOutletVelocityFvPatchVectorField

## Group
grpInletBoundaryConditions grpOutletBoundaryConditions

## Description
This velocity inlet/outlet boundary condition is applied to patches in a
rotating frame where the pressure is specified.  A zero-gradient is applied
for outflow (as defined by the flux); for inflow, the velocity is obtained
from the flux with a direction normal to the patch faces.

## Usage

        Property     | Description             | Required    | Default value
        phi          | flux field name         | no          | phi
        tangentialVelocity | tangential velocity field | no  |
        omega        | angular velocty of the frame [rad/s] | yes    |


Example of the boundary condition specification:
```
<patchName>
{
        type            rotatingPressureInletOutletVelocity;
        phi             phi;
        tangentialVelocity uniform (0 0 0);
        omega           100;
}
```

The \c omega entry is a Function1 type, able to describe time varying
functions.

## Note
Sign conventions:
- positive flux (out of domain): apply zero-gradient condition
- negative flux (into of domain): derive from the flux in the patch-normal
      direction

## See also
Foam::pressureInletOutletVelocityFvPatchVectorField
Foam::Function1Types

## SourceFiles
rotatingPressureInletOutletVelocityFvPatchVectorField.C

