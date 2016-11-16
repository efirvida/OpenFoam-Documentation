# emptyFvPatchField 
## Class
Foam::emptyFvPatchField

## Group
grpConstraintBoundaryConditions

## Description
This boundary condition provides an 'empty' condition for reduced
dimensions cases, i.e. 1- and 2-D geometries.  Apply this condition to
patches whose normal is aligned to geometric directions that do not
constitue solution directions.

## Usage
Example of the boundary condition specification:
```
<patchName>
{
        type            empty;
}
```

## SourceFiles
emptyFvPatchField.C

