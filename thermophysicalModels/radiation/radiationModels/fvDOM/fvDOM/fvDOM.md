# fvDOM 
## Class
Foam::radiation::fvDOM

## Description

Finite Volume Discrete Ordinates Method. Solves the RTE equation for n
directions in a participating media, not including scatter.

Available absorption models:
        constantAbsorptionEmission
        greyMeanAbsoprtionEmission
        wideBandAbsorptionEmission

i.e. dictionary
```
        fvDOMCoeffs
        {
            nPhi        4;          // azimuthal angles in PI/2 on X-Y.
                                    //(from Y to X)
            nTheta      0;          // polar angles in PI (from Z to X-Y plane)
            convergence 1e-3;       // convergence criteria for radiation
                                    //iteration
            maxIter     4;          // maximum number of iterations
            cacheDiv    true;       // cache the div of the RTE equation.
            //NOTE: Caching div is "only" accurate if the upwind scheme is used
            //in div(Ji,Ii_h)
        }

        solverFreq   1; // Number of flow iterations per radiation iteration
```

The total number of solid angles is  4*nPhi*nTheta.

In 1D the direction of the rays is X (nPhi and nTheta are ignored)
In 2D the direction of the rays is on X-Y plane (only nPhi is considered)
In 3D (nPhi and nTheta are considered)

## SourceFiles
fvDOM.C

