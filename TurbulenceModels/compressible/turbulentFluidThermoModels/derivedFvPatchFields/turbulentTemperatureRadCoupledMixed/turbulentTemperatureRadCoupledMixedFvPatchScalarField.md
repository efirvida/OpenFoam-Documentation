# turbulentTemperatureRadCoupledMixedFvPatchScalarField 
## Class
Foam::compressible::
        turbulentTemperatureRadCoupledMixedFvPatchScalarField

## Description
Mixed boundary condition for temperature and radiation heat transfer
to be used for in multiregion cases. Optional thin thermal layer
resistances can be specified through thicknessLayers and kappaLayers
entries.

The thermal conductivity, \c kappa, can either be retrieved from the
mesh database using the \c lookup option, or from a \c solidThermo
or \c fluidThermo thermophysical package.

## Usage

        Property     | Description             | Required    | Default value
        kappa        | thermal conductivity option | yes     |
        kappaName    | name of thermal conductivity field | no  |
        Tnbr         | name of the field    | no | T
        QrNbr      | name of the radiative flux in the nbr region | no | none
        Qr         | name of the radiative flux in this region | no | none
        thicknessLayers | list of thicknesses per layer [m] | no |
        kappaLayers  | list of thermal conductivites per layer [W/m/K] | no |


Example of the boundary condition specification:
```
<patchName>
{
        type            compressible::turbulentTemperatureRadCoupledMixed;
        Tnbr            T;
        kappa           lookup;
        kappaName       kappa;
        QrNbr           Qr; // or none. Name of Qr field on neighbour region
        Qr              Qr; // or none. Name of Qr field on local region
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
turbulentTemperatureRadCoupledMixedFvPatchScalarField.C

