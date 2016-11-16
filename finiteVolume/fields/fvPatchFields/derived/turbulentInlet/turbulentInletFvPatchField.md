# turbulentInletFvPatchField 
## Class
Foam::turbulentInletFvPatchField

## Group
grpInletBoundaryConditions

## Description
This boundary condition generates a fluctuating inlet condition by adding
a random component to a reference (mean) field.

\f[
        x_p = (1 - \alpha) x_p^{n-1} + \alpha (x_{ref} + s C_{RMS} x_{ref})
\f]

where

\vartable
        x_p     | patch values
        x_{ref} | reference patch values
        n       | time level
        \alpha  | fraction of new random component added to previous time value
        C_{RMS} | RMS coefficient
        s       | fluctuation scale
\endvartable

## Usage

        Property     | Description             | Required    | Default value
        fluctuationScale | RMS fluctuation scale (fraction of mean) | yes |
        referenceField | reference (mean) field | yes        |
        alpha | fraction of new random component added to previous| no| 0.1


Example of the boundary condition specification:
```
<patchName>
{
        type            turbulentInlet;
        fluctuationScale 0.1;
        referenceField  uniform 10;
        alpha           0.1;
}
```

## See also
Foam::fixedValueFvPatchField

## SourceFiles
turbulentInletFvPatchField.C

