# sutherlandTransport 
## Class
Foam::sutherlandTransport

## Description
Transport package using Sutherland's formula.

Templated into a given thermodynamics package (needed for thermal
conductivity).

Dynamic viscosity [kg/m.s]
\f[
        \mu = A_s \frac{\sqrt{T}}{1 + T_s / T}
\f]

## SourceFiles
sutherlandTransportI.H
sutherlandTransport.C

