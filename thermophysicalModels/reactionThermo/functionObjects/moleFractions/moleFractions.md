# moleFractions 
## Class
Foam::moleFractions

## Description
This function object calculates mole-fraction fields from the mass-fraction
fields of the psi/rhoReactionThermo and caches them for output and further
post-processing.

The names of the mole-fraction fields are obtained from the corresponding
mass-fraction fields prepended by "X_"

Example of function object specification:
```
moleFractions
{
        type psiReactionThermoMoleFractions;
}
```
or
```
moleFractions
{
        type rhoReactionThermoMoleFractions;
}
```
depending on the thermodynamics package used in the solver.

## See also
Foam::functionObjects::fvMeshFunctionObject

## SourceFiles
moleFractions.C

