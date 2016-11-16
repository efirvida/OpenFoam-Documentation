# kOmegaSSTBase 
## Class
Foam::kOmegaSST

## Group
grpTurbulence

## Description
Implementation of the k-omega-SST turbulence model for
incompressible and compressible flows.

Turbulence model described in:
```
        Menter, F. R. & Esch, T. (2001).
        Elements of Industrial Heat Transfer Prediction.
        16th Brazilian Congress of Mechanical Engineering (COBEM).
```

with updated coefficients from
```
        Menter, F. R., Kuntz, M., and Langtry, R. (2003).
        Ten Years of Industrial Experience with the SST Turbulence Model.
        Turbulence, Heat and Mass Transfer 4, ed: K. Hanjalic, Y. Nagano,
        & M. Tummers, Begell House, Inc., 625 - 632.
```

but with the consistent production terms from the 2001 paper as form in the
2003 paper is a typo, see
```
        http://turbmodels.larc.nasa.gov/sst.html
```

and the addition of the optional F3 term for rough walls from
```
        Hellsten, A. (1998).
        "Some Improvements in Menter’s k-omega-SST turbulence model"
        29th AIAA Fluid Dynamics Conference, AIAA-98-2554.
```

Note that this implementation is written in terms of alpha diffusion
coefficients rather than the more traditional sigma (alpha = 1/sigma) so
that the blending can be applied to all coefficuients in a consistent
manner.  The paper suggests that sigma is blended but this would not be
consistent with the blending of the k-epsilon and k-omega models.

Also note that the error in the last term of equation (2) relating to
sigma has been corrected.

Wall-functions are applied in this implementation by using equations (14)
to specify the near-wall omega as appropriate.

The blending functions (15) and (16) are not currently used because of the
uncertainty in their origin, range of applicability and that if y+ becomes
sufficiently small blending u_tau in this manner clearly becomes nonsense.

The default model coefficients are
```
        kOmegaSSTCoeffs
        {
            alphaK1     0.85;
            alphaK2     1.0;
            alphaOmega1 0.5;
            alphaOmega2 0.856;
            beta1       0.075;
            beta2       0.0828;
            betaStar    0.09;
            gamma1      5/9;
            gamma2      0.44;
            a1          0.31;
            b1          1.0;
            c1          10.0;
            F3          no;
        }
```

## SourceFiles
kOmegaSST.C
