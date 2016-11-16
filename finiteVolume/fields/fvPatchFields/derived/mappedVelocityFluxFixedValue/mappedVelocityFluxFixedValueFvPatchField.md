# mappedVelocityFluxFixedValueFvPatchField 
## Class
Foam::mappedVelocityFluxFixedValueFvPatchField

## Group
grpInletBoundaryConditions grpCoupledBoundaryConditions

## Description
This boundary condition maps the velocity and flux from a neighbour patch
to this patch

## Usage

        Property     | Description             | Required    | Default value
        phi          | flux field name         | no          | phi


Example of the boundary condition specification:
```
<patchName>
{
        type            mappedVelocityFlux;
        phi             phi;
        value           uniform 0;  // place holder
}
```

The underlying sample mode should be set to \c nearestPatchFace or
\c nearestFace

## Note
This boundary condition can only be applied to patches that are of
the \c mappedPolyPatch type.

## See also
Foam::mappedPatchBase
Foam::mappedPolyPatch
Foam::mappedFvPatch
Foam::fixedValueFvPatchVectorField

## SourceFiles
mappedVelocityFluxFixedValueFvPatchField.C

