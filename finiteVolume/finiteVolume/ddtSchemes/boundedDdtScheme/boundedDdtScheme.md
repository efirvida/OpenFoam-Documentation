# boundedDdtScheme 
## Class
Foam::fv::boundedDdtScheme

## Description
Bounded form of the selected ddt scheme.

Boundedness is achieved by subtracting ddt(phi)*vf or Sp(ddt(rho), vf)
which is non-conservative if ddt(rho) != 0 but conservative otherwise.

Can be used for the ddt of bounded scalar properties to improve stability
if insufficient convergence of the pressure equation causes temporary
divergence of the flux field.

## SourceFiles
boundedDdtScheme.C

