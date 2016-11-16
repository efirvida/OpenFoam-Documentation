# processorCyclicFvPatchField 
## Class
Foam::processorCyclicFvPatchField

## Group
grpCoupledBoundaryConditions

## Description
This boundary condition enables processor communication across cyclic
patches.

## Usage
Example of the boundary condition specification:
```
<patchName>
{
        type            processor;
}
```

## See also
Foam::processorFvPatchField

## SourceFiles
processorCyclicFvPatchField.C
processorCyclicFvPatchFields.H
processorCyclicFvPatchFields.C
processorCyclicFvPatchFieldsFwd.H

