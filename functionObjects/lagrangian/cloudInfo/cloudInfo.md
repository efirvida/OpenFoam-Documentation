# cloudInfo 
## Class
Foam::functionObjects::cloudInfo

## Group
grpLagrangianFunctionObjects

## Description
This function object outputs Lagrangian cloud information to a file.  The
current outputs include:
- total current number of parcels
- total current mass of parcels

Example of function object specification:
```
cloudInfo1
{
        type        cloudInfo;
        libs ("libcloudFunctionObjects.so");
        ...
        clouds
        (
            kinematicCloud1
            thermoCloud1
        );
}
```


## Usage

        Property     | Description             | Required    | Default value
        type         | type name: cloudInfo    | yes         |
        clouds       | list of clouds names to process |yes  |


The output data of each cloud is written to a file named \<cloudName\>.dat

## See also
Foam::functionObject
Foam::functionObjects::writeFiles

## SourceFiles
cloudInfo.C

