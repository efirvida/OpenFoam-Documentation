# LienLeschziner 
## Class
Foam::incompressible::RASModels::LienLeschziner

## Group
grpIcoRASTurbulence

## Description
Lien and Leschziner low-Reynolds number k-epsilon turbulence model for
incompressible flows.

This turbulence model is described in:
```
        Lien, F. S., & Leschziner, M. A. (1993).
        A pressure-velocity solution strategy for compressible flow
        and its application to shock/boundary-layer interaction
        using second-moment turbulence closure.
        Journal of fluids engineering, 115(4), 717-725.
```

Implemented according to the specification in:
<a href=
"http://personalpages.manchester.ac.uk/staff/david.d.apsley/specturb.pdf"
>Apsley: Turbulence Models 2002</a>

In addition to the low-Reynolds number damping functions support for
wall-functions is also included to allow for low- and high-Reynolds number
operation.

## SourceFiles
LienLeschziner.C

