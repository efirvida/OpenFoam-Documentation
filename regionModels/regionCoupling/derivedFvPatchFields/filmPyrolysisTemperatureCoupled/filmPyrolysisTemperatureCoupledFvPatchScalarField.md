# filmPyrolysisTemperatureCoupledFvPatchScalarField 
## Class
Foam::filmPyrolysisTemperatureCoupledFvPatchScalarField

## Description
This boundary condition is designed to be used in conjunction with surface
film and pyrolysis modelling.  It provides a temperature boundary condition
for patches on the primary region based on whether the patch is seen to
be 'wet', retrieved from the film alpha field.

- if the patch is wet, the temperature is set using the film temperature
- otherwise, it is set using pyrolysis temperature

Example of the boundary condition specification:
```
<patchName>
{
        type            filmPyrolysisTemperatureCoupled;
        phi             phi;      // name of flux field (default = phi)
        rho             rho;      // name of density field (default = rho)
        deltaWet        1e-4;     // threshold height for 'wet' film
        value           uniform   300; // initial temperature / [K]
}
```

## SourceFiles
filmPyrolysisTemperatureCoupledFvPatchScalarField.C

