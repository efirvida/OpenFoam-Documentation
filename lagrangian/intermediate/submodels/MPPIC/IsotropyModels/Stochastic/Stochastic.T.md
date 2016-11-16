# Stochastic.T 
## Class
Foam::IsotropyModels::Stochastic

## Description
Stochastic return-to-isotropy model.

Particle velocities are modified by sampling a gaussian-plus-delta
distribution, which depends on a time-scale. This randomises some particle
velocities whilst leaving others unchanged. The lower the value of the
time-scale, the greater the proportion of particle velocities affected.

A correction step is performed at the end to ensure that the model
conserves both momentum and granular temperature.

Reference:
```
        "Inclusion of collisional return-to-isotropy in the MP-PIC method"
        P O'Rourke and D Snider
        Chemical Engineering Science
        Volume 80, Issue 0, Pages 39-54, December 2012
```

## SourceFiles
Stochastic.C

