# targetCoeffTrim 
## Class
Foam::targetCoeffTrim

## Description
Target trim forces/coefficients

Solves:

        c^old + J.d(theta) = c^target

Where:

        n     = time level
        c     = coefficient vector (thrust force, roll moment, pitch moment)
        theta = pitch angle vector (collective, roll, pitch)
        J     = Jacobian [3x3] matrix


The trimmed pitch angles are found via solving the above with a
Newton-Raphson iterative method.  The solver tolerance can be user-input,
using the 'tol' entry.

If coefficients are requested (useCoeffs = true), the force and moments
are normalised using:

                         force
        c = ---------------------------------
            alpha*pi*rho*(omega^2)*(radius^4)

and

                         moment
        c = ---------------------------------
            alpha*pi*rho*(omega^2)*(radius^5)

Where:

        alpha = user-input conversion coefficient (default = 1)
        rho   = desity
        omega = rotor angulr velocity
        pi    = mathematical pi


## SourceFiles
targetCoeffTrim.C

