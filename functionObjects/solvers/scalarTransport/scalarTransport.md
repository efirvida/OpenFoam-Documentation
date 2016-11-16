# scalarTransport 
## Class
Foam::functionObjects::scalarTransport

## Group
grpSolversFunctionObjects

## Description
This function object evolves a passive scalar transport equation.

- To specify the field name set the 'field' entry
- To employ the same numerical schemes as another field set
      the 'schemesField' entry,
- The diffusivity can be set manually using the 'D' entry, or retrieved
      from the turbulence model (if applicable).

## See also
Foam::functionObjects::fvMeshFunctionObject

## SourceFiles
scalarTransport.C

