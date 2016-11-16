# laplaceFilter 
## Class
Foam::laplaceFilter

## Description
Laplace filter for LES

```
    Kernel                 as filter          as Test filter with ratio 2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Box filter:            g = delta2/24  ->  g = delta2/6
Spherical box filter:  g = delta2/64  ->  g = delta2/16
    Gaussian filter:       g = delta2/24  ->  g = delta2/6
```

## SourceFiles
laplaceFilter.C

