# fieldCoordinateSystemTransform 
## Class
Foam::functionObjects::fieldCoordinateSystemTransform

## Group
grpFieldFunctionObjects

## Description
This function object transforms a user-specified selection of fields from
global Cartesian co-ordinates to a local co-ordinate system.  The fields
are run-time modifiable.

Example of function object specification:
```
fieldCoordinateSystemTransform1
{
        type        fieldCoordinateSystemTransform;
        libs ("libfieldFunctionObjects.so");
        ...
        fields
        (
            U
            UMean
            UPrime2Mean
        );
        coordinateSystem
        {
            origin  (0.001  0       0);
            e1      (1      0.15    0);
            e3      (0      0      -1);
        }
}
```

## Usage

        Property     | Description             | Required    | Default value
        type         | type name: fieldCoordinateSystemTransform | yes |
        fields       | list of fields to be transformed |yes |
        coordinateSystem | local co-ordinate system | yes    |


## See also
Foam::functionObjects::fvMeshFunctionObject
Foam::coordinateSystem

## SourceFiles
fieldCoordinateSystemTransform.C
fieldCoordinateSystemTransformTemplates.C

