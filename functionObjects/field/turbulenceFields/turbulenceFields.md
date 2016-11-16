# turbulenceFields 
## Class
Foam::functionObjects::turbulenceFields

## Group
grpFieldFunctionObjects

## Description
This function object stores turbulence fields on the mesh database for
further manipulation.

Fields are stored as copies of the original, with the prefix
"tubulenceModel:", e.g.:

```
turbulenceModel:R
```

Example of function object specification:
```
turbulenceFields1
{
        type        turbulenceFields;
        libs ("libfieldFunctionObjects.so");
        ...
        fields
        (
            R
            devRhoReff
        );
}
```

## Usage

        Property     | Description                 | Required | Default value
        type         | type name: processorField   | yes      |
        fields       | fields to store (see below) | yes      |


Where \c fields can include:
\plaintable
        k           | turbulence kinetic energy
        epsilon     | turbulence kinetic energy dissipation rate
        omega       | turbulence specific dissipation rate
        nut         | turbulence viscosity (incompressible)
        nuEff       | effective turbulence viscosity (incompressible)
        mut         | turbulence viscosity (compressible)
        muEff       | effective turbulence viscosity (compressible)
        alphat      | turbulence thermal diffusivity (compressible)
        alphaEff    | effective turbulence thermal diffusivity (compressible)
        R           | Reynolds stress tensor
        devReff     | Deviatoric part of the effective Reynolds stress
        devRhoReff  | Divergence of the Reynolds stress
\endplaintable

## See also
Foam::functionObjects::fvMeshFunctionObject
Foam::functionObjects::timeControl

## SourceFiles
turbulenceFields.C

