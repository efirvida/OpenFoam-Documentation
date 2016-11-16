# ReactingMultiphaseLookupTableInjection.T 
## Class
Foam::ReactingMultiphaseLookupTableInjection

## Description
Particle injection sources read from look-up table. Each row corresponds to
an injection site.

(
       (x y z) (u v w) d rho mDot T cp (Y0..Y2) (Yg0..YgN) (Yl0..YlN) (Ys0..YsN)
       (x y z) (u v w) d rho mDot T cp (Y0..Y2) (Yg0..YgN) (Yl0..YlN) (Ys0..YsN)
       ...
       (x y z) (u v w) d rho mDot T cp (Y0..Y2) (Yg0..YgN) (Yl0..YlN) (Ys0..YsN)
);

where:
        x, y, z  = global cartesian co-ordinates [m]
        u, v, w  = global cartesian velocity components [m/s]
        d        = diameter [m]
        rho      = density [kg/m3]
        mDot     = mass flow rate [kg/m3]
        T        = temperature [K]
        cp       = specific heat capacity [J/kg/K]
        Y(3)     = total mass fraction of gas (Y0), liquid (Y1), solid (Y3)
        Yg(Ngas) = mass fractions of gaseous components
        Yl(Nliq) = mass fractions of liquid components
        Ys(Nsld) = mass fractions of solid components

## SourceFiles
ReactingMultiphaseLookupTableInjection.C

