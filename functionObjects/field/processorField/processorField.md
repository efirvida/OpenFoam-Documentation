# processorField 
## Class
Foam::functionObjects::processorField

## Group
grpFieldFunctionObjects

## Description
This function object writes a scalar field whose value is the local
processor ID.  The output field name is 'processorID'.

Example of function object specification:
```
processorField1
{
        type        processorField;
        libs ("libfieldFunctionObjects.so");
        ...
}
```

## Usage

        Property     | Description             | Required    | Default value
        type         | type name: processorField | yes       |


## See also
Foam::functionObjects::fvMeshFunctionObject

## SourceFiles
processorField.C

