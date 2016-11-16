# atmBoundaryLayerInletEpsilonFvPatchScalarField 
## Class
Foam::atmBoundaryLayerInletEpsilonFvPatchScalarField

## Group
grpRASBoundaryConditions grpInletBoundaryConditions

## Description
This boundary condition specifies an inlet value for the turbulence
dissipation, \f$\epsilon\f$, appropriate for atmospheric boundary layers.

See Foam::atmBoundaryLayer for details.

Example of the boundary condition specification:
```
ground
{
        type            atmBoundaryLayerInletEpsilon;
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
Foam::atmBoundaryLayerInletKFvPatchScalarField

## SourceFiles
atmBoundaryLayerInletEpsilonFvPatchScalarField.C

