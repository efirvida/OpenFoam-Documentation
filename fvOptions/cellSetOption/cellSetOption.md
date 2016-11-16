# cellSetOption 
## Class
Foam::fv::cellSetOption

## Description
Cell-set options abtract base class.  Provides a base set of controls,
e.g.:
```
        type            scalarExplicitSource    // Source type
        active          on;                     // on/off switch

        scalarExplicitSourceCoeffs
        {
            timeStart       0.0;        // Start time
            duration        1000.0;     // Duration
            selectionMode   cellSet;    // cellSet, points, cellZone
            .
            .
            .
        }
```

## Note
Source/sink options are to be added to the equation R.H.S.

## SourceFiles
cellSetOption.C
cellSetOptionIO.C

