# wallShearStress 
## Class
Foam::functionObjects::wallShearStress

## Group
grpForcesFunctionObjects

## Description
This function object evaluates and outputs the shear stress at wall
patches.  The result is written as a volVectorField to time directories as
field 'wallShearStress'

        \f[
            Stress = R \dot n
        \f]

where
\vartable
        R       | stress tensor
        n       | patch normal vector (into the domain)
\endvartable

The shear stress (symmetrical) tensor field is retrieved from the
turbulence model.  All wall patches are included by default; to restrict
the calculation to certain patches, use the optional 'patches' entry.

Example of function object specification:
```
wallShearStress1
{
        type        wallShearStress;
        libs ("libfieldFunctionObjects.so");
        ...
        patches     (".*Wall");
}
```

## Usage

        Property | Description               | Required    | Default value
        type     | type name: wallShearStress | yes        |
        patches  | list of patches to process | no         | all wall patches


## See also
Foam::functionObject
Foam::functionObjects::writeFiles
Foam::functionObjects::pressureTools
Foam::functionObjects::timeControl

## SourceFiles
wallShearStress.C

