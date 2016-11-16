# writer 
## Class
Foam::writer

## Description
Base class for graphics format writing. Entry points are
- write(..). \n
      Write to an Ostream a table of points with corresponding values.
- write(scalar/vector/sphericalTensor/symmTensor/tensor). \n
      Write single scalar/vector/sphericalTensor/symmTensor/tensor.
      Default is to write space separated components.

Example:
```
        // Construct writer of xmgr type
        autoPtr<writer<scalar>> scalarFormatter(writer<scalar>::New("xmgr"));

        // Output list of points and corresponding values
        scalarFormatter().write
        (
            coordSet(...)
            "U.component(0)",   // name of values
            vals                // values
        );
```

## SourceFiles
writer.C

