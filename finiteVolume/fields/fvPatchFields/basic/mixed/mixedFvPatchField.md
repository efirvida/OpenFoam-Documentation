# mixedFvPatchField 
## Class
Foam::mixedFvPatchField

## Group
grpGenericBoundaryConditions

## Description
This boundary condition provides a base class for 'mixed' type boundary
conditions, i.e. conditions that mix fixed value and patch-normal gradient
conditions.

The respective contributions from each is determined by a weight field:

        \f[
            x_p = w x_p + (1-w) \left(x_c + \frac{\nabla_\perp x}{\Delta}\right)
        \f]

where
\vartable
        x_p   | patch values
        x_c   | patch internal cell values
        w     | weight field
        \Delta| inverse distance from face centre to internal cell centre
        w     | weighting (0-1)
\endvartable


## Usage

        Property     | Description             | Required    | Default value
        valueFraction | weight field           | yes         |
        refValue     | fixed value             | yes         |
        refGrad      | patch normal gradient   | yes         |


## Note
This condition is not usually applied directly; instead, use a derived
mixed condition such as \c inletOutlet

## See also
Foam::inletOutletFvPatchField

## SourceFiles
mixedFvPatchField.C

