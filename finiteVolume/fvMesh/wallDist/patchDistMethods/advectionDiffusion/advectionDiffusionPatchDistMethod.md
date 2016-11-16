# advectionDiffusionPatchDistMethod 
## Class
Foam::patchDistMethods::advectionDiffusion

## Description
Calculation of approximate distance to nearest patch for all cells and
boundary by solving the Eikonal equation in advection form with diffusion
smoothing.

If the diffusion coefficient is set to 0 this method is exact in principle
but the numerical schemes used are not rendering the scheme approximate, but
more accurate than the Poisson method.  Also many models relying on the
distance to the wall benefit from this field being smooth and monotonic so
the addition of diffusion smoothing improves both the convergence and
stability of the solution of the Eikonal equation and the behavior of the
models using the distance field generated.  However, it is not clear what
the optimum value for the diffusion coefficient epsilon should be; a
default value of 0.1 is provided but higher values may be preferable under
some circumstances.

Convergence is accelerated by first generating an approximate solution
using one of the simpler methods, e.g. Poisson.  The method used for
this prediction step is specified in the 'advectionDiffusionCoeffs'
sub-dictionary, see below.

References:
```
        P.G. Tucker, C.L. Rumsey, R.E. Bartels, R.T. Biedron,
        "Transport equation based wall distance computations aimed at flows
         with time-dependent geometry",
        NASA/TM-2003-212680, December 2003.
```

Example of the wallDist specification in fvSchemes:
```
        laplacianSchemes
        {
            .
            .
            laplacian(yPsi) Gauss linear corrected;
            laplacian(yWall) Gauss linear corrected;
            .
            .
        }

        wallDist
        {
            method advectionDiffusion;

            // Optional entry enabling the calculation
            // of the normal-to-wall field
            nRequired false;

            advectionDiffusionCoeffs
            {
                method    Poisson;
                epsilon   0.1;
                tolerance 1e-3;
                maxIter   10;
            }
        }
```
Also the solver specification for yWall is required in fvSolution, e.g.
for simple cases:
```
        yPsi
        {
            solver          PCG;
            preconditioner  DIC;
            tolerance       1e-4;
            relTol          0;
        }

        yWall
        {
            solver          PBiCG;
            preconditioner  DILU;
            tolerance       1e-4;
            relTol          0;
        }

        relaxationFactors
        {
            equations
            {
                .
                .
                yWall           1;
                .
                .
            }
        }

or for more complex cases:

        yPsi
        {
            solver          GAMG;
            smoother        GaussSeidel;
            cacheAgglomeration true;
            nCellsInCoarsestLevel 10;
            agglomerator    faceAreaPair;
            mergeLevels     1;
            tolerance       1e-4;
            relTol          0;
        }

        yWall
        {
            solver          GAMG;
            smoother        symGaussSeidel;
            cacheAgglomeration true;
            nCellsInCoarsestLevel 10;
            agglomerator    faceAreaPair;
            mergeLevels     1;
            tolerance       1e-4;
            relTol          0;
        }

        relaxationFactors
        {
            equations
            {
                .
                .
                yWall           0.7;
                .
                .
            }
        }
```

## See also
Foam::patchDistMethod::Poisson
Foam::patchDistMethod::meshWave
Foam::wallDist

## SourceFiles
advectionDiffusionPatchDistMethod.C

