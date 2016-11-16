# GAMGSolver 
## Class
Foam::GAMGSolver

## Description
Geometric agglomerated algebraic multigrid solver.

  Characteristics:
      - Requires positive definite, diagonally dominant matrix.
      - Agglomeration algorithm: selectable and optionally cached.
      - Restriction operator: summation.
      - Prolongation operator: injection.
      - Smoother: Gauss-Seidel.
      - Coarse matrix creation: central coefficient: summation of fine grid
        central coefficients with the removal of intra-cluster face;
        off-diagonal coefficient: summation of off-diagonal faces.
      - Coarse matrix scaling: performed by correction scaling, using steepest
        descent optimisation.
      - Type of cycle: V-cycle with optional pre-smoothing.
      - Coarsest-level matrix solved using PCG or PBiCG.

## SourceFiles
GAMGSolver.C
GAMGSolverAgglomerateMatrix.C
GAMGSolverInterpolate.C
GAMGSolverScale.C
GAMGSolverSolve.C

