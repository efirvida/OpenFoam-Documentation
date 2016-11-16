# fieldMinMax 
## Class
Foam::functionObjects::fieldMinMax

## Group
grpFieldFunctionObjects

## Description
This function object calculates the value and location of scalar minimim
and maximum for a list of user-specified fields.  For variables with a rank
greater than zero, either the min/max of a component value or the magnitude
is reported.  When operating in parallel, the processor owning the value
is also given.

Example of function object specification:
```
fieldMinMax1
{
        type        fieldMinMax;
        libs ("libfieldFunctionObjects.so");
        ...
        write       yes;
        log         yes;
        location    yes;
        mode        magnitude;
        fields
        (
            U
            p
        );
}
```

## Usage

        Property     | Description             | Required    | Default value
        type         | type name: fieldMinMax  | yes         |
        write        | write min/max data to file |  no      | yes
        log          | write min/max data to standard output | no | no
        location     | write location of the min/max value | no | yes
        mode         | calculation mode: magnitude or component | no | magnitude


Output data is written to the file \<timeDir\>/fieldMinMax.dat

## See also
Foam::functionObject
Foam::functionObjects::writeFiles

## SourceFiles
fieldMinMax.C

