# mixtureFractionSoot 
## Class
Foam::radiation::mixtureFractionSoot

## Description
This soot model is purely an state model. The ammount of soot produced is
determined by a single step chemistry as :

        nuf Fuel + nuOx Ox = nuP P + nuSoot soot

nuSoot is prescribed by the user.

The single step chemistry used is read from the combustion.
The soot is not considered into the thermodynamics of the system and it
is not considered as an extra specie in the solver.

The spacial distribution is given by the normalization of the first product
on the rhs of the reaction by default or it can be added as input.

The input dictionary reads like in the radiationProperties dictionary:

sootModel mixtureFractionSoot<gasHThermoPhysics>;

mixtureFractionSootCoeffs
{
        nuSoot              0.015;
        Wsoot               12;
        mappingField        P;
}

## SourceFiles
mixtureFractionSoot.C

