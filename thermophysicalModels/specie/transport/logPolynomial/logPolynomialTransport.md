# logPolynomialTransport 
## Class
Foam::logPolynomialTransport

## Description
Transport package using polynomial functions of ln(T) for mu and kappa:

        ln(mu)    = sum_i=1^N( a[i] * ln(T)^(i-1) )
        ln(kappa) = sum_i=1^N( b[i] * ln(T)^(i-1) )

## SourceFiles
logPolynomialTransportI.H
logPolynomialTransport.C

