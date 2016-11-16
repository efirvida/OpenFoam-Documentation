# thermalBaffleFvPatchScalarField 
## Class
Foam::compressible::thermalBaffleFvPatchScalarField

## Group
grpThermoBoundaryConditions

## Description
This boundary condition provides a coupled temperature condition between
multiple mesh regions.

The regions are generally referred to as the:
      - primary region,
      - and baffle region.

The primary region creates the baffle region and evolves its energy
equation either:
      - 1-D, normal to each patch face
      - 2-D, normal and tangential components

The thermodynamic properties of the baffle material are specified via
dictionary entries on the master patch.

## Usage
Example of the boundary condition specification:
```
<masterPatchName>
{
        type                compressible::thermalBaffle;

        // Underlaying coupled boundary condition
        Tnbr               T;
        kappa              fluidThermo; // or solidThermo
        KappaName          none;
        QrNbr              Qr;//or none.Name of Qr field on neighbourregion
        Qr                 none;// or none.Name of Qr field on localregion
        value              uniform 300;

        // Baffle region name
        regionName          baffleRegion;
        active              yes;

        // Solid thermo in solid region
        thermoType
        {
            type            heSolidThermo;
            mixture         pureMixture;
            transport       constIso;
            thermo          hConst;
            equationOfState rhoConst;
            specie          specie;
            energy          sensibleEnthalpy;
        }

        mixture
        {
            specie
            {
                nMoles          1;
                molWeight       20;
            }
            transport
            {
                kappa           0.01;
            }
            thermodynamics
            {
                Hf              0;
                Cp              15;
            }
            density
            {
                rho             80;
            }
        }

        radiation
        {
            radiationModel  opaqueSolid;
            absorptionEmissionModel none;
            scatterModel    none;
        }

        // Extrude model for new region

        extrudeModel        linearNormal;
        nLayers             50;
        expansionRatio      1;
        columnCells         false; //3D or 1D
        linearNormalCoeffs
        {
            thickness           0.02;
        }

}
```

Slave patch on primary region:
```
<slavePatchName>
{
        type                compressible::thermalBaffle;
        kappa               fluidThermo;
        kappaName           none;
        value               uniform 300;
```

Patches on baffle region:
```
bottom
{
        type                compressible::thermalBaffle;
        kappa               solidThermo;
        kappaName           none;
        value               uniform 300;
}

top
{
        type                compressible::thermalBaffle;
        kappa               solidThermo;
        kappaName           none;
        value               uniform 300;
}
```

## See also
Foam::compressible::turbulentTemperatureCoupledBaffleMixedFvPatchScalarField
Foam::regionModels::thermalBaffleModels::thermalBaffleModel

## SourceFiles
thermalBaffleFvPatchScalarField.C

