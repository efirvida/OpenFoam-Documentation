# mappedPatchFieldBase 
## Class
Foam::mappedPatchFieldBase

## Description
Functionality for sampling fields using mappedPatchBase. Every call to
mappedField() returns a sampled field, optionally scaled to maintain an
area-weighted average.

Example usage:

{
        fieldName           T;          // default is same as fvPatchField
        setAverage          false;
        average             1.0;        // only if setAverage=true
        interpolationScheme cellPoint;  // default is cell
}

## SourceFiles
mappedPatchFieldBase.C

