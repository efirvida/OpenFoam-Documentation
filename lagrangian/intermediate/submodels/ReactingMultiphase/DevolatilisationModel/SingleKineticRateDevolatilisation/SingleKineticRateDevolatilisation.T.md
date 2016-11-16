# SingleKineticRateDevolatilisation.T 
## Class
Foam::SingleKineticRateDevolatilisation

## Description
Single kinetic rate devolatisation model.
- acts on a per-specie basis
- Rate given by Arrhenius eqn

        kappa = A1.exp(- E/R.T)

Where:
        kappa = rate constant
        A1    = activation energy (user input)
        E     = pre-exponential factor (user input)
        R     = universal gas constant
        T     = temperature

Usage:

        SingleKineticRateDevolatilisationCoeffs
        {
            volatileData
            (
                (CH4     12     0.5)   // (name A1 E)
                (CO2     12     0.5)   // (name A1 E)
            );

            volatileResidualCoeff 1e-6;
        }

