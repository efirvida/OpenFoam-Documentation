# polynomialFunction 
## Class
Foam::polynomialFunction

## Description
Polynomial function representation

        poly = logCoeff*log(x) + sum(coeff_[i]*x^i)

where 0 \<= i \<= N

- integer powers, starting at zero
- value(x) to evaluate the poly for a given value
- integrate(x1, x2) between two scalar values
- integral() to return a new, integral coeff polynomial
      - increases the size (order)
- integralMinus1() to return a new, integral coeff polynomial where
      the base poly starts at order -1

## See also
Foam::Polynomial for a templated implementation

## SourceFiles
polynomialFunction.C

