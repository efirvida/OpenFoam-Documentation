# advectiveFvPatchField 
## Class
Foam::advectiveFvPatchField

## Group
grpOutletBoundaryConditions

## Description
This boundary condition provides an advective outflow condition, based on
solving DDt(psi, U) = 0 at the boundary.

The standard (Euler, backward, CrankNicolson, localEuler) time schemes are
supported.  Additionally an optional mechanism to relax the value at
the boundary to a specified far-field value is provided which is
switched on by specifying the relaxation length-scale \c lInf and the
far-field value \c fieldInf.

The flow/wave speed at the outlet is provided by the virtual function
advectionSpeed() the default implementation of which requires the name of
the flux field \c (phi) and optionally the density \c (rho) if the
mass-flux rather than the volumetric-flux is given.

The flow/wave speed at the outlet can be changed by deriving a specialised
BC from this class and over-riding advectionSpeed()  e.g. in
waveTransmissiveFvPatchField the advectionSpeed() calculates and returns
the flow-speed plus the acoustic wave speed creating an acoustic wave
transmissive boundary condition.

## Usage

        Property     | Description             | Required    | Default value
        phi          | flux field name         | no          | phi
        rho          | density field name      | no          | rho
        fieldInf     | value of field beyond patch | no      |
        lInf         | distance beyond patch for \c fieldInf | no |


Example of the boundary condition specification:
```
<patchName>
{
        type            advective;
        phi             phi;
}
```

## Note
If \c lInf is specified, \c fieldInf will be required; \c rho is only
required in the case of a mass-based flux.

## SourceFiles
advectiveFvPatchField.C

