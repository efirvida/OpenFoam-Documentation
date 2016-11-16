# seriesProfile 
## Class
Foam::seriesProfile

## Description
Series-up based profile data - drag and lift coefficients computed as
sum of cosine series

        Cd = sum_i(CdCoeff)*cos(i*AOA)
        Cl = sum_i(ClCoeff)*sin(i*AOA)

where:
        AOA = angle of attack [deg] converted to [rad] internally
        Cd = drag coefficent
        Cl = lift coefficent

Input in two (arbitrary length) lists:

        CdCoeffs (coeff1 coeff2 ... coeffN);
        ClCoeffs (coeff1 coeff2 ... coeffN);

## SourceFiles
seriesProfile.C

