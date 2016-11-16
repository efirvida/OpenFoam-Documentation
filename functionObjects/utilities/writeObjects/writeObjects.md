# writeObjects 
## Class
Foam::functionObjects::writeObjects

## Group
grpUtilitiesFunctionObjects

## Description
Allows specification of different writing frequency of objects registered to
the database.

It has similar functionality as the main time database through the
writeControl setting:
      - timeStep
      - writeTime
      - adjustableRunTime
      - runTime
      - clockTime
      - cpuTime

Example of function object specification:
```
writeObjects1
{
        type        writeObjects;
        libs        ("libutilityFunctionObjects.so");
        exclusiveWriting     true;
        ...
        objects     (obj1 obj2);
}
```

## Usage

        Property     | Description             | Required    | Default value
        type         | type name: writeObjects | yes |
        objects      | objects to write        | yes         |
        exclusiveWriting    | Takes over object writing | no | yes


\c exclusiveWriting disables automatic writing (i.e through database) of the
objects to avoid duplicate writing.

## See also
Foam::functionObject
Foam::functionObjects::timeControl

## SourceFiles
writeObjects.C

