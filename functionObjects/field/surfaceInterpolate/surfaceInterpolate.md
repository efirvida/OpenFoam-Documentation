# surfaceInterpolate 
## Class
Foam::surfaceInterpolate

## Group grpFieldFunctionObjects

## Description
This function object linearly interpolates volume fields to generate
surface fields

Fields are stored
- every time step the field is updated with new values
- at output it writes the fields

This functionObject can either be used
- to calculate a new field as a  post-processing step or
- since the fields are registered, used in another functionObject

Example of function object specification:
```
surfaceInterpolate1
{
        type        surfaceInterpolate;
        libs ("libfieldFunctionObjects.so");
        ...
        fields      ((p pNear)(U UNear));
}
```

## Usage

        Property | Description               | Required    | Default value
        type     | type name: nearWallFields | yes         |
        fields   | list of fields with correspoding output field names | yes |



## See also
Foam::functionObjects::fvMeshFunctionObject
Foam::functionObjects::timeControl

## SourceFiles
surfaceInterpolate.C

