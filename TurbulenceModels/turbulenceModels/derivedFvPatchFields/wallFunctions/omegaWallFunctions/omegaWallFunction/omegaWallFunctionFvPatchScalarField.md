# omegaWallFunctionFvPatchScalarField 
## Class
Foam::omegaWallFunctionFvPatchScalarField

## Group
grpWallFunctions

## Description
This boundary condition provides a wall function constraint on turbulnce
specific dissipation, omega.  The values are computed using:

        \f[
            \omega = sqrt(\omega_{vis}^2 + \omega_{log}^2)
        \f]

where

\vartable
        \omega_{vis} | omega in viscous region
        \omega_{log} | omega in logarithmic region
\endvartable

Model described by Eq.(15) of:
```
        Menter, F., Esch, T.
        "Elements of Industrial Heat Transfer Prediction"
        16th Brazilian Congress of Mechanical Engineering (COBEM),
        Nov. 2001
```

## Usage

        Property     | Description             | Required    | Default value
        Cmu          | model coefficient       | no          | 0.09
        kappa        | Von Karman constant     | no          | 0.41
        E            | model coefficient       | no          | 9.8
        beta1        | model coefficient       | no          | 0.075


Example of the boundary condition specification:
```
<patchName>
{
        type            omegaWallFunction;
}
```

## SourceFiles
omegaWallFunctionFvPatchScalarField.C

