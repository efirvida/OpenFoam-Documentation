# alphaContactAngleFvPatchScalarField 
## Class
Foam::alphaContactAngleFvPatchScalarField

## Group
grpWallBoundaryConditions grpGenericBoundaryConditions

## Description
Abstract base class for alphaContactAngle boundary conditions.

Derived classes must implement the theta() fuction which returns the
wall contact angle field.

The essential entry "limit" controls the gradient of alpha1 on the wall:
      - none - Calculate the gradient from the contact-angle without limiter
      - gradient - Limit the wall-gradient such that alpha1 remains bounded
        on the wall
      - alpha - Bound the calculated alpha1 on the wall
      - zeroGradient - Set the gradient of alpha1 to 0 on the wall, i.e.
        reproduce previous behaviour, the pressure BCs can be left as before.

Note that if any of the first three options are used the boundary condition
on \c p_rgh must set to guarantee that the flux is corrected to be zero at
the wall e.g.:

```
<patchName>
{
        type            alphaContactAngle;
        limit           none;
}
```

## SourceFiles
alphaContactAngleFvPatchScalarField.C

