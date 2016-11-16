# flowRateInletVelocityFvPatchVectorField 
## Class
Foam::flowRateInletVelocityFvPatchVectorField

## Group
grpInletBoundaryConditions

## Description
This boundary condition provides a velocity boundary condition, derived
from the flux (volumetric or mass-based), whose direction is assumed
to be normal to the patch.

For a mass-based flux:
- the flow rate should be provided in kg/s
- if \c rho is "none" the flow rate is in m3/s
- otherwise \c rho should correspond to the name of the density field
- if the density field cannot be found in the database, the user must
      specify the inlet density using the \c rhoInlet entry

For a volumetric-based flux:
- the flow rate is in m3/s

## Usage

        Property     | Description             | Required    | Default value
        massFlowRate | mass flow rate [kg/s]   | no          |
        volumetricFlowRate | volumetric flow rate [m3/s]| no |
        rhoInlet     | inlet density           | no          |
        extrapolateProfile | Extrapolate velocity profile | no | false


Example of the boundary condition specification for a volumetric flow rate:
```
<patchName>
{
        type                flowRateInletVelocity;
        volumetricFlowRate  0.2;
        extrapolateProfile  yes;
        value               uniform (0 0 0);
}
```

Example of the boundary condition specification for a mass flow rate:
```
<patchName>
{
        type                flowRateInletVelocity;
        massFlowRate        0.2;
        extrapolateProfile  yes;
        rho                 rho;
        rhoInlet            1.0;
        value               uniform (0 0 0);
}
```

The \c flowRate entry is a \c Function1 of time, see Foam::Function1Types.

## Note
- \c rhoInlet is required for the case of a mass flow rate, where the
      density field is not available at start-up
- The value is positive into the domain (as an inlet)
- May not work correctly for transonic inlets
- Strange behaviour with potentialFoam since the U equation is not solved

## See also
Foam::fixedValueFvPatchField
Foam::Function1Types

## SourceFiles
flowRateInletVelocityFvPatchVectorField.C

