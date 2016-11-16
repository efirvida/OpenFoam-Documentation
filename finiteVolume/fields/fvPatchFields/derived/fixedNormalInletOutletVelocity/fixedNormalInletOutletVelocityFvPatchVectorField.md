# fixedNormalInletOutletVelocityFvPatchVectorField 
## Class
Foam::fixedNormalInletOutletVelocityFvPatchVectorField

## Group
grpInletletBoundaryConditions grpOutletBoundaryConditions

## Description

This velocity inlet/outlet boundary condition combines a fixed normal
component obtained from the "normalVelocity" patchField supplied with a
fixed or zero-gradiented tangential component depending on the direction
of the flow and the setting of "fixTangentialInflow":
- Outflow: apply zero-gradient condition to tangential components
- Inflow:
      - fixTangentialInflow is true
        apply value provided by the normalVelocity patchField to the
        tangential components
      - fixTangentialInflow is false
        apply zero-gradient condition to tangential components.

## Usage

        Property     | Description             | Required    | Default value
        phi          | flux field name         | no          | phi
  fixTangentialInflow | If true fix the tangential component for inflow | yes |
        normalVelocity | patchField providing the normal velocity field | yes |


Example of the boundary condition specification:
```
<patchName>
{
        type            fixedNormalInletOutletVelocity;

        fixTangentialInflow false;
        normalVelocity
        {
            type            uniformFixedValue;
            uniformValue    sine;
            uniformValueCoeffs
            {
                frequency 1;
                amplitude table
                (
                    (0  0)
                    (2  0.088)
                    (8  0.088)
                );
                scale     (0 1 0);
                level     (0 0 0);
            }
        }

        value           uniform (0 0 0);
}
```

## SourceFiles
fixedNormalInletOutletVelocityFvPatchVectorField.C

