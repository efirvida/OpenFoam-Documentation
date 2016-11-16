# v2f 
## Class
Foam::RASModels::v2f

## Group
grpRASTurbulence

## Description
Lien and Kalitzin's v2-f turbulence model for incompressible and
compressible flows, with a limit imposed on the turbulent viscosity given
by Davidson et al.

The model solves for turbulence kinetic energy k and turbulence dissipation
rate epsilon, with additional equations for the turbulence stress normal to
streamlines, v2, and elliptic damping function, f.

The variant implemented employs N=6, such that f=0 on walls.

Wall boundary conditions are:

        k       = kLowReWallFunction
        epsilon = epsilonLowReWallFunction
        v2      = v2WallFunction
        f       = fWallFunction

These are applicable to both low- and high-Reynolds number flows.

Inlet values can be approximated by:

        v2      = 2/3 k
        f       = zero-gradient

References:
```
        Lien, F. S., & Kalitzin, G. (2001).
        Computations of transonic flow with the v2f turbulence model.
        International Journal of Heat and Fluid Flow, 22(1), 53-61.

        Davidson, L., Nielsen, P., & Sveningsson, A. (2003).
        Modifications of the v2-f model for computing the flow in a
        3D wall jet.
        Turbulence, Heat and Mass Transfer, 4, 577-584
```

The default model coefficients are
```
        v2fCoeffs
        {
            Cmu         0.22;
            CmuKEps     0.09;
            C1          1.4;
            C2          0.3;
            CL          0.23;
            Ceta        70;
            Ceps2       1.9;
            Ceps3       -0.33;
            sigmaEps    1.3;
            sigmaK      1;
        }
```

## Note
If the kLowReWallFunction is employed, a velocity variant of the turbulent
viscosity wall function should be used, e.g. nutUWallFunction.  Turbulence
k variants (nutk...) for this case will not behave correctly.

## See also
Foam::RASModels::v2fBase
Foam::RASModels::kEpsilon
Foam::kLowReWallFunctionFvPatchScalarField
Foam::epsilonLowReWallFunctionFvPatchScalarField
Foam::v2WallFunctionFvPatchScalarField
Foam::fWallFunctionFvPatchScalarField

## SourceFiles
v2f.C

