# COxidationHurtMitchell.T 
## Class
Foam::COxidationHurtMitchell

## Description
Char oxidation model given by Hurt and Mitchell:

Based on the reference:
        Hurt R. and Mitchell R., "Unified high-temperature char combustion
        kinetics for a suite of coals of various rank", 24th Symposium in
        Combustion, The Combustion Institute, 1992, p 1243-1250

Model specifies the rate of char combustion.

        C(s) + Sb*O2 -> CO2

where Sb is the stoichiometry of the reaction

Model validity:
        Gas temperature: Tc > 1500 K
        Particle sizes:  75 um -> 200 um
        Pox > 0.3 atm

