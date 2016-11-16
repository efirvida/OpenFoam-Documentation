# readFields 
## Class
Foam::functionObjects::readFields

## Group
grpFieldFunctionObjects

## Description
This function object reads fields from the time directories and adds them to
the mesh database for further post-processing.

Example of function object specification:
```
readFields1
{
        type        readFields;
        libs ("libfieldFunctionObjects.so");
        ...
        fields
        (
            U
            p
        );
}
```

## Usage

        Property     | Description             | Required    | Default value
        type         | type name: readFields   | yes         |
        fields       | list of fields to read  |  no         |


## See also
Foam::functionObjects::fvMeshFunctionObject

## SourceFiles
readFields.C

