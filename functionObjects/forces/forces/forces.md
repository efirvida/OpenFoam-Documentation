# forces 
## Class
Foam::functionObjects::forces

## Group
grpForcesFunctionObjects

## Description
This function object calculates the forces and moments by integrating the
pressure and skin-friction forces over a given list of patches.

Member function forces::write() calculates the forces/moments and
writes the forces/moments into the file \<timeDir\>/forces.dat and bin
data (if selected) to the file \<timeDir\>/forces_bin.dat

Example of function object specification:
```
forces1
{
        type        forces;
        libs ("libforces.so");
        ...
        log         yes;
        patches     (walls);

        binData
        {
            nBin        20;
            direction   (1 0 0);
            cumulative  yes;
        }
}
```

## Usage

        Property     | Description             | Required    | Default value
        type         | Type name: forces       | yes         |
        log          | Write force data to standard output | no | no
        patches      | Patches included in the forces calculation | yes |
        p            | Pressure field name     | no          | p
        U            | Velocity field name     | no          | U
        rho          | Density field name (see below) | no   | rho
        CofR         | Centre of rotation (see below) | no   |
        directForceDensity | Force density supplied directly (see below)|no|no
        fD           | Name of force density field (see below) | no | fD


Bin data is optional, but if the dictionary is present, the entries must
be defined according o

        nBin         | number of data bins     | yes         |
        direction    | direction along which bins are defined | yes |
        cumulative   | bin data accumulated with incresing distance | yes |


## Note
  - For incompressible cases, set \c rho to \c rhoInf.  You will then be
required to provide a \c rhoInf value corresponding to the free-stream
constant density.
  - If the force density is supplied directly, set the \c directForceDensity
flag to 'yes', and supply the force density field using the \c
fDName entry
  - The centre of rotation (CofR) for moment calculations can either be
specified by an \c CofR entry, or be taken from origin of the local
coordinate system.  For example,
```
        CofR        (0 0 0);
```
or
```
        coordinateSystem
        {
            origin  (0 0 0);
            e3      (0 0 1);
            e1      (1 0 0);
        }
```

## See also
Foam::functionObject
Foam::functionObjects::writeFiles
Foam::functionObjects::timeControl
Foam::forceCoeffs

## SourceFiles
forces.C

