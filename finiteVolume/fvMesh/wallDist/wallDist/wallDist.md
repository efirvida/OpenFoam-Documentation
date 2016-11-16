# wallDist 
## Class
Foam::wallDist

## Description
Interface to run-time selectable methods to calculate the distance-to-wall
and normal-to-wall fields.

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
Foam::patchDistMethod::meshWave
Foam::patchDistMethod::Poisson
Foam::patchDistMethod::advectionDiffusion

## SourceFiles
wallDist.C

