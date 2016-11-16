# PoissonPatchDistMethod 
## Class
Foam::patchDistMethods::Poisson

## Description
Calculation of approximate distance to nearest patch for all cells and
boundary by solving Poisson's equation.

References:
```
        D.B. Spalding,
        "Calculation of turbulent heat transfer in cluttered spaces",
        Proc. 10th Int. Heat Transfer Conference, Brighton, UK, (1994).

        E. Fares and W. Schroder,
        "Differential Equation for Approximate Wall Distance",
        Int.J.Numer.Meth., 39:743-762, (2002).

        P.G. Tucker,
        "Differential equation based wall distance computation for DES and
         RANS",
        J.Comp.Phys., Vol. 190, Issue 1, 1 st September, pp. 229-248 (2003)
```

Example of the wallDist specification in fvSchemes:
```
        laplacianSchemes
        {
            .
            .
            laplacian(yPsi) Gauss linear corrected;
            .
            .
        }

        wallDist
        {
            method Poisson;

            // Optional entry enabling the calculation
            // of the normal-to-wall field
            nRequired false;
        }
```
Also the solver specification for yPsi is required in fvSolution, e.g.
for simple cases:
```
        yPsi
        {
            solver          PCG;
            preconditioner  DIC;
            tolerance       1e-5;
            relTol          0;
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
            tolerance       1e-5;
            relTol          0;
        }
```

## See also
Foam::patchDistMethod::meshWave
Foam::wallDist

## SourceFiles
PoissonPatchDistMethod.C

