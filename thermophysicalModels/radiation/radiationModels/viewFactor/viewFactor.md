# viewFactor 
## Class
Foam::radiation::viewFactor

## Description
View factor radiation model. The system solved is: C q = b
where:
            Cij  = deltaij/Ej - (1/Ej - 1)Fij
            q    = heat flux
            b    = A eb - Ho
and:
            eb   = sigma*T^4
            Ej   = emissivity
            Aij  = deltaij - Fij
            Fij  = view factor matrix


## SourceFiles
viewFactor.C

