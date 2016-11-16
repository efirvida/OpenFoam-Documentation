# EulerSI.T 
## Class
Foam::EulerSI

## Description
Semi-implicit Euler ODE solver of order (0)1.

The method calculates the new state from:
\f[
        y_{n+1} = y_n
          + \delta_x\left[I - \delta_x\frac{\partial f}{\partial y}\right]^{-1}
            \cdot \left[f(y_n) + \delta_x\frac{\partial f}{\partial x}\right]
\f]
The error is estimated directly from the change in the solution,
i.e. the difference between the 0th and 1st order solutions:
\f[
        err_{n+1} = y_{n+1} - y_n
\f]

## SourceFiles
EulerSI.C

