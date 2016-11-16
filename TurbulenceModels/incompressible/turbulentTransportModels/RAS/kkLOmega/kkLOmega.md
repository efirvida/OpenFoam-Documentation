# kkLOmega 
## Class
Foam::incompressible::RASModels::kkLOmega

## Group
grpIcoRASTurbulence

## Description
Low Reynolds-number k-kl-omega turbulence model for
incompressible flows.

This turbulence model is described in:
```
        Walters, D. K., & Cokljat, D. (2008).
        A three-equation eddy-viscosity model for Reynolds-averaged
        Navier–Stokes simulations of transitional flow.
        Journal of Fluids Engineering, 130(12), 121401.
```

however the paper contains several errors which must be corrected for the
model to operation correctly as explained in

```
        Furst, J. (2013).
        Numerical simulation of transitional flows with laminar kinetic energy.
        Engineering MECHANICS, 20(5), 379-388.
```

All these corrections and updates are included in this implementation.

The default model coefficients are
```
        kkLOmegaCoeffs
        {
            A0             4.04
            As             2.12
            Av             6.75
            Abp            0.6
            Anat           200
            Ats            200
            CbpCrit        1.2
            Cnc            0.1
            CnatCrit       1250
            Cint           0.75
            CtsCrit        1000
            CrNat          0.02
            C11            3.4e-6
            C12            1.0e-10
            CR             0.12
            CalphaTheta    0.035
            Css            1.5
            CtauL          4360
            Cw1            0.44
            Cw2            0.92
            Cw3            0.3
            CwR            1.5
            Clambda        2.495
            CmuStd         0.09
            Prtheta        0.85
            Sigmak         1
            Sigmaw         1.17
        }
```

## SourceFiles
kkLOmega.C

