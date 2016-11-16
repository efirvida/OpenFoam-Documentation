# FixedValueConstraint.T 
## Class
Foam::fv::FixedValueConstraint

## Description
Constrain the field values within a specified region.

## Usage
For example to set the turbulence properties within a porous region:
```
porosityTurbulence
{
        type            scalarFixedValueConstraint;
        active          yes;

        scalarFixedValueConstraintCoeffs
        {
            selectionMode   cellZone;
            cellZone        porosity;
            fieldValues
            {
                k           1;
                epsilon     150;
            }
        }
}
```

## See also
Foam::fvOption

## SourceFiles
FixedValueConstraint.C
fixedValueConstraints.C

