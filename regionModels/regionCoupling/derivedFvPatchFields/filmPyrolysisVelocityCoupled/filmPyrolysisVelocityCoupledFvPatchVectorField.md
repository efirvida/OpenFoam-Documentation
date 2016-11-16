# filmPyrolysisVelocityCoupledFvPatchVectorField 
## Class
Foam::filmPyrolysisVelocityCoupledFvPatchVectorField

## Description
This boundary condition is designed to be used in conjunction with surface
film and pyrolysis modelling.

It provides a velocity boundary condition for patches on the primary region
based on whether the patch is seen to be 'wet', retrieved from the film
alpha field.
      - if the patch is wet, the velocity is set using the film velocity
      - otherwise, it is set using pyrolysis out-gassing velocity

Example of the boundary condition specification:
```
<patchName>
{
        type            filmPyrolysisVelocityCoupled;
        phi             phi;      // name of flux field (default = phi)
        rho             rho;      // name of density field (default = rho)
        deltaWet        1e-4;     // threshold height for 'wet' film
        value           uniform   (0 0 0); // initial velocity / [m/s]
}
```

## SourceFiles
filmPyrolysisVelocityCoupledFvPatchVectorField.C

