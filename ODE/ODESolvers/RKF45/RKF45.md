# RKF45 
## Class
Foam::RKF45

## Description
4/5th Order Runge-Kutta-Fehlberg ODE solver

References:
```
        "Low-order classical Runge-Kutta formulas with step size control
         and their application to some heat transfer problems."
        Fehlberg, E.,
        NASA Technical Report 315, 1969.

        "Solving Ordinary Differential Equations I: Nonstiff Problems,
         second edition",
        Hairer, E.,
        Nørsett, S.,
        Wanner, G.,
        Springer-Verlag, Berlin. 1993, ISBN 3-540-56670-8.
```

This method embedds the 4-th order integration step into the 5-th order step
and allows to perform an adapdive step-size control using these two order
without the need of re-evaluation.

## SourceFiles
RKF45.C

