# KinematicLookupTableInjection.T 
## Class
Foam::KinematicLookupTableInjection

## Description
Particle injection sources read from look-up table. Each row corresponds to
an injection site.

```
(
        (x y z) (u v w) d rho mDot   // injector 1
        (x y z) (u v w) d rho mDot   // injector 2
        ...
        (x y z) (u v w) d rho mDot   // injector N
);
```

where:
\plaintable
        x, y, z | global cartesian co-ordinates [m]
        u, v, w | global cartesian velocity components [m/s]
        d       | diameter [m]
        rho     | density [kg/m3]
        mDot    | mass flow rate [kg/m3]
\endplaintable

## SourceFiles
KinematicLookupTableInjection.C

