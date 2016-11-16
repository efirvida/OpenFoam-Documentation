# nearWallFields 
## Class
Foam::functionObjects::nearWallFields

## Group
grpFieldFunctionObjects

## Description
This function object samples near-patch volume fields

Fields are stored
- every time step the field is updated with new values
- at output it writes the fields

This functionObject can either be used
- to calculate a new field as a  post-processing step or
- since the fields are registered, used in another functionObject

Example of function object specification:
```
nearWallFields1
{
        type        nearWallFields;
        libs ("libfieldFunctionObjects.so");
        ...
        fields      ((p pNear)(U UNear));
        patches     (movingWall);
        distance    0.13;
}
```

## Usage

        Property | Description               | Required    | Default value
        type     | type name: nearWallFields | yes         |
        fields   | list of fields with correspoding output field names | yes |
        patches  | list of patches to sample | yes         |
        distance | distance from patch to sample | yes     |


## See also
Foam::functionObjects::fvMeshFunctionObject

## SourceFiles
nearWallFields.C

