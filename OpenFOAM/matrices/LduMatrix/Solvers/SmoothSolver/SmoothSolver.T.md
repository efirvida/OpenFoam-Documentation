# SmoothSolver.T 
## Class
Foam::SmoothSolver

## Description
Iterative solver for symmetric and assymetric matrices which uses a
run-time selected smoother e.g. GaussSeidel to converge the solution to
the required tolerance.  To improve efficiency, the residual is evaluated
after every nSweeps smoothing iterations.

## SourceFiles
SmoothSolver.C

