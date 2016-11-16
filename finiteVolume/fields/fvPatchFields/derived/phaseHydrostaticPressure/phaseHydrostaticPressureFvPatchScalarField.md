# phaseHydrostaticPressureFvPatchScalarField 
## Class
Foam::phaseHydrostaticPressureFvPatchScalarField

## Group
grpGenericBoundaryConditions

## Description
This boundary condition provides a phase-based hydrostatic pressure
condition, calculated as:

        \f[
            p_{hyd} = p_{ref} + \rho g (x - x_{ref})
        \f]

where
\vartable
        p_{hyd} | hyrostatic pressure [Pa]
        p_{ref} | reference pressure [Pa]
        x_{ref} | reference point in Cartesian co-ordinates
        \rho    | density (assumed uniform)
        g       | acceleration due to gravity [m/s2]


The values are assigned according to the phase-fraction field:
- 1: apply \$fp_{hyd}\$f
- 0: apply a zero-gradient condition

## Usage

        Property      | Description                 | Required | Default value
        phaseFraction | phase-fraction field name   | no       | alpha
        rho           | density field name          | no       | rho
        pRefValue     | reference pressure [Pa]     | yes      |
        pRefPoint     | reference pressure location | yes      |


Example of the boundary condition specification:
```
<patchName>
{
        type            phaseHydrostaticPressure;
        phaseFraction   alpha1;
        rho             rho;
        pRefValue       1e5;
        pRefPoint       (0 0 0);
        value           uniform 0; // optional initial value
}
```

## See also
Foam::mixedFvPatchScalarField

## SourceFiles
phaseHydrostaticPressureFvPatchScalarField.C

