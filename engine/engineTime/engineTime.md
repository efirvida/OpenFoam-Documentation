# engineTime 
## Class
Foam::engineTime

## Description
Manage time in terms of engine RPM and crank-angle.

When engineTime is in effect, the userTime is reported in degrees
crank-angle instead of in seconds. The RPM to be used is specified in
\c constant/engineGeometry. If only a time conversion is required,
the geometric engine parameters can be dropped or set to zero.

For example,
```
        rpm             rpm  [0 0 -1 0 0]  2000;

        conRodLength    conRodLength  [0 1 0 0 0] 0.0;
        bore            bore          [0 1 0 0 0] 0.0;
        stroke          stroke        [0 1 0 0 0] 0.0;
        clearance       clearance     [0 1 0 0 0] 0.0;
```

## Note
   The engineTime can currently only be selected at compile-time.

## SourceFiles
engineTime.C

