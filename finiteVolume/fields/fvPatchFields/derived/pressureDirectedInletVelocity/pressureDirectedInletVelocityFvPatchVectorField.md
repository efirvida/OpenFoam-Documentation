# pressureDirectedInletVelocityFvPatchVectorField 
## Class
Foam::pressureDirectedInletVelocityFvPatchVectorField

## Group
grpInletBoundaryConditions

## Description
This velocity inlet boundary condition is applied to patches where the
pressure is specified.  The inflow velocity is obtained from the flux with
the specified inlet direction" direction.

## Usage

        Property     | Description             | Required    | Default value
        phi          | flux field name         | no          | phi
        rho          | density field name      | no          | rho
        inletDirection | inlet direction per patch face | yes |


Example of the boundary condition specification:
```
<patchName>
{
        type            pressureDirectedInletVelocity;
        phi             phi;
        rho             rho;
        inletDirection  uniform (1 0 0);
        value           uniform 0;
}
```

## Note
If reverse flow is possible or expected use the
pressureDirectedInletOutletVelocityFvPatchVectorField condition instead.


## See also
Foam::fixedValueFvPatchField
Foam::pressureDirectedInletOutletVelocityFvPatchVectorField

## SourceFiles
pressureDirectedInletVelocityFvPatchVectorField.C

