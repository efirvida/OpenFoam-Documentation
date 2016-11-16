# variableHeightFlowRateFvPatchField 
## Class
Foam::variableHeightFlowRateFvPatchScalarField

## Group
grpInletBoundaryConditions

## Description
This boundary condition provides a phase fraction condition based on the
local flow conditions, whereby the values are constrained to lay between
user-specified upper and lower bounds.  The behaviour is described by:

if alpha > upperBound:
- apply a fixed value condition, with a uniform level of the upper bound

if lower bound <= alpha <= upper bound:
- apply a  zero-gradient condition

if alpha < lowerBound:
- apply a fixed value condition, with a uniform level of the lower bound

## Usage

        Property     | Description             | Required    | Default value
        phi          | flux field name         | no          | phi
        lowerBound   | lower bound for clipping | yes        |
        upperBound   | upper bound for clipping | yes        |


Example of the boundary condition specification:
```
<patchName>
{
        type            variableHeightFlowRate;
        lowerBound      0.0;
        upperBound      0.9;
        value           uniform 0;
}
```

## SourceFiles
variableHeightFlowRateFvPatchScalarField.C

