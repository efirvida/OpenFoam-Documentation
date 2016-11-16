# atmBoundaryLayerInletVelocityFvPatchVectorField 
## Class
Foam::atmBoundaryLayerInletVelocityFvPatchVectorField

## Group
grpRASBoundaryConditions grpInletBoundaryConditions

## Description
This boundary condition specifies a velocity inlet profile appropriate
for atmospheric boundary layers (ABL).

See Foam::atmBoundaryLayer for details.

Example of the boundary condition specification:
```
ground
{
        type            atmBoundaryLayerInletVelocity;
        n               (1 0 0);
        z               (0 0 1);
        Uref            10.0;
        Zref            20.0;
        z0              uniform 0.1;
        zGround         uniform 0.0;
}
```

## See also
Foam::atmBoundaryLayer,
Foam::atmBoundaryLayerInletKFvPatchScalarField,
Foam::atmBoundaryLayerInletEpsilonFvPatchScalarField

## SourceFiles
atmBoundaryLayerInletVelocityFvPatchVectorField.C

