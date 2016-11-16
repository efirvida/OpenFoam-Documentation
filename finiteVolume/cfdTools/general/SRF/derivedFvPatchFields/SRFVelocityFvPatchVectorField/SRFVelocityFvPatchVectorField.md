# SRFVelocityFvPatchVectorField 
## Class
Foam::SRFVelocityFvPatchVectorField

## Group
grpInletBoundaryConditions grpWallBoundaryConditions

## Description
Velocity condition to be used in conjunction with the single
rotating frame (SRF) model (see: SRFModel class)

Given the free stream velocity in the absolute frame, the condition
applies the appropriate rotation transformation in time and space to
determine the local velocity.

The optional \c relative flag switches the behaviour of the patch
such that:

        - relative = yes: inlet velocity applied 'as is':

        \f[
            U_p = U_{in}
        \f]

        - relative = no : SRF velocity is subtracted from the inlet velocity:

        \f[
            U_p = U_{in} - U_{p,srf}
        \f]

where
\vartable
        U_p     = patch velocity [m/s]
        U_{in}  = user-specified inlet velocity
        U_{p,srf} = SRF velocity
\endvartable


## Usage

        Property     | Description             | Required    | Default value
        inletValue   | inlet velocity          | yes         |
        relative     | inletValue relative motion to the SRF? | yes     |


Example of the boundary condition specification:
```
<patchName>
{
        type            SRFVelocity;
        inletValue      uniform (0 0 0);
        relative        yes;
        value           uniform (0 0 0);    // initial value
}
```

## See also
Foam::fixedValueFvPatchField

## SourceFiles
SRFVelocityFvPatchVectorField.C

