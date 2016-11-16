# NonSphereDragForce.T 
## Class
Foam::NonSphereDragForce

## Description
Drag model for non-spherical particles.

Takes the form of

        24.0/Re*(1.0 + a_*pow(Re, b_)) + Re*c_/(Re + d_);

Where a(phi), b(phi), c(phi) and d(phi) are model coefficients, with phi
defined as:

              area of sphere with same volume as particle
        phi = -------------------------------------------
                       actual particle area

Equation used is Eqn (11) of reference below - good to within 2 to 4 % of
RMS values from experiment.

H and L also give a simplified model with greater error compared to
results from experiment - Eqn 12 - but since phi is presumed
constant, it offers little benefit.

Reference:
```
        "Drag coefficient and terminal velocity of spherical and nonspherical
        particles"
        A. Haider and O. Levenspiel,
        Powder Technology
        Volume 58, Issue 1, May 1989, Pages 63-70
```


