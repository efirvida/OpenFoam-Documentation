# Lun 
## Class
Foam::ParticleStressModels::Lun

## Description
Inter-particle stress model of Lun et al

The stress value takes the following form:
\f[
        \left( \alpha \rho + \alpha^2 \rho (1 + e) \frac{3}{5}
        \left( 1 - \left( \frac{\alpha}{\alpha_{pack}} \right)^\frac{1}{3}
        \right) \right) \frac{1}{3} \sigma^2
\f]
Here, \f$\alpha\f$ is the volume fraction of the dispersed phase,
\f$\rho\f$ is the density of the dispersed phase, \f$e\f$ is a coefficient
of restitution, and \f$\sigma\f$ is the RMS velocity fluctuation.

Reference:
```
        "Kinetic theories for granular flow: inelastic particles in Couette
        flow and slightly inelastic particles in a general flowfield"
        C Lun, S Savage, G Jeffrey, N Chepurniy
        Journal of Fluid Mechanics
        Volume 140, Pages 223-256, 1984
```

## SourceFiles
Lun.C

