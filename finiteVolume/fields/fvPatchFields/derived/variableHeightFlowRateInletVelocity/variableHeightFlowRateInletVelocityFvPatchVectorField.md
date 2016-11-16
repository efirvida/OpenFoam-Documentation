# variableHeightFlowRateInletVelocityFvPatchVectorField 
## Class
Foam::variableHeightFlowRateInletVelocityFvPatchVectorField

## Group
grpInletBoundaryConditions

## Description
This boundary condition provides a velocity boundary condition for
multphase flow based on a user-specified volumetric flow rate.

The flow rate is made proportional to the phase fraction alpha at each
face of the patch and alpha is ensured to be bound between 0 and 1.

## Usage

        Property     | Description             | Required    | Default value
        flowRate     | volumetric flow rate [m3/s] | yes |
        alpha        | phase-fraction field    | yes |


Example of the boundary condition specification:
```
<patchName>
{
        type            variableHeightFlowRateInletVelocity;
        flowRate        0.2;
        alpha           alpha.water;
        value           uniform (0 0 0); // placeholder
}
```

The \c flowRate entry is a \c Function1 of time, see Foam::Function1Types.

## Note
- the value is positive into the domain
- may not work correctly for transonic inlets
- strange behaviour with potentialFoam since the momentum equation is
      not solved

## See also
Foam::fixedValueFvPatchField
Foam::Function1Types

## SourceFiles
variableHeightFlowRateInletVelocityFvPatchVectorField.C

