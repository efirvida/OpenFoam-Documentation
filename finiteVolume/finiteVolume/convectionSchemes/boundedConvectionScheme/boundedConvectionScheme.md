# boundedConvectionScheme 
## Class
Foam::fv::boundedConvectionScheme

## Description
Bounded form of the selected convection scheme.

Boundedness is achieved by subtracting div(phi)*vf or Sp(div(phi), vf)
which is non-conservative if div(phi) != 0 but conservative otherwise.

Can be used for convection of bounded scalar properties in steady-state
solvers to improve stability if insufficient convergence of the pressure
equation causes temporary divergence of the flux field.

## SourceFiles
boundedConvectionScheme.C

