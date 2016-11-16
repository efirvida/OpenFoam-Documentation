# Euler.T 
## Class
Foam::Euler

## Description
Euler ODE solver of order (0)1.

The method calculates the new state from:
\f[
        y_{n+1} = y_n + \delta_x f
\f]
The error is estimated directly from the change in the solution,
i.e. the difference between the 0th and 1st order solutions:
\f[
        err_{n+1} = y_{n+1} - y_n
\f]

## SourceFiles
Euler.C

