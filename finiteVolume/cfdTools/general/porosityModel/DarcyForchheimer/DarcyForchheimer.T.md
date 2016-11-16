# DarcyForchheimer.T 
## Class
Foam::DarcyForchheimer

## Description
Darcy-Forchheimer law porosity model, given by:

        \f[
            S = - (\mu d + \frac{\rho |U|}{2} f) U
        \f]

where
\vartable
        d        | Darcy coefficient [1/m2]
        f        | Forchheimer coefficient [1/m]
\endvartable

Since negative Darcy/Forchheimer parameters are invalid, they can be used
to specify a multiplier (of the max component).

The orientation of the porous region is defined with the same notation as
a co-ordinate system, but only a Cartesian co-ordinate system is valid.

## SourceFiles
DarcyForchheimer.C
DarcyForchheimerTemplates.C

