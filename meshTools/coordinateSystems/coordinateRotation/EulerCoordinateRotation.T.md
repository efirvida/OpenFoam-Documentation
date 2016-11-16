# EulerCoordinateRotation.T 
## Class
Foam::EulerCoordinateRotation

## Description
A coordinateRotation defined in the z-x-y Euler convention.

The 3 rotations are defined in the Euler convention
(around Z, around X' and around Z').
For reference and illustration, see
http://mathworld.wolfram.com/EulerAngles.html
Note, however, that it is the reverse transformation
(local->global) that is defined here.

- the rotation angles are in degrees, unless otherwise explictly specified:

```
coordinateRotation
{
        type        EulerRotation;
        degrees     false;
        rotation    (0 0 3.141592654);
}
```

## SourceFiles
EulerCoordinateRotation.C

