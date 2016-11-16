# coordinateSystem 
## Class
Foam::coordinateSystem

## Description
Base class for other coordinate system specifications.

All systems are defined by an origin point and a co-ordinate rotation.

```
coordinateSystem
{
        type    cartesian;
        origin  (0 0 0);
        coordinateRotation
        {
            type        cylindrical;
            e3          (0 0 1);
        }
}
```

Types of coordinateRotation:
      -# axesRotation
      -# \link STARCDCoordinateRotation STARCDRotation \endlink
      -# cylindricalCS cylindrical
      -# EulerCoordinateRotation

Type of co-ordinates:
      -# \link cartesianCS cartesian \endlink


## SourceFiles
coordinateSystem.C
coordinateSystemNew.C

