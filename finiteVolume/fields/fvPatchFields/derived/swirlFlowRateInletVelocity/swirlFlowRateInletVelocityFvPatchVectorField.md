# swirlFlowRateInletVelocityFvPatchVectorField 
## Class
Foam::swirlFlowRateInletVelocityFvPatchVectorField

## Group
grpInletBoundaryConditions

## Description
This boundary condition provides a volumetric- OR mass-flow normal vector
boundary condition by its magnitude as an integral over its area with a
swirl component determined by the angular speed, given in revolutions per
minute (RPM)

The basis of the patch (volumetric or mass) is determined by the
dimensions of the flux, phi. The current density is used to correct the
velocity when applying the mass basis.

## Usage

        Property     | Description             | Required    | Default value
        phi          | flux field name         | no          | phi
        rho          | density field name      | no          | rho
        flowRate     | flow rate profile       | yes         |
        rpm          | rotational speed profile | yes        |


Example of the boundary condition specification:
```
<patchName>
{
        type            swirlFlowRateInletVelocity;
        flowRate        constant 0.2;
        rpm             constant 100;
}
```

## Note
- the \c flowRate and \c rpm entries are Function1 types, able to describe
      time varying functions.  The example above gives the usage for supplying
      constant values.
- the value is positive into the domain

## See also
Foam::fixedValueFvPatchField
Foam::Function1Types

## SourceFiles
swirlFlowRateInletVelocityFvPatchVectorField.C

