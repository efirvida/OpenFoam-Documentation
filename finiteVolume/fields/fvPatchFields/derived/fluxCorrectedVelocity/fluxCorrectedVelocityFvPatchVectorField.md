# fluxCorrectedVelocityFvPatchVectorField 
## Class
Foam::fluxCorrectedVelocityFvPatchVectorField

## Group
grpOutletBoundaryConditions

## Description
This boundary condition provides a velocity outlet boundary condition for
patches where the pressure is specified.  The outflow velocity is obtained
by "zeroGradient" and then corrected from the flux:

        \f[
            U_p = U_c - n (n \cdot U_c) + \frac{n \phi_p}{|S_f|}
        \f]

where

\vartable
        U_p | velocity at the patch [m/s]
        U_c | velocity in cells adjacent to the patch [m/s]
        n   | patch normal vectors
        \phi_p | flux at the patch [m3/s or kg/s]
        S_f | patch face area vectors [m2]
\endvartable

where


        Property     | Description             | Required    | Default value
        phi          | name of flux field      | no          | phi
        rho          | name of density field   | no          | rho


Example of the boundary condition specification:
```
<patchName>
{
        type            fluxCorrectedVelocity;
        phi             phi;
        rho             rho;
}
```

## Note
If reverse flow is possible or expected use the
pressureInletOutletVelocity condition instead.

## See also
Foam::zeroGradientFvPatchField
Foam::pressureInletOutletVelocityFvPatchVectorField

## SourceFiles
fluxCorrectedVelocityFvPatchVectorField.C

