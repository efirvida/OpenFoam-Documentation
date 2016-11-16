# uniformInterpolatedDisplacementPointPatchVectorField 
## Class
Foam::uniformInterpolatedDisplacementPointPatchVectorField

## Description
Interpolates pre-specified motion.

Motion specified as pointVectorFields.

## Usage
Example:
```
walls
{
        type                uniformInterpolatedDisplacement;
        value               uniform (0 0 0);
        field               wantedDisplacement;
        interpolationScheme linear;
}
```

This will scan the case for \a wantedDisplacement pointVectorFields
and interpolate those in time (using \c linear interpolation) to
obtain the current displacement.
The advantage of specifying displacement in this way is that it
automatically works through decomposePar.

## SourceFiles
uniformInterpolatedDisplacementPointPatchVectorField.C

