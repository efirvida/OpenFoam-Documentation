# uniformDensityHydrostaticPressureFvPatchScalarField 
## Class
Foam::uniformDensityHydrostaticPressureFvPatchScalarField

## Group
grpGenericBoundaryConditions

## Description
This boundary condition provides a hydrostatic pressure condition,
calculated as:

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


## Usage

        Property     | Description             | Required    | Default value
        rho          | uniform density [kg/m3] | yes         |
        pRefValue    | reference pressure [Pa] | yes         |
        pRefPoint    | reference pressure location | yes     |


Example of the boundary condition specification:
```
<patchName>
{
        type            uniformDensityHydrostaticPressure;
        rho             rho;
        pRefValue       1e5;
        pRefPoint       (0 0 0);
        value           uniform 0; // optional initial value
}
```

## SourceFiles
uniformDensityHydrostaticPressureFvPatchScalarField.C

