# tabulatedAccelerationSource 
## Class
Foam::fv::tabulatedAccelerationSource

## Description
Solid-body 6-DoF acceleration source

## Usage
Example usage:
```
SBM
{
        type            tabulatedAccelerationSource;
        active          yes;

        tabulatedAccelerationSourceCoeffs
        {
            timeDataFileName "constant/acceleration-terms.dat";
        }
}
```


## SourceFiles
tabulatedAccelerationSource.C

