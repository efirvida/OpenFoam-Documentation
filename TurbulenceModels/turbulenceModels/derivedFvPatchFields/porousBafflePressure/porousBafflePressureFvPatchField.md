# porousBafflePressureFvPatchField 
## Class
Foam::porousBafflePressureFvPatchField

## Group
grpCoupledBoundaryConditions

## Description
This boundary condition provides a jump condition, using the \c cyclic
condition as a base.

The porous baffle introduces a pressure jump defined by:

        \f[
            \Delta p = -(D \mu U + 0.5 I \rho |U|^2 )L
        \f]

where

\vartable
        p      | pressure [Pa]
        \rho   | density [kg/m3]
        \mu    | laminar viscosity [Pa s]
        D      | Darcy coefficient
        I      | inertial coefficient
        L      | porous media length in the flow direction
\endvartable


## Usage

        Property     | Description             | Required    | Default value
        patchType    | underlying patch type should be \c cyclic| yes |
        phi          | flux field name         | no          | phi
        rho          | density field name      | no          | rho
        D            | Darcy coefficient       | yes         |
        I            | inertial coefficient    | yes         |
        length       | porous media length in the flow direction | yes |


Example of the boundary condition specification:
```
<patchName>
{
        type            porousBafflePressure;
        patchType       cyclic;
        jump            uniform 0;
        D               0.001;
        I               1000000;
        length          0.1;
        value           uniform 0;
}
```

## Note
     The underlying \c patchType should be set to \c cyclic

## SourceFiles
porousBafflePressureFvPatchField.C

