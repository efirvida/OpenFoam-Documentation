# epsilonWallFunctionFvPatchScalarField 
## Class
Foam::epsilonWallFunctionFvPatchScalarField

## Group
grpWallFunctions

## Description
This boundary condition provides a turbulence dissipation wall function
condition for high Reynolds number, turbulent flow cases.

The condition can be applied to wall boundaries, whereby it
- calculates \c epsilon and \c G
- inserts near wall epsilon values directly into the epsilon equation
        to act as a constraint

where

\vartable
        epsilon | turblence dissipation field
        G       | turblence generation field
\endvartable

## Usage

        Property     | Description             | Required    | Default value
        Cmu          | model coefficient       | no          | 0.09
        kappa        | Von Karman constant     | no          | 0.41
        E            | model coefficient       | no          | 9.8


Example of the boundary condition specification:
```
<patchName>
{
        type            epsilonWallFunction;
}
```

## See also
Foam::fixedInternalValueFvPatchField

## SourceFiles
epsilonWallFunctionFvPatchScalarField.C

