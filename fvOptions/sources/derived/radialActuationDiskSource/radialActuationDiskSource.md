# radialActuationDiskSource 
## Class
Foam::fv::radialActuationDiskSource

## Description
Actuation disk source including radial thrust

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


The thrust is distributed by a radial function:
\f[
        thrust(r) = T (C_0 + C_1 r^2 + C_2 r^4)
\f]

## Usage
Example usage:
```
actuationDiskSourceCoeffs
{
        fieldName       U;          // name of field to apply source
        diskDir         (-1 0 0);   // disk direction
        Cp              0.1;        // power coefficient
        Ct              0.5;        // thrust coefficient
        diskArea        5.0;        // disk area
        coeffs          (0.1 0.5 0.01); // radial distribution coefficients
        upstreamPoint   (0 0 0);    // upstream point
}
```


## SourceFiles
radialActuationDiskSource.C
radialActuationDiskSourceTemplates.C

