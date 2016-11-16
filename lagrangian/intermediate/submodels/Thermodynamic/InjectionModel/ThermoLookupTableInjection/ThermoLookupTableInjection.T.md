# ThermoLookupTableInjection.T 
## Class
Foam::ThermoLookupTableInjection

## Description
Particle injection sources read from look-up table. Each row corresponds to
an injection site.

(
        (x y z) (u v w) d rho mDot T cp  // injector 1
        (x y z) (u v w) d rho mDot T cp  // injector 2
        ...
        (x y z) (u v w) d rho mDot T cp  // injector N
);

where:
        x, y, z = global cartesian co-ordinates [m]
        u, v, w = global cartesian velocity components [m/s]
        d       = diameter [m]
        rho     = density [kg/m3]
        mDot    = mass flow rate [kg/m3]
        T       = temperature [K]
        cp      = specific heat capacity [J/kg/K]

## SourceFiles
ThermoLookupTableInjection.C

