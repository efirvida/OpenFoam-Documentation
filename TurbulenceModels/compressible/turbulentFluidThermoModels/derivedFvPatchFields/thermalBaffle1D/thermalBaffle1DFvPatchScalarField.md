# thermalBaffle1DFvPatchScalarField 
## Class
Foam::compressible::thermalBaffle1DFvPatchScalarField

## Group
grpThermoBoundaryConditions

## Description
This BC solves a steady 1D thermal baffle.

The solid properties are specify as dictionary. Optionaly radiative heat
flux (Qr) can be incorporated into the balance. Some under-relaxation might
be needed on Qr.  Baffle and solid properties need to be specified on the
master side of the baffle.

## Usage
Example of the boundary condition specification using constant
solid thermo :

```
<masterPatchName>
{
        type   compressible::thermalBaffle1D<hConstSolidThermoPhysics>;
        samplePatch     <slavePatchName>;

        thickness       uniform 0.005;  // thickness [m]
        Qs              uniform 100;    // heat flux [W/m2]

        Qr              none;
        relaxation      1;

        // Solid thermo
        specie
        {
            nMoles          1;
            molWeight       20;
        }
        transport
        {
            kappa           1;
        }
        thermodynamics
        {
            Hf              0;
            Cp              10;
        }
        equationOfState
        {
            rho             10;
        }

        value               uniform 300;
}

<slavePatchName>
{
        type   compressible::thermalBaffle1D<hConstSolidThermoPhysics>;
        samplePatch     <masterPatchName>;

        Qr              none;
        relaxation      1;
}
```

## SourceFiles
thermalBaffle1DFvPatchScalarField.C

