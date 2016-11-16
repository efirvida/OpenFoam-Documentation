# removeRegisteredObject 
## Class
Foam::functionObjects::removeRegisteredObject

## Group
grpUtilitiesFunctionObjects

## Description
Removes registered objects if present in the database.

Example of function object specification:
```
removeRegisteredObject1
{
        type        removeRegisteredObject;
        libs        ("libutilityFunctionObjects.so");
        ...
        objects     (obj1 obj2);
}
```

## Usage

        Property     | Description             | Required    | Default value
        type         | type name: removeRegisteredObject | yes |
        objects      | objects to remove       | yes         |


## See also
Foam::functionObject

## SourceFiles
removeRegisteredObject.C

