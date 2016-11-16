# SRFFreestreamVelocityFvPatchVectorField 
## Class
Foam::SRFVelocityFvPatchVectorField

## Description
Freestream velocity condition to be used in conjunction with the single
rotating frame (SRF) model (see: SRFModel class)

Given the free stream velocity in the absolute frame, the condition
applies the appropriate rotation transformation in time and space to
determine the local velocity using:

        \f[
            U_p = cos(\theta)*U_{Inf} + sin(theta) (n^UInf) - U_{p,srf}
        \f]

where
\vartable
        U_p     = patch velocity [m/s]
        U_{Inf} = free stream velocity in the absolute frame [m/s]
        theta   = swept angle [rad]
        n       = axis direction of the SRF
        U_{p,srf} = SRF velocity of the patch
\endvartable


## Usage

        Property        | Description               | Required | Default value
        UInf            | freestream velocity       | yes      |
        relative        | UInf relative to the SRF? | no       |


Example of the boundary condition specification:
```
<patchName>
{
        type            SRFFreestreamVelocity;
        UInf            uniform (0 0 0);
        relative        no;
        value           uniform (0 0 0);    // initial value
}
```

## See also
Foam::freestreamFvPatchField
Foam::SRFVelocityFvPatchVectorField

## SourceFiles
SRFFreestreamVelocityFvPatchVectorField.C

