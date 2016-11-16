# thixotropicViscosity 
## Class
Foam::thixotropicViscosity

## Description
Thixotropic viscosity model based on the evolution of the structural
parameter \f$ \lambda \f$:

        \f[
            \lambda = a(1 - \lambda)^b - c \lambda \dot{\gamma}^d
        \f]

The viscosity is then calculated using the expression

        \f[
            \mu = \frac{\mu_{\infty}}{{1 - K \lambda}^2}
        \f]

Where the parameter K is given by:

        \f[
            K = 1 - \sqrt{\frac{\mu_{\infty}}{\mu_{0}}}
        \f]

Here:
\vartable
        \lambda         | structural parameter
        a               | model coefficient
        b               | model coefficient
        c               | model coefficient
        d               | model coefficient
        \dot{\gamma}    | stress rate [1/s]
        \mu_{0}         | limiting viscosity when \f$ \lambda = 1 \f$
        \mu_{\infty}    | limiting viscosity when \f$ \lambda = 0 \f$
\endvartable

Reference:
```
        Barnes H A, 1997.  Thixotropy - a review.  J. Non-Newtonian Fluid
        Mech 70, pp 1-33
```

## SourceFiles
thixotropicViscosity.C

