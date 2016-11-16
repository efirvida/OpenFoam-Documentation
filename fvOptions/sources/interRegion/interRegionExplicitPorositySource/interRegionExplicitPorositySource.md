# interRegionExplicitPorositySource 
## Class
Foam::fv::interRegionExplicitPorositySource

## Description
Inter-region explicit porosity source.

Sources described by, for example using the DarcyForchheimer model:

```
interRegionExplicitPorositySourceCoeffs
{
        type            DarcyForchheimer;
        DarcyForchheimerCoeffs
        {
            d   d [0 -2 0 0 0 0 0] (5e7 -1000 -1000);
            f   f [0 -1 0 0 0 0 0] (0 0 0);

            coordinateSystem
            {
                e1  (0.70710678 0.70710678 0);
                e2  (0 0 1);
            }
        }
}
```

## Note
The porous region must be selected as a cellZone.

## SourceFiles
interRegionExplicitPorositySource.C

