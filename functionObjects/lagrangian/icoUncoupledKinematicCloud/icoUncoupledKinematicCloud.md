# icoUncoupledKinematicCloud 
## Class
Foam::functionObjects::icoUncoupledKinematicCloud

## Group
grpLagrangianFunctionObjects

## Description
This functionObject tracks a uncoupled kinematic particle cloud in the
specified velocity field of an incompressible flow (laminar, RANS or LES).

It may be used in conjunction with any transient single-phase incompressible
flow solver such as pisoFoam or pimpleFoam and tracks the particles or
parcels without affecting the the flow-field.

The kinematicCloud requires the the density of the fluid which is looked-up
from constant/transportProperties dictionary and the acceleration due to
gravity which is read from the constant/g file if present or defaults to
zero.

The kinematicCloud properties are read from the
constant/kinematicCloudProperties dictionary in the usual manner.

Example of function object specification:
```
        tracks
        {
            libs ("liblagrangianFunctionObjects.so");
            type icoUncoupledKinematicCloud;
        }
```

## Usage

        Property | Description                     | Required   | Default value
        type     | Type name: icoUncoupledKinematicCloud | yes  |
        U        | Name of the velocity field       | no        | U
        kinematicCloud | Name of the kinematicCloud | no        | kinematicCloud


## See also
Foam::functionObjects::fvMeshFunctionObject

## SourceFiles
icoUncoupledKinematicCloud.C

