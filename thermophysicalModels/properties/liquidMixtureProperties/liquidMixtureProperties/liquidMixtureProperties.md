# liquidMixtureProperties 
## Class
Foam::liquidMixtureProperties

## Description
A mixture of liquids

An example of a two component liquid mixture:
```
        <parentDictionary>
        {
            H2O
            {
                defaultCoeffs   yes;     // employ default coefficients
            }
            C7H16
            {
                defaultCoeffs   no;
                C7H16Coeffs
                {
                    ... user defined properties for C7H16
                }
            }
        }
```

## SourceFiles
liquidMixtureProperties.C

## See also
Foam::liquidProperties

