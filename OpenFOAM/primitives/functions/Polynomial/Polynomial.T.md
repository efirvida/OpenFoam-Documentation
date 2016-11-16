# Polynomial.T 
## Class
Foam::Polynomial

## Description
Polynomial templated on size (order):

        poly = sum(coeff_[i]*x^i) logCoeff*log(x)

where 0 \<= i \<= N

- integer powers, starting at zero
- value(x) to evaluate the poly for a given value
- derivative(x) returns derivative at value
- integral(x1, x2) returns integral between two scalar values
- integral() to return a new, integral coeff polynomial
      - increases the size (order)
- integralMinus1() to return a new, integral coeff polynomial where
      the base poly starts at order -1

## SourceFiles
Polynomial.C

