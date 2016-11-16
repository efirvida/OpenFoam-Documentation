# lookupProfile 
## Class
Foam::lookupProfile

## Description
Look-up based profile data - drag and lift coefficients are lineraly
interpolated based on the supplied angle of attack

Input in list format:

        data
        (
            (AOA1 Cd1 Cl2)
            (AOA2 Cd2 Cl2)
            ...
            (AOAN CdN CdN)
        );

where:
        AOA = angle of attack [deg] converted to [rad] internally
        Cd  = drag coefficient
        Cl  = lift coefficient

## SourceFiles
lookupProfile.C

