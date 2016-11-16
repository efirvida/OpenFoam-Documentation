# LienCubicKE 
## Class
Foam::incompressible::RASModels::LienCubicKE

## Group
grpIcoRASTurbulence

## Description
Lien cubic non-linear low-Reynolds k-epsilon turbulence models for
incompressible flows.

This turbulence model is described in:
```
        Lien, F.S., Chen, W.L. & Leschziner, M.A. (1996).
        Low-Reynolds-number eddy-viscosity modeling based on non-linear
        stress-strain/vorticity relations.
        Engineering Turbulence Modelling and Experiments 3, 91-100.
```

Implemented according to the specification in:
<a href=
"http://personalpages.manchester.ac.uk/staff/david.d.apsley/specturb.pdf"
>Apsley: Turbulence Models 2002</a>

In addition to the low-Reynolds number damping functions support for
wall-functions is also included to allow for low- and high-Reynolds number
operation.

## See also
Foam::incompressible::RASModels::ShihQuadraticKE

## SourceFiles
LienCubicKE.C

