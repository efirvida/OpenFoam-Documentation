# solidMixtureProperties 
## Class
Foam::solidMixtureProperties

## Description
A mixture of solids

An example of a two component solid mixture:
```
        <parentDictionary>
        {
            C
            {
                defaultCoeffs   yes;     // employ default coefficients
            }
            ash
            {
                defaultCoeffs   no;
                ashCoeffs
                {
                    ... user defined properties for ash
                }
            }
        }
```


## SourceFiles
solidMixtureProperties.C

## See also
Foam::solidProperties

