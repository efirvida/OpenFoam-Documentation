# externalCoupledMixedFvPatchField 
## Class
Foam::externalCoupledMixedFvPatchField

## Group
grpGenericBoundaryConditions grpCoupledBoundaryConditions

## Description
This boundary condition provides an interface to an external application.
Values are transferred as plain text files, where OpenFOAM data is written
as:

```
        # Patch: <patch name>
        <magSf1> <value1> <surfaceNormalGradient1>
        <magSf2> <value2> <surfaceNormalGradient2>
        <magSf3> <value3> <surfaceNormalGradient3>
        ...
        <magSfN> <valueN> <surfaceNormalGradientN>
```

and received as the constituent pieces of the `mixed' condition, i.e.

```
        # Patch: <patch name>
        <value1> <gradient1> <valueFracion1>
        <value2> <gradient2> <valueFracion2>
        <value3> <gradient3> <valueFracion3>
        ...
        <valueN> <gradientN> <valueFracionN>
```

Data is sent/received as a single file for all patches from the directory

```
        $FOAM_CASE/<commsDir>
```

At start-up, the boundary creates a lock file, i.e..

```
        OpenFOAM.lock
```

... to signal the external source to wait.  During the boundary condition
update, boundary values are written to file, e.g.

```
        <fileName>.out
```

The lock file is then removed, instructing the external source to take
control of the program execution.  When ready, the external program
should create the return values, e.g. to file

```
        <fileName>.in
```

... and then re-instate the lock file.  The boundary condition will then
read the return values, and pass program execution back to OpenFOAM.


## Usage

        Property     | Description             | Required    | Default value
        commsDir     | communications directory   | yes         |
        fileName     | transfer file name      | yes         |
        waitInterval | interval [s] between file checks | no | 1
        timeOut      | time after which error invoked [s] |no |100*waitInterval
        calcFrequency | calculation frequency  | no          | 1
        initByExternal | external app to initialises values  | yes |
        log          | log program control     | no          | no


Example of the boundary condition specification:
```
<patchName>
{
        type            externalCoupled;
        commsDir        "$FOAM_CASE/comms";
        fileName        data;
        calcFrequency   1;
        initByExternal  yes;
}
```

## See also
mixedFvPatchField

## SourceFiles
externalCoupledMixedFvPatchField.C

