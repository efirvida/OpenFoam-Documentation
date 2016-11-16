# kOmegaSSTDES 
## Class
Foam::LESModels::kOmegaSST

## Description
Implementation of the k-omega-SST-DES turbulence model for
incompressible and compressible flows.

DES model described in:
```
        Menter, F. R., Kuntz, M., and Langtry, R. (2003).
        Ten Years of Industrial Experience with the SST Turbulence Model.
        Turbulence, Heat and Mass Transfer 4, ed: K. Hanjalic, Y. Nagano,
        & M. Tummers, Begell House, Inc., 625 - 632.
```

Optional support for zonal filtering based on F1 or F2 is provided as
described in the paper.

For further details of the implementation of the base k-omega-SST model
see Foam::kOmegaSST.

## Group
grpLESTurbulence

## See also
Foam::kOmegaSST

## SourceFiles
kOmegaSST.C

