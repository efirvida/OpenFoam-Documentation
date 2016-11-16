# meshWavePatchDistMethod 
## Class
Foam::patchDistMethods::meshWave

## Description
Fast topological mesh-wave method for calculating the distance to nearest
patch for all cells and boundary.

For regular/un-distorted meshes this method is accurate but for skewed,
non-orthogonal meshes it is approximate with the error increasing with the
degree of mesh distortion.  The distance from the near-wall cells to the
boundary may optionally be corrected for mesh distortion by setting
correctWalls = true.

Example of the wallDist specification in fvSchemes:
```
        wallDist
        {
            method meshWave;

            // Optional entry enabling the calculation
            // of the normal-to-wall field
            nRequired false;
        }
```

## See also
Foam::patchDistMethod::Poisson
Foam::wallDist

## SourceFiles
meshWavePatchDistMethod.C

