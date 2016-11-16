# explicitPorositySource 
## Class
Foam::fv::explicitPorositySource

## Description
Explicit porosity source

## Usage
Example usage, here employing the Darcy-Forchheimer model:
```
explicitPorositySourceCoeffs
{
        type            DarcyForchheimer;

        DarcyForchheimerCoeffs
        {
            d   d [0 -2 0 0 0 0 0] (5e7 -1000 -1000);
            f   f [0 -1 0 0 0 0 0] (0 0 0);

            coordinateSystem
            {
                type    cartesian;
                origin  (0 0 0);
                coordinateRotation
                {
                    type    axesRotation;
                    e1  (0.70710678 0.70710678 0);
                    e2  (0 0 1);
                }
            }
        }
}
```

## Note:
The porous region must be selected as a cellZone.

## SourceFiles
explicitPorositySource.C

