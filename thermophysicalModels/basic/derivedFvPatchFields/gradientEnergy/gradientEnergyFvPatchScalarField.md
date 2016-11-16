# gradientEnergyFvPatchScalarField 
## Class
Foam::gradientEnergyFvPatchScalarField

## Group
grpThermoBoundaryConditions

## Description
This boundary condition provides a gradient condition for internal energy,
where the gradient is calculated using:

        \f[
            \nabla(e_p) = \nabla_\perp C_p(p, T) + \frac{e_p - e_c}{\Delta}
        \f]

where
\vartable
        e_p     | energy at patch faces [J]
        e_c     | energy at patch internal cells [J]
        p       | pressure [bar]
        T       | temperature [K]
        C_p     | specific heat [J/kg/K]
        \Delta  | distance between patch face and internal cell centres [m]
\endvartable

## Usage
Example of the boundary condition specification:
```
<patchName>
{
        type            gradientEnergy;
        gradient        uniform 10;
}
```

## See also
Foam::fixedGradientFvPatchField

## SourceFiles
gradientEnergyFvPatchScalarField.C

