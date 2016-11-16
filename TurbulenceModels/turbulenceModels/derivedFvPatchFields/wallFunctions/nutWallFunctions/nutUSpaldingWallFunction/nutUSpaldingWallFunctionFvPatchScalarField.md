# nutUSpaldingWallFunctionFvPatchScalarField 
## Class
Foam::nutUSpaldingWallFunctionFvPatchScalarField

## Group
grpWallFunctions

## Description
This boundary condition provides a turbulent kinematic viscosity condition
when using wall functions for rough walls, based on velocity,  using
Spalding's law to give a continuous nut profile to the wall (y+ = 0)

        \f[
            y^+ = u^+ + \frac{1}{E} \left[exp(\kappa u^+) - 1 - \kappa u^+\,
                - 0.5 (\kappa u^+)^2 - \frac{1}{6} (\kappa u^+)^3\right]
        \f]

where
\vartable
        y^+     | non-dimensional position
        u^+     | non-dimensional velocity
        \kappa  | Von Karman constant
\endvartable


## Usage
Example of the boundary condition specification:
```
<patchName>
{
        type            nutUSpaldingWallFunction;
}
```

## See also
Foam::nutWallFunctionFvPatchScalarField

## SourceFiles
nutUSpaldingWallFunctionFvPatchScalarField.C

