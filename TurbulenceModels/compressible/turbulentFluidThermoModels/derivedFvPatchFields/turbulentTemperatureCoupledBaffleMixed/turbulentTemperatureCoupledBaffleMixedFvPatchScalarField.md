# turbulentTemperatureCoupledBaffleMixedFvPatchScalarField 
## Class
Foam::compressible::
        turbulentTemperatureCoupledBaffleMixedFvPatchScalarField

## Description
Mixed boundary condition for temperature, to be used for heat-transfer
on back-to-back baffles. Optional thin thermal layer resistances can be
specified through thicknessLayers and kappaLayers entries.

The thermal conductivity, \c kappa, can either be retrieved from the
mesh database using the \c lookup option, or from a \c solidThermo
or \c fluidThermo thermophysical package.

Specifies gradient and temperature such that the equations are the same
on both sides:
      - refGradient = zero gradient
      - refValue = neighbour value
      - mixFraction = nbrKDelta / (nbrKDelta + myKDelta())

where KDelta is heat-transfer coefficient K * deltaCoeffs

## Usage

        Property     | Description             | Required    | Default value
        kappa        | thermal conductivity option | yes     |
        kappaName    | name of thermal conductivity field | no  |
        Tnbr         | name of the field    | no | T
        thicknessLayers | list of thicknesses per layer [m] | no |
        kappaLayers  | list of thermal conductivites per layer [W/m/K] | no |


Example of the boundary condition specification:
```
<patchName>
{
        type            compressible::turbulentTemperatureCoupledBaffleMixed;
        Tnbr            T;
        kappa           lookup;
        kappaName       kappa;
        thicknessLayers (0.1 0.2 0.3 0.4);
        kappaLayers     (1 2 3 4);
        value           uniform 300;
}
```

Needs to be on underlying mapped(Wall)FvPatch.

Note:
      - \c kappa and \c kappaName are inherited from temperatureCoupledBase.


## See also
Foam::temperatureCoupledBase

## SourceFiles
turbulentTemperatureCoupledBaffleMixedFvPatchScalarField.C

