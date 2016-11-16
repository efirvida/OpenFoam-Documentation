# syringePressureFvPatchScalarField 
## Class
Foam::syringePressureFvPatchScalarField

## Group
grpInletBoundaryConditions

## Description
This boundary condition provides a pressure condition, obtained from a
zero-D model of the cylinder of a syringe.

The syringe cylinder is defined by its initial volume, piston area and
velocity profile specified by regions of constant acceleration, speed
and deceleration.  The gas in the cylinder is described by its initial
pressure and compressibility which is assumed constant, i.e. isothermal
expansion/compression.

## Usage

        Property     | Description             | Required    | Default value
        Ap           | syringe piston area [m2] | yes        |
        Sp           | syringe piston speed [m/s] | yes      |
        VsI          | initial syringe volume [m3] | yes     |
        tas          | start of piston acceleration [s] | yes |
        tae          | end of piston acceleration [s] | yes  |
        tds          | start of piston deceleration [s] | yes |
        tde          | end of piston deceleration [s] | yes  |
        psI          | initial syringe pressure [Pa] | yes   |
        psi          | gas compressibility [m2/s2] | yes     |
        ams          | added (or removed) gas mass [kg] | yes |


Example of the BC specification:
```
<patchName>
{
        type            syringePressure;
        Ap              1.388e-6;
        Sp              0.01;
        VsI             1.388e-8;
        tas             0.001;
        tae             0.002;
        tds             0.005;
        tde             0.006;
        psI             1e5;
        psi             1e-5;
        ams             0;
        value           uniform 0;
}
```

## See also
Foam::fixedValueFvPatchField

## SourceFiles
syringePressureFvPatchScalarField.C

