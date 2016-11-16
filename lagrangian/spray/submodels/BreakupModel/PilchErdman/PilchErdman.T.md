# PilchErdman.T 
## Class
Foam::PilchErdman

## Description
Particle secondary breakup model, based on the reference:

```
Pilch, M. and Erdman, C.A.
"Use of breakup time data and velocity history data
     to predict the maximum size of stable fragments for acceleration
     induced breakup of a liquid drop."
Int. J. Multiphase Flows 13 (1987), 741-757
```

The droplet fragment velocity is described by the equation:

\f[
        V_d = V sqrt(epsilon)(B1 T + B2 T^2)
\f]

Where:
        V_d     : fragment velocity
        V       : magnitude of the relative velocity
        epsilon : density ratio (rho_carrier/rho_droplet)
        T       : characteristic break-up time
        B1, B2  : model input coefficients

The authors suggest that:
        compressible flow   : B1 = 0.75*1.0; B2 = 3*0.116
        incompressible flow : B1 = 0.75*0.5; B2 = 3*0.0758


