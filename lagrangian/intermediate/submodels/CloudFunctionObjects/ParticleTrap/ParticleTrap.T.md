# ParticleTrap.T 
## Class
Foam::ParticleTrap

## Description
Traps particles within a given phase fraction for multi-phase cases.

Model is activated using:
```
particleTrap1
{
        type        particleTrap;
        alphaName   alpha;      // name volume fraction field
        threshold   0.95;       // alpha value below which model is active
}
```


## SourceFiles
ParticleTrap.C

