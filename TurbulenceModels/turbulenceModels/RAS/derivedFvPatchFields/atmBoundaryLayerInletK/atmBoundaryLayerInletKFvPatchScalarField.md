# atmBoundaryLayerInletKFvPatchScalarField 
## Class
Foam::atmBoundaryLayerInletKFvPatchScalarField

## Group
grpRASBoundaryConditions grpInletBoundaryConditions

## Description
This boundary condition specifies an inlet value for the turbulence
kinetic energy, \f$k\f$, appropriate for atmospheric boundary layers.

See Foam::atmBoundaryLayer for details.

Example of the boundary condition specification:
```
ground
{
        type            atmBoundaryLayerInletK;
        z               (0 0 1);
        Uref            10.0;
        Zref            20.0;
        z0              uniform 0.1;
        zGround         uniform 0.0;
}
```

## See also
Foam::atmBoundaryLayer,
Foam::atmBoundaryLayerInletVelocityFvPatchVectorField,
Foam::atmBoundaryLayerInletEpsilonFvPatchScalarField

## SourceFiles
atmBoundaryLayerInletKFvPatchScalarField.C

