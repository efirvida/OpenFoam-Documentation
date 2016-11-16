# STARCDCoordinateRotation 
## Class
Foam::STARCDCoordinateRotation

## Description
A coordinateRotation defined by the STAR-CD convention.

The 3 rotations are defined in the STAR-CD convention
(around Z, around X' and around Y'').
The order of the parameter arguments matches this rotation order.

- the rotation angles are in degrees, unless otherwise explictly specified:

```
coordinateRotation
{
        type        STARCDRotation;
        degrees     false;
        rotation    (0 0 3.141592654);
}
```

## SourceFiles
STARCDCoordinateRotation.C

