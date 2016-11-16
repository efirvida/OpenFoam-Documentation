# actuationDiskSource 
## Class
Foam::fv::actuationDiskSource

## Description
Actuation disk source

Constant values for momentum source for actuation disk
\f[
        T = 2 \rho A U_{o}^2 a (1-a)
\f]
and
\f[
        U_1 = (1 - a)U_{o}
\f]

where:
\vartable
        A   | disk area
        U_o | upstream velocity
        a   | 1 - Cp/Ct
        U_1 | velocity at the disk
\endvartable

## Usage
Example usage:
```
actuationDiskSourceCoeffs
{
        fieldNames      (U);        // names of fields to apply source
        diskDir         (-1 0 0);   // disk direction
        Cp              0.1;        // power coefficient
        Ct              0.5;        // thrust coefficient
        diskArea        5.0;        // disk area
        upstreamPoint   (0 0 0);    // upstream point
}
```


## SourceFiles
actuationDiskSource.C
actuationDiskSourceTemplates.C

