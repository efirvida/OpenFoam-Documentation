# outletPhaseMeanVelocityFvPatchVectorField 
## Class
Foam::outletPhaseMeanVelocityFvPatchVectorField

## Group
grpOutletBoundaryConditions

## Description
This boundary condition adjusts the velocity for the given phase to achieve
the specified mean thus causing the phase-fraction to adjust according to
the mass flow rate.

Typical usage is as the outlet condition for a towing-tank ship simulation
to maintain the outlet water level at the level as the inlet.

## Usage

        Property     | Description             | Required    | Default value
        Umean        | mean velocity normal to the boundary [m/s] | yes |
        alpha        | phase-fraction field    | yes |


Example of the boundary condition specification:
```
<patchName>
{
        type            outletPhaseMeanVelocity;
        Umean           1.2;
        alpha           alpha.water;
        value           uniform (1.2 0 0);
}
```

## See also
Foam::mixedFvPatchField
Foam::variableHeightFlowRateInletVelocityFvPatchVectorField

## SourceFiles
outletPhaseMeanVelocityFvPatchVectorField.C

