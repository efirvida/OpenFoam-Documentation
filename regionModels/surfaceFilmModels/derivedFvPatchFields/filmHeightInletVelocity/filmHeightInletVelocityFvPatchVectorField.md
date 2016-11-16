# filmHeightInletVelocityFvPatchVectorField 
## Class
Foam::filmHeightInletVelocityFvPatchVectorField

## Group
grpSurfaceFilmBoundaryConditions

## Description
This boundary condition is designed to be used in conjunction with
surface film modelling.  It provides a velocity inlet boundary condition
for patches where the film height is specified.  The inflow velocity is
obtained from the flux with a direction normal to the patch faces using:

\f[
        U_p = \frac{n \phi}{\rho |Sf| \delta}
\f]

where
\vartable
        U_p    | patch velocity [m/s]
        n      | patch normal vector
        \phi   | mass flux [kg/s]
        \rho   | density [kg/m3]
        Sf     | patch face area vectors [m2]
        \delta | film height [m]
\endvartable

## Usage

        Property     | Description             | Required    | Default value
        phi          | Flux field name         | no          | phi
        rho          | density field name      | no          | rho
        deltaf       | height field name       | no          | deltaf


Example of the boundary condition specification:
```
<patchName>
{
        type            filmHeightInletVelocity;
        phi             phi;
        rho             rho;
        deltaf          deltaf;
        value           uniform (0 0 0); // initial velocity / [m/s]
}
```

## See also
Foam::fixedValueFvPatchField

## SourceFiles
filmHeightInletVelocityFvPatchVectorField.C

